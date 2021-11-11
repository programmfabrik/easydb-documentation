---
menu:
  main:
    name: "5.92 (November 2021)"
    identifier: "5.92"
    parent: "releases"
    weight: -592
---

> This version **does not require a new index build**, the new Elastic image works with the existing index files.

# Version 5.92.0

*Released on 10.11.2021*

## Web frontend

### New

* Share button for asset versions

### Improved

* Quick access: multiline view for grouped object lists
* CSV import: show name of uploaded mapping file
* `_all_fields` mask definitions only loaded if required
* remove redundant display of system IDs in print view

### Fixed

* fixed Javascript error on unexpected server response
* fixed nested manual sorting
* CSV import: fix for default tags
* CSV import: fix for missing/invalid mapping
* don't show objecttypes of connector instances in rights manager
* Hotfolder: don't send invalid mapping configuration
* fixed deeplink to messages

## Server

### New

* support `webp` image format
* new localization support for swedish (`sv-SE`)

### Improved

* improve error handling for linked object import
* no special casing of sort field in `fields` response

### Fixed

* build SHA224 sum when importing asset with `rput`
* compute missing SHA224 sums for existing assets
* prevent invalid triggers when changing column types

# Checksums

Here are the checksums of our Docker images (latest version): 

```ini
docker.easydb.de/pf/chrome               sha256:29b9cbc9d8a53a263b2f995588fffe323cafad67d70307f92d51c8eedda4da7a
docker.easydb.de/pf/eas                  sha256:0078e914d8a9ec4cfae6e813c61c3d746974b835bf9a154b0fda77f116b97e9e
docker.easydb.de/pf/elasticsearch        sha256:db2b1a10642527d6f319356552aa7d63e69ea086dc8b6f61a25455462acab201
docker.easydb.de/pf/fylr                 sha256:879881269be708e8f1d0d4a274ba83f21a5cd4adcc10abae098f0340a816f514
docker.easydb.de/pf/postgresql-11        sha256:47e9c630cbca425e43cf00c6a0bc17831bf152811f7f3963dcfd1ed84620f4e6
docker.easydb.de/pf/server-base          sha256:0ad1bc46eb4f779f493b6c91c2277727cc0ec0910b1e816eccae63dcdb501f9e
docker.easydb.de/pf/webfrontend          sha256:6be72be56ea5c16c4395a3e0fa6784e14ec2c4973285f98b0eaa221b1d093589
```
