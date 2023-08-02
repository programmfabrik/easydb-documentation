---
menu:
  main:
    name: "5.113 (Early March 2023)"
    identifier: "5.113"
    parent: "releases5110"
    weight: -613
---


> This version **does not require** a new index build

# Version 5.113.1

*Released on 03.03.2023*

# Webfrontend

## Fixed

* **Detail View**:
  * fixed problems with the new output of the object **UUID**

# Version 5.113.0

*Released on 01.03.2023*

# Webfrontend

## New

* **Detail View**:
  * alphabetical order for linked objects in Custom Mask Splitter
* **Collection Presentation**:
  * added a new slide type: Image and Text side by side
* Added output of object **UUID** to footer of Detail View, Editor as well as Expert Search

## Improved

* **Performance**:
  * Objecttype Manager loads faster since it uses the new `short` format of the `objecttype` Api
* **Email Adress Input**:
  * Email Adress validation is done according to the `RFC5322` standard

## Fixed

* **Search**:
  * fixed "Remove from collection" in search context menu
* **Expert Search**:
  * remove duplicate "Not Set" button
* **Detail View**:
  * fixed state of checkbox in diff viewer in change history
* **Collections**:
  * fixed problems when collections that have been deleted in the meantime are selected
* **Datamodel**:
  * checks for duplicate mask names are now done on the client side as well, not only in the server


# Server

## New

* New `short` format for the `objecttype` Api to avoid requesting unnecessary data

## Improved

* **Collections**:
  * collections of deleted users are removed from the index
* **Datamodel**:
  * improved unique constraint checks for columns with changed type


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.113.0         sha256:184d742babb22902ce3e8db124d04e99f7f20bfe1a752407617293e32a18685d
docker.easydb.de/pf/eas:5.113.0            sha256:46958db7d7af789ee62c9ba535af4e80bae450f29c0eddb8ab5ba161d4f55fa6
docker.easydb.de/pf/elasticsearch:5.113.0  sha256:ad2cf4201f3e46b7e42e0704f9f6382b3a0a45e69eaf8118f3c36d921938b890
docker.easydb.de/pf/fylr:5.113.0           sha256:2378b05ced5aa50ffd07b73b883c265e1f1510d80d3ad91f44a3351da35e5edf
docker.easydb.de/pf/postgresql-11:5.113.0  sha256:48ffbcc1bc716668bff83606434392fb5590406fcd33c643da2e496ee7d4af6d
docker.easydb.de/pf/postgresql-14:5.113.0  sha256:a35666b028a44dd581c582cf3fa5d563b165c5af053a0936e658ee98477ce64e
docker.easydb.de/pf/server-base:5.113.1    sha256:890f2dc7116f81360f3f83429ed81b28697b477ea0c1d39e44fd170153385659
docker.easydb.de/pf/webfrontend:5.113.1    sha256:4db53d12a63b81b86823f8ec4c433b7e53a9a814656fc9924a7c503d1d43d6dd
```

