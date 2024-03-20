---
menu:
  main:
    name: "5.124 (Early November 2023)"
    identifier: "5.124"
    parent: "releases5120"
    weight: -624
---

> This version **does not require** a new index build

# Version 5.124.0

*Released on 2023-11-01*


# Webfrontend

## New

* **Collections**: display of shared collections is now paginated, limited to 100 collections per page
* **Detail View**: for each objecttype, remember the mask that was used the last time

## Improved

* **Import of users with CSV**: added support for import of user passwords
* **Search**: Improved visibility of used wildcards in the suggest/autocomplete popup
* **Quick Access**: also show linked objects where the `Filter` option in the mask setting for `Search` is enabled
* **CSV Importer**:
  * Fixed importing of number fields
  * Improved importing of daterange values with a textual representation
  * Tags can be imported by the `shortname` or `reference`
  * Added filter options for rows: allow to filter by warnings and operations

## Fixed

* **Filter Tree**: fixed filtering for linked hierarchical objects
* Fixed error when loading the transitions panel


# Server

## Improved

* **Hotfolder-Plugin**
  * Recognizing and linking of file series (files with matching basename suffixes like `-1`, `-2` etc.) has been improved
  * Importing with metadata mapping: improved handling of pools in linked objects


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.124.0         sha256:88a93e887dc95b48f03fa0fb3c16cc3c90722914e3c797a07c8784fa23d8c904
docker.easydb.de/pf/eas:5.124.0            sha256:6fcdcb1a2032aaf0c478b4b418719dc7f3c88ebf3532f2b69bba70cd170da520
docker.easydb.de/pf/elasticsearch:5.124.0  sha256:e2de1132d7d569ac20250cb9e7e2ba15079d4e422a2e558ce5cd4225cdb8c74a
docker.easydb.de/pf/fylr:5.124.0           sha256:3507a1fe66d21e0e208f3a51758b83ed67379693ad231db5038bb3ff0414496b
docker.easydb.de/pf/postgresql-14:5.124.0  sha256:2e0f69218239ac4f3cadf5b3bd1fc871ea2306c0877f96b0ebeba967e98183f0
docker.easydb.de/pf/server-base:5.124.0    sha256:051e8108ce6beccc3a22519f0da892cb4fa5c1eaa2da582c3aad5942b976b03e
docker.easydb.de/pf/webfrontend:5.124.0    sha256:e242f10dfa4e544ec16148aabef274e877529ffdfe9289343ed37fa888a17a76
```
