---
menu:
  main:
    name: "5.150 (November 2025)"
    identifier: "5.150"
    parent: "releases"
    weight: -650
---

> This version **does not require** a new index build


# Version 5.150.0

*Released on 2025-11-26*


# Webfrontend

## Fixed

* **Shared Collection:**
  * Fixed a bug that occurred when attempting to transfer an object from one collection to another while using the quick-access search filter
  * **Pagination:** Fixed a bug where pagination in shared collections stopped working after using the quick-access search filter
* **Unknown Custom Mask Splitters:**
  * Improved the app’s behaviour when a mask splitter fails to initialise correctly, which typically happens if the plugin is disabled or crashes
  * Previously the frontend displayed an error and did not show the object detail
  * Now the object detail will be shown and a placeholder mask splitter will be used to replace the failing one
* **Table View:**
  * Fixed an issue that caused random errors to appear in the Table View when the frontend received an object-updated event


# Server

## Fixed

* **API**:
  * Added safety checks in `api/v1/db` with `?all_versions`
  * Before, in some rare corner cases, internal server errors could happen


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.150.0            sha256:9e02793739b8cefc199d72e023bf066413db7a7fd662ad0120298b52d4c0b528
docker.easydb.de/pf/elasticsearch:5.150.0  sha256:d05abf7bd45390c1cd707ec9008c912a47bb944a92c8ddbf3ff2cc40509f5028
docker.easydb.de/pf/fylr:5.150.0           sha256:9516b9c4a51fac32f968e34b18d1adc53846c2ff070a946a536729c7f3757f64
docker.easydb.de/pf/postgresql-14:5.150.0  sha256:62db7a5ed433a817426c49931168a0018954402fb3d3c450a59d921bc7f13416
docker.easydb.de/pf/server-base:5.150.0    sha256:4938a03a78d703c007c24a13f18204c3495d75858ecc6ca888916dc96d9da177
docker.easydb.de/pf/webfrontend:5.150.0    sha256:9a45d916bf9b71d66ca256a06474f6bd8c833dc8da9f03a2f5ce68e72711235a
```
