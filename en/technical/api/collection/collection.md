# Retrieve collection

    GET /api/v1/collection/<id>?token=<token>
    GET /api/v1/collection/uuid/<uuid>?token=<token>

Retrieves information about a collection.

The system provides one top level Root-Collection which can be used to set top level rights. The top level Root-Collection is not included in searches and object output.

## Path parameters

Depending on the call, the collection ID or UUID must be provided.

|   |   |
|---|---|
| `id`   | Collection ID (integer) |
| `uuid` | Collection UUID (text) |

## Query String

|   |   |
|---|---|
| `token`  | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Output

A [collection](/technical/types/collection/collection.md).

## Permissions

The user must own the collection or have the `bag_read` right for it
(see [rights management](/technical/rightsmanagement/rightsmanagement.md)).

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Insufficient Rights](/technical/errors/errors.md#insufficient_rights): no "bag_read" right |
| 400 | [Collection Not Found](/technical/errors/errors.md#collection_not_found): collection `id` not found |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |

## Examples


[include](./get.json)






# Retrieve collections

    GET /api/v1/collection/list[/<id>]?token=<token>

The collections build a hierarchy. This call returns all children from a given collection or,
if no ID is given, the top level collections.

## Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer, optional) - if not set, return the top level collections |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Output

Array of [collections](/technical/types/collection/collection.md) (may be empty).

## Permissions

The session must be authenticated. The list of collections returned are filtered as in the previous call
(`bag_read` or owned by user).

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Collection Not Found](/technical/errors/errors.md#collection_not_found): collection `id` not found |
| 400 | [User Not Found](/technical/errors/errors.md#user_not_found): user not found (in `_acl.who` or `_owner.who`) |
| 400 | [Group Not Found](/technical/errors/errors.md#group_not_found): group not found (in `_acl.who` or `_owner.who`) |
| 400 | [Tag Not Found](/technical/errors/errors.md#tag_not_found): tag not found (in `_acl.tagfilter`) |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |

## Example


[include](./get_list.json)



[include](./get_list_id.json)






# Create or update collection

    PUT  /api/v1/collection?token=<token>
    POST /api/v1/collection/<id>?token=<token>

Creates a new collection (PUT) or updates a collection (POST).

## Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |
| `collection_rights_policy` | What to do if the operation causes the owner of a collection to lose grantable rights over collection objects (see [rightsmanagement](/technical/rightsmanagement/rightsmanagement.md#collection_rights_policy)) |

## Input

A [collection](/technical/types/collection/collection.md).

## Output

The [collection](/technical/types/collection/collection.md) that was created / updated.

## Collection sharing

Collection sharing is accomplished by providing special "who" entries in the collection ACL (see [user (short format)](/technical/types/user/user.md#short)):

- "email" users are identified by the e-mail provided and, if not, automatically generated (the user may specify a `frontend_language` for e-mail users)
- "collection" users are automatically generated using the secret provided: if the secret exists an error is returned

The collection ACL has a special attribute "send_email_notification" that can be used to send an e-mail when the ACL is updated.


[include](./share.json)


## Permissions

The user must own the collection or have the `bag_read` right for it

- the `bag_write` right for the collection, if it is an update (POST)
- the `bag_acl` right if any rights management attribute (\*) is updated
- the `bag_create` right for the parent collection (PUT)
- if the collection is owned by the user, `bag_write` and `bag_acl` are not needed
- if the parent collection is owned by the user, `bag_create` is not needed

System collections cannot be created, but they can be updated. Only the following parameters are allowed to be modified:

- rights management attributes (this requires the `system.rights_management` right)
- `create_object` attributes

(\*) The following attributes are in the rights management group:
`_acl`, `_private_acl`.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 202 | [Confirmation Response (collection owner rights revoked)](/technical/confirmation/confirmation.md#corr): the operation requires confirmation with a `collection_rights_policy` |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Collection Name Repeated](/technical/errors/errors.md#collection_name_repeated): a collection with the same name exists under the same parent collection |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Insufficient Rights](/technical/errors/errors.md#insufficient_rights): no "bag_write" right |
| 400 | [No System Right](/technical/errors/errors.md#no_system_right): user lacks the required system right to update the collection |
| 400 | [Collection Does Not Allow Children](/technical/errors/errors.md#collection_does_not_allow_children): trying to create or move a collection under a collection that does not allow children |
| 400 | [System Collection Update](/technical/errors/errors.md#system_collection_update): trying to change an attribute of a system collection which cannot be changed |
| 400 | [Collection Not Found](/technical/errors/errors.md#collection_not_found): collection `id` or `collection._id_parent` not found (the error tells which one) |
| 400 | [Tag Not Found](/technical/errors/errors.md#tag_not_found): a tag that was provided for a tag filter in the collection `_acl` was not found |
| 400 | [Right Not Found](/technical/errors/errors.md#right_not_found): a right that was provided in the `_acl` was not found |
| 400 | [Collection Requires Parent](/technical/errors/errors.md#collection_requires_parent): a new collection (PUT) requires a parent |
| 400 | [Collection Is Not Under User Collection](/technical/errors/errors.md#collection_is_not_under_user_collection): the collection is not under the user collection |
| 400 | [Collection User Secret Already Exists](/technical/errors/errors.md#collection_user_secret_already_exists): the secret already exists |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |

## Examples


[include](./put.json)



[include](./post.json)






# Remove collection

    DELETE /api/v1/collection/<id>?token=<token>

Removes a collection.

## Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Output

The [collection](/technical/types/collection/collection.md) that was removed.

## Permissions

The user must own the collection or have the `bag_delete` right for it
(see [rights management](/technical/rightsmanagement/rightsmanagement.md)).

System collections are not allowed to be deleted.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Insufficient Rights](/technical/errors/errors.md#insufficient_rights): no "bag_read" right |
| 400 | [Collection Not Found](/technical/errors/errors.md#collection_not_found): collection `id` not found |
| 400 | [System Collection Delete](/technical/errors/errors.md#system_collection_delete): operation not allowed because collection `id` is a system collection |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |

## Examples

```json
Request:  DELETE /api/v1/collection/9
Response: HTTP 200
```





# Retrieve objects from a collection

    GET /api/v1/collection/objects/<id>?token=<token>[&offset=<offset>][&limit=<limit>]

## Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

## Query String

|   |   |
|---|---|
| `token`  | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |
| `offset` | Index of the first object to be returned (integer): defaults to 0 |
| `limit`  | Maximum number of objects to be returned (integer): defaults to *unlimited* |

## Output

The output is given as a map with the following parameters:

|   |   |
|---|---|
| `_version` | Collection version (integer) |
| `offset`   | Given offset (integer) |
| `limit`    | Given limit (integer or null) |
| `count`    | Total number of objects in the collection (integer) |
| `objects`  | Array of "collection objects" |

The order of the objects in a collection is important. A "collection object" has the following
attributes:

|   |   |
|---|---|
| `_global_object_id`  | Global Object ID (string): ref [object](/technical/types/object/object.md).\_global\_object\_id |
| `_webfrontend_props` | Custom data (object, nullable): frontend-defined properties |

## Permissions

The user must own the collection or have the `bag_read` right for it
(see [rights management](/technical/rightsmanagement/rightsmanagement.md)).

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Insufficient Rights](/technical/errors/errors.md#insufficient_rights): no "bag_read" right |
| 400 | [Collection Not Found](/technical/errors/errors.md#collection_not_found): collection `id` not found |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |

## Examples


[include](./get_objects.json)






# Update collection objects

    POST /api/v1/collection/objects/<id>?token=<token>

## Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Input

The input is given as a map with the following parameters:

|   |   |
|---|---|
| `objects`  | Array of "collection objects" |

## Output

The output is given as a map with the following parameters:

|   |   |
|---|---|
| `_version` | Collection version (integer) |
| `count`    | Number of objects in the collection (integer) |

## Permissions

The session must be authenticated and the user needs:

- the `link` right for the objects that are added to the collection (filtered by object type or pool)
- the `unlink` right for the objects that are removed from the collection (filtered by object type or pool)
- if the collection is owned by the user, `link` and `unlink` are not needed

New objects are granted some rights through the collection ACL. The owner of the collection must have these rights
over the objects before the operation. Furhtermore, they must be grantable.

See [rights management](/technical/rightsmanagement/rightsmanagement.md).

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Insufficient Rights](/technical/errors/errors.md#insufficient_rights): no "link" or "unlink" right |
| 400 | [No Grantable Right](/technical/errors/errors.md#no_grantable_right): the owner of the collection has no grantable right for the new objects |
| 400 | [Collection Not Found](/technical/errors/errors.md#collection_not_found): collection `id` not found |
| 400 | [Object Not Found](/technical/errors/errors.md#object_not_found): object not found, the global object id is given as parameter of the error |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |

## Examples


[include](./post_objects.json)






# Insert objects to a collection

    POST /api/v1/collection/push/<id>

This call appends objects to the end of the collection. It works the same way as
the previous call, but extending the list, rather than replacing it.

## Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Input

The input is given as a map with the following parameters:

|   |   |
|---|---|
| `objects`  | Array of "collection objects" |

## Output

The output is given as a map with the following parameters:

|   |   |
|---|---|
| `_version` | Collection version (integer) |
| `count`    | Number of objects in the collection (integer) |

## Permissions

The session must be authenticated and the user must own the collection of have
the `link` right for the objects that are added to it (filtered by object type or pool).

New objects are granted some rights through the collection ACL. The owner of the collection must have these rights
over the objects before the operation. Furhtermore, they must be grantable.

See [rights management](/technical/rightsmanagement/rightsmanagement.md).

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Insufficient Rights](/technical/errors/errors.md#insufficient_rights): no "link" right |
| 400 | [No Grantable Right](/technical/errors/errors.md#no_grantable_right): the owner of the collection has no grantable right for the new objects |
| 400 | [Collection Not Found](/technical/errors/errors.md#collection_not_found): collection `id` not found |
| 400 | [Object Not Found](/technical/errors/errors.md#object_not_found): object not found, the global object id is given as parameter of the error |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |





# Remove collection objects

	POST /api/v1/collection/remove/<id>

Remove certain objects from a collection

## Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Input

An array of "collection objects". `_webfrontend_props` is not used in this case.

## Output

The output is given as a map with the following parameters:

|   |   |
|---|---|
| `_version` | Collection version (integer) |
| `count`    | Number of objects in the collection (integer) |

## Permissions

The session must be authenticated and the user must own the collection of have
the `link` right for the objects that are added to it (filtered by object type or pool).

New objects are granted some rights through the collection ACL. The owner of the collection must have these rights
over the objects before the operation. Furhtermore, they must be grantable.

See [rights management](/technical/rightsmanagement/rightsmanagement.md).

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Insufficient Rights](/technical/errors/errors.md#insufficient_rights): no "link" right |
| 400 | [No Grantable Right](/technical/errors/errors.md#no_grantable_right): the owner of the collection has no grantable right for the new objects |
| 400 | [Collection Not Found](/technical/errors/errors.md#collection_not_found): collection `id` not found |
| 400 | [Object Not Found](/technical/errors/errors.md#object_not_found): object not found, the global object id is given as parameter of the error |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |





# Splice collection objects

    POST /api/v1/collection/splice/<id>

Perform a splice operation with the collection objects.

## Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Input

An object with the following properties:

|   |   |
|---|---|
| `index`   | Start position to remove items (integer, defaults to size of collection) |
| `count`   | Number of items to be removed (integer, defaults to all elements from start to end) |
| `objects` | Items to be added (array of "collection objects", defaults to an empty array) |

## Output

An object with the following properties

|   |   |
|---|---|
| `_version` | Collection version (integer) |
| `count`    | Number of elements in the collection (integer) |
| `objects`  | Removed items (array of strings): instead of "collection objects", this is a list of global object IDs |

## Permissions

The session must be authenticated and the user needs:

- the `link` right for the objects that are added to the collection (filtered by object type or pool)
- the `unlink` right for the objects that are removed from the collection (filtered by object type or pool)
- if the collection is owned by the user, `link` and `unlink` are not needed

New objects are granted some rights through the collection ACL. The owner of the collection must have these rights
over the objects before the operation. Furhtermore, they must be grantable.

See [rights management](/technical/rightsmanagement/rightsmanagement.md).

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Insufficient Rights](/technical/errors/errors.md#insufficient_rights): no "link" or "unlink" right |
| 400 | [No Grantable Right](/technical/errors/errors.md#no_grantable_right): the owner of the collection has no grantable right for the new objects |
| 400 | [Collection Not Found](/technical/errors/errors.md#collection_not_found): collection `id` not found |
| 400 | [Object Not Found](/technical/errors/errors.md#object_not_found): object not found, the global object id is given as parameter of the error |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |

## Example

```json
Request: GET /api/v1/collection/objects/1
Response: 200 OK
[ image-7, video-8, image-10, video-14, image-11, image-17 ]

Request: POST /api/v1/collection/splice/1
{ "index": 3, "count": 2, "objects": [ image-7, image-10, video-14, video-15 ] }
Response: 200 OK
{ "objects": [ video-14, image-11 ], "count": 6 }

Request: GET /api/v1/collection/objects/1
Response: 200 OK
[ video-8, image-7, image-10, video-14, video-15, image-17 ] // 6 elements
```
