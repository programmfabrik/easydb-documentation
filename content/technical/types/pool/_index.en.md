---
title: "133 - Pool"
menu:
  main:
    name: "Pool"
    identifier: "technical/types/pool"
    parent: "technical/types"
---
# Pool

A pool is a container for objects. Only objects from an object type with "pool management" are
stored in pools, and they have to be in exactly one pool. The pool can be used to:

- manage object rights using ACLs, tags and transitions
- set a watermark for its objects
- set standard masks for its objects

The pools build a hierarchy, which is represented by the relation `pool._id_parent` in the pool
object. When searching pools, easydb offers special attributes relating to the pool hierarchy
(`_has_children`, `_level` and `_path`).

Easydb creates automatically some "system pools". These pools cannot be deleted or moved in the pool
hierarchy (that is, change their `_id_parent`).

There are different formats to present a pool: full, full search, short and short search.

## <a name="full"></a> Full format

This format is used by [/api/pool](/en/technical/api/pool) and contains all attributes that can be set for a pool.
It is intended for administrators and is managed by the right `bag_write`.

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `_basetype`                 | Name of the base type (string, r): **pool**                                                               |
| `_acl`                      | ACL (array of [acl entries](/en/technical/types/acl_entry), rw, optional)                                         |
| `_private_acl`              | Marks the ACL as private (see [rights management](/en/technical/rightsmanagement)) (bool, rw, optional): defaults to **false** |
| `_standard_masks`           | ordered list of masks per objecttype for objects in this pool (object mapping objecttype ids to list of mask ids, e.g. `{"12": [14, 1, 2], "13": [3, 4]}`, optional): ref. [objecttype](/en/technical/types/objecttype).\_id, [mask](/en/technical/types/maskset).mask\_id. If set to **null**, the list is derived from the objecttype.  |
| `_tags`                     | Tags (array of [tag entries](/en/technical/types/tag_entry), rw, optional)                                        |
| `_compiled_tags`            | Compiled tags for objects in this pool (array of [tag entries](/en/technical/types/tag_entry)), r)                |
| `_private_tags`             | Marks the tags as private (bool, rw, optional): defaults to **false**                                     |
| `_transitions`              | Transitions (array of [transitions](/en/technical/types/transition), rw, optional)                                |
| `_private_transitions`      | Private transitions flag (bool, rw, optional): defaults to **false**                                      |
| `_has_children`             | Whether this pool has nested pools (boolean, r)                                                           |
| `_generated_rights`         | Rights that the session user has for the pool ([rights specification](/en/technical/types/right)): bag_read, bag_write, bag_delete, bag_acl, bag_create |
| `_set_spec`                 | OAI/PMH name for this set |
| `pool`                      | Pool attributes:                                                                                          |
| &#8614; `_id`               | Pool ID (integer, unique, r\*)                                                                            |
| &#8614; `lookup:_id`        | [Lookup for pool ID](/en/technical/datamanagement/lookups/#pools)                                         |
| &#8614; `_id_parent`        | Parent pool ID (integer, rw)                                                                              |
| &#8614; `lookup:_id_parent` | [Lookup for ID of parent pool](/en/technical/datamanagement/lookups/#pools)                               |
| &#8614; `_version`          | Pool version (integer, rw)                                                                                |
| &#8614; `is_system_pool`    | Whether this is a system pool (boolean, r)                                                                |
| &#8614; `name`              | Pool name ([l10n](/en/technical/types/l10n), unique for pools with the same parent, rw)                           |
| &#8614; `description`       | Pool description ([l10n](/en/technical/types/l10n), optional, rw)                                                 |
| &#8614; `watermark`         | Watermark to apply to the objects of this pool ([watermark](/en/technical/types/watermark), optional, rw)         |
| &#8614; `contact`           | Contact ([user (contact)](/en/technical/types/user), optional, rw)                                        |
| &#8614; `mapping_image_export`     | Export mapping image to be used for this pool (integer/string, optional, rw): either an ID or one of the following: "parent", "objecttype", "none" |
| &#8614; `mapping_image_import`     | Import mapping image to be used for this pool (integer/string, optional, rw): either an ID or one of the following: "parent", "objecttype", "none" |
| &#8614; `mapping_dc_export`        | Dublin Core mapping to be used for this pool (integer/string, optional, rw): either an ID or one of the following: "parent", "objecttype", "none" |
| &#8614; `custom_data`       | Custom JSON data, can contain any additional data for this pool (JSON object, optional, rw) |
| &#8614; `reference`         | Pool reference (string, unique, optional, rw): can be used for lookups for `_id` and `_id:parent`                            |
| &#8614; `shortname`         | Pool short name (string, unique, optional, rw): can be used for lookups for `_id` and `_id:parent`                                 |
| &#8614; `created_timestamp`      | timestamp of creation of this pool (timestamp, r) |
| &#8614; `last_updated_timestamp` | timestamp of the last update of this pool (timestamp, r) |

