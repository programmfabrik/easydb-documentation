# Retrieve the list of rights

    GET /api/v1/right[/<context>]?token=<token>

Returns a list of available system rights. Rights are grouped by the context they
may be used in. Optionally, the list can be filtered by context.

## Path parameters

|   |   |
|---|---|
| `context`       | Right context |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Output

The output is a JSON object with an attribute for each context, which contains the following attributes:

| Name           | Description                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------|
| `capabilities` | Features supported in this context. Each feature is a key in the capabilities map (see below)             |
| `presets`      | If the `capabilities` include "preset", this attributes shows a list of the right presets for this context (output of GET /api/v1/right/<context>/presets) |
| `rights`       | Array of [right descriptions](/technical/types/right/right.html#description) |

The capabilities are given as a map in order to support attributes in future versions. Currently they have no attributes, so
each capability has an empty object as value.

## Permissions

The session must be authenticated.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed or the provided context does not support presets |
| 400 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |






# Retrieve right presets

    GET /api/v1/right/<context>/presets[/<id>]?token=<token>

Returns the list of presets for a context, or a particular right preset in this context.

## Path parameters

|   |   |
|---|---|
| `context`       | Right context (this context must have the capability "preset") |
| `id`            | Right preset ID (integer, optional): if set, get right preset `id` |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Returns

If `id` was set, this call returns a [right preset](/technical/types/right_preset/right_preset.html). Otherwise, it returns an array of right presets.
The presets are ordered by their `_position`.

## Permissions

The session must be authenticated.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed or the provided context does not support presets |
| 400 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |





# Edit right presets

    POST /api/v1/right/<context>/presets?token=<token>

Edit right presets for a given context.

## Path parameters

|   |   |
|---|---|
| `context`       | Right context (this context must have the capability "preset") |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Input

An array of [right presets](/technical/types/right_preset/right_preset.html).

## Returns

Array of right presets.

## Permissions

The user requires the `system.righpresetmanager` right.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed or the provided context does not support presets |
| 400 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 400 | [No System Right](/technical/errors/errors.html#no_system_right): user lacks the required system right |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |





# Delete right preset

    DELETE /api/v1/right/<context>/presets/<id>?token=<token>

Delete a right preset.

## Path parameters

|   |   |
|---|---|
| `context`       | Right context (this context must have the capability "preset") |
| `id`            | Preset ID |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Permissions

The user requires the `system.righpresetmanager` right.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed or the provided context does not support presets |
| 400 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 400 | [No System Right](/technical/errors/errors.html#no_system_right): user lacks the required system right |
| 400 | [Right Preset Not Found](/technical/errors/errors.html#right_preset_not_found): right preset `id` not found in the provided `context` |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |
