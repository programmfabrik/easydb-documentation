---
title: "132 - Objecttype"
menu:
  main:
    name: "Objecttype"
    identifier: "technical/types/objecttype"
    parent: "technical/types"
---
# Objecttype

Objecttypes are defined in the user [schema](/en/technical/types/schema), but main objecttypes can also have
some properties attached to them that can be changed without having any impact in the data model.
This type is used for that.

## Attributes

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `_basetype`                 | Name of the base type (string, r): **objecttype**                                                         |
| `_acl`                      | ACL (array of [acl entries](/en/technical/types/acl_entry), rw, optional)                                         |
| `_private_tags`             | Allow private tags to be set (boolean, rw, optional): defaults to **false**                               |
| `_tags`                     | Tags (array of [tag entries](/en/technical/types/tag_entry), rw, optional)                                        |
| `_maskfilters`              | Tag filters to be applied for each mask (see below, optional)                                             |
| `_columnfilters`            | Column filters (list of objects, rw, optional)                                                            |
| &#8614; `internal_name`     | internal name, has to be unique for each object type (string, rw, optional)                               |
| &#8614; `tagfilter`         | [tag filter](../tag_filter) |
| &#8614; `who`               | list of target users, as in [ACL entry](../acl_entry) |
| &#8614; `columns`           | list of column IDs |
| &#8614; `system_fields`     | object with column names of system fields as boolean values (rw, optional) |
| `_transitions`              | Transitions (array of [transitions](/en/technical/types/transition), rw, optional)                                |
| `_private_transitions`      | Private transitions flag (bool, rw, optional): defaults to **false**                                      |
| `_standard_masks`           | mask order to use for this objecttype (non-empty array of integer, optional, rw): ref [mask](/en/technical/types/maskset).mask\_id. If set to **null**, the standard mask is derived from the datamodel. |
| `_export_asset_filenames`   | per-field configuration of export filename, see [below](#export_asset_filenames).                         |
| `objecttype`                | Objecttype attributes:                                                                                    |
| &#8614; `_id`               | Objecttype ID (integer, unique, r\*): ref [table definition](/en/technical/types/schema).table\_id          |
| &#8614; `_version`          | Objecttype database version (integer, rw): detect and prevent concurrent updates.                         |
| &#8614; `name`              | Objecttype name (string, unique, r): ref [table definition](/en/technical/types/schema).name                |
| &#8614; `contact`           | Contact ([user (contact)](/en/technical/types/user), optional, rw)                                        |
| &#8614; `mapping_image_export`     | Export mapping image to be used for this objecttype (integer/string, optional, rw): either an ID or "none"       |
| &#8614; `mapping_image_import`     | Import mapping image to be used for this objecttype (integer/string, optional, rw): either an ID or "none"       |
| &#8614; `mapping_dc_export`        | Dublin Core mapping to be used for this objecttype (integer/string, optional, rw): either an ID or "none"       |
| &#8614; `description`       | Objecttype description ([l10n](/en/technical/types/l10n), optional, rw)                                           |
| &#8614; `show_in_collections` | Flag to save whether this Objecttype will be shown in the quick access panel of the search in the frontend (boolean, optional, rw, defaults to **false**) |

Remarks:

- `_id` has to be set for POST operations
- `_private_tags` and `_tags` only exist for objecttypes with `pool_link` set to **false**. See [tag management](/en/technical/tagmanagement).
- if `_standard_masks` contains a subset of all masks, only these will be indexed
- `_columnfilters.system_fields` is an object with any of the following keys for boolean values: `["parent", "owner"]` (system fields that have field rights)
  - if the value is **false** or not set, the system field will be not visible

## Mask filters

For each mask except the standard mask, a tag filter can be specified. When indexing objects, the newest version which fulfills the tag filter
is used (no tag filter means that the current version will be used). That means that the user can control which version of an object can be
found with a certain mask. It is possible for an object not to be indexed at all for a particular mask.

The attribute `_maskfilters` is a map from mask IDs to tag filters, like this:


{{< include_json "./maskfilters.json" >}}


<a name="export_asset_filenames"></a>

### Export filename templates

`_export_asset_filenames` is an object containing a localized filename template per asset field:


{{< include_json "./export_asset_filenames.json" >}}


The given template only specifies the filename base, the file extension is automatically added. The variables replaced (`%...%`) include fields from object record (e.g. `%bilder.name%`) and some special fields (e.g. `%_export.name%`). The following special fields are recognized:

| Variable         | Description         |
|------------------|---------------------|
| `%_asset.id%`    | EAS asset ID        |
| `%_asset.class%` | asset file class    |
| `%_asset.extension%` | asset extension |
| `%_asset.original_filename%` | base of original filename of asset (without extension) |
| `%_asset.technical_metadata.height%` | height of asset |
| `%_asset.technical_metadata.max_dimension%` | bigger value of width and height |
| `%_asset.technical_metadata.width%` | width of asset |
| `%_asset.version%` | version name of asset |
| `%_export.name%` | name of export |
| `%_global_object_id%` | global object ID of record |
| `%_system.easydb.name%` | name (ID) of easydb |
| `%_system_object_id%` | system object ID of record |

## Related operations

- [/objecttype](/en/technical/api/objecttype): set/get properties of objecttypes

