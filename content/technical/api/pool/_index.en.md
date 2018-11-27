---
title: "70 - pool"
menu:
  main:
    name: "pool"
    identifier: "technical/api/pool"
    parent: "technical/api"
---
# Retrieve pools

    GET /api/v1/pool[/<id>]?token=<token>

Get one or all pools.

The system provides one top level Root-Pool which can be used to set top level transitions, tags and right. The top level Root-Pool is not included in searches and object output.

## Path parameters

|   |   |
|---|---|
| `id`    | Pool ID (integer, optional): if set, get pool `id` |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Output

Array of [pools](/en/technical/types/pool) (full format).

Whether information about the ACL (fields `_acl` and `_private_acl`) of the pool is included in the output depends on the right of the user. If the user has the `bag_write` right, the ACL information is included. If the user only has the `bag_read` right, this information is not included.

## Permissions

The session must be authenticated and the user needs the `bag_write` or `bag_read` right for the pool(s)
(see [rights management](/en/technical/rightsmanagement)).

Notice that if an `id` was provided and the pool is not readable this API call returns a 400 error, but
if no `id` is provided, the non-readable pools are filtered out. This call may return an empty array.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no `bag_write` right |
| 400 | [Pool Not Found](/en/technical/errors): pool `id` not found |
| 500 | [Server error](/en/technical/errors): internal server error |

## Examples


{{< include_json "./get.json" >}}



{{< include_json "./get_id.json" >}}






# Insert or update pools

    PUT/POST /api/v1/pool?token=<token>

Creates or updates a set of pools.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `collection_rights_policy` | What to do if the operation causes the owner of a collection to lose grantable rights over collection objects (see [rightsmanagement](/en/technical/rightsmanagement)) |

## Input

Array of [pools](/en/technical/types/pool) (full format).

## Output

Array of [pools](#pool) (full format) that were inserted / updated.

## Permissions

The session must be authenticated and the user needs:

- the `bag_write` right for the pools to be updated
- the `bag_acl` right if any rights management attribute (\*) is updated, for pools other than the root pool
- the `system.rights_management` right if any rights management attribute (\*) is updated, for the root pool
- the `bag_create` right for the parent pools of the pools to be created

(\*) The following attributes are in the rights management group:
`_acl`, `_private_acl`, `_tags`, `_private_tags`, `_transitions`, `_private_transitions`.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 202 | [Confirmation Response (collection owner rights revoked](/en/technical/confirmation): the operation requires confirmation with a `collection_rights_policy` |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "bag_write" right |
| 400 | [No System Right](/en/technical/errors): user lacks the required system right to update the pool |
| 400 | [System Pool Update Parent](/en/technical/errors): trying to change the parent of a system pool |
| 400 | [Pool Not Found](/en/technical/errors): pool `id` or `pool._id_parent` not found (the error tells which one) |
| 400 | [User Not Found](/en/technical/errors): user not found (in `_acl.who`, `_transitions.who` or `contact`) |
| 400 | [Group Not Found](/en/technical/errors): group not found (in `_acl.who` or `_transitions.who`) |
| 400 | [Tag Not Found](/en/technical/errors): tag not found (in `_tags` or `_acl.tagfilter`) |
| 400 | [Pool Requires Parent](/en/technical/errors): a new pool (PUT) requires a parent |
| 500 | [Server error](/en/technical/errors): internal server error |

## Examples


{{< include_json "./put.json" >}}



{{< include_json "./post.json" >}}






# Delete pool

    DELETE /api/v1/pool/<id>?token=<token>

Delete a pool. In order to delete a pool, it must be empty. That means that it
cannot contain other pools, but also that there are no objects in it.

## Path parameters

|   |   |
|---|---|
| `id`    | Pool ID (integer) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Examples

```javascript
Request:  DELETE /api/v1/pool/3
Response: HTTP 200
```

## Permissions

The session must be authenticated and the user needs the `bag_delete` right for the pool
(see [rights management](/en/technical/rightsmanagement)).

System pools are not allowed to be deleted.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "bag_delete" right |
| 400 | [Pool Not Found](/en/technical/errors): pool `id` not found |
| 400 | [System Pool Delete](/en/technical/errors): pool `id` is a system pool |
| 500 | [Server error](/en/technical/errors): internal server error |
