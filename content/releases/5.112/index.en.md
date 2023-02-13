---
menu:
  main:
    name: "5.112 (February 2023)"
    identifier: "5.112"
    parent: "releases"
    weight: -612
---


> This version **does not require** a new index build

# Version 5.112.1

*Released on 13.02.2023*

# Webfrontend

## Fixed

* **Filter**: fixed labels
* **Download**: no Zip option for single-file downloads

# Version 5.112.0

*Released on 08.02.2023*

# Webfrontend

## New

* **Change History**: new option that highlights changes to the previous version.
* **Detail View**: Button in the asset browser that can be used to download the file currently being viewed.

## Improved

* **Input fields**: automatic detection of input direction
* **Detail View**: Disable all tools and plugins when change history is open.
* **CSV/JSON importer**: URLs with unencoded special characters can be imported.
* **Version details**: new indication if version contains a watermark
* **Data Model Editor**: use of Markdown without debug mode possible
* **Detail View**: some metadata fields hidden in short view

## Fixed

* System name from base configuration is used correctly
* Selection for linked pool only visible if linked objects with pools are available in the mask
* Method `getSiblingFromData` for plugins fixed

# Server

## New

* new data languages "Catalan" ("ca"), "Occitan" ("oc"), "Portuguese" ("pt") and "Ukrainian" ("uk")

## Improved

* `/api/v1/objecttype`: accelerated short format
* Input/output for `collection.create_object.linked_object_pools`.

## Fixed

* Pool watermark links in asset table are better maintained, cleanup errors thus avoided.
* Expiration time of uploaded assets is also set for `rput` and in base configuration

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.112.0         sha256:bc43f3e689458a0fd4f91d7ad7a828da76c586d8a7fb0d63b08b74bd07a133b5
docker.easydb.de/pf/eas:5.112.0            sha256:8a93a759ef2ad04ceb1821080a38855d7de95a90d5dad5c91537604fa4e530e3
docker.easydb.de/pf/elasticsearch:5.112.0  sha256:f5d982e8a5463ac58e9c03f0aa107cf3588dea33f5bfc2c7d52bd127f853d215
docker.easydb.de/pf/fylr:5.112.0           sha256:cdc2d2352c63b590c095668c92100c595e806be101c4f3afce842bbc67260bf1
docker.easydb.de/pf/postgresql-11:5.112.0  sha256:90025affc266723073046d5d0ffa9d856095034cb9476a2d01eacfcd87bd923b
docker.easydb.de/pf/postgresql-14:5.112.0  sha256:253c5a26cbf18729933d1fe357b93fd5180181f11fb0b70cf4c992f11b9412f7
docker.easydb.de/pf/server-base:5.112.1    sha256:476efcd6e3962585dd030fa7a35ab3a8eb0ddc2bdc4ec3a8edad32326b6bab56
docker.easydb.de/pf/webfrontend:5.112.1    sha256:b0b4f17b483552e7c407baad0aabe47994a1971cfeae50c65359237ba4e3cf2c
```

Translated with www.DeepL.com/Translator (free version)
