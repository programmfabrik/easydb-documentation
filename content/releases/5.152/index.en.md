---
menu:
  main:
    name: "5.152 (Late January 2026)"
    identifier: "5.152"
    parent: "releases"
    weight: -652
---

> This version **does not require** a new index build


# Version 5.152.0

*Released on 2026-01-28*


# Webfrontend


## Improved

* **Mask Editor**:
  * The behavior of the mask editor has been improved when unknown mask splitters are present in a mask
  * i.e. mask splitters implemented in plugins that are not loaded
  * They can now be deleted correctly and no longer cause the mask to become corrupted

* **Variant Editor**:
  * A new checkbox has been added when creating a new variant from the variant editor
  * It allows to automatically set the new variant as the default variant

* **Search Input**:
  * Improvements have been made to how different types of searches are processed in the search input

* **Export Manager**:
  * New descriptive texts have been added to the export manager


## Fixed

* **Sidebar**:
  * An issue has been fixed where, in certain situations, the detail sidebar opened empty when reopening a previously loaded object

* **Field Visibility**:
  * A bug has been fixed where field visibility settings were ignored in the detail view

* **Linked Objects**:
  * A bug has been fixed where using linked objects in the expert search incorrectly displayed a missing permissions message

* **CSV Importer**:
  * An issue with importing empty values in *Date Range* Columns has been fixed
  * These imported values are now evaluated correctly and clear the current value when performing an object update

* **Datamodel**:
  * *Date Range* Column: The display of *Date Range* fields with text representation in the table view has been fixed
  * In addition, the automatic recognition of ranges from text has been improved to allow months starting with lowercase letters


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.152.0            sha256:a295b058504b8880e22ffb958152320f549db2b17a6f3b372585f8aa070cde35
docker.easydb.de/pf/elasticsearch:5.152.0  sha256:e1e1ba2935e4f9777c267fcf1bd73c1d37b6a526e3550d62100310fa4f2cecf5
docker.easydb.de/pf/fylr:5.152.0           sha256:9dede0c6895cdb44f72c4b40bf714cf583db6a60327351b2470523ad225afda5
docker.easydb.de/pf/postgresql-14:5.152.0  sha256:3f32e39a8ac803fbf31e31ab1f994f5b38ac9add7bdd1163426f6bf314d44ad3
docker.easydb.de/pf/server-base:5.152.0    sha256:7db7e7c5510d54152e49a6a88a1f9ebee559522537b56a7b7bfd889af542582c
docker.easydb.de/pf/webfrontend:5.152.0    sha256:b570cf993db83da04d8b05f4ce70020ab1444780fd953cffbc30fb709c63acea
```
