---
menu:
  main:
    name: "5.93 (Early December 2021)"
    identifier: "5.93"
    parent: "releases"
    weight: -593
---

> This version **does not require a new index build**

# Version 5.93.2

*Released on 03.12.2021*

This patch release contains an additional mitigation for the security flaw in `log4j` known as `CVE-2021-44228` (https://logging.apache.org/log4j/2.x/security.html). According to the Elasticsearch team this flaw is not exploitable anyways (https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476).

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
docker.easydb.de/pf/elasticsearch        sha256:4525a6ad2174fdceeef9fdf2672d60f66af678d7cfddcece6d1dd8a256512846
docker.easydb.de/pf/fylr                 sha256:8d14e6ae1d0dd3d49756221bac0f7f3ea6bd7f810a62ffaa81a5d75faa5ef0c9
docker.easydb.de/pf/postgresql-11        sha256:6452d22df1f49980a84dd246a6683bcc5e42bba0351f80fea2f8571223349dd4
docker.easydb.de/pf/server-base          sha256:4c57dc78ffef39b06cac1200e521cfcda1a28145dbd1ff11cedab503dba8e31e
docker.easydb.de/pf/webfrontend          sha256:00c5ef438fb109f6a7169f944e5ffbee517a22750f5fbf097f7f88ee868c4c71
```
