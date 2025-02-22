---
title: "127 - Group"
menu:
  main:
    name: "Group"
    identifier: "technical/types/group"
    parent: "technical/types"
---
# Group

A group is an entity that allows to define rights for users. A user can belong to several groups and
inherits the rights granted to them.

Easydb creates automatically some "system groups". See below for a description.

There are different formats to present a user: full, short and short search.

## <a name="full"></a> Full format

This format is used by [/api/group](/en/technical/api/group) and contains all attributes that can be set for a group.
It is intended for administrators and is managed by the right `bag_write`.

| Name                         | Description                                                                                               |
|------------------------------|-----------------------------------------------------------------------------------------------------------|
| `_basetype`                  | Name of the base type (string, r): **group**                                                              |
| `_owner`                     | Owner of this group ([group (short)](/en/technical/types/group) or [user (short)](/en/technical/types/user), rw): see below |
| `_acl`                       | ACL (array of [acl entries](/en/technical/types/acl_entry), rw, optional)                                         |
| `_system_rights`             | System rights ([rights specification](/en/technical/types/right), rw, optional)                     |
| `_has_acl`                   | Whether this group has a non-empty ACL (boolean, r)                                                       |
| `_generated_rights`          | Rights that the session user has for the group ([rights specification](/en/technical/types/right)): bag_read, bag_write, bag_delete |
| `_automatic_auth`            | Information of source of this group link. Only available in `_groups` list in [user records](/en/technical/types/user), read-only |
| &#8614; `type`               | Authentication type of the group link source, something like `sso` or `ldap` (string, r)                  |
| &#8614; `timestamp`          | Time of authentication, when the group was linked to the user (timestamp, r) |
| `_auth_method_group_maps`    | Configuration for mapping groups when using single-sign-on (optional)                                     |
| &#8614; `<type-1>`           | - for each type (for example "sso"), an array of mappings can be defined                                  |
| &#8614; `<type-2>`           | - each element contains a `method` ("eq" or "regexp") and a `value`                                       |
| &#8614; ...                  | - the order is relevant: the first match is used                                                          |
| `_ipv4_subnet_filter`        | IPv4 subnet filter for group (array of strings, rw, optional, non-system groups only). When set, a group associated to the user is only valid in session when at least one of the subnets given matches the IPv4 address of the client during authentication. Examples: `127.0.0.0/8`, `203.0.113.42/32` |
| `group`                      | Group attributes:                                                                                         |
| &#8614; `_id`                | Group ID (integer, unique, r\*)                                                                           |
| &#8614; `_version`           | Group version (integer, rw)                                                                               |
| &#8614; `type`               | Group type (text, rw, optional): "easydb" (default), "system" or any text beginning with "custom-" (see "Group types" below) |
| &#8614; `name`               | Name (string, unique, rw): name of the group (not writable for "system" groups)                           |
| &#8614; `displayname`        | Name used to display the group ([l10n](/en/technical/types/l10n), unique)                               |
| &#8614; `comment`            | Comment (text, rw)                                                                                        |
| &#8614; `frontend_prefs`     | Extra properties that the frontend can set and retrieve (object, optional, rw)                            |
| &#8614; `authorization_info` | Extra information required for authorization purposes (string, optional, rw)                              |
| &#8614; `reference`          | Group reference (string, unique, optional, rw): can be used for lookups for `_id`                |
| &#8614; `created_timestamp`      | timestamp of creation of this group (timestamp, r) |
| &#8614; `last_updated_timestamp` | timestamp of the last update of this group (timestamp, r) |

Remarks:

- `_id` has to be set for POST operations to identify the object

## <a name="short"></a> Short format

This is a short format that is used by some calls. This form allows to set and retrieve groups,
for example: the owner of a collection or the groups a user belongs to.
If the attribute referencing this group is marked as writable, `group._id` is writable. The other fields are readable-only.

It contains the following attributes:

| Name                             | |
|----------------------------------|---|
| `_basetype`                      | |
| `group`                          | |
| &#8614; `_id`                    | |
| &#8614; `_displayname`           | |
| &#8614; `type`                   | |
| &#8614; `name`                   | |

## <a name="short_search"></a> Short search format

The column "Search" specifies the search type that can be used (see [/api/search](/en/technical/api/search)).

| Name                        | Search        |
|-----------------------------|---------------|
| `_basetype`                 |               |
| `group`                     |               |
| &#8614; `_id`               | Number        |
| &#8614; `_version`          | Number        |
| &#8614; `displayname`       | L10n (all)    |
| &#8614; `comment`           |               |
| &#8614; `type`              | NotAnalyzed   |
| &#8614; `name`              | NotAnalyzed   |

## Owner

The group always has an owner. On creation, it is set automatically by the server to the group's creator, but the API won't complain if it is explicitly
set. It will return an error if it is set to something different. The owner cannot be set to **null** but can always be left out, meaning that it should not be changed.

System groups have the system user "root" as owner.

## Group types

System groups are created automatically and cannot be deleted:

| Name			  |                                     |
|-------------------------|-------------------------------------|
| `:all`                  | All users. |
| `:non_system`           | All users, except for the system users **root**, **oai_pmh** and **deep_link** (see [User types](../../../webfrontend/rightsmanagement/users/#user-types)). |
| `:internet_connection`  | User is connected through internet channels. |
| `:intranet_connection`  | User is connected through safer intranet channels. |
| `:authenticated`        | User is authenticated. |
| `:easydb`               | Regular users. |
| `:email`                | User who was invited by e-mail (by collection sharing or e-mail tranport of an export). |
| `:collection`           | User is a pseudo user, allowed to see one or more collections. |
| `:anonymous`            | Anonymous users. |
| `:easydb-self-register` | Self-registered users |
| `:fallback`             | Fallback owner for (base) objects that have lost their owner (the owner was deleted). |
| `:sso`                  | Users authenticated using single-sign on. |

These groups cannot be assigned to users directly. They are assigned dynamically by the server.

Regular groups are created by the user. Their default type is "easydb", but the user is allowed to create custom types, which begin with "custom-".

## Related operations

- [/group](/en/technical/api/group): CRUD operations on groups
- [/search](/en/technical/api/search): Search types "group\_management" and "acl"

