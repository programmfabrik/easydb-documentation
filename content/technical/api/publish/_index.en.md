---
title: "70 - publish"
menu:
  main:
    name: "publish"
    identifier: "technical/api/publish"
    parent: "technical/api"
---
# Retrieve the list of published objects

	GET /api/v1/publish[/<system_object_id>]?token=<token>

Retrieves publishing information.

## Path parameters

| parameter  | description  |
|---|---|
| `system_object_id` | System Object ID to get publish information for (integer, optional). If not provided, publish information for all objects is returned |

## Query String

| parameter  | description |
|---|---|
| `limit` | Maximum number of items returned (integer, optional). When not provided or if it exceeds 1000, a limit of 1000 is used. |
| `offset` | Offset in result set (integer, optional). 0 is used if none is requested. |
| `token`  | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Output

a list of [publish](/en/technical/types/publish) objects.

## Permissions

The system right `system.api.publish.get` is required to use this request.

# Publish an object

	POST /api/v1/publish?token=<token>

Only new publishing can be done using this API. There is no possibility to update an existing objects. Use `DELETE` as documented below to remove the object and publish it again.

## Input

a list of [publish](/en/technical/types/publish) objects.

## Output

a list of [publish](/en/technical/types/publish) objects. In addition to the data in input an ID is added for each object.

## Query String

| parameter  | description |
|---|---|
| `token`  | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Permissions

The system right `system.api.publish.post` is required to use this request.

# De-publish an object

	DELETE /api/v1/publish/<publish_id>?token=<token>

## Path parameters

| parameter  | description  |
|---|---|
| `publish_id` | ID of publishing object (integer, optional). |

## Query String

| parameter  | description |
|---|---|
| `token`  | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Permissions

The system right `system.api.publish.delete` is required to use this request.
