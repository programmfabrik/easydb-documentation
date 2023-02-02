---
title: "68 - objecttype"
menu:
  main:
    name: "objecttype"
    identifier: "technical/api/objecttype"
    parent: "technical/api"
---
# Retrieve objecttypes

    GET /api/v1/objecttype[/<id>]?token=<token>

Get one or all objecttypes.

## Path parameters

|   |   |
|---|---|
| `id` | Objecttype ID (integer, optional) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `format` | If set to `short`, the fields requiring the `system.objecttypemanager` right (see below) are not returned, even if the user has been granted this right. |

## Output

Array of [objecttypes](/en/technical/types/objecttype). If `id` was given, that objecttype is returned. Otherwise, all
objecttypes are returned.

## Permissions

The session must be authenticated.

The following fields are not returned if the user lacks the `system.objecttypemanager` right:
`_acl`, `_tags`, `_private_tags`, `_transitions`, `_private_transitions`.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 404 | [Not Found](/en/technical/errors): objecttype `id` not found |
| 500 | [Server error](/en/technical/errors): internal server error |





# Update objecttypes

Objecttypes are created using the /api/v1/schema calls, the calls described
here can only add additional information to already existing objecttypes.

    POST /api/v1/objecttype?token=<token>[&collection_rights_policy=<collection_rights_policy>]

Update a list of objecttypes.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `collection_rights_policy` | What to do if the operation causes the owner of a collection to lose grantable rights over collection objects (see [rightsmanagement](/en/technical/rightsmanagement)) |

## Input

Array of [objecttypes](/en/technical/types/objecttype). The `_id` must be set.

## Output

Array of updated [objecttypes](/en/technical/types/objecttype).

## Permissions

The session must be authenticated.

The following fields cannot be modifed if the user lacks the `system.rights_management` right:
`_acl`, `_tags`, `_private_tags`, `_transitions`, `_private_transitions`.
An attempt to modify any of these will result in a 403 error.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 202 | [Confirmation Response (collection owner rights revoked](/en/technical/confirmation): the operation requires confirmation with a `collection_rights_policy` |
| 400 | [API error](/en/technical/errors): something is malformed |
| 403 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 403 | [No System Right](/en/technical/errors): user lacks the required system right to update the objecttype |
| 500 | [Server error](/en/technical/errors): internal server error |
