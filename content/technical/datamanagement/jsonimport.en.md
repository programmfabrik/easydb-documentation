---
title: "86 - JSON Import"
menu:
  main:
    name: "JSON Import"
    identifier: "technical/datamanagement/jsonimport"
    parent: "technical"
---
# Object Import with JSON Payloads

Using the [frontend JSON Importer](../../../webfrontend/datamanagement/lists/jsonimport), objects can be imported into the Easydb by uploading files with objects that are conform to the [API requirements of objects](../../types/object).

## Server Lookups for IDs

When objects and basetypes are imported, they are not saved in the database yet and have no ID yet. To link to objects and basetypes in the migration payloads, instead of using IDs lookups for these IDs can be defined. In the server, these lookup keywords are used to replace the lookup object with the correct ID of the object.

A lookup is a JSON object that is used instead of the ID (integer). It defines a column in the database that contains the unique value that is referenced. The reference value must exist in the database during the time of the import, must be unique, and known when the payloads are created.

The column can be a standard reference column (`"reference"` for all basetypes Tag, Tag Group, User, Group, Pool, Collection and Message), any unique text field in a user object, or an extra reference field. The name of the reference column must be known during the creation of the payloads.

Lookups generally are only considered in PUT/POST requests. They are ignored in any other request type. Lookups are never returned by the API, but instead the original ID as the result of the lookup is returned.

### General structure

The structure of all lookup objects is

```javascript
"lookup:<type of id>": {
    "<reference column>": "<reference value>"
}
```

The use of more keys in the lookup object would cause an API Error, since the server can not determine which of the keys would be the name of the reference column in the database. The only exception is a lookup for an object with an arbitrary objecttype (used for example when objects are linked to collections).

In this case, the keyword `"_objecttype"`, which defines the table, is also allowed in the lookup object:

```javascript
"lookup:_id": {
    "<reference column>": "<reference value>",
    "_objecttype": "<objecttype = reference table name>"
}
```

The server performs a lookup in the database by returning the ID of the object or basetype that has the value `"reference_to_linked_object_5804d0ce"` in the column `"reference"`.

If there is no result for this query, or more then one, the lookup failed and an API Error is thrown. In this case, the complete batch failed and the lookup must be fixed.

#### Example:

To create a link to an object in the payload

```javascript
{
    "lk_linkedobject_id": {
        "linkedobject": {
            "lookup:_id": {
                "reference": "reference_to_linked_object_5804d0ce"
            }
        },
        "_objecttype": "linkedobject",
        "_mask": "_all_fields"
    }
}
```

would be used instead of referencing the linked object with its ID:

```javascript
{
    "lk_linkedobject_id": {
        "linkedobject": {
            "_id": 87654
        },
        "_objecttype": "linkedobject",
        "_mask": "_all_fields"
    }
}
```

### Lookup Keywords

The JSON keys for the lookups are keywords that can not be used for other keys, else the import would fail.

#### `lookup:_id`

Perform a lookup for the ID of an object or basetype in the current table. Objects with arbitrary object types require the key `"_objecttype"` as well.

Lookups for an ID can be performed for:

