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
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Authentication

This call requires the `system.message` system right.

## Output

Array of [messages](/technical/types/message/message.html).

## Examples


[include](./get.json)



[include](./get_id.json)


## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed |
| 403 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 404 | [Message Not Found](/technical/errors/errors.html#message_not_found): message `id` not found |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |





# Insert or update messages

    POST/PUT /api/v1/message?token=<token>

Creates (PUT) or updates (POST) messages.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Authentication

This call requires the `system.message` system right.

## Input

Array of [messages](/technical/types/message/message.html). POST only updates fields
that are set, leaving the rest as they currently are.

## Ouput

Array of [messages](/technical/types/message/message.html) that were updated.

## Examples


[include](./put.json)



[include](./post.json)


## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed |
| 403 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 403 | [Change Owner On Creation](/technical/errors/errors.html#change_owner_on_creation): the user attempted to set a different owner than him-/herself when creating a message |
| 404 | [Message Not Found](/technical/errors/errors.html#message_not_found): message `message._id` not found |
| 404 | [User Not Found](/technical/errors/errors.html#user_not_found): user not found (in `_owner.who`) |
| 404 | [Group Not Found](/technical/errors/errors.html#group_not_found): group not found (in `_owner.who` or `_groups`) |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |





# Delete message

    DELETE /api/v1/message/<id>?token=<token>

## Path parameters

|   |   |
|---|---|
| `id`    | Message ID (integer) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Authentication

This call requires the `system.message` system right.

## Output

*empty*

## Examples

```json
Request:  DELETE /api/v1/message/32
Response: HTTP 200
```

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed |
| 403 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 404 | [Message Not Found](/technical/errors/errors.html#message_not_found): message `id` not found |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |
