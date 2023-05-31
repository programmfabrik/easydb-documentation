---
menu:
  main:
    name: "5.117 (End of May 2023)"
    identifier: "5.117"
    parent: "releases"
    weight: -617
---


> This version **does not require** a new index build


# Version 5.117.0

*Released on 31.05.2023*


# Webfrontend

## New

* **Editor**:
  * **Adhoc template**: new feature to allow copying an object as a template. A temporary template appear in the template selector which contains the data of the last object copied as a template
* a parent field has been added to the header-detail section of hierarchy objects when the hierarchy is configured to be displayed on the mask

## Improved

* **Collection Presentation**: "Show Standard Info" option is now set as the default option for slides in presentations
* **Maskset**: mask editor for object types has been improved when selecting the "Index" option for nested fields. now the other masks of the object will copy this attribute, ensuring that all masks have the same nested index value for a specific field. Previously, the server was responsible for this
* **Search**: sub-menu of the stored search collection has been improved, options that should not appear in this sub-menu have been removed
* **Pool Manager**:
  * enhanced the pool field order on general form
  * enhanced the navigation tool texts on pool manager list
* **Transitions / Workflow Manager**: fixed "Delete" and "Copy" button on transitions manager
* changed the default value of update policy for collection upload forms to "create new preferred asset version"
* the admin messages before downloads have been improved, now all asset download options include these messages
* enhanced the group tag editor, now it needs less requests to modify the tags

## Fixed

* **Objecttype Manager**:
  * fixed a problem with the Export Assets Filename on objecttype general tab
  * main menu objecttype buttons have been enhanced to be displayed to users who only have read permissions for these object types
* **Share Asset Versions**: share buttons are only displayed for users with permissions
* bug fixes in expert search menu of the "Filter for Linked Objects" panel
* bugs in the "Filter for Linked Objects" functionality have been fixed
* fixed an error when trying to open group editor multiple times
* fixed a problem with the default pool for "pool for linked object" option on a collection upload settings
* error in the detail view has been fixed when the only available version of an asset was a watermarked version
* problem with "Reverse Linked Nested" has been fixed when there is a reference to an object where the configured field to be displayed in the reverse nested table has been emptied


# Server

## Improved

* references to archived users are replaced by the fallback system user `deleted_user`


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.117.0         sha256:51aa8f6572748f163d90100970cb835c9149edb0815e98763bd889a83d54ab23
docker.easydb.de/pf/eas:5.117.0            sha256:bd466ce347605349b2cd9055a1644cad6b167448cf5bfee436593ed15a4c16af
docker.easydb.de/pf/elasticsearch:5.117.0  sha256:ff10cf15bf50d9f7cd3b40073e398af07d2bb52f836eb03850cef49c595e5ec9
docker.easydb.de/pf/fylr:5.117.0           sha256:265f6630b4ac897e1f68dd42e7fcc6b66e1e1398e681cf51efe58ec746b25d8b
docker.easydb.de/pf/postgresql-14:5.117.0  sha256:6a9cca4fb7b73d47434963bafb75700df5b1e0ad6744732e6ef8d23650371b2c
docker.easydb.de/pf/server-base:5.117.0    sha256:3239013b4a05bdf0c5b21d01d7f79050e821cc8a63de3b6fb28d704c539b2029
docker.easydb.de/pf/webfrontend:5.117.0    sha256:33f6a9539a55b3e68834df1470f5bbe6da108f57b54b64a62f7e26041c8ba3ed
```
