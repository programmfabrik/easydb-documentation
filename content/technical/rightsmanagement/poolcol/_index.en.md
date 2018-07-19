---
title: "113 - Pools and collections"
menu:
  main:
    name: "Pools and collections"
    identifier: "technical/rightsmanagement/poolcol"
    parent: "technical/rightsmanagement"
---
# Rights management for pools and collections

These rights affect the manipulation and visibility of pools and collections. In order to separate them from object rights, they begin with "bag".

The root pool and root collection do not have these rights, but instead use the `system.rightsmanagement` (see [system rights](/en/technical/rightsmanagement/system)).

## Realms

The rights management for pools and collections are simpler than that of objects. The rights are given in their respective
realms (pool / collection) and are inherited just like in the case of object rights. There is no rights mangement across realms.

You can find a description of how the realms work in [rights management for objects](/en/technical/rightsmanagement/objects).


## Rights

| Right             | Parameters               | Realm            |   Description        |
|-------------------|--------------------------|------------------|----------------------|
|`bag_read`         | -                        | pool             | Pool can be searched and viewed in "search" format |
|`bag_read`         | -                        | collection       | Collection can be searched and viewed |
|`bag_write`        | -                        | pool             | Pool can be written and viewed in "full" format |
|`bag_write`        | -                        | collection       | Collection can be written |
|`bag_delete`       | -                        | pool, collection | Pool / collection can be deleted     |
|`bag_acl`          | -                        | pool, collection | ACL of the pool / collection can be changed |
|`bag_create`       | -                        | pool, collection | Create subpools / subcollections inside this pool / collection |

## Right dependencies

The following dependencies exist:

- the **bag_access** group: `bag_delete` &#8658; `bag_write` &#8658; `bag_read`

## ACL properties

Tagfilters and the "grantable" flag will be ignored by these rights.

The attribute `sticky` is used the same way as described for object-related rights.
