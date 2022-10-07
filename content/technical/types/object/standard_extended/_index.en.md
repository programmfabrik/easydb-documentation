---
title: "1312 - Object Format standard_extended"
menu:
  main:
    name: "Object Format standard_extended"
    identifier: "technical/types/object/standard_extended"
    parent: "technical/types/object"
---

# Object Format `standard_extended`

> Attention: this feature is **only available in [fylr](http://fylr.io/)**. It is not available in easydb5!

The `standard_extended` format for objects provides the object data in a fixed structure. It can be displayed by using a generic parser without any knowledge about the database schema.

## System fields

The `standard_extended` format is an extension of an object in **standard** format, that only adds new fields without changing anything else in the object compared to other formats.

The following fields are additionaly included in this format and contain translations for the names of system fields:

* `_objecttype_display_name`
  * The display name of the objecttype in mutltiple languages ([see below](#multilanguage-values))
  * correlates to `_objecttype`
* `_mask_display_name`
  * The display name of the mask in mutltiple languages
  * correlates to `_mask`
* `_tags`
  * List of tags, includes the following fields:
    * `_id`: ID of the tag
    * `displayname`: display name of the tag in mutltiple languages
    * `reference` (optional): Reference of the tag, if it is set
    * `shortname` (optional): Shortname of the tag, if it is set
* `_values`
  * List of fields and data ([see below](#list-of-values))

All other [system fields](/en/technical/types/object/#attributes) are available as well. These field names are always fix.

## List of values

All object data is in a list `_values`, where each list element has the following structure:

* `api_name`
  * string, mandatory
  * internal technical name of the field
* `display_name`
  * object, mandatory
  * contains the name of the field in multiple languages
  * the display name for each language can be display as is
* `type`
  * string, mandatory
  * describes the data type of the field
  * is also used as the key to access the actual data of the field in this object
  * possible values are:
    * [`text`](#text)
    * [`text_loca`](#text_loca)
    * [`number`](#number)
    * [`bool`](#bool)
    * [`date`](#date)
    * [`date_range`](#date_range)
    * [`custom`](#custom)
    * [`file`](#file)
    * [`linked_object`](#linked_object)
    * [`nested`](#nested)
    * [`reverse_nested`](#reverse_nested)
* data (key with the same name as the value of `type`)
  * mandatory
  * the data type depends on `type`
  * some data can be displayed as is, some needs parsing

### text

A string that can be displayed as is.

**Example:**

```!javascript
{
  "api_name": "reference",
  "display_name": {
    "de-DE": "Referenz",
    "en-US": "Reference"
  },
  "type": "text",
  "text": "Ref 1"
}
```

### text_loca

An object with data in multiple languages.

**Example:**

```!javascript
{
  "api_name": "name",
  "display_name": {
    "und": "name"
  },
  "type": "text_loca",
  "text_loca": {
    "de-DE": "Deutscher Text",
    "en-US": "English Text"
  }
}
```

### number

An object that contains a numeric value in integer or float format:

* `number`
  * number value that can be displayed as is
* `print`
  * a rendered string that can be displayed as is
  * the print value is localized in the first data language which is configured for the user

**Example:**

```!javascript
{
  "api_name": "currency",
  "display_name": {
    "de-DE": "Währung",
    "en-US": "Currency"
  },
  "type": "number",
  "number": {
    "number": 2.57,
    "print": "2,57"
  }
}
```

### bool

`true` / `false`, can be displayed as is or be parsed.

**Example:**

```!javascript
{
  "api_name": "yes_no",
  "display_name": {
    "de-DE": "Ja / Nein",
    "en-US": "Yes / No"
  },
  "type": "bool",
  "bool": true
}
```

### date

An object that contains data of a timestamp (date and time), using the following fields:

* `to`
  * start timestamp of the date range in ISO8601 format
* `from`
  * end timestamp of the date range in ISO8601 format
* `print`
  * a rendered string that can be displayed as is
  * the date value is rendered as short and simple as possible

**Example:**

```!javascript
{
  "api_name": "date",
  "display_name": {
    "de-DE": "Datum",
    "en-US": "Date"
  },
  "type": "date",
  "date": {
    "from": "2022-02-12T00:00:00Z",
    "to": "2022-02-12T23:59:59Z",
    "print": "2022-02-12"
  }
}
```

The values `from` and `to` do not define a date range, but are used to define the granularity of the date.

```
{
  "from": "2021-12-01T00:00:00Z",
  "to": "2021-12-31T23:59:59Z"
}
```

would be used for the whole month of december 2021, without specifying a day. The resulting `print` value would be `2021-12`.

### date_range

An object that contains data of a date range following fields:

* `to`
  * start timestamp of the date range in ISO8601 format
* `from`
  * end timestamp of the date range in ISO8601 format
* `print`
  * a rendered string that can be displayed as is
  * the date range value is rendered as short and simple as possible

**Example:**

```!javascript
{
  "api_name": "daterange",
  "display_name": {
    "de-DE": "Datumsbereich",
    "en-US": "Date Range"
  },
  "type": "date_range",
  "date_range": {
    "from": "2009-01-01T00:00:00Z",
    "to": "2019-12-31T23:59:59Z",
    "print": {
      "und": "2009 - 2019"
    }
  }
}
```

### custom

A complex object that contains data of a custom data type field:

* `_standard`
  * an object that contains the standard of the custom data type in multiple languages
* `_values`
  * list of fields in the custom data type
  * the values are based on the [search mapping](/en/technical/plugins/customdatatype/#search-mapping) that is defined in the `manifest.yml` of the custom datatype plugin

**Example:**

```!javascript
{
  "api_name": "custom",
  "display_name": {
    "und": "Custom"
  },
  "type": "custom",
  "custom": {
    "_standard": {
      "de-DE": "Custom Datentyp",
      "en-US": "Custom Data Type"
    },
    "_values": [
      {
        "api_name": "locafield",
        "display_name": {
          "und": "locafield"
        },
        "text_loca": {
          "de-DE": "loca DE",
          "en-US": "loca US"
        },
        "type": "text_loca"
      },
      [...]
    ]
  }
}
```

### file

An object with [data about a linked file](/technical/types/asset/#attributes), includes file information, urls and technical metadata.

To download / display / embed the image, the provided `url` can be used.

**Example:**

```!javascript
{
  "api_name": "file",
  "display_name": {
    "de-DE": "Datei",
    "en-US": "File"
  },
  "type": "file",
  "file": {
    "technical_metadata": {
      "extension": "jpg",
      [...]
    },
    "versions": {
      "original": {
        "url": "http://...",
        [...]
      },
      "preview": {
        "url": "http://...",
        [...]
      },
      [...]
    },
    [...]
  }
}
```

### linked_object

An object with information about a linked object (in standard format)

**Example:**

```!javascript
{
  "api_name": "link_keyword",
  "display_name": {
    "de-DE": "Schlagwort",
    "en-US": "Keyword"
  },
  "type": "linked_object",
  "linked_object": {
    "_mask": "keywords__all_fields",
    "_mask_display_name": {
        "und": "keywords__all_fields"
    },
    "_objecttype": "keyword",
    "_objecttype_display_name": {
        "und": "Keyword"
    },
    "_standard": {
      [...]
    },
    "_system_object_id": 6,
    "keyword": {
      "_id": 3,
      "_version": 1,
      [...]
    },
    [...]
  }
}
```

### nested

Nested tables are lists of lists of values. The outer list contains multiple entries in the nested table. The inner list contains rows in the nested table entry and has the same structure as `_values` in the top level object. Nested tables can be parsed using the same parsing algorithm and applying it in a recursive way.

**Example:**

```!javascript
{
  "api_name": "_nested:object__techniques",
  "display_name": {
      "de-DE": "Techniken",
      "en-US": "Techniques"
  },
  "type": "nested",
  "nested": [
    [
      {
        "api_name": "remark",
        "display_name": {
          "und": "remark"
        },
        "type": "text",
        "text": "Test Keyword"
      },
      {
        "api_name": "link_keyword",
        "display_name": {
          "de-DE": "Schlagwort",
          "en-US": "Keyword"
        },
        "type": "linked_object",
        "linked_object": {
          "_mask": "keywords__all_fields",
          "_mask_display_name": {
            "und": "keywords__all_fields"
          },
          "_objecttype": "keyword",
          "_objecttype_display_name": {
            "und": "Keyword"
          },
          "_standard": {
            [...]
          },
          "_system_object_id": 6,
          "keyword": {
            "_id": 3,
            "_version": 1,
            [...]
          }
        }
      },
      [...]
    ],
    [
      [...]
    ]
  ]
}
```

### reverse_nested

Reverse nested tables are lists of reverse linked objects, each entry is an object which only contains a sub set of the system fields and `_values`.

Most important difference is that `_id` and `_version` are not included in the sub object for the object, but are on top level.

**Example:**

```!javascript
{
  "api_name": "_reverse_nested:images:lk_nested_id",
  "display_name": {
    "de-DE": "Revers verlinkt: Bilder",
    "en-US": "Reverse nested: Images"
  },
  "type": "reverse_nested",
  "reverse_nested": [
    {
      "_objecttype": "images",
      "_objecttype_display_name": {
        "en-US": "Images",
        "de-DE": "Bilder"
      },
      "_id": 1,
      "_global_object_id": "5@...",
      "_system_object_id": 5,
      "_version": 1,
      "_values": [
        [...]
      ]
    },
    [...]
  ]
}
```

## Multilanguage values

If a value is available in multiple langauges, the value is an object with a simple key-value-structure.

Depending on the configured languages, there can be multiple different language codes as keys in this object. The value for each key is the translation in this language. If the objects are to be rendered in a specific language, this object can be filtered for the language. If the value is not language specific, it is included at the key `und` (for undefined). This value can also be used as a fallback language.

