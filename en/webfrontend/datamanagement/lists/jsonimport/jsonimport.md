# JSON Importer

The JSON importer can be used to bulk import data in JSON format.

The importer can be found under "Lists > JSON Import".

The importer can be configured using a ".json" file with configuration.

## manifest.json

```js
{
  "source": "ADDH Helmsmuseum",
  "payload_base_uri": "http://myfile/...",
  "payloads": [
    "schlagworte/schlagworte_1_100.json",
    "bilder_all.json"
  ]
}
````

## playload.json

```js
{
  "objects:" [
    { easydb object json notation },
    { easydb object json notation }
  ]
}
```

## easydb object json notation

### EAS loader. prefix eas:

```js
{
  objects: [
    {
      "objecttype": "schlagworte",
      "schlagworte": {
        "_id": null,
        "name": "Keyword A",
        "old_system_reference": "keyword:37186"
      }
    },
    {
      "objecttype": "schlagworte",
      "schlagworte": {
        "_id": null
        "name": "Keyword B",
        "old_system_reference": "keyword:37187"
      }
    },
    {
      "_objecttype": "bilder",
      "bilder": {
        "_id": null,
        "_nested:bilder__schlagworte": [
          {
            "lk_schlagwort_id": "[lookup:old_system_reference]keyword:37186"
          },
          {
            "lk_schlagwort_id": "[lookup:old_system_reference]keyword:37187"
          }
        ],
        "image": {
          "_id": "[eas] http://easydb-server-old/henk..."
        }
      }
    }
  ]

}
```
