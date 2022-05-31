---
title: "71 - right"
menu:
  main:
    name: "right"
    identifier: "technical/api/right"
    parent: "technical/api"
---
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
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Output

The output is a JSON object with an attribute for each context, which contains the following attributes:

| Name           | Description                                                                                               |
|----------------|-----------------------------------------------------------------------------------------------------------|
| `capabilities` | Features supported in this context. Each feature is a key in the capabilities map (see below)             |
| `presets`      | If the `capabilities` include "preset", this attributes shows a list of the right presets for this context (output of GET /api/v1/right/<context>/presets) |
| `rights`       | Array of [right descriptions](/en/technical/types/right) |

The capabilities are given as a map in order to support attributes in future versions. Currently they have no attributes, so
each capability has an empty object as value.

## Permissions

The session must be authenticated.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed or the provided context does not support presets |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 500 | [Server error](/en/technical/errors): internal server error |






# Retrieve right presets

    GET /api/v1/right/<context>/presets?token=<token>

Returns the list of presets for a context.

## Path parameters

|   |   |
|---|---|
| `context`       | Right context (this context must have the capability "preset") |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Returns

An array of [right presets](/en/technical/types/right_preset) is returned. The presets are ordered by their `_position`.

## Permissions

The session must be authenticated.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed or the provided context does not support presets |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 500 | [Server error](/en/technical/errors): internal server error |





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
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Input

An array of [right presets](/en/technical/types/right_preset).

## Returns

Array of right presets.

## Permissions

The user requires the `system.righpresetmanager` right.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed or the provided context does not support presets |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [No System Right](/en/technical/errors): user lacks the required system right |
| 500 | [Server error](/en/technical/errors): internal server error |





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
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Permissions

The user requires the `system.righpresetmanager` right.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed or the provided context does not support presets |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [No System Right](/en/technical/errors): user lacks the required system right |
| 400 | [Right Preset Not Found](/en/technical/errors): right preset `id` not found in the provided `context` |
| 500 | [Server error](/en/technical/errors): internal server error |
