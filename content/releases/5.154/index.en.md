---
menu:
  main:
    name: "5.154 (Late May 2026)"
    identifier: "5.154"
    parent: "releases"
    weight: -654
---

> This version **does not require** a new index build


# Version 5.154.0

*Released on 2026-05-27*


# Webfrontend

## Improved

* **Editor**:
  * Incompatible tags on pool change: when changing the pool, incompatible tags are now removed and the user is warned before saving
* **Secure token handling on uploads** :
  * The authentication token is no longer sent as a URL parameter in PUT/POST requests for EAS uploads
  * it is now passed in the request headers
* **Browser context menu on text and inputs**:
  * The context-menu override on right click is now disabled when the target is selected text or inside an input
  * the native browser menu (copy/paste, etc.) works as expected when handling text
* **Group Manager**:
  * Default settings panel: the panel that shows the default settings copied from a user no longer lists object types that are no longer available in the main search
* **Drag & drop assets**:
  * Dragging assets to create records no longer triggers when the asset is dropped on a detail view or the editor
  * this avoids false positives (e.g. when missing a drop on an EAS field)
* **Tokenizer**:
  * Ranges with spaces: the tokenizer in expert search (string columns) now allows ranges that include spaces, for example `A 1 - A 5`

## Fixed

* **Connector Plugin**:
  * Availability check of remote instances: fixed an error when checking connector availability for the new version of the connector plugin
* **Print Manager**:
  * Fixed harmless warnings from print assertions
  * Stopped the frontend from trying to render tooltips in print scenarios on some browsers like Firefox
  * Turned a `cUI.dom.empty` error into a log warning instead of throwing
* **Cross-instance request headers**:
  * Fixed an unsafe header in cross-instance requests (such as the connector)
  * Cleared some harmless console warnings in connector scenarios
* **Hierarchy "not found" label**:
  * Fixed the "not found" label in search for hierarchy mode set to auto, which was wrongly using the top-level "not found" variant
* **CSV importer**:
  * Fixed a race condition when building the CSV importer configurator panel
  * This could render before the proper dbinfo data was available and throw an error
* **Collection Settings**:
  * Fixed the initial data check in collection settings so the save button honors the initial state and stays disabled when no changes have been made
* **DBInfo masks**:
  * Fixed a null check in the "get available masks" function
  * This could be called before real dbinfo data was available and throw an error
* **Right Presets**:
  * Fixed a bug where the preset list was not persisted correctly when navigating through the preset manager
  * This caused deleted elements to remain visible
* **Facet/saved search**:
  * Fixed a critical frontend error when generating a search from saved search data
  * If the saved search had a filter, it could fail on target systems with no filter manager (e.g. the popover search)
* **Table View**:
  * Fixed a bug that selected the wrong rows in table view after an `OBJECT_INDEX` event


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.154.0            sha256:637647f8097a9b3eecce850f804dc646f4a645cf12ad710c581d2baba7511a6e
docker.easydb.de/pf/elasticsearch:5.154.0  sha256:049e98512933bb582bdb54c6c014aa6dbd144d19b18fb2bf7b07479ee21c1397
docker.easydb.de/pf/fylr:5.154.0           sha256:78ff91b129b383f334757e3a191b3334bfb531a79e03d3e3ffbb7c208d1f4aa7
docker.easydb.de/pf/postgresql-14:5.154.0  sha256:d5816a18d74ba7f3336077c5363bda988e827e2b4e00372bc422a02e415b3b1b
docker.easydb.de/pf/server-base:5.154.0    sha256:928e9dab82fa464219c2d186290006839f58b0ef58938c790fee164d7c5c0f56
docker.easydb.de/pf/webfrontend:5.154.0    sha256:bc16b904441dac0f8782b25c70555e9ae803b397ff5a4d20ba238bbfd6e088b0
```
