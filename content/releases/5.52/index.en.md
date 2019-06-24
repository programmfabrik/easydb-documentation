---
menu:
  main:
    name: "5.52"
    identifier: "5.52"
    parent: "releases"
    weight: -552
---

# Version 5.52.3

*Published on 24.06.2019*

### Web frontend

*Fixed*

- Pool change for editable Reverse Hierarchy objects works again (was faulty since 5.52.2.).
- Fixed **custom** group selection in user and group selection menus.

### Server

*Fixed*

- Standard compliant **OAI/PMH** response for **NoRecordFound**.
- Search language dependent autocompletion is now correctly supported. 

# Version 5.52.2

*Published on 20.06.2019*

### Web frontend

*Fixed*

- Display problems in some Connector scenarios fixed.
- Saving reverse nested for new objects with pools fixed.

### Server

*Fixed*

- Fixed localization of workflow messages.
- Webhook callbacks generated from the group editor now also send the `_version` of the object to the webhook.

# Version 5.52.1

*Published on 17.06.2019*

### Web frontend

*Improved*

- Autocompletion now starts after 500 milliseconds without entering a new character. The previous 200 milliseconds were too short.

### Server

*New*

- **/api/suggest** supports a new parameter **fields_suggest** to avoid the search for **fields** in the response. This leads to shorter response times.

# Version 5.52.0

*Published on 12.06.2019*

### Web frontend

*New*

* New objects: Setting to permanently skip the duplicate check.
* **Collections**: New context menu option to display foreign objects from connector databases.

*Improved*

* **Collections**: When sharing with the **All Users** or **Anonymous Users** group, a link is created that is explicitly authenticated with **anonymous**. This simplifies the test of such links and known users are not logged in with their cookie but as new users.
* **Improved display** of the selection menu for users and groups.
* **Data model**: Input help for field and object type identifiers.
* **New progress bar** when uploading files in the editor.
* Graphical detail improvements.

*Fixed*

* **Saving** and updating pools in child reverse nested objects did not work correctly in some cases.
* **Fixed printing of folders** with connector objects: Connector objects can only be printed via search, not directly from the folder.

### Server

*Improved*

* Memory requirements of the Janitor have been reduced.
* Faster CSV export for events.

*Fixed*

* **OAI/PMH**: Scrolling through the sets was corrected and was faulty with many objecttypes / pool combinations.
* Standard for multiple fields was not sorted correctly in some cases.
* Fixed a search error that could occur with certain language combinations.
* Improved re-indexing of dependent objects.
* Rights check on reverse linked assets fixed.

*Translated with www.DeepL.com/Translator*