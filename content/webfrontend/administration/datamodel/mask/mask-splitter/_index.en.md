---
title: "Splitter"
menu:
  main:
    name: "Splitter"
    identifier: "webfrontend/administration/datamodel/mask/mask-splitter"
    parent: "webfrontend/administration/datamodel/mask"
---
# Splitter

In masks, so-called separators can be used to structure the fields, for example in tabs or panels. Individual separators can also be used to integrate additional functions into masks (see "Plugin separators").

Some separators consist of two lines that mark the beginning and the end. Related fields are placed between the start and end line.

> NOTE: The position of all separators and fields in masks can be changed by drag & drop. Both the beginning and the end of the separator can be moved to vary the range defined by the separator. This allows the column widths for the input areas to be adjusted individually.



## Standard-Splitter

Tabs, panels, blocks and horizontal dividers are available as standard.



### Tab system with tabs

Fields can be displayed in a tab system. A display name can be assigned to the tab system, which is displayed above the tabs. At least one tab must be created in the tab system. This tab is added with the tab separator. Any number of tabs can be created in the tab system. Fields that are created below the tab system retain their position across all tabs.

Several tabs can be defined within a tab system. The fields for a tab are then placed below the tab separator.



### Panel

Fields can be grouped within a panel and can be opened and closed as a unit. Panels, like tabs, can be used to arrange complex field models more clearly. Like the tab system, a panel consists of a header and an end line. The name of the panel is entered in the header line. The fields are created between the header and end line. By default, the panels are displayed closed. You can use the options to set the panel for the detail view, the editor and the expert search to open by default.



### Block

Similar to the Panel, fields within a block can be grouped as a unit. Blocks cannot be closed, but they are dynamic in appearance. Several blocks are displayed one below the other in the sidebar. If the sidebar is dragged to the width or the full screen is selected, the blocks slide next to each other. Unlike the other separators, blocks cannot be created within a tab system.



### Horizontal separator

This separator is a simple subheading between fields.



## Plugin-Splitter

Further separators can be added via individual plugins. 



### Barcode

This separator can be used to generate a barcode.



### Display field values

The plugin display-field-values is available on [Github](https://github.com/programmfabrik/easydb-display-field-values) and installation instructions can be found [here](../../../../../../en/sysadmin/configuration/easydb-server.yml/plugins/display-field-values/). 

The following options are available:

| Option                                     | Description                                                  |
| ------------------------------------------ | ------------------------------------------------------------ |
| Field width                                | Select whether the output of this mask splitter should take up the full width in editor and detail, or only 25, 50 or 75 percent. |
| Output                                     | Enter the text to be displayed here. You can use markdown syntax to format the text and insert links. You can use placeholders, such as %title%, to access the contents of free text fields. If you are using content in a URL, please choose the replacements with :urlencoded (e.g. %titel:urlencoded%). |
| Hide text if no replacements are available | Activate this checkbox to hide the complete text if no replacements are available (e.g. if a used field has no content). Otherwise, the text will still be displayed (e.g. if the "Title" field is not filled in, the output of "This is the %title%. only "This is the." would be displayed). |
| Also render field values as markdown       | Activate this checkbox if the content of a field already contains Markdown syntax and you want it to be rendered as Markdown. Otherwise, the field content is output as text. |



### Hijri to Gregorian converter

This plugin converts Hijri dates to Gregorian calendar dates.



### Display of References

The plugin custom-mask-splitter-detail-linked is available on [Github](https://github.com/programmfabrik/custom-mask-splitter-detail-linked) and installation instructions can be found [here](../../../../../../en/sysadmin/configuration/easydb-server.yml/plugins/custom-mask-splitter-detail-linked/).

With the help of this plugin, all entries of other object types that refer to a record can be displayed automatically in the detail view of that record. For example, if you have tagged images with keywords, you can see in the detail view of each keyword which images are linked to it. 

The following options are available:

| Option      | Description                                                  |
| ----------- | ------------------------------------------------------------ |
| Field Width | Choose whether the field should occupy 100%, 75%, 50% or 25% of the width in the detail view. |
| Mode        | Choose whether to display the entries in standard, text or short format. |
| Objecttypes | Select the object types whose links should be displayed.     |

