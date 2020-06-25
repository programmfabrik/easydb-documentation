---
title: "129 - Maskset"
menu:
  main:
    name: "Maskset"
    identifier: "technical/types/maskset"
    parent: "technical/types"
---
# Maskset

A mask defines how objects of a certain objecttype are seen and manipulated. Easydb lets you define
different masks for an objecttype and associate them with users.
For each user schema definition, a maskset definition must be provided, which comprises all masks that
apply for the objecttypes of the given schema. The maskset definition can change while the schema
definition remains unchanged.

The maskset can be provided/retrieved in JSON and XML format. Below is a description of the JSON format.

## Attributes

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `version`                   | Maskset version (integer, rw): the version starts at 1 and is used to control concurrent changes          |
| `based_on_schema_version`   | Schema version this maskset is based on (integer, rw): ref [Schema](/en/technical/types/schema).version           |
| `max_mask_id`               | Maximum value of a mask ID (integer, optional, rw)                                                        |
| `masks`                     | Masks (array of [mask definitions](#mask), rw)                                                            |

### <a name="mask"></a> Mask definition

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `name`                      | Name of the mask (string, unique, rw)                                                                     |
| `mask_id`                   | Mask ID (integer, unique, auto-generated, r)                                                              |
| `table_id`                  | Table this mask applies to (integer, rw): ref [table definition](/en/technical/types/schema).id           |
| `is_preferred`              | Marks the preferred mask for an objecttype (boolean, optional, rw): defaults to **false**                 |
| `hide_in_editor`            | Hide in editor (not used by server; boolean, optional, rw). Defaults to **false**                         |
| `hide_in_detail`            | Hide in detail (not used by server; boolean, optional, rw). Defaults to **false**                         |
| `require_comment`           | Ask user to supply a comment on saving an object (enum, optional, rw). Possible values: `never`, `default-enabled`, `default-disabled`, `always`.          |
| `fields`                    | Fields (array of [field definitions](#field), rw)                                                         |

The maskset must define a preferred mask - and only one - for a given objecttype.

The mask `name` must follow these rules:

- It must have at least 3 characters
- It can only be composed of english lower case letters, numbers and the special symbols "-" and "\_"
- The first character must be a letter
- The last character must be a letter or a number

### <a name="column"></a> Field definition

Fields can be regular fields, links, linked tables or splitters. They are classified using the attribute "kind".

#### Regular fields:

A mask definition for a regular column (see [Schema](/en/technical/types/schema)).

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `kind`                      | Field kind (string, rw): **field**                                                                        |
| `column_id`                 | Column this field refers to (integer, rw): ref [column definition](/en/technical/types/schema).id (\*)     |
| `column_name_hint`          | Column this field refers to (string, rw): ref [column definition](/en/technical/types/schema).name (\*)    |
| `edit`                      | Edit properties ([edit properties](#edit), rw)                                                            |
| `output`                    | Output properties ([output properties](#output), rw)                                                      |
| `search`                    | Search properties ([search properties](#search), optional, rw)                                            |

(\*) at least one of `column_id` and `column_name_hint` must be provided when updating a mask.

#### Link:

A mask definition for a link (see [Schema](/en/technical/types/schema)). Links use the masks that are defined for the linked type.

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `kind`                      | Field kind (string, rw): **link**                                                                         |
| `column_id`                 | Column this field refers to (integer, rw): ref [column definition](/en/technical/types/schema).id (\*)     |
| `column_name_hint`          | Column this field refers to (string, rw): ref [column definition](/en/technical/types/schema).name (\*)    |
| `other_table_id`            | Referenced table ID (integer, rw): ref [table definition](/en/technical/types/schema).id (\*)               |
| `other_table_name_hint`     | Referenced table name (string, rw): ref [table definition](/en/technical/types/schema).name (\*)            |
| `mask_id`                   | Mask that should be used (string, rw): ref [mask](#mask).id or "PREFERRED"                                |
| `inline`                    | Inline format (one of `standard`, `text`, `short`, optional, defaults to `standard`)                      |
| `edit`                      | Edit properties ([edit properties](#edit), rw)                                                            |
| `output`                    | Output properties ([output properties](#output), rw)                                                      |
| `search`                    | Search properties ([search properties](#search), optional, rw)                                            |

(\*) at least one of `xxx_id` and `xxx_name_hint` must be provided when updating a mask.

Setting `mask_id` to PREFERRED means that the mask that has `is_preferred` set to **true** for the table will be used.

#### Linked table:

A mask definition for a (reverse) linked table (see [Schema](/en/technical/types/schema)).

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `kind`                      | Field kind (string, rw): **linked-table** or **reverse-linked-table**                                     |
| `is_hierarchical`           | Whether the table is hierarchical (integer, optional, rw) (\*)                                            |
| `other_table_id`            | Referenced table ID (integer, rw): ref [table definition](/en/technical/types/schema).id (\*)               |
| `other_table_name_hint`     | Referenced table name (string, rw): ref [table definition](/en/technical/types/schema).name (\*)            |
| `other_column_id`           | Referenced column ID (integer, rw): ref [column definition](/en/technical/types/schema).id (\*)            |
| `other_column_name_hint`    | Referenced column name (string, rw): ref [column definition](/en/technical/types/schema).name (\*)         |
| `mask`                      | (Private) mask definition to be applied for the table ([mask definition](#mask))                          |
| `sort_first_field`          | Set sort order for first field (optional, "asc", "desc" or empty). Sorting is currently not done by server but this attribute is saved for client implementation. |
| `edit`                      | Edit properties for linked tables ([edit properties](#edit_linked), rw)                                   |

(\*) when `is_hierarchical` is **true**, the attributes `xxx_id` and `xxx_name_hint` are omitted. Else, at least one of `xxx_id` and
`xxx_name_hint` must be provided when updating a mask

#### Splitter:

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `kind`                      | Field kind (string, rw): **splitter**                                                                     |
| `type`                      | Type of splitter (string, rw): for example: "panel-begin", "panel-end", "h1"                              |
| `options`                   | Splitter options (string, optional, rw)                                                                   |

### <a name="edit"></a> Edit properties for regular fields

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `mode`                      | Edit mode (string, rw): **edit**, **off** or **show**                                                     |
| `group_edit`                | Whether this field can be used in a group edit action (boolean, rw)                                       |

### <a name="edit"></a> Edit properties for linked tables

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `mode`                      | Edit mode (string, rw): **edit**, **off** or **show**                                                     |
| `append_only`               | Only allow to append entries (boolean, rw): only for (reverse) linked tables                              |
| `as_table`                  | Show as table (boolean, rw): only for (reverse) linked tables                                             |
| `show_labels`               | Show labels (boolean, rw): only for (reverse) linked tables                                               |

### <a name="output"></a> Output properties

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `text`                      | Show as text (boolean)                                                                                    |
| `detail`                    | Show in detail view (boolean)                                                                             |
| `table`                     | Show in table view (boolean)                                                                              |
| `standard`                  | Stardard rendering options ([standard properties](#standard))                                             |

### Standard properties

The Server [builds the standard for objects according to the standard properties](build_standard) of the mask.

#### <a name="standard"></a> Standard for Text and HTML

| Name     | Description                                                  |
| -------- | ------------------------------------------------------------ |
| `order`  | Order (integer, rw): `1`, `2`, `3`                           |
| `design` | Design options (string, rw): **bold**, **normal** or **thin** |
| `format` | Format options (string, rw): **brackets**, **newline**, **comma**, **semicolon**, **round-parentheses**, **square-brackets**, **pipe** |

#### <a name="standard_eas"></a> Standard for Assets (EAS)

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `order`                     | Order (integer, rw): `1`, `2`, `3`                                                                              |

### Standard `A`, `B` and `C` usages

|                      |                                           | A    | B    | C    | Standard file | Comment                                                      |
| -------------------- | ----------------------------------------- | ---- | ---- | ---- | ------------- | ------------------------------------------------------------ |
| Search standard view |                                           |      |      |      |               |                                                              |
|                      | Mini                                      |      |      |      | X             | Only the image is shown if defined.                          |
|                      | Midi                                      | X    |      |      | X             |                                                              |
|                      | Maxi + Fill + Overlay                     | X    |      |      | X             |                                                              |
|                      | Maxi + Thumbnail/Cover + Overlay/Underlay | X    |      |      | X             |                                                              |
|                      | Maxi + Thumbnail/Cover + Sideways         | X    | X    | X    | X             |                                                              |
| Search text view     |                                           |      |      |      | X             | No standard information is displayed, the "text" fields from the object are shown. |
| Search table view    |                                           |      |      |      |               |                                                              |
|                      | Mini                                      | X    |      |      | X             |                                                              |
|                      | Midi                                      | X    |      |      | X             |                                                              |
|                      | Maxi                                      | X    |      |      | X             |                                                              |
| Sorting heading      |                                           | X    |      |      |               |                                                              |
| Search list view     |                                           |      |      |      |               |                                                              |
|                      | Mini                                      | X    |      |      | X             |                                                              |
|                      | Midi                                      | X    |      |      | X             |                                                              |
|                      | Maxi                                      | X    |      |      | X             |                                                              |
| Detail view          |                                           |      |      |      |               |                                                              |
|                      | Summary                                   | X    |      |      |               | Only the first not empty standard is shown.                  |
|                      | Hierarchy browser                         | X    |      |      | X             | Only the first not empty standard is shown.                  |
|                      | Hierarchy field                           | X    |      |      | X             | Only the first not empty standard is shown.                  |
|                      | Fullscreen                                | X    |      |      | X             |                                                              |
| Linked object        |                                           |      |      |      |               |                                                              |
|                      | Standard                                  | X    | (X)  |      | X             | B is shown in editor only.                                   |
|                      | Text                                      |      |      |      |               | No standard information is displayed, the "text" fields from the linked object are shown. |
|                      | Short                                     | X    |      |      |               |                                                              |

`Notes:`

- When only one standard is shown, the priority to show them is A > B > C



### <a name="search"></a> Search properties

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `fulltext`                  | Fulltext search allowed (boolean)                                                                         |
| `expert`                    | Expert search allowed (boolean)                                                                           |
| `facet`                     | Faceting allowed (boolean)                                                                                |

## Related operations

- [/mask](/en/technical/api/mask): manipulate maskset

