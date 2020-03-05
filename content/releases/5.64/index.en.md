---
menu:
  main:
    name: "5.64"
    identifier: "5.64"
    parent: "releases"
    weight: -564
---

> This version brings a change in the behavior for **workflows** (see below).
>
> There is no re-index so that an update only requires a server restart.

## Version 5.64

*Published on 04.03.2020*

### Webfrontend

*New*

- Checkbox to switch on and off all **resources** directly in the search.
- **Editor**: A user setting allows the individual switching on and off of languages in multilingual input fields.
- **Mass deletion** requires the new system right `editor_bulk_delete`.
- **Mask option**: Multiple fields can be sorted by pool when displayed.
- **Mask option**: Multiple fields with Booleans can influence the sorting of thumbnails in the Asset Browser.
- **Mask Option**: Masks in the print menu can be hidden with this option.
- **Updates via upload** in Collections (currently only visible in debug mode, beta)
- **Workflows**: It is now possible to copy lines.
- **CSV importer**: The import of hierarchical objects has been extended so that the parent element can now be set.

*Fixed*

- The integration with **cloudsight.ai** was repaired. 
- Creating new **linked objects** directly in the editor has been fixed for special mask rights settings.

### Server

*New*

- Custom-Data-Type-Updater now gets the complete system configuration in the `start_update` action.
- **/api/mask**: New option `hide_in_print_dialog`. 
- **Export**: The **FTP** transport now supports storing as **ZIP file** on the FTP server.
- **/api/user**: Support for `custom_data`.
- New **system right**: `frontend_features.editor_bulk_delete`.

*Improved*

- Acceleration of the **deletion** of records with many files.
- **Workflows**: For tag filters, an empty tag list is assumed for objects of an object type that has no tags activated. Previously the tag filters for the corresponding workflow were ignored.
- **XML-Export**: `_path`of linked objects are now exported. In addition, `_standard.2.text` and `_standard.3.text` are now also exported.
- **/api/db**, **/api/search**: Format `standard` now contains the pool of linked objects.

*Fixed*

- **Janitor**: Configuration may not have been loaded correctly, causing Janitor to be started too often and putting unnecessary load on the system.
- **LDAP**: Problems could occur at logins if the user was previously logged in as easydb user and was deleted.

- The **sorting** by leaf entries of hierarchical linked objects was fixed for most cases.

*Translated with www.DeepL.com/Translator*