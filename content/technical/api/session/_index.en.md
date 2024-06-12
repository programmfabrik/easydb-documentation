---
title: "75 - session"
menu:
  main:
    name: "session"
    identifier: "technical/api/session"
    parent: "technical/api"
---
# Start a session

    GET /api/v1/session[?language=<language>]

This call starts a new session. The new session will be unauthorized and will contain the required
parameters needed to authorize it:

- a token, and
- the allowed authentication_methods

## Query String

|   |   |
|---|---|
| `language` | Session language (string, optional) |

## Output

An unauthorized [session](/en/technical/types/session).

## Permissions

This call does not require any permission.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Language Not Found](/en/technical/errors): the user provided a `language` that does not exist |
| 500 | [Server error](/en/technical/errors): internal server error |





# Retrieve current session

    GET /api/v1/session?token=<token>[&language=<language>]

It returns the session object associated with this `token`. This call also lets the frontend update the session language.

## Query String

|   |   |
|---|---|
| `token`    | Session token (string) |
| `language` | Session language (string, optional) |

## Output

The current [session](/en/technical/types/session).

## Permissions

This call does not require any permission.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Session Not Found](/en/technical/errors): session not found for the given `token` |
| 500 | [Server error](/en/technical/errors): internal server error |


# Authenticate a session {#authenticate-a-session}

    POST /api/v1/session/authenticate?token=<token>[&method=<method>][&login=<login>&password=<password>][&success=<success>][&error=<error>][&response_type=<response_type>][&remember_me={1|0}][&log_event={1|0}]

Authenticate a session using the provided user credentials.

The authentication methods are tested in the given order until one of them succeeds, in which case the session will be authenticated
and will provide which method was used; or until all fail, in which case, the request will redirect to the error URL.

The supported authentication methods are:

- "easydb" (default): authenticate easydb user
    - `login` can be either the user login, if it is not **null** or a user e-mail address, if it is marked as `use_for_login`
    - `password` is the user password
- "task": authenticate easydb to perform a task - this method is called during the "forgot password" and "confirm e-mail" processes
    - `login` is an e-mail address
    - `password` is an authentication token for the process
- "easydb_cookie": authenticate easydb user using a cookie
- "anonymous": a virtual user will be created
- "email": authenticate an easydb user of type "email" using its email as login and a collection UUID as password
- "collection": authenticate an easydb user of type "collection" using the collection UUID as login and the collection secret as password

The method task is only supported if it is given as sole method (not in combination with others). This method does not support `success`, `error`,
`response_type` or `remember_me`. It always returns a session with pending tasks.

When the system detects a series of failed login attempts, it will block the user for a certain time.
The amount of attempts and the duration of the block can be configured in the base configuration.

## Query String

|   |   |
|---|---|
| `token`         | Session token (string) |
| `method`        | Authentication method(s) (string): comma-separated list of authentication methods |
| `login`         | Login (string): mandatory except for **anonymous** and **easydb_cookie** |
| `password`      | Password (string): mandatory except for **anonymous** and **easydb_cookie** |
| `response_type` | Response type (see "Output"): **redirect** (default) or **javascript** |
| `success`       | URL to redirect / function to be called in case of success (string, optional) |
| `error`         | URL to redirect / function to be called in case of authentication error (string, optional) |
| `remember_me`   | If set to `"1"`, remember user using a cookie (only for method "easydb", optional, defaults to `"0"`) |
| `log_event`   | If set to `"0"`, for the authentication no **USER_LOGIN** event is logged, optional, defaults to `"1"`) |

All query parameter can also be sent in an HTML form in the request body (content type `application/x-www-form-urlencoded`)

### Authenticating any user account with a root account

To login into any user account without knowledge of the users password, provide the `password` in the form `<root login>/<root password>`.

- `<root login>`: Login of the Root account `root` or any user account that has the system right `root`
- `<root password>`: Password of the Root account

Example: to login as the user `user01` without knowing the actual user password, provide `?login=user01&password=root/admin` as URL parameters, where `root` and `admin` are the login credentials of an account with root rights.

## Output

The output depends on the `response_type`.

### Response type "redirect"

If the response is successful and `success` was given, a HTTP 302 response (redirect) is returned with the "Location" header
pointing to the given URL. If no `success` was given, the [session](/en/technical/types/session) is returned.

If the response is not successful and `error` was given, a HTTP 302 response (redirect) is returned with the "Location" header
pointing to the given URL, extended with a fragment identifier: `<error>#m:<reason>#l:<login>`. If no `error` was given, an
appropriate error response is returned.

### Response type "javascript"

For this response type, `success` and `error` must be given. They contain the name of a function that should be called on success
or error, respectively. A HTML page is returned with a simple script that calls the corresponding function with the session or
error response as argument. The HTTP status code will be 200 or 403 depending on the success of the authentication.

