# Collection

A collection is a container for objects. Collections are used to organize and share objects
with other users. Objects from any object type can be stored to a collection, and they can
belong to multiple collections (unlike pools).

The collections build a hierarchy, which is represented by the relation `collection._id_parent`
in the collection object. When searching collections, easydb offers special attributes relating to
the collection hierarchy (`_path` and `_level`).

Easydb creates automatically some "system collections". These collections cannot be deleted or moved in the collection
hierarchy (that is, change their `_id_parent`).

## Attributes

| Name                           | Description                                                                                                  | Search        |
|--------------------------------|--------------------------------------------------------------------------------------------------------------|---------------|
| `_basetype`                    | Name of the base type (string, r): **collection**                                                            |               |
| `_owner`                       | Owner of this collection ([user (short)](/technical/types/user/user.html#short), r): see below                              | Number(\*) |
| `_acl`                         | ACL (array of [acl entries](/technical/types/acl_entry/acl_entry.html), rw, optional)                                            | *not present* |
| `_private_acl`                 | Marks the ACL as private (see [rights management](/technical/rightsmanagement/rightsmanagement.html)) (bool, rw, optional): defaults to **false** | *not present* |
| `_has_children`                | Whether this collection has nested collections (boolean, r)                                                  | Boolean       |
| `_has_acl`                     | Whether this collection has a non-empty ACL (boolean, r)                                                     | Boolean       |
| `_level`                       | Level of this collection in the hierarchy (integer, r)                                                       | Number(\*)    |
| `_path`                        | Path to this collection (array of collections, r)                                                            | (\*)          |
| `_count`                       | Number of objects in the collection (integer, r)                                                             | Number        |
| `_create_object_compiled`      | Effective create object properties, as inherited from ancestors (r): see below                               |               |
| `_generated_rights`            | Rights that the session user has for the collection ([rights specification](/technical/types/right/right.html#specification)): bag_read, bag_write, bag_delete, bag_acl, bag_create, link, unlink |
| `_hotfolder_upload_urls`       | Hotfolder URLs (object, r): only shown if the hotfolder is configured and the collection allows uploads      |               |
| `_set_spec`                    | OAI/PMH name for this set |
| `collection`                   | Collection attributes:                                                                                       |               |
| &#8614; `_id`                  | Collection ID (integer, unique, r\*)                                                                         | Number        |
| &#8614; `_id_parent`           | Parent collection ID (integer, rw)                                                                           | Number        |
| &#8614; `_version`             | Collection version (integer, rw)                                                                             | Number        |
| &#8614; `is_system_collection` | Whether this is a system collection (boolean, r)                                                             | Boolean       |
| &#8614; `displayname`          | Collection name ([l10n](/technical/types/l10n/l10n.html), unique for collections with the same parent, rw)                  | L10n (all)    |
| &#8614; `description`          | Collection description ([l10n](/technical/types/l10n/l10n.html), optional, rw)                                              | L10n (all)    |
| &#8614; `type`                 | Collection type (string, optional, rw)                                                                       | Text          |
| &#8614; `children_allowed`     | Whether this collection is allowed to have nested collections (boolean, optional, rw): defaults to **false** |               |
| &#8614; `objects_allowed`      | Whether this collection is allowed to contain objects (boolean, optional, rw): defaults to **false**         |               |
| &#8614; `webfrontend_props`    | Extra properties that the frontend can set and retrieve (object, optional, rw)                               |               |
| &#8614; `create_object`        | Configuration for objects that are directly created in the collection (rw, optional, nullable): see below    |               |
| &#8614; `uuid`                 | Collection UUID (text, unique, r)                                                                            |               |

The following fields are only present when searching: `_has_acl`, `_level`, `_path`.

Remarks:

- `_id` has to be set for POST operations
- the hierarchy begins at level 1. The array in `_path` only contains the fields `_basetype`, `_has_acl`, `_count` and `collection`
- `_path.collection._id` is searchable as a Number
- the fields `_level` and `_path` are only provided by `/api/search`
- `_groups.group._id` is searchable as Number
- `_owner.user._id` is searchable as Number

Notice that all collections must have a valid `_id_parent` (except for the root collection, which is a system collection).

### webfrontend_props

#### presentation

| Name                              | Type                 | Description                                                                               |
|-----------------------------------|----------------------|-------------------------------------------------------------------------------------------|
| `settings`                        | PlainObject          |                                                                                           |
| &#8614; `show_info`               | String               |  Values: "standard-info" or "no-info"                                                     |
| `slide_idx`                       | Number               |  Frontend position for the current slide which is shown on load                           |
| `slides`                          | Array of PlainObject |                                                                                           |
| &#8614; `type`                    | String               |  Values: "start", "one", "duo", "bullets"                                                 |
| &#8614; `data`                    | PlainObject          |  It's set if type is "start" or "bullets"                                                 |
| &#8614; &#8614; `title`           | String               |                                                                                           |
| &#8614; &#8614; `info`            | String               |  Description multiline                                                                    |
| &#8614; `center`                  | PlainObject          |  It's set if type is "one"                                                                |
| &#8614; &#8614; `global_object_id`| String               |  ID of the referenced and shown object                                                    |
| &#8614; `left`                    | PlainObject          |  It's set if type is "duo"                                                                |
| &#8614; &#8614; `global_object_id`| String               |  ID of the referenced and shown object                                                    |
| &#8614; `right`                   | PlainObject          |  It's set if type is "duo"                                                                |
| &#8614; &#8614; `global_object_id`| String               |  ID of the referenced and shown object                                                    |

##### slide types

- **start**: Includes a title and a description
- **one**: Possibility to add an object
- **duo**: Possibility to add two objects vertically rendered
- **bullets**: Almost the same as **start** slide, with the difference that the description will have a bullet for each newline.

##### Example

```json
"presentation": {
    "settings": {
        "show_info": "standard-info"
    },
    "slide_idx": 0,
    "slides": [
        {
            "type": "start",
            "data": {
                "info": "This is a long description.",
                "title": "Presentation title"
            }
        },
        {
            "type": "one",
            "center": {
                "global_object_id": "2@aefb0f5c-75b1-4779-a128-1264d527cabb"
            }
        },
        {
            "type": "duo",
            "left": {
                "global_object_id": "2@aefb0f5c-75b1-4779-a128-1264d527cabb"
            },
            "right": {
                "global_object_id": "4@aefb0f5c-75b1-4779-a128-1264d527cabb"
            }
        },
        {
            "type": "bullets",
            "data": {
                "info": "Bullet 1\nBullet 2\nBullet 3\nBullet 4",
                "title": "This is a title"
            }
        }
    ]
}
```

## Owner

The collection always has an owner. On creation, it is set automatically by the server to the parent collection's owner.

## System collections

| Collection | Owner | Description |
|----------------------|------------------|-------------------|
| **Root collection**  | root             | used as the root collection in the hierarchy |
| **User collections** | an "easydb" user | directly under the root collection, there is a collection for each "easydb" user |

All collections created by users are directly or indirectly under their user collection. When a user is deleted, the user collection is deleted, along with
its subtree.

## Create object properties

A user can create an object directly into a collection if they have the right `create_in_collection`.
The properties under `collection.create_object` define what kind of objects can be created and how the should be populated:

|  |  |  |
|--|--|--|
| `objecttype` | objecttype name (string, nullable)     | object MUST have this objecttype |
| `mask_id`    | mask ID (integer, nullable)            | object MUST be rendered using this mask, or the "standard" mask, if null |
| `pool_id`    | pool ID (integer, nullable)            | object MUST be linked to this pool, if the objecttype has a pool link |
| `eas_field`  | field name (string, nullable)          | if set, this field is the preferred field for assets |
| `tags`       | tag IDs (array of integers, nullable)  | if set, new objects SHOULD have these tags |
| `mapping`    | mapping to be used (integer, nullable) | mapping to be applied to the objects that are created in the collection |

If `objecttype` is **null**, the value is inherited from the parent collection and so on.
If no collection in the hierarchy has set an objecttype, no object can be created.

The mask and the EAS field are taken from the same collection where the objecttype is defined,
in order to avoid incorrect objecttype-mask-field combinations.

If `pool_id` is **null**, the value is inherited from the parent collection and so on.
If no collection in the hierarchy has set a pool ID and the object requires a pool, no object can be created.

The attributes `eas_field` and `tags` are only relevant to the frontend.

The result of inheriting the create object properties is provided in the field `_create_object_compiled`.

## Related operations

- [/collection](/technical/api/collection/collection.html): CRUD operations on collections
- [/search](/technical/api/search/search.html): Search type "collection"
- [/db](/technical/api/db/db.html): create objects in collections with POST/PUT and parameter `collection`
