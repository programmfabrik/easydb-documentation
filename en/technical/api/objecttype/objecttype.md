# Retrieve objectypes

    GET /api/v1/objecttype[/<id>]?token=<token>

Get one or all objecttypes.

## Path parameters

|   |   |
|---|---|
| `id` | Objecttype ID (integer, optional) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Output

Array of [objecttypes](/technical/types/objecttype/objecttype.md). If `id` was given, that objecttype is returned. Otherwise, all
objecttypes are returned.

## Permissions

The session must be authenticated.

The following fields are not returned if the user lacks the `system.objecttypemanager` right:
`_acl`, `_tags`, `_private_tags`, `_transitions`, `_private_transitions`.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 403 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 404 | [Not Found](/technical/errors/errors.md#not_found): objecttype `id` not found |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |





# Update objecttypes

Objecttypes are created using the /api/v1/schema calls, the calls described
here can only add additional information to already existing objecttypes.

    POST /api/v1/objecttype?token=<token>[&collection_rights_policy=<collection_rights_policy>]

Update a list of objecttypes.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |
| `collection_rights_policy` | What to do if the operation causes the owner of a collection to lose grantable rights over collection objects (see [rightsmanagement](/technical/rightsmanagement/rightsmanagement.md#collection_rights_policy)) |

## Input

Array of [objecttypes](/technical/types/objecttype/objecttype.md). The `_id` must be set.

## Output

Array of updated [objecttypes](/technical/types/objecttype/objecttype.md).

## Permissions

The session must be authenticated.

The following fields cannot be modifed if the user lacks the `system.rights_management` right:
`_acl`, `_tags`, `_private_tags`, `_transitions`, `_private_transitions`.
An attempt to modify any of these will result in a 403 error.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 202 | [Confirmation Response (collection owner rights revoked](/technical/confirmation/confirmation.md#corr): the operation requires confirmation with a `collection_rights_policy` |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 403 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 403 | [No System Right](/technical/errors/errors.md#no_system_right): user lacks the required system right to update the objecttype |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |
