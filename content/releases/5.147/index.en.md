---
menu:
  main:
    name: "5.147 (End of August 2025)"
    identifier: "5.147"
    parent: "releases"
    weight: -647
---

> This version **does not require** a new index build

# Version 5.147.2

*Released on 2025-09-03*

# Webfrontend

## Fixed

* **Detail**:
  * fixed an error in the mask preview if there was no standard "A" in the object
  * this had an error message which made it impossible to upload files
* **Editor**:
  * fixed tags which were not shown in linked objects
  * tags were displayed as text

# Version 5.147.1

*Released on 2025-08-28*

# Webfrontend

## Fixed

* **Detail**: fix an error preventing opening detail in some cases

# Version 5.147.0

*Released on 2025-08-27*

# Server

## Fixed

* **Search**: rolled back incompatible change in string phrase search
* **Docker containers**: replace high UIDs/GIDs

# Webfrontend

## Fixed

- **Nested Tables and Reverse Nested Tables**: Fixed a bug where, if a nested table was configured as readonly in the mask configuration, the data was not correctly sent when saving the object.  
- **Print Manager**: Improved the print manager to ensure that images are loaded before calling the browser's print context. This helps in situations where large amounts of records were being printed.  
- **Nested Rows**: Improved the delete button in nested tables; now, if a nested table is configured to always show a first empty row, the delete button will allow clearing that row.  
- **CSS**: Adjustments and fixes applied to various parts of easydb5's CSS.  

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.147.0            sha256:60d835e6afa49690ae5b8f91c056070751044b3a4678fdc5a8fb932b2bc45501
docker.easydb.de/pf/elasticsearch:5.147.0  sha256:2afe7cb91c3ba1d36d80e2929e84904cbf694fab5e9fba60004fa44eeb21125c
docker.easydb.de/pf/fylr:5.147.0           sha256:289c4c1c6418636ed6b7735e31296fb9967ee45e0ac67264ac78a76972d8e782
docker.easydb.de/pf/postgresql-14:5.147.0  sha256:7440d687452800694b86db7aa3627a07d3505d0c21e605dc1f5d25a9f0693702
docker.easydb.de/pf/server-base:5.147.2    sha256:b56b3c4ea7193453de43b7bec196850dac2237576a3d4069774becf77cf7f735
docker.easydb.de/pf/webfrontend:5.147.2    sha256:0c8d9591d7903f8e7b5f88c3485dff4572869350e8a0b522bdc86e61feb4a96c
```
