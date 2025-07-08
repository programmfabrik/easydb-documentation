---
menu:
  main:
    name: "5.145 (End of June 2025)"
    identifier: "5.145"
    parent: "releases"
    weight: -645
---

> This version **does not require** a new index build

# Version 5.145.2

*Released on 2025-07-08*

# Server

## Fixed

* fixed error parsing external, non-standard cookies
* removed wrong warning when sorting nested objects

# Version 5.145.1

*Released on 2025-06-26*

# Server

## Fixed

* fixed an error on upgrade to 5.145 when database is incomplete

# Version 5.145.0

*Released on 2025-06-25*


# Server

## Improved

* **Download of Files**: updated the internal export behavior to allow the download of a specific file version

## Fixed

* `api/v1/db` with `all_versions=true`:
  * fixed the order of elements in nested tables
  * in history versions of records, the order was not defined and not stable
  * now the elements are returned in the order of the old version


# Webfrontend

## Fixed

* **Detail Sidebar**: Corrected an issue where the correct object mask was not applied, causing an incorrect mask to be displayed
* **Save Preferences**:
  * Fixed a bug that disabled the `savePrefs` method when a user-session preference request failed
  * This affected the correct behavior of the registration form for users
* **Filter Manager**: Resolved an error triggered when the Filter Manager received a request without aggregations


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.145.0            sha256:fa31b022f424f3ac9733f1fbd3a4f4526addd4580b7333190b1f3c2c7a0bbd4d
docker.easydb.de/pf/elasticsearch:5.145.0  sha256:833dbbdf2056989c4ebb78e4f64762802dc85b5400705bc32d6d5c301b6f41fd
docker.easydb.de/pf/fylr:5.145.0           sha256:b6389af0155a070870340206353d21a65314086f845ff02571daa21a4439534a
docker.easydb.de/pf/postgresql-14:5.145.0  sha256:1251dc9510977ec5b80d70d306ec7287c70e63f9af0677551ff2e012b46010da
docker.easydb.de/pf/server-base:5.145.2    sha256:586011aa5e08c4208540ee402074f00bd06c252b60ac540ff62dbcd66a3e9267
docker.easydb.de/pf/webfrontend:5.145.2    sha256:5c1fd30e682f18922a9eafff4660b9e4e0fbc52d14b17bbcd3ce08ec6475c673
```
