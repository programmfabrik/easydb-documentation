---
title: "211 - How To Get Started"
menu:
  main:
    name: "1. Datamodel"
    identifier: "tutorials/get_started/get_started_1_datamodel"
    parent: "tutorials/get_started"

---

[&rArr; 2. Structure of objects](../get_started_2_structure/)

----

# 1. Datamodel

The objects in the easydb are based on a freely configurable schema. The schema defines different objecttypes, which are represented as database tables. Each objecttype consists of a number of fields (columns) of different types.

The objects are represented by one or more masks which can be configured to control which data is writable, readable and searchable.

## Objecttypes and fields in the schema

Objecttypes are defined as [tables](/en/technical/types/schema/#table) in the schema. Each field in an objecttype is defined as a [column](/en/technical/types/schema/#column) with a specific name and type in the table.

The schema can be read and written using the [API `api/v1/schema/user`](/en/technical/api/schema/).

For this tutorial, we assume a simple datamodel with a main objecttype including text fields, file (asset), [list of links](#fields-in-nested-tables) and a link to a hierarchical object:

- `main` (main object)
  - `title` (text field: type `text_oneline`)
  - `description` (text field: type `text_oneline`)
  - `picture` (asset field: type `eas`)
  - `place` (field with a link to another objecttype: `place`)
  - `keywords` (nested table: list of rows of fields)
    - `keyword` (link to another objecttype: `keyword`)
    - `comment` (text field: type `text_oneline`)
- `keyword` (simple list object)
  - `name` (text field: type `text_oneline`)
- `place` (hierarchical list object)
  - `name` (text field: type `text_oneline`)

This datamodel is defined in this (simplified) JSON object. For the detailled overview of the schema structure, see [Schema Attributes](/en/technical/types/schema/#attributes). The complete schema, maskset and localization keys can be found [here](../datamodel/).

<a name="simple_schema"></a>
{{< include_json "../samples/simple_schema.jsonc" >}}
[&uArr; go to beginning of this snippet](#simple_schema)

### Fields in nested tables

To insert repeated rows of the same structur into a field, the field is linked to another (nested) table. The field is defined as `"kind": "link"` and includes the internal id of the nested table it links to (`"other_table_id"`).

In the example, the column `"keywords"` in the objecttype `"main"` contains another table which itself contains a link to the objecttype `"keyword"` as well as a simple textfield. The object can contain an arbitrary number of rows of this structure.

The nested table itself (`"main__keywords"`) is defined like any other schema table, but the key `"owned_by"` which contains information about the table which links to this nested table, defines it as not an actual objecttype. The fields in this nested table are defined as columns like in any other table.

## Masks for objecttypes

Masks are used to control fields of an objecttype. For each field, a mask contains information, wether the field is writable, readable or searchable, as well as other information used to display fields. All objects have at least one mask, but multiple masks can be defined to control access to objects using the [rights management](/en/webfrontend/rightsmanagement). One mask is always defined as the standard mask for this objecttype.

The server also always provides the out-of-the-box mask `_all_fields`, which is no real mask, but used as an information for the server to include all fields without any limitations.

The maskset can be read and written using the [API `api/v1/mask`](/en/technical/api/mask/).

For the detailled overview of the maskset and mask structure, see [Mask Definition](/en/technical/types/maskset/#mask).

<a name="simple_maskset"></a>
{{< include_json "../samples/simple_maskset.jsonc" >}}
[&uArr; go to beginning of this snippet](#simple_maskset)

The objecttype `"main"` in the example has two masks.

Mask `"main__standard"` contains all fields, the asset, links and nested tables. These fields are writable (`"edit": { "mode": "edit" }`), which automatically means they are also readable. All fields are also included in the expert, fulltext and facet [search](#4-searching-for-objects). This mask is also defined as the standard (preferred) mask for this objecttype.

The other mask `"main__simple"` excludes most fields, and only the main title field `"title"` and the image `"picture"` is shown. These fields are not writable but only readable (`"edit": { "mode": "show" }`). All other fields are not included in the object at all (`"edit": { "mode": "off" }`), so they can not be read or written.

Using the rights management, the following scenario can be set up:

Allow certain users or groups to see the `"main__standard"` mask, so they can see and edit all fields. Other users or groups can be restricted, so they can only see objects in the `"main__simple"` mask, so these users can only see some fields of the object and can not edit any data in the object.

## Localization

The names of objecttypes, fields and masks we used so far are technical names which are used internally in the database and the [JSON objects](#2-structure-of-objects-based-on-the-user-schema). To render human readable localizations in different languages, the translations can assigned to the fields. JSON keys are formatted in a specific way ([see below](#objecttype-names)), and contain a simple object where each key is a specific l10n key which then contains the translation.

The localizations can be read and written using the [API `api/v1/l10n/user`](/en/technical/api/l10n/).

<a name="simple_l10n"></a>
{{< include_json "../samples/simple_l10n.jsonc" >}}
[&uArr; go to beginning of this snippet](#simple_l10n)

### Objecttype Names

Objecttype names are stored at keys of the format `"schema.<table name>.name"`.

In this example, the translation for the `"main"` objecttype is found at the key `"schema.main.name"` and contains the german translation "Hauptobjekt" (`"de-DE"`), and the english translation "Main" (`"en-US"`).

### Column Names

Column names are stored at keys of the format `"schema.<table name>.column.<column name>"`. This applies to actual objecttypes as well as for nested tables.

### Mask Names

Mask names are stored at keys of the format `"mask.<mask id>.<mask name>.name"`.

----

[&rArr; 2. Structure of objects](../get_started_2_structure/)
