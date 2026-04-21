---
menu:
  main:
    name: "5.153 (Late March 2026)"
    identifier: "5.153"
    parent: "releases"
    weight: -653
---

> This version **does not require** a new index build


# Version 5.153.1

*Released on 2026-04-21*

# Server

## Fixed

* `/api/db?all_versions`: hide nested object which don't exist at the end of an object version's lifetime.
* Server no longer creates core dumps on exit. May be reenabled with `debug.max_core_size`.

# Webfrontend

## Fixed

* Group editor: fix display/functionality of boolean fields in easydb 5 theme.

# Version 5.153.0

*Released on 2026-03-25*


# Webfrontend

## Improved

- **Full Screen Detail**: When in full screen detail mode and using the option to view a linked object in the detail, the fullscreen browser will now update to display the linked object.
- **File Name Search**: It is now possible to use multiple search values separated by commas when searching using the file name field.

## Fixed

- **Search List**: Fixed a bug where hierarchies were not displayed correctly when pools were selected in the Pool selector of the search.
- **Linked Object**: Improved validation to check whether a linked object is corrupted or does not exist in the database.
- **CSV Importer**: Fixed the import of localized strings within nested structures.
- **Mask Remember Feature**: Fixed bugs in the initialization of the system that controls masks when opening editors or details.
- **Metadata Mapping Editor**: Fixed drag and drop of fields in the metadata mapping editor.
- **Tooltips**: Fixed the behavior of tooltips in vertical menus; tooltips are now displayed along the horizontal axis.
- **Export Manager**: Fixed a bug when attempting to infer object sorting from a selection that does not contain sort data.
- **Metadata Mapping**: Fixed a bug related to the use of custom data types and metadata mapping.
- **Linked Object**: Fixed a bug where newly created linked objects were shown as "Not Found". Also fixed a bug where the standard sent by the server was ignored and the full linked object was attempted to be loaded, potentially showing a "No rights" alert in cases where the user had limited rights.


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.153.0            sha256:6fa0ce2b13ae30e00a1a24894b14e91d0d53d8cb90f3f9287ec50f188125b51a
docker.easydb.de/pf/elasticsearch:5.153.0  sha256:be0527b75cdaae3b2ae4a1c341fa9437a52598ae12729116b6d23766962d8b81
docker.easydb.de/pf/fylr:5.153.0           sha256:23e36d632cb5101f43766d830f9e0a4e7047ae9112f5ec90c1411b055c838485
docker.easydb.de/pf/postgresql-14:5.153.0  sha256:8d7710d5687f2cb81b0f040f9a66138522c8593b76e4a230ab5e18975fa20ccd
docker.easydb.de/pf/server-base:5.153.1    sha256:9cb3c7fa1374bd609c4eab244ce47cceb747edf5fc134c255ac0044ec8321481
docker.easydb.de/pf/webfrontend:5.153.1    sha256:d3a7e5b3eb56f14764af7fd1a55bdcb9458c20de99bc50bea1fc13a0e82216c6
```
