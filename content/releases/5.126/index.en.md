---
menu:
  main:
    name: "5.126 (December 2023)"
    identifier: "5.126"
    parent: "releases"
    weight: -626
---

> This version **does not require** a new index build

> A new feature in the Easydb Asset Server will trigger new version calculations which will temporarily cause more load

# Version 5.126.0

*Released on 2023-12-13*


# Webfrontend

## New

* **Editor**: Improved the behavior of nested fields configured as "Append only":
  * the rows that already existed in the table will be shown as read-only fields
  * only adding new fields will be allowed

## Improved

* **Design**: Numerous corrections and adjustments have been made in the CSS

## Fixed

* **Metadata Mapping Editor**: Corrected an issue where some tags were not displayed correctly
* Fixed a bug in the permission settings for shared collections
* Fixed an issue where the server parameter was sometimes erroneously included in URLs for sharing objects


# Server

## New

* **Easydb Asset Server**: new feature that allows access to files inside archives
  * it is now possible to access files inside archives by concatenating the `versions.directory.url` with the filenames
  * *this will trigger new version calculations which will temporarily cause more load in the Easydb Asset Server*

## Improved

* **Standard Rendering**: only render the first file in the `eas` part of the standard to reduce traffic and improve performance

## Fixed

* Fixed a bug in the self register process for new users


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.126.0         sha256:ab51d95640f8e0f608ed26015a30f19e5e25534d1224a972b8b381def9b99fdd
docker.easydb.de/pf/eas:5.126.0            sha256:1d572a161595ec5267fbe35a913cf4b229ec638084fbab17f1075d4bdc0289ab
docker.easydb.de/pf/elasticsearch:5.126.0  sha256:3092714720e3e3eca85106941aefc305152edc13e044383ecc6f99faf7b82664
docker.easydb.de/pf/fylr:5.126.0           sha256:db47b3a6ad0bef5e8d881006812a56974a133badcb041b5defd782e2b5c4ba0b
docker.easydb.de/pf/postgresql-14:5.126.0  sha256:c1d3b7882cdb4ea9a3293ae0d6bea21417e20ffc2e133f6274afeba72409e0c8
docker.easydb.de/pf/server-base:5.126.0    sha256:d4412665a021f9c51d58d12c50b70164190f6dc69a69e9cda2ecd8297a764aff
docker.easydb.de/pf/webfrontend:5.126.0    sha256:b69aba45095acf6941bd548ec33e1ce1d479eccd6e9da2edbf9484b5ce4c6f7f
```
