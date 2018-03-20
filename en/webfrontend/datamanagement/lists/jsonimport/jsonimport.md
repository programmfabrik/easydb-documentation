# JSON Importer

The JSON importer can be used to bulk import data in JSON format.

The importer can be found under "Lists > JSON Import".

The importer can be configured using a ".json" file with configuration.

## Frontend form

Fields:
- URL manifest.json: (Optional) This is a URL to get the manifest.json by clicking 'Load' button next to the input.
- Source: (Optional) Name of the source instance.
- Payloads base URI: (Optional) Base URI for all the payloads in the list. It will be prepended to each payload.
- EAS Type: Depending on the option, the file will be processed in a different way.
    - Direct: The file will be downloaded and then uploaded by using /eas/put.
    - URL (remote PUT): The file is not downloaded, and /eas/rput is invoked directly using the file url. Therefore the server will download and upload the file. (this option should be the fastest)
    - FYLR. Proxy: This option is almost the same as 'Direct'. The difference is that the URL will use the FYLR. Proxy configured in the base config. 
- EAS replace url: (Optional) The location for each file URL will be replaced by the value configured here.
- Payload list
    - Enabled: Checkbox to enable or skip the payload
    - Status: Current status of the payload. Pending/Success/Error
    - URL: The url of the payload
    - Actions
        - Open the payload in a new tab.
        
Buttons:
- Start: It starts the import of all the enabled payloads.
- Rollback: - Rollback: It makes a rollback of the imported data. The rollback data will be lost if the JSON Importer modal is closed.
- Logs


## Server Lookups for IDs

When objects and basetypes are imported, they are not saved in the database yet and have no ID yet. To link to objects and basetypes in the migration payloads, instead of using IDs lookups for these IDs can be defined. In the server, these lookup keywords are used to replace the lookup object with the correct ID of the object.

A lookup is a JSON object that is used instead of the ID (integer). It defines a column in the database that contains the unique value that is referenced. The reference value must exist in the database during the time of the import, must be unique, and known when the payloads are created.

The column can be a standard reference column (`"reference"` for all basetypes Tag, Tag Group, User, Group, Pool, Collection and Message), any unique text field in a user object, or an extra reference field. The name of the reference column must be known during the creation of the payloads.

### General structure

The structure of all lookup object is

```json
"lookup:<type of id>": {
  "<reference column>": "<reference value>"
}
```

The use of more keys in the lookup object would cause an API Error, since the server can not determine which of the keys would be the name of the reference column in the database. The only exception is a lookup for an object with an arbitrary objecttype (used for example when objects are linked to collections).

In this case, the keyword `"_objecttype"`, which defines the table, is also allowed in the lookup object:

```json
"lookup:_id": {
  "<reference column>": "<reference value>",
  "_objecttype": "<objecttype = reference table name>"
}
```

The server performs a lookup in the database by returning the ID of the object or basetype that has the value `"reference_to_linked_object_5804d0ce"` in the column `"reference"`.

If there is no result for this query, or more then one, the lookup failed and an API Error is thrown. In this case, the complete batch failed and the lookup must be fixed.

#### Example:

To create a link to an object in the payload

```json
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

```json
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

- Linked objects
- Pools
  - Add an object to a pool
- Tags
  - Add a tag to an object
- Tag Groups
  - Add a tag to a tag group
- Groups
  - Add a user to a group

#### `lookup:_id_parent`

Perform a lookup for the parent ID of an object or basetype in the current table. This is used to add the parent-child-relation to a hierarchical basetype or user object.

Lookups for a parent ID can be performed for:

- Hierarchical objects
- Pools
  - Set a pool as the child of another pool
- Collections
  - Set a collection as the child of another collection

#### `lookup:_global_object_id`

Perform a lookup for the global object ID of a user object.

Lookups for a parent ID can be performed for:

- Objects in a collection
  - This also requires the key `"_objecttype"`

## manifest.json

This file is useful to fill the JSON Importer form, therefore all values are optional.

```json
{
  "source": "",
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

```json
{
  import_type: "group",
  groups: [ <group object> ]
}
```

#### Default References for System Groups

All System Basetypes have predefined, read only references. The references have the form `system:<internal name>`.

For example the group "All users" (internal name `:all`) has the reference `system::all`.

### Users

```json
{
  import_type: "user",
  users: [ <user object> ]
}
```

#### Default References for System Users

The references have the form `system:<login name>`.

For example the root user (login name `root`) has the reference `system:root`.

### Pools

```json
{
  import_type: "pool",
  pools: [ <pool object> ]
}
```

#### Default References for System Pools

The references have the form `system:<internal_unique_id>`.

For example the standard pool (internal_unique_id `standard`) has the reference `system:standard`.

### Tags

Tags and Taggroups are sent together in one package to the server. All existing Taggroups and Tags are replaced.

```json
{
  import_type: "tags",
  tags: [ <tags object> ]
}
```

### Collections

```json
{
  import_type: "collection"
  collections: [
    {
        "_basetype": "collection",
        "collection": {
            "displayname": {
                "de-DE": "Neue Mappe"
            }
            "description": {
                "de-DE": "Eine freigegebene Mappe für Ticket: #44450"
            }
        }
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


### References for

... coming ...
