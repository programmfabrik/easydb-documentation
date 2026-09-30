---
menu:
  main:
    name: "5.156 (Late September 2026)"
    identifier: "5.156"
    parent: "releases"
    weight: -656
---

> This version **does not require** a new index build


# Version 5.156.0

*Released on 2026-09-30*

# Webfrontend

## Improved

* **Mask editor**:
	* Select several fields with Shift / Ctrl and move them together
	* The mask editor warns when a NOT NULL field can't be filled in with the mask. The warning goes away once the field is fillable again
* **Datamodel CSV**: The datamodel CSV export and upload keep reverse edit and bidirectional link settings. Upload is only offered on an instance without a datamodel
* **Detail**: Fullscreen opened from the detail sidebar shows the detail right away. The editor sidebar menu gets "Open editor in fullscreen"
* **Renditions & Variants**: The tab is usable at once. Link checks run in the background, one per class and version instead of one per file
* **Asset browser**:
	* The version picked in the asset info control stays selected when the window is resized
	* Entries of technical metadata lists in the asset browser info get their proper labels
* **Collections**:
	* A wrong pin and an expired share now show different messages
	* While filtering collections, a collection opens with only the matching children. Clicking it now shows all of them
* **Markdown**: Markdown rendering updated to the latest renderer. Admin messages keep their full formatting and links keep opening in a new tab. Code editor and third-party dependencies updated
* **Accessibility**: A non-interactive focus helper is hidden from screen readers

## Fixed

* **Managers**:
	* Saving a pool, object type or user no longer drops `custom_data` written by plugins, the API or migrations
	* No error popup when a delete, save or load finishes after leaving the page
* **CSV importer**: A linked object referenced by system object id that doesn't exist marks the row invalid with a clear message instead of failing the whole chunk
* **Collections**: The list of collections is loaded every time the menu opens, so collections added in the meantime show up and the empty placeholder is not repeated
* **Datamodel**:
	* Commit and Reset stay disabled when there is nothing to commit. Reset stays available while a node is selected without changes
	* Clearing the display name of a nested field is saved
* **Collection upload**: Upload settings show the file column as unset instead of silently picking the first one, and an upload without a file column can't be saved
* **Shared collections**: Only show an expand arrow when they have children the user can read, also on paginated pages, loaded children and after reloads
* **Filepicker**:
	* Each copy event is saved on its own record (they all went to the first file). The file URL is no longer stored in the event
	* The loading progress counts records instead of every exported file
* **Developer menu**: OK no longer throws a browser error when reloading the theme
* **Group editor**: The nested delete button showed a raw loca key
* **Dialogs**: Session expiry, user settings, saving preferences and changing the language no longer hang when the user can't be read or reloaded
* **Result views**: Switching the result view while a search runs no longer crashes or leaves the search button spinning
* **Presentations**: Leaving a presentation no longer warns about unsaved changes when nothing was edited, e.g. selecting a slide or opening slides with default values
* **Saved searches**: No crash when the own collection is not in the panels
* **Linked records**: Clicking the file of a linked record in a reverse or nested row opens the quick view. Layout fixes for linked records shown as text
* **Selection menu**: No exception when the Edit flyout opens
* **Field visibility (tags)**: The filter panel and the expert search no longer hide fields because of the tag part of a visibility rule
* **Hierarchy path**: A click while the search is pending or failed no longer crashes
* **Schedule editor**: "+" stays disabled until the schedules are loaded. Closing the dialog early no longer throws
* **Messages**: Active from/until dates are validated, only when the user changes them
* **Date formats**: Custom date formats of the frontend language apply again. Unknown database locales no longer fail once a date field has been shown
* **File variants**: File variants are reachable again in builds with asserts on
* **Connector**: The console no longer fills with "Refused to get unsafe header" on cross-origin responses
* **Console notices**: "ResizeObserver loop" browser notices are no longer reported as frontend errors

# Server

## Fixed

* **Plugin Callbacks**:
  * the correct external EAS URL (if set) is passed to plugins
  * This fixes problems with wrong exported EAS URLs, e.g. in the OAI/PMH endpoint

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.156.0            sha256:0ed419620bbbf72de7c1ed86a48a7be6e34ea5138a7badfd81423ec124a9b500
docker.easydb.de/pf/elasticsearch:5.156.0  sha256:edeeec8b19a2043be8d1af9a54b562376b8f4ef117ea1f8ced76fe29ed472c9e
docker.easydb.de/pf/fylr:5.156.0           sha256:4d5b9ca6329c7e673592109bf1faf4b9593aafc1d018e74324757483ef440962
docker.easydb.de/pf/postgresql-14:5.156.0  sha256:81fad6654102622a079f56ad704cdc5250722c25594107fc8fdb5b3c69fb07e5
docker.easydb.de/pf/server-base:5.156.0    sha256:5df140da5a514a19f106dff6d8b5a2073b7f9db8dfe22f1dbfe12c36e9e3bfa7
docker.easydb.de/pf/webfrontend:5.156.0    sha256:d686d28e0c712e2cebefeceb04a9fef29651ea42429221f8ac14975d7f1159b2
```
