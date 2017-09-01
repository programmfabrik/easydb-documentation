# Group

A group is an entity that allows to define rights for users. A user can belong to several groups and
inherits the rights granted to them.

Easydb creates automatically some "system groups". See below for a description.

There are different formats to present a user: full, short and short search.

## <a name="full"></a> Full format

This format is used by [/api/group](/technical/api/group/group.md) and contains all attributes that can be set for a group.
It is intended for administrators and is managed by the right `bag_write`.

| Name                         | Description                                                                                               |
|------------------------------|-----------------------------------------------------------------------------------------------------------|
| `_basetype`                  | Name of the base type (string, r): **group**                                                              |
| `_owner`                     | Owner of this group ([group (short)](/technical/types/group/group.md#short) or [user (short)](/technical/types/user/user.md#short), rw): see below |
| `_acl`                       | ACL (array of [acl entries](/technical/types/acl_entry/acl_entry.md), rw, optional)                                         |
| `_system_rights`             | System rights ([rights specification](/technical/types/right/right.md#specification), rw, optional)                     |
| `_has_acl`                   | Whether this group has a non-empty ACL (boolean, r)                                                       |
| `_generated_rights`          | Rights that the session user has for the group ([rights specification](/technical/types/right/right.md#specification)): bag_read, bag_write, bag_delete |
| `_auth_method_group_maps`    | Configuration for mapping groups when using single-sign-on (optional)                                     |
| &#8614; `<type-1>`           | - for each type (for example "sso"), an array of mappings can be defined                                  |
| &#8614; `<type-2>`           | - each element contains a `method` ("eq" or "regexp") and a `value`                                       |
| &#8614; ...                  | - the order is relevant: the first match is used                                                          |
| `group`                      | Group attributes:                                                                                         |
| &#8614; `_id`                | Group ID (integer, unique, r\*)                                                                           |
| &#8614; `_version`           | Group version (integer, rw)                                                                               |
| &#8614; `type`               | Group type (text, rw, optional): "easydb" (default), "system" or any text beginning with "custom-" (see "Group types" below) |
| &#8614; `name`               | Name (string, unique, rw): name of the group (not writable for "system" groups)                           |
| &#8614; `displayname`        | Name used to display the group ([l10n](/technical/types/l10n/l10n.md), unique)                               |
| &#8614; `comment`            | Comment (text, rw)                                                                                        |
| &#8614; `frontend_prefs`     | Extra properties that the frontend can set and retrieve (object, optional, rw)                            |
| &#8614; `authorization_info` | Extra information required for authorization purposes (string, optional, rw)                              |

Remarks:

- `_id` has to be set for POST operations to identify the object

## <a name="short"></a> Short format

This is a short format that is used by some calls. This form allows to set and retrieve groups,
for example: the owner of a collection or the groups a user belongs to.
If the attribute referencing this group is marked as writable, `group._id` is writable. The other fields are readable-only.

It contains the following attributes:

| Name                             | |
|----------------------------------|-|
| `_basetype`                      | |
| `group`                          | |
| &#8614; `_id`                    | |
| &#8614; `_displayname`           | |
| &#8614; `type`                   | |
| &#8614; `name`                   | |

## <a name="short_search"></a> Short search format

The column "Search" specifies the search type that can be used (see [/api/search](/technical/api/search/search.md)).

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

- [/group](/technical/api/group/group.md): CRUD operations on groups
- [/search](/technical/api/search/search.md): Search types "group\_management" and "acl"

