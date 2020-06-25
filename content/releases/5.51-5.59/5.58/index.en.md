---
menu:
  main:
    name: "5.58"
    identifier: "5.58"
    parent: "releases"
    weight: -558
---

> This update requires re-indexing, schedule an appropriate time for the update.

# Version 5.58.1

*Published on 24.10.2019*

### Web frontend

*Improved*

- **Copying rights** is more stable and allows copying individual lines again.

*Fixed*

- **Mask selection** in Exporter works correctly with more than one object type.
- Error messages in the print preview with some mouse clicks no longer appear.
- Disappearance of the cursor in search suggestions is fixed.

### Server

*Improved*

- Recognition of **email addresses** when saving is enhanced and improved.
- Improved **performance** for the XML exporter, also for OAI/PMH.
- XML Exporter exports all system fields for Linked Objects and Reverse Objects.
- **Rotating and cropping** images is repaired.

# Version 5.58.0

*Published on 17.10.2019*

### Web frontend

*New*

- **Rights** of a type can now be copied completely.
- **Multi-line input fields** are automatically adjusted in height.

*Improved*

- The display of standard A, B and C is refined and more consistent in the individual views.
- The display of pool and object type for linked objects (Text display type) and in the table display is now optional and off by default.
- **User manager**: The groups are now sorted alphabetically.
- Filters: The **search in filters** now allows an upper and lower case independent search and placeholder.

*Fixed*

- The display of file types is fixed for some cases.
- **CSV Importer**: Uploading mappings is now more stable when data models have changed.
- **Group Manager**: The Users tab is hidden for newly created groups.
- **Preferences**: The Tag Filter tab is no longer available for folders. Tag filters are not supported for folder rights.
- **Usermanager**: Save is now active if only the schedule is changed.

### Server

*New*

- **/api/event/poll**: New parameter `limit`.

*Improved*

- **Performance improvements** for many operations, especially for hierarchical object types.
- **/api/search**: Only the database languages of the user are returned in _standard, not all configured languages.
- When deleting objects, you are asked whether linked objects should also be deleted or not.

*Fixed*

- **/api/pool**: mask right without masks in _acl is now read and written correctly 
- **Filter**: The initialization is repaired for some cases, e.g. truncated first letters. This change requires the index to be reindexed.
- **/api/db**: `skip_reverse_nested` now correctly returns forward links, even if used as reverse link. 
- **/api/search**: Fixed descending order by pool.

*Translated with www.DeepL.com/Translator*