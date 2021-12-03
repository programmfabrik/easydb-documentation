---
menu:
  main:
    name: "5.93 (Early December 2021)"
    identifier: "5.93"
    parent: "releases"
    weight: -593
---

> This version **does not require a new index build**

# Version 5.93.1

*Released on 03.12.2021*

## Web frontend

### Fixed

* **Image Upload**:
  * fix for missing session token for EAS requests

# Version 5.93.0

*Released on 01.12.2021*

## Web frontend

### New

* **Search**:
  * `without` search for nested fields
  * sorting by *date, datetime, daterange* for nested fields
* Added deeplink for `#detail/<id>`
* New size for standard in result view: `huge`
* Upload objects modal dialog: new `RPUT` option
* **Rights Management**:
  * added optional hint for `list` parameters

### Improved

* **Search**:
  * Hide the finder when the collection manager has no content
* Do not show *'Share'* button when deeplink is disabled in the info versions of the asset

### Fixed

* **CSV Importer**:
  * fix for linked objects column id & system object id
* Show only objecttypes with file-fields in the collection hotfolder config
* Linked object filter feature bugfixes
* Small fix in the workflows confirm message

## Server

### New
* **Search**:
  * sorting by *date, datetime, daterange* for nested fields

### Improved

* **Performance**:
  * **XML Export**: Improved performance of merging of linked objects
  * Improved performance of `api/v1/objecttype`

### Fixed

* **Search**:
  * sorting by complete paths of hierarchical linked objects
  * improved handling of standard in search results: use fallbacks for languages that are not included in the search result
* **Group Editor**:
  * Update mirrored pool id of reverse-nested objects
* **Deeplink**:
  * fixed and simplified asset selection from standard (`api/v1/objects/.../file/standard/...`)
* **Datamodel Editor**:
  * Fixed corner case when a datatype of a field inside a nested tables is changed

# Checksums

Here are the checksums of our Docker images (latest version): 

```ini
docker.easydb.de/pf/chrome               sha256:94e5539d1e2ca44c798f6f84227ec06d513029e2e4e2912020827fd9e37848f6
docker.easydb.de/pf/eas                  sha256:2e3ed5ac9e6d2813260679eec3dda2b4a1ce1b48bec489a9cf06f4d45d620353
docker.easydb.de/pf/elasticsearch        sha256:044ff57d7d46f67ce89d6f952f146a2ecb3d4b193b93369c1d3f63f50d6c0a0f
docker.easydb.de/pf/fylr                 sha256:8d14e6ae1d0dd3d49756221bac0f7f3ea6bd7f810a62ffaa81a5d75faa5ef0c9
docker.easydb.de/pf/postgresql-11        sha256:6452d22df1f49980a84dd246a6683bcc5e42bba0351f80fea2f8571223349dd4
docker.easydb.de/pf/server-base          sha256:59f5d18c4fdffe98f880b7f2f2173de414d2352342ae35382a27f571791fe44a
docker.easydb.de/pf/webfrontend          sha256:95c99a2c13d98b67e1d9f920517e8878246af7e69d73036a87bc39e797272f73
```
