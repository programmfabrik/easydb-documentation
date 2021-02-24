---
menu:
  main:
    name: "5.80 (LateFebruary 2021)"
    identifier: "5.80"
    parent: "releases"
    weight: -580
---

> No re-index is necessary for this release. 

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

- **/api/.../list:** These endpoints are now only accessible to users with system.root privileges. Previously objects were filtered according to visibility before the result was returned. Thusoffsetand limit did not work as expected.
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
docker.easydb.de/pf/server-base          sha256:34cfb296d10a1cd71dcd7fa13cbffce8966646959ac76c320f0bb07b3ab8b707
docker.easydb.de/pf/webfrontend          sha256:a06b01b808e82b72d115cdab76a3ac2bccc1b81a62306989eaff4393dc16f4b4
```

*Translated with www.DeepL.com/Translator*