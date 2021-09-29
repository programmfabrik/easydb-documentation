---
menu:
  main:
    name: "5.89 (Early September 2021)"
    identifier: "5.89"
    parent: "releases"
    weight: -589
---

> A **re-index is required** for release 5.89.0, please allow appropriate time to apply the update. 

# Version 5.89.2

*Published 20.09.2021*

## Web frontend

### Fixed

- **Powerpoint export**: Calling the exporter is now possible again.
- **Collections**: Share links did not work correctly in some cases.

## Server

### New

- **Pool management**: The rights check for folders can be skipped by users with the `system.root` right after confirmation.

# Version 5.89.1

*Published 10.09.2021*

## Web frontend

### Fixed

- **New objects**: In some cases the dialog did not open correctly and a javascript error occurred.

# Version 5.89.0

*Published on 08.09.2021*

## Web frontend

### Improved

- **CSV importer**: update support for number fields has been added.
- **Metadata**: *Fixed Value* can now be changed.
- **Mask management**: More sort fields for multiple fields in **FYLR** (easydb 6).

### Fixed

- **Collections**: Improved error handling for linked object types with asset fields.
- **Detail / Editor**: Corrections for paths in format *Short* of linked objects.
- **Search**: Fixed display problem with reverse nested objects in table view.
- **Editor**: Minor fixes for textual recognition of dates.

## Server

### Improved

- **/api/user**: More fields searchable by users.
- **Suggest index** building is 20-30% faster.
- **Plugins**: The configuration files for plugins have all been renamed to `manifest.yml`.

### Fixed

- **/api/collection**: create_object is updated when corresponding base types are affected.
- **/api/user**: Improved error message if wrong version.

# Checksums

Here are the checksums of our Docker images (latest version): 

```ini
docker.easydb.de/pf/chrome               sha256:b5fe29ee03c23bea847c4333ad8d675ed333d51834ce8ee5855072e213a4a5c8
docker.easydb.de/pf/eas                  sha256:1031f6e7459e430a3233d38f5a3678562fde6bf2e578672838b4128a1eb258d1
docker.easydb.de/pf/elasticsearch        sha256:2a9ca9620e35567d8ea6c666055e4377ca556d16b0a619f2198d9cc9fe9bc526
docker.easydb.de/pf/fylr                 sha256:a8e34a88bb2604f5f4cfc58776854f7cc2b07979c55171d017eabc54821a9652
docker.easydb.de/pf/postgresql-11        sha256:b5cd1da4a100450e07b3f6111a4842b1741b018465c6923e62ab636a705c2b93
docker.easydb.de/pf/server-base          sha256:e341f0e9857e1ea18b349037f55807691b955133b17f70888ca4dbf4a2c85d20
docker.easydb.de/pf/webfrontend          sha256:53d135e2aa1f159d3d0c53e7982f0870448e8dd437f71d2fe0019a23a9e0dc12
```

*Translated with www.DeepL.com/Translator*