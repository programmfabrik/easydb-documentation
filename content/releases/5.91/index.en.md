---
menu:
  main:
    name: "5.91 (October 2021)"
    identifier: "5.91"
    parent: "releases"
    weight: -591
---

> This version **does not require a new index build**, the new Elastic image works with the existing index files.

# Version 5.91.0

*Released on 20.10.2021*

## Web frontend

### New

- **CSV importer**: `system_object_id` can be used for linked object types and hierarchical fields for mapping.
- **CSV importer**: support for data input as text.
- **Plugins**: support for central loading (easydb 6) of all files.

### Improved

- **Detail**: Linked objects with assets now show graphically if they have more than one asset.
- **IUCN plugin**: use bulk API for accelerated queries.
- **Search**: improved display of filter names when localization is missing.

### Fixed

- **Search**: When filtering empty searches with hierarchical object types, the top-level filter is now no longer automatically removed for top-level-only searches.
- **Script Runner**: Fields Migrator did not work for masks with splitters.
- **Datamodel**: Reverse Edit was always displayed as deactivated in the "Current" data model, even if it was activated.
- **Datamodel**: Display of localized name for reverse object types was incorrect under certain circumstances.
- **Editor**: Sending time zones was corrected when saving (easydb 6).
- **New objects**: Display from pool was not visible under some circumstances.
- **Search**: Filter for tags was fixed.

## Server

### New

- **New language**: `fi-FI` (frontend preparation & database).

### Improved

- **XML export**: no automatic semicolon between entries, this can be set up manually with a fixed value.
- **Hierarchical objects** can use values of parent objects in default (in reverse).
- Accelerated processing of **/api/event/poll**.
- **XML export**: addition of asset name on export.
- **Schema update**: improvements in switching from text to localized text.
- **Accelerated authentication** of anonymous users.

# Checksums

Here are the checksums of our Docker images (latest version): 

```ini
docker.easydb.de/pf/chrome               sha256:c7a06bca14634f897e8b300fb5e3f624d89adb0dd8cfb746e92975a81868974b
docker.easydb.de/pf/eas                  sha256:33d981b6e54af916e03f38f299c546e053e348cdf5541fc0cdf61cb14d3a8e3f
docker.easydb.de/pf/elasticsearch        sha256:9caf333392a56946bc28e68251c4c146e017b901920ff3042054cd2e14f577b2
docker.easydb.de/pf/fylr                 sha256:fbb1b412cfc82477393ec65c2135d261e3de26507f589c1141d952db8e333d05
docker.easydb.de/pf/postgresql-11        sha256:29114c653a20bafbf505864b0fc1fe3b85b276656620cddd36a65a4dc90b4284
docker.easydb.de/pf/server-base          sha256:1ed640d5d9c5c02e47b196990d93ea62d3f004bd1b558458efac5ec23ebaeade
docker.easydb.de/pf/webfrontend          sha256:17a3b9b783ad360374ed743183a2ad93829e024bd0f2b811e940c0856cfb8464
```

*Translated with www.DeepL.com/Translator*