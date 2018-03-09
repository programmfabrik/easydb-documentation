# JSON Importer

The JSON importer can be used to bulk import data in JSON format.

The importer can be found under "Lists > JSON Import".

The importer can be configured using a ".json" file with configuration.

## manifest.json

```js
{
  "source": "ADDH Helmsmuseum",
  "batch_size": 100, // client batch size
  "payloads": [
    "schlagworte.json",
    "bilder.json"
  ]
}
````

## groups.json

```js
{
  import_type: "group",
  groups: [
    {...}
  ]
}
```


## users.json

```js
{
  import_type: "user",
  users: [
    {...}
  ]
}
```

## pools.json

```js
{
  import_type: "pool",
  pools: [
    { ... }
  ]
}
```


## tags.json

Tags & Taggroups are sent togther in one package to the server. All existing Taggroups and Tags are replaced.

```js
{
  import_type: "tags",
  tags: [
     ...
  ]
}
```




## collections.json

```js
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

... coming ...

## schlagworte.json

```js
{
  import_type: "db"
  objecttype: "schlagworte"

  objects: [
    {
      "_objecttype": "schlagworte",
      "_mask": "_all_fields",
      "schlagworte": {
        "_id": null,
        "name": "Keyword A",
        "old_system_reference": "keyword:37186"
      }
    },
    {
      "_objecttype": "schlagworte",
      "_mask": "_all_fields",
      "schlagworte": {
        "_id": null
        "name": "Keyword B",
        "old_system_reference": "keyword:37187"
      }
    }
  ]
}
```

## bilder.json

```js
objects: [
    {
      "_objecttype": "bilder",
      "_mask": "_all_fields"
      "bilder": {
        "_id": null,
        "_nested:bilder__schlagworte": [
          {
            "lookup:lk_schlagwort_id": "old_system_reference:keyword:37186"
          },
          {
            "lookup:lk_schlagwort_id": "old_system_reference:keyword:37187"
          }
        ],
        "image": [
          {
            "preferred": true,
            "eas:url": "http://easydb-server-old/henk...",
            "eas:preview:url": "...",
            "eas:filename"
          }
        ]
      }
    }
  ]
}
```
