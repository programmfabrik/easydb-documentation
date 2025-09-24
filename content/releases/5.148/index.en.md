---
menu:
  main:
    name: "5.148 (September 2025)"
    identifier: "5.148"
    parent: "releases"
    weight: -648
---

> This version **does not require** a new index build


# Version 5.148.0

*Released on 2025-09-24*


# Server

## Improved

* **Docker Container:**
  * improved handling of UIDs/GIDs


# Webfrontend

## Fixed

* **Search:**
  * **Selection:**
    * Fixed a bug that blocked the loading process when selecting a larger number of objects (`>700`) with the *Select All* option or shortcut
  * **Inputs:**
    * Fixed `Ctrl+A` shortcut behavior in input fields when search is open
* **Editor:**
  * Fixed the reload prompt when an update event is received, avoiding multiple stacked prompts
  * Fixed multiple new record modals triggered by consecutive `Alt+N` shortcuts
  * Fixed an error when using the `Ctrl+S` shortcut to save
  * **Mask Manager:**
    * Fixed a bug when restoring a preselected mask via the mask memory manager;
    * the object data was not loaded correctly, showing incomplete data in the editor
  * **Rights Management:**
    * Fixed a bug that showed multiple "no rights" popups for linked objects with limited rights
* **Table View:**
  * Fixed a bug that sent incorrect excluded fields
* **Collections:**
  * Enhanced sorting performance for faster and smoother UX
* **Tags:**
  * Fixed a bug when trying to access top-level data in detail rendering for tag fields


# Checksums

Here are the checksums of our Docker images (latest version):

```inidocker.easydb.de/pf/eas:5.148.0            sha256:fdfe11685fe6fc45580d7d0950023a09e2f8783ea4a1afd662fd38580991a9a4
docker.easydb.de/pf/elasticsearch:5.148.0  sha256:f9daa78c17e9a19a8b69f4ada666dc969118490fdae6beb335ffab197a9535f4
docker.easydb.de/pf/fylr:5.148.0           sha256:dfcf2ed7ef0f050e16982ee8dc57dc8177ebd4de2e63c3a5a494394958a993c8
docker.easydb.de/pf/postgresql-14:5.148.0  sha256:507104d84da06ae8d64d2964516bdaf10a3991d1800f4b703cc4dbece8b3fd41
docker.easydb.de/pf/server-base:5.148.0    sha256:7b6d0053b207d17c22b9c09d620d0b1c23aaeb45531f57808d3c89e19200730b
docker.easydb.de/pf/webfrontend:5.148.0    sha256:7d7e5be598bacb7eee83814b72c7e3c5f5ad67212747a3f1c9269780653052f1
```
