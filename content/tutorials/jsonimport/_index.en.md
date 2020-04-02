---
title: "Using the JSON Importer"
menu:
  main:
    name: "Json Importer"
    identifier: "tutorials/jsonimport"
    parent: "tutorials"
---

# Using the JSON Importer

This is a step by step tutorial on how to generate JSON Payloads, that can be imported into the easydb using the [JSON Importer](/en/tools/jsonimport/) in the frontend.

The importer reads a [manifest](#1-import-manifest) that defines the import and loads a list of payloads. Each payload is stored in a file. Each payload contains tge definition of the API endpoint, and a list if JSON objects that define basetypes or user objects. Mixed types in payloads are not allowed. All payloads are then posted to the API in the order of the payload list.

This tutorial uses an [example datamodel](/en/tutorials/jsonimport/datamodel) that covers most (but not necessarily all) aspects of importing payloads.

### Names used in this tutorial

* Basetypes: Basetype objects like tags, users, groups or pools
* Objects / User objects:
    * Objects defined in the datamodel (by the user), that contain the actual data
    * Here, objects means *user objects*, in contrast to *basetype objects*

### The general steps are:

1. Write the [Import Manifest](#1-import-manifest)
    * The import manifest is read by the importer and contains information about the payload URI and batch size, and most important, a list of all payload files
    * The filenames of all payloads that are generated have to be added to the payload list in the order in which they have to be imported

2. Create payloads for [basetypes](#2-payloads-for-basetypes)
    1. [Tags](#tags)
    2. [Groups](#groups)
    3. [Users](#users)
    4. [Pools](#pools)

3. Create payloads for [user objects](#3-payloads-for-user-objects) (actual easydb objects that contain data)
    1. [Simple objects](#simple-linked-objects) that are linked in main objects
    2. [Main objects](#main-objects) that link to simple objects

4. [Collections](#collections) and collection objects

5. If necessary, [import second versions](#importing-of-second-versions-of-objects) of objects to link to objects that could not be referenced in the first import round.

6. Load the manifest in the JSON Importer and [start the migration](#6-starting-the-migration)

### Important things to consider

* The order of importing is important!
    * Every object that is referenced by another object, must have already imported in a different payload, otherwise a database error can be caused
    * Every parent of a hierarchical basetype or object must have been imported before
        * Hierarchical objects must be imported level by level
        * This means the payloads have to be sorted to represent a breadth first search of the hierarchical tree
    * Linked objects that are referenced must have been imported before

* Masks should not be used for importing, since values might be ignored if they are not enabled in the mask
    * Always use `"_mask": "_all_fields"` so that all fields are imported without any limitations

*Tip*: The easiest way to see how a payload is formatted, is to capture the POST/PUT request that is sent by the frontend when a basetype or object is saved. In a browser, open the developer console and find the network tab to see the requests. Save an object and find the request that is performed. In the body of the post request contains an object JSON represantation, which has exactly the same structure as the objects in the payloads that are used here.

### Using lookups instead of IDs

Every object is identified by the `_id`. If you reference a basetype or object in another basetype or object, you need to know its ID, so that they can be linked. These IDs are assigned in the server to any new inserted object.

Since during migration, the IDs are not known yet, you need to use lookups. All basetypes have a unique field `reference`, that is used to find the object using a lookup, instead of referencing it by ID.

For user objects, you can use any unique (and not empty) text/string field for referencing the object, or you add an extra field in the datamodel, that can be used as a reference.

More detailled information on lookups can be found here: [Lookups for IDs](/en/technical/datamanagement/lookups/)

### Basic payload structure

Each payload file must contain a JSON object with the following structure:

```javascript
{
    "import_type": "db",
    "objecttype": "bilder", // only needed for import_type "db"
    "objects": []
}
```

All Payloads must define an `import_type` and an array of objects. Each object in the array defines a single basetype or user object. The import type specifies the API endpoint. For `db`, which is the endpoint for user objects, you also must specify the `objecttype`.

* Tags:
    * import type: `tags`
    * array name: `tags`

* Groups:
    * import type: `group`
    * array name: `groups`

* Users:
    * import type: `user`
    * array name: `users`

* Pools:
    * import type: `pool`
    * array name: `pools`

* Collections:
    * import type: `collection`
    * array name: `collections`

* User Objects:
    * import type: `db`
    * array name: `objects`
    * `objecttype` must be set

# Tutorial steps

The following steps show some basic import payloads.

## 1. Import Manifest

Create a file named `manifest.json` with the following content:

```javascript
{
    "source": "Example Migration",
    "batch_size": 100,
    "payload_base_uri": "",
    "payloads": []
}
```

This manifest is used to preload the migration data in the JSON Importer. All information in the manifest can also be changed in the frontend, so a manifest file is not needed, but very helpful.

* `source`: A name to identify the migration, can be freely chosen
* `batch_size`: Maximum number of objects from a payload that are posted in a single request. If the payloads contain more objects, the payloads are uploaded in parts. This value is necessary to control the request size. For complex objects which take a long time to be saved, it is possible that the request might time out. In this case, the batch size needs to be decreased. The internal limit of the server is 1000.
* `payload_base_uri`: If the payloads are not stored in the same folder as the manifest (or on another server), this is needed to build absolute paths from the payload file names. This value needs to be the relative path to the payload folder.
* `payloads`: List of the filenames of all payloads, in the order they are posted

## 2. Payloads for basetypes

Basetype payloads should always be imported first since they are referenced in most user objects. There is no strict order of the basetypes, but you have to consider that they can reference each other. Since circular references between basetypes are possible, importing of second versions of the basetypes might be needed (update migration).

Possible, but not exclusive, references between basetypes:

* Tags:
    * do not reference other basetypes
    * can be referenced by all other basetypes by tagfilter based rights management
    * tags, users, groups as part of the rightsmanagement

* Groups:
    * tags, users, groups as part of the rightsmanagement

* Users:
    * can reference groups (as being inside a group)
    * tags, users, groups as part of the rightsmanagement

* Pools:
    * hierachical, so pools reference other pools as a parent
    * tags, users, groups as part of the rightsmanagement

### Tags

Tags belong to tag groups. We add a tag "Public Access" to a new tag group "Tag Group 1". To reference this tag later, it will get the reference `"public"`.

The tag group and the tag(s) inside the group are stored in one JSON object. The object is added to the array of the payload:

```javascript
{
    "import_type": "tags",
    "tags": [
        {
            "taggroup": {
                "displayname": {
                    "en-US": "Tag Group 1"
                },
                "reference": "taggroup1",
                "type": "checkbox"
            },
            "_tags": [
                {
                    "tag": {
                        "displayname": {
                            "en-US": "Public Access"
                        },
                        "displaytype": "facet",
                        "enabled": true,
                        "frontend_prefs": {
                            "webfrontend": {
                                "color": "green",
                                "icon": "fa-eye"
                            }
                        },
                        "is_default": false,
                        "reference": "public",
                        "sticky": false,
                        "type": "individual"
                    }
                }
            ]
        }
    ]
}
```

Save this file as `basetype-tags.json` and add this filename to the payload list in the manifest.

For an overview of all fields that can be set in the tag and tag group object, see [Type Tag](/en/technical/types/tag/).

### Groups

We create a group, to which migrated users will be assigned. Any user who is in this group, will have the right to use the search function in the frontend, and manage collections.

The group will be named "Migrated Users", and it will get the reference `"migrated_users"`.

The group payload is:

```javascript
{
    "import_type": "group",
    "groups": [
        {
            "_basetype": "group",
            "group": {
                "_version": 1,
                "displayname": {
                    "en-US": "Migrated Users"
                },
                "reference": "migrated_users"
            },
            "_system_rights": {
                "system.search": {
                    "has_own_collections": true,
                    "show_fixed_searches": false
                }
            }
        }
    ]
}
```

Save this file as `basetype-groups.json` and add this filename to the payload list in the manifest.

For an overview of all fields that can be set in a group, see [Type Group](/en/technical/types/group/).

### Users

Add a test user and assign it to the group "Migrated Users".

We name the user "Max Mustermann", with the easydb login `"mustermann"` and the password `"password123"`. The reference of the user will be `"mustermann"`.

To add the new user to the group "Migrated Users", use the lookup `"lookup:_id"` for the group reference `migrated_users`.

The user payload is:

```javascript
{
    "import_type": "user",
    "users": [
        {
            "_basetype": "user",
            "user": {
                "type": "easydb",
                "login": "mustermann",
                "first_name": "Max",
                "last_name": "Mustermann",
                "reference": "mustermann",
                "_version": 1
            },
            "_password": "password123",
            "_groups": [
                {
                    "_basetype": "group",
                    "group": {
                        "lookup:_id": {
                            "reference": "migrated_users"
                        }
                    }
                }
            ]
        }
    ]
}
```

Save this file as `basetype-users.json` and add this filename to the payload list in the manifest.

For an overview of all fields that can be set in a user, see [Type User](/en/technical/types/user/).

### Pools

Any empty easydb always contains two system pools:

* "All pools" (reference: `"system:root"`)
    * "Default pool" (reference: `"system:standard"`) (child of `system:root`)

All pools have to be inserted into this hierarchy. Any new pool needs to have a parent.

For this tutorial, we create a new pool "Migrated Objects" and use "All pools" as the parent pool. To reference it later, set the reference to `"migrated_objects"`.

Instead of setting the parent pool using `"_id_parent": 1`, we have to use the lookup to let the server find the ID of "All pools". The lookup is done by replacing `"_id_parent": 1` with `"lookup:_id_parent": { "reference": "system:root" }`.

Add the pool JSON object to a pool payload. This payload is defined as:

```javascript
{
    "import_type": "pool",
    "pools": [
        {
            "_basetype": "pool",
            "pool": {
                "lookup:_id_parent": {
                    "reference": "system:root"
                },
                "_version": 1,
                "reference": "migrated_objects"
                "name": {
                    "en-US": "Migrated Objects"
                }
            }
        }
    ]
}
```

Save this file as `basetype-pools.json` and add this filename to the payload list in the manifest.

For an overview of all fields that can be set in the pool object, see [Type Pool](/en/technical/types/pool/).

## Payloads for user objects

Here we will create payloads for objects of different objecttypes, as well as linking these objects together using lookups.

### Simple linked objects

These objects are simple and are not linking other objects.

#### Orte (`orte`)

This objecttype is hierarchic. Each field contains a link (`_id_parent`) to reference its parent. Instead of `_id_parent`, we will use `lookup:_id_parent` instead. The unique field that is used for reference is `name`. Apart from this, there are no other fields in this objecttype.

All user objects consist of meta-fields, and an object with the actual data under a key which must be the same as the value of `_objecttype`. For importing, always use the `_mask` `_all_fields`.

We will create the following hierarchical structure of places:

* Europa
    * Deutschland
        * Berlin
        * Brandenburg

There are four levels, so we need to upload the objects in four different payloads in the following order: `["Europa"]`, `["Deutschland"]` and `["Berlin", "Brandenburg"]`. So we make sure that the parent has always been imported already before it is referenced.

**Payload #1**

The structure for the user object payloads is always the following:

```javascript
{
    "import_type": "db",
    "objecttype": "orte",
    "objects": []
}
```

The objects have the following structure:

```javascript
{
    "_objecttype": "orte",
    "_mask": "_all_fields",
    "orte": {
        "_id_parent": null,
        "_version": 1,
        "name": "Europa"
    }
}
```

On top level, the `_objecttype` and `_mask` must be defined. The value of `_objecttype` is `"orte"`, so we define the object itself under the key `orte`.

In `orte`, the `_id_parent` is `null` (or it can also be not set at all), since this object is on the top level of the hierarchy and has no parent.

Every imported object must have the `_version`, since it is a object that will be newly created.

The actual data "Europa" is saved under the key `name`. The key is the same as the internal field name in the datamodel.

The complete first payload looks like this:

```javascript
{
    "import_type": "db",
    "objecttype": "orte",
    "objects": [
        {
            "_objecttype": "orte",
            "_mask": "_all_fields",
            "orte": {
                "_id_parent": null,
                "_version": 1,
                "name": "Europa"
            }
        }
    ]
}
```

Save this payload as `userobject-orte-level-0.json` and add the filename to the manifest.

For hierarchical objects it is good practice to include the hierarchy level in the payload filenames to make sure they are in the correct order.

**Payload #2**

Define the object that contains the name "Deutschland", which is a child of "Europa".

The complete second payload looks like this:

```javascript
{
    "import_type": "db",
    "objecttype": "orte",
    "objects": [
        {
            "_objecttype": "orte",
            "_mask": "_all_fields",
            "orte": {
                "lookup:_id_parent": {
                    "name": "Europa"
                },
                "_version": 1,
                "name": "Deutschland"
            }
        }
    ]
}
```

The parent object is referenced by the field `name` in `lookup:_id_parent`. The only key in this object is the field name, and the value is the value of this field in the database. This feature only works, if you know that the field is set and unique for all objects of this objecttype.

Here we tell the server to use the ID of the object with `name = "Europa"` as the parent ID.

Save this payload as `userobject-orte-level-1.json` and add the filename to the manifest.

**Payload #3**

On this level, there are two objects, that both have the same parent "Deutschland". Both can be saved in the same payload, since they are not depending on each other in any way.

The complete second payload looks like this:

```javascript
{
    "import_type": "db",
    "objecttype": "orte",
    "objects": [
        {
            "_objecttype": "orte",
            "_mask": "_all_fields",
            "orte": {
                "lookup:_id_parent": {
                    "name": "Deutschland"
                },
                "_version": 1,
                "name": "Berlin"
            }
        },
        {
            "_objecttype": "orte",
            "_mask": "_all_fields",
            "orte": {
                "lookup:_id_parent": {
                    "name": "Deutschland"
                },
                "_version": 1,
                "name": "Brandenburg"
            }
        }
    ]
}
```

Save this payload as `userobject-orte-level-2.json` and add the filename to the manifest.

#### Personen (`personen`)

This objecttype is not hierarchical, so all objects can be saved in the same payload:

```javascript
{
    "import_type": "db",
    "objecttype": "personen",
    "objects": [
        {
            "_objecttype": "personen",
            "_mask": "_all_fields",
            "personen": {
                "_version": 1,
                "name": "Max Mustermann",
                "adresse": "Straße 123\n45678 Stadt"
            }
        },
        {
            "_objecttype": "personen",
            "_mask": "_all_fields",
            "personen": {
                "_version": 1,
                "name": "Peter Tester"
            }
        }
    ]
}
```

Note that you can use the newline character `\n` in multiline text fields (`adresse` in first object). Also you can leave any field empty, as long as it has no `NOT NULL` constraint or any other check constraints that do not allow empty fields (missing key `adresse` in second object).

Save this payload as `userobject-personen.json` and add the filename to the manifest.

#### Schlagwörter (`schlagwoerter`)

This objecttype is not hierarchical, so all objects can be saved in the same payload:

```javascript
{
    "import_type": "db",
    "objecttype": "schlagwoerter",
    "objects": [
        {
            "_objecttype": "schlagwoerter",
            "_mask": "_all_fields",
            "schlagwoerter": {
                "_version": 1,
                "name": "Insekt"
            }
        },
        {
            "_objecttype": "schlagwoerter",
            "_mask": "_all_fields",
            "schlagwoerter": {
                "_version": 1,
                "name": "Schmetterling"
            }
        }
    ]
}
```

Save this payload as `userobject-schlagwoerter.json` and add the filename to the manifest.

### Main objects

<!-- todo -->

#### Objekte (`objekte`)

<!-- todo -->

#### Bilder (`bilder`)

<!-- todo -->

## 4. Collections

<!-- todo -->

## 5. Importing of second versions of objects

<!-- todo -->

## 6. Starting the migration

After all payloads have been created and the filenames have been added to the payload list, this is the manifest we use to migrate all basetypes and objects:

```javascript
{
    "source": "Example Migration",
    "batch_size": 100,
    "payload_base_uri": "",
    "payloads": [
        "basetype-tags.json",
        "basetype-groups.json",
        "basetype-users.json",
        "basetype-pools.json",
        "userobject-orte-level-0.json",
        "userobject-orte-level-1.json",
        "userobject-orte-level-2.json",
        "userobject-personen.json",
        "userobject-schlagwoerter.json"
    ]
}
```

<!-- todo -->

