---
menu:
  main:
    name: "5.42"
    identifier: "5.42"
    parent: "releases550"
    weight: -542
---

> - This update requires a re-index, schedule appropriate downtime / update time.
> - The bugfix of the the misinterpretation of `Standard` in multiple fields caused problems for fields with the same name (e.g. "title" and "additional__titel.titel"). Check the mask settings for `Standard`.
> - This release currently has a problem with download + export when connector instances are activated. For Download + Export deactivate the connector instances (at user level).
>

# Version 5.42.1

*Published on Nov 1st 2018*

### Webfrontend

*Fixed*

- Saving new objects after uploading has been fixed.

# Version 5.42.0

*Published on Oct 31st 2018*

## Webfrontend

*New*

- Upload menu on right click and as favorite for folders.
- Exporter: A new function allows you to select your own masks for each exported object type. When exporting, the easydb-side selection of the best mask can be overwritten.

*Improved*

- Display of multilingualism: All set languages are displayed in the editor and detail. The user settings for the data language determine the input languages of the editors that are at least visible.
- Exporter: Dialog opens faster, in some cases too much data was loaded from the server.
- Developer: In debug mode, no session cookies are set and checked by the server. This makes it easier to copy the entire request in CURL format in Chrome.
- Data model: Loading defective data models no longer leads to a crash, but allows you to discard at least the defective data model.
- Data model: Enlarged and more informative display of information in the overview.
- CUI: Correct calculation of display positions even if margin and border are used for the BODY. This concerns the use of easydb with its own CSS.
- Small searches and editors have a full screen function.
- Improved design of printouts.
- Pools: Display in the administration area has been accelerated by automatically opening only the first child level.
- CSV-Importer: More information in the log file.

*Fixed*

- Search: Improved cursor setting when filtering in Quick Display.
- Basic configuration: Correct setting of the minimum display of list items (such as languages).
- Search: Corrected display of linked images from other object types in the text view.
- CSV-Importer: Incorrect import of linked objects has been fixed.
- Presentation: Export of PPTX from unsaved changes was fixed.
- Display of a menu for files in reverse nested objects was fixed.
- Display of more than 1000 folders of a user is now possible.
- Data model: UNIQUE support for custom data types has been fixed.

### Server

*New*

- Login to a normal user account with the access data of an admistrative account.
- Search by asset status enabled.
- Languages for the Suggest-Index are now selectable in the basic configuration.

*Improved*

- Enables aggregations for multiple fields that have "Nested Index" enabled in the mask settings.
- Improvement for `/api/suggest`, no multiple suggestions.
- Enabled use of custom data type fields in group editor.

*Fixed*

- Fixed bug when changing passwords migrated from easydb-4.
- Fixed _standard creation bug when fields on different levels had the same name.
- Indexing of message objects is preferred to improve user notification when re-indexing.
- Improved error handling (collections, saved searches).

### Fylr

*Improved*

- Zip: Check URLs before compression to improve error handling.
- Error page design improved.

