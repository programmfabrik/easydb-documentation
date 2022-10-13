---
menu:
  main:
    name: "5.107 (October 2022)"
    identifier: "5.107"
    parent: "releases"
    weight: -607
---

> This update requires a re-index, schedule appropriate downtime / update time

# Version 5.107.0

*Released on 12.10.2022*

# Webfrontend

## New

* **CSV Import**: added support for reverse linked objects

## Fixed

* **User Manager**: the root user can't be deactivated anymore
* **PDF Creator**: do not include empty fields in the stored data, this drastically minimizes the data stored in the server
* **Connector**: bugfix when accessing a instance with anonynous access
* Drag and drop keywords allocator now updates the keyword counts
* Fixed design bug when changing language in language settings


# Server

## New

* **Standard Rendering**:
  * the depth of linked objects, that are included when the standard of an object is rendered can be limited
  * to enable limitting, set the server variable `debug/limited_standard_depth` to `true` (default is `false`, so there is no changed behavior for now)

## Improved

* **User Login**: users of types `anonymous`, `ldap` and `sso` can no longer log in with a password stored in easydb (e.g. if the account was previously configured with such a password and has changed account type in the meantime)
* **Asset Versions**: display name of the `full` version has been updated to "Original (formatted)"


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:4f3ec61075c605b674340179f4a2630be6ab903aa3f1ca6b7b54f00a15ee2f1c
docker.easydb.de/pf/eas                  sha256:b8a405baf379d185c93f32763cd8eee67246fd34f02847003f37aad8c60358e9
docker.easydb.de/pf/elasticsearch        sha256:60d4a819ab5311f6fa6d8d7c0a9e4a89eff7dad1d2e016d8a286370893bf51e6
docker.easydb.de/pf/fylr                 sha256:df80ddc7ea48cebeff89bd88b51c6da531bd1b0d5676f87c79b269cc9f586b9a
docker.easydb.de/pf/postgresql-11        sha256:95a52158929dd466bc6d2fd86c22c2ed17c2486005387bb79b80697a0650c170
docker.easydb.de/pf/postgresql-14        sha256:35aa4a484a832850e0d17e6ce6efcc3dc37e5d601102ac54db6edf77dd17c896
docker.easydb.de/pf/server-base          sha256:d62a82ed973537df46a735f155f186215f4d58bd00aa55ec6bacf2d93237d446
docker.easydb.de/pf/webfrontend          sha256:4609b8d8d52122d1a7be1c213640388bbafa78bd2b3eb72a7a83fcb1935015fe
```
