---
menu:
  main:
    name: "5.63"
    identifier: "5.63"
    parent: "releases569"
    weight: -563
---

>  This release brings many new features in the web frontend, a new page view in the editor and a detailed preview in the CSV importer.
>
> No new index is necessary, so updates only require a restart.

# Version 5.63.2

*Published on 17.02.2020*

### Web server

*Fixed*

- **New objects**: Error message at close dialog fixed.

### Server

*Fixed*

- **Rights management**: Pool ACLs with tag filter now also work for objects whose object type has no tag management activated.

# Version 5.63.1

*Published on 14.02.2020*

### Web server

*Fixed*

- **Editor**: Using the sidebar for the first time no longer causes the dialog to overlap.
- **CSV importer**: **Preparation** now only becomes active when a Pool has been selected (if necessary).

### Server

*Fixed*

- **Janitor**: A bug caused the **Base configuration settings** not to be taken into account and Janitor was started every 10 minutes. This in turn led to unnecessary load for larger databases.

# Version 5.63.0

*Published on 12.02.2020*

### Web server

*New*

- A new **Versions** tab in the file information shows an overview of the available versions of a file. In the overview you can also select the displayed preview image.
- **Editor**: In full screen mode the file preview can be moved to a page view. This leaves the previews visible, even with more complex stacked input forms.
- **Editor**: `ALT`-click `+` to open stacked input forms in full screen mode.
- **Mask management**: A new setting allows to **hide a tab system** if only one tab is displayed.
- **Mask management**: New option allows different **output settings** for linked objects in table and text view.
- **Table view**: Settings for manual widths are now saved for the user.
- **CSV importer**: Selection of a pool for newly created linked objects is now possible.
- **CSV importer**: New display of records in a detail view.

*Improved*

- **JSON/CSV importers** are now available in the **Tools** main menu.
- **Developer menu** is now available in the **Tools** main menu.
- **Detail View**: Strong performance improvements in the display of many thumbnails when they are taken from linked objects.

*Fixed*

- **Group editor**: saving is now possible if only the user settings have been changed. 
- **Mac**: In the resources dialog `META` (Swedish camping ground key) can now be used just like `CTRL` under Windows / Linux. 
- **Editor**: The template function for pure number fields has been fixed. 
- **Domain+Path Support**: Improved support for easydb 6.
- Minor bugs in **CUI layer management** fixed.

### Server

*New*

- **Base configuration**: Individual values of the configuration can be protected with a system right. Available for server plug-ins.
- **Server configuration** is available in custom datatype update plug-ins.

*Improved*

- Transaction runtime when building the **Suggest Index** has been optimized so that there are fewer database commit blockages.

*Fixed*

- **Deletion** of object types with files in Exporter was fixed.
- **Export** of decimal numbers was fixed.
- **Setting the user language** for anonymous logons was corrected.
- **Indexer crash** with inconsistent folder settings was corrected.

*Translated with www.DeepL.com/Translator*
