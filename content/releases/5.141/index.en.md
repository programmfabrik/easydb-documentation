---
menu:
  main:
    name: "5.141 (February 2025)"
    identifier: "5.141"
    parent: "releases"
    weight: -641
---

> This version **does not require** a new index build

# Version 5.141.0

*Released on 2025-02-26*


# Webfrontend

## New

* **Add Collection to Search Tool**:
  * Added a new tool to append the collection query search to the end of the search input, instead of overriding the entire search input
  * This allows users to combine collection queries with other query elements

## Improved

* **Search Autocomplete Suggestions**: Improved the autocomplete speed in the search input to enhance the user experience
* **Main Search and Deep Links**:
  * Improved the execution order when a deep link is present in the URL in the main search
  * Now, the deep link search runs within the main search, saving resources and enhancing the startup flow
* **Search Reset Tool**: The reset button now also resets the Search Type Selector Manager, enabling all options in the Resources panel
* **CSV Importer**:
  * Added a warning text for numbers that will be converted from decimal formats to integers in the CSV importer
  * This warning is included in the corresponding `warning_text` column during import preparation

## Fixed

* **Collection Properties**: Fixed an issue that prevented the correct display of a collection's properties if the instance had an object type without masks
* **Read-Only Mode**: Fixed the read-only message display in read-only mode
* **Detail Sidebar**: Fixed a bug where the detail sidebar was opened without a `global_object_id` after the server informed the frontend that the user lacks permission to create an object
* **Search Tokens**: Fixed a bug where exact token suggestions were not clickable
* **Search Input**:
  * Fixed a bug where the search input became unusable after an empty call was made
  * The placeholder token was not re-added after the empty call, preventing user input
* **Autocomplete in Search Input**:
  * Fixed the cleanup of items when the autocomplete popup is displayed
  * Previously, results from prior searches lingered for a few milliseconds, making the UI less fluid when loading new results
* **Metadata Mapping**:
  * Fixed a bug that caused the "Deep Link URL" tag to be added in easydb, which is only supported in fylr
  * Fixed a bug where the copy button for metadata fields was activated for all fields (this button should only be enabled for custom metadata fields)
* **Page Viewer**: Fixed an error in the paged viewer
* **Editor Templates**: Fixed a bug when merging editor templates in a record with linked objects created by metadata mapping
* **Default Tags in New Editor**: Default tags are now properly set in `dbinfo` when creating a new object in the editor
* **CSV Importer**:
  * Fixed support for zero values when importing numbers in the CSV importer
  * Fixed an issue that prevented finding all parent objects in an import with more than 100 objects


# Server

## Improved

* `api/v1/db/*?all_versions=1`: don't output IDs of assets in historic versions which have been deleted

## Fixed

* **Bidirectional Links**:
  * Fixed problems with automatic updates of bidirectional links
  * Automatic cache invalidation and dirty queueing after changes in bidirectional links


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.141.0            sha256:22d2742af819a4498f9d2658ca62b6737d2ed6fd504e65c5504b8a46cd6b0484
docker.easydb.de/pf/elasticsearch:5.141.0  sha256:697c8aea400507f242d9137935414591e288d93b42eb2c4144a32347958bf3e9
docker.easydb.de/pf/fylr:5.141.0           sha256:21d450138f3745d41cbda05ab256c4af6bdf50deeaaaa273ad11fec018e3d377
docker.easydb.de/pf/postgresql-14:5.141.0  sha256:24df38ec98ac77d0d38cd4ab87e57f0255b276215e5f867e9eaefde1919e0b40
docker.easydb.de/pf/server-base:5.141.0    sha256:4dbe5876b158024958c4c6285d5e3deca3d52fa20a1ef4a97683adfa5d834b5a
docker.easydb.de/pf/webfrontend:5.141.0    sha256:4375ebaa7603accdb2c138c64b99d7abb4278e77191c6c8c30b5890dae828bc7
```
