# Retrieve database schema

    GET /api/v1/schema/user/{[1-n]|HEAD|CURRENT}?token=<token>[&format=<format>]

Retrieve the user database schema for a specific version. When easydb is first started, this call will return *404 Not found* for any version.
The first user update will be the version 1. CURRENT points to the database version currently used and HEAD points to the version currently
updated (but not yet commited).

## Path parameters

|   |   |
|---|---|
| `version` | Can be directly specified, as a number, or through the pointers "HEAD" or "CURRENT" |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |
| `format`| The format the definition will be output in (optional): see below |

Available formats:

- `xml`: database schema as XML document (this is the default format)
- `json`: database schema as JSON object
- `svg`: graphical representation of the database schema as SVG
- `png`: graphical representation of the database schema as PNG

## <a name="schema"></a>Output

If the format is `xml`or `json`, this call returns a [schema](/technical/types/schema/schema.md).
If the format is `svg` or `png`, this call returns a file.

## Permissions

This call requires an authenticated session. Frontends can use the "system.datamodel.current" right to decide
if they show the schema to the user.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 403 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 404 | [Not Found](/technical/errors/errors.md#not_found): the requested schema version was not found |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |





# Update database schema

    POST /api/v1/schema/user/HEAD?token=<token>

Update the HEAD version of the user database schema.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Input

New [schema](/technical/types/schema/schema.md) as JSON.

## Output

The new [schema](/technical/types/schema/schema.md). Notice that several changes will be present in the output, such
as auto-generated IDs.

## Permissions

The user needs the "system.datamodel.development" right.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 403 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 403 | [No System Right](/technical/errors/errors.md#no_system_right): user lacks the required "system.datamodel.development" right |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |





# Commit database schema

    POST /api/v1/schema/commit?token=<token>

Commit the HEAD schema version and make it the current version. This
call changes the database according to the new schema. It adds, changes
and drops tables, columns.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Permissions

The user needs the "system.datamodel.commit" right.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 403 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 403 | [No System Right](/technical/errors/errors.md#no_system_right): user lacks the required "system.datamodel.commit" right |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |
