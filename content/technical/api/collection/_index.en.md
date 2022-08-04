---
title: "56 - collection"
menu:
  main:
    name: "collection"
    identifier: "technical/api/collection"
    parent: "technical/api"
---

{{< toc-en >}}

## Retrieve collection

    GET /api/v1/collection/<id>?token=<token>
    GET /api/v1/collection/uuid/<uuid>?token=<token>

Retrieves information about a collection.

The system provides one top level Root-Collection which can be used to set top level rights. The top level Root-Collection is not included in searches and object output.

### Path parameters

Depending on the call, the collection ID or UUID must be provided.

|   |   |
|---|---|
| `id`   | Collection ID (integer) |
| `uuid` | Collection UUID (text) |

### Query String

|   |   |
|---|---|
| `token`  | Session token acquired with [/api/v1/session](/en/technical/api/session) |

### Output

A [collection](/en/technical/types/collection).

### Permissions

The user must own the collection or have the `bag_read` right for it
(see [rights management](/en/technical/rightsmanagement)).

### HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "bag_read" right |
| 400 | [Collection Not Found](/en/technical/errors): collection `id` not found |
| 500 | [Server error](/en/technical/errors): internal server error |

### Examples


{{< include_json "./get.json" >}}






## Retrieve collections

    GET /api/v1/collection/list[/<id_parent>]?token=<token>[&offset=<offset>][&limit=<limit>]

The collections build a hierarchy. This call returns all children of a given collection or, if the parent ID is set to `null`, the top level collections are returned.

If no parent ID is given, the hierarchy is ignored and all collections are returned, ordered by the collection ID.

### Path parameters

|   |   |
|---|---|
| `id_parent` | Collection ID (integer or string `null`, optional) - if set to `null`, return the top level collections; if not set, return all collections without hierarchy |
| `offset` | Index of the first object to be returned (integer, optional): defaults to `0` |
| `limit`  | Maximum number of objects to be returned (integer, optional): defaults to `1000`, maximum: `1000` |

### Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

### Output

Array of [collections](/en/technical/types/collection) (may be empty).

### Permissions

The session must be authenticated. The list of collections returned are filtered as in the previous call
(`bag_read` or owned by user).

### HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Collection Not Found](/en/technical/errors): collection `id_parent` not found |
| 400 | [User Not Found](/en/technical/errors): user not found (in `_acl.who` or `_owner.who`) |
| 400 | [Group Not Found](/en/technical/errors): group not found (in `_acl.who` or `_owner.who`) |
| 400 | [Tag Not Found](/en/technical/errors): tag not found (in `_acl.tagfilter`) |
| 500 | [Server error](/en/technical/errors): internal server error |

### Example


{{< include_json "./get_list.json" >}}



{{< include_json "./get_list_id.json" >}}






## Create or update collection

    PUT  /api/v1/collection?token=<token>
    POST /api/v1/collection/<id>?token=<token>

Creates a new collection (PUT) or updates a collection (POST).

### Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

### Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `collection_rights_policy` | What to do if the operation causes the owner of a collection to lose grantable rights over collection objects (see [rightsmanagement](/en/technical/rightsmanagement)) |

### Input

A [collection](/en/technical/types/collection).

### Output

The [collection](/en/technical/types/collection) that was created / updated.

### Collection sharing

Collection sharing is accomplished by providing special "who" entries in the collection ACL (see [user (short format)](/en/technical/types/user)):

- "email" users are identified by the e-mail provided and, if not, automatically generated (the user may specify a `frontend_language` for e-mail users)
- "collection" users are automatically generated using the secret provided: if the secret exists an error is returned

The collection ACL has a special attribute "send_email_notification" that can be used to send an e-mail when the ACL is updated.


{{< include_json "./share.json" >}}


### Permissions

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

### HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 202 | [Confirmation Response (collection owner rights revoked)](/en/technical/confirmation): the operation requires confirmation with a `collection_rights_policy` |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Collection Name Repeated](/en/technical/errors): a collection with the same name exists under the same parent collection |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "bag_write" right |
| 400 | [No System Right](/en/technical/errors): user lacks the required system right to update the collection |
| 400 | [Collection Does Not Allow Children](/en/technical/errors): trying to create or move a collection under a collection that does not allow children |
| 400 | [System Collection Update](/en/technical/errors): trying to change an attribute of a system collection which cannot be changed |
| 400 | [Collection Not Found](/en/technical/errors): collection `id` or `collection._id_parent` not found (the error tells which one) |
| 400 | [Tag Not Found](/en/technical/errors): a tag that was provided for a tag filter in the collection `_acl` was not found |
| 400 | [Right Not Found](/en/technical/errors): a right that was provided in the `_acl` was not found |
| 400 | [Collection Requires Parent](/en/technical/errors): a new collection (PUT) requires a parent |
| 400 | [Collection Is Not Under User Collection](/en/technical/errors): the collection is not under the user collection |
| 400 | [Collection User Secret Already Exists](/en/technical/errors): the secret already exists |
| 500 | [Server error](/en/technical/errors): internal server error |

### Examples


{{< include_json "./put.json" >}}



{{< include_json "./post.json" >}}






## Remove collection

    DELETE /api/v1/collection/<id>?token=<token>

Removes a collection.

### Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

### Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

### Output

There is no output when the collection was removed successfully.

### Permissions

The user must own the collection or have the `bag_delete` right for it
(see [rights management](/en/technical/rightsmanagement)).

System collections are not allowed to be deleted.

### HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "bag_read" right |
| 400 | [Collection Not Found](/en/technical/errors): collection `id` not found |
| 400 | [System Collection Delete](/en/technical/errors): operation not allowed because collection `id` is a system collection |
| 500 | [Server error](/en/technical/errors): internal server error |

### Examples

```javascript
Request:  DELETE /api/v1/collection/9
Response: HTTP 200
```





## Retrieve objects from a collection

    GET /api/v1/collection/objects/<id>?token=<token>[&offset=<offset>][&limit=<limit>]

### Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

### Query String

|   |   |
|---|---|
| `token`  | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `offset` | Index of the first object to be returned (integer): defaults to `0` |
| `limit`  | Maximum number of objects to be returned (integer): defaults to `1000`, maximum: `1000` |

### Output

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
| `_global_object_id`  | Global Object ID (string): ref [object](/en/technical/types/object).\_global\_object\_id |
| `_webfrontend_props` | Custom data (object, nullable): frontend-defined properties |

### Permissions

The user must own the collection or have the `bag_read` right for it
(see [rights management](/en/technical/rightsmanagement)).

### HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "bag_read" right |
| 400 | [Collection Not Found](/en/technical/errors): collection `id` not found |
| 500 | [Server error](/en/technical/errors): internal server error |

### Examples


{{< include_json "./get_objects.json" >}}






## Update collection objects

    POST /api/v1/collection/objects/<id>?token=<token>

### Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

### Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

### Input

The input is given as a map with the following parameters:

|   |   |
|---|---|
| `objects`  | Array of "collection objects" |

### Output

The output is given as a map with the following parameters:

|   |   |
|---|---|
| `_version` | Collection version (integer) |
| `count`    | Number of objects in the collection (integer) |

### Permissions

The session must be authenticated and the user needs:

- the `link` right for the objects that are added to the collection (filtered by object type or pool)
- the `unlink` right for the objects that are removed from the collection (filtered by object type or pool)
- if the collection is owned by the user, `link` and `unlink` are not needed

New objects are granted some rights through the collection ACL. The owner of the collection must have these rights
over the objects before the operation. Furhtermore, they must be grantable.

See [rights management](/en/technical/rightsmanagement).

### HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "link" or "unlink" right |
| 400 | [No Grantable Right](/en/technical/errors): the owner of the collection has no grantable right for the new objects |
| 400 | [Collection Not Found](/en/technical/errors): collection `id` not found |
| 400 | [Object Not Found](/en/technical/errors): object not found, the global object id is given as parameter of the error |
| 500 | [Server error](/en/technical/errors): internal server error |

### Examples


{{< include_json "./post_objects.json" >}}






## Insert objects to a collection

    POST /api/v1/collection/push/<id>

This call appends objects to the end of the collection. It works the same way as
the previous call, but extending the list, rather than replacing it.

### Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

### Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

### Input

The input is given as a map with the following parameters:

|   |   |
|---|---|
| `objects`  | Array of "collection objects" |

### Output

The output is given as a map with the following parameters:

|   |   |
|---|---|
| `_version` | Collection version (integer) |
| `count`    | Number of objects in the collection (integer) |

### Permissions

The session must be authenticated and the user must own the collection of have
the `link` right for the objects that are added to it (filtered by object type or pool).

New objects are granted some rights through the collection ACL. The owner of the collection must have these rights
over the objects before the operation. Furhtermore, they must be grantable.

See [rights management](/en/technical/rightsmanagement).

### HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "link" right |
| 400 | [No Grantable Right](/en/technical/errors): the owner of the collection has no grantable right for the new objects |
| 400 | [Collection Not Found](/en/technical/errors): collection `id` not found |
| 400 | [Object Not Found](/en/technical/errors): object not found, the global object id is given as parameter of the error |
| 500 | [Server error](/en/technical/errors): internal server error |





## Remove collection objects

	POST /api/v1/collection/remove/<id>

Remove certain objects from a collection

### Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

### Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

### Input

An array of "collection objects". `_webfrontend_props` is not used in this case.

### Output

The output is given as a map with the following parameters:

|   |   |
|---|---|
| `_version` | Collection version (integer) |
| `count`    | Number of objects in the collection (integer) |

### Permissions

The session must be authenticated and the user must own the collection of have
the `link` right for the objects that are added to it (filtered by object type or pool).

New objects are granted some rights through the collection ACL. The owner of the collection must have these rights
over the objects before the operation. Furhtermore, they must be grantable.

See [rights management](/en/technical/rightsmanagement).

### HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "link" right |
| 400 | [No Grantable Right](/en/technical/errors): the owner of the collection has no grantable right for the new objects |
| 400 | [Collection Not Found](/en/technical/errors): collection `id` not found |
| 400 | [Object Not Found](/en/technical/errors): object not found, the global object id is given as parameter of the error |
| 500 | [Server error](/en/technical/errors): internal server error |





## Splice collection objects

    POST /api/v1/collection/splice/<id>

Perform a splice operation with the collection objects.

A splice operation removes a given range of objects, and appends a given set of objects to the collection. The range can be specified by giving a starting **index** and a **count** of objects to be removed.

If no **index** is specified, no objects will be removed before new objects are appended. If **count** is not set, all objects from the start index are removed.

If **index** and **count** are not specified, no objects are removed.

### Handling of existing objects

If any of the new collection objects in **objects** are already in the collection, they will be moved from their current position in the collection to a new position at the end, according to the sorting of the appended objects.

### Path parameters

|   |   |
|---|---|
| `id` | Collection ID (integer) |

### Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

### Input

An object with the following properties:

|   |   |
|---|---|
| `index`   | Start position to remove items (integer, defaults to size of collection) |
| `count`   | Number of items to be removed (integer, defaults to all elements from start to end) |
| `objects` | Items to be added (array of "collection objects", defaults to an empty array) |

### Output

An object with the following properties

|   |   |
|---|---|
| `_version` | Collection version (integer) |
| `count`    | Number of elements in the collection (integer) |
| `objects`  | Removed items (array of strings): instead of "collection objects", this is a list of global object IDs |

### Permissions

The session must be authenticated and the user needs:

- the `link` right for the objects that are added to the collection (filtered by object type or pool)
- the `unlink` right for the objects that are removed from the collection (filtered by object type or pool)
- if the collection is owned by the user, `link` and `unlink` are not needed

New objects are granted some rights through the collection ACL. The owner of the collection must have these rights
over the objects before the operation. Furhtermore, they must be grantable.

See [rights management](/en/technical/rightsmanagement).

### HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "link" or "unlink" right |
| 400 | [No Grantable Right](/en/technical/errors): the owner of the collection has no grantable right for the new objects |
| 400 | [Collection Not Found](/en/technical/errors): collection `id` not found |
| 400 | [Object Not Found](/en/technical/errors): object not found, the global object id is given as parameter of the error |
| 500 | [Server error](/en/technical/errors): internal server error |

### Example

```javascript
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
