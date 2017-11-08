# <a name="list"></a> Retrieve groups

    GET /api/v1/group[/<id>]?token=<token>

Retrieves one or all groups.

## Path parameters

|   |   |
|---|---|
| `id`            | Object ID (integer, optional): if set, get group `id` |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Returns

Array of [groups](/technical/types/group/group.html).

If `id` was specified and no group was found, this call returns an empty array.

## Permissions

The session must be authenticated and the user requires the `system.group` right.

The following groups can be read by a user:

- "easydb" groups the user belongs to
- groups for which the user has the `bag_read` right

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 400 | [No System Right](/technical/errors/errors.html#no_system_right): no `system.group` right |
| 400 | [Insufficient Rights](/technical/errors/errors.html#insufficient_rights): no `bag_read` right |
| 400 | [Group Not Found](/technical/errors/errors.html#group_not_found): group `id` not found |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |

## Examples


[include](./get.json)



[include](./get_id.json)






# Insert or update groups

    POST/PUT /api/v1/group?token=<token>

Creates (PUT) or updates (POST) groups.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Input

Array of [groups](/technical/types/group/group.html).

## Ouput

Array of [groups](/technical/types/group/group.html) that were updated.

## Permissions

The session must be authenticated.

### Updating a group

The user must have the `bag_write` right for the group.

### Creating a group

If a group is created, the user requires the `system.group` right with `create`.

When creating a group, the owner will be set to the session user. An attempt to set a different owner will trigger a Change Owner On Creation error.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 400 | [Insufficient Rights](/technical/errors/errors.html#insufficient_rights): no "bag_write" right |
| 400 | [No System Right](/technical/errors/errors.html#no_system_right): user lacks the required system right to update the group |
| 400 | [Change Owner On Creation](/technical/errors/errors.html#change_owner_on_creation): the user attempted to set a different owner than him-/herself when creating a user |
| 400 | [Group Not Found](/technical/errors/errors.html#group_not_found): group not found (`group._id`, or in `_acl.who` or `_owner.who`) |
| 400 | [User Not Found](/technical/errors/errors.html#user_not_found): user not found (in `_acl.who` or `_owner.who) |
| 400 | [Right Not Found](/technical/errors/errors.html#right_not_found): a right that was provided for `_acl` or `_system_rights` was not found |
| 400 | [Custom Type Required](/technical/errors/errors.html#custom_type_required): attempting to assign the "system.user.create_new" right with type "custom" but without specifying the "custom_type" |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |

## Examples


[include](./put.json)



[include](./post.json)






# Delete group

    DELETE /api/v1/group/<id>?token=<token>

Delete a group.

## Path parameters

|   |   |
|---|---|
| `id`            | Group ID (integer) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Examples

```json
Request:  DELETE /api/v1/group/2
Response: HTTP 200
```

## Permissions

The session must be authenticated and:

- the user must have the `bag_delete` right for the group provided

System groups are not allowed to be deleted.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 400 | [Group Not Found](/technical/errors/errors.html#group_not_found): group `id` not found |
| 400 | [Insufficient Rights](/technical/errors/errors.html#insufficient_rights): no "bag_delete" right |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |
