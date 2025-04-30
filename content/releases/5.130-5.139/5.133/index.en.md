---
menu:
  main:
    name: "5.133 (End of May 2024)"
    identifier: "5.133"
    parent: "releases5130"
    weight: -633
---

> This version **does not require** a new index build

# Version 5.133.0

*Released on 2024-05-29*

# Webfrontend

## Improved

* **Standard view**: View mode configuration improved, option to hide info
* **CSV Importer**: it is now possible to use the same linked object in different mappings
* **Tag editor**: Design improved
* **Notifications**: Permanent notifications (main menu/header) only open the link instead of a popup when only one link is given

## Fixed

* **PDF printing**: Fields were not hidden correctly even though they were deselected in the settings
* **Metadata mapping**: Mapping of data to the correct nested element
* **PDF printing**: now compatible with table view for nested fields

# Server

## Fixed

* Error when changing the order of nested fields with assets corrected

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.133.0         sha256:0355b3149203cd65a9400299b0ec32e8fe488125481b0d65bb67519570e75164
docker.easydb.de/pf/eas:5.133.0            sha256:7f0dd427f3a2db7c858d9b67bba6ac96eedf7c8c06e0e8579b84140b97759d60
docker.easydb.de/pf/elasticsearch:5.133.0  sha256:2b836e1442365416b2924a4496cfe324385469e28d339fdd50d231c5071534b1
docker.easydb.de/pf/fylr:5.133.0           sha256:ce77c10c357c976b3711baa7ea7b99754335058d90a660fa3ad6de2e678bdc5a
docker.easydb.de/pf/postgresql-14:5.133.0  sha256:004542d0d9555b9d02195597b1844d93b8a80ce2777e4a1476764f74ced048f2
docker.easydb.de/pf/server-base:5.133.0    sha256:a8318066c65ac134f69d5f2db0a8ba4270cc3125e175b0e7cafce4d10c67a9b0
docker.easydb.de/pf/webfrontend:5.133.0    sha256:e3111d6815a09fd578c83d2a37828c3cb6ab0db811dc581c8e2e440a22ac165f
```
