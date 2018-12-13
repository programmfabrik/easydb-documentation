---
title: "206 - Build Standard for Objects"
menu:
  main:
    name: "Build Standard for Objects"
    identifier: "technical/types/build_standard"
    parent: "technical/types"
---

# <a name="standard"></a> Building of standards for objects

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `order`                     | Order (integer, rw): `1`, `2`, `3`                                                                              |
| `design`                    | Design options (string, rw): **bold**, **normal** or **thin** (only for Text/HTML standard)                                            |
| `format`                    | Format options (string, rw): **brackets**, **newline**, **comma**, **semicolon**, **round-parentheses**, **square-brackets** (only for Text/HTML standard) |

The Server builds the standard and returns it in the following structure as part of the object response:

```!json
{
    "_standard": {
        "1": {
            "text": {
                "en-US": "Title"
            },
            "html": {
                "en-US": "<span class=\"ez-design-bold ez-format-comma\">Title</span>"
            }
        },
        "2": {
            "text": {
                "en-US": "Subtitle"
            },
            "html": {
                "en-US": "<span class=\"ez-design-normal ez-format-comma\">Subtitle</span>"
            }
        },
        "3": {
            "text": {
                "en-US": "Description"
            },
            "html": {
                "en-US": "<span class=\"ez-design-normal ez-format-comma\">Description</span>"
            }
        },
        "eas": {
            "1": [
                {
                    "_id": 1000012345
                }
            ]
        }
    }
}
```

## Building of the Text/HTML standards


For each Mask Field, that has standard properties set, the values are combined to build the standards **A** (Title), **B** (Subtitle) and **C** (Description). Hidden fields with standard properties are also rendered into the standard.

The `order` property defines for which standards the field value is used (`1` for **A**, `2` for **B**, `3` for **C**). The Frontend decides which of those parts will be displayed in which context.

**Example standard definition for a mask field:**

```!json
"standard": {
    "design": "bold",
    "format": "comma",
    "order": 1
}
```

Each standard has a text and a HTML representation, the property `design` is used to format the HTML output, but is ignored for the text output.

For each standard there is the following procedure to generate the representation:

- The field values for this standard are collected
  - The order of the fields in the mask is preserved for the order in the standard

- The fields values are concatenated using the delimiter that is specified in `format`
  - Different delimiters for fields with the same order number can be combined
  - Each field will be followed by the specified delimiter if it is not the last field

- Multilanguage fields are renderered in the current frontend language

- Empty fields are ignored and not concatenated
  - If all fields are empty, the System Object ID is used as a fallback (in the form "`#<_system_object_id>`")

### Standard and Fulltext Search:

All standards of any object are always added to the fulltext search. This means that for every field that is not enabled for the fulltext search, but is used for any of the standard fields, the object will be (indirectly) searchable for the value of the field.

### Linked Objects:

A field that contains a linked object is rendered by using the standard of the linked object with the highest order.

The rule to build the standard of a linked object is applied recursively. If a linked object contains linked objects itself that are used for the standard, also only the standard with the highest order is used. Since the recursive building of the standard of linked objects is unlimited in depth, the standard can get very long.

If the linked object has no standard (either it is not defined in the selected mask of the linked object, or all fields are empty), the System Object ID is used as the fallback.

### Nested Tables:

Each field value in the nested table is concatenated using the specified delimiter for the field. If the nested table is emtpy, it is not contained in the standard at all.

Since there is no limit for the number of fields in a nested table that are rendered into the standard, the standard can get very long.

For linked objects in nested tables, the general rule to build the standard of linked objects also applies.

### Reverse Nested Tables:

<!-- TODO: check how reverse links are handled for standard -->

Fields from Reverse Nested Fields are never contained in a standard.

## <a name="standard_eas"></a> Building of the Asset (EAS) standards

Asset Fields can also be set for a standard with an `order`, which means that these assets are to be displayed in the standard of the object. For using an asset for the standard, is it possible to select multiple asset fields. Since only one asset is displayed as the standard, the first available asset is displayed (the order of the asset fields in the mask is preserved).

**Example standard definition for a mask field:**

```!json
"standard_eas": {
    "order": 1
}
```

To use the asset in a linked object as the standard of the main object, the linked object must be selected for the asset standard. At least one asset field must also be selected for the standard in the mask of the linked object.

