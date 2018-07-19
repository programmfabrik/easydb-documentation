---
title: "78 - tags"
menu:
  main:
    name: "tags"
    identifier: "technical/api/tags"
    parent: "technical/api"
---
# Retrieve tags

    GET /api/v1/tags?token=<token>

Retrieves all tags and tag groups. Tags have an order inside tag groups.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Returns

Array of [tag groups](/en/technical/types/tag).

## Examples


{{< include_json "./get.json" >}}


## Permissions

The session must be authenticated.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |





# Update tags

    POST /api/v1/tags?token=<token>

Updates all tags and tag groups. The list should be always complete. That means, if a tag or tag group
is not provided, it will be deleted. Tags or tag groups with `_id` will be updated; otherwise, they will
be created.

## Input

Array of [tag groups](/en/technical/types/tag).

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `collection_rights_policy` | What to do if the operation causes the owner of a collection to lose grantable rights over collection objects (see [rightsmanagement](/en/technical/rightsmanagement)) |

## Returns

Array of [tag groups](/en/technical/types/tag).

## Permissions

The user requires the `system.tagmanager` right.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 202 | [Confirmation Response (collection owner rights revoked](/en/technical/confirmation): the operation requires confirmation with a `collection_rights_policy` |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [No System Right](/en/technical/errors): no system right for "\_all\_fields" |
| 500 | [Server error](/en/technical/errors): internal server error |
