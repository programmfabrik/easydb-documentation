---
menu:
  main:
    name: "5.77 (December 2020)"
    identifier: "5.77"
    parent: "releases"
    weight: -577
---

> This release brings an extension of the user management. Users can now choose to delete or archive. In a later release the user can be pseudonomized for archiving.

# Version 5.77.4

*Released on 08.01.2020*

## Web frontend

*Fixed*

* **Search**: Rendering of standard info in table view was repaired.

# Version 5.77.3

*Released on 05.01.2021*

## Web frontend

*Improved*

* **Search**: Faster rendering of text view for complex masks.

# Version 5.77.2

*Released on 17.12.2020*

## Web frontend

*Fixed*

* Fixed error when printing collections
* Fixed possible error when filter view is visible

## Server

*Fixed*

* Fixed abort in `/api/v1/objects` when filename template is processed

*Improved*

* Less verbose logging when index is created

# Version 5.77.1

*Released on 15.12.2020*

## Web frontend

*Improved*

* Search: **Accelerated display** of elaborate text views.
* **Search / Detail**: Linked objects without file are now displayed **without file placeholder**.
* Search: **Filter** headings are now all consistent.
* Minor design improvements (new objects, pool information button).

*Fixed*

* **CSV Importer**: Fixed importing files with metadata into a multiple field.

# Version 5.77.0

*Released on 09.12.2010*

## Web frontend

*New*

* **Plugin (Beta)**: The new **custom-mask-splitter-detail-linked** can perform automatic searches for objects in detail and display these ads that link to the displayed object.
* **Plugin (Beta)**: The new **custom-data-type-html-editor** provides a data type with a rich text editor ([Tiny](https://www.tiny.cloud/)).
* **Data model**: New option "Not empty" for fields with ranges.
* **Search**: Boolean fields in filter.
* **Download**: Allow automatic download of multiple files instead of as ZIP.

*Enhanced*

* **CSV importer**: Improved marking of mandatory fields.

*Fixed*

* **PPTX-Exporter**: An error in connection with fade in / fade out of the standard info was fixed.

* **Data model**: Fixed an error in displaying the editor preview.
* **Print**: Sorting on printing now follows the sorting of the search result.
* Search: Error in displaying the **More** button has been fixed.
* **Editor**: The template is now called **#Template** again.

## Server

*New*

* **User management**: archiving or deletion of users.
* Download: Pool name can be configured in the file name.
* **Data model**: The range check has been extended and can now force a client-side filled in.
* **/api/search**: Aggregation for Boolean fields.
* **SSO**: Extensions in the mapping configuration.

*Fixed*

* **/api/suggest**: Preparation of the file URL with complete domain name.
* **/api/suggest**: A multiple data model update could lead to duplicated returns of linked objects.
* Improved error handling in the **PPTX exporter**.
* **Hotfolder**: Fixed an error in connection with linked objects.

# Checksums

Here are the checksums of our docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:3b0d0e3b97be2fc7129f29f56434608f6fcb3a213b2f7cfe042eccd6adbe6d0b
docker.easydb.de/pf/eas                  sha256:9b6e0c97187f681416f07e75e13a5641785f1649d569d5c4e81364fde56535d4
docker.easydb.de/pf/elasticsearch        sha256:2c61c8d9096a741cadaa496861ae13bdc4ce808995710a2849c29e25160350c3
docker.easydb.de/pf/fylr                 sha256:07246271f67c95532b44fa962eabe08eb4d0cf33fa58c96d046dc18d51b8dfc2
docker.easydb.de/pf/postgresql-11        sha256:98756185f6e1995f6cf64f46d1190968f771311967187dd5bf5c433157517290
docker.easydb.de/pf/server-base          sha256:93de5de71d79f853624593a2b62ed9de05d407c820294787eb0ab4efdc20f4cf
docker.easydb.de/pf/webfrontend          sha256:df363b2a820d422104704421bd3766e2e9e2295e3efc9b609aab078aa1a461b6
```

*Translated with www.DeepL.com/Translator*

