---
menu:
  main:
    name: "5.139 (December 2024)"
    identifier: "5.139"
    parent: "releases"
    weight: -639
---

> This version **does not require** a new index build

# Version 5.139.1

*Released on 2025-01-10*

# Webfrontend

## Fixed

* **detail map plugin**: fixed a JS error preventing opening the detail view

# Version 5.139.0

*Released on 2024-12-11*


# Webfrontend

## New

* **Date Columns**: Added a new "Avoid B.C. / A.C. conversion" mask option for date columns
  * This disables the automatic conversion of dates to BC format, providing greater flexibility in date handling

## Improved

* **Standard View**:
  * Improved HTML elements to support the HTML `"title"` attribute, enabling tooltips that display full values
* **Linked Objects**:
  * Linked object fields in the editor now refresh automatically when another field referencing the same object updates its data
  * This ensures all related fields remain up-to-date
* **Collection Manager**:
  * Reactivated event listeners for visible collections
  * This enables the frontend to automatically update when a collection is edited in another session
* **User / Group Selector**:
  * Increased the number of objects requested when displaying groups and users
  * This is to address limitations experienced in larger environments
* **Mask Editor** & **Configuration Panel**:
  * Ensured that default custom settings remain visible for custom data types without `manifest.yml` configurations
  * The settings button is always accessible, allowing users to access default settings without explicit configuration

## Fixed

* Fixed the download helper method to correctly apply the specified file name
  * Previously, the helper ignored the defined download name property, defaulting to the browser’s behavior
  * Now, the file downloads with the user-specified name
* **Reverse Linked Tables**:
  * Corrected issues when updating reverse linked fields that are simultaneously open and edited in another editor
  * Changes now propagate correctly, ensuring data consistency
* **Scheduler Editor**: Resolved a bug preventing the display of `weekdays` and `days_of_the_week` inputs
* **User Manager**: Fixed an issue where deactivating all visible columns caused the user list to fail to render and disrupted user search functionality
* **Decimal Fields**: Corrected range validation hints for decimal fields to provide accurate guidance
* **User Templates**: Fixed an issue preventing proper persistence of changes in editor user templates


# Server

## New

* New optional URL parameter for `/api/event/list`:
  * `skip_count` (boolean): when set, `"total"` count is not present in output
  * Can improve performance for large event lists

## Improved

* **Easydb Asset Server** (EAS):
  * `rput` endpoint has improved status code handling when loading files from URL
  * HTTP status is reflected in the (error) status of the file
* Improved performance of `/api/db?all_versions`


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.139.0            sha256:444f97c0f781f1ad96a1df2e929a34aa993d143898a9deba08e0548760d68678
docker.easydb.de/pf/elasticsearch:5.139.0  sha256:225b72c92d11646811353ba4961b44ea81b948715ee799cd58d89cd582ccf613
docker.easydb.de/pf/fylr:5.139.1           sha256:63a841187de0022be6e642b62695d61ba9b0894b2885e337e807ef7420d49f9e
docker.easydb.de/pf/postgresql-14:5.139.0  sha256:47cfa219dc0935685ed5626ee70c5ed95fffe31e31ebed729fc71fd9000759c0
docker.easydb.de/pf/server-base:5.139.1    sha256:b652df495f4703121e0c51b1931ea51a6a32fdac7fdbf6412428dce1e63bf72e
docker.easydb.de/pf/webfrontend:5.139.1    sha256:6618d7a291c9d280f0a171a8278c56fc62f6e109e0341e1277e2fae6facc9dda
```
