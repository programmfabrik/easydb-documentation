---
title: "58 - db"
menu:
  main:
    name: "db"
    identifier: "technical/api/db"
    parent: "technical/api"
---

{{< toc-en >}}

## Retrieve objects
    GET /api/v1/db/<objecttype>/<mask>/<id>?token=<token>[&version=<version>[&schemaversion=<schemaversion>]][&format=<format>][&skip_reverse_nested=<skip_reverse_nested>]
Object by object ID (`<objecttype>._id` field). One object in the resulting array.

    GET /api/v1/db/<objecttype>/<mask>/global_object_id/<id>?token=<token>[&version=<version>[&schemaversion=<schemaversion>]][&format=<format>][&skip_reverse_nested=<skip_reverse_nested>]
Object by global object ID (`_global_object_id` field): "local" is a valid alias for the server's instance. One object in the resulting array.

    GET /api/v1/db/<objecttype>/<mask>/system_object_id/<id>?token=<token>[&version=<version>[&schemaversion=<schemaversion>]][&format=<format>][&skip_reverse_nested=<skip_reverse_nested>]
Object by system object ID (`_system_object_id` field). One object in the resulting array.

    GET /api/v1/db/<objecttype>/<mask>/list?token=<token>[&limit=<limit>][&offset=<offset>][&version=<version>[&schemaversion=<schemaversion>]][&format=<format>][&skip_reverse_nested=<skip_reverse_nested>]
List of objects, sorted ascending by object IDs (length of array controlled by parameters `limit` and `offset`). Multiple objects in the resulting array.

### Path parameters

|   |   |
|---|---|
| `objecttype` | Object type (string) |
| `mask`       | Mask (string): can be a specific mask name or **\_all\_fields** (see [/api/v1/mask](/en/technical/api/mask)). |
| `id`         | Object ID (integer): get the object with the given **id**. |
| `limit`      | Maximal length of the list of objects (integer): if path specifies **list** instead of a single **id**, return not more than **limit** objects.<br>Default: `100`, Maximum: `1000` |
| `offset`     | Offset in the list of objects (integer): if path specifies **list** instead of a single **id**, return objects from this position in the database |
| `version`    | Object version (integer or **current**, optional): if set, get an archived version of the object(s). Requires an ID.<br>Defaults to the current object version. |
| `schema`     | Schema version (**current**, optional): if set to **current** the object version is rendered in the latest schema version. Defaults to the schema version that was used when the object version was created.<br>Any other value than **current** will cause an error. |
| `format`     | Object format (string): **short**, **standard**, **long** or **full** (default) |
| `skip_reverse_nested` | Do not export any reverse nested tables (optional): **1**, **y**, **yes** or **true** for `true` (default `false`) |

If the given `mask` does not exist in the schema for the given object version, an [Old Mask Missing](/en/technical/errors) error is returned.

If no schema for the given object `version` is found, an [Old Schema Missing](/en/technical/errors) error is returned.

### Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

### Output

Array of [objects](/en/technical/types/object) in the requested format.

### Permissions

The user needs the "read" right for the requested object and the "mask" right for the given mask
(see [rights management](/en/technical/rightsmanagement)).

In order to use the "\_all\_fields" mask, the user needs any of the following system rights: "system.root", "system.datamodel.development", "system.datamodel.commit".

### HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "read" or "mask" right (the error parameters explain which) |
| 400 | [No System Right](/en/technical/errors): no system right for "\_all\_fields" |
| 400 | [Objecttype Not Found](/en/technical/errors): `objecttype` not found |
| 400 | [Mask Not Found](/en/technical/errors): `mask` not found |
| 400 | [Object Not Found](/en/technical/errors): object `id` not found |
| 400 | [Instance Not Found](/en/technical/errors): instance not found (for requests with global object ID) |
| 400 | [Old Mask Missing](/en/technical/errors): the given `mask` does not exist in the given `schemaversion` |
| 500 | [Server error](/en/technical/errors): internal server error |

## Retrieve all versions of objects

    GET /api/v1/db/<objecttype>/_all_fields?token=<token>&all_versions=true[&limit=<limit>][&offset=<offset>]

Returns all versions of all objects of this type, not filtered by any mask.

### Path parameters

|   |   |
|---|---|
| `objecttype` | Object type (string) |

### Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `all_versions` | always `true` for this type of request, otherwise the usual retrieval of objects is done as shown above |
| `limit` | limit of objects (not versions) returned, defaults to `1000` |
| `offset` | offset of first object to retrieve, defaults to `0` |

### Output

Array of [objects](/en/technical/types/object) as above, ordered by object ID and version number. These differences to the single-version output exist:

* the newest version has a `_latest_version` marker set to `true`
* the comment given when creating the version is added as `_comment`
* there is a `_last_modified` timestamp for each version
* the ID of the user creating the version (creating or modifying the object) is present in `_create_user`
* the `_owner` field is simplified, no names but only ID of user or group is included (format and `_basetype` marker are kept compatible)
* there is no changelog

### Permissions

The system right `system.root` is required to use this request.

### HTTP status codes

See single-version object retrieval for possible HTTP status codes.

## Create or update objects
    POST/PUT /api/v1/db/<objecttype>?token=<token>[&confirm=<confirm>][&collection=<collection_id>][&priority=<priority>][&format=<format>][&base_fields_only=1][&progress_uuid=<progress_uuid>]

Creates or updates objects for the given `objecttype`.

Objects are stored in the order of appearance. Each object must specify a `_mask` to be used for reading
the object structure (see [Object type](/en/technical/types/object)). The **\_all\_fields** mask is accepted under certain conditions (see "Permissions").

With every mask change, a batch is send to the Importer.

New objects must have either the creator or any of the groups they belong to as owner (except for the special case **create in collection**).

**Group edit**: It is possible to edit a group of objects in such a way that all of them are
updated with the same data. In this mode, only one object is given in the input array, but the `_id` field
is an array containing the IDs of the objects to be updated. The `_version` is automatically updated by the server.

**Create in collection**: If the parameter `collection` is provided, only insertions are allowed. The collection parameters
define which objecttype, mask and pool are allowed for the objects (see [collection](/en/technical/types/collection)).
The objects will be created and inserted in the collection. The owner of the object will be the collection owner.

**Base fields only**: This is a special case in which no mask is provided. Only updates for pool and tags are allowed.

Notice: POST for masks with mask filters is not allowed.

### Path parameters

|   |   |
|---|---|
| `objecttype` | Object type (string) |

### Query String

|   |   |
|---|---|
| `token`      | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `confirm`    | Confirmation code (see below "Transitions") |
| `collection` | ID of the collection where the objects should be inserted |
| `collection_rights_policy` | What to do if the operation causes the owner of a collection to lose grantable rights over collection objects (see [rightsmanagement](/en/technical/rightsmanagement)) |
| `priority`   | Priority for the indexer (integer): possible values are:
|              | **-1** very low priority, doesn't generate an `OBJECT_INDEX` event |
|              | **0** (default): low priority, typically used by non-interactive clients, such as the migration tool |
|              | **1**: normal priority, used to signal user interaction |
|              | **2**: high priority, used when a specially fast response is expected |
| `format`     | Object format for the result objects (string): **short** (default), **standard**, **long** or **full** |
| `base_fields_only` | If set to "1", use "base fields only" mode |
| `progress_uuid` | If this variable is set, API_PROGRESS events will be generated during the operation, the `progress_uuid` can then be used to match the events to the operation |

### Input

Array of [objects](/en/technical/types/object). The following restrictions apply:

- `_id` must be set for POST and must be not set for PUT. It is an array in the group edit mode.
- `_version` must be 1 (PUT) or the current version plus one (POST).
- `<object-type.name>._pool.pool.id` can be set, but other properties of `<object-type.name>._pool.pool` are read-only.
- the rules for user-defined attributes depend on the object type and the `_mask`.
- other attributes are read-only.
- an object cannot be linked to the root pool, either on creation or update

> `_id` and `_id_parent` can be set using a lookup feature, which selects the object using a reference column. More information about this feature can be found in the [Lookups for IDs](/en/technical/datamanagement/lookups/) documentation.

#### Creation or regular update

The object is updated as a whole. That means that if the user only wants to change the value of a certain field,
all other fields must be sent with their current values. Exceptions to this rule are:

- `_acl` - the user can leave the `_acl` as-is by not specifying it (no `_acl` entry) or setting it to **null**. To delete an `_acl` an empty array ([]) is needed
- `_owner` may be left out when creating an object

When creating an object, the owner must be the user that creates it. If `_owner` is left out, Easydb will fill this value.
When using the `collection` parameter, the owner is automatically set to the owner of the collection.

#### Group edit

In group edit mode, only the given fields will be updated. Special instructions can be specified for lists:

**Nested objects**

If a nested field `<field>` is updated, the API expects a silbling string attribute `<field>:group_mode`, which can
have the following values:

| Nested group edit mode | Meaning |
|------------------------|-------|
| **append**             | Add the new list to the end of the old one |
| **prepend**            | Add the new list to the beginning of the old one |
| **replace**            | Replace the old list with the new one |
| **remove**             | Remove the elements of the given list from the old list |

**Tags**

If the `_tags` are updated, the API expects a silbling string attribute `_tags:group_mode`, which can
have the following values:

| Nested group edit mode | Meaning |
|------------------------|-------|
| **tag_add**            | Add the new tags, if they do not already exist. If a tag from a "choice" tag group is added, it will replace the old tag for that group, if it was set |
| **tag_replace**        | Replace the old tags with the new ones |
| **tag_remove**         | Remove the tags provided |
| **tag_remove_all**     | Remove all tags |

The mode **tag_remove_all** can be specified without `_tags` (if specified, they will be ignored).

**ACL**

If the `_acl` is updated, the API expects a silbling string attribute `_acl:group_mode`, which can
have the following values:

| Nested group edit mode | Meaning |
|------------------------|-------|
| **acl_add**            | Add the new ACL entries, if they do not already exist |
|                        | If the `who` attribute is empty, its `rights` will be appended to all existing ACL entries |
|                        | If a `right_preset` is provided, `who` must be set |
| **acl_replace**        | Replace the old ACL with the new ones |
|                        | If the `who` attribute is empty, replace the `rights` in all existing ACL entries |
|                        | If a `right_preset` is provided, `who` must be set |
| **acl_remove**         | Remove the provided ACL |
|                        | If the `who` attribute is empty, remove `rights` from all existing ACL entries. This is not valid in combination with a right preset |
|                        | If the `rights` attribute is empty, remove all rights for the provided `who`. This is not valid in combination with a right preset |
| **tag_remove_all**     | Remove complete ACL |

The mode **acl_remove_all** can be specified without `_acl` (if specified, it will be ignored).

### Output

If the request is a group edit or "base fields only", the response body will be empty. Otherwise, it is an array of [objects](/en/technical/types/object) in the requested format.

### Permissions

The user needs the following rights at the beginning of the operation (see [rights management](/en/technical/rightsmanagement)):

- "create", if it is a new object
    - if `collection` was set, "create\_in\_collection" for the collection is required
- "write", if it is an existing object
- "mask", for the given mask
    - if `collection` was set, this is not required (the allowed mask is controlled via collection configuration)
- "acl", if `_acl` is specified
- "change\_owner", if the `_owner` is changed (only when updating an object)
- if the user changes the pool of the object:
    - "link" for the new pool
    - "unlink" for the old pool

Transitions are checked (see [transitions](/en/technical/transitions)). If any transition needs confirmation,
the call will return a confirmation response (see below "HTTP status codes").
The code provided in the confirmation response should be passed as parameter (`confirm`) when repeating the call.

If the transitions change the tags of the object, the rights are checked again. The user is not
allowed to lose them at this point.

The user needs the following rights at the end of the operation:

- "mask", for the given mask
- "read"
- "acl", if `_acl` and/or `_private_acl` was specified

In order to use the "\_all\_fields" mask, the user needs any of the following system rights: "system.root", "system.datamodel.development", "system.datamodel.commit".

If the parameter `collection` is set, the owner of the collection must have the rights granted by the collection to the created objects
before they are inserted. Furthermore, they must be grantable. Otherwise, an error is returned.

The root pool is never allowed.

### Example


{{< include_json "./post.json" >}}


### HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 202 | [Confirmation Response (transitions)](/en/technical/confirmation): the operation requires confirmation for one of several transitions |
| 202 | [Confirmation Response (collection owner rights revoked)](/en/technical/confirmation): the operation requires confirmation with a `collection_rights_policy` |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [No Mask Defined For Collection](/en/technical/errors): no mask defined for the collection provided (`collection`) |
| 400 | [No Pool Defined For Collection](/en/technical/errors): no pool defined for the collection provided (`collection`) |
| 400 | [Bad Objecttype For Collection](/en/technical/errors): wrong objecttype when creating in a collection (the parameter "expected_objecttype_id" tells which is the expected one) |
| 400 | [Bad Mask For Collection](/en/technical/errors): wrong mask when creating in a collection (the parameter "expected_mask_id" tells which is the expected one) |
| 400 | [Bad Pool For Collection](/en/technical/errors): wrong pool when creating in a collection (the parameter "expected_pool_id" tells which is the expected one) |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "create", "create_in_collection", "write" or "mask" right (the error parameters explain which) |
| 400 | [Insufficient Rights After Transition](/en/technical/errors): no "read", "write" or "mask" right (the error parameters explain which) |
| 400 | [Rights Revoked](/en/technical/errors): no "read", "write" or "mask" right (the error parameters explain which) |
| 400 | [Transition Reject](/en/technical/errors): the operation was rejected by a transition |
| 400 | [Bad Confirm Code](/en/technical/errors): the given `confirm` code is incorrect |
| 400 | [Change Owner On Creation](/en/technical/errors): the user attempted to set a different user as owner when creating an object |
| 400 | [Invalid Owner On Creation](/en/technical/errors): the user attempted to set an invalid owner  when creating an object |
| 400 | [No Grantable Right](/en/technical/errors): the owner of the collection has no grantable right for the objects |
| 400 | [Objecttype Not Found](/en/technical/errors): `objecttype` not found |
| 400 | [Mask Not Found](/en/technical/errors): `mask` not found |
| 400 | [Object Not Found](/en/technical/errors): object `id` not found |
| 400 | [Version Mismatch](/en/technical/errors): the given `_version` is not correct |
| 400 | [Object Owner Null](/en/technical/errors): no owner was provided when updating an object |
| 400 | [Integrity Constraint Violation](/en/technical/errors): the operation violates an integrity constraint (the error specifies which) |
| 400 | [Check Constraint Violation](/en/technical/errors): the operation violates an integrity constraint (the error specifies which) |
| 400 | [Foreign Key Constraint Violation](/en/technical/errors): the operation violates a foreign key (the error specifies which) |
| 400 | [Bad Mask For Update](/en/technical/errors): a mask with mask filter was provided |
| 400 | [Link Root Pool](/en/technical/errors): the root pool was provided |
| 500 | [Server error](/en/technical/errors): internal server error |





## Delete objects

    DELETE /api/v1/db/<objecttype>?token=<token>[&confirm=<confirm>][&priority=<priority>]

Deletes one or more objects from the database.

*Hierarchical objects:*
Deleting a hierarchical object automatically results in the deletion of all dependent objects.

*Linked objects:*
Attempting to delete an object which is referenced from another object results in an error (HTTP code 409).

### Path parameters

|   |   |
|---|---|
| `objecttype` | Object type (string) |

### Query String

|   |   |
|---|---|
| `token`    | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `confirm`  | Confirmation code (see below "Transitions") |
| `priority` | Priority for the indexer (integer): see "POST" above |

### Input

An array of tuples `(ID, version[, comment])`. `comment` is optional and may be omitted.


[
  [ 123, 4, "useless..." ],
  [ 124, 5, "replaced by 'Test 3'" ],
  [ 126, 3 ]
]


### Permissions

The user needs the "delete" right for the requested objects (see [rights management](/en/technical/rightsmanagement)).

Transitions are also checked (see [transitions](/en/technical/transitions)). If
transitions need confirmation, the `confirm` parameter should be provided.

### HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 202 | [Confirmation Response (transitions)](/en/technical/confirmation): the operation requires confirmation for one of several transitions |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [Insufficient Rights](/en/technical/errors): no "delete" right |
| 400 | [Insufficient Rights After Transition](/en/technical/errors): no "delete" right |
| 400 | [Transition Check Failed](/en/technical/errors): the transitions check failed |
| 400 | [Bad Confirm Code](/en/technical/errors): the given `confirm` code is incorrect |
| 400 | [Objecttype Not Found](/en/technical/errors): `objecttype` not found |
| 400 | [Object Not Found](/en/technical/errors): object `id` not found |
| 400 | [Version Mismatch](/en/technical/errors): the given `_version` is not correct |
| 400 | [Foreign Key Constraint Violation](/en/technical/errors): the operation violates a foreign key (the error specifies which) |
| 500 | [Server error](/en/technical/errors): internal server error |
