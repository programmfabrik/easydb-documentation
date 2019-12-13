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

Lookups for IDs of other user objects or basetypes can be used in the payloads. See [detailled information about lookups](/en/technical/datamanagement/lookups/).

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
                                    "global_object_id": "58@b40f205b-fa95-48cc-b9f2-dfad8fcaa641"
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

### Update objects

It is possible to update existing objects by adding the attributes **_id** and **"_version:auto_increment": true**. When the attribute **_version:auto_increment** is set, the client will fetch the existing object by its **_id** and the version will be incremented.

The update works in a way that the existing data is not replaced, it only updates the fields that don't contain data.


```javascript
{
  ...
    "bilder": {
      "_id": 1,
      "_version:auto_increment": true,
      "file": [{
         "eas:url": "http://127.0.0.1:8887/json/image.jpg",
         "eas:preview:url": "http://127.0.0.1:8887/image-preview.jpg"
      }],
      "titel": "Title"
    },
  ...
}
```
For nested fields it is possible to append new data to existing data by using the group mode 'append'.

```javascript
{
  ...
    "bilder": {
      "_id": 1,
      "_version:auto_increment": true,
      "_nested:keywords": [{
      	...   
      }],
      "_nested:keywords:group_mode": "append"
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
