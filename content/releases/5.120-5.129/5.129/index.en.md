---
menu:
  main:
    name: "5.129 (End of February 2024)"
    identifier: "5.129"
    parent: "releases5120"
    weight: -629
---

> This version **does not require** a new index build

# Version 5.129.2

*Released on 2024-03-07*

# Webfrontend

## Fixed

* **Editor**: fix a bug when trying to render the asset browser on editors that dont have a place for it like editor popover

# Version 5.129.1

*Released on 2024-03-05*

# Webfrontend

## Fixed

* **Search**: error with hierarchy button fixed, function extended and made available in lists

# Version 5.129.0

*Released on 2024-02-28*

# Webfrontend

## Improved

* **Search**: button "Top Level Only" replaces the "Flat Hierarchy" option
* **CSV importer**: status panel moved to its own tab
* **Detail**: linked objects in dropdown are dynamically loaded when missing, starting with max. 100 items

## Fixed

* **Search**: fixed bug triggering search on when typing after a query tag was deleted
* **Common**: multi-input fields (e.g. in datamodel editor) had an issue when application language was changed
* **Group edit**: bug fixed when object was already open in editor sidebar
* **Text view**: fix improper rendering
* **Collections**: fix "compare view"
* **Detail**: fix reset of hierarchy lists on selection
* **History**: fix display of boolean values, were always shown as deleted
* **Rights**: asset version names in rights like in other places

# Server

## New

* new parameter `changelog_with_user` in `frontend_features` system right

## Improved

* URL added to `ASSET_DOWNLOAD` events

## Fixed

* cleanup of empty lists and rights for `link`/`unlink`, when a pool was removed
* correct error, when a pool ID is missing in import process

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.129.0         sha256:d98c3c3e94d030d653d7a423565fe44484e1857a4f6a85e58b9730cd31c8b92c
docker.easydb.de/pf/eas:5.129.0            sha256:896e8eac41e75633625c1e1fe5fc5fe9183c09f8b097a46b253ccb47d2e2bf8c
docker.easydb.de/pf/elasticsearch:5.129.0  sha256:f1be13d659b310d39737f42a0d83c1b7284333f58a01731cf773906bca819a6e
docker.easydb.de/pf/fylr:5.129.0           sha256:d7bf98ef34ab8f596ab38221e2a01c2e4d0b732068e2ec7b09d527f512961722
docker.easydb.de/pf/postgresql-14:5.129.0  sha256:6ac8581884e16aa4b48ef9af07e050da0eb7e256409e9aa5c96aaac154093db4
docker.easydb.de/pf/server-base:5.129.2    sha256:5e2b036bc06a2b5cb7009a2d830a19e60496a20c88940ba50a7fc157f9c877b8
docker.easydb.de/pf/webfrontend:5.129.2    sha256:9d150b4bd1df77ef04d33178761ffbb429248117ae03a908c2a50a9006be4831
```
