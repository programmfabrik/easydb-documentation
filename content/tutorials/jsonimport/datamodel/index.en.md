---
title: "Sample Datamodel"
menu:
  main:
    name: "Sample Datamodel"
    identifier: "tutorials/jsonimport/datamodel"
    parent: "tutorials/jsonimport"
---

# Sample Datamodel

This is an overview over the datamodel that is used as a basis for the tutorial on the JSON Importer.

## Tables

### Linked Objects (not searchable objects)

* **Orte** (`orte`)
	* is hierarchical

* **Personen** (`personen`)

* **Schlagwörter** (`schlagwoerter`)

### Main Objects (searchable objects)

* **Objekte** (`objekte`)
	* has pool management
	* contains a reverse link to **Bilder**

* **Bilder** (`bilder`)
	* has pool management
	* has an asset field (`datei`)
	* contains a link to **Orte** (`aufnahmeort`)
	* contains links to **Personen** (`person`) in a nested table (`personen`)
	* contains links to **Schlagwörter** (`schlagwort`) in a nested table (`schlagwoerter`)
	* contains a reverse editable link to **Objekte**

## Datamodel to download

{{< include_json "./datamodel.json" >}}
