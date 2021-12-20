---
menu:
  main:
    name: "5.93 (Early December 2021)"
    identifier: "5.93"
    parent: "releases"
    weight: -593
---

> This version **does not require a new index build**

# Version 5.93.4

*Released on 20.12.2021*

In addition to the changes in 5.93.2 the class `JndiLookup.class` has been removed from Elasticsearch image to cope with the recent security vulnerabilities.

# Version 5.93.3

*Released on 16.12.2021*

## Server

### Enhancements

* writing of database transaction is avoided for read-only requests. This speeds up said requests.
* optimized search for non-existence of date fields. Search for messages is sped up by this change, for example.
* avoid adding unneeded languages in pool links to Elasticsearch mapping. This change is only done the next time the index has to be rebuilt, it is not enforced in patch release.

# Version 5.93.2

*Released on 13.12.2021*

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
docker.easydb.de/pf/elasticsearch        sha256:3e036c545e8e5c87a64d5e673bf9e1e455eb218006f3c53d518efc8867299111
docker.easydb.de/pf/fylr                 sha256:8d14e6ae1d0dd3d49756221bac0f7f3ea6bd7f810a62ffaa81a5d75faa5ef0c9
docker.easydb.de/pf/postgresql-11        sha256:6452d22df1f49980a84dd246a6683bcc5e42bba0351f80fea2f8571223349dd4
docker.easydb.de/pf/server-base          sha256:c686164eba710465b70954db1398cf997fa656a08e1264925d7d83ded4d4909e
docker.easydb.de/pf/webfrontend          sha256:82b2c93daae750e6bf4344497aa61b8bb1bbc82364bf433f804f6de2afc2cfc7
```
