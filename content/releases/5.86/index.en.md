---
menu:
  main:
    name: "5.86 (Early July 2021)"
    identifier: "5.86"
    parent: "releases"
    weight: -586
---

> A **re-index** is required for this release, please allow appropriate time to apply the update.

# Version 5.86.2

*Published on 21.07.2021*

## Webapp

### Improved

- **Detail**: The display of the URL in the parts display has been broadened.

### Fixed

- **Collections**: The selection (with ALT) of object types that are not displayed in the skin search was issued for the configuration of the upload, since objects in such object types cannot be collected in folders.
- **Plugin custom-mask-splitter-detail-linked**: The data model used for the display was incorrectly the development model but not the current one.
- **Search**: The selection of a sub-pool in the filter could not be carried out in some databases.
- **Search**: The Resource selection menu could not correctly display the special case of only one object type without a pool.

## Server

### Fixed

- **Collections**: Fixed bug when moving folders between different users.

# Version 5.86.1

*Published on 07/13/2021*

## Webapp

### Fixed

- **Search**: A recursion problem in the filter tree has been fixed
- **Data model**: An error resulted in an illegal duplication of the reverse mask when copying object types with a reverse-linked object type. This bug had no visible effect.

## Server

### Fixed

- **Index**: Indexing of date ranges for the filter tree has been fixed.

# Version 5.86.0

*Published 07.07.2021*

## Webapp

### New

- **Detail**: There are now back and forward buttons in the display.
- **Data model**: Support of a context menu when creating.
- **Pool / group manager**: display of modification and creation date.
- **Detail**: In the share menu there is now a button to call the links.
- Beta: Support of **combined filters** (only in debug mode).

### Improved

- Keyboard focus changes for **improved accessibility**.
- **Editor**: The preview bar can now be manually adjusted in width.
- **CSV importer**: Support for emptying fields.
- **Layout improvements** in system permissions, print dialog and base configuration (the latter only easydb 6).

### Fixed

- **CSV importer**: Imports of timestamps with time zone no longer lead to an error.
- **Finder**: Javascript errors could occur when filtering some map types.

## Server

### New

- `pool` and `group` now have a `created_timestamp` and `last_updated_timestamp`.

- **Date range fields** can be aggregate and search the middle of dates via `:middle`.
- **Build info** for plugins is generated.
- Support for **Postgres** version **12** and **13**.

### Improved

- **Performance improvements** when **loading folders**.
- Warning when deleting **metadata mappings** that are in use.
- Filters for **date ranges** now work with the center of the range.

### Fixed

- **XML export**: output of EAS URL also in linked objects.
- **CSV export**: output of `_standard` was not done correctly when selecting fields manually.

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:dec745a2f97ff54e3fb34289c0ac5abc368bc8dcbb95ec93fe6124d35c9574c5
docker.easydb.de/pf/eas                  sha256:18f3f17f11d865a1ad953d36541747dde4fb1363a0e8e2174f5a23989c3dd768
docker.easydb.de/pf/elasticsearch        sha256:01564b2dbaf9cb2d7d1666fd2d954ffc61cf0bde2ea6a598330a31c5ab0e56a4
docker.easydb.de/pf/fylr                 sha256:386ee9ef4249ebda216bc4818d09fc84cd3f94ce062ceb2c0c64941b5cb58612
docker.easydb.de/pf/postgresql-11        sha256:4454c79b53e696726507f934be08705ef16916641548d922186838b83f993309
docker.easydb.de/pf/server-base          sha256:1cb11fbc288e89513be11ff635028556a7ba9c7ca72b9e5eb38e3c74c881a0f4
docker.easydb.de/pf/webfrontend          sha256:005dc15b9428f22e6db4b321632cde4ed35934b020825a8ec49d52694f19ad35
```

*Translated with www.DeepL.com/Translator*

