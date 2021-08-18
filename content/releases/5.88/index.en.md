---
menu:
  main:
    name: "5.88 (August 2021)"
    identifier: "5.88"
    parent: "releases"
    weight: -588
---

> No **re-index** is necessary for this release. 

> The **plugin names** and configuration files have changed. For plugins delivered by Programmfabrik, the configuration file is now always called `manifest.yml`. More information can be found [hier](https://docs.easydb.de/en/technical/plugins/#plugin-definition).

# Version 5.88.0

*Published on 18.08.2021*

## Webfrontend

### New

- **Mask management**: A new option allows to render only the first entry of multiple fields in the standard info.
- **User management**: Various sorting options for the user list have been added.

### Improved

- When creating a **new email user** in the user search (e.g. folders), you can now always create a new user, even if a similar email already exists in the system.
- **Metadata**: `Fixed value` dialog can be canceled.
- **Editor**: Changing the pool did not activate the save button in some cases.
- **System messages** on unreachable servers was improved.
- **CSV Importer**: Uploading hierarchies has been improved and now allows referencing parent records from the CSV, i.e. records that are not yet in the database.
- **Folders**: Moving a folder to the highest level is now possible.

### Fixed

- **Asset Browser**: The display could not be switched in some cases and a javascript error occurred.
- **Editor**: The date range field did not automatically fill in the to date in some cases.
- **PDF Creator**: Display error for text fields fixed.
- **Fullscreen view**: Display of empty objects (without image) now shows placeholder text.
- **Detail/Editor**: Display of tags for linked objects in text mode has been fixed.
- **Search**: Javascript errors could occur in the filter when the development data model was changed.
- **Search**: In the table view, some rows disappeared after the records were edited.

## Server

### New

- Support of `.obj` files as `vector3d`.
- Standard info in multiple fields can now consider only the first entry.

### Improved

- Changes in plugin names and paths.
- Improvements in internal HTTP call of Easydb asset server.

- **Standard info** for date ranges now only shows a date if from and to are the same dates.

### Fixed

- **/api/schema**: When loading new data models, masks with reverse linked object types are maintained correctly. Previously, inconsistencies could occur in the data model, but this has no further effect.

- **/api/db_info**: Queries with pool_id for object types without pool support no longer cause errors.
- **Memory management** bug fixes.

# Checksums

Here are the checksums of our Docker images (latest version): 

```ini
docker.easydb.de/pf/chrome               sha256:ce4ccb312e12cdcb8daa9151e80081738b2612b1c109ecdcb39519e3f367c6ec
docker.easydb.de/pf/eas                  sha256:ca98bb2b8ad5b7f185e730446752153dfc5fac0b8bae5e06326aa41b66b794b4
docker.easydb.de/pf/elasticsearch        sha256:5432f0d5bd8ad5a8695e300ffa86db1d13c5183b12a70ce5f76c77a0e6b3c209
docker.easydb.de/pf/fylr                 sha256:c468d4f73670d4fb2b40b62290c3a680ba83ed611b5991102c940c15013d7272
docker.easydb.de/pf/postgresql-11        sha256:0edc0e28c643c886790c5b5d84ab224e4950edaad3b4d27dda04fa875c0f6ce1
docker.easydb.de/pf/server-base          sha256:4b3890e40111bf3ffe1f852f098d3bd3c241b601f77a2a6c9e6f2813e798c11c
docker.easydb.de/pf/webfrontend          sha256:25d9660da3ec81005611e342744ded663f343d4f75a43bdf173ac7c3591d12c9
```

*Translated with www.DeepL.com/Translator*
