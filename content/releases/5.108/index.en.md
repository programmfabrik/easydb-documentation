---
menu:
  main:
    name: "5.108 (early November 2022)"
    identifier: "5.108"
    parent: "releases"
    weight: -608
---

> Versions of video assets will be recalculated with this version. This also requires reindex of a part of the objects. It happens in background, but may affect the performance of the application.

# Version 5.108.1

*Released on 03.11.2022*

# Webfrontend

## Fixed

* fixed download

# Version 5.108.0

*Released on 02.11.2022*

# Webfrontend

## New

* **Messages**: pool filter for messages before download

## Improved

* **PDF creator**: display progress while creating PDF

## Fixed

* **Metadata mapping**: fixed error when filter was used
* **Metadata mapping**: removed mapping of fixed values as target for import mapping
* **Metadata mapping**: remove duplicate tag info
* **Print search results**: remove hard-coded limit for maximum number of printable objects, adhere to configuration
* **User image**: placeholder icon when there is no image
* **Detail**: asset browser visible for anonymous users by default
* **CSV import**: fixed problem with empty pool field
* **Fullscreen view**: fixed detail button

# Server

## New

* Option `tokens_dont_split_query` for `/api/suggest

## Improved

* **Video assets**: rebuild video versions with higher bit rates to improve quality

## Fixed

* **XML mapping**: allow usage of fields not searchable in export mapping


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:58463979ca8515e6cb156d8b96dbaec67930edcbe8143ab69345dafe8f03d4cd
docker.easydb.de/pf/eas                  sha256:df5946ca633ffe4ecd890de077b1814009f32fa41d5f62637dad20495009cfec
docker.easydb.de/pf/elasticsearch        sha256:69bd37e20ee4a588e95c037071d6cf99e6cb3eec5f42d96a047b28116a18aab9
docker.easydb.de/pf/fylr                 sha256:744b61cdeab8b9d2158089ef4da234bf076a10e523b654318fb233d7258bda68
docker.easydb.de/pf/postgresql-11        sha256:1aeb133fff1848b498c5e6887629bac088fec0aef318fbee2d278a0d90af2830
docker.easydb.de/pf/postgresql-14        sha256:174855604dc22ef42c2baed8f18872392d5c599d95ad3b6709dbed5e28fbbf8e
docker.easydb.de/pf/server-base          sha256:06932d49cd4547c64732bbc255e3f0ea7410d6c6f6fa9f22d0e55f5a3d80dbae
docker.easydb.de/pf/webfrontend          sha256:9614e04f9097795ae3783217cbb9e5681f62389ced3a19263b5a114a794b32b2
```
