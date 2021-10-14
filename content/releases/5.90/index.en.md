---
menu:
  main:
    name: "5.90 (Ende September 2021)"
    identifier: "5.90"
    parent: "releases"
    weight: -590
---

> This release **includes a new Elastic Docker image** (version **7.15.0**). We had shipped a version of Elastic in the last releases that had some unpleasant performance properties, so the aggregations (filters) were sometimes very slow. These problems should now be solved with **7.15.0**. We don't know exactly since when Elastic had this performance slump, for sure we know that **7.10.0** was still ok.

> This version **does not require a new index build**, the new Elastic image works with the existing index files.

> In this version, **unused files in the system** are marked in preparation. This is done by setting a negative EAS ID. As a result, these assets are no longer available to the server and would report an error if accessed. Currently no files are actually deleted, this will come in one of the next versions.

# Version 5.90.2

*Published 14.10.2021*

## Web frontend

### Improved

- **Performance**:
  - better usage of caches for `api/v1/l10n/user/CURRENT`

### Fixed

- **Editor**: do not allow saving before the request that saves an object has completly returned. This avoids inconsistent states between the editor and the current object in the server

## Server

### Improved

- **Performance**:
  - Better usage of caches: Requests for `api/v1/l10n/user/CURRENT` are cached
  - Improve speed of event polling

# Version 5.90.1

*Published 11.10.2021*

## Web frontend

### Improved

- **Performance**:
  - use a minified version of the web frontend javascript to reduce load time
  - better usage of caches for `api/v1/objecttype`

### Fixed

- **Editor for new objects**: fixed problems with missing pool selection for linked objects
- Bug fix for tag facetting
- Bug fix for possible reload problems when deleting linked objects

## Server

### Improved

- **Performance**:
  - Better usage of caches:
    - Requests for *CURRENT* schema and maskset are cached to drastically reduce time for repeated requests
    - Use cache headers for requests to base db
  - Responses for *CURRENT* schema and maskset are compressed

# Version 5.90.0

*Published 29.09.2021*

## Web frontend

### Improved

- **Popover searches**: In filtered hierarchical subsearches, it is now no longer possible to select parent objects that are not covered by the filter, but are needed to display the hierarchy. Such objects are marked grayed out.

### Fixed

- **CSV Importer**: An update problem related to hierarchies has been fixed.
- **CSV Importer**: A problem with object types without available tags was fixed.
- **Editor**: The Save button was enabled in rare cases without saving being allowed.

# Server

### New

- Support for Apple's `HEIC` file format (**High Efficiency Image File Format**).
- **/api/objects**: version access by date was implemented.

### Improved

- **Easydb asset server**: The Python-based server for managing files now runs Python 3 instead of Python 2.7.

### Fixed

- **/api/db**: Access to deleted objects is blocked now.
- **/api/schema**: Creating a file field with a name that existed before was fixed.

# Checksums

Here are the checksums of our Docker images (latest version): 
```ini
docker.easydb.de/pf/chrome               sha256:b5fe29ee03c23bea847c4333ad8d675ed333d51834ce8ee5855072e213a4a5c8
docker.easydb.de/pf/eas                  sha256:ca4eae963eae7986706ce66dac3bb5c2de6fd05672086dcb2810b6378ada8cd3
docker.easydb.de/pf/elasticsearch        sha256:81314bcaa640d8a366733a242c6902aaee32b4aaadfa2be86999a6ddc266c5e3
docker.easydb.de/pf/fylr                 sha256:cad5248dab0ddaddb7d93aa0f53a580507963636922b14d42ef259c73cfcad4e
docker.easydb.de/pf/postgresql-11        sha256:7d4565382d4ac1beb9d1ef7a9b97800605a9f8bfef34210e66531bb7c9f68045
docker.easydb.de/pf/server-base          sha256:e6eab654b35a4296c775f1a3eb11ccf4e9a4720994841881389185b1e8c0ee71
docker.easydb.de/pf/webfrontend          sha256:cb263dce2325534d1b848ac9914346967d22d4672ecf1305ed621e5b68ea0fe0
```
*Translated with www.DeepL.com/Translator*
