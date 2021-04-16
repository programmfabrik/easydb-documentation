---
menu:
  main:
    name: "5.82 (May 2021)"
    identifier: "5.82"
    parent: "releases"
    weight: -582
---

> A **re-index** is required for this release, please allow appropriate time to apply the update. 

# Version 5.82.0

*Published on 14.04.2021*

## Webfrontend

### New

- **Editor**: With the new function "Filter for linked objects" searches of linked objects can be filtered automatically.
- **User manager**: Display and search of archived users.
- **Data model**: Support of server-side sorting of multiple fields.
- **Mask management**: Panels can now be expanded automatically if they are not empty.

### Improved

- **Export**: The _uuid field has been added to the field selection.
- **Workflow**: After saving, the workflow tab remains active.

### Fixed

- Folders without names no longer lead to an error.
- CSV Importer: Saving mapping with tags has been fixed.
- CSV Importer: Non-searchable fields are ignored.
- **Export**: Non-searchable fields are ignored.
- **Editor**: Input in date range fields when From or To is empty has been fixed.
- **Mask management**: Preview was fixed for big data model.
- **Change history**: Tags are no longer shown twice.

## Server

### New

- **Exporter**: In CSV format _uuid,_tagsnud _last_modified_date are exported.

### Improved

- **Folders**: General speedup of permissions checks for shared folders. This also affects the speed of saving pools.

### Fixed

- **Export**: Loading of linked objects in XML export has been improved and partially fixed.
- **Hotfolder**: Several bug fixes for complex object structures.
- **User**: Some cases for pseudonymization were fixed.

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:e3599220fca5194ee6b1e4792a10009982b4528f4484162d9b6a8da42b2bae10
docker.easydb.de/pf/eas                  sha256:6da52cee973c66ff69e61ced2f8b1cef36dcd4cd89fd7a091143a32b95d0e022
docker.easydb.de/pf/elasticsearch        sha256:efacf01d4b972fbfd87923598b48a761dab2d01d95282b6d987cf8932d10974e
docker.easydb.de/pf/fylr                 sha256:8a8d3be7d46ee32cbcea12b0fad14be82ebec8845b8d4e68c2288947a89e9d4b
docker.easydb.de/pf/postgresql-11        sha256:16374ce88db01d7b83f785423a04616f5175a6b52ff190cc19d8e5972f11a611
docker.easydb.de/pf/server-base          sha256:a17434bc4ca0584a01e775554831cb650fbc66f81cc032c632bbc00f5731badd
docker.easydb.de/pf/webfrontend          sha256:179a5190f4d1ab3a99e4a673188196aa2a7953c8094971613a70a882ec9ed9b5
```

*Translated with www.DeepL.com/Translator*

