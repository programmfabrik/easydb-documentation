---
menu:
  main:
    name: "5.140 (January 2025)"
    identifier: "5.140"
    parent: "releases"
    weight: -640
---

> This version **does not require** a new index build

# Version 5.140.1

*Released on 2025-02-13*

# Webfrontend

## Fixed

* **Search**: welcome message disappeared after some seconds
* **Detail**: fixed error when opening PDF viewer

# Server

## Fixed

* Hide IDs of deleted assets in `/api/db?all_versions=1`
* PDF printing of big documents fixed in environments with limited `/dev/shm` (such as Kubernetes pod)

# Version 5.140.0

*Released on 2025-01-29*

# Webfrontend

## New

* **Metadata Mapping**: Adds support in the import metadata mappings to add Custom Metadata Tags that are not listed in the server metadata tags.
* **Hide in Sort Manager**: Now it is possible to filter fields from the sort manager per mask. There is a new mask field option **"hide in sort manager"** that will make the field not visible in the sort manager.

## Improved

* **User Editor Templates**: The templates manager has been significantly improved; a new button to preview templates before applying them has been added in the *customize* menu.
* **Expert Search**: The System Fields are now inside a collapsible panel in the Expert Search.
* **Sort Manager**: System Fields will now be in a collapsible panel in the sort manager, making the interface cleaner.
* **Group Editor**: A cancel button has been added to the Group Editor.
* **Localization Fallback**: If an error occurs while loading the instance and translations have not been loaded yet, preloaded translations will now be used to display errors.
* **Pool Selector**: The behavior of the pool selector field has been improved.

## Fixed

* **Sharing Records**: A bug has been fixed when checking the user permissions to share a record.
* **Date Ranges**: Fixed the date ranges validation checks. Now each field (from and to) is correctly validated, and the error messages indicate which field is invalid.
* **Main Search**: Fixed a bug where the **"no results"** label was shown incorrectly when changing the result view mode.
* **Default Tags**: A bug has been fixed that occurred when using default tags in the editor's template object if the user did not have permission to use these tags.
* **Export Manager Templates**: Fixed a bug where new export templates were not saved correctly in the export manager.
* **Nested Table Check Values**: Fixed a bug triggered by *dateTimes checkValue* inside a nested table. DateTimes with ranges could output multiple errors for each field (from and to), and the nested table was not prepared for that.
* **ChangeLogColumn**: Now the change log column follows the same visibility rules in sort mode as in Expert Search mode. This means it will not be visible in the sort manager if the user does not have access to it.
* **Date Columns**: Added the correct format for the timestamps in the validation hint for date columns, ensuring the hint for range validation shows the correct time format.
* **Date Facets**: Fixed the order of the date filters when using **"Sort by count"** and **"Sort by term"**.
* **Linked Object Field**: Fixed the mask used in the linked object field in editor mode. Previously, the *best_mask* from the search popover was used, but a specific mask could be configured for the field, leading to mismatched text output. Now the *linkmask* is used for the output.
* **Mask Selection In Pools**: Fixed a bug that prevented a mask from being moved correctly in a pool's configuration.
* **Fix Collection Upload Settings**: Fixed the collection upload form to send an empty object (instead of *null*) when removing the linked object pools options.
* **Autocomplete Popup**: Fixed the focus behavior when pressing the *up* button while on the first element. Now the focus returns to the input field, allowing the user to continue typing.
* **Tag Rendering**: Fixed a critical error caused when a tag does not have a **displayType** property set.
* **Reverse Linked Tables Listener**: Fixed the cleaning of the poll listener in reverse linked fields when the editor is reloaded. Previously, the listener could remain active, causing false positives when checking for external changes in reverse linked tables.

# Server

## Improved

* **/api/event/list**: new parameter `skip_count` to skip expensive calculation of overall number of events

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.140.0            sha256:c1b44aa0f1dab4e2bc81f6a851d5d0622e20f87bd320365336af0f9e8bc439ee
docker.easydb.de/pf/elasticsearch:5.140.0  sha256:5e2ca062a092853c8694b8a4dfb5dcb1e0c98da429e214c0c9952eda8a3a8d18
docker.easydb.de/pf/fylr:5.140.1           sha256:effc4b5f5d1ff48e8ad853eece54c4b73843f1e10aaa50b913fd1ec3faa49525
docker.easydb.de/pf/postgresql-14:5.140.0  sha256:73a17d2c461c1538ae30c73f76ade294f6a65566a031dfed4d5bbfaba55d8df0
docker.easydb.de/pf/server-base:5.140.1    sha256:55b1866704f2737e87d81ff7d0ea6a2538d8b663508616ce07ddfb47d5bda93e
docker.easydb.de/pf/webfrontend:5.140.1    sha256:790b86995bf87cd4eac39d85a737a36a5300278bde940e2d613468fdd4a4bf62
```
