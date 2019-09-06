---
menu:
  main:
    name: "5.56"
    identifier: "5.56"
    parent: "releases"
    weight: -556
---

>  There is a small API change in this release to GET /api/collection/list. See below.

# Version 5.56.1

*Published 06.09.2019*

### Server

* **OAI/PMH**: Version 5.56.0. was shipped with a page size of 5 (**verb=ListRecords**). We made a basic configuration out of the page size, default is 100.

# Version 5.56.0

*Published 04.09.2019*

### Web frontend

*New*

- **Expert Search**: Displayed masks and fields are now filtered by the current **Objecttype/pool selection**, rather than by all available object types and pools. 
- **Data model**: A new option allows frontend input validation for Not empty now also for **Custom Data Type** fields. 
- **Multi-line text fields** are no longer automatically adjusted in height during input. The code of the used framework did not work correctly with Chinese keyboards under Windows 10, so we decided to do without this feature for the time being. Text fields are now 100px high and can be adjusted manually with a drag handle.

Improved

- **Lists**: The `+` button is now also available in the table view (CSV importer, create new object).
- **CSV-Importer**: The file selection is filtered by **.csv** and **.txt**.
- Improved error handling in **WebDVD** player.
- Improved display of **Markdown fields** in the detail view.
- **Printout**: The pages now have 1cm margins, so no text is cut when the pages are printed.
- Minor graphical improvements.

Fixed

- **Connector**: Loading files from Connector easydb was allowed even if the user did not have the **system right to download** for Connector easydb.  
- When **adding files in nested fields** (also reverse), the system now checks whether data already exists in the currently displayed nested entry or not. Depending on this, new entries are created (file selection allows the selection of multiple files) or if the file is loaded into the current entry (file selection only allows the selection of exactly one file).
- **Table headings** no longer get browser focus.
- A display problem with **text display for date range fields** has been fixed.
- In **user and group** selection no collection users are displayed anymore (users created to share with link).
- **Group Editor**: In cases where nested fields were hidden in a panel, the template function did not work correctly.
- **Group editor**: The pool in the template is no longer prefilled.
- **CSV Importer**: Fixed the import of nested fields where the cell starts with a blank line. The blank line was incorrectly ignored, which could result in mismatches with other columns for the same nested field.
- **Versions**: When uploading custom versions for a file, the newly uploaded file was incorrectly automatically saved as the preferred file.

### Server

*New*

- **GET /api/pool** and **GET /api/collection** now output the **_path** in the objects. 
- **GET /api/collection/list** now returns all collections, the old behavior to only output the top-level collection can be achieved with **GET /api/collection/list/null**.

Improved

- **Custom Data Type Updater** can be disabled by configuration.
- **Custom Data Type Updater** can now also work in **nested fields**. The **version** of the affected objects is **no longer increased** during updates. 
- Users that are automatically created to **share by link** will now also be automatically deleted when the collection is deleted.

Fixed

- When you **rename a pool**, all objects in the pool and below are reindexed. They now appear correctly in the filter and in the object type/pool selection.
- Some **indexing for language-dependent** data has been improved. In case of problems, please perform a Reindex manually.
- When **deleting mappings**, links in pools and object types are also deleted.
- **Fixed rights management** in nested fields for files.
- The **order of rights** for Objecttypes is now saved correctly. This has no relevance for the assignment of rights, since the order at this point is not taken into account.

*Translated with www.DeepL.com/Translator*