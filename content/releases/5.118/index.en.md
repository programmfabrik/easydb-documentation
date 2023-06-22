---
menu:
  main:
    name: "5.118 (June 2023)"
    identifier: "5.118"
    parent: "releases"
    weight: -618
---


> This version **does not require** a new index build


# Version 5.118.0

*Released on 2023-06-22*

# Webfrontend

## Improved

* **Detail**: Web link detection improved
* **Asset display**: AAC files can be played directly in the browser
* **Detail**: Buttons for searching nested objects improved
* **PDF Creator**: Text fields now also allow line breaks
* **HTML Editor custom type**: Template support

## Fixed

* **Editor**: Copying of records fixed
* **User Search**: Display of filter icon for "archived users" corrected.
* **Main menu**: Configuration of objects as buttons corrected
* **Quick View**: completely hidden if user has no rights to see content there
* **General**: Fixed bug with unexpected language tags
* **User Management**: prevented the browser from filling in fields incorrectly
* **Metadata Mapping Configuration**: Prevented duplication of fields during editing

# Server

## Fixed

* missing System Object IDs are added during upgrade

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.118.0         sha256:9d30fa74fe6a6a1ad9d0f36e84e4489093d04a37b341c4fe8f98f96969ba054a
docker.easydb.de/pf/eas:5.118.0            sha256:ffef84b28e04fb77f9935fa9d0cada573a250954021aa5acaeda58270aee82d0
docker.easydb.de/pf/elasticsearch:5.118.0  sha256:78f15e8aa21be1be55145969d37613849ce3d6aa5724efa08ce2a5f9b6c02b35
docker.easydb.de/pf/fylr:5.118.0           sha256:f731980cbdb55ef4f24e3902753dd8ad7735b53b921943fb8c1f6b3eb8e4dc5b
docker.easydb.de/pf/postgresql-14:5.118.0  sha256:41aefdf99d296cfa189215fa3ff1fc60e1073091d8bfba0fa156a54ce42d14df
docker.easydb.de/pf/server-base:5.118.0    sha256:c9b4010e0eb9d7547f492aa51f1d5d16f7c8bf1e7a8df3ceb53ee548184080dd
docker.easydb.de/pf/webfrontend:5.118.0    sha256:38406c5d4e631754cda84c4fb710b09d4b67f50ca9f4c09f05a55ceb08e846ef
```
