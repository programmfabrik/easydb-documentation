---
title: "123 - Collection"
menu:
  main:
    name: "Collection"
    identifier: "technical/types/collection"
    parent: "technical/types"
---
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
| `_owner`                       | Owner of this collection ([user (short)](/en/technical/types/user), r): see below                              | Number(\*) |
| `_acl`                         | ACL (array of [acl entries](/en/technical/types/acl_entry), rw, optional)                                            | *not present* |
| `_private_acl`                 | Marks the ACL as private (see [rights management](/en/technical/rightsmanagement)) (bool, rw, optional): defaults to **false** | *not present* |
| `_has_children`                | Whether this collection has nested collections (boolean, r)                                                  | Boolean       |
| `_has_acl`                     | Whether this collection has a non-empty ACL (boolean, r)                                                     | Boolean       |
| `_level`                       | Level of this collection in the hierarchy (integer, r)                                                       | Number(\*)    |
| `_path`                        | Path to this collection (array of collections, r)                                                            | (\*)          |
| `_count`                       | Number of objects in the collection (integer, r)                                                             | Number        |
| `_create_object_compiled`      | Effective create object properties, as inherited from ancestors (r): see below                               |               |
| `_generated_rights`            | Rights that the session user has for the collection ([rights specification](/en/technical/types/right)): bag_read, bag_write, bag_delete, bag_acl, bag_create, link, unlink, create_in_collection |
| `_hotfolder_upload_urls`       | Hotfolder URLs (object, r): only shown if the hotfolder is configured and the collection allows uploads (\*\*) |               |
| `_set_spec`                    | OAI/PMH name for this set |
| `_has_pin`                     | Indicates whether this collection is protected by a `pin_code` (see below) (boolean, r): defaults to **false** |
| `_pin_ok`                      | If this collection is protected by a `pin_code`, and the [user has a correct pin for this collection stored](/en/technical/types/user/#collection_pins), this indicates that the pin was correct (see below) (boolean, optional, r): defaults to **false** |
| `collection`                   | Collection attributes:                                                                                       |               |
| &#8614; `_id`                  | Collection ID (integer, unique, r\*)                                                                         | Number        |
| &#8614; `_id_parent`           | Parent collection ID (integer, rw)                                                                           | Number        |
| &#8614; `lookup:_id_parent`    | [Lookup for ID of parent collection](/en/technical/datamanagement/lookups/#collections-and-collection-objects) |             |
| &#8614; `_version`             | Collection version (integer, rw)                                                                             | Number        |
| &#8614; `is_system_collection` | Whether this is a system collection (boolean, r)                                                             | Boolean       |
| &#8614; `displayname`          | Collection name ([l10n](/en/technical/types/l10n), unique for collections with the same parent, rw)                  | L10n (all)    |
| &#8614; `description`          | Collection description ([l10n](/en/technical/types/l10n), optional, rw)                                              | L10n (all)    |
| &#8614; `type`                 | Collection type (string, optional, rw)                                                                       | Text          |
| &#8614; `children_allowed`     | Whether this collection is allowed to have nested collections (boolean, optional, rw): defaults to **false** |               |
| &#8614; `objects_allowed`      | Whether this collection is allowed to contain objects (boolean, optional, rw): defaults to **false**         |               |
| &#8614; `webfrontend_props`    | JSON map for arbritary use by clients. Defaults to **null**. (\*\*\*)                                        |               |
| &#8614; `create_object`        | Configuration for objects that are directly created in the collection (rw, optional, nullable): see below    |               |
| &#8614; `uuid`                 | Collection UUID (text, unique, r)                                                                            |               |
| &#8614; `reference`            | Collection reference (string, unique, optional, rw): can be used for lookups for `_id:parent`                  |
| &#8614; `shortname`            | Collection short name (string, unique, optional,rw): can be used for lookups for `_id:parent` |
| &#8614; `pin_code`             | Value for the PIN to protect this collection (string, optional, rw), see [Collection PIN-Code](/de/webfrontend/datamanagement/search/quickaccess/collection/#pin-code) |


The following fields are only present when searching: `_has_acl`, `_level`, `_path`.

### \* Remarks:

- `_id` has to be set for POST operations
- the hierarchy begins at level 1. The array in `_path` only contains the fields `_basetype`, `_has_acl`, `_count` and `collection`
- `_path.collection._id` is searchable as a Number
- the fields `_level` and `_path` are only provided by `/api/search`
- `_groups.group._id` is searchable as Number
- `_owner.user._id` is searchable as Number

Notice that all collections must have a valid `_id_parent` (except for the root collection, which is a system collection).

### \*\* `_hotfolder_upload_urls`

This array contains all available upload urls for the hotfolder for this collection. The URLs are generated from the [configured Hotfolder URLs](/en/sysadmin/configuration/easydb-server.yml/plugins/hotfolder/#server-yaml-variables-to-configure-the-hotfolder).

The `type` is the same as it is specified in the configuration. The `url` is generated using the following pattern:

    <configured url> <configured separator> <server instance> <configured separator> <collection uuid>

Based on the [example configuration](/en/sysadmin/configuration/easydb-server.yml/plugins/hotfolder/#example-configuration), with the server instance `d3cea042-64f0-4e8b-b5a5-c3f30390648c` and the collection uuid `860f45c0-3586-4249-b490-b9ee68eac6cf`, the generated hotfolder URLs will be the following:

```json
"_hotfolder_upload_urls": [
    {
        "type": "windows_webdav",
        "url": "\\easydb.example.com@SSL\upload\collection\d3cea042-64f0-4e8b-b5a5-c3f30390648c\860f45c0-3586-4249-b490-b9ee68eac6cf"
    },
    {
        "type": "webdav_http",
        "url": "https://easydb.example.com/upload/collection/d3cea042-64f0-4e8b-b5a5-c3f30390648c/860f45c0-3586-4249-b490-b9ee68eac6cf"
    }
]
```

### \*\*\* `webfrontend_props`

It's an optional object with extra properties that the frontend can set and retrieve. This JSON map needs to be updated carefully by clients.

It is also used to store the definition of a presentation that is based on the collection (see [below](#presentation)).

> Clients should only update the parts they care about and write back other parts which might have been written by other clients.

#### Presentation

| Name                              | Type                 | Description                                                                               |
|-----------------------------------|----------------------|-------------------------------------------------------------------------------------------|
| `settings`                        | PlainObject          |                                                                                           |
| &#8614; `show_info`               | String               |  Possible values: **standard-info** will render the object with the standard render, and **no-info** will render just the object image if there is one available, without extra information.                                                    |
| `slide_idx`                       | Number               |  Frontend position for the current slide which is shown on load                           |
| `slides`                          | Array of Slide       |  Explained below                                                                          |

##### Slide

Slides has four different types: **start**, **one**, **duo** and **bullets**

##### Slide **start** and **bullets**

Both includes a title and a description, the difference is that the description for type **bullets** will have a bullet for each newline. Also there will be just one **start** slide which will be the first slide.

| Name                              | Type                 | Description                                                                                  |
|-----------------------------------|----------------------|----------------------------------------------------------------------------------------------|
| &#8614; `type`                    | String               |  Indicates the slide type. In this case is "start" or "bullets"                              |
| &#8614; `data`                    | PlainObject          |                                                                                              |
| &#8614; &#8614; `title`           | String               |  This is the title of the slide, it will be shown in the upper center above the description. |
| &#8614; &#8614; `info`            | String               |  The description is multi line and it will be shown in the center of the slide.              |

##### Slide **one**

It will show just one object and will be rendered depending **show_info** property value.

| Name                              | Type                 | Description                                                                               |
|-----------------------------------|----------------------|-------------------------------------------------------------------------------------------|
| &#8614; `type`                    | String               |  Indicates the slide type. In this case is "one"                                          |
| &#8614; `center`                  | PlainObject          |  It's an object that includes the ID for the object shown                                 |
| &#8614; &#8614; `global_object_id`| String               |  ID of the referenced and shown object. A [lookup](/en/technical/datamanagement/lookups/#collections-and-collection-objects) for the `global_object_id` can also be used. |

##### Slide **duo**

It's similar to type **one**, with the difference that it will show two objecs vertically rendered

| Name                              | Type                 | Description                                                                               |
|-----------------------------------|----------------------|-------------------------------------------------------------------------------------------|
| &#8614; `type`                    | String               |  Indicates the slide type. In this case is "duo"                                          |
| &#8614; `left`                    | PlainObject          |  It's an object that includes the ID for the object shown in the left side                |
| &#8614; &#8614; `global_object_id`| String               |  ID of the referenced and shown object. A [lookup](/en/technical/datamanagement/lookups/#collections-and-collection-objects) for the `global_object_id` can also be used. |
| &#8614; `right`                   | PlainObject          |  It's an object that includes the ID for the object shown in the right side               |
| &#8614; &#8614; `global_object_id`| String               |  ID of the referenced and shown object. A [lookup](/en/technical/datamanagement/lookups/#collections-and-collection-objects) for the `global_object_id` can also be used. |


##### Example

```javascript
"presentation": {
    "settings": {
        "show_info": "standard-info"
    },
    "slide_idx": 0,
    "slides": [
        {
            "type": "start",
            "data": {
                "title": "Presentation title",
                "info": "This is a long description."
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
|---|---|---|
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

- [/collection](/en/technical/api/collection): CRUD operations on collections
- [/search](/en/technical/api/search): Search type "collection"
- [/db](/en/technical/api/db): create objects in collections with POST/PUT and parameter `collection`