### Method "task"

This method returns a session with pending tasks to guide the client through a process ("forgot_password" or "confirm_email").

## Permissions

The authentication method "anonymous" is allowed

- if the configuration variable `login_intranet` is set to **true** and the user comes from an intranet address, or
- if the configuration variable `login_internet` is set to **true** and the user comes from an internet address

The other authentication methods are always allowed. However, the authentication itself may fail:

- The authentication method "easydb" will fail if the user flag `login_disabled` is set. This can be used by the administrator to block users
- The authentication method "easydb" may fail due to wrong credentials
- The authentication methods "email" and "collection" may fail due to wrong credentials or because the sharing has stopped. If the latter case, a message explains what happened

## HTTP status codes

If an error is redirected (302), the <reason> for the fragment identifier will be the one indicated in the column "reason".
Notice that only known user errors are redirected.

|   |   | reason |
|---|---|--------|
| 200 | Success (the body may be JSON or HTML, depending on the `response_type`) | |
| 302 | See "Output" | |
| 400 | [API error](/en/technical/errors): something is malformed | |
| 400 | [Session Not Found](/en/technical/errors): session not found for the given `token` | session_missing |
| 400 | [Username or Password Empty](/en/technical/errors): username or password empty | username_or_password_empty |
| 400 | [Login Failed](/en/technical/errors): login failed | login_failed |
| 400 | [Login Disabled](/en/technical/errors): login disabled | login_disabled |
| 400 | [Login Disabled From](/en/technical/errors): login disabled from a timestamp on | login_disabled |
| 400 | [Login Disabled To](/en/technical/errors): login disabled until a timestamp | login_disabled |
| 400 | [Login Blocked](/en/technical/errors): login blocked | login_blocked |
| 400 | [Authentication Method Not Allowed](/en/technical/errors): authentication method not allowed | |
| 400 | [Collection Sharing Inactive](/en/technical/errors): Collection sharing has been deactivated (for "email" or "collection") | |
| 400 | [Collection Sharing Too Soon](/en/technical/errors): Collection sharing is not valid yet (for "email" or "collection") | |
| 400 | [Collection Sharing Too Late](/en/technical/errors): Collection sharing is no longer valid (for "email" or "collection") | |
| 400 | [Authentication Token Expired](/en/technical/errors): The authentication token used as `password` has expired ([1](#note1)) | |
| 400 | [Authentication Token Used](/en/technical/errors): The authentication token used as `password` has already been used ([1](#note1)) | |
| 403 | Login failed and `response_type` javascript; the body will be HTML | |
| 403 | Login disabled and `response_type` javascript; the body will be HTML | |
| 500 | [Server error](/en/technical/errors): internal server error | |

<a name="note1">1</a>: the authentication token is only used in the password reset process and should not be confused with the session token.

# Authenticate a session using single-sign-on

    GET /api/v1/session/sso/authenticate

This authentication method is only allowed if some plugin has registered an "sso_get_user" callback.

The user is authenticated using the underlying authentication method (this is configured as part of the Apache configuration).

The plugin is responsible for generating a partial user record. The server will create the user if it does not exist (based on
the user login).

If this user record contains an array of strings under "_groups", the server will try to map them to actual groups and link the
user to them. The mapping is based on the configuration of the [group](/en/technical/types/group): field `_auth_method_group_maps`. The
methods are processed in order:

- "eq" means that the name provided by the plugin must match the value
- "regexp" means that the name provided by the plugin must match the regexp described by the value

## Query String

|   |   |
|---|---|
| `token`         | Session token (string) |
| `success`       | Function to be called in case of success (string, optional) |
| `error`         | Function to be called in case of authentication error (string, optional) |

## Output

An authenticated [session](/en/technical/types/session). If `success` is set, a HTML page is returned with a
simple script that calls the corresponding function with the session as argument.

## HTTP status codes

If `error` is set, a HTML page is returned with a simple script that calls the corresponding function with the error as argument.

|   |   |
|---|---|
| 200 | Success |
| 500 | [Server error](/en/technical/errors): internal server error |





# Deauthenticate a session

    POST /api/v1/session/deauthenticate?token=<token>[&error=<error>]

Deauthenticate a session. If the session was not authenticated, this call does nothing.

## Query String

|   |   |
|---|---|
| `token` | Session token (string) |
| `error` | URL to redirect in case of authentication error (string, optional) |

## Output

An unauthenticated [session](/en/technical/types/session).

## Permissions

This call does not require any permission.

## HTTP status codes

If an error occurs and `error` is set, the response will be a redirection. See previous call for details.

|   |   | reason |
|---|---|--------|
| 200 | Success | |
| 302 | See "Output" | |
| 400 | [API error](/en/technical/errors): something is malformed | |
| 400 | [Session Not Found](/en/technical/errors): session not found for the given `token` | session_missing |
| 500 | [Server error](/en/technical/errors): internal server error | |





# Confirm messages for a session

    POST /api/v1/session/messages_confirm?token=<token>

## Query String

|   |   |
|---|---|
| `token`         | Session token (string) |

## Input

A JSON array of confirmation keys (string). The keys are included in the session's `pending_tasks`.

## Output

The current [session](/en/technical/types/session).

## Permissions

The session must be authenticated.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 500 | [Server error](/en/technical/errors): internal server error |




# Change password

    POST /api/v1/session/change_password?token=<token>

## Query String

|   |   |
|---|---|
| `token` | Session token (string) |

## Input

A JSON object containing the keys:

- `password`: the current password (string)
- `new_password`: the new password (string)

## Permissions

The user needs the `system.user.change_password` or be required to change its password via `set_change_password` (see [user](/en/technical/types/user)).

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Invalid Password](/en/technical/errors): the provided `password` is wrong |
| 400 | [Bad Password](/en/technical/errors): the `new_password` violates the password policy |
| 400 | [Same Password](/en/technical/errors): the `new_password` is the same as the old password |
| 400 | [No System Right](/en/technical/errors): user lacks `system.user.change_password` |
| 500 | [Server error](/en/technical/errors): internal server error |





# Set password

    POST /api/v1/session/set_password?token=<token>[&email=<email>&code=<code>]

This call can be used to set the user's password. It can be called directly using an authenticated session
or as part of the "forgot password" process with an email and code as authentication method.

## Query String

|   |   |
|---|---|
| `token` | Session token (string) |
| `email` | E-mail address (string, optional) |
| `code`  | Authentication code (string, optional) |

## Input

A JSON object containing the keys:

- `new_password`: the new password (string)

## Output

The current [session](/en/technical/types/session).

## Permissions

If the session is authenticated, the user needs the `system.user.change_password` or be required to change its password
via `set_change_password` (see [user](/en/technical/types/user)).

If the session is not authenticated, `email` and `code` are mandatory. These are the parameters sent to the user's e-mail
address as part of the "forgot password" process. If the call uses the parameters AND is authenticated, it will only work
if the authenticated user is the same as the user identified by the `email` address.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Invalid Password](/en/technical/errors): the provided `password` is wrong |
| 400 | [Bad Password](/en/technical/errors): the `new_password` violates the password policy |
| 400 | [Same Password](/en/technical/errors): the `new_password` is the same as the old password |
| 400 | [Login Failed](/en/technical/errors): authentication via `email` and `code` failed |
| 400 | [Authentication Token Expired](/en/technical/errors): the `code` has expired |
| 400 | [Authentication Token Used](/en/technical/errors): the `code` has already been used |
| 400 | [No System Right](/en/technical/errors): user lacks `system.user.change_password` |
| 500 | [Server error](/en/technical/errors): internal server error |





# Forgot password

    POST /api/v1/session/forgot_password

## Query String

|   |   |
|---|---|
| `token` | Session token (string, optional) |

## Input

A JSON object with the key:

- `forgot`: either a login name or an e-mail address (string)

On success, an e-mail is sent out to the user identified by `forgot` containing a link to set a new password. If a primary e-mail is found, the link to reset the password is sent to this e-mail address.

If the confirmation of this e-mail address was requested, but the user has not yet confirmed it, the confirmation request will be resent to the user.

## Permissions

This call does not require any permission.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [User error](/en/technical/errors) `error.user.forgotten_password_process_disabled`: the forgot password process has been disabled |
| 400 | [User error](/en/technical/errors) `error.user.forgot_password.unknown`: the user specified in `forgot` could not be identified |
| 500 | [Server error](/en/technical/errors): internal server error |

# Base configuration entries

(`l10n-base-config.csv`)

email sending keys are shared with [POST /api/v1/user](/en/technical/api/user):

| l10n key | description |
|---       |---          |
|`email.usermanagement.block.subject`    | subject of mail to send |
|`email.usermanagement.block.header`     | header of email body    |
|`email.usermanagement.block.password.forgot_password` | body of mail to send, if process was success    |
|`email.usermanagement.block.email.confirm`            | body of mail to send, if email address needs to get confirmed |
|`email.usermanagement.block.footer`     | footer of email body    |

within the email templates the following keys are replaced (using the `%(key)s` syntax):

| key | description |
|---  |---          |
| `displayname` | name of recipient             |
| `token`       | one-time authentication token |
| `url`         | URL to easydb frontend        |
