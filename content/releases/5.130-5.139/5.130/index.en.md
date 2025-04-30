---
menu:
  main:
    name: "5.130 (March 2024)"
    identifier: "5.130"
    parent: "releases5130"
    weight: -630
---

> This version **does not require** a new index build

# Version 5.130.0

*Released on 2024-03-20*



# Webfrontend

## New

* **Add To Collection Tool**: The "Add to Collection" tool has been added in more places of the app, such as the detail panel and full screen view
* **Hierarchy Mode View Selector**:
  * A selector has been added in the main search and the list search to choose how hierarchical objects are displayed.
  * This new selector replaces the "Top Level Only" button included in the previous release and also replaces the old "flat hierarchy" options.
* **Connector Plugin**:
  * The connector plugin has been updated to support connections between *easydb5* and *fylr* instances
  * Support for the connector plugin has been added in *fylr*


## Improved

* **Event Manager**:
  * Design corrections have been made to the event manager
  * A button to view the referenced asset has been added for events related to assets
* **CSS**: Numerous improvements have been made to the applications CSS
* **Data Filters**: Limited the date filters to only show 10 items, similar to other filters


## Fixed

* **Editor**: Fixed a bug where the editor popover would throw a JavaScript error on load, making it impossible to use
* **Group Editor**: Fixed a JavaScript error when trying to load the group editor with a user who did not have certain permissions
* **Search**:
  * Result Views: Fixed a JavaScript error that occurred if search views were changed too quickly in the main search while the search was executing
  * Search Filters: Fixed an error when trying to sort search filters by name
* **Table View**:
  * Corrections have been made when conducting searches using the table view
  * Corrected the empty search message in Table View Searches
* **Collection Upload**: The error message has been corrected when attempting to upload files to collections using drag and drop, and the user did not have permission to do so
* **SVG Schema Download**: Fixed the button for downloading SVGs of a schema. In some cases, the incorrect schema was being used
* **Audio Player**: A bug has been fixed that caused the audio player in the asset browser to not display correctly when the asset came from a linked object
* **Top Level Only Button**: The button added in the previous version to display only top-level records has been replaced by a selector



# Server

## New

* New timestamp field `_id_parent_deleted_at` was added for hierarchical objects in `/api/v1/db` with `all_versions=1`


## Fixed

* **Metadata Import Mapping**: fix wrong tag for video frame rate
* Asset links update now handles pool watermarks. This fixes problems when trying to delete pools which use/used assets



# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.130.0         sha256:3a118631706619b1de46fc84d1f598cf49d3622260ab779f6fd44326ed6ffb7a
docker.easydb.de/pf/eas:5.130.0            sha256:a7e640665b211602d20e2e9f0b1f70c8b8e52ce2ecc2c6f708e71f25f8acf36d
docker.easydb.de/pf/elasticsearch:5.130.0  sha256:df6333c4b9ccc9f59ade4e4ca8597466e8397993d385f49b607722c44ee7f34c
docker.easydb.de/pf/fylr:5.130.0           sha256:e5854f18a4a889a4167bc5e27acc0f98f692085a9e1b325c331f196c08bd5d5e
docker.easydb.de/pf/postgresql-14:5.130.0  sha256:1196d0427d7ecb87e1948a47a5ab7ff8135638fa0b1c524061536ed1d241229a
docker.easydb.de/pf/server-base:5.130.0    sha256:8a43c66c22d3a4b7b59b66c09d2fa07243d361399cb33fc569711a701ddaa596
docker.easydb.de/pf/webfrontend:5.130.0    sha256:63a36686172075e13b7416e2d9694cb68bbd8bbd0794cc5223221caffecc14ea
```
