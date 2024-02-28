---
menu:
  main:
    name: "5.129 (End of February 2024)"
    identifier: "5.129"
    parent: "releases"
    weight: -629
---

> This version **does not require** a new index build

# Version 5.128.0

*Released on 2024-02-28* (not yet)

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
```
