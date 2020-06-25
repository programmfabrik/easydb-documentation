---
menu:
  main:
    name: "5.53"
    identifier: "5.53"
    parent: "releases559"
    weight: -553
---

> * This release requires a complete **re-index**. Schedule a downtime for the update, since the system cannot be used completely during the re-indexing period.

# Version 5.53.2

*Published on 12.07.2019*

### Web frontend

*Improved*

- **Editor**: If a mask is not configured to show in editor, it will be shown if it is the best mask for the user.

*Fixed*

- **Display of Collection contents in full screen** did not work correctly.
- Display of read-only fields in the editor did not work correctly in certain cases (e.g. in panels).
- In version 5.53.0 of the **dialog for creating new objects**, the menu item for uploading new files was lost and is now visible again.

### Server

*Fixed*

- The **indexing of collections** has been fixed. This error caused several update problems in the web frontend.
- **OAI/PMH**: The interface now has an extended error handling, so that [Open Archives Initiative](http://openarchives.org) now validates correctly. 

# Version 5.53.1

*Published on 09.07.2019*

### Web frontend

*Fixed*

- Simple CustomMaskSplitters work again in multiple fields.
- Exports containing a deleted object type can be changed without an error. 

### Server

*Improved*

- Accelerated and in some cases repaired saving in the editor by optimizing ACL checking in associated collections.

*Fixed*

- Right check in **/api/message** corrected for a case.

# Version 5.53.0

*Published on 03.07.2019*

### Web frontend

*New*

- The **date range field** now supports the text input and output of data known from easydb 4. This allows e.g. "1st century" to be specified.

- Search: For date fields there are now compilations in the filter for **today**, **tomorrow**, **this** & **next week**, **next month**. 
- **Lists**: Hierarchical lists can now be displayed by setting without hierarchy.
- EditorPlugin now supports onSave callback.
- The **display of user hints** in the editor are rendered using markdown, i.e. formatting can now be used here.
- **Editor**: Any number of new empty records can now be added. 

*Improved*

- It is now also possible to change watermarks in the **pool** if the user only has the `BAG_WRITE` right.
- **Events**: The display at startup no longer performs an automatic search for events. In databases with a lot of events an unfiltered search takes too long and timeouts may occur.
- Minor graphical improvements.

*Fixed*

- Support of host-only domains in EAS URLs. 

### Server

*New*

- New plugin [easydb-editor-field-visibility](https://github.com/programmfabrik/easydb-editor-field-visibility).

*Improved*

- Optimized list of events published via the poll interface, reducing server load. `EPORT_ASSET`, `JANITOR_USER_PURGE`, `JANITOR_SESSION_PURGE` have been removed.
- **/api/db/list** returns an empty result instead of an error if no objects were found.
- Improvements in password forget-request process.
- Re-index for updates coming from plugins improved.
- Base types are now reindexed by server code and without database triggers.
- Saving has been accelerated by new indexes on history tables.

*Fixed*

- Fixed **Intranet** assignment for anonymous users.
- **/api/pool** now saves without BAG_ACL permission.
- **History of deleted tables** is now also deleted when an object type is deleted.
- Language-dependent pool names in aggregations have been corrected.
- Fixed server status for empty databases (no assets).

*Translated with www.DeepL.com/Translator*