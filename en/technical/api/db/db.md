# Retrieve objects
    (1) GET /api/v1/db/<objecttype>/<mask>/<id>?token=<token>[&version=<version>[&schemaversion=<schemaversion>]][&format=<format>]
    (2) GET /api/v1/db/<objecttype>/<mask>/global_object_id/<id>?token=<token>[&version=<version>[&schemaversion=<schemaversion>]][&format=<format>]
    (3) GET /api/v1/db/<objecttype>/<mask>/system_object_id/<id>?token=<token>[&version=<version>[&schemaversion=<schemaversion>]][&format=<format>]

Retrieves an object from the database by:

(1) object ID (`<objecttype>._id` field)
(2) global object ID (`_global_object_id` field): "local" is a valid alias for the server's instance
(3) system object ID (`_system_object_id` field)

## Path parameters

|   |   |
|---|---|
| `objecttype`    | Object type (string) |
| `mask`          | Mask (string): can be a specific mask name or **\_all\_fields** (see [/api/v1/mask](/technical/api/mask/mask.md)). |
| `id`            | Object ID (integer): get the object with the given **id**. |
| `version`       | Object version (integer or **current**, optional): if set, get an archived version of the object(s). Requires an ID.<br>Defaults to the current object version. |
| `schema`        | Schema version (**current**, optional): if set to **current** the object version is rendered in the latest schema version. Defaults to the schema version that was used when the object version was created.<br>Any other value than **current** will cause an error. |
| `format`        | Object format (string): **short**, **standard**, **long** or **full** (default) |

If the given `mask` does not exist in the schema for the given object version, an [Old Mask Missing](/technical/errors/errors.md#old_mask_missing) error is returned.

If no schema for the given object `version` is found, an [Old Schema Missing](/technical/errors/errors.md#old_schema_missing) error is returned.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Output

Array of [objects](/technical/types/object/object.md) in the requested format.

## Permissions

The user needs the "read" right for the requested object and the "mask" right for the given mask
(see [rights management](/technical/rightsmanagement/rightsmanagement.md)).

In order to use the "\_all\_fields" mask, the user needs any of the following system rights: "system.root", "system.datamodel.development", "system.datamodel.commit".

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Insufficient Rights](/technical/errors/errors.md#insufficient_rights): no "read" or "mask" right (the error parameters explain which) |
| 400 | [No System Right](/technical/errors/errors.md#no_system_right): no system right for "\_all\_fields" |
| 400 | [Objecttype Not Found](/technical/errors/errors.md#objecttype_not_found): `objecttype` not found |
| 400 | [Mask Not Found](/technical/errors/errors.md#mask_not_found): `mask` not found |
| 400 | [Object Not Found](/technical/errors/errors.md#object_not_found): object `id` not found |
| 400 | [Instance Not Found](/technical/errors/errors.md#instance_not_found): instance not found (for requests with global object ID) |
| 400 | [Old Mask Missing](/technical/errors/errors.md#old_mask_missing): the given `mask` does not exist in the given `schemaversion` |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |





# Create or update objects
    POST/PUT /api/v1/db/<objecttype>?token=<token>[&confirm=<confirm>][&collection=<collection_id>][&priority=<priority>][&format=<format>][&base_fields_only=1][&progress_uuid=<progress_uuid>]

Creates or updates objects for the given `objecttype`.

Objects are stored in the order of appearance. Each object must specify a `_mask` to be used for reading
the object structure (see [Object type](/technical/types/object/object.md)). The **\_all\_fields** mask is accepted under certain conditions (see "Permissions").

With every mask change, a batch is send to the Importer.

New objects must have either the creator or any of the groups they belong to as owner (except for the special case **create in collection**).

**Group edit**: It is possible to edit a group of objects in such a way that all of them are
updated with the same data. In this mode, only one object is given in the input array, but the `_id` field
is an array containing the IDs of the objects to be updated. The `_version` is automatically updated by the server.

**Create in collection**: If the parameter `collection` is provided, only insertions are allowed. The collection parameters
define which objecttype, mask and pool are allowed for the objects (see [collection](/doc/types/collection/collection.md)).
The objects will be created and inserted in the collection. The owner of the object will be the collection owner.

**Base fields only**: This is a special case in which no mask is provided. Only updates for pool and tags are allowed.

Notice: POST for masks with mask filters is not allowed.

## Path parameters

|   |   |
|---|---|
| `objecttype` | Object type (string) |

## Query String

|   |   |
|---|---|
| `token`      | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |
| `confirm`    | Confirmation code (see below "Transitions") |
| `collection` | ID of the collection where the objects should be inserted |
| `collection_rights_policy` | What to do if the operation causes the owner of a collection to lose grantable rights over collection objects (see [rightsmanagement](/technical/rightsmanagement/rightsmanagement.md#collection_rights_policy)) |
| `priority`   | Priority for the indexer (integer): possible values are:
|              | **-1** very low priority, doesn't generate an `OBJECT_INDEX` event |
|              | **0** (default): low priority, typically used by non-interactive clients, such as the migration tool |
|              | **1**: normal priority, used to signal user interaction |
|              | **2**: high priority, used when a specially fast response is expected |
| `format`     | Object format for the result objects (string): **short** (default), **standard**, **long** or **full** |
| `base_fields_only` | If set to "1", use "base fields only" mode |
| `progress_uuid` | If this variable is set, API_PROGRESS events will be generated during the operation, the `progress_uuid` can then be used to match the events to the operation |

## Input

Array of [objects](/technical/types/object/object.md). The following restrictions apply:

- `_id` must be set for POST and must be not set for PUT. It is an array in the group edit mode.
- `_version` must be 1 (PUT) or the current version plus one (POST).
- `<object-type.name>._pool.pool.id` can be set, but other properties of `<object-type.name>._pool.pool` are read-only.
- the rules for user-defined attributes depend on the object type and the `_mask`.
- other attributes are read-only.
- an object cannot be linked to the root pool, either on creation or update

### Creation or regular update

The object is updated as a whole. That means that if the user only wants to change the value of a certain field,
all other fields must be sent with their current values. Exceptions to this rule are:

- `_acl` - the user can leave the `_acl` as-is by not specifying it (no `_acl` entry) or setting it to **null**. To delete an `_acl` an empty array ([]) is needed
- `_owner` may be left out when creating an object

When creating an object, the owner must be the user that creates it. If `_owner` is left out, Easydb will fill this value.
When using the `collection` parameter, the owner is automatically set to the owner of the collection.

### Group edit

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

## Output

If the request is a group edit or "base fields only", the response body will be empty. Otherwise, it is an array of [objects](/technical/types/object/object.md) in the requested format.

## Permissions

The user needs the following rights at the beginning of the operation (see [rights management](/technical/rightsmanagement/rightsmanagement.md)):

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

Transitions are checked (see [transitions](/technical/transitions/transitions.md)). If any transition needs confirmation,
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

## Example

~~~~json
@@include:post.json@@
~~~~

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 202 | [Confirmation Response (transitions)](/technical/confirmation/confirmation.md#transitions): the operation requires confirmation for one of several transitions |
| 202 | [Confirmation Response (collection owner rights revoked)](/technical/confirmation/confirmation.md#corr): the operation requires confirmation with a `collection_rights_policy` |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [No Mask Defined For Collection](/technical/errors/errors.md#no_mask_defined_for_collection): no mask defined for the collection provided (`collection`) |
| 400 | [No Pool Defined For Collection](/technical/errors/errors.md#no_pool_defined_for_collection): no pool defined for the collection provided (`collection`) |
| 400 | [Bad Objecttype For Collection](/technical/errors/errors.md#bad_objecttype_for_collection): wrong objecttype when creating in a collection (the parameter "expected_objecttype_id" tells which is the expected one) |
| 400 | [Bad Mask For Collection](/technical/errors/errors.md#bad_mask_for_collection): wrong mask when creating in a collection (the parameter "expected_mask_id" tells which is the expected one) |
| 400 | [Bad Pool For Collection](/technical/errors/errors.md#bad_pool_for_collection): wrong pool when creating in a collection (the parameter "expected_pool_id" tells which is the expected one) |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Insufficient Rights](/technical/errors/errors.md#insufficient_rights): no "create", "create_in_collection", "write" or "mask" right (the error parameters explain which) |
| 400 | [Insufficient Rights After Transition](/technical/errors/errors.md#insufficient_rights_after_transition): no "read", "write" or "mask" right (the error parameters explain which) |
| 400 | [Rights Revoked](/technical/errors/errors.md#rights_revoked): no "read", "write" or "mask" right (the error parameters explain which) |
| 400 | [Transition Reject](/technical/errors/errors.md#transition_reject): the operation was rejected by a transition |
| 400 | [Bad Confirm Code](/technical/errors/errors.md#bad_confirm_code): the given `confirm` code is incorrect |
| 400 | [Change Owner On Creation](/technical/errors/errors.md#change_owner_on_creation): the user attempted to set a different user as owner when creating an object |
| 400 | [Invalid Owner On Creation](/technical/errors/errors.md#invalid_owner_on_creation): the user attempted to set an invalid owner  when creating an object |
| 400 | [No Grantable Right](/technical/errors/errors.md#no_grantable_right): the owner of the collection has no grantable right for the objects |
| 400 | [Objecttype Not Found](/technical/errors/errors.md#objecttype_not_found): `objecttype` not found |
| 400 | [Mask Not Found](/technical/errors/errors.md#mask_not_found): `mask` not found |
| 400 | [Object Not Found](/technical/errors/errors.md#object_not_found): object `id` not found |
| 400 | [Version Mismatch](/technical/errors/errors.md#version_mismatch): the given `_version` is not correct |
| 400 | [Object Owner Null](/technical/errors/errors.md#object_owner_null): no owner was provided when updating an object |
| 400 | [Integrity Constraint Violation](/technical/errors/errors.md#integrity_constraint_violation): the operation violates an integrity constraint (the error specifies which) |
| 400 | [Check Constraint Violation](/technical/errors/errors.md#check_constraint_violation): the operation violates an integrity constraint (the error specifies which) |
| 400 | [Foreign Key Constraint Violation](/technical/errors/errors.md#foreign_key_constraint_violation): the operation violates a foreign key (the error specifies which) |
| 400 | [Bad Mask For Update](/technical/errors/errors.md#bad_mask_for_update): a mask with mask filter was provided |
| 400 | [Link Root Pool](/technical/errors/errors.md#link_root_pool): the root pool was provided |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |





# Delete objects

    DELETE /api/v1/db/<objecttype>?token=<token>[&confirm=<confirm>][&priority=<priority>]

Deletes one or more objects from the database.

*Hierarchical objects:*
Deleting a hierarchical object automatically results in the deletion of all dependent objects.

*Linked objects:*
Attempting to delete an object which is referenced from another object results in an error (HTTP code 409).

## Path parameters

|   |   |
|---|---|
| `objecttype` | Object type (string) |

## Query String

|   |   |
|---|---|
| `token`    | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |
| `confirm`  | Confirmation code (see below "Transitions") |
| `priority` | Priority for the indexer (integer): see "POST" above |

## Input

An array of tuples `(ID, version[, comment])`. `comment` is optional and may be omitted.

~~~~json
[
  [ 123, 4, "useless..." ],
  [ 124, 5, "replaced by 'Test 3'" ],
  [ 126, 3 ]
]
~~~~

## Permissions

The user needs the "delete" right for the requested objects (see [rights management](/technical/rightsmanagement/rightsmanagement.md)).

Transitions are also checked (see [transitions](/technical/transitions/transitions.md)). If
transitions need confirmation, the `confirm` parameter should be provided.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 202 | [Confirmation Response (transitions)](/technical/confirmation/confirmation.md#transitions): the operation requires confirmation for one of several transitions |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Insufficient Rights](/technical/errors/errors.md#insufficient_rights): no "delete" right |
| 400 | [Insufficient Rights After Transition](/technical/errors/errors.md#insufficient_rights_after_transition): no "delete" right |
| 400 | [Transition Check Failed](/technical/errors/errors.md#transition_check_failed): the transitions check failed |
| 400 | [Bad Confirm Code](/technical/errors/errors.md#bad_confirm_code): the given `confirm` code is incorrect |
| 400 | [Objecttype Not Found](/technical/errors/errors.md#objecttype_not_found): `objecttype` not found |
| 400 | [Object Not Found](/technical/errors/errors.md#object_not_found): object `id` not found |
| 400 | [Version Mismatch](/technical/errors/errors.md#version_mismatch): the given `_version` is not correct |
| 400 | [Foreign Key Constraint Violation](/technical/errors/errors.md#foreign_key_constraint_violation): the operation violates a foreign key (the error specifies which) |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |
