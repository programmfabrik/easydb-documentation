---
menu:
  main:
    name: "5.46"
    identifier: "5.46"
    parent: "releases"
    weight: -546
---

> - Versions **5.45.0** and later have introduced a new indexing procedure for assets. In the course of this introduction, the storage space requirement for the Postgres database has increased considerably. This was due to a history table that was overfilled. **5.46.0** does without this table and should only be about 10% higher than version **5.44.0** in terms of memory.
>

> - Version **5.46.0** requires a Re-Index, schedule a corresponding downtime of the system during the update.
>

> - With the release **5.46.0.** there were dramatically extended postgress-queries with some installations, which could lead to slow object selection and detail view. In **5.46.1** Postgres we forced all available Indeces to be used which should bring the performance in the affected installations back to the previous state. 
>

# Version 5.46.2

*Published on 19.02.2019*

### Web frontend

*Improved*

- In the hit display, the hierarchy button was moved to the right so that it no longer covers the multiple image icon.
- The hierarchy display in detail now only shows the direct way to the displayed object without displaying siblings and cousins in the tree. This speeds up the display and makes it clearer. Siblings and all elements in the tree can be displayed by opening and closing the sheet.

*Fixed*

- Fixed the use of automatic completion in connector search. 
- Some entries could lead to a frontend error in the automatic completion.
- Display of information in the pool was repaired for some cases.

### Server

*Fixed*

- Error with confirmation of workflows fixed.

# Version 5.46.1

*Published on 12.02.2019*

### Web frontend

*New*

- ScriptRunner: Selection possibility as in the exporter, in order not to work with the standard mask.
- Sorting by original filename.

*Improved*

- Hirji-Gregorian date conversion also works without day & month on request.

*Fixed*

- Preview without length and width will no longer cause an error in the zoomer.
- Sorting by file properties has been fixed.

### Server

*Fixed*

- Detection of duplicates for linked objects ignores not set columns
- Fix for partially missing parameters in the base configuration

*Improved*

- Performance in rights management has been improved by postgres optimization.

# Version 5.46.0

*Published on 07.02.2019*

### Web frontend

*New*

- Beta: New plugin FieldMigrator. With this plugin for ScriptRunner field contents can be copied from one field to another.
- The language settings for users now offer the option to hide languages that are not switched on but are present in the object in the detail view.
- JSON-Importer: New checkbox to skip already existing import objects without errors.
- CSV-Importer: Settings can be saved and loaded.
- Detailed view (full screen): Support of cursor keys for scrolling.

*Improved*

- CSV-Importer: When searching for linked objects, no terms longer longer than the word boundary of 256 characters are used. This avoids a server error. 
- The link to the documentation (displayed at the top right, if configured) no longer automatically adds the language of the frontend to the URL.
- CustomMaskSplitters are now also available for panels and tabs.
- Many minor graphical improvements.

*Fixed*

- Editor: When using special constellations of preset tags in connection with the new objects dialog and field rights to switch the tabs on and off, there were visibility problems with the tabs.
- Detail view: The display of linked objects in the Text mode was incorrectly done with the Standard setting in the mask with the standard from the data model and not with the standard (best mask) mask of the user. 
- Data model: The preview for new object types not yet adopted was repaired.
- Editor: The warning dialog which shows that another user has saved the opened object was repaired.
- Group editor: The automatic creation of new linked objects directly in the group editor was repaired.

### Server

*Improved*

- Cache for ES Analyze requests.
- Batch processing for value loading, e.g. in rights management and basic configuration.

- Support of Intranet rights management during export.
- Only database languages selected in the basic configuration are exported.
- More information in Asset and Download Events.

*Fixed*

- Removed internal information from search results.

*Translated with www.DeepL.com/Translator*