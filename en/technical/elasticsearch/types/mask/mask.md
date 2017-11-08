# Mask type

For each mask, there is a type called `mask-<mask_id>`. Depending on the mask properties, the mapping will be different.

This type contains a document for each object rendered with the mask \<mask-id\>. Notice that the same object may exist as document in
other types because its objecttype has several masks.

A mask can link other masks, so it is important to distinguish between the mapping of the "mask type" and the mapping of a certain mask.
In this article, the section "Type mapping" describes the attributes that are only found once for a mask type. The section "mask mapping"
contains the mapping for a mask.

## Type mapping

The type `mask-<mask_id>` contains the following fields plus the fields in "Mask mapping" for the mask \<mask-id\>.

| Field                     | Datatype     | Visible | Comments |
|---------------------------|--------------|---------|----------|
| `_all_text`               | object       | No      | All field for text fields |
| &#8614; `<lang>`          | Text         | No      | - l10n fields for language "lang" |
| &#8614; `not_localized`   | Text         | No      | - regular fields (not l10n) |
| `_all_string`             | String       | No      | All field for string fields |
| `_acl_allowed_user_ids`   | long         | No      | Users that are allowed to see this object (combined `read` rights from object, pool, tag and collection ACLs) |
| `_acl_allowed_group_ids`  | long         | No      | Groups that are allowed to see this object (combined `read` rights from object, pool, tag and collection ACLs) |
| `_pool_path_sort`         | L10n-sort    | No      | Sort field for pools (special sorting type "\_pool" for search). It exists also for non-pool objects, but it will always have the value **null** |
| `_tokens`                 | object       | No      | Tokens for suggest (`include_in_parent`) |
| &#8614; `field_name`      | string       | No      | - field name for this token, or **\_all** |
| &#8614; `text`            | Token-Text   | No      | - value, only if the token is a text token |
| &#8614; `string`          | Token-String | No      | - value, only if the token is a string token |
| `_linked`                 | object       | No      | Linked objects information (used by search element "in" with "objecttype") |
| &#8614; `_asset`          | Asset        | No      | - for each asset, the preferred version is mapped (`include_in_parent`) - see below: "Regular Fields" |
| &#8614; `<objecttype>`    | FacetInfo    | No      | - for each linked object, the facet information - ses below: "Links" |
| `_schema_version`         | long         | Yes     | User schema version used to render this object (see [metadata](/technical/elasticsearch/types/metadata/metadata.html) for more information) |
| `_changelog`              | Changelog    | Yes     | |
| `_collections`            | long         | Yes     | Array of collection IDs |
| `_tags`                   | long         | Yes     | Array of tag IDs (only for objecttypes with tags) |
| `_standard_flat`          | string       | No      | Flat representation of the `_path` field. This allows to get `_path` using "fields" |
| `_owner.user._id`         | long         | Yes     | Owner ID (only for users), in order to check the owner rights for the security filter |

## Mask mapping

The mask mapping consists of the following fields:

- common fields
- regular fields
- links
- nested tables
- reverse links (**TODO**)

If a mask is visited a second time in the same path when rendering an object, regular fields and links
are not rendered nor mapped. This prevents infinite loops.

### Common fields

| Field                      | Datatype  | Visible | Comments |
|----------------------------|-----------|---------|----------|
| `_mask`                    | string    | Yes     | Mask name |
| `_mask_id`                 | long      | No      | Mask ID: used internally to filter by mask |
| `_pool_id`                 | long      | No      | Pool ID: used internally to filter by pool; **null** if the object has no pool |
| `objecttype`               | string    | Yes     | Objecttype name |
| `objecttype_id`            | long      | No      | Objecttype ID: used internally to filter by objecttype |
| `_system_object_id`        | long      | Yes     | |
| `_global_object_id`        | string    | Yes     | |
| `_global_object_id_search` | string    | No      | Used to search the `_global_object_id` also by "local" |
| `_standard`                | object    | Yes     | |
| &#8614; `<order>`          | object    | Yes     | For `<order>` = 1,2,3 |
| &#8614; &#8614; `text`     | L10n      | Yes     | |
| `_standard_flat`           | string    | No      | Flat representation of the `_standard` field. This allows to get `_standard` using "fields" |
| `<objecttype_name>`        | object    | Yes     | |
| &#8614; `_id`              | long      | Yes     | |
| &#8614; `_version`         | long      | Yes     | |

Objecttypes with a pool link also have:

| Field                      | Datatype  | Visible | Comments |
|----------------------------|-----------|---------|----------|
| `<objecttype_name>._pool`  | Pool      | Yes     | **TODO**: pool properties |

Hierarchical objecttypes also have:

| Field                              | Datatype  | Visible |
|------------------------------------|-----------|---------|
| `_has_children`                    | bool      | Yes     |
| `_level`                           | long      | Yes     |
| `_path`                            | object    | Yes     |
| &#8614; `_global_object_id`        | string    | Yes     |
| &#8614; `_global_object_id_search` | string    | No      |
| &#8614; `<objecttype>`             | object    | Yes     |
| &#8614; &#8614; `_id`              | long      | Yes     |
| `<objecttype_name>._id_parent`     | long      | Yes     |

The following fields are not rendered when the mask is visited a second time:

- `<objecttype_name>._pool`
- `_level`
- `_path`

### Regular fields

For each mask field that is visible (i.e. "edit mode" is not "off"), an attribute is added.
Its datatype depends on the field type:

Regular fields are mapped according to their type as follows:

| Field                       | Easydb Type | Datatype    | Visible |
|-----------------------------|-------------|-------------|---------|
| `<objecttype_name>.<field>` | text        | Text-sort   | Yes     |
|                             | string      | String-sort | Yes     |
|                             | l10n        | L10n        | Yes     |
|                             | date        | Date        | Yes     |
|                             | daterange   | DateRange   | Yes     |

In the case of an asset, the contents of the preferred version of the asset are copied to a field called `<field>:preferred`. This field, and not
the original one is mapped as Asset. The original field is visible, but the new one is hidden.

| Field                                 | Datatype       | Visible |
|---------------------------------------|----------------|---------|
| `<objecttype_name>.<field>`           | *not mapped*   | Yes     |
| `<objecttype_name>.<field>:preferred` | Asset          | Yes     |

If a visible asset is found, the top-level mapping `_linked._asset` is created (see "Type mapping" above). When rendering an object, all linked assets
are appended to that field. Notice that assets are linked at top level, so, if an object links to another object, and the second one links to a
(visible) asset, the asset will be appended to the `_linked._asset` at top level. There are no `_linked` fields at mask level.

### Links

Visible links are defined by these conditions:

- "edit mode" is not "off"
- it is not an uplink
- it is not a self-reference

For each link in the mask that is visible:

- get the mask that should be used to render the linked object
- render the mask using the corresponding mask mapping (Note: not the top-level mapping)
- add the following fields:

| Field                      | Datatype       | Visible |
|----------------------------|----------------|---------|
| `<field>`                  | "mask mapping" | Yes     |
| `<field>._facet_term`      | **TODO**       | No      |
| `<field>._facet_term_self` | **TODO**       | No      |

If a visible link is found, the top-level mapping `_linked.<objecttype>` is created (see "Type mapping" above).
When rendering an object, the facet information for all linked objects is appended to that field.
This is similar to the asset links, but there is a list for each objecttype (see "Regular fields" above).

### Nested tables

If a nested table is visible (i.e. "edit mode" is not "off"), it is rendered using the provided mask
but with `include_in_parent` (as opposed to linked objects). This allows to search without a nested query.

The field is added like this:

| Field                           | Datatype       | Visible |
|---------------------------------|----------------|---------|
| `_nested:<nested_table>`        | "mask mapping" | Yes     |
