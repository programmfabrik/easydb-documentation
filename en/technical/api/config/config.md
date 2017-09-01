# Get config

GET /api/v1/config?token=<token>

Outputs the current config as visible to the current session.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Authentication

This call requires the system right `system.config`.

## Output

~~~~json
@@include: config.output.json @@
~~~~

|   |   |
|---|---|
| 200 | Success |
| 403 | Unauthorized session |





# Save config

POST /api/v1/config?token=<token>

Use this call to update and insert config information.

Currently all keys need to be send at once per class. All not-sent keys
in the same class will be removed.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Authentication

This call requires the system right `system.config`.

## Input

~~~~json
@@include: config.input.json @@
~~~~

## Output

This call redirects to the given urls depending on the succes or failure
of the login attempt.

|   |   |
|---|---|
| 200 | Success |
| 400 | Bad Request. Something is malformed |
| 403 | Unauthorized session |





# Get configuration options

GET /api/v1/config/list?token=<token>

Outputs the available config options.

|  |                    |
|-----|--------------------|
| `token` |   The session token.		 |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Output

~~~~json
@@include: config.list.json @@
~~~~

# Config Variables

|Name					|Format/Parameters		| Description					|
|-----------------------|-----------------------|-------------------------------|
|`system.name`			| string `^[a-zA-Z][a-zA-Z0-9_-.]{5,31}$` | Name of the easydb. This name is used as a reference in filenames, emails, domain names.|
|`system.displayname`	| l10n-string			| Name of the easydb to display. |
|`system.logo`			| eas-id				| Base logo of this easydb. Use /api/v1/eas to get an EAS-ID.  |
|`system.administrator.emails`| multi-line string | Email-Addresses of system administrators. easydb uses this to send system related emails. There can be one email on each line.|
|`system.intranet.nets`		   | multi-line string, one network per line | Newline separated list of networks which will be considered *intranet*.|
|`system.languages`   		   | list of languages for frontend and database. | Ordered list of user available frontend languages and languages for db-l10n-fields. |
|`system.upload`   	   		   | list of fileclasses, extensions, upload limits. | This list is the global limit.  |
@@include: config.loginmanagement.md@@
