---
menu:
  main:
    name: "5.147 (End of August 2025)"
    identifier: "5.147"
    parent: "releases"
    weight: -647
---

> This version **does not require** a new index build

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
docker.easydb.de/pf/server-base:5.147.0    sha256:6dbb178e20d095ea743f1ff7c6a17fef6b192fc04a2cbbc024763d31b5c3432b
docker.easydb.de/pf/webfrontend:5.147.0    sha256:00d732e5f7bf227605c0128c389904f68d332bfb8a49654346045a2e615480f4
```
