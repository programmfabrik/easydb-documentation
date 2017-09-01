# User

The user is the central entity for security management. It defines the authentication method
(currently login+password) and keeps track of its status. Users can belong to several groups.
Users and groups can be granted permissions using access control lists.

Easydb creates automatically system and anonymous users. See below for a description.

There are different formats to present a user: full, short and contact.

## <a name="full"></a> Full format

This format is used by [/api/user](/technical/api/user/user.md) and contains all attributes that can be set for a user.

| Name                             | Description                                                                                               |
|----------------------------------|-----------------------------------------------------------------------------------------------------------|
| `_basetype`                      | Name of the base type (string, r): `user`                                                                 |
| `_owner`                         | Owner of this user ([group (short)](/technical/types/group/group.md#short) or [user (short)](/technical/types/user/user.md#short), rw): see below |
| `_acl`                           | ACL (array of [acl entries](/technical/types/acl_entry/acl_entry.md), rw, optional)                                         |
| `_system_rights`                 | System rights ([rights specification](/technical/types/right/right.md#specification), rw, optional)                     |
| `_groups`                        | Groups this user belongs to (array of [groups (short)](/technical/types/group/group.md#short), r)                       |
| `_has_acl`                       | Whether this user has a non-empty ACL (boolean, r)                                                        |
| `_password`                      | Password for login (string, `true` or `false`, optional, w). When `true` a new password is generated and send by email, when `false` the current password is archived (disabled). |
| `_generated_rights`              | Rights that the session user has for the user ([rights specification](/technical/types/right/right.md#specification)): read, write, delete |
| `user`                           | User attributes:                                                                                          |
| &#8614; `_id`                    | User ID (integer, unique, r\*)                                                                            |
| &#8614; `_version`               | User version (integer, rw)                                                                                |
| &#8614; `_generated_displayname` | Name to display for this user (string, r): see below                                                      |
| &#8614; `type`                   | User type (string, rw): see below                                                                         |
| &#8614; `login_disabled`         | Whether the authentication method "easydb" is disabled for the user (boolean, optional, rw): defaults to `false` |
| &#8614; `login_valid_from`       | If set, the authentication method "easydb" is only valid from this timestamp on, inclusively (timestamp, optional, rw) |
| &#8614; `login_valid_to`         | If set, the authentication method "easydb" is only valid until this timestamp, exclusively (timestamp, optional, rw) |
| &#8614; `login`                  | Username for login (string, unique, optional, rw): unique if set                                          |
| &#8614; `first_name`             | First name (string, optional, rw)                                                                         |
| &#8614; `last_name`              | Last name (string, optional, rw)                                                                          |
| &#8614; `displayname`            | Displayname (string, rw)                                                                                  |
| &#8614; `remarks`                | Remarks (string, rw)                                                                                      |
| &#8614; `frontend_language`      | Frontend language (string, rw): language to be used when applying l10n to the frontend: defaults to the first frontend language |
| &#8614; `database_languages`     | Database languages (array of strings, rw, nullable): subset of backend languages to be considered for the user (\*) |
| &#8614; `search_languages`       | Search languages (array of strings, rw, nullable): subset of backend languages to be used by search (\*)  |
| &#8614; `picture`                | User avatar ([Asset](/technical/types/asset/asset.md), optional, rw)                                                    |
| &#8614; `frontend_prefs`         | Extra properties that the frontend can set and retrieve (object, optional, rw)                            |
| &#8614; `company`                | Company (string, optional, rw)                                                                            |
| &#8614; `department`             | Department (string, optional, rw)                                                                         |
| &#8614; `phone`                  | Phone (string, optional, rw)                                                                              |
| &#8614; `street`                 | Street (string, optional, rw)                                                                             |
| &#8614; `house_number`           | House number (string, optional, rw)                                                                       |
| &#8614; `address_supplement`     | Address supplement (string, optional, rw)                                                                 |
| &#8614; `postal_code`            | Postal code (string, optional, rw)                                                                        |
| &#8614; `town`                   | Town or city (string, optional, rw)                                                                       |
| &#8614; `country`                | Country (string, optional, rw)                                                                            |
| &#8614; `mail_schedule`          | Mail schedule preferences for the user ([schedule](/technical/types/schedule/schedule.md), optional, rw): defaults to `{}` (once a day) |
| &#8614; `_primary_email`         | User primary e-mail (string, optional, r)                                                                 |
| &#8614; `_new_primary_email`     | New primary e-mail requested (string, optional, rw)                                                      |
| &#8614; `require_password_change` | user is requested to change or set his password by a pending task the next time he logs in (bool, optional, rw) |
| &#8614; `created_timestamp`      | timestamp of creation of this user (timestamp, r) |
| &#8614; `last_updated_timestamp` | timestamp of the last update of this user (timestamp, r) |
| `_emails`                        | list of email addresses, each of them may contain the following attributes:                               |
| &#8614; `email`                  | actual email address (string, rw)                                                                         |
| &#8614; `needs_confirmation`     | request email address to get confirmed by sending out an email (`true`, optional, rw)                     |
| &#8614; `send_email_include_password` | When set to `true`, an email is sent to user containing the generated password. (boolean, optional, rw, default `false`) |
| &#8614; `requested_confirmation_date` | date of confirmation request sent by email (date, r)                                            |
| &#8614; `confirmed_date`         | date of email confirmation (date, r)                                                                      |
| &#8614; `use_for_login`          | use this email address for login (identification of user; boolean, rw, default `false`)                   |
| &#8614; `use_for_email`          | use this email address for sending informational emails (boolean, rw, default `false`)                    |
| &#8614; `send_email`             | send emails to this address                              (boolean, rw, default `true`)                    |
| &#8614; `send_email_include_password` | include plain text passwords when sending emails to this address (if applicable; boolean, rw, default `true`) |
| &#8614; `is_primary`             | whether this is the current primary e-mail (bool, rw) |
| &#8614; `intended_primary`       | whether this e-mail is intended as the new primary e-mail (bool, rw) |


Remarks:

- `_id` has to be set for POST operations
- if `search_languages` is not set, the first backend language will be used
- if `database_languages` is not set, the first backend language will be used
- if the base config specifies a password policy and `_password` is set to a string, it will be checked against the policy
- only one e-mail can have `is_primary` set to true
- only a valid e-mail can have `is_primary` set to true
- only one e-mail can have `intended_primary` set to true
- only an e-mail with a pending confirmation request (`needs_confirmation`) can have `intended_primary` set to true
- `_groups` contains only groups to which this user is statically linked, except for the session format, which also includes dynamically assigned groups

## <a name="short"></a> Search format

This format is returned when searching users.
The column "Search" specifies the search type that can be used (see [/api/search](/technical/api/search/search.md)).

| Name                             | Description | Search               |
|----------------------------------|-------------|----------------------|
| `_basetype`                      |             |                      |
| `_groups`                        |             |                      |
| &#8614; `group`                  |             |                      |
| &#8614; &#8614; `_id`            |             | Number               |
| `user`                           |             |                      |
| &#8614; `_generated_displayname` |             | Text                 |
| &#8614; `_id`                    |             | Number               |
| &#8614; `_version`               |             | Number               |
| &#8614; `type`                   |             | NotAnalyzed          |
| &#8614; `login`                  |             | String (all)         |
| &#8614; `last_name`              |             | Text (all)           |
| &#8614; `first_name`             |             | Text (all)           |
| &#8614; `company`                |             | Text (all)           |
| &#8614; `department`             |             | Text (all)           |
| &#8614; `street`                 |             | Text (all)           |
| &#8614; `address_supplement`     |             | Text (all)           |
| &#8614; `postal_code`            |             | Text (all)           |
| &#8614; `town`                   |             | Text (all)           |
| &#8614; `country`                |             | Text (all)           |
| &#8614; `displayname`            |             | Text (all)           |
| &#8614; `phone`                  |             | String (all)         |
| &#8614; `house_number`           |             | String (all)         |
| &#8614; `_primary_email`         |             | String (only in all) |
| &#8614; `created_timestamp`      |             | Timestamp            |
| &#8614; `last_updated_timestamp` |             | Timestamp            |

## <a name="short"></a> Short format

This is a short format that is used when specifying users inside other types (i.e. "who" in ACL entries).
For fields that are already present in the full format a description is not provided.

| Name                             | Description |
|----------------------------------|-------------|
| `_basetype`                      |             |
| `_groups`                        |             |
| &#8614; `group`                  |             |
| &#8614; &#8614; `_id`            |             |
| `user`                           |             |
| &#8614; `_generated_displayname` |             |
| &#8614; `_id`                    |             |
| &#8614; `_version`               |             |
| &#8614; `type`                   |             |
| &#8614; `login`                  |             |
| &#8614; `_primary_email`         |             |
| &#8614; `frontend_language`      | writable when creating ad-hoc users |

When creating an ad-hoc user inside a collection ACL, the `_id` is not provided; the `type` is set to the kind of user and the `login` contains the e-mail or secret (depending on the user type).

## <a name="contact"></a> Contact format

This format is used when retrieving a pool or objecttype contact.
If the attribute referencing this user is marked as writable, `user._id` is writable. The other fields are readable-only.

It contains the same attributes as "short", plus:

| Name                             | |
|----------------------------------|-|
| `_basetype`                      | |
| `user`                           | |
| &#8614; `first_name`             | |
| &#8614; `last_name`              | |
| &#8614; `company`                | |
| &#8614; `department`             | |
| &#8614; `phone`                  | |

## <a name="session"></a> Session format

This format is used inside the [session](/technical/types/session/session.md) object.
It contains the same attributes as "short" plus the following, providing the user has the corresponding `system.user.write_self` right:

- `user.first_name`
- `user.last_name`
- `user.displayname`
- `user.company`
- `user.department`
- `user.phone`
- `user.picture` (full; if no `system.user.write_self` right is present, only the small version is provided)
- `user.mail_schedule`

The session format also includes:

- `_groups`
- `user._version`
- `user.search_languages`.
- `user.database_languages`
- `user.frontend_prefs`
- `user.picture`

## User types

There are different kinds of users: regular users (type "easydb") are created by users with the required authorization; system users (type "system")
are provided by the system. The other types are created ad-hoc during different interactions with the system.

| Type                 | Creation | Comments |
|----------------------|----------|----------|
| easydb               | [PUT /api/user](/technical/api/user/user.md) | regular users |
| easydb_self_register | [PUT /api/user](/technical/api/user/user.md) | users created via `system.user.create_new` when this type is selected |
| system               | automatically created on system start-up | only the following attributes can be modified: `login`, `_acl`, `_system_rights` and `_groups` |
| anonymous            | [POST /api/session/authenticate](/technical/api/session/session.md) with authentication type "anonymous" | cannot be modified |
| email                | [POST /api/collection](/technical/api/collection/collection.md) with an ACL containing an "email" user | cannot be modified |
| collection           | [POST /api/collection](/technical/api/collection/collection.md) with an ACL containing a "collection" user | cannot be modified |
| sso                  | [GET /api/session/sso/authenticate](/technical/api/session/session.md) when the user does not already exist |
| custom-{custom_type} | [PUT /api/user](/technical/api/user/user.md) with "create_new" and custom type | custom type |

There is currently only one system user: `root`.

Users of type "email" and "collection" belong in the system group ":collection".

Currently, only the following type conversions are allowed:

- from "email" to "easydb"
- from "easydb_self_register" to "easydb"

## Owner

The user always has an owner. On creation, it is set automatically by the server to the user's creator, but the API won't complain if it is explicitly
set. It will return an error if it is set to something different. The owner cannot be set to **null** but can always be left out, meaning that it should not be changed.

System users have the system user "root" as owner.

## Generated display name

from one of the following sources:

- "displayname"
- "first\_name" and/or "last\_name"
- "login"

## Related operations

- [/user](/technical/api/user/user.md): CRUD operations on users
- [/search](/technical/api/search/search.md): Search types "user\_management" and "acl"
- [/session/authenticate](/technical/api/session/session.md): Creates anonymous users when the authentication method is "anonymous" and the user is not known to the system.

