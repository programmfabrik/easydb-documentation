# System rights

System rights are a bit different than the other rights. They are attached to users using the `_system_rights` parameter,
either of the user itself or a group it belongs to. Therefore, no ACL is involved. All system rights begin with "system".

## Rights

The system rights are classified into groups. This is just a classification that can be used in the frontend to group related rights.

### Group main

| Right                                  | Description | Parameters |
|----------------------------------------|-------------|------------|
| `system.root`                          | User is allowed to do anything, rights management does not apply | - |
|                                        | The system user "root" always has this right. Only users with this right may pass it on to other users | - |
| `system.datamodel`                     | Datamodel permissions | `level`, one of the following: |
|                                        | | - "current": view the current datamodel; this is a frontend-only right, as the server needs to publish the datamodel to every user |
|                                        | | - "development": update the development branch of the datamodel and maks definitions |
|                                        | | - "commit": commit the development branch of the datamodel and make it current |
| `system.server.error.self_uuid_detail` | User is allowed to retrieve detailed information about a server error caused by him/herself | - |
| `system.server.error.uuid_detail`      | User is allowed to retrieve detailed information about any server error | - |
| `system.config` 			 | Access /api/config | - |
| `system.health`                        | Access /api/health | - |
| `system.profile`                       | Modify profiles with /api/xmlmapping | - |
| `system.message`                       | Access /api/message and frontend app | - |
| `system.objecttypemanager`             | Access objecttype manager | - |
| `system.poolmanager`                   | Access pool manager | - |
| `system.tagmanager`                    | Access tags and transitions manager | - |
| `system.rightpresetmanager`            | Access right presets manager | - |
| `system.search`			 | Access frontend "Search" | `show_fixed_searches` (bool, defaults to **false**): show fixed searches |
|                    			 |                          | `collection_only` (bool, defaults to **false**): collection_only user |
| `system.allow_custom_in_right_with_preset` | User is allowed to set custom rights in an ACL entry that also works with presets (only frontend) | - |
| `system.frontend_features`             | Fronted features (on/off)                          | `changelog` |
|                                        | (all parameters are bool and default to **false**) | `download` |
|                                        |                                                    | `export` |
|                                        |                                                    | `edit_bulk` |
|                                        |                                                    | `deep_link_sharing` |
|                                        |                                                    | `print` |

### Group user

This group covers user and group management related rights

| Right                          | Description                        | Parameters |
|--------------------------------|------------------------------------|------------|
| `system.user`                  | Access frontend "User Management", GET /api/user  | `create` (bool, defaults to **false**): creation of users is allowed |
| `system.group`                 | Access frontend "Group Management", GET /api/group | `create` (bool, defaults to **false**): creation of groups is allowed |
| `system.user.write_self`       | User is allowed to edit some of its own configuration | see below |
| `system.user.change_password`  | User is allowed to change its password | - |
| `system.user.create_new`       | User is allowed to create a new user (used for registration) | see below |

**system.user.write_self** and **system.user.create_new**

These rights have several parameters of type bool. All of them are optional and default to *false*. Each parameter set to *true* allows a user to:

- modify the value of a certain field of its own user record (for **system.user.write_self**)
- set the value of a certain field when creating a new user (for **system.user.create_new**)

| Parameter            | Field                     |
|----------------------|---------------------------|
| `first_name`         | `user.first_name`         |
| `last_name`          | `user.last_name`          |
| `displayname`        | `user.displayname`        |
| `company`            | `user.company`            |
| `department`         | `user.department`         |
| `phone`              | `user.phone`              |
| `street`             | `user.street`             |
| `house_number`       | `user.house_number`       |
| `address_supplement` | `user.address_supplement` |
| `postal_code`        | `user.postal_code`        |
| `town`               | `user.town`               |
| `country`            | `user.country`            |
| `picture`            | `user.picture`            |
| `mail_schedule`      | `user.mail_schedule`      |
| `_new_primary_email` | `_new_primary_email`      |

The right **system.user.create_new** has additional parameters:

| | |
|-----------------|----------------------|
| `type`          | Type for the new user: choice between **easydb**, **easydb_self_register** or **custom_type** |
| `custom_type`   | Custom type for the new user: see below |
| `require_group` | Whether a group is required when creating the user (bool): defaults to **false** |
| `_password`     | `_password` |
| `login`         | `login` |

If the right parameter `type` is set to "custom_type", a `custom_type` has to be provided. Newly created users using this right will have the
type "custom-<custom_type>".

## <a name="comment"></a>Comments

The management of the system rights and ACL itself is divided in two parts:

1. The system rights management, granted through the system right `system.rightsmanagement`. This right allows a user to:
- manage the ACL of objecttypes, users, groups
- manage the ACL of the root pool and the root collection
- manage the system rights of users and groups
- edit tags and transitions

2. The regular rights management, granted through the `acl` and `bag_acl` rights discussed in the previous sections:
- `acl` right for objects at objecttype, tag and pool levels
- `bag_acl` right for pools and collections, other than root
