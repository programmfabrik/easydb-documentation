# Retrieve transitions

    GET /api/v1/transitions?token=<token>

Retrieves all transitions. Transitions are returned in the order they are processed.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Returns

Array of [transitions](/technical/types/transition/transition.html).

## Examples


[include](./get.json)


## Permissions

The session must be authenticated.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |





# Update transitions

    POST /api/v1/transitions?token=<token>

Updates all transitions. The list should be always complete. That means, if a transition
is not provided, it will be deleted. The order of the list is relevant: it determines the
processing order of the transitions.

## Input

Array of [transitions](/technical/types/transition/transition.html).

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Returns

Array of [transitions](/technical/types/transition/transition.html).

## Permissions

The session must be authenticated and the user needs the `system.rights_management` right.
Otherwise, an error will be returned.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 400 | [No System Right](/technical/errors/errors.html#no_system_right): no system right for "\_all\_fields" |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |
