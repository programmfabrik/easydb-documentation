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

# Version 5.90.0

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
docker.easydb.de/pf/eas                  sha256:f9c00a88acc1363657184902da0bcf137df97baca67a6203a5823f2c53323279
docker.easydb.de/pf/elasticsearch        sha256:81314bcaa640d8a366733a242c6902aaee32b4aaadfa2be86999a6ddc266c5e3
docker.easydb.de/pf/fylr                 sha256:cad5248dab0ddaddb7d93aa0f53a580507963636922b14d42ef259c73cfcad4e
docker.easydb.de/pf/postgresql-11        sha256:7d4565382d4ac1beb9d1ef7a9b97800605a9f8bfef34210e66531bb7c9f68045
docker.easydb.de/pf/server-base          sha256:e5f3910faee1d4927001e43bf49d2411ee09289b49d45b50f03ac0a7552f1854
docker.easydb.de/pf/webfrontend          sha256:003619e5341f91941a5edf1c05183d135ee3f3f312404c24ca0ae2d02418d34e
```
*Translated with www.DeepL.com/Translator*