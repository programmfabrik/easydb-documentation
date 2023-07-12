---
menu:
  main:
    name: "5.119 (July 2023)"
    identifier: "5.119"
    parent: "releases"
    weight: -619
---


> This version **does not require** a new index build


# Version 5.119.0

*Released on 2023-07-12*

# Webfrontend

## Improved

* **Search**: Search is automatically executed when query is processed
* **easydb-editor-tagfilter-defaults plugin**: Date entries are supported
* **General**: Indicator when areas in quick access are empty.

## Fixed

* **CSV Importer**: Fixed issue when selecting a reverse link field as destination.
* **General**: Date formats for some languages added (fi, sv, fr).
* **Print**: Fixed CSS issue where all languages were displayed in multiple input fields.
* **Downloads**: Fixed display of messages before asset download
* **Linked-Object-Filter**: fixed bug
* **Tooltips**: Fixed issue with tooltips staying open.
* **Search**: Behavior of the resource button for new instances corrected

# Server

## Improved

* Server-side nested sorting: support for asset columns (sorting by original file name).
* New data language Nepali (`ne`).

## Fixed

* EAS Supervisor no longer tries to handle failed originals.
* Cropping of raw images fixed, target format becomes JPEG instead of the unsupported source format.

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.119.0         sha256:ba585893b5bc343f2c03e08ffe7e2074c564abc18bc6ee7460910b5050766e4f
docker.easydb.de/pf/eas:5.119.0            sha256:205eadef7b37677ad70e8069a9f4a381bd507b1bc8e06f185bfe463a316a49d5
docker.easydb.de/pf/elasticsearch:5.119.0  sha256:bb4053497f821b524aae9624f7a019059c8a242d8c761b64488994cdfa2fec7c
docker.easydb.de/pf/fylr:5.119.0           sha256:fd595fcc78aa7f078a11577dae20de87939dd9151b5633e967b4482ef56512f6
docker.easydb.de/pf/postgresql-14:5.119.0  sha256:a9f76cf58c9ab60d3b940892dd12133095ca7885c119d5d186defc538118d7b2
docker.easydb.de/pf/server-base:5.119.0    sha256:fafc9352252c00a37dba6e671c6fccfc2700b7ea6958ff3e99d57e568520bd11
docker.easydb.de/pf/webfrontend:5.119.0    sha256:f5ab8176317b84064866a684169f11ad56e90e3d0d6d1d853c7fcf141c69403d
```
