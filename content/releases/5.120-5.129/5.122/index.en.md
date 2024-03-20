---
menu:
  main:
    name: "5.122 (September 2023)"
    identifier: "5.122"
    parent: "releases5120"
    weight: -622
---

> This version **does not require** a new index build

# Version 5.122.0

*Released on 2023-09-20*

# Webfrontend

## New

* **Base Configuration**: for changes in specific keys (like `email` settings), before saving the user needs to confirm these changes
* **Plugins**: plugins will be displayed using the `name` property
  * the `display-name` property is now deprecated
* **Detail View**: in the change history, the responsible user is always shown

## Improved

* **Print Manager**: improved field selection button
* Corrections in the textual representation of daterange fields
* Default search settings for collections have been changed to display 100 objects instead of 10
* **Display Field Values Plugin**: added more top level fields that can be selected

## Fixed

* **Event Manager**: multiple smaller bug fixes
* **Detail View**: errors in buttons in the template manager have been fixed
* **Json Importer**: fixed problems when URLs are replaced

# Server

## New

* **XML Export**: export of reverse nested objects: added output of `_version` and `_pool`

## Improved

* **Performance**: shorter loading times for (unmodified) schema and maskset

## Fixed

* EAS URLs for files that have been inserted into the easydb5 from a remote URL, the generated filename is fixed
* **XML Export**: export of reverse nested objects: fixed output of `_id`
* **Datamodel**: fixed `UNIQUE` constraints for daterange fields

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.122.0         sha256:dbca3ff79c4853f2c6b683af8ecf48da05939923a44769062c37aa1e39caffb3
docker.easydb.de/pf/eas:5.122.0            sha256:2c50af6c3aac6136d81e1d4f4a2ff08359a89162cb45d770ebecdc109bdc3b82
docker.easydb.de/pf/elasticsearch:5.122.0  sha256:bd3f0199ae861484335ffa00be9e3d023cfd0a96066a8563b61a4077e19b4236
docker.easydb.de/pf/fylr:5.122.0           sha256:f1e2e6e68011e39b54627ab0efe74027cad5e9b23af2785f2807a4bcd882edf6
docker.easydb.de/pf/postgresql-14:5.122.0  sha256:ee1b5ab450b2fd1e3c0954009da188283db6215c83aad20daf65b77c81799793
docker.easydb.de/pf/server-base:5.122.0    sha256:a9a495c3a67082b143de74a583f5c98afb2d043413d1cd3c10b5cd46236788e1
docker.easydb.de/pf/webfrontend:5.122.0    sha256:641ef40f79309007619f0360490159762a42fa89b21c94eea2f5ef913bbedba0
```
