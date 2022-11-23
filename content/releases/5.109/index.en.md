---
menu:
  main:
    name: "5.109 (November 2022)"
    identifier: "5.109"
    parent: "releases"
    weight: -609
---



> This version **does not require** a new index build


# Version 5.109.0

*Released on 23.11.2022*


# Webfrontend

## New

* **User Manager**: added new expert search for user filter in user management, now users can be searched by name, phone etc
* **Localization**: added danish specific datetimes format
* **Collection**: added a language selector for anonymous users in collection shares

## Improved

* **Asset Browser**: asset browser in editor now behaves the same way as the asset browser in the detail view: if there is no eas column then the asset browser is not shown
* **Datamodel Editor**: added checks for internal names of object types and fields to avoid sending wrong data to the server
* **Mini Search**: improved searching of linked objects. Now the search uses `fulltext` mode in the filter by default, to find more relevant search results

## Fixed

* **Connector**: fixed a bug where the pagination of main search would display wrong data if there are multiple connector instances activated
* **Collection**: fixed the move slides options in presentation editor
* **Export**: fixed a bug where the exporter would not display media files correctly if a large number of objects was selected
* **Detail View**: fixed a bug where the record history in the detail view would display wrong data if the history selection was changed too quick
* **Mini Search**: fixed autocompletition
* Fixed a bug where the upload information in the new editor modal would not show the correct information
* Fixed a bug where the group edit button in search tools could be duplicated
* Fixed a bug where tooltips prevented the closing of modal windows


# Server

## New

* **Automatic deleting of Assets**:
  * After deleting files in easydb, they are finally deleted from the storage medium of the easydb server
  * This feature is now **enabled by default**
  * The technical variable `server/janitor/enable_asset_cleanup` is now enabled by default

## Improved

* **XML Mapping**: allow usage of not searchable fields for XML export mappings

## Fixed

* **Asset Version Configuration**: Fixed hi-res video bit rates


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:c0f17ed1f925787b8eae7971c9a98ebea02c2a41e8d7df0a5fb520cd40c89a3c
docker.easydb.de/pf/eas                  sha256:f010d3d88650c1723f49383843f1a990d4e08aee18b66e914a31a56d806c0a64
docker.easydb.de/pf/elasticsearch        sha256:1fbb7466b69ec9bebff2e0340c4ca59d72d9c3b8faad99b72659c0aa45d3c58f
docker.easydb.de/pf/fylr                 sha256:50e3d9840a5707f003865b65c61d0f6f5890b12cdc1afd8530abe65d3ecf59ed
docker.easydb.de/pf/postgresql-11        sha256:69717d744cd8f2b666a0d9882259b2ca0ea96241b8764d9f2c05357d84489ea0
docker.easydb.de/pf/postgresql-14        sha256:d447e0b2e6abbbf45845192b983fff930d57dbb838159823a5ddf4f85b35a16b
docker.easydb.de/pf/server-base          sha256:9524a6ef51290ac362cdb71d43e366bff3586a12f93c90fd4a2710817723646d
docker.easydb.de/pf/webfrontend          sha256:8f9e2e1b6ac25711bc742fe5af9193e2bcac995ae765b4e504a6cd43c9810db2
```
