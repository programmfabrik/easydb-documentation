---
title: "62 - export"
menu:
  main:
    name: "export"
    identifier: "technical/api/export"
    parent: "technical/api"
---
# Get exports

    GET /api/v1/export?token=<token>

Retrieves an overview of all exports owned by the user.

## Query String

|   |   |
|---|---|
| `token`    | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `limit`    | maximum number of returned exports (optional, integer, `1000` if unset, maximum: `1000`) |
| `offset`   | offset of first export to be returned (optional, integer, `0` if unset) |
| `filter`   | Comma-separated, disjunctive list of multiple filters. Each filter may contain a `type` and/or a `status` filter part, multiple parts are separated by `+` and used in conjunction. Each parts consists of the filter variable name (either `type` or `status`) and its value(s), separated by `:`. Multiple values may be specified, separated by `|`. Example: `filter=type:download|export+status:failed,type:export_incremental`. Note, that `+` has to be URL-encoded (`%2B`) when used in query string. |

## Output

Object containing the following fields:

| Name         | Description  |
|--------------|--------------|
| `limit`      | requested maximum number of returned exports, `null` if not requested in URL |
| `offset`     | offset of first export to be returned, `0` if not requested in URL |
| `count`      | total number of exports found, ignoring `limit` |
| `objects`    | array of [exports](/en/technical/types/export). The exports do not include `_files`, `_downloads`, `_schedules` `_transports` and `_log`. |

## Permissions

The session must be authenticated. A user can only manage its own exports.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 500 | [Server error](/en/technical/errors): internal server error |





    GET /api/v1/export/<export-id>?token=<token>

Retrieves a specific export.

## Path parameters

|   |   |
|---|---|
| `export-id` | Export ID (integer) |

## Query String

|   |   |
|---|---|
| `token`    | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Output

An [export](/en/technical/types/export).

## Permissions

The session must be authenticated. A user can only manage its own exports.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 404 | [Not Found](/en/technical/errors): export `export_id` not found |
| 500 | [Server error](/en/technical/errors): internal server error |





# Create an export

    PUT /api/v1/export?token=<token>

Create a new export.

*TODO*: a secret passkey to access an Export's downloadable files, is generated and stored for the new Export.

## Query String

|   |   |
|---|---|
| `token`    | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Input

An [export](/en/technical/types/export).

## Output

The created [export](/en/technical/types/export).

## Permissions

The session must be authenticated.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 500 | [Server error](/en/technical/errors): internal server error |




# Update an export

    POST /api/v1/export/<export-id>?token=<token>

Update an export. POST only updates fields that are set, leaving the rest as they currently are.

*TODO*: if an update happens to an Export which is not in *done* or *new* state, the currently active Export is purged. After an update the Export gets again the *new* state.

## Path parameters

|   |   |
|---|---|
| `export-id` | Export ID (integer) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Input

An [export](/en/technical/types/export).

If the export is scheduled (there are one or more `_schedules`), it requires an explicitly set `name`.

## Output

The updated [export](/en/technical/types/export).

## Permissions

The session must be authenticated. A user can only manage its own exports.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Export Name Required](/en/technical/errors): export requires a name |
| 404 | [Not Found](/en/technical/errors): export `export_id` not found |
| 500 | [Server error](/en/technical/errors): internal server error |





# Delete an export

    DELETE /api/v1/export/<export-id>?token=<token>

Delete export `export-id`.

## Path parameters

|   |   |
|---|---|
| `export-id` | Export ID (integer) |

## Query String

|   |   |
|---|---|
| `token`    | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Permissions

The session must be authenticated. A user can only manage its own exports.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 404 | [Not Found](/en/technical/errors): export `export_id` not found |
| 500 | [Server error](/en/technical/errors): internal server error |



# Get files from an Export

    GET /api/v1/v1/export/<export-id>/file/<path>?token=<token>

The *\<path\>* can be retrieved from the *\_files* Array returned in the Export. Clients can use this to build an Export browser. *\<path\>* needs to be a file.