### Remarks:

- `_id` has to be set for POST operations
- for the meaning of `_tags`, `_private_tags` and `_compiled_tags`, see [tag management](/en/technical/tagmanagement)
- the field `_private_acl` is not available for the root pool
- for each objecttype, if `_standard_masks` contains a subset of all masks, only these will be indexed

Notice that all pools must have a valid `_id_parent` (except for the root pool, which is a system pool).

## <a name="full_search"></a> Full search format

This format is used when searching pools. The column "Search" specifies the search type that can be used (see [/api/search](/en/technical/api/search)).
For fields that are already present in the full format a description is not provided.
This format is intended for all users when they need to view or choose a pool and is managed by the right `bag_read`.

| Name                        | Description                                                                                               | Search        |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|---------------|
| `_basetype`                 |                                                                                                           |               |
| `_has_children`             |                                                                                                           |               |
| `_has_acl`                  | Whether this pool has a non-empty ACL (boolean, r)                                                        | Boolean       |
| `_level`                    | Level of this pool in the hierarchy (integer, r)                                                          | Number        |
| `_path`                     | Path to this pool (array of pools (short), r): from top level to this pool, including it                  | Number (`_path.pool._id`) |
| `pool`                      |                                                                                                           |               |
| &#8614; `_id`               |                                                                                                           | Number        |
| &#8614; `_id_parent`        |                                                                                                           | Number        |
| &#8614; `_version`          |                                                                                                           | Number        |
| &#8614; `is_system_pool`    |                                                                                                           | Boolean       |
| &#8614; `name`              |                                                                                                           | L10n (all)    |
| &#8614; `shortname`         |                                                                                                           | NonAnalyzed   |
| &#8614; `description`       |                                                                                                           | L10n (all)    |
| &#8614; `contact`           |                                                                                                           |               |
| &#8614; `mapping_image`     |                                                                                                           |               |

## <a name="short"></a> Short format

The short format is used to render pools inside user objects and other pools.
If the attribute referencing this pool is marked as writable, `pool._id` is writable. The other fields are readable-only.

It contains the following attributes:

| Name                             | |
|----------------------------------|---|
| `_basetype`                      | |
| `_path` (pools in short format)  | |
| `pool`                           | |
| &#8614; `_id`                    | |
| &#8614; `_id_parent`             | |
| &#8614; `name`                   | |

The pools inside `_path` do not have a `_path` themselves.

## <a name="short_search"></a> Short search format

This format is used when searching objects using the fields of their linked pools.
The column "Search" specifies the search type that can be used (see [/api/search](/en/technical/api/search)).
For fields that are already present in the short or full search format a description is not provided.

| Name                             | Description | Search        |
|----------------------------------|-------------|---------------|
| `_basetype`                      |             |               |
| `_level`                         |             | Number        |
| `_path` (pools in short format)  |             | Number (`_path.pool._id`) |
| `pool`                           |             |               |
| &#8614; `_id`                    |             | Number        |
| &#8614; `_id_parent`             |             | Number        |
| &#8614; `_version`               |             | Number        |
| &#8614; `name`                   |             | L10n          |

The pools inside `_path` do not have a `_path` themselves.

## System pools

| 					|			 |
|-----------------------|-------------------------------------|
| **Root pool**		| used as the root pool in the hierarchy |
| **Standard pool**     | standard pool |

## Related operations

- [/pool](/en/technical/api/pool): CRUD operations on pools
- [/db](/en/technical/api/db): read and update pool of an object
- [/search](/en/technical/api/search): Search types "pool" and "pool_management"

