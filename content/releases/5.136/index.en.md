---
menu:
  main:
    name: "5.136 (August 2024)"
    identifier: "5.136"
    parent: "releases"
    weight: -636
---

> This version **does not require** a new index build

# Version 5.136.0

*Released on 2024-08-29*


# Webfrontend

## New
- Custom Fields Placeholders: A new field has been added in the mask editor to add custom placeholders in the fields.
- Nested Tables: A new option has been added in nested tables to hide the first empty item in a nested table. This provides a more compact UI in data models where nested tables have many fields.

## Improved
- Data Model Manager: The error message when attempting to delete an objecttype being used as a linked object in another objecttype has been improved. The message now includes the full path of each field where the objecttype is used, making it much easier to identify the fields that need to be modified before proceeding with the deletion.
- Default Values Plugin: The plugin `editor-tagfilter-defaults-plugin` has been updated to allow default values to be configured for bool fields.
- Editor Templates: Now the name of a new editor template is checked before saving. If an existing template has the same name, the user will be asked to introduce a different name.
- Objectstore: Support has been added to configure an instance as "pull-only" in the objectstore. Ez5 instances using this objectstore instance will only be able to pull new data models but won't be able to modify them.
- Scheduler: The schedule form in the user panel has been improved to prevent invalid data combinations, such as selecting both days of the week and specific days of the month.
- Filter Panel: The behavior of hierarchical filters when using the OR operator in the filter panel has been improved.
- Event Manager: The filename when exporting a list in the event manager has been improved.

## Fixed
- Fulltext Suggestions on Expert Search: Fixed full text suggestions in string inputs of expert search. The wildcard will now be correctly added.
- Detail Hierarchy: Fixed an issue where hierarchies were not displayed correctly in the detail panel.
- Tag Filters: Fixed an issue in the filter panel when attempting to display tags without text in the name.

# Server

## Improved

* `/api/db?all_versions`: add hierarchy `_level` to all versions
* Extensions to auto keyworder plugin

## Fixed

* fix for special metadata types preventing correct upload of some files 

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.136.0            sha256:841f65883c90252a73ab1a101c88f76b9842ffb6275be7460cb52b32b5be3b81
docker.easydb.de/pf/elasticsearch:5.136.0  sha256:1480fbb397bd5258dbed1c4275003696b8b862542bcd754449ae941e602dae04
docker.easydb.de/pf/fylr:5.136.0           sha256:78fbe5dfda52339fe92609e3c1a033be3fa6bcac7944ace3ad5a3eb24dbf1c89
docker.easydb.de/pf/postgresql-14:5.136.0  sha256:f50d2d5759520962f49c49f68eb14c1541691de955f169ab22dba64fd9cf8325
docker.easydb.de/pf/server-base:5.136.0    sha256:c4a7fe799f934a6d7b4e096703dc1e8b708e8f9cce59bd45ed02d153b246d577
docker.easydb.de/pf/webfrontend:5.136.0    sha256:a2a3a209d7c892f5f24352198d36a162b5722eec8439fd8d11553ff785f3f21a
```
