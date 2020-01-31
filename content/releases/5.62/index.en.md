---
menu:
  main:
    name: "5.62"
    identifier: "5.62"
    parent: "releases"
    weight: -562
---

# Version 5.62.2

*Published on 31.01.2020*

### Web server

*Fixed*

- Sources popover is showing a scrollbar for really long lists..

# Version 5.62.1

*Published on 28.01.2020*

### Web server

*Fixed*

- Login and workflow popovers grow again when their content changes.

### Server

*Fixed*

- Saving pools in databases with object types with names of SQL commands was fixed.

# Version 5.62.0

*Published on 22.01.2020*

### Webfrontend

*New*

- The **Single-Sign-On** login has got new settings for the buttons in the base configuration.
- Support of numbers with thousands separators in the **CSV importer**.

*Improved*

- **Object types/pool** selection button is now called **Sources**.
- Detailed textual display of the current **sources**.
- Display of the objects in a pool shows the number of objects in a pool when collapsed, including all subpools. When expanded, only the number in the pool itself is displayed.
- **Popover** display of the editor has been improved.

*Fixed*

- Loading invalid **templates** no longer leads to a Javascript error but is made transparent in an error message.
- The import of hierarchies in the **CSV importer** was fixed for some cases.
- The creation of multiple fields and the display of pool names and linked objects created during upload in the **New Objects dialog** has been fixed.
- The **editor preview** in the data model has been fixed for some cases.

### Server

*Improved*

- Improved **indexer performance**.
- **Streamlined** **index** for normal reverse-nested objects (**re-index** necessary, not done automatically).

*Fixed*

- Setting the **language** for some **anonymous users** has been fixed, as a result the suggestions work in the search for affected users.
- **Preferences** with rights management for obsolete asset versions are corrected at server startup and affected versions are no longer delivered via the API
- **/api/event** now works correctly when users are deleted in events.
- Fix for **hotfolder** and umlaut problems on installation with incorrectly set language in the environment.

*Translated with www.DeepL.com/Translator*