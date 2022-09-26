---
menu:
  main:
    name: "5.106 (September 2022)"
    identifier: "5.106"
    parent: "releases"
    weight: -606
---

> This update requires a re-index, schedule appropriate downtime / update time

# Version 5.105.1

*Released on 26.09.2022*

# Webfrontend

## Fixed

* **Editor**: creating a new object was not possible for certain data models

# Version 5.105.0

*Released on 21.09.2022*

# Webfrontend

## New

* **Video player**: subtitle files can be uploaded and used

## Improved

* **Export**: Dialog option, whether to export linked objects

## Fixed

* **Login**: label of SSO button fixed
* **Duplicate check**: fixed text covered by image
* **Upload**: fixed JS error
* **Detail**: fixed error opening detail view
* **New records**: show selection of linked objects pool when required
* **CSV importer**: parsing error fixed
* **CSV importer**: fix possible recursion error when many fields were in use
* **Collection sharing**: preview used existing session, leading to undesired logout
* **Expert search**: fixed error when connector was used
* **Fullscreen view**: fixed error opening detail view
* **Upload**: fixed asset preview, e.g. for videos

# Server

## Fixed

* **Wildcard search**: tokens are combined with AND now like they are for other search modes
* **Preview generation**: fixed detection of assets which require updated previews
* **Export**: fixed saving of transport definition
* **Hotfolder**: Handling of pools for linked objects fixed

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:6cfaac8df2e341c2fbe0b49d5cd6020c15fa39ee93f36348141f07c20b342bd0
docker.easydb.de/pf/eas                  sha256:74830079a85b7d557af066dcc4b11d5b9fa3262f6361361b5f7c3d9988e4eaad
docker.easydb.de/pf/elasticsearch        sha256:e4a937ea817ee833388103a7fb14650fd2973e4e989e43979610629cd35187c7
docker.easydb.de/pf/fylr                 sha256:88c997a80224d6210f946bf78272237e066c4426221527aec7c249578c767ff3
docker.easydb.de/pf/postgresql-11        sha256:db10bb134cdb452d71368b7a21b8aba6329a81e3ad85b8493f552075d475e2be
docker.easydb.de/pf/postgresql-14        sha256:37c049a62eada24218f13ec760d4b48f686b793d89622464d18bfc48693b2185
docker.easydb.de/pf/server-base          sha256:66062632a3a0c0107f2f22e579990569c458360ef52ddfb3ad6cd3f09f4db032
docker.easydb.de/pf/webfrontend          sha256:b549449c08f27019b61c904e98a0dadfe0f1f9ab496b907a0173bf2d26d04081```
