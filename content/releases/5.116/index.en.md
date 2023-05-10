---
menu:
  main:
    name: "5.116 (May 2023)"
    identifier: "5.116"
    parent: "releases"
    weight: -616
---


> This version **does not require** a new index build


# Version 5.115.0

*Released on 10.05.2023*


## Webfrontend

## Improved

* **Search**: Main search is executed when options in expert search or autocomplete entries are enabled.
* **General**: Improved names for generated CSV and JSON files, e.g. when exporting the data model.
* **Basic configuration**: Improved display of password fields
* **Main Menu**: Improved update when changes are made to object types contained in the main menu.
* **Collections**: Order of menu items optimized
* **Folders**: Creation of new folders accelerated, they are created directly on top level without prompting
* **Read-Only mode**: Indicator for new read-only mode

## Fixed

* **Quick Access**: Fixed error when opening the menu
* **detail-linked-plugin**: fixed missing display when plugin is sole element in Mask Splitter
* **collection settings**: error when activating uploads prevented saving of settings made
* **Object Preview**: Fixed display when objects cannot contain assets.
* **Main Menu**: URL corrected when clicking on object types contained in main menu.
* **CSV Importer**: Fixed error when used on object types with display-field-value-mask-splitter.
* **Editor**: Validation of date range fields improved

# Server

## New

* **Read-Only mode**: enabled in base configuration, prevents objects and most base types from being written.

## Improved

* `SESSION_INVALID` events are not saved anymore

## Fixed

* Loading users with archived owners no longer causes errors
* Intranet check no longer aborts if individual network masks are invalid


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.116.0         sha256:9b292c2407f3540c65bd7cf2662a4f3041050f5ba0cc185ce06b8b8ed0fe6505
docker.easydb.de/pf/eas:5.116.0            sha256:cf200ee1e48fa1748490287f74f42df76872f9ecaced3e4ee2902dcf6b3fe6c2
docker.easydb.de/pf/elasticsearch:5.116.0  sha256:a0035a635c38d61f0241cd9de6bbe2d4cbf0f4d072acf19041a77b8b1e67874a
docker.easydb.de/pf/fylr:5.116.0           sha256:a79ecc20278fb3ebd217e9231c409e9be4592b456c342eb21059f55521516336
docker.easydb.de/pf/postgresql-14:5.116.0  sha256:c5a6b41852aeec745bc2c945f282bd092988390a44d277e53e16c6a6d4bc2668
docker.easydb.de/pf/server-base:5.116.0    sha256:1a160b4c8fbe4ad26fb48a328d9589e9f4bbd139629946dc1463eb78a678dbd5
docker.easydb.de/pf/webfrontend:5.116.0    sha256:aefd5bae6bbfc7bc409c2682cefa9eeead354eeeb9133b81ed78907711d7cf69
```
