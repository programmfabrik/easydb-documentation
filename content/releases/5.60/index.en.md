---
menu:
  main:
    name: "5.60"
    identifier: "5.60"
    parent: "releases"
    weight: -560
---

> This release brings performance improvements for building the Collection Manager for installations with many users.

# Version 5.60.0

*Published on 27.11.2019*

### Web frontend

*New*

- For **AssetDetailPlugin** there is a new function getSiblingsFromDataum to access other asset versions.

*Improved*

- **Publications** now have extended configuration options for display in detail.
- **Data model:** In the mask manager, individual options are now shown and hidden depending on the context.
- **Data model:** Schemaserver improvements.

*Fixed*

- **CSV-Importer:** A bug with finding linked objects in lists with more than 100 entries was fixed.
- **Collection Manager:** Split mode now works correctly again.
- **Search for tags** across all object types has been corrected.
- **New objects:** Fixed saving of pool and mask selections for the user.
- The **loading of the web frontend** was not possible in some browser/operating system combinations for cross server use. Currently we work around this problem by running **webfrontend sessions without cookies**.

### Server

*Improved*

- **Performance improvements** in invoice management, in particular the structure of collections, should now be faster.

*Fixed*

- **/api/user:** POST returns `database_languages` and `search_languages` correctly, so that users can change their languages correctly without having to log in again.

- **/api/objecttype:** Support for `:eas_data`in custom_data.
- The unsolicited massively **sending of emails** in some cases has been corrected. 
- **/api/db:** output of _changelog for archived users was fixed.
- **CustomDataTypeUpdater:** Fixes for cases where an object type was renamed multiple times.

*Translated with www.DeepL.com/Translator*

