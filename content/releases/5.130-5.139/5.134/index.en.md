---
menu:
  main:
    name: "5.134 (June 2024)"
    identifier: "5.134"
    parent: "releases5130"
    weight: -634
---

> This version **does not require** a new index build

# Version 5.134.1

*Released on 2024-07-05*

# Webfrontend

## Fixed

* **Search**: Fixed sorting by changelog

# Server

## Fixed

* **Easydb Asset Server (EAS)**: Fixed encoding of filenames in Redirect-URLs to the EAS


# Version 5.134.0

*Released on 2024-06-19*

# Webfrontend

## Improved

* **Filter**: Combination of several values with `AND` or `OR`, selectable in the filter view
* **Asset browser**: `vector2d` preview enabled in the zoomer
* **Main search**: Added menu item to cancel the selection
* **CSV Importer**: Mapping multiple columns to populate the same nested table enabled
* **List popover**: Hierarchy mode selection enabled

## Fixed

* **Table view**: Update behavior for events corrected
* **CSV Importer**: Assignment of numerical data for nested tables corrected
* **CSV Importer**: Position of empty rows when importing nested entries with index corrected
* **CSV-Importer**: Search for linked objects corrected if more than one identifier was specified
* **Tags**: Display of available tags corrected
* **Filepicker plugins**: removed empty error if the CMS does not return a response if the request is successful
* **Editor**: Display of placeholders for date range columns corrected
* **Search**: Sorting by changelog fixed
* **List popover**: Opening the entire tree when loading prevented

# Server

## Fixed

* **EAS**: Display of embedded graphics in WebDVD preview images corrected
* **Rights management**: Use of tag filters when assigning `link`/`unlink` to pools fixed

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.134.0         sha256:e0a7ba0e456deddaf7f6e3d2f45d541729372584b5cad3ff52bf0ccf849e7767
docker.easydb.de/pf/eas:5.134.0            sha256:6c7a82834b8a0de3817df864d20346a9e47e4a9a52a0d6ea4c3fc0690d944bc7
docker.easydb.de/pf/elasticsearch:5.134.0  sha256:69b78bf26196f74011c5b5cd4a3415a1f8a5e33b758829fa60570a27a3581831
docker.easydb.de/pf/fylr:5.134.0           sha256:36964511e3a522a1d59a375d52f073dffbef1333687077065dd063a7d6f16fc6
docker.easydb.de/pf/postgresql-14:5.134.0  sha256:d705d451b0ffb5b6f6cf2f3bc11ae862df1f6c82c098c8aba684d9211e7f969d
docker.easydb.de/pf/server-base:5.134.1    sha256:30000ecb75b5a5526de24e079212f1a7a65044693a4030b26b8d7027d8abb904
docker.easydb.de/pf/webfrontend:5.134.1    sha256:46ef361d1aede63c96239127733d88b8173d6790009f37297fe98ea4fd60d999
```
