---
menu:
  main:
    name: "5.57"
    identifier: "5.57"
    parent: "releases"
    weight: -557
---
> * This update fixes a **security problem**, so it is **strongly recommended** to install it.
>* A few new **system rights** and a new setting may require administrative action, since some functions are now only available via a corresponding right or the new setting:
>   * **Access for Search** has been extended to **Manage own collections**.
>   * **Use CSV-Importer** and **Use JSON-Importer** have been added to the **Frontend Features**.
>   * Display of **aggregated filters** for linked object types must now be enabled explicitly.

# Version 5.57.2

*Published on 07.10.2019*

### Server

*Fixed*

- **/api/db**: Fixed multiple field removal (group and single editor).
- **Easydb-Asset-Server**: Debug log output was removed.

### Web frontend

*Fixed*

- **Group manager**: When copying with rights lines, the saving was repaired. 
- **CSV-Importer**: When searching for linked objects with more than one set field, duplicates were inserted into the database in some cases. 

# Version 5.57.1

*Published on 02.10.2019*

### Server

*Fixed*

- **/api/search**: Fixed output of default information for language combinations with more than two languages.
- **Webhook plugin**: call of Node.JS environment was buggy. 

# Version 5.57.0

*Published on 26.09.2019*

### Web frontend

*New*

- **Data model**: Multiple fields can now be set to `not_null`. This is checked by the server at API level when saving and updating.
- **Rights management**: A new system right **Access for Search** reporting has been added with a parameter **Manage own collections**. Users and groups for whom **Access to Search** reporting is set before the update are automatically granted this right.
- **Filter**: With a setting it is possible to display linked object types in a common filter or not, whereby this setting is deactivated by default. Previously, this was done automatically as soon as the linked object type was linked in at least two fields.
- **Lists**: The display of **CSV-Importer** and **JSON-Importer** is now off by default and must be activated via parameters of the system right **Frontend Features** for users and / or groups.
- **Detail view**: Text fields now also display **email addresses** as links in addition to **web addresses**.
- **User management**: A new column **Login** shows the login name of the user.

*Improved*

- **Messages**: Messages are sorted alphabetically in the administration area and the menus.
- **User management**: Groups are sorted in ascending order by ID, so that they get a traceable order. This is important for the automatic assignment of settings for new users that can be based on groups.
- **Editor**: When saving reverse objects from different object types, the reverse objects are also moved into the new pool in group mode when a pool is changed. However, this only happens if no further fields are updated. A corresponding message is displayed below the pool selection.
- **Change history**: The display now starts with the current object.
- **Graphical improvements**: The input field for email has been widened. Multiline text fields in columns are displayed lower. 

*Fixed*

- **CSV-Importer**: When loading incompatible settings, some conflicts are now corrected automatically.
- **Messages**: Under certain circumstances, messages in submenus were not always loaded in time so that they were not displayed.
- **User management**: fixed copy for users in custom groups.
- **Print**: Fixed printing of linked objects displayed in text mode.

### Server

*New*

- **Basic configuration**: Description field for **IP filter**
- **/api/db**: Allows the automatic setting of pools in reverse objects in the group editor.
- **/api/db**: New URL parameter `skip_reverse_nested.
- **New system rights**: `frontend_features.csv_importer`, `frontend_features.json_importer`, `search.has_own_collections`.
- **Custom Data Type Updater**: New callback action start_update and improved state handling.
- **/api/objecttype**: New frontend parameter show_in_facet_grouping.
- **Exporter**: Timestamp in XML, CSV and JSON exports.
- Support for `.notebook` file type.

Improved

- **Custom-Data-Type-Updater**: Call of the Node-Script now via STDIN, no more size limitation.
- **/api/session**: Sort user groups by group._id.
- **/api/eas**: Mapping for `_all_fields` is now allowed.
- **/api/group**: Paging and multiple values for URL parameter type.
- Indexing improvements.

*Fixed*

- **IP filter** for non 8-bit aligned netmask corrected.
- **/api/db**: Changelog entries for group changes of only tags or pools are now written.
- When **uploading** with remote PUT, the **original filename** may not have been correctly adopted.

*Translated with www.DeepL.com/Translator*
