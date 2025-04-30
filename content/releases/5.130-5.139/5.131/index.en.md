---
menu:
  main:
    name: "5.131 (April 2024)"
    identifier: "5.131"
    parent: "releases5130"
    weight: -631
---

> This version **does not require** a new index build

# Version 5.131.0

*Released on 2024-04-10*



# Webfrontend

## New

* **List view**: Filter Manager is now available in the lists.

## Improved

* **Filter Manager**: Message instead of blank page when no filters are available.
* **Asset Browser**: Name of the currently displayed asset variant is shown.
* **User configuration**: Customization of the necessary fields when configuring your own user.
* **System messages**: Usability improvements.

## Fixed

* **General**: numerous corrections in CSS.
* **Full screen view**: Selection of displayed asset variant corrected.
* **Pool selection**: Pools that are necessary for structuring but cannot be used are no longer displayed as selectable.
* **CSV Importer**: numerous corrections to the search for linked objects.
* **Mask editor**: Corrected display of the "Hide field name" option for nested fields.
* **Main search**: Fixed display in search after copying an object.
* **CSV Importer**: Fixed metadata mapping when using RPUT to upload an asset.
* **Filter sorting**: Sorting for custom type fields fixed.
* **Search**: Fixed behavior when double-clicking to edit a search tag.

# Server

## Improved

* **Webhooks**: server response is saved in `WEBHOOK_ERROR` events for diagnostics.

## Fixed

* **/api/objects**: better error which generates not error file on server, as it is done for unexpected errors.

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.131.0         sha256:c4c775d6986e532ec47076206c2d14d55e159bfe6014535fac1ccbe6a43d2963
docker.easydb.de/pf/eas:5.131.0            sha256:d2b08de3d9a65b7adfedd30ff4624c3cf7c3798144d59670fb554545fffb759c
docker.easydb.de/pf/elasticsearch:5.131.0  sha256:7274934dd0a1f827d3427f1305915ccdf7e5d84b5b647df60183f9e60747171e
docker.easydb.de/pf/fylr:5.131.0           sha256:1a18e12b4181a457bb1072f08a97a8029cb99afd04484a9109ab8f9eca3c1751
docker.easydb.de/pf/postgresql-14:5.131.0  sha256:eac1d8c752478c05aba4f599c42f42be48990df69c278d74456c1992a77a77da
docker.easydb.de/pf/server-base:5.131.0    sha256:0dafc1a150bc4493896d6d44b9334bae4172f16c959fdf39260d4246645cd702
docker.easydb.de/pf/webfrontend:5.131.0    sha256:a726e01fee390da4052033bd90caa819228337951c6fe56d40b71d9dfbe76e32
```
