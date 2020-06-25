---
menu:
  main:
    name: "5.54"
    identifier: "5.54"
    parent: "releases559"
    weight: -554
---

# Version 5.54.2

*Published on 01.08.2019*

### Webfrontend

*Fixed*

- Detail: **Long texts in multilingual fields** were not wrapped correctly.
- Editor: Multiple use of **+ New objects** could cause an error.
- Folders: The icon for folders with **PIN code** was only available in the German language version.

### Server

*Fixed*

- A rights management error with **shared folders** has been fixed.

# Version 5.54.1

*Custom release without affecting the general code.*

# Version 5.54.0

*Published on 12.07.2019*

### Web frontend

*New*

* Beta: **PIN code support** for folders. Each rights list of a folder can be secured with a PIN code. If a user wants to access a folder with a PIN, they must enter the PIN first.
- Search result: **Pools** and **tags** can now be optionally displayed in the text view.
- In **presentations**, titles, subtitles and descriptions can now be displayed when standard titles, subtitles and descriptions are output.
- **JSON/CSV Importer**: A **metadata mapping** can be selected for importing files.
- **Data model**: A new column in the mask editor allows the creation of user notes for detailed output.

*Improved*

* Editor/Detail: The **display logic of masks** has been improved. Now also allowed masks are removed from the respective list in the editor, if they should not be displayed in the editor.
- **Structure folders** have an icon for better readability.
- The **date filter** got new groupings for future dates.
- Display improvements for **text input in date range fields**.
- The list of metadata mappings is filtered if the object types are known. 

*Fixed*

* Expert search: The search for **change history** with a date filter was repaired.

<h3>Server</h3

*New*

- Beta: **PIN code support** for folders.
- Possibility to use custom fields for the **metadata mapping profile**.

*Improved*

- The Text formatting in the **Presentation plugin** was improved.
- Search for *without content* for **multilingual fields** now only considers records in which all activated languages are not filled in.
- **Optimization** for pool changes in the group editor.
- **Stable mask order**,when loaded from Datamodel. 
- Improved security for **remote objects** in collections.
- **Export of publications** im XML / CSV - exports.

*Fixed*

- Sort by **date range fields** was fixed.
- Error when deleting and creating the same table in one run fixed.
- Fixes for **indexing** when changing base objects.
- Fixed bug when **exporting to multilingual XMP fields**.