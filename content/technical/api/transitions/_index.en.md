---
title: "79 - transitions"
menu:
  main:
    name: "transitions"
    identifier: "technical/api/transitions"
    parent: "technical/api"
---
# Retrieve transitions

    GET /api/v1/transitions?token=<token>

Retrieves all transitions. Transitions are returned in the order they are processed.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Returns

Array of [transitions](/en/technical/types/transition).

## Examples


{{< include_json "./get.json" >}}


## Permissions

The session must be authenticated.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |





# Update transitions

    POST /api/v1/transitions?token=<token>

Updates all transitions. The list should be always complete. That means, if a transition
is not provided, it will be deleted. The order of the list is relevant: it determines the
processing order of the transitions.

## Input

Array of [transitions](/en/technical/types/transition).

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Returns

Array of [transitions](/en/technical/types/transition).

## Permissions

The session must be authenticated and the user needs the `system.rights_management` right.
Otherwise, an error will be returned.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [No System Right](/en/technical/errors): no system right for "\_all\_fields" |
| 500 | [Server error](/en/technical/errors): internal server error |
