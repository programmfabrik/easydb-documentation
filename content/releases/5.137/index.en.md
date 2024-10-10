---
menu:
  main:
    name: "5.137 (Early October 2024)"
    identifier: "5.137"
    parent: "releases"
    weight: -637
---

> This version **does not require** a new index build

# Version 5.137.1

*Released on 2024-10-10*

# Webfrontend

## Fixed

* **Group editor**: remove unwanted error message after successful run
* **Login**: don't save user on every login
* **Table view**: fixed Javascript error

# Version 5.137.0

*Released on 2024-10-02*


# Webfrontend

## New

- **Skip New Modal Upload:** Adds a new option on the new object modal to skip the configuration window the next time the new object modal opens

## Improved

- **Hierarchy Handles Tooltip:** Added a tooltip to the hierarchy handles indicating that it is possible to expand the entire hierarchy using a shortcut
- **Date Time Calendar Localization:** Improvements made to the date-time calendar regarding localization
- **Server Calls for PDFs with Images:** Reduced unnecessary server calls when printing PDFs with images
- **Leaflet Bundle:** Included the Leaflet library directly in the frontend bundle to avoid an additional request from the frontend to obtain the library
- **Deep Link:** Now, when a deep link is opened linking to a record, it will always be displayed in the main search
- **Tags:** Improved tooltips for tags throughout the application, making this functionality more consistent across the app
- **Migrations:** Prevents a frontend fatal error if the server does not include `frontend_locale` and `database_locale` in the session data
  - This can happen when opening migrated instances from easydb5
  - Also fixes issues with custom metadata fields in mappings migrated from other instances
- **Directory Upload:** Excludes `.DS_Store` files when uploading directories in the new object modal
- **CSS:** General adjustments and improvements have been made to the CSS of the application

## Fixed

- **Hidden Tags:** Fixed the behavior of tags configured as hidden and default simultaneously
  - Now, these tags will be automatically added even if they are hidden
  - Previously, these tags were ignored
- **Filter Panel:** Fixed multiple issues in the filter panel related to the use of the new `AND/OR` system
- **Saved Searches:** Fixed an error when trying to reuse tag facets from saved searches
- **Date Expert Search Fields:** Added placeholders for date fields in the changelog expert search options
  - Previously, these placeholders were not localized
- **Date Filters:** Removed the option to use the `AND` operator in date fields that are not inside a nested table
- **Date Fields:** Fixed an issue that occurred when trying to select an unsupported language in date fields
- **Collections Update:** Fixed an issue where open collections were not updated correctly when an object was added or removed
- **Event Poller on Developer Panel:** Fixed the selector for choosing the type of poller in the developer menu
- **User Manager:** Fixed the behavior of the user manager when we do not have permission to read an object after saving it
  - Now, the manager will update the list of users and clear the detail view
- **Linked Object:** Fixed an issue where a record could not be saved when a non-visible linked object was marked as required
- **Filter Panel:** Fixed a bug where the “Show more” button was not displayed correctly in hierarchical filters
- **AND/OR Switch:** Now the `AND/OR` switch will not be displayed unless these modes are actually usable
  - This prevents the switch from appearing in filters where it did not make sense to have it
- **Nested Table Structures:** Fixed a bug where complex nested table structures were rendered without field names


# Server

## Fixed

- **AI Auto Keyworder:** obsolete settings for connections to Cloudsight have been removed
  - This feature is now available as part of the [Auto Keyworder Plugin](/en/webfrontend/administration/base-config/auto_keyworder/)


# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.137.0            sha256:a55e9a53ce0b9f64a997936c5f1419125825a036cd15bf0140e8b1080870c529
docker.easydb.de/pf/elasticsearch:5.137.0  sha256:72822a7cdfa41ecbe044e6fce90f2b2400db62f71fd9233e0d5845b0c7601823
docker.easydb.de/pf/fylr:5.137.0           sha256:cde9a84dca0dd2ee1ff3a2a3e22cb423c60344562b2ed6a1487c490ae0c892ad
docker.easydb.de/pf/postgresql-14:5.137.0  sha256:cb42e48f794a18309ba94e9bd24839b0b0d888d8e28865d0c3e80b8aef87844c
docker.easydb.de/pf/server-base:5.137.1    sha256:58a09eac5f78731aaacf7e6c31461eca1db2def72299c50bad1824fa37abb19d
docker.easydb.de/pf/webfrontend:5.137.1    sha256:4ab8a05b9b3ac1227cd49a7347cd4dc5a2d536dd3968b99212ee0a9affcedc01
```
