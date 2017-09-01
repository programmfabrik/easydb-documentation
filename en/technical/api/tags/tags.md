# Retrieve tags

    GET /api/v1/tags?token=<token>

Retrieves all tags and tag groups. Tags have an order inside tag groups.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Returns

Array of [tag groups](/technical/types/tag/tag.md#taggroup).

## Examples

~~~~json
@@include:get.json@@
~~~~

## Permissions

The session must be authenticated.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |





# Update tags

    POST /api/v1/tags?token=<token>

Updates all tags and tag groups. The list should be always complete. That means, if a tag or tag group
is not provided, it will be deleted. Tags or tag groups with `_id` will be updated; otherwise, they will
be created.

## Input

Array of [tag groups](/technical/types/tag/tag.md#taggroup).

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |
| `collection_rights_policy` | What to do if the operation causes the owner of a collection to lose grantable rights over collection objects (see [rightsmanagement](/technical/rightsmanagement/rightsmanagement.md#collection_rights_policy)) |

## Returns

Array of [tag groups](/technical/types/tag/tag.md#taggroup).

## Permissions

The user requires the `system.tagmanager` right.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 202 | [Confirmation Response (collection owner rights revoked](/technical/confirmation/confirmation.md#corr): the operation requires confirmation with a `collection_rights_policy` |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [No System Right](/technical/errors/errors.md#no_system_right): no system right for "\_all\_fields" |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |
