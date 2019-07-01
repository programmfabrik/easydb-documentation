---
title: "72 - schema"
menu:
  main:
    name: "schema"
    identifier: "technical/api/schema"
    parent: "technical/api"
---
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
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `format`| The format the definition will be output in (optional): see below |

Available formats:

- `xml`: database schema as XML document (this is the default format)
- `json`: database schema as JSON object
- `svg`: graphical representation of the database schema as SVG
- `png`: graphical representation of the database schema as PNG

## <a name="schema"></a>Output

If the format is `xml`or `json`, this call returns a [schema](/en/technical/types/schema).
If the format is `svg` or `png`, this call returns a file.

## Permissions

This call requires an authenticated session. Frontends can use the "system.datamodel.current" right to decide
if they show the schema to the user.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 404 | [Not Found](/en/technical/errors): the requested schema version was not found |
| 500 | [Server error](/en/technical/errors): internal server error |





# Update database schema

    POST /api/v1/schema/user/HEAD?token=<token>

Update the HEAD version of the user database schema.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Input

New [schema](/en/technical/types/schema) as JSON.

## Output

The new [schema](/en/technical/types/schema). Notice that several changes will be present in the output, such
as auto-generated IDs.

## Permissions

The user needs the "system.datamodel.development" right.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 403 | [No System Right](/en/technical/errors): user lacks the required "system.datamodel.development" right |
| 500 | [Server error](/en/technical/errors): internal server error |





# Commit database schema

    POST /api/v1/schema/commit?token=<token>

Commit the HEAD schema version and make it the current version. This
call changes the database according to the new schema. It adds, changes
and drops tables, columns.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `reindex_generate_events` | If set to `1`, reindex jobs created after schema changes will generate `OBJECT_INDEX` events. Defaults to not generate events. |

## Permissions

The user needs the "system.datamodel.commit" right.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 403 | [No System Right](/en/technical/errors): user lacks the required "system.datamodel.commit" right |
| 500 | [Server error](/en/technical/errors): internal server error |
