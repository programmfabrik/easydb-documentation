---
title: "116 - Users and groups"
menu:
  main:
    name: "Users and groups"
    identifier: "technical/rightsmanagement/usergroup"
    parent: "technical/rightsmanagement"
---
# Rights management for users and groups

These rights affect the manipulation and visibility of users and groups.

Notice that there is a related system right `system.user.write_self`.

## Realms

### User

An ACL can be specified for a [user](/en/technical/types/user) (attribute `_acl`). The rights in
this ACL refer to the accessibility of this user.

### Group

An ACL can be specified for a [group](/en/technical/types/group) (attribute `_acl`). The rights in
this ACL refer to the accessibility of this group.

## Rights

As with pools and collections, the "bag" prefix is used to indicate that a right refers to a group
rather than the users it contains.

| Right             | Parameters               | Realm            |   Description        |
|-------------------|--------------------------|------------------|----------------------|
|`read`             | -                        | user             | User can be searched |
|`read`             | -                        | group            | Users of this group can be searched |
|`bag_read`         | -                        | group            | Group can be searched |
|`write`            | -                        | user             | User can be modifed and seen in full format |
|`write`            | -                        | group            | Users of this group can be modified and seen in full format |
|`bag_write`        | -                        | group            | Group can be modified and seen in full format|
|`delete`           | -                        | user             | User can be deleted |
|`delete`           | -                        | group            | Users of this group can be deleted |
|`bag_delete`       | -                        | group            | Group can be deleted |
|`link`             | -                        | group            | The user can add users to this group |
|`unlink`           | -                        | group            | The user can remove users from this group |

## ACL properties

Tagfilters and the "grantable" and "sticky" flags will be ignored by these rights.

## Right dependencies

The following dependencies exist:

- the **access** group: `delete` &#8658; `write` &#8658; `read`
- the **bag_access** group: `bag_delete` &#8658; `bag_write` &#8658; `bag_read`

## Owner

The owner of a user has the following rights:

- `read`, `write`, `delete`

The owner of a gruop has the following rights:

- `bag_read`, `bag_write`, `bag_delete`

Note: If an user/group has a group as owner, all users in the group are considered to own the user/group.
