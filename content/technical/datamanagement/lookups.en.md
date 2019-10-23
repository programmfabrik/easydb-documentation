---
title: "205 - Lookups for IDs"
menu:
  main:
    name: "Lookups for IDs"
    identifier: "technical/datamanagement/lookups"
    parent: "technical"
---

# Lookups for IDs

When objects and basetypes are imported, they are not saved in the database yet and have no ID yet. To link to objects and basetypes in the migration payloads, instead of using IDs lookups for these IDs can be defined. In the server, these lookup keywords are used to replace the lookup object with the correct ID of the object.

A lookup is a JSON object that is used instead of the ID (integer). It defines a column in the database that contains the unique value that is referenced. The reference value must exist in the database during the time of the import, must be unique, and known when the payloads are created.

The column can be a standard reference column (`"reference"` for all basetypes Tag, Tag Group, User, Group, Pool, Collection and Message), any unique text field in a user object, or an extra reference field. The name of the reference column must be known during the creation of the payloads.

Lookups generally are only considered in PUT/POST requests. They are ignored in any other request type. Lookups are never returned by the API, but instead the original ID as the result of the lookup is returned.

## General structure

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

## Lookup Keywords

The JSON keys for the lookups are keywords that can not be used for other keys, else the import would fail.

### `lookup:_id`

Perform a lookup for the ID of an object or basetype in the current table. Objects with arbitrary object types require the key `"_objecttype"` as well.

Lookups for an ID can be performed for:

- [Linked objects](/en/technical/types/object/#object-attributes)
  - A unique text or string field for `reference` must be added in the datamodel
  - It is also possible to use any other unique field that might already exist in the datamodel for this objecttype
  - See [example below](#example-lookup-for-id-of-linked-objects)
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

### `lookup:_id_parent`

Perform a lookup for the parent ID of an object or basetype in the current table. This is used to add the parent-child-relation to a hierarchical basetype or user object.

Lookups for a parent ID can be performed for:

- [Hierarchical objects](/en/technical/types/object/#object-attributes)
- [Pools](/en/technical/types/pool)
  - Set a pool as the child of another pool
- [Collections](/en/technical/types/collection/)
  - Set a collection as the child of another collection
  - See [example below](#collections-and-collection-objects)

### `lookup:_global_object_id`

Perform a lookup for the global object ID of a user object. Lookups for the global ID can be performed for:

- Objects in a collection
  - This also requires the key `"_objecttype"`

Inside `webfrontend_props` for presentations of collections, the format is `lookup:global_object_id`, without the underscore. See [example below](#collections-and-collection-objects).

## User objects

### Example lookup for ID of linked objects

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
This only works if there is a unique column `reference` in the objecttype. A specific column that is only used for referencing other objects can be added to the datamodel, or any unique column that is already in the objecttype can be used. Lookups can only be performed, if the reference value is found exactly once in the reference column in the database.

The reference column can contain any string value to reference other objects. The reference value must be set in the referenced object. In this example, the parent object must exist:

```javascript
{
    "linkedobject": {
        "_id": 123,
        "reference": "reference_to_linked_object_5804d0ce"
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

### Example lookup for parent ID of hierarchical objects

The lookup for `_id_parent`

```javascript
{
    "object": {
        "lookup:_id_parent": {
            "reference": "object:123"
        }
    }
}
```

would be used instead of referencing the parent object with its ID:

```javascript
{
    "object": {
        "_id_parent": 123
    }
}
```


## Groups

### Example lookup for Group ID

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

### Default References for System Users

The references have the form `system:<login name>`.

For example the root user (login name `root`) has the reference `system:root`.

## Pools

### Default References for System Pools

The references have the form `system:<internal_unique_id>`.

For example the standard pool (internal_unique_id `standard`) has the reference `system:standard`.

### Example lookup for Pool ID

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

### Example lookup for parent ID of a Pool

This will set the parent pool the pool to the Standard Pool (which has the reference `"system:standard"`):

```javascript
[
    {
        "_basetype": "pool",
        "pool": {
            "lookup:_id_parent": {
                "reference": "system:standard"
            }
        }
    }
]
```

## Tags

### Example lookup for Tag ID

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

## Collections and Collection Objects

For collections and collection objects, the following lookups are possible:

* Lookup for a parent collection: `"lookup:_id_parent"`
* Lookup for a user object in a presentation slide: `"lookup:global_object_id"`
* Lookup for a user object in the collection: `"lookup:_global_object_id"`

Please note the different lookup keys `"lookup:global_object_id"` and `"lookup:_global_object_id"`.

### Default References for System Collections

The references have the form `system:<internal_unique_id>`.

For example the collection "All Collections" (internal_unique_id `root`) has the reference `system:root`.

### Default References for User Collections

User collections are system collections that are created when a new user is created. Also all system users have user collections.

#### System User Collections

The references for system user collections have the form `user:ref:<user reference>`.

For example the user collection of the root user (user reference `system:root`) has the reference `user:ref:system:root`.

#### User Collections

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

### Example lookups

```javascript
{
    "import_type": "collection",
    "collections": [
        {
            "_basetype": "collection",
            "collection": {
                "lookup:_id_parent": {
                    "reference": "user:ref:system:root"
                },
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
                                "type": "one",
                                "center": {
                                    "lookup:global_object_id": {
                                        "_objecttype": "bilder",
                                        "reference_column": "reference-value"
                                    }
                                }
                            }
                        ]
                    }
                }
            },
            "_objects": [
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
