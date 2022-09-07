---
menu:
  main:
    name: "5.105 (Late August 2022)"
    identifier: "5.105"
    parent: "releases"
    weight: -605
---

> This version **does not require** a new index build

# Version 5.105.1

*Released on 07.09.2022*

# Webfrontend

## Fixed

* **PDF Creator**: fixed form layout
* **Common**: Localization updated

# Version 5.105.0

*Released on 31.08.2022*


# Webfrontend

## New

* **Record History**: deleted pools in older object versions are displayed as *"Without Pool"*

## Improved

* frontend can now parse date time values in `"YYYY-MM-DDTHH:mm:ss.SSSSZ"` format

## Fixed

* **Search**: Fixed a bug when getting the data for the filter panel in a saved search
* **Print Manager**: Fixed a bug with the pulldown of the PDF templates on the print manager window
* Fixed a problem with Custom Field Renderer rendering empty mask splitters


# Server

## New

* **Janitor**: in the basic configuration, the janitor can be configured to delete *all* events after a certain time

## Improved

* **Custom Data Types**:
  * added compatibility for custom data types from plugins
  * fixes problems with custom datatype plugins that were changed from `base` to `extension` plugins
* **Rights Management**: for objects with reverse linked objects, the rights on the main object are used for all reverse linked objects as well

## Fixed

* **Record History**: if a pool from an older object version was deleted, do not throw an error but return `null` to mark the pool as deleted


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:c148459d9c44b1862f54dabe6d5c9548e3a22871640be42558b5a3bf5696c162
docker.easydb.de/pf/eas                  sha256:7f197576091088a8876d39021b97a05e175c8d6908c5faa233045de2a37fe81f
docker.easydb.de/pf/elasticsearch        sha256:8c60a124e33167925eb772d277df818786af7a2a6479ae4c0e35cce45a1fa6a0
docker.easydb.de/pf/fylr                 sha256:6106612af4eaeff6311fad03708e61745a52e21aaccc9ea557ea8d49601bb774
docker.easydb.de/pf/postgresql-11        sha256:ec0d1d09dfff4bb3f4dd659e8ef7b8e4c66d72f6414283a9b824cc8bbfcc2458
docker.easydb.de/pf/postgresql-14        sha256:e807fe051782b693d970bc5938a78a896a6d042efc82e0ba08af6a9ce3f4d719
docker.easydb.de/pf/server-base          sha256:0c3b748d4448ca5cf5b1e46640a0407cd46546e2cc1e7a667b2513706a53b249
docker.easydb.de/pf/webfrontend          sha256:7162acc548112c4af762db5377130672c412c791e8e60414b842f0d556bc054d
```
