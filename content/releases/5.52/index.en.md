---
menu:
  main:
    name: "5.52"
    identifier: "5.52"
    parent: "releases"
    weight: -552
---

# Version 5.52.0

*Published on 12.06.2019*

### Web frontend

*New*

- New objects: Setting to permanently skip the duplicate check.
- **Collections**: New context menu option to display foreign objects from connector databases.

*Improved*

- **Collections**: When sharing with the **All Users** or **Anonymous Users** group, a link is created that is explicitly authenticated with **anonymous**. This simplifies the test of such links and known users are not logged in with their cookie but as new users.
- **Improved display** of the selection menu for users and groups.
- **Data model**: Input help for field and object type identifiers.
- **New progress bar** when uploading files in the editor.
- Graphical detail improvements.

*Fixed*

- **Saving** and updating pools in child reverse nested objects did not work correctly in some cases.
- **Fixed printing of folders** with connector objects: Connector objects can only be printed via search, not directly from the folder.

### Server

*Improved*

- Memory requirements of the Janitor have been reduced.
- Faster CSV export for events.

*Fixed*

- Standard for multiple fields was not sorted correctly in some cases.
- Fixed a search error that could occur with certain language combinations.
- Improved re-indexing of dependent objects.
- Rights check on reverse linked assets fixed.

*Translated with www.DeepL.com/Translator*