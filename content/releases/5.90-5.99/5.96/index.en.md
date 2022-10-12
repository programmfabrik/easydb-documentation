---
menu:
  main:
    name: "5.96 (February 2022)"
    identifier: "5.96"
    parent: "releases599"
    weight: -596
---

> This version **does not require a new index build**

# Version 5.96.1

*Released on 25.02.2022*

## Webfrontend

### Fixed
* **Export manager**: avoid invalid aggregation
* **Login**: fix error for cases where anonymous search was allowed

# Version 5.96.0

*Released on 23.02.2022*

## Webfrontend

### Improved
* **filter**: tooltips showing long field names
* **filter**: aggregation and search uses the same fields, result sizes match now
* **search result**: optimized behaviour of focus and selection

### Fixed
* **objecttype settings**: fixed JS error
* **upload**: fixed linking of assets in cascaded nested fields
* **lists**: fixed error when an invalid limit was set
* **expert search**: fixed badges for boolean values
* **JSON importer**: error with lookups fixed
* **session**: language selection on first start fixed
* **filter**: missing year 2020 for date aggregations added
* **editor**: "save" button keeps active on errors saving an object

## Server

### New
* subfield `.from_to` added for daterange search and aggregation
* collection of assets to delete activated by default again (not yet finally deleted)

### Fixed
* fixed check of system rights, parameter values might be passed by non-root users now, too.
* fixed aggregation of date fields

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:92a28b8e623b2ccea6a5432187bb456840dd4daa53b5157dc935840063a48f2d
docker.easydb.de/pf/eas                  sha256:57347ba2a6424f833134f6a9e4f45629cf0e84a68c93ed6a7ae819f04bb3344e
docker.easydb.de/pf/elasticsearch        sha256:ab52585539b6da9746161316c9fbd01eb14b6b5fa5fa9a47d367df63d09763b0
docker.easydb.de/pf/fylr                 sha256:29d8bef5582ec5e2252af7e6537046e152eb1f672e7b1c7c93bb66216f038952
docker.easydb.de/pf/postgresql-11        sha256:2199d9e062db47ba58b3dcf11d65f605cfc47f278c9853e392f076e76a392f2a
docker.easydb.de/pf/server-base          sha256:453cf50e1e287a67ee65c01377cf7ab65135b8e4fd8be321733687460e4a4ef6
docker.easydb.de/pf/webfrontend          sha256:3ac74bf18ab5fde753261cb2e990f8c2f9d0c5439cf26af907dbd7027a9f3a52
```
