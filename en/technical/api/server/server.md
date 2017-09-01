# Retrieve status information about the server
GET /api/v1/plugin/base/server/status?token=<token>

Retrieves status information about a the server, including information about external components such as EAS and Elasticsearch.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Output

TBD

## Permissions

The user needs the "system.server.error" right (see [rights management](/technical/rightsmanagement/rightsmanagement.md)).

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [No System Right](/technical/errors/errors.md#no_system_right): user lacks the required "system.server.error" right |
| 400 | [Error Not Found](/technical/errors/errors.md#error_not_found): the error `uuid` was not found |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |





# Retrieve detailed information about a server error
GET /api/v1/plugin/base/server/error/<uuid>?token=<token>

Retrieves detailed information about a server error, identified by its <uuid>.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Path parameters

|   |   |
|---|---|
| `uuid` | UUID of the server error (see [server errors](/technical/errors/errors.md#server)) |

## Output

A JSON object containing:

|   |   |
|---|---|
| `code`            | Error code (string), see [server errors](/technical/errors/errors.md#server) |
| `description`     | Error description (string) |
| `timestamp`       | Timestamp (string) |
| `request`         | Information about the request that provoked the error |
| &#8614; `method`  | Request method (string) |
| &#8614; `url`     | Request URL (string): the request URL will use the host provided in the headers, or "localhost" if none was provided |
| &#8614; `body`    | Request body (string) |
| &#8614; `headers` | Request headers (string) |
| `session`         | Information about the session (null, if there was no session) |
| &#8614; `token`   | Session Token (string) |
| &#8614; `created` | Timestamp of session creation (string) |
| &#8614; `user`    | Authenticated user (user in short format): this is only given if the session was successfully authenticated |
| `log`             | Additional information (string): this may be multiline, using the line separator `\n` |

## Permissions

The user needs the "system.server.error" right (see [rights management](/technical/rightsmanagement/rightsmanagement.md)).

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [No System Right](/technical/errors/errors.md#no_system_right): user lacks the required "system.server.error" right |
| 400 | [Error Not Found](/technical/errors/errors.md#error_not_found): the error `uuid` was not found |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |





# Generate an error
POST /api/v1/plugin/base/server/error/<type>?token=<token>

Returns an error of the requested `type`.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Path parameters

|   |   |
|---|---|
| `type` | Type of error to be generated (string): **user**, **server** or **api** |

## Permissions

The user needs the "system.root" right (see [rights management](/technical/rightsmanagement/rightsmanagement.md)).

## HTTP status codes

Notice that this call never returns 200. The requested errors are:

- API error: error.api.type_mismatch
- User error: error.user.user_not_found
- Server error: error.server.generic

|   |   |
|---|---|
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed, or the requested API error |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [No System Right](/technical/errors/errors.md#no_system_right): user lacks the required "system.root" right |
| 400 | [User Not Found](/technical/errors/errors.md#user_not_found): the requested user error |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error, or the requested server error |
