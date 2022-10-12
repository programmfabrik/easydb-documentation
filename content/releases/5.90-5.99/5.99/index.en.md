---
menu:
  main:
    name: "5.99 (April 2022)"
    identifier: "5.99"
    parent: "releases599"
    weight: -599
---

> This version **does not require a new index build**

# Version 5.99.0

*Released on 27.04.2022*

## Webfrontend

### Improved

* **Table view**: fields of reverse linked objects are visible again
* **Common**: different dialog type for server questions
* **Datamodel editor**: marker for standard mask
* **Datamodel editor**: mask option to show system object ID of linked objects in text view

### Fixed

* **Group editor**: fix usage of templates
* **Editor**: don't set pool of reverse linked objects when main pool is changed
* **Search**: fix display of selected expert search
* **Filter**: fix count when multiple filters are selected
* **Search**: error at "without" search of boolean fields fixed
* **Editor**: create object template contains reverse linked fields (not in group editor)
* **Detail**: fixed error when subordinate objects are shown
* **Collection**: fixed error when multiple assets were uploaded at once

## Server

### New

* **Search**: search types `user` and `group` don't require additional system rights anymore
* **Common**: new language code `smi` (Sami)
* **Event polling**: `info` and `pollable` fields removed from `/api/v1/event/poll`

### Fixed

* **EAS**: fix missdetection of nxs/nxz files
* **Suggest**: fix highlighting
* **objects API**: file index check fixed
* **Search**: search type `acl` now always allows to view requesting user
* **Custom datatype updater**: ensure indexing of changed objects in case of errors

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:0937c04eb4377979bd6c88a53c8031677335b8dd00e5a374465f335b01410e3d
docker.easydb.de/pf/eas                  sha256:5ce17eabb860e340a1f7fe5fb3a9c5cc988ebd8916f4a794dd1ef160bcbd03e0
docker.easydb.de/pf/elasticsearch        sha256:c4fe3bd00d884cc8f9a03dedb924a18c65218a16f04b141cdcb0e1a39d699492
docker.easydb.de/pf/fylr                 sha256:3c62bdd33fdd3b6c2cfc339baf817ca989058eb4c2bc1401f2ecd9667c00734d
docker.easydb.de/pf/postgresql-11        sha256:1bc3449abc2511c5445af5088f4bb15f6f8baa05feb53aba9304aa1929f784ad
docker.easydb.de/pf/server-base          sha256:95b5002f574710844096c935507113b1bbd0b5e6115c3bdc12bfa0518ef6f9c2
docker.easydb.de/pf/server-base-py3      sha256:ee5cc91b4f691fa4c6664cb96f13e80c802d44c213866e9e134ec6db9f74bb65
docker.easydb.de/pf/webfrontend          sha256:fb11c50387a45e73758b8f9b65758b23cb2efea0ea2984dee06c2ab88bd09ed7
```
