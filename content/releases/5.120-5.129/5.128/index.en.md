---
menu:
  main:
    name: "5.128 (February 2024)"
    identifier: "5.128"
    parent: "releases5120"
    weight: -628
---

> This version **does not require** a new index build

# Version 5.128.1

*Released on 2024-02-08*

# Server

## Fixed

* EAS: fixed problems with rendering of preview versions of files

# Version 5.128.0

*Released on 2024-02-07*

# Webfrontend

## New

* The quick access view now shows the asset browser by default

## Improved

* The PDF creator has been improved by adding the ability to select a mask within the editor, allowing the user to preview how the PDF template will appear with a given mask
* The "Show history" button in the print manager has been improved
* The number of objects displayed in the detail hierarchy view has been increased, and the functionality of the "Load more objects" button has been corrected
* The functionality of the main search has been improved:
  * if an item in the detail view is changed using the lower navigation buttons, the selection in the main search is correctly changed to display the new selected item.
* The functionality of the root menu has been improved
  * now the application remembers its configuration (whether the user has it open or closed)
* The behavior of the asset browser when loading new assets into the application has been significantly improved:
  * Now, the asset browser will progressively display the processed versions
  * This means that if, for example, a video is uploaded, the asset browser will first show the preview as soon as it is available and will go on to display the video's processed versions (360p, 720p, etc.)
* The use of the EAS Poller in the application has been improved, making it not run when it is not necessary

## Fixed

* A bug in the input search that duplicated double quotes in search terms has been fixed
* The full screen editor now correctly displays the asset browser when opened
* The "System Object ID" field in the expert search and in the sort menu has been corrected
* A bug that prevented the new object loaded in the main search from being displayed has been fixed
* The order of options in the video player's quality selector has been corrected
* Corrections have been made to the functionality of the fullscreen editor

# Server

## Fixed

* Datamodel: fixed problems with renaming of fields with long names

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.128.0         sha256:a0912128b9537b1cc74716007eb74e819d6fa72720882301b39050b66d25bc84
docker.easydb.de/pf/eas:5.128.1            sha256:034967147768a1d0bebb96c9669af5ae05f8606323eea2032b89866690858595
docker.easydb.de/pf/elasticsearch:5.128.0  sha256:a50b7a670d2c85b1bc2cbda0a58c1bca2d081b25ca58ec34e8cfca699679de93
docker.easydb.de/pf/fylr:5.128.0           sha256:16b6a996996c546ad7d123e513ee5069c72d2a48ca76ce2dc6ecef2835217376
docker.easydb.de/pf/postgresql-14:5.128.0  sha256:c4fb4892e216034df67ef53118faa2c73df60604ff07e80cf513b1d44bb66bdd
docker.easydb.de/pf/server-base:5.128.1    sha256:2b4c18f945292722b6381f2bd204bcad79aaccd4a5fd1ad1087f25c3cde28e3f
docker.easydb.de/pf/webfrontend:5.128.1    sha256:365f59bad2a7b7cf8a0f7cd465c7f8d8538eecf522f1e0700125196085529f4d
```
