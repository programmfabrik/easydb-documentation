---
menu:
  main:
    name: "5.66"
    identifier: "5.66"
    parent: "releases"
    weight: -566
---

> A re-index is required for this release, please allow adequate time for installing the update. 

# Version 5.66.1

*Published on 24.04.2020*

### Web frontend

*New*

- **Group manager**: Input option for the new **IPv4 filter**.

*Fixed*

- With activated Connector-Plugin there was an error **logging off** the user.

### Server

*Fixed*

- **Startup problems** with activated **connector plugin** were fixed.
- **Startup problems** in some databases during **Easydb asset server** database upgrade.

# Version 5.66.0

*Published on 22.04.2020*

### Webfrontend

*New & Improved*

- **Messages**: The message type `Download` now allows to add a form in which a maximum number of selected checkboxes can be specified.
- **Mask management**: Improved support for sorting multiple fields.
- **CSV importer**: Better organization of linked object options and other minor improvements and bug fixes.
- **Mask management**: Demo data can now be downloaded from the data model instead of just being displayed.
- **Basic configuration**: For larger input forms a `+` button is now used to add more entries. 
- **Connector**: Security improvements in password management.

*Fixed*

- The **upload settings** for folders have in some cases displayed fields from reverse nested without supporting them. The display of the pool in this dialog was also corrected.
- Improved **multi-instance support** when closing the sidebar.
- **Filtertree**: Language dependent output of B.C. data was corrected.
- **New objects**: The display of pools could get confused in some cases.

### Server

*New & Improved*

- **/api/group**: Groups have an IPv4 filter for subnets now. This allows you to filter group assignments to specific IP address ranges. 
- **/api/xmlmapping**: Field names are checked for validity.

*Fixed*

- Problems with **reindex/purge** for multi-instance Elastics installations have been fixed. 
- **/api/search**: sorting for flat hierarchies was fixed.
- **/api/db**: `_path` in old versions is now shown correctly.
- **/api/export**: `easydb_flat` format has been fixed for some cases with reverse nested.

# Checksums

- Here are the checksums of our docker images (latest version)

```ini
docker.easydb.de/pf/chrome sha256:5b01af4f17676ee4295fa3cc279d15f7b6e4a43f9faad41dace54fe1b36861fd
docker.easydb.de/pf/eas sha256:5a35553dcddae1614821a38e8f207b6065b9082ee1499a65fa3b03fed3f2c57f
docker.easydb.de/pf/elasticsearch sha256:1475d92455542b0102cf0ddc6110b17cc452cc986556857dbcf0ab79e888224f
docker.easydb.de/pf/fylr sha256:2fd1ab38a06a2f365984653da1546f56d6cf988602b640266cea91a4129c86b1
docker.easydb.de/pf/postgresql-11 sha256:86172297d81a82a0b303137ed5857783c6419b14358587cef05eb794da627154
docker.easydb.de/pf/postgresql sha256:3374be1a129f4e751fce7b1ddcd561cd209a197faf9faabba5d0454d16946420
docker.easydb.de/pf/server-base sha256:861cc740faf24b9251684bbce9cb5506f8f467c5c1d919dec68c894d8760684d
docker.easydb.de/pf/webfrontend sha256:c5cfc1cca7970c9f7bd6ae351d66f1b93c361044ad81488ae4f2353cb26c0735
```

*Translated with www.DeepL.com/Translator*