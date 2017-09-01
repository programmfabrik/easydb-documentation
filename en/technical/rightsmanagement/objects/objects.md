# Rights management for objects

These rights affect the manipulation and visibility of user-defined objects. Notice that object ownership also affects
rights management.

## Realms

The rights management for [objects](/technical/types/object/object.md) consists of multiple levels or realms:

* objecttype-without-pool
* tag
* pool
* collection
* object

### Objecttype Without Pool

An ACL can be specified for an [objecttype](/technical/types/objecttype/objecttype.md) (attribute `_acl`).
All objects from that objecttype will gain the rights assigned in that ACL.
There is no inheritance between Objecttype-ACLs. Objecttypes are independent from each other.

You cannot assign rights directly through objecttypes with a pool link. Instead, the pool hierarchy
can be used. If you wish to assign a right for all objects of an objecttype with pool link, assign them
at the root pool for that objecttype.

### Tag

An ACL can be specified for a [tag](/technical/types/tag/tag.md#tag) (attribute `_acl`).
All objects that have that tag attached (via `_tags`) will gain the rights assigned in that ACL.
There is no inheritance between Tag-ACLs. Tags are independent from each other.

### Pool

An ACL can be specified for a [pool](/technical/types/pool/pool.md) (attribute `_acl`). Pools also inherit all ACL from all their ancestors.
However, if a Pool has the `_private_acl` flag set, the ACL to that pool is private and only
`sticky` [ACL entries](/technical/types/acl_entry/acl_entry.md) from their ancestors are inherited.
An invisible Root-Pool is created as a top-level-node holding a master ACL.

All objects in a pool will gain the rights that result from this procedure.

### Collection

Collections inherit all ACL from all their parents.

However, if a Collection has the `_private_acl` flag set (see [collection](/technical/types/collection/collection.md)),
the ACL to that Collection is private and only sticky ACLs from all their parents are inherited.

An invisible Root-Collection is created as a top-level-node holding a master ACL.

All objects in a collection will gain the rights that result from this procedure.

Furthermore, objects inside a collection require that the Owner of the collection has all necessary *grantable*
rights which are in the ACL of the Collection at any time.

> <a name="collection_rights_policy"></a> When rights for the Owner of Collections are withdrawn, the respective /api/objecttype, /api/tag, /api/pool or /api/db
request can be refused by the server to get additional confirmation from the user. The server then offers a
choice to the user: "remove_acl" removes affected ACLs from affected Collections, "remove_objects" removes the objects affected by this change.

### Object

An ACL can be specified for a specific [object](/technical/types/object/object.md) (attribute `_acl`) if the objecttype is configured in the user [schema](/technical/types/schema/schema.md) with the flag `acl_table` set.

Objects whose objecttype is hierarchical inherit all ACL from all their parents.

However, if an Object has the `_private_acl` flag set (see [object](/technical/types/object/object.md)),
the ACL to that Object is private and only sticky ACLs from all their parents are inherited.

## Rights

Note: "Parameters" contains a list fo parameters specified as `<parameter-name> (<parameter-type>)`. If a parameter is optional, its
name will be enclosed in square brackets.

| Right                 | Parameters                         | Realm                   | Grantable in collection | Description |
|-----------------------|------------------------------------|-------------------------|-------------------------|-------------|
|`read`                 | -                                  | object                  | yes | Object can be read (and searched) |
|`read`                 | -                                  | objecttype-without-pool | yes | Objects of this Objecttype can be read (and searched) |
|`read`                 | objecttype_ids (objecttype-select) | pool                    | yes | Objects from the given objecttypes in this Pool can be read (and searched) |
|`read`                 | -                                  | collection              | yes | Objects in this collection can be read (and searched) |
|`read`                 | -                                  | tag                     | yes | Objects with this tag can be read (and searched) |
|`write`                | -                                  | object                  | yes | Object can be written |
|`write`                | -                                  | objecttype-without-pool | yes | Objects of this objecttype can be written |
|`write`                | objecttype_ids (objecttype-select) | pool                    | yes | Objects from the given objecttypes in this pool can be written |
|`write`                | -                                  | collection              | yes | Objects in this collection can be written |
|`write`                | -                                  | tag                     | yes | Objects with this tag can be written |
|`delete`               | -                                  | object                  | yes | Object can be deleted |
|`delete`               | -                                  | objecttype-without-pool | yes | Objects of this Objecttype can be deleted |
|`delete`               | objecttype_ids (objecttype-select) | pool                    | yes | Objects from the given objecttypes in this Pool can be deleted |
|`delete`               | -                                  | tag                     | yes | Objects with this tag can be deleted |
|`delete`               | -                                  | collection              | yes | Objects in this collection can be deleted |
|`mask`                 | mask ids (mask-select)             | pool                    | no  | Masks that can be used, by objecttype |
|`mask`                 | mask ids (mask-select)             | objecttype-without-pool | no  | Masks that can be used (only the target objecttype is allowed to be present) |
|`acl`                  | -                                  | objecttype-without-pool | no  | ACL of objects of this objecttype can be changed |
|`acl`                  | -                                  | tag                     | no  | ACL of objects with this tag can be changed |
|`acl`                  | objecttype_ids (objecttype-select) | pool                    | no  | ACL of objects of this objecttype in this pool can be changed |
|`create`               | -                                  | objecttype-without-pool | no  | Objects of this Objecttype can be created |
|`create`               | objecttype_ids (objecttype-select) | pool                    | no  | Objects can be created inside the Pool for the allowed Objecttypes |
|`create_in_collection` | -                                  | collection              | no  | Objects can be created in the collection for the default objecttype-mask-pool combination for that collection (see [collection](/technical/types/collection/collection.md)) |
|`change_owner`         | -                                  | objecttype-without-pool | no  | Owner can be changed for the objects of this Objecttype |
|`change_owner`         | objecttype_ids (objecttype-select) | pool                    | no  | Owner can be changed for the objects of the given Objecttypes in this Pool |
|`link`                 | objecttype_ids (objecttype-select) | pool                    | no  | Objects from the given objecttypes can be linked to this pool |
|`link`                 | objecttype_ids (objecttype-select) | collection              | no  | Objects from the given objecttypes and/or pools can be linked to this collection |
|                       | pool_ids (pool-select)             |                         |     | |
|`unlink`               | objecttype_ids (objecttype-select) | pool                    | no  | Objects from the given objecttypes can be unlinked from this pool |
|`unlink`               | objecttype_ids (objecttype-select) | collection              | no  | Objects from the given objecttypes and/or pools can be unlinked from this collection |
|                       | pool_ids (pool-select)             |                         |     | |

Remarks:

- Objects cannot be linked to the root pool. However, pool rights for objects can be distributed through the root pool.
For instance, a sticky `link` right for a user in the root pool will grant the user the right to link objects (of the given objecttypes) to any pool.
- for `link` and `unlink`, an empty list means that every objecttype / pool is allowed
- although "delete" is not grantable, the attribute "_grantable" exists for it because it is taken into account for the implied rights "write" and "read"

## Right dependencies

The following dependencies exist:

- the **access** group: `delete` &#8658; `write` &#8658; `read`

## ACL properties

ACL entries containing object-related rights can be filtered by the tags the object is attached to using a [tag filter](/technical/types/tag_filter/tag_filter.md).
That ACL-entry is taken into account only if the object passes the object filter. Notice that this filter will be ignored by other rights there may
be in the ACL.

ACL entries in the pool and collection realms use the attribute `sticky`, as described above. This also applies for the object realm when the objecttype is hierarchical.

## Owner

The owner of an object has the following rights:

- `read`, `write`, `delete`
- `acl`

Note: If an object has a group as owner, all users in the group are considered to own the object.

