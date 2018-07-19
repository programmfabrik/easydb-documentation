---
title: "137 - Schema"
menu:
  main:
    name: "Schema"
    identifier: "technical/types/schema"
    parent: "technical/types"
---
# Schema

Easydb lets users define their own data model using a definition called "user schema". Easydb
also uses internally a schema definition for the base data model (users, groups, pools, etc.)
which is called "base schema".

A schema is composed of several tables, each one representing an object type.

The schema can be provided/retrieved in JSON and XML format. Below is a description of the JSON format.

## Attributes

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `type`                      | Schema type (string, rw): **user** or **base**                                                            |
| `version`                   | Schema version (integer, rw): the version starts at 1 and is used to control concurrent changes           |
| `based_on_version`          | Schema version this schema is based on (integer, optional, rw)                                            |
| `based_on_base_version`     | Corresponding base schema version (integer, optional, rw): for a user schema                              |
| `max_table_id`              | Maximum value of a table ID (integer, optional, rw)                                                       |
| `max_column_id`             | Maximum value of a column ID (integer, optional, rw)                                                      |
| `tables`                    | Schema tables (array of [table definitions](#table), optional, rw)                                        |

### <a name="table"></a> Table definition

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `table_id`                  | Table ID (integer, unique, auto-generated, r)                                                             |
| `name`                      | Name of the objecttype (string, unique, rw)                                                               |
| `is_hierarchical`           | Whether this objecttype is hierarchical (bool, optional, rw): defaults to **false**                       |
| `pool_link`                 | Whether objects of this type are stored in a pool or not (bool, optional, rw): defaults to **false**      |
| `acl_table`                 | Whether objects of this type can have an ACL attached to them (bool, optional, rw): defaults to **false** |
| `has_tags`                  | Whether objects of this type can have tags attached to them (bool, optional, rw): defaults to **false**   |
| `in_main_search`            | Whether this objecttype appears in the main search (bool, optional, rw)                                   |
| `in_facets`                 | Whether this objecttype can be used for facets (bool, optional, rw)                                       |
| `require_comment`           | Whether a user comment is required when updating this table (bool, optional, rw)                          |
| `columns`                   | Table columns (array of [column definitions](#column), optional, rw)                                      |
| `primary_key`               | This table's primary key ([primary key definition](#pkey), optional, rw)                                  |
| `foreign_keys`              | This table's foreign keys (array of [foreign key definitions](#fkey), optional, rw)                       |
| `unique_keys`               | This table's unique keys (array of [unique key definitions](#ukey), optional, rw)                         |
| `omni_directional`          | Omnidirectional columns (array of [omni-directional definitions](#omni), optional, rw)                    |
| `owned_by`                  | Reference to table and column that owns this table ([table-column reference](#tcref), optional, rw): see below |

Hierarchical objecttypes have a parent of their same type. For instance, an objecttype "location" would be a good candidate for a
hierarchical object, since we can have something like:

- Europe
  - Germany
    - Berlin
  - UK

Hierarchical objecttypes have an auto-generated column called "\_id\_parent" which behaves like a nullable link to the same
objecttype (see [Object](/en/technical/types/object) for more details).

If an objecttype has `pool_link` set to **true** its objects *must* be in a pool. The objecttype has an auto-generated column
called "_pool" which is a link to a [Pool](/en/technical/types/pool) (see [Object](/en/technical/types/object) for more details).

The attribute `owned_by` is used to mark private tables that are used in link columns (see below).

### <a name="column"></a> Column definition

Columns can be regular columns or links. They are classified using the attribute "kind".

**Regular columns**:

Represents a field in the objecttype that holds a single value. The column `type` defines the data type of the field.

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `kind`                      | Column kind (string): **column**                                                                          |
| `column_id`                 | Column ID (integer, unique, auto-generated, r)                                                            |
| `name`                      | Column name (string, unique, rw)                                                                          |
| `type`                      | Column type (string, rw):  see below                                                                      |
| `not_null`                  | Do not accept null as value (boolean, optional, rw): defaults to **false**                                |
| `default`                   | Default value for this column (string, optional, rw)                                                      |
| `reverse_edit`              | Whether a reverse edit is possible for this link (bool, optional, rw): only for type **link**, defaults to **false** |
| `check`                     | Type of per-column check constraint to create (enum, optional, rw). Possible values: `not_empty`, `email`, `regexp`, `range` |
| `check_regexp`              | Regular expression for check constraint (string, rw). Only for check type `regexp`. The [Tcl Advanced Regular Expression](http://www.regular-expressions.info/tcl.html) flavor is used. |
| `check_regexp_flags`        | String containing one-character modifiers for regular expression (string, optional, rw). Only for check type `regexp`. Currently only the `i` modifier (match case-insensitive) is supported. |
| `check_range_lower`         | Lower boundary of interval (integer, optional, rw). Only for check type `range`. Conflicts with `check_range_lower_open`. For check type `range` at least one of `check_range_lower`, `check_range_lower_open`, `check_range_upper` or `check_range_upper_open` has to be provided. |
| `check_range_lower_open`    | Lower boundery exluding given endpoint of interval (integer, optional, rw). Only for check type `range`. Conflicts with `check_range_lower`. |
| `check_range_upper`         | Upper boundary of interval (integer, optional, rw). Only for check type `range`. Conflicts with `check_range_upper_open`. |
| `check_range_upper_open`    | Upper boundary exluding given endpoint of interval (integer, optional, rw). Only for check type `range`. Conflicts with `check_range_upper`. |
| `length_min`                | Minimum length (integer, optional, rw) of a "text" or "string" field. |
| `length_max`                | Maximum length (integer, optional, rw) of a "text" or "string" field. |

The column types are:

- **integer**: integer
- **serial**: auto-incremented integer
- **decimal.2**: decimal number with 2-digit precision
- **boolean**: boolean (true/false)
- **text**: text
- **text_oneline**: text that should be represented in one line
- **text_l10n**: localized text
- **text_l10n_oneline**: localized text (one line)
- **string**: string
- **date**: date
- **date_range**: a range of dates (from-to, inclusive)
- **date_time**: date and time
- **eas**: an EAS asset
- **link**: link to another table in the schema. The actual details are defined in the `foreign_keys` (see above)

The difference between "text" and "string" has to do with [/api/search](/en/technical/api/search) and
[/api/suggest](/en/technical/api/suggest). Texts are considered as lists of words that can be matched at
the beginning of each word. Strings are considered as a block of characters that can be matched
at any position. An example of text could be a book title, whereas a good candidate for a string
would be a book signature.

The indication "one_line" does not have any consequence on how the data is stored;
it is just an indication about the representation in the frontend. Localized columns are columns that
have a value for each of the languages defined for the backend (see [L10n](/en/technical/types/l10n)).

**Link columns:**

Link columns are repetition groups of a table inside the main table. For example, a "painting" may have one or more "artists".
Additional fields can be specified for the relation (for example: "role" and "comment"). If the `kind` of the column is "link",
the nested table is private to the main table. If the `kind` is "reverse_link", the referenced table is another main table, and can
be edited from within this table.

Private tables are marked by the attribute `owned_by` (see [table definition](#table)).

Reverse links have to be declared in the referenced table using the attribute `reverse_edit` (see [column definition](#column)).

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `kind`                      | Column kind (string): **link** or **reverse_link**                                                        |
| `other_table_id`            | Linked table ID (integer, optional, rw)                                                                   |
| `other_table_name_hint`     | Linked table name (string, optional, rw)                                                                  |
| `other_column_id`           | Linked table column (integer, optional, rw)                                                                   |
| `other_column_name_hint`    | Linked table column (string, optional, rw)                                                                  |
| `check`                     | Type of per-column check constraint to create (enum, optional, rw). Possible values: `not_empty` |

In a typical scenario, like the one above with the painting and the artists, all tables are created at once, with a single schema update.
In that case, the nested table does not have an ID, but can be referenced by name. This is what the attribute `other_table_name_hint` is for.

### <a name="pkey"></a> Primary key

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `name`                      | Name for the primary key (string, optional, unique, rw)                                                   |
| `columns`                   | Columns that compose the primary key (array of [column references](#cref), 1+, rw)                        |

### <a name="fkey"></a> Foreign key

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `name`                      | Name for the foreign key (string, optional, unique, rw)                                                   |
| `on_delete`                 | Operation to be done on delete (string, optional, rw): see below                                          |
| `on_update`                 | Operation to be done on update (string, optional, rw): see below                                          |
| `referenced_table`          | Table referenced by the foreign key ([table reference](#tref), rw)                                        |
| `columns`                   | Columns that compose the foreign key (array of [column references](#cref), 1+, rw)                        |

The `columns` array contains the local columns that compose the foreign key. The `columns` array inside the `referenced_table` contains
the foreign columns being referenced in the same order.

The valid values for foreign key operations are:

- **cascade**: propagate operation to referenced tables
- **restrict**: prevent deletion of a referenced row
- **set null**: set referencing column to null
- **set default**: set referencing column to its default value

### <a name="ukey"></a> Unique key

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `name`                      | Name of the unique key (string, optional, unique, rw)                                                     |
| `columns`                   | list of [column references](#cref).                                                                       |
| `group`                     | Group name (string, optional, rw). May be used by client for own purposes.                                |

### <a name="cref"></a> Column reference

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `auto_column_primary_key`   | Use primary key column (boolean, optional, rw)                                                            |
| `auto_column_uplink`        | Use uplink column (link to nesting table; boolean, optional, rw)                                          |
| `auto_column_parent`        | Use parent column in hierarchical table (boolean, optional, rw)                                           |
| `column_id`                 | Column ID (integer, optional, rw)                                                                         |
| `column_name_hint`          | Column name (string, optional, rw)                                                                        |
| `unique_true`               | Uniqueness only for `true` values (boolean, optional, rw). Only for `boolean` type columns and in [unique key](#ukey) column references. |

The attribute `column_name_hint` is useful when the ID of the column is not yet known. For example, when creating a new table with a
primary key constraint.

##### `auto_column_primary_key`, `auto_column_uplink`, `auto_column_parent` and normal column references (`column_id`/`column_name_hint`) are mutually exclusive.

### <a name="cref"></a> Table reference

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `table_id`                  | Table ID (integer, optional, rw)                                                                          |
| `table_name_hint`           | Table name (string, optional, rw)                                                                         |
| `columns`                   | Referenced columns (array of [column references](#cref), 1+, rw)                                          |

### <a name="tcref"></a> Table and column reference

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `column_id`                 | Column ID (integer, optional, rw)                                                                         |
| `column_name_hint`          | Column name (string, optional, rw)                                                                        |
| `other_table_id`            | Table ID (integer, optional, rw)                                                                          |
| `other_table_name_hint`     | Table name (string, optional, rw)                                                                         |

### <a name="omni"></a> Omni-directional definitions

It is possible to declare omni-directional relationships between columns for a table. Omni-directional relationships are composed
typically of two link columns (but they may be more), so that when a relationship between two objects is established in one direction, it
also appears in the other(s). For example, to map a relationship "follows" between two users, you may define something like:


{{< include_json "./omni.json" >}}


Now you can get user 1 and update it so that it follows user 2. If you get user 2, you will also see the corresponding entry.

## Related operations

- [/schema](/en/technical/api/schema): manipulate user schema

