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

## schlagworte.json

```js
{
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
        "image": {
          "eas:url": "http://easydb-server-old/henk..."
        }
      }
    }
  ]
}
```
