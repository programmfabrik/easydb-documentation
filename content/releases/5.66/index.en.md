---
menu:
  main:
    name: "5.66"
    identifier: "5.66"
    parent: "releases"
    weight: -566
---

> A re-index is required for this release, please allow adequate time for installing the update. 

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
docker.easydb.de/pf/chrome               sha256:5b01af4f17676ee4295fa3cc279d15f7b6e4a43f9faad41dace54fe1b36861fd
docker.easydb.de/pf/eas                  sha256:b2fabc3363625c814493745e35a4f0c5c2de5b93eb5c262743f2227ebc6f6b6e
docker.easydb.de/pf/elasticsearch        sha256:1475d92455542b0102cf0ddc6110b17cc452cc986556857dbcf0ab79e888224f
docker.easydb.de/pf/fylr                 sha256:2fd1ab38a06a2f365984653da1546f56d6cf988602b640266cea91a4129c86b1
docker.easydb.de/pf/postgresql-11        sha256:86172297d81a82a0b303137ed5857783c6419b14358587cef05eb794da627154
docker.easydb.de/pf/postgresql           sha256:3374be1a129f4e751fce7b1ddcd561cd209a197faf9faabba5d0454d16946420
docker.easydb.de/pf/server-base          sha256:17b8ba143ef6781417c34506522a617b1d83c0e1391960ad65bb34d5667dcc2c
docker.easydb.de/pf/webfrontend          sha256:b1a0d1ffebd574cebd515803d83a59d8af7a17be4c47a16651401a38e454a70a
```

*Translated with www.DeepL.com/Translator*