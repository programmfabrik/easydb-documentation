---
menu:
  main:
    name: "5.120 (Early August 2023)"
    identifier: "5.120"
    parent: "releases"
    weight: -620
---

> This version **does not require** a new index build


# Version 5.120.0

*Released on 2023-08-02*


# Webfrontend

## New

* **Editor**: It is now possible to open the full screen editor of a record directly from the search using the shortcut `alt + double click` or `cmd + double click`

## Improved

* Improvements have been made at the start of the application to improve performance
* If you access the application through a pool deep link, the welcome message will not be displayed
* Improved behavior when deleting objects in the List Panel
* **Collection Sharing**: The user and group selector in the share panel has been improved. If users have an email adress assigned, it will be displayed in the selector to facilitate user selection
* **Event Manager**:
  * Improved the detail panel
  * A button has been added to reset the search filters
* Improved and corrected the EAS selector in the ACL configuration panels

## Fixed

* Fixed a bug where the mutilanguage column could not be edited with an empty value in the group editor
* **Event Manager**: Fixed a bug when trying to delete all events from the list
* Fixed a bug that did not allow downloading the original assets in EAS fields from the base config
* Fixed a bug when using the metadata mapping to add new elements to a nested object that already contained elements


# Server

## New

* **Plugin loader**: allow putting the configuration file `manifest.yml` in `build`` folder

## Improved

* **`/api/v1/db`** with `all_versions` enabled:
  * all linked objects in history versions have a `_system_object_id`
  * skip stray nested entries
* **Metadata Mapping**:
  * enabled list mode for `XMP-iptcCore:Scene` tag
  * `api/xmlmapping/mapping/<name>`: return mapping `id` as int


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.120.0         sha256:713e13856c004ab026c8e7258dfd6a299b67ed1b57650b88488f5c47c64af6d5
docker.easydb.de/pf/eas:5.120.0            sha256:c02b34ea47f8f1fa43b042ad760f3f85667aafb10d03369f8b02de0df071423a
docker.easydb.de/pf/elasticsearch:5.120.0  sha256:73b11a4096079138a39fe92e1967c5f6b6e00c982e20cb54da34bc7727b6586c
docker.easydb.de/pf/fylr:5.120.0           sha256:babab810fab1a09d712cd97497b587f974073f3889ad263a90c37c815c767c60
docker.easydb.de/pf/postgresql-14:5.120.0  sha256:7bc2f9c717adfa1a25e8efb08936b245c6bbb70bca3105b3ea023447a62e7487
docker.easydb.de/pf/server-base:5.120.0    sha256:223c3f758a437043a93e70e7342b06fb06e7274bae4c46e31bf3c90f38a7dcb0
docker.easydb.de/pf/webfrontend:5.120.0    sha256:ff62fe50677be30fef2041f5b25d62f2039c9596294def4971ba5537636ba8d0
```
