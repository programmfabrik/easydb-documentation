---
menu:
  main:
    name: "5.149 (October 2025)"
    identifier: "5.149"
    parent: "releases"
    weight: -649
---

> This version **does not require** a new index build


# Version 5.149.1

*Released on 2025-11-10*


# Webfrontend

## Fixed

* **Fullscreen**: Fixed display errors

# Version 5.149.0

*Released on 2025-10-29*


# Webfrontend

## Fixed

- **Sort Manager / Expert Search Panels**: Fixed a bug that prevented the sort criteria configured in the sort manager from being processed correctly if the panel containing the field was closed in the sort manager.
- **Has Value**: Fixed multiple issues related to the expert search filter “has value”.
- **Default Tags**: Fixed a bug that caused default tags that were also configured as hidden not to be added correctly.
- **Shared Collections**: Fixed pagination issues in shared collections when a user had more than 100 shared collections.
- **Tag and Workflows**: Fixed a bug that prevented the workflow panel from opening if the saved data contained any errors, thus preventing the user from correcting them.
- **Collection Presentation**: Fixed a bug that could prevent a presentation within a collection from being opened and edited if one of the assets was no longer available.
- **Nested Table**: Fixed a bug where a new row was incorrectly added to an empty nested table when loading an asset into an EAS column in the first row. The file now loads into the correct row.
- **Export Transport**: Fixed a bug that prevented the transport editor in the export manager from opening if the transport data was invalid, making it impossible to fix the data.
- **Group Editor**: Fixed the order of control buttons and checkboxes

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.149.0            sha256:dd77214b2d62b084faadfe28490aa984de48b7758fa7028368e867b232b1ad0a
docker.easydb.de/pf/elasticsearch:5.149.0  sha256:f2004f759cfd7f3218d6f15d9b972de3d9cccad3a2efa98bdb3f16bd084f7ac2
docker.easydb.de/pf/fylr:5.149.0           sha256:30a320ea3f95b5fa2300a93d701b327343598c0e074e76ce523967ec66ddda55
docker.easydb.de/pf/postgresql-14:5.149.0  sha256:1d2874de390056e7ff7e8401d4e9a3ac2c1a8b0fe75fc161c1effac8aa11fe38
docker.easydb.de/pf/server-base:5.149.1    sha256:911b8444e23cb3e0d8f0b09c48b51b68be1aa64300c6eadd4e0aeba8caad83de
docker.easydb.de/pf/webfrontend:5.149.1    sha256:e786aa4427ff0374454ac4e0cc62e7873689b2b458e02bdac8fd932669f13556
```
