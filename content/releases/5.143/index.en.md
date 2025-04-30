---
menu:
  main:
    name: "5.143 (Late April 2025)"
    identifier: "5.143"
    parent: "releases"
    weight: -643
---

> This version **does not require** a new index build

# Version 5.143.0

*Released on 2025-04-30*


# Webfrontend

## New

* **CSV Importer**:
  * Added support for multi-nested values in "Date Range" fields
  * Users can now include multiple nested values in the same "From" cell

## Improved

* **Search Input**:
  * Improved query execution to prevent invalid searches, query input is now validated before auto-execution
  * Improved parsing of query input to correctly apply `OR` and `AND` operators
* **Boolean Field**:
  * Updated the boolean field view in the editor to always display "Yes", improving clarity.

## Fixed

* **Display Field Values**:
  * Fixed an issue in the plugin that prevented loading owner fields when Groups were used instead of Users
* **Workflows Validation**:
  * Fixed silent error in `getSaveData` method in `TagTransition`
  * Also resolved issue where multiple warning icons appeared in invalid workflows
* **Read-Only Mode**:
  * Disabled hotfolder drag-and-drop and prevented adding new objects to collections in read-only mode
* **Main App**:
  * Fixed error when dropping a file into the main app
* **Query Element Field Editor**:
  * Fixed rendering issues with fields requiring a search instance
* **Change History Diff View**:
  * Fixed error caused by accessing null properties during diff calculation
* **CSV Importer**:
  * Fixed unhandled error when importing linked objects via CSV


# Server

## New

* **Api**:
  * `/api/v1/user?include_last_seen=true` adds `_last_seen_at` timestamp to `user`, if the user logged in at least once

## Improved

* **Search**:
  * Switch subfield for `fulltext` + `phrase` search in `string` fields

## Fixed

* **Api**:
  * `/api/v1/db/.../list?all_versions=true`:
    * Remove duplicate entries from nested tables
    * Also fix some problems with sorting of nested objects
* Fix supervisor database statement not returning valid rows


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.143.0            sha256:e9ccacabbf14d2af78b8d6ce189e203597b74a4bd0cb04e8165e63c726b12386
docker.easydb.de/pf/elasticsearch:5.143.0  sha256:06d73caccf650d2de383970d17e7d17e8bee9dd8898d513e1e8cad0d7029dc84
docker.easydb.de/pf/fylr:5.143.0           sha256:d1aadee8563d7fe1db654427c3c04c83fedc30502bf847528a1ac09ef993edb0
docker.easydb.de/pf/postgresql-14:5.143.0  sha256:865abb0cdf238713a5c29b06ff508b9a247ff2147765c4f7ecc9b0e2a88b56b4
docker.easydb.de/pf/server-base:5.143.0    sha256:958ad3f2aebd879986c335b37ec41cc642061a7979eddea84c8d40516a62e902
docker.easydb.de/pf/webfrontend:5.143.0    sha256:476d01e9f1ba33207dcff9eb562c469d83cb3b379d62f187f421e311cb551403
```
