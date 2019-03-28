---
menu:
  main:
    name: "5.48"
    identifier: "5.48"
    parent: "releases"
    weight: -548
---

> A new system right **Access only for collections (research without search function)** has been added. We will **remove** the old system right **Search not allowed (collection-only users)** in **Version 5.50.0** (planned publication on 02.05.2019). Make sure to change your rights management to the new right by then.

# Version 5.48.1

*Published on 27.03.2019*

### Web frontend

*New*

- **JSON Importer**: There is now an explicit prepare button to load the payloads. This separates the verification of the payloads from the actual upload.
- **Change history**: For the change history, the **read permission** for the object required is now sufficient. 

*Improved*

- Improved **performance** when rendering the **detail display** with many tabs. In particular, switching between tabs is now faster than before.
- **All available tools** are now loaded when **selecting** in Search, Secondary Search and Folders, i.e. Editor, Group Editor and others are now available in all context menus as well as in the 3-point menus.
- **ScriptRunner**: The search of the objects is now completely performed before the script for the objects is started. This ensures that the number of objects does not change during a run, e.g. due to tags updated by a script or other metadata that would affect the search result.
- **ScriptRunner**: When used in hierarchical lists, a search is now performed as for export. This also includes all child objects in the run.
- Small graphical improvements in different dialogs.

*Fixed*

- Fixed the **display of a message** that did not require confirmation. If the message type has previously allowed confirmation, this confirmation has also been included in the changed type.

### Server

*New*

- **/api/db** and **/api/search**: In full format, _changelog is now also published for users who only have the **READ** right for the object and the system right **frontend_features[changelog]**.

*Fixed*

  - **Server status**: For some installations, the server status could not be determined and terminated with an error.

# Version 5.48.0

*Published on 20.03.2019*

### Web frontend

*New*

- New system right **Access only for collections (research without search function)** was added.
- The status of the **Quick access** is now automatically saved for each user. The status is also stored in the group profiles for new users.
- Field rights can now be given to the **Owner** of an object. Please note that the mask option **Owner** must be set to at least visible.
- In the **Debug Mode** of the web frontend, all rights are now displayed with their API name.
- Editor: In the **upload dialog** a navigation is shown for **100 files** or more. A maximum of 1000 files can be uploaded in one process.
- In the basic configuration the **logging and saving of personal data** for export, search and detail view events can be set.
- The **Server Status plugin** now has the ability to restart the server and force a Reindex.
- **New plugin interface** to include own tabs in the **pool manager**, which can then save custom data.

*Improved*

- The **pool/object type selection** and **sort selection** no longer have an **Apply** button. The selection is automatically activated when clicking outside the selection. This dialog behaves analogous to the other smaller dialogs in the search.
- Detail: The **display of hierarchies** has been improved. Now (again) the siblings (also all fathers) are displayed.
- New Coffeescript UI version with improved **tooltip behavior** and new rules for form spacing in the display.
- **JSON-Importer**: New possibilities to mark all payloads at once.
- **Print** output improvements for some browsers.
- Editor: When **changing a pool** in objects with reverse nested objects that are also in pools, the pool is also updated for the nested objects.
- **Change history**: The user names of the changes are only displayed if the user has write permission for the object, otherwise only the time of the change is displayed.
- Pool manager: Support for more than **1000 pools**.
- **Metadata mapping**: Field names are now displayed with full path.

*Fixed*

- The easydb **index.html** page no longer contains DUMMY text indexed by Google.
- In some cases the + button in the **folder overview** has been deactivated and never activated again.

### Server

*New*

- **config**: The **logging and saving of personal data** for export, search and detail view events can be set.
- **config**: In the basic configuration, number values up to a maximum of 2^64 - 1 (UINT64) can be specified.
- **pool**: Save custom_data possibleSave custom data
- **config**: Upload limits for files per class
- **settings/reindex** allows complete re-indexing

*Improved*

- **EAS Supervisor** will no longer attempt to retrieve the status from the EAS when assets and asset versions fail.
- **Performance when deleting** collections and objects in collections has been improved.
- **Improved performance** when re-indexing objects.
- Upload limit for all files: maximum 25 GB.

*Fixed*

- After deleting tags, objects that had these tags set are reindexed.
- **After logging on using SSO**, the session status is updated and all groups are reloaded.
- Error when deleting objects that link themselves (self-reference) has been fixed.
- The **inheritance of persistent pool rights** was repaired.

*Translated with www.DeepL.com/Translator*