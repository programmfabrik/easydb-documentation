# Object

An object represents an instance of a certain objecttype, which is defined in the user [schema](/technical/types/schema/schema.md).
Objects have a set of common properties, which are independent of the objecttype definition.

## Attributes

| Name                        | Description                                                                                               | Search        |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|---------------|
| `_format`                   | Format of this record (string, r): **full**, **long**, **standard** or **short** (see below)              |               |
| `_schema_version`           | User schema version this object was generated with (integer, r)                                           |               |
| `_objecttype`               | Name of the objecttype (string, r): ref [table-definition](/technical/types/schema/schema.md#table).name       | NotAnalyzed   |
| `_system_object_id`         | System object ID (string, unique ID for this easydb instance, r)                                          | Number        |
| `_global_object_id`         | Global object ID (string, unique ID for all easydb instances, r): see below                               | NotAnalyzed   |
| `_uuid`                     | Universal Unique ID (string, unique ID for all easydb instances, r)                                       | NotAnalyzed   |
| `_acl`                      | ACL (array of [acl entries](/technical/types/acl_entry/acl_entry.md), rw, optional) (\*)                          |               |
| `_has_acl`                  | Whether this object has a non-empty ACL (boolean, r)                                                      | Boolean       |
| `_private_acl`              | Marks the ACL as private (see [rights management](/technical/rightsmanagement/rightsmanagement.md)) (bool, rw, optional): defaults to **false** |  |
| `_tags`                     | Tags (array of [tags](/technical/types/tag/tag.md), rw, optional\*): only `_id` is rendered; `_id` is searchable      | Number        |
| `_collections`              | Collections this object is in (array of objects with `_id`), r): `_id` is searchable                      | Number        |
| `_has_children`             | Whether this object has children (boolean, r): only for hierarchical objects                              | Boolean       |
| `_level`                    | Depth of this object in the hierarchy (integer, r): only for hierarchical objects                         | Number        |
| `_path`                     | Hierarchy path, starting from the root (array of objects, r): only for hierarchical objects               | (\*)          |
| `_standard`                 | Information for standard rendering (standard object, r): see below                                        |               |
| `_mask`                     | Mask the object was rendered with (string, rw\*): ref [mask](/technical/maskmanagement/maskmanagement.md).name                       | NotAnalyzed   |
| `_comment`                  | Comment to be saved in changelog (string, w)                                                              |               |
| `_owner`                    | Owner ([group (short)](/technical/types/group/group.md#short) or [user (short)](/technical/types/user/user.md#short), rw): see below  |    |
| `_changelog`                | History of changes performed on this object (array of [changelog entries](/technical/types/cl_entry/cl_entry.md), sorted by `version`) |   |
| `_generated_rights`         | Rights that this user has for the object ([rights specification](/technical/types/right/right.md#specification)): see below | |
| `_current_version`          | Whether this object is in the current version (bool, r)                                                   | Boolean       |
| `_last_modifed`             | Last modifed date in UTC (string, r)                                                                      | Timestamp     |
| `<object-type-name>`        | Object attributes (the attribute name is the value of `_objecttype`): see below                           |               |

(\*) Remarks:

- `_acl` and `_private_acl` only exists if the objecttype [table definition](/technical/types/schema/schema.md#table) has the `acl_table` flag.
- `_tags` only exists if the objecttype [table definition](/technical/types/schema/schema.md#table) has the `has_tags` flag.
- `_path.<object-type-name>._id` is searchable as Number.
- `_path._global_object_id` is searchable as NotAnalyzed.

The following fields can be used when searching:

| Name                        | Description                                                                                               | Search        |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|---------------|
| `_changelog`                |                                                                                                           |               |
| &#8614; `date_created`      | Creation date of the user object                                                                          | Timestamp     |
| &#8614; `date_last_updated` | Date of last update                                                                                       | Timestamp     |
| &#8614; `user_created`      | User that created the object                                                                              | Number        |
| &#8614; `user_last_updated` | User that updated the object the last time                                                                | Number        |
| &#8614; `comment`           | Comment that was provided for an insert/update                                                            | Text          |

### Generated rights

The `_generated_rights` are the rights that the user has for a particular object. They allow to build the possible actions into the client.
The following is a list of all possible rights:

- `write`: the user can modify this object
- `delete`: the user can delete this object
- `acl`: the user can modify this object's ACL
- `change_owner`: the user can transfer ownership of this object
- `unlink`: the user can change the pool of this object (provided they have a `link` right for the target pool)

The `_generated_rights` are always provided by [/api/db](/technical/api/db/db.md).
[/api/search](/technical/api/search/search.md) provides them on demand (attribute `generate_rights`).

### Format

Objects can be rendered in three different formats. The **full** format contains all fields, as described here.

The **short** format contains:

- `_format`
- `_mask`
- `_objecttype`
- `_system_object_id`
- `_global_object_id`
- `_uuid`
- `<objecttype>._id`
- `<objecttype>._version`
- `_has_children` (only for hierarchical objects)
- `<objecttype>._id_parent` (only for hierarchical objects)
- `_tags`
- `_last_modifed`

The **standard** format contains the same fields as **short** plus:

- `_standard`
- `_path` (only for hierarchical objects)
- `_pool` (only for objects with pool link and visible pool)

The **long** format contains all fields, except:

- `_changelog`

### Global object ID

The global object ID is composed of a system ID and an instance name ("\<system_object_id\>@\<instance_name\>"). It allows to identify an object
uniquely across all Easydb instances. When performing a search, the instance name can be replaced by the alias "local", but the response will always
contain the instance name.

### Owner

An object alway has a valid owner. On object creation, the server initializes this field to the user creating the object, but it won't complain if the
API call sets the same value. If the user attempts to set a different owner, the error [403 Change Owner On Creation](/technical/errors/errors.md#change_owner_on_creation)
is returned. When updating an object, the owner has to be provided, and it cannot be set to **null**.

The owner of an object has the following rights:

- `read`, `write`, `delete`
- `acl`

### Standard object

The standard object is rendered according to the mask. It contains up to 3 levels of textual representation (text and HTML) plus up to 2 levels of
assets. The number of actual levels depends on the mask. The keys `<level>` are strings that contain the level number ("1", "2", "3").

| Name                        | Description                                                                                               | Search        |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|---------------|
| `<level>`                   | Level of textual representation (can be interpreted as title, subtitle and description, for example)      |               |
| &#8614; `text`              | - as plain text ([l10n](/technical/types/l10n/l10n.md))                                                                | L10n          |
| &#8614; `html`              | - as HTML ([l10n](/technical/types/l10n/l10n.md))                                                                      |               |
| `eas`                       | Standard assets                                                                                           |               |
| &#8614; `<level>`           | Level of asset representation (can be interpreted as main and detailed, for example)                      |               |
|                             | The asset record has a subset of the attributes of an asset (see [asset](/technical/types/asset/asset.md)):             |               |
| &#8614; &#8614; `_id`                    | | |
| &#8614; &#8614; `class`                  | | |
| &#8614; &#8614; `extension`              | | |
| &#8614; &#8614; `class_extension`        | | |
| &#8614; &#8614; `compiled`               | | |
| &#8614; &#8614; `technical_metadata`     | | |
| &#8614; &#8614; `filesize`               | | |
| &#8614; &#8614; `original_filename`      | | |
| &#8614; &#8614; `versions`               | | |
| &#8614; &#8614; &#8614; `small`          | | |
| &#8614; &#8614; &#8614; &#8614; `status` | | |
| &#8614; &#8614; &#8614; &#8614; `url`    | | |
| &#8614; &#8614; &#8614; &#8614; `width`  | | |
| &#8614; &#8614; &#8614; &#8614; `height` | | |
| &#8614; &#8614; &#8614; `preview`        | | |
| &#8614; &#8614; &#8614; &#8614; `status` | | |
| &#8614; &#8614; &#8614; &#8614; `url`    | | |
| &#8614; &#8614; &#8614; &#8614; `width`  | | |
| &#8614; &#8614; &#8614; &#8614; `height` | | |

### Object attributes

There are some common attributes, which begin with "\_" and user-defined attributes.
The latter depend on the mask used for rendering (`_mask`). All are located under `<object-type-name>`:

| Name                        | Description                                                                                               | Search        |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|---------------|
| `_id`                       | Object ID (integer, r, unique for a given object type)                                                    |               |
| `_version`                  | Object version (integer, rw)                                                                              | Number        |
| `_id_parent`                | Parent object ID (integer, rw, optional): ID of the parent (only for hierarchical objects)                | Number        |
| `_pool`                     | Pool this object is in ([pool (short)](/technical/types/pool/pool.md#short), rw\*): only for objects with pool link                  | Number (\*)   |
| `<field_name>`              | Value of the field `field_name`, the format depends on the field type (see comments below)                | (see below)   |

**Pool:**

When the attribute `pool_link` is set for the objecttype (see [Schema](/technical/types/schema/schema.md)), the `_pool` field is used to
get/set the pool this object is in. When updating an object's pool, only `_pool.pool._id` is set, but the record is returned
as a complete pool record. The fields `_pool._id` and `_pool._path.pool._id` are searchable as Number.

**Parent ID:**

When the attribute `is_hierarchical` is set for the objecttype (see [Schema](/technical/types/schema/schema.md)), the `_id_parent` field is used to
get/set the parent of this object. For top-level objects, set this field to null or do not set it.

### Fields

The value of the fields depend on the `kind` and `type` defined for them (see [Schema](/technical/types/schema/schema.md)):

**Kind "column":**

Regular columns have a `field_name` equal to the column name.

| Field type        | Value type (JSON)                        | Search  |
|-------------------|------------------------------------------|---------|
| integer           | integer                                  | Number  |
| serial            | integer                                  | Number  |
| decimal.2         | decimal                                  | Number  |
| boolean           | boolean                                  | Boolean |
| text              | string                                   | Text    |
| text_oneline      | string                                   | Text    |
| text_l10n         | [L10n](/technical/types/l10n/l10n.md)                 | L10n    |
| text_l10n_oneline | [L10n](/technical/types/l10n/l10n.md)                 | L10n    |
| string            | string                                   | String  |
| date              | [Date](/technical/types/date/date.md#date)            | Date    |
| date_range        | [Date Range](/technical/types/date/date.md#daterange) | Date    |
| date_time         | [Date](/technical/types/date/date.md#date)            | Date    |
| eas               | array of [assets](/technical/types/asset/asset.md), one for each version | Nested (\*) |
| link              | [Object](/technical/types/object/object.md) in **standard** format |         |
| custom            | JSON object, as defined by the Custom Data Type plug-in | Custom (\*\*) |

Notice that the column "Search" specifies the indexing type for the field, but a specific field can be not
searchable for a certain user because of the mask.

Whether the field can be searched in "all" or not depends on the configuration of the mask (option "fulltext").

(\*) see [Asset](/technical/types/asset/asset.md) to find out which fields are indexed and how

(\*\*) custom fields can be searched using an "elasticsearch" search element

**Kind "link":**

Links have the following `field_name`:

- `_nested:<table-name>` for a regular linked table
- `_reverse_nested:<table-name>` for a reverse linked table

The value is an array of objects. The composition of the objects depends on the linked mask and follows the
rules of "Fields".

## Related operations

- [/db](/technical/api/db/db.md): CRUD operations on objects
- [/search](/technical/api/search/search.md): Search type "objects"

