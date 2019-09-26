---
menu:
  main:
    name: "5.38"
    identifier: "5.38"
    parent: "releases550"
---

# Version 5.38.2

*Released on 08/09/2018*

### Webfrontend

*Fixed*

- Custom Data Type Link: Fixed an error with empty names.
- Pool select: Fixed invisible scrollbar in long lists.

### Server

*Improved*

- New **wkhtmltox** for improved WebDVD previews.

# Version 5.38.1

*Released on 08/03/2018*

### Webfrontend

*Fixed*

- PowerPoint Exporter: The created **pptx** files did not contain any images.
- Custom Data Type Link: Fix for usage inside Nested with templates.
- CSV Importer: Fixed a bug with importing Hierarchy Nested Objecttypes which include a Linked Object.
- User CSV Importer: Fixed upload of a **csv** file.

# Version 5.38.0

*Released on 08/01/2018*

### Webfrontend

*New*

- Base Configuration: Support for download without linked files.
- Self Register: Admin messages can be added which need to be confirmed.
- Data Model: Mask editor supports moving fields using buttons.
- Custom Data Type Link: Support for URL templates.

*Improved*

- CSV Importer: Deletion of nested fields is supported.
- CSV Importer: Improved support for nested fields (also nested in nested).
- CSV Importer: Improved error message for ambiguous mapping.
- Plugin Manager: JavaScript is pulled in using a **\<script\>** instead of **eval**.
- Presentation: Improved performance by using a rolling cache for 10 objects.
- Selects: CUI.ItemList now supports *multiline* items for long texts. This improves readability. 
- CSV/JSON Importer are now available in the main dialog for new objects and can be found in the List App next to the *plus* button. With this change, users without the *create* right can no longer reach neither importer.
- Sorting of Custom Data Types in nested fields is supported.
- Search: The expert menu now shows masks and field lists even with only one Objecttype available.
- Improved preview sized in list results.

*Fixed*

* Nested fields with empty date as first field would cause a loading error in the Editor.
* Drag & Drop: Fixed timing problems which led to wrong count of marked objects.
* Export Manager: Fixed list view after delete.
* New objects: Fixed save during cancel.
* Detail: Display of forbidden objects could lead to a eternal spinner.
* Editor: Fixed enabling save button after changes in Date Range fields.
* Data model: Fixed some refresh and save problems.
* Quick View: For very large objects the layer would be displayed off-screen, fixed in CUI.Layer.
* Date picker: The header showing the names of the weekdays is back.

### Server

*New*

- Support for archive filetypes: **tar**, **tgz**, **bz2**, **gz**.
- Support for Vector 2D: **dwg**, **dxf**.
- POST /api/config supports nested **type: table** for Custom Data Types.

*Improved*

- Faster search queries with lots of Pools.
- Right presets need to be unique by context only.
- Faster save for Pools with long Access Control Lists.
- Support for ZIP files compressed with DEFLATE64.

*Fixed*

- CSV Exporter: Improved support for objects with nested fields, enabling the import of the unchangbed file using the CSV-Importer.
- Metadata export: In some cases metadata was not written correctly in exported files.