---
title: "83 - user"
menu:
  main:
    name: "user"
    identifier: "technical/api/user"
    parent: "technical/api"
---
# Retrieve users
    GET /api/v1/user[/<id>]?token=<token>[&limit=<limit>][&offset=<offset>][&groupids=<groupids>][&type=<type>][&changed_since=<changed_since>]

Retrieves one user.

## Path parameters

|   |   |
|---|---|
| `id`            | User ID (integer, optional): get user `id`. If `id` is omitted, all users (filtered by rights management) are returned. |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `limit` | Return no more than <limit> users.  Default: `1000` |
| `offset` | Skip first <offset> users.  Default: `0` |
| `groupids` | Return users belonging to at least one of the groups with ID <groupids>.  Format: `groupid1,groupid2,...` |
| `type` | Filter users by type. |
| `changed_since` | Filter users with date of update greater or equal than <changed_since>. Format: `<YYYY-MM-DD>[THH:MM][:SS][T(+|-)HH:MM]` Ex: `2017-06-05`, `2017-06-05T19:30`, `2017-06-05T19:30-03:00` |

## Returns

Array of [users](/en/technical/types/user). The field `password` will **not** be returned.

Depending on the rights of the user, some fields may not be visible. See "Permissions".

## Permissions

The session must be authenticated.

The session user requires the `system.user` right and `read` for the user.

Additionally, a user can read some information about itself (session user is the same as requested user), even if it does not have the `write` right:

- all "short" format fields
- `frontend_prefs`
- any fields that are checked in the `system.user.write_self`

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [No System Right](/en/technical/errors): no `system.user` right |
| 400 | [User Not Found](/en/technical/errors): user `id` not found |
| 400 | [Insufficient Rights](/en/technical/errors): no `read` right |
| 500 | [Server error](/en/technical/errors): internal server error |

## Examples


{{< include_json "./get_id.json" >}}






# Insert or update users
    POST/PUT /api/v1/user?token=<token>

Creates (PUT) or updates (POST) users. The related "user collection" will be created or updated (if required).

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Input

Array of [users](/en/technical/types/user). Depending on the user rights, more or less information is available: see GET above.

## Ouput

Array of [users](/en/technical/types/user) that were updated.

## New primary e-mail

If the request includes a `_new_primary_email` it will be processed as follows:

- if the e-mail address exists
    - if it is already primary, an error is returned
    - if it is not primary but it is not confirmed, mark it as intended primary and resend the confirmation e-mail
    - if it is not primary and it is confirmed, it will become primary
- if the e-mail address does not exist, create it and mark it to become primary when it is confirmed
    - if there is already a pending confirmation for a different address, delete it

The e-mail address remains as `_new_primary_email` until it is confirmed.

## Email sending

Inserting or updating users might trigger sending of emails to one or more of the user's email addresses. Each email contains different parts:

| name              | l10n key | description  |
|---                |---       |---           |
|subject            | `email.usermanagement.block.subject`    | Subject of email, identical for all types of emails |
|header             | `email.usermanagement.block.header`     | Common text at the beginning of the email body |
|*email part*       | `email.usermanagement.block.email.*`    | Information regarding email address |
|*password part*    | `email.usermanagement.block.password.*` | Information regarding password |
|footer             | `email.usermanagement.block.footer`     | Common text at the end of the email body |

For the *email part* and the *password part* there is at most one part each, it may also be missing completely. If neither an *email part* or a *password part* is given, no email is sent at all.

When `sent_email` of the email address is not set to `true`, no email is sent to this address, either.

### *email part*

The first part which meets all conditions is used:

| name              | l10n key | conditions   | description  |
|---                |---       |---           |---           |
| confirm address   | `email.usermanagement.block.email.confirm` | `needs_confirmation` is set to `true` | email part requests user to confirm the email address, `confirm_url` is replaced in l10n key. This URL contains an authentication token and the email address to be confirmed: `<proto>://<base-url>/#confirm_email:<token>:<email>`. The email part is URL-encoded. This data can be used to confirm the email using the [`/session/confirm_email`](/en/technical/api/session) API call. |
| info new address  | `email.usermanagement.block.email.new_email` | email address is newly created | information about  email address is included, `use_for_login` and `use_for_email` are replaced using localized values of `yes` and `no` |
| info updated address  | `email.usermanagement.block.email.update_email` | email address is updated | information about  email address is included, `use_for_login` and `use_for_email` are replaced using localized values of `yes` and `no` |

#### *cancel a requested confirmation of an email address*

When a confirmation request has been sent, the confirmation request can be cancelled by sending the write-only parameter `"cancel_confirmation": true`.

This also overrules the write-only parameter `needs_confirmation`.

### *password part*

The first part which meets all conditions is used:

