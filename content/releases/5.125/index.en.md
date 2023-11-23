---
menu:
  main:
    name: "5.125 (End of November 2023)"
    identifier: "5.125"
    parent: "releases"
    weight: -625
---

> This version **does not require** a new index build

# Version 5.125.0

*Released on 2023-11-22*


# Webfrontend

## New

* **Quick View**: Asset browser available when viewing linked objects
* **Asset browser**: animated GIFs can be played

## Improved

* **PDF print**: Change history can optionally be displayed at the bottom of the page
* **Data model editor**: improved error handling when using the object store
* **CSV Importer**: Check for non-existent parent objects
* **Full screen view**: when changing the object, the selection in the main search is updated accordingly
* **Mask editor**: various improvements
* **Standard view**: more suitable asset version is used

## Fixed

* **Main search**: Corrections for the filter bar
* **Shared search**: all parameters are transmitted via URL
* **JSON importer**: Fixed bug when using ID lookups in objects with URL assets
* **Full screen view**: Multimedia playback did not stop correctly when object was changed

# Server

## Fixed

* Fixed aspect ratio for rotated video versions
* Fixed loading of images with undefined resolution

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.125.0         sha256:c9edf7be3cf068ce9558344ab6efdc7d9e6f65647cdfa99832b309909348c225
docker.easydb.de/pf/eas:5.125.0            sha256:108dd4864af5cfd32f5dee4ffef044f1363bd8db208a0782de7ab8e9dc4a1ce3
docker.easydb.de/pf/elasticsearch:5.125.0  sha256:f34eb6e02820efbf9db5a175d080a200a536307349f4a6a411cefcc79b7a1b08
docker.easydb.de/pf/fylr:5.125.0           sha256:0576800ac4b9f8fcd69a627d87ed34252e03ba3851e9eda24d22bf2aab158df3
docker.easydb.de/pf/postgresql-14:5.125.0  sha256:b7f6984ce0ae1ae85bfa5af2063086a4308a9ec119ddb988d646432442f31dfd
docker.easydb.de/pf/server-base:5.125.0    sha256:59b1e9df7b1abcbbf5bf2c33934c4026791c27cdfe20ec5d276e450b053cc015
docker.easydb.de/pf/webfrontend:5.125.0    sha256:7f95b7ba14c5e9881b2fd56ec630798c8de52897273ebf2feb196ff75f7f71e6
```