- [Linked objects](/en/technical/types/object/#object-attributes)
  - A unique text or string field for `reference` must be added in the datamodel
  - It is also possible to use any other unique field that might already exist in the datamodel for this objecttype
  - See [example above](#example)
- [Pools](/en/technical/types/pool)
  - Add an object to a pool
  - Use the `reference` field as a field that is always unique (must be set for non-system-pools)
  - See [example below](#example-lookup-for-pool-id)
- [Tags](/en/technical/types/tag/)
  - Add a tag to an object
  - Use the `reference` field as a field that is always unique (must be set for all tags)
  - See [example below](#example-lookup-for-tag-id)
- [Tag Groups](/en/technical/types/tag/#taggroup)
  - Add a tag to a tag group
  - Use the `reference` field as a field that is always unique (must be set for all tag groups)
- [Groups](/en/technical/types/group/)
  - Add a user to a group
  - Use the `reference` field as a field that is always unique (must be set for all groups)
  - See [example below](#example-lookup-for-group-id)

#### `lookup:_id_parent`

Perform a lookup for the parent ID of an object or basetype in the current table. This is used to add the parent-child-relation to a hierarchical basetype or user object.

Lookups for a parent ID can be performed for:

- [Hierarchical objects](/en/technical/types/object/#object-attributes)
- [Pools](/en/technical/types/pool)
  - Set a pool as the child of another pool
- [Collections](/en/technical/types/collection/)
  - Set a collection as the child of another collection
  - See [example below](#collections)

#### `lookup:_global_object_id`

Perform a lookup for the global object ID of a user object. Lookups for the global ID can be performed for:

- Objects in a collection
  - This also requires the key `"_objecttype"`

Inside `webfrontend_props` for presentations of collections, the format is `lookup:global_object_id`, without the underscore. See [example below](#collections).

## manifest.json

This file is useful to fill the JSON Importer form, therefore all values are optional.

```javascript
{
    "source": "Some name",
    "batch_size": 100,
    "payload_base_uri": "",
    "payloads": [
        "payload_1.json",
        "payload_2.json"
    ]
}
```

## Basetypes payloads

### Groups

```javascript
{
    "import_type": "group",
    "groups": [
        {
            <group object>
        }
    ]
}
```

#### Default References for System Groups

All System Basetypes have predefined, read only references. The references have the form `system:<internal name>`.

For example the group "All users" (internal name `:all`) has the reference `system::all`.

### Users

```javascript
{
    "import_type": "user",
    "users": [
        {
            <user object>
        }
    ]
}
```

#### Example lookup for Group ID

This will add the group with the reference `"ref_group_1"` to the user:

```javascript
[
    {
        "_basetype": "user",
        "user": {},
        "_groups": [
            {
                "_basetype": "group",
                "group": {
                    "lookup:_id": {
                        "reference": "ref_group_1"
                    }
                }
            }
        ]
    }
]
```

#### Default References for System Users

The references have the form `system:<login name>`.

For example the root user (login name `root`) has the reference `system:root`.

### Pools

```javascript
{
    "import_type": "pool",
    "pools": [
        {
            <pool object>
        }
    ]
}
```

#### Default References for System Pools

The references have the form `system:<internal_unique_id>`.

For example the standard pool (internal_unique_id `standard`) has the reference `system:standard`.

#### Example lookup for Pool ID

This will set the pool for the object of type `<objecttype>` to the Standard Pool (which has the reference `"system:standard"`):

```javascript
[
    "<objecttype>": {
        "_pool": {
            "pool": {
                "lookup:_id": {
                    "reference": "system:standard"
                }
            }
        },
        ...
    }
]
```
### Tags

Tags and Taggroups are sent together in one package to the server. All existing Taggroups and Tags are replaced.

```javascript
{
    "import_type": "tags",
    "tags": [
        {
            <tags object>
        }
    ]
}
```

#### Example lookup for Tag ID

This will add the Tag with the reference `"ref_tag_1"` to the object of type `<objecttype>`:

```javascript
[
    "<objecttype>": { ... },
    "_tags": [
        {
            "lookup:_id": {
                "reference": "ref_tag_1"
            }
        }
    ]
]
```

### Collections

```javascript
{
    "import_type": "collection",
    "collections": [
        {
            "_basetype": "collection",
            "collection": {
                "displayname": {
                    "de-DE": "Neue Mappe"
                },
                "description": {
                    "de-DE": "Eine freigegebene Mappe für Ticket: #44450"
                },
                "webfrontend_props": {
                    "presentation": {
                        "settings": {
                            "show_info": "no-info"
                        },
                        "slide_idx": 0,
                        "slides": [
                            {
                                "type": "start",
                                "data": {
                                    "info": "",
                                    "title": "A title"
                                }
                            },
                            {
                                "type": "duo",
                                "left": {
                                    "lookup:global_object_id": {
                                        "_objecttype": "bilder",
                                        "reference_column": "reference-value"
                                    }
                                },
                                "right": {
                                    "global_object_id": "58@b40f205b-fa95-48cc-b9f2-dfad8fcaa641"
                                }
                            },
                            {
                                "type": "one",
                                "center": {
                                    "global_object_id": "58@b40f205b-fa95-48cc-b9f2-dfad8fcaa641"
                                }
                            }
                        ]
                    }
                }
            },
            "_objects": [
                {
                    "_global_object_id": "14@e84132d0-9173-444c-ab66-cbd7cce0baf4",
                    "_webfrontend_props": null
                },
                {
                    "_global_object_id": "14@e84132d0-9173-444c-ab66-cbd7cce0baf4",
                    "_webfrontend_props": null
                },
                {
                    "lookup:_global_object_id": {
                        "_objecttype": "bilder",
                        "reference": "Bilder:15"
                    },
                    "_webfrontend_props": null
                }
            ]
        }
    ]
}
```

### Objects

The "import_type" for objects is always "db", and it is necessary to add a new attribute to specify the object type.

```javascript
{
    "objecttype": "bilder",
    "import_type": "db",
    "objects": [
        {
            "bilder": {
                "_id": null,
                "_version": 1,
                "file": [
                    {
                        "preferred": true,          // mark image as the preview version
                        "eas:url": "http://127.0.0.1:8887/json/image.jpg",
                        "eas:preview:url": "http://127.0.0.1:8887/image-preview.jpg",
                        "eas:filename": "image.jpg" // overwrite http header
                    }
                ],
                "titel": "Title"
            },
            "_mask": "bilder__all_fields",
            "_objecttype": "bilder"
        }
    ]
}
```

#### Default References for System Collections

The references have the form `system:<internal_unique_id>`.

For example the collection "All Collections" (internal_unique_id `root`) has the reference `system:root`.

#### Default References for User Collections

User collections are system collections that are created when a new user is created. Also all system users have user collections.

##### System User Collections

The references for system user collections have the form `user:ref:<user reference>`.

For example the user collection of the root user (user reference `system:root`) has the reference `user:ref:system:root`.

##### User Collections

The references for other (non-system-user) user collections have the form `user:<user reference type>:<unique user identification>`. The user identification is formed from three user fields, that are unique and at least one of them is always set:

1. **User reference**
 - If the user reference is set, the user collection reference has the format `user:ref:<user reference>`

2. **User login**
 - Fallback, if user reference is not set
 - If the user login is set, the user collection reference has the format `user:login:<user login>`

3. **User ID**
 - Fallback, if user reference and user login are not set
 - If the user ID is set, the user collection reference has the format `user:id:<user ID>`

For example the user collection of a user with the ID `123`, but without reference and login, has the reference `user:id:123`


<!--
### References for

... coming ...
-->

### Update objects

It is possible to update existing objects by adding the attributes **_id** and **"_version:auto_increment": true**. When the attribute **_version:auto_increment** is set, the client will fetch the existing object by its **_id** and the version will be incremented.

```javascript
{
    ...
    "bilder": {
        "_id": 1,
        "_version:auto_increment": true,
        "file": [
            {
                "eas:url": "http://127.0.0.1:8887/json/image.jpg",
                "eas:preview:url": "http://127.0.0.1:8887/image-preview.jpg"
            }
        ],
        "titel": "Title"
    },
    ...
}
```

If the **_id** is not available, it is posible to use the lookup feature by adding the attribute **lookup:_id** instead of **_id**. This **lookup** has a client side implementation, where the object's **_id** will be fetched from the server by using the given reference, and then the version will be incremented.

```javascript
{
    ...
    "bilder": {
        "lookup:_id": {
            "reference_field": "reference_value"
        },
        "_version:auto_increment": true,
        "file": [
            {
                "eas:url": "http://127.0.0.1:8887/json/image.jpg",
                "eas:preview:url": "http://127.0.0.1:8887/image-preview.jpg"
            }
        ],
        "titel": "Title"
    },
    ...
}
```