## Query String

|   |   |
|---|---|
| `token`        | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `disposition`  | If set, a *Content-Disposition* header is set in response. Valid values: *inline*, *attachment* |
| `filename`     | If set, an alternative name for the downloaded file is used. The file extension is added automatically. |

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 302 | Client is redirected to show an error page (using scheme `/#server_error:<localization key>`. This is only done if `disposition` parameter is set. |
| 400 | [API error](/en/technical/errors): something is malformed |

# Get files zipped from an Export

    GET /api/v1/v1/export/<export-id>/zip/<path>?token=<token>

The *\<path\>* can be retrieved from the *\_files* Array returned in the Export. The ZIP format is ZIP64, if ZIP32 is required a transport has to be used. Single files or directories can be zipped. With no path given, the full export is zipped.

> The server generates the ZIP file on-thy-fly, so there is no Content-Length HTTP-Header set in the response.

|   |   |
|---|---|
| `token`        | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `disposition`  | If set, a *Content-Disposition* header is set in response. Valid values: *inline*, *attachment* |
| `filename`     | If set, an alternative name for the downloaded ZIP file is used. Defaults to export name and (if a path other than "/" is provided) the leaf path name with a ".zip" suffix. The file extension (always ".zip") is added automatically. |

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 302 | Client is redirected to show an error page (using scheme `/#server_error:<localization key>`. This is only done if `disposition` parameter is set. |
| 400 | [API error](/en/technical/errors): something is malformed |

# Download files from an Export

> Each export generates a list of files to download the Export from. The *ZIP* files and *TAR* file is available through an anonymous access using a secret-passkey which is uniquely generated for each Export upon PUT.

## Get a downloadable files from an Export

    GET /api/v1/v1/export/<export-id>/download/<secret-passkey>/<name-of-export>[.<1-n>].zip>
    GET /api/v1/v1/export/<export-id>/download/<secret-passkey>/<name-of-export>.zip>
    GET /api/v1/v1/export/<export-id>/download/<secret-passkey>/<name-of-export>.tar>

The URL can be retrieved from the *\_download* Map returned in the Exports Transports List.

Only Exports in the *done* state can be downloaded.

The URL can be retrieved from the *\_download* Map returned in the Exports Transports List.

> The URL for a downloadable file will be persistent over the lifetime of an export.

|   |   |
|---|---|
| `token`        | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `disposition`  | If set, a *Content-Disposition* header is set in response. Valid values: *inline*, *attachment* |
| `filename`     | If set, an alternative name for the downloaded file is used. The file extension is added automatically. |

## Get with an invalid secret-passkey

If the secret-passkey used is invalid, the server uses a response with a "HTTP Location" redirect to redirect the Requester to a Frontend-URL to display a server error.

> //#server_error:export.invalid.passkey

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 302 | Client is redirected to show an error page (using scheme `/#server_error:<localization key>`. This is only done if `disposition` parameter is set. |
| 400 | [API error](/en/technical/errors): something is malformed |

# Start an export

The export is queued to run immediately.

	POST /api/v1/export/<export-id>/start?token=<token>

## Path parameters

|   |   |
|---|---|
| `export-id` | Export ID (integer) |

## Query String

|   |   |
|---|---|
| `token`    | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Permissions

The session must be authenticated. A user can only manage its own exports.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Already Running](/en/technical/errors): the export requested to start is already running |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 404 | [Not Found](/en/technical/errors): export `export_id` not found |
| 500 | [Server error](/en/technical/errors): internal server error |

# Stop an export

	POST /api/v1/export/<export-id>/stop?token=<token>

## Path parameters

|   |   |
|---|---|
| `export-id` | Export ID (integer) |

## Query String

|   |   |
|---|---|
| `token`    | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Permissions

The session must be authenticated. A user can only manage its own exports.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 404 | [Not Found](/en/technical/errors): export `export_id` not found or not running |
| 500 | [Server error](/en/technical/errors): internal server error |
