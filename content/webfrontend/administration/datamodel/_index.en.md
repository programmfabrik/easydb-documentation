---
title: "163 - Data Model"
menu:
  main:
    name: "Data Model"
    identifier: "webfrontend/administration/datamodel"
    parent: "webfrontend/administration"
---
# Data model

In the data model, the current data model <code class="tab">Current</code> can be viewed, and with proper access rights the development version <code class="tab">Development</code> can be viewed as well. <code class="button">Activate Changes</code> to accept changes made in the development version. This will overwrite the current version.

> NOTE: Be aware that this process causes a lot of activity on the server side, A complete re-indexing of all records. Until full indexing, users may find records in the old format. In some cases, it may also happen that records affected by changes are not displayed to users until the re-indexing is complete.

## Definition of fields

Object types and masks are defined in the data model. Object types describe the structure of the data in the database. Masks describe the input and output views of the object types and therefore the data records. If, for example, 20 fields are defined for an object type, different field combinations can be viewable from masks. For instance, user 1 could have the right to mask 1, perhaps 5 of these fields. User 2 could be provided with mask 2, another 5 fields and with mask 3 they could view the other 15 fields.

* [Object Types](objecttype)

* [Masks](mask)

> NOTE: It is possible to hide individual fields for certain users or groups and to refine the view of an object type and its corresponding masks using the [field rights](../../rightsmanagement/objecttypes) for the object type.

## Export/Import data model {#datamodelfile}

easydb offers the possibility to download the data model of any easydb instance and to save or reuse it as a JSON-file or a CSV-file. A JSON file contains the configuration of all object types with associated masks and settings. A CSV file contains the tables for all object types without masks and without settings.

It is also possible to import an externally saved data model (JSON & CSV) into easydb.

The data model can be downloaded and uploaded via the data model in the main menu. It is available below the list of object types in the development environment via the cog-menu. 

![](datamodel_load_en.jpg)

NOTE: Uploading data models is primarily intended for transferring existing data models to new instances. Note that uploading and activating a new data model overwrites an existing data model and does not supplement it.


### Use cases 

1. The download and upload of data models serves as backup. This is especially recommended in JSON format, since masks and settings for the object types are also saved.

2. The use of stored data models facilitates the rapid creation of new instances if they are supposed to base on existing data models.

3. Data models saved as CSV can be displayed in a table. CSV files can be opend with Spreadsheet Programs such as Excel. The tables for all object types are displayed in one spreadsheet.

4. For example, a CSV can be used to add translations for the data model outside the database.

5. With the backup of CSV files at regular intervals, the development of a data model can be documented.

## Reset data model

The menu within development environment provides the option to reset the data model in development mode. Changes within the data model in development mode are thus reset to the status of the current data model.

## Objectstore {#objectstore}

The Objectstore (data model server) works as a node, which allows to work on a data model from different instances. The current data model is stored in a virtual environment and synchronized with other instances before further changes can be made.

![](objectstore_en.jpg)

If the Objectstore is configured, a <i class="fa fa-lock"> </i>-button appears next to the <i class="fa fa-cog"> </i>-menu. 

* If the icon is activated it appears <i class="fa fa-unlock"> </i> (open) and it is possible to work on the data model. It is not possible to work on the data model from other instances during this time. The icon remains locked there. 
* Once the changes to the data model are complete and activated, the <i class="fa fa-unlock"> </i>-icon must be clicked again to complete the process. The current data model is then transferd to the Objectstore. 
* If another editor from another instance starts editing the data model, a message appears that the data model must be updated first. Once synchronization with the data model from the Objectstore is complete, the data model can be edited.

Ist der Objectstore aktiv, kann über das <i class="fa fa-cog"> </i>-Menü mit _Datenmodell auf dem Server überprüfen_ ein Check aller Datenmodellversionen durchgeführt werden. Es wird dabei verglichen, ob die Version, die im Objectstore ist, diesselbe ist, wie sie lokal installiert ist. Sollte es ein Problem geben (z.B. fehlende Version oder Mismatched), dann bietet das Frontend an die lokalen Version auf den Objectstore zu speichern (und damit alle Versionen im Objectstore zu überschreiben).

If the Objectstore is active, a check of all data model versions can be performed via the <i class="fa fa-cog"> </i> menu with _Check Data Model on the Server_. It is compared whether the version that is in the Objectstore is the same as it is installed locally. If there is a problem (e.g. missing version or mismatched), the frontend offers to store the local version on the Objectstore (and thus overwrite all versions in the Objectstore).

> HINWEIS: [Here](/en/sysadmin/konfiguration/fylr.yml/) you finde an instructions for the installation.


## Graphic of individual data model

The options menu allows you to visualize the structure of the data model. The current data model can be downloaded as an svg graphic.

![Graphic of the data model](svg_datamodel_en.jpg)

