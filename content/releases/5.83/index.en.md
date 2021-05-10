---
menu:
  main:
    name: "5.83 (May 2021)"
    identifier: "5.83"
    parent: "releases"
    weight: -583
---

> No re-index is necessary for this release.

# Version 5.83.1

*Published 10.05.2021*

## Webfrontend

* group edit mode allows batch size of 1 to circumvent errors when objects with mutual links are edited
* fixed wrong object type in table view
+ fixed wrong types in export
* fixed error at asset fields in expert search

## Plugins

* fix lockup in auto keyworder when database schema is committed
* fix error with pending tasks in connector

# Version 5.83.0

*Published 05.05.2021*

## Web frontend

### New

- **Export**: Support of templates for export.
- **Editor**: option for hierarchical lists to link only objects without children (leaves only).

### Improved

- **Accessibility**: Placeholders and annotations added for some fields.
- **Date range:** Display of textual represenation improved.

### Fixed

- **Custom data type location:** automatic correction of old data as part of regular updates.
- **Upload**: A Javascript error could occur with certain combinations of linked objects and metadata profiles.
- CSV Importer: Support for line breaks in multiple fields.
- **CSV Importer**: Re-import of columns with *easydb|* prefix has been fixed.
- User CSV importer: insertion of users was fixed.
- **Editor**: Boolean values from templates were not filled correctly.
- **Editor**: Fixed error with pool management enabled in reverse linked objects.
- **Search**: Selection of hierarchical objects in table view did not work correctly in some cases.
- **Export / Download**: Support for very complex data models where previously a limit was reached on the number of fields in Elasticsearch.
- **Export / Download**: Mask settings without *filter* column enabled caused files of linked objects not to be exported.

## Server

### Improved

- Improvements in **XML export** when including linked objects
- Improved error when trying to re-archive an already archived user
- Improved error when trying to edit bidirectionally linked objects with the group editor
- Archived LDAP and SSO users are reactivated when logging in again
- IP addresses are removed from events and will not be stored there in the future (affected only a small part of event types)
- Implemented server-side sorting by "default" of linked objects

### Fixed

- Version specification in EXPORT_OBJECT events corrected
- Error when specifying invalid fields in exclude_fields of search corrected

## Plugins

### Hotfolder

- Encoding problems fixed
- Fixed problem with capturing without metadata profile
- Appending assets in nested fields fixed

### Auto-Keyworder

- Update in Auto-Keyworder fixed

## Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:61f854f622586be9bcd7cb68d31d56b7578421ac5352a7cbaa00b39011f376b2
docker.easydb.de/pf/eas                  sha256:61702fe554b6b1dc57adfa35ef148e8b821058fd5fd0566fe355f805b38350ad
docker.easydb.de/pf/elasticsearch        sha256:e62e8c0a3b299c15f2d8c3f134e5d5f6123bf109d931bdf58c647e48663d36df
docker.easydb.de/pf/fylr                 sha256:a851233526c2fe3d063672e2ebb598fdd166e2d0eaf55b002312ae6af85271c1
docker.easydb.de/pf/postgresql-11        sha256:ef5daf3bad0933736b4f41a5f98e9b9c0e47738a8e01708683972b00fe8da7ce
docker.easydb.de/pf/server-base          sha256:a93b4bba8ea96220995b7729b6ecc006cde5faa7258cf990aac87bf9fcb6d9de
docker.easydb.de/pf/webfrontend          sha256:a848845fd50e0f6240f8ecb21034261384636aae82cb85ea57a6771692044aa2
```


Translated with www.DeepL.com/Translator
