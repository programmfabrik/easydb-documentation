---
menu:
  main:
    name: "5.135 (July 2024)"
    identifier: "5.135"
    parent: "releases5130"
    weight: -635
---

> This version **does not require** a new index build

> The container `pf/chrome` is now obsolete and is not part of the release anymore. Its tasks are performed by the container `pf/fylr`.
>
> The old `pf/chrome` container image can be removed.


# Version 5.135.0

*Released on 2024-07-24*


# Webfrontend

## Improved

* **Search**:
  * Removed the "unset" option for the parent field in hierarchical objects in the expert search. To search for objects without a parent, the "Options" button can be used
  * Significantly improved the functionality of hierarchical list   results in the main search and list search
* Improved the interface of the sorting panel
* Enhanced the layout of the "More..." panel in search filters
* Improved the base type managers to persist the active tab when saving an element
  * This means that after saving, for example, a pool, the active tab on the screen will remain visible
* **Zoomer**:
  * Added new enhancements to the zoomer to avoid excessive server calls when zooming
  * These extra calls caused server blocking and slowed down the zoomer

## Fixed

* **CSV-Importer**: Corrected an error when attempting to use number fields as identifier fields to create linked objects
* Fixed an issue when sorting using the field change log
* Corrected a problem when sending empty values in the base config instead of default values
* Fixed a bug when using large BC dates in date range fields
* Corrected validations in daterange type fields
* Fixed bugs in the rights preset manager
* Fixed an issue when trying to copy object types that included fields configured as bidirectional
* Fixed a bug where the collection manager took too long to respond after adding a new collection


# Server

## Fixed

* **PDF Creator**: fixed creation of PDF files by using another container to do the job
* URL redirects to `/api/objects`: percent-encoding of filenames


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.135.0            sha256:7c497989191305d99c0da3dd2ef1bcf1a491c7e21c488a2a8c7985604b99dea1
docker.easydb.de/pf/elasticsearch:5.135.0  sha256:1d6640f903d68b06660b873186330f533171e59f67725c8dc5cd127c528317d9
docker.easydb.de/pf/fylr:5.135.0           sha256:2f5ada17c5d66875717dd218b7330f94450f15df5c87c54a74eb082058165012
docker.easydb.de/pf/postgresql-14:5.135.0  sha256:f8166da72c3cbcc17f972363c670ac7da80511639d0aaf0dc7857c6cfe006566
docker.easydb.de/pf/server-base:5.135.0    sha256:62e245851f52149f412e9bdcb144cd2d599c8aca503b00c3c2628f9800ebb9e2
docker.easydb.de/pf/webfrontend:5.135.0    sha256:110231137b690b25a944e8a65d156a7a45ba9240d1425b81a4dd2324b9fcc11c
```
