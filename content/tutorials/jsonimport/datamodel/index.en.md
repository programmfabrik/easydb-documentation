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
	* Field `name` has a unique constraint and will be used as the reference

* **Personen** (`personen`)
	* Field `name` has a unique constraint and will be used as the reference

* **Schlagwörter** (`schlagwoerter`)
	* Field `inventarnummer` has a unique constraint and will be used as the reference

### Main Objects (searchable objects)

* **Objekte** (`objekte`)
	* has pool management
	* contains a reverse editable link to **Bilder** (*1 to N* relation between `objekte` and `bilder`)
	* Field `inventarnummer` has a unique constraint and will be used as the reference

* **Bilder** (`bilder`)
	* has pool management
	* has an asset field (`datei`)
	* contains a link to **Orte** (`aufnahmeort`)
	* contains links to **Personen** (`person`) in a nested table (`personen`)
	* contains links to **Schlagwörter** (`schlagwort`) in a nested table (`schlagwoerter`)
	* contains a reverse link to **Objekte** (*N to 1* relation between `bilder` and `objekte`)
	* Field `reference` was added as a hidden, unique field to be used as the reference

## Datamodel to download

{{< include_json "./datamodel.json" >}}
