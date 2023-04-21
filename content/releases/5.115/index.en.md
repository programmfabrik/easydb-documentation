---
menu:
  main:
    name: "5.115 (Mid April 2023)"
    identifier: "5.115"
    parent: "releases"
    weight: -615
---


> This version **does not require** a new index build


# Version 5.115.0

*Released on 19.04.2023*


# Webfrontend

The webfrontend now uses NodeJS in at least version 16

## Improved

* **Search**:
  * Enhanced filters for date fields
* **Objects with missing standard**:
  * Enhance search popover for missing eas standard
  * Enhance preview of objects without standard
* If no configured language is available, a fallback language is used

## Fixed

* Fixed error in the fullscreen view of collection details
* Fixed drag and drop behavior of files/assets in the editor
* Fixed errors in the weblink custom datatype (plugin) for links containing `#` and `?` parameters
* Fixed problems in the group editor with more than 100 objects
* Fixed errors with field rights
* Fixed errors in expert search
* Fixed problems with mask splitters and nested table with no visible children


# Server

## New

* **XML Export**:
  * top level fields `_id`, `_system_object_id`, `_version` are now optional

## Improved

* For transitions which revoke permissions: improved handling of confirmation codes and policy in the api


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.115.0         sha256:0dec1b427f6d420c3793e8f0d6a2952d9e82f026f20d9cf7332aa40933363630
docker.easydb.de/pf/eas:5.115.0            sha256:6ecfd1750ec0319a64c197a4849329bdb3809a9a54d6ec287074fa4b9bd67d65
docker.easydb.de/pf/elasticsearch:5.115.0  sha256:576e7ae7f45f2eabd18a88a24cb5b49314c4289c4e23bacc53eb7f8f5058306c
docker.easydb.de/pf/fylr:5.115.0           sha256:88e88dbc881b5f7145c981b8daccb640feb6c2bada70597121306867048f72e0
docker.easydb.de/pf/postgresql-11:5.115.0  sha256:86d2ea1d89d245a77017bce8f3c454dc3cd36bb80a5e0f00e4231d3d8f61725c
docker.easydb.de/pf/postgresql-14:5.115.0  sha256:726f3ca5e83fcb75f98c97c90d1102d5b1795c3c60320427c03e217804f1af47
docker.easydb.de/pf/server-base:5.115.0    sha256:470040311fe0ffce2a82260884baf8cc2d9553578fb139eba4ec2ce8d3b2ca78
docker.easydb.de/pf/webfrontend:5.115.0    sha256:62f5f24dd405bc41e8869e4abcaa81fa46c691a1186fea05637447e9b25dbad5
```
