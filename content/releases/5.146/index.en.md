---
menu:
  main:
    name: "5.146 (End of July 2025)"
    identifier: "5.146"
    parent: "releases"
    weight: -646
---

> This version **does not require** a new index build

# Version 5.145.0

*Released on 2025-07-30*

# Server

## Improved

* **/api/db?all_versions**: add `_child_idx` & `_parent_child_idx` to allow preserving order in migration for some cases.

## Fixed

* **/api/db?all_versions**: fix selection of double-nested objects, improve duplicate detection

# Webfrontend

## Fixed

- **Admin Event Manager**: Fixed several issues with some events in the Admin Event Manager.  
- **Sticky Headers**: Fixed an issue with group headers when sorting results.  
- **Group Editor**: Fixed an issue where the save button state was not updating correctly.  
- **Tags**: Fixed a bug that could display icons in tags that have no icons set if the tag name matches any of our system icons.  
- **FullScreenDetail**: Fixed an error when using the fullscreen detail view with the detail hierarchy list opened in the fullscreen sidebar.

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.146.0            sha256:b203fa1bc898a57d8ba67e4b1f82593d4bbdc53241f0024925734e55bc5ddfad
docker.easydb.de/pf/elasticsearch:5.146.0  sha256:07a0ff763ba5029769b9686dce16a8830e3510ef37202584b94270d91273b67a
docker.easydb.de/pf/fylr:5.146.0           sha256:5de5a8f90a3e27eb6bf506b44b5b17ff7dcd2903d9697fdb723aca4f9f052710
docker.easydb.de/pf/postgresql-14:5.146.0  sha256:298cd7ec49ee09f66b254cae39504cdbed5ddeec5e889c0ddb3785ddea9f2d1a
docker.easydb.de/pf/server-base:5.146.0    sha256:66fa5091d86027680fa03d2071b41f20b8df8dfb6d3a10221830b5e56cb53ce8
docker.easydb.de/pf/webfrontend:5.146.0    sha256:43341d5eb9ba4f211a6f8dba0c5dce9c6e3cba13786931e912dc20a727d257bd
```
