---
title: "212 - How To Get Started"
menu:
  main:
    name: "2. Structure of objects"
    identifier: "tutorials/get_started/get_started_2_structure"
    parent: "tutorials/get_started"

---

[&lArr; 1. Datamodel](../get_started_1_datamodel/)

[&rArr; 3. Searching for objects](../get_started_3_search/)

----

# 2. Structure of objects based on the user schema

[User objects](/en/technical/types/object/) are transported over the API as JSON objects. The objects consist of a fixed "header" and a key with the name of the objecttype which contains the actual data. The fields in the schema for this objecttype translate to database columns and to key-value-pairs in this sub object.

An example object for the `"main"` objecttype would have this (simplified) structure:

<a name="sample_object_main"></a>
{{< include_json "../samples/sample_object_main.jsonc" >}}
[&uArr; go to beginning of this snippet](#sample_object_main)

| Objecttype (table) | Field (column) | Column ID in schema | Type in schema | Path to the field in JSON | JSON type |
|---|---|---|---|---|---|
| `main` | `title` | 1 | `text_oneline` | `"main.title"` | `string` |
| `main` | `description` | 2 | `text_oneline` | `"main.description"` | `string` |
| `main` | `picture` | 3 | `eas` | `"main.picture"` | `array` |
| `main` | `place` | 4 | link to objecttype `place` | `"main.place"` | `object` |
| `main` | `keywords` |  | nested table | `"main._nested:main__keywords"` | `array` |
| `main__keywords` | `keyword` | 5 | link to objecttype `keyword` | `"main._nested:main__keywords.#.keyword"` | `object` |

Objects can be rendered in different [formats](/en/technical/types/object/#format). Linked objects are only included in the standard format, which means that only the standard is included, but the actual object needs to be loaded using the `_system_object_id` (see [below](#3-saving-and-loading-objects-from-the-database)).

## JSON objects over different API endpoints

This object format is the basis for all object operations over the api.

### Database API

It is used in the database api (`/api/v1/db/`) to [read](/en/technical/api/db/#retrieve-objects) and [write](/en/technical/api/db/#create-or-update-objects) objects directly from/to the database. This API can handle multiple objects. The objects are included in an array:

```
[
    {
        // object 1
    },
    {
        // object 2
    },
    ...
]
```

### Search API

The object structure is also used in search responses. The found objects are included in the `"objects"` array in the search result:

```
{
    "objects": [
        {
            // object 1
        },
        {
            // object 2
        },
        ...
    ]
}
```

----

[&lArr; 1. Datamodel](../get_started_1_datamodel/)

[&rArr; 3. Searching for objects](../get_started_3_search/)