| name              | l10n key | conditions   | description  |
|---                |---       |---           |---           |
| forgot password   | `email.usermanagement.block.password.forgot_password` | `/api/v1/session/forgot_password` called; email address doesn't need to get confirmed | not possible using `/api/v1/user`, just for reference |
| change password   | `email.usermanagement.block.password.change_password` | `set_change_password` set to `true` (either request or database) and active password present | user is requested to change password, `set_password_url` is replaced in l10n key |
| set password   | `email.usermanagement.block.password.set_password` | `set_change_password` set to `true` (either request or database) and no active password present | user is requested to change password, `set_password_url` is replaced in l10n key |
| password in email | `email.usermanagement.block.password.password_is` | `send_email_include_password` is true and `_password` is either `true` or a new password | inform user about the new password, `password` is replaced in l10n key |
| password set, call admin | `email.usermanagement.block.password.call_admin` | `_password` set in request | inform user about a password change, user has receive to new password by other means |

## Permissions

The session must be authenticated.

### Updating a user

If the session user has the `write` right for the user, the user is editable.

In the case that the user groups are provided (`_groups`), notice that:

- if a group is added, the user requires the `link` right for the group
- if a group is deleted, the user requires the `unlink` right for the group
- system groups cannot be added or deleted, they are automatically set for the session

Additionally, a user can edit some information about itself (session user is the same as requested user), even if it does not have the `write` right:

- `frontend_prefs`
- `language`
- any fields that are checked in the `system.user.write_self`

If the user is a system user (type "system"), the following parameters cannot be modified:

- `login`
- `_acl`
- `_system_rights`.
- `_groups`.

Any attempt to modify one of them will result in a User Update System Group error.

A user cannot disable its own login (i.e. set `login_disabled` to **true**).

### Creating a user

If a user is created, the session user requires the `system.user` right with `create`. This right implies the `write` right and
the rules for update apply. This means, for example, that if the user is linked to a group, the `link` right for the group must
exist for the user.

When creating a user, the owner will be set to the session user. An attempt to set a different owner will trigger a Change Owner On Creation error.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Bad Password](/en/technical/errors): new password is not valid due to policy |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "write", "link" or "unlink" right (the error tells which) |
| 400 | [No System Right](/en/technical/errors): user lacks the required system right to create/update a user (the error tells which) |
| 400 | [Change Owner On Creation](/en/technical/errors): the user attempted to set a different owner than him-/herself when creating a user |
| 400 | [Invalid Password](/en/technical/errors): invalid password |
| 400 | [User Update System Group](/en/technical/errors): the user attempted to put the user in a system group |
| 400 | [Update System User](/en/technical/errors): the user attempted to update a system user's property that is now allowed to change (the error parameters tell which one) |
| 400 | [User Not Found](/en/technical/errors): user not foudn (`user._id`, or in `_acl.who` or `_owner.who`) |
| 400 | [Group Not Found](/en/technical/errors): group not found (in `_acl.who`, `_owner.who` or `_groups`) |
| 400 | [Right Not Found](/en/technical/errors): a right that was provided for `_acl` or `_system_rights` was not found |
| 400 | [Invalid User Type Change](/en/technical/errors): invalid user change: see [user](/en/technical/types/user) |
| 400 | [Email Already Exists](/en/technical/errors): the provided e-mail already exists in the system |
| 400 | [Primary Check Number](/en/technical/errors): the user has provided more than one primary e-mail addresses |
| 400 | [Primary Check Active](/en/technical/errors): the user is trying to set an inactive e-mail to be primary |
| 400 | [Intended Primary Check Number](/en/technical/errors): the user has provided more than one intended primary e-mail addresses |
| 400 | [Intended Primary Check Requested](/en/technical/errors): the user is trying to set an e-mail to be intended primary without requesting confirmation |
| 400 | [User Auto Disable](/en/technical/errors): the user is trying to set `login_disabled` to **true** for its own user record |
| 400 | [Register User Login Or Email Required](/en/technical/errors): attempting to register as new user without login nor e-mail address |
| 400 | [Custom Type Required](/en/technical/errors): attempting to assign the "system.user.create_new" right with type "custom" but without specifying the "custom_type" |
| 400 | [Group Required](/en/technical/errors): attempting to create a user without group when "require_group" was set |
| 400 | [Login Change Not Allowed For Email User](/en/technical/errors): attempting to change the login of an "email" user |
| 500 | [Server error](/en/technical/errors): internal server error |

## Examples


{{< include_json "./put.json" >}}



{{< include_json "./post.json" >}}






# Delete user
    DELETE /api/v1/user/<id>?token=<token>

Delete a user. The user is *archived* if there has been activity, otherwise deleted.

The user collection is also deleted, along with its subtree.

## Path parameters

|   |   |
|---|---|
| `id`            | Object ID (integer) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Permissions

The session must be authenticated and have the `delete` right for the user provided.

System users are not allowed to be deleted.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "delete" right |
| 400 | [User Not Found](/en/technical/errors): user `id` not found |
| 400 | [Delete System User](/en/technical/errors): the user attempted to delete a system user |

## Examples

```javascript
Request:  DELETE /api/v1/user/2
Response: HTTP 200
```
