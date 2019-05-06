---
menu:
  main:
    name: "5.50"
    identifier: "5.50"
    parent: "releases"
    weight: -550
---

> * The old system right **Search not allowed (collection-only users)** has been replaced by the new **Access only for collections (research without search function)**. Make sure that you change your rights management to the new rights **before updating**.
> * This release requires a complete **re-index**. Schedule a downtime for the update, since the system cannot be used completely during the re-indexing period.

# Version 5.50.0

*Published on 04.05.2019*

### Web frontend

*New*

- **Data model: Horizontal line and block** as well as all CustomMaskSplitters that are set up for this can be used **in multiple fields**.
- In the **context menu** there is a new option to copy to the clipboard.
- The list view now optionally allows **1000 hits** per page.

*Improved*

- Rights management: For object types without assets, the **display in rights management has been streamlined** so that the rights for assets are no longer displayed.
- The system object ID has been added to the **print text view**.
- The **expert search** now only shows Tags that are available for the current search.
- Editor: The currently selected mask is used for **copying records**.
- Detail: The **Copy** function is now also available in the 3-point menu.
- The display of **selected multiple fields** in the search has been improved.
- **Presentations**: Improved output for records without previews.

*Fixed*

- **Connector**: Fixed scrolling in search results.
- Object Type Manager: The **Save button** was not activated for exclusive tag changes.
- Fixed display of **owner field** depending on field rights and tags.
- A Javascript error was produced with **Esc** in an empty pool search.
- Fixed **display of rotated images** in small previews.
- In **side editors**, the display no longer jumps up when typing in a scrolled area.

### Server

*New*

- **CustomDataTypeUpdater**: A new server process allows the automatic periodic updating of CustomDataTypes. As an example we provide an updater in the [custom-data-type-gazetteer](https://github.com/programmfabrik/easydb-custom-data-type-gazetteer/). (Beta). 
- **Data model**: Boolean fields are no longer supported for standard generation.
- **CSV export**: Output of asset ID and output of hierarchies also for top-level data sets (not only for linked objects).

Improved

- **Performance**: Rights management for some calls is faster for complex configurations. The improvements are mainly for **/api/db_info**, but also **/api/search** (with generate_rights, used in detail view) is faster.
- **Performance**: Loading settings has been speeded up, making calling **/api/session** faster.
- The **Webhook Python plugin** now uses **node.js** of the system.

*Fixed*

- The use of passwords via **LDAP** with **special characters** is supported correctly.
- Generating the **Standard in multiple fields** correctly takes the order of the fields into account.
- When creating new objects, race conditions could occur in some cases which caused a Javascript error in the frontend. The reason was that the **/api/eas** endpoint did not always return the original file names. This was corrected.
- Fixed **wildcard search** for associated words. Searching for "worta wortb*" now works correctly.

*Translated with www.DeepL.com/Translator*