---
menu:
  main:
    name: "5.80 (LateFebruary 2021)"
    identifier: "5.80"
    parent: "releases"
    weight: -580
---

> No re-index is necessary for this release. 

# Version 5.80.1

*Published 2021-03-01*

## Webfrontend

### Improved

- **Table View:** for hierarchical objects not all levels of children are opened when an object is clicked

### Fixed

- **Editor:** masks with fields, which are hidden/shown depending on tags, are updated when tags are changed
- **Expert Search:** hide tags which are not enabled in search mode

## Server

### New

- **Server Environment:** effective UID/GID of the server can be set

### Improved

- **Custom Data Type Gazetteer:** old gazetteer custom datatype values that include an older `_fulltext` format, can be updated and fixed using the [Custom Datatype Updater](/en/technical/plugins/customdatatype/customdatatype_updater/#custom-data-type-updater)

### Fixed

- **Privacy:** clear text passwords were removed from the server configuration in the server status, also the output of the server configuration in the server log has been removed

# Version 5.80.0

*Published 24.02.2021*

## Webfrontend

### New

- **User management:** The list of users can now be sorted per column.
- **Editor**: Reverse linked objects can be sorted manually.
- **Search**: Sorting by reverse linked objects.
- **Export**: A new all_languages parameter allows exporting all database languages now also for XML.

### Improved

- **Mask management:** The field width can now also be set for the text view.
- **Typo3 plugin:** When exporting, all configured languages are now taken over, not only the user's set languages.
- Graphical improvements in most views.
- **Event manager:** Sorting has been improved.
- **Detail/Editor:** Multiple fields are now sorted server-side.
- **CSV importer:** Deleting tags is now possible.

### Fixed

- **Presentation:** fixed the toggle to show default info.
- **Detail:** In Zoomer, the 100% button sometimes did not work correctly.
- **Editor:** Copying and immediate closing of the editor was fixed.
- **Expert search:** The search with range details was fixed.

## Server

### New

- **/api/db:** support for manual sorting of reverse linked objects.
- **/api/export:** A new all_languages parameter allows exporting all database languages for all formats.

### Improved

- **/api/.../list:** These endpoints are now only accessible to users with system.root privileges. Previously objects were filtered according to visibility before the result was returned. Thus `offset`and `limit` did not work as expected.
- Performance improvement when loading folders and permissions (e.g. also when saving a pool) 

### Fixed

- **/api/export:** URLs in CSV export were fixed.
- **/api/user/list:** Output of _automatic_authwas fixed.

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:15e82b1a80281b83372c92b0ace52f343bc9eb8457497a76843f3ec8650af8d9
docker.easydb.de/pf/eas                  sha256:fceaf1329c063c6bc6ae8d37e2c2df5076d9aa0d8e2e0f0bf3e51469afd59f7a
docker.easydb.de/pf/elasticsearch        sha256:34843553d665c05e684a5a8c65372c61f232bb3ff5de0767da769b6bb72f99e5
docker.easydb.de/pf/fylr                 sha256:7c1b6949957fa32c9dd90f0710b92b109dd2b298c03aa6d7f5f665eb68594602
docker.easydb.de/pf/postgresql-11        sha256:8c9ac649827eec7cdb080cd2ffb5fcc865066093e95c196f0e529e91a3b07ce5
docker.easydb.de/pf/server-base          sha256:4dd13ff0378f8d8765032dd9ae06cdc19818bac4e190c56fcd46956118060404
docker.easydb.de/pf/webfrontend          sha256:aa7f77841af2a74bfd95be3b4fcb55c51a8f520e35b1847172093aafb27fedd9
```

*Translated with www.DeepL.com/Translator*