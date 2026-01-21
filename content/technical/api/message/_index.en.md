---
title: "66 - message"
menu:
  main:
    name: "message"
    identifier: "technical/api/message"
    parent: "technical/api"
---
# Retrieve messages

    GET /api/v1/message[/<id>]?token=<token>

Get one or all messages.

## Path parameters

|   |   |
|---|---|
| `id`    | Message ID (integer, optional): if set, get message `id` |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Authentication

This call requires the `system.message` system right.

## Output

Array of [messages](/en/technical/types/message).

## Examples

{{< include_json "./get.json" >}}

{{< include_json "./get_id.json" >}}


## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 404 | [Message Not Found](/en/technical/errors): message `id` not found |
| 500 | [Server error](/en/technical/errors): internal server error |





# Insert or update messages

    POST/PUT /api/v1/message?token=<token>

Creates (PUT) or updates (POST) messages.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Authentication

This call requires the `system.message` system right.

## Input

Array of [messages](/en/technical/types/message). POST only updates fields
that are set, leaving the rest as they currently are.

## Output

Array of [messages](/en/technical/types/message) that were updated.

## Examples


{{< include_json "./put.json" >}}



{{< include_json "./post.json" >}}


## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 403 | [Change Owner On Creation](/en/technical/errors): the user attempted to set a different owner than him-/herself when creating a message |
| 404 | [Message Not Found](/en/technical/errors): message `message._id` not found |
| 404 | [User Not Found](/en/technical/errors): user not found (in `_owner.who`) |
| 404 | [Group Not Found](/en/technical/errors): group not found (in `_owner.who` or `_groups`) |
| 500 | [Server error](/en/technical/errors): internal server error |





# Delete message

    DELETE /api/v1/message/<id>?token=<token>

## Path parameters

|   |   |
|---|---|
| `id`    | Message ID (integer) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Authentication

This call requires the `system.message` system right.

## Output

*empty*

## Examples

```javascript
Request:  DELETE /api/v1/message/32
Response: HTTP 200
```

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 404 | [Message Not Found](/en/technical/errors): message `id` not found |
| 500 | [Server error](/en/technical/errors): internal server error |
