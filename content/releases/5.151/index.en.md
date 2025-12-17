---
menu:
  main:
    name: "5.151 (Dezember 2025)"
    identifier: "5.151"
    parent: "releases"
    weight: -651
---

> This version **does not require** a new index build


# Version 5.151.0

*Released on 2025-12-17*


# Webfrontend

## Fixed

* **TagFormManager**: Tag labels in tag forms now display in the **best available frontend language**. Previously, only the currently selected FE language was used, which caused some labels to appear empty.
* **Video Player**: Fixed a bug in variant value checks that could create a video player that was **not visible** in the frontend.
* **Filter Panel**: Fixed filter rendering for fields using **right management via tags** in the *ObjectType Manager*.
* **Table View**: Fixed an issue where the object hierarchy was not shown when the search had **only one Pool** selected. If the root object was not in that Pool, the table would not display any other objects. The frontend now renders the hierarchy correctly, and objects outside the search scope are shown in **grey**.

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.151.0            sha256:d55d9f62d0d4878b18a557d584a3df7b5f8b623ebc83938edea4988e4a35c845
docker.easydb.de/pf/elasticsearch:5.151.0  sha256:ec332d919c26e1c42ad04698df5cdb4bdab5f6e32669f75cea19ab39881316a1
docker.easydb.de/pf/fylr:5.151.0           sha256:f4f07c2266b647051ef7205d97045fafe0589adbf042212551dacc423398a005
docker.easydb.de/pf/postgresql-14:5.151.0  sha256:85ba93a993a95581e57f9984041356d06473520e9b753fcbfeaab2e567d5e78c
docker.easydb.de/pf/server-base:5.151.0    sha256:5d3d7a04984a59fe5761c7b25c21f88afa42ceede82a8710bfb27d9ebcc5ada5
docker.easydb.de/pf/webfrontend:5.151.0    sha256:45efd4c55a8c7241bc7c1c010d90824f0c8069b0a1c37b4643b73554406278eb
```
