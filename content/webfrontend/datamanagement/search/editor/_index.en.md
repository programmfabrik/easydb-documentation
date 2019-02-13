---
title: "185 - Editor"
menu:
  main:
    name: "Editor"
    identifier: "webfrontend/datamanagement/search/editor"
    parent: "webfrontend/datamanagement/search"
---
# Input


The input, modification, recreation etc. of records is done in easydb in the *Editor**. The size of the editor can be different, depending on where the editor is started from. The editors works in the same way, except for some functions that are intended for the respective type of editing.

|Editor|Call|File Preview|History|
|---|---|---|---|
|New editor| By clicking on [New records](/en/webfrontend/datamanagement/new_objects) in the main menu or by drag & drop of files from a local server.|X|-|
|Sidebar|Click on a record from the search result or from the folder preview. |X|-|
|Fullscreen|When using the context menu from the search result and *Lists* in the admin area. |X|X|
|Group Editor|Context menu after selecting multiple records in the search result. |-|-|
|Popover|Little editor accessible from expert search and other editors when searching linked records. |-|-|

The file preview in the editor can be activated and deactivated via <i class="fa fa-picture-o" aria-hidden="true"></i>. It presents all files of a data set (if specified in the mask) in a preview browser. It provides [Zoomer](../../features/datatypes) and [Office-Viewer](../../features/datatypes) .

> NOTE: Depending on the data type, there are different types of input fields. More information about this can be found [here](../../features/datatypes).

## Functions in the editor {#editor}

|Button|Explanation|Availability|
|---|---|---|
|<code class="button">Edit</code>|Can be activated and deactivated to switch to the [detail view](../editor)|- Sidebar-Editor (Button) <br>- Context menu in search|
|<code class="button">Save</code>|Saves the record(s) or updates the record(s) after changing or editing fields. The editor closes after saving, when it is used in fullscreen mode.|- Sidebar-Editor (Button) <br>- Full screen editor (Button)|
|<code class="button">Apply</code>|Is currently only available in the simple full screen editor. Saves the changes to the record without closing the editor.|- Full screen editor|
|Mandatory Fields | must be filled in to save. If a mandatory field consists of several fields for multilingualism, it is sufficient to fill in one language (=field).|- Sidebar-Editor <br>- Full screen editor|
|Comment (Checkbox)|If set, a comment is requested before saving, which is then displayed in the history. Depending on whether the comment is optional or mandatory, the checkbox can be activated or deactivated or is grayed out.|- Sidebar-Editor <br>- Full screen editor|
|<code class="button">Copy</code>|Open an unsaved copy of the current record for editing as a new record. |- Sidebar-Editor (Toolbar) <br>- Full screen editor (Button)<br> - Context menu in search|
|<code class="button">Delete</code>|Deletes the current record. Deleted records cannot be found again in easydb. However, old versions of the deleted data record can still be traced by direct access to the database. Currently it is not yet possible to restore them from the database. |- Sidebar-Editor (Toolbar) <br>- Full screen editor (Button)<br> - Context menu in search|
|<code class="button"> < </code> & <code class="button"> > </code>|Appears below the preview for records for which multiple files can be saved. This allows you to browse through the attached files. |- Sidebar-Editor <br>- Full screen editor|
|<code class="button">File Preview</code>|Turns the file preview on or off. |- Sidebar-Editor (Button) <br>- Full screen editor (Button)|
|<code class="button">Change History</code>|Hide the modification history (see below). - Sidebar-Editor (Toolbar) <br>- Full screen editor (Button)|
|<code class="button">Mask</code>|Turns the mask, you may have to save it first to avoid losing your data. |- Sidebar-Editor (Button) <br>- Full screen editor (Button)|
|<i class="fa fa-thumb-tack"> </i>|Use and create templates. If you have saved templates, this menu provides a list of your templates. <br > *Save as template... *: A template is created based on this data record. A dialog opens in which a name for the template is assigned. <br > *Customize*: Change the name of existing templates or delete templates. |- Sidebar-Editor (Toolbar) <br>- Full screen editor(Button)|
|Last Modification |A hint at the bottom of the fields shows when the record has been modified the last time.|- Sidebar-Editor|


The group editor is only available in full screen mode and has some additional functions in addition to the functions of the simple editor. See the section [Group Editor](#groupedit).

> NOTE: Templates can only be saved per user and per object type and/or mask. If a template is supposed to be available to several users, templates must be defined at pool level. Via a pool users have access to general templates and can add them to their own template list.


## <a name="history"></a> Change History

![Change History in Full Screen Editor](historie_en.png)

In the change history, you can display earlier versions of the data record. The system displays who changed the data record and when and the comment, if one has been created.


# Group Editor {#groupedit}

In the group editor, you can update up to 1000 data records for an object type at the same time. You can select one or more fields, then the update for every data record will be limited only to the specified fields, every other field will remain unaffected by this action.

The group editor is available in the context menu, when more than one record is selected. If the selection contains different object types, the context menu provides the option to select the object type.

![Group-Editor](group_editor_en.jpg)

Editing fields in the group editor works similar to all other editors. In addition to the general functions of the editor, the group editor also offers some special functions:

|Function|Explanation|
|---|---|
|Template|Is the first element on the left in the selection display. You can use the template to edit all records that are listed below the template.|
|Ckeckbox|In front of each field there is a checkbox that has to be activated to change it for all records when saving. Each field has different options for adding, replacing or removing entries.  |
|<code class="button"> < </code> & <code class="button"> > </code>|The pagination appears when more than 50 records have been selected for group editing.|
|<i class="fa fa-minus"> </i>| Removes the selected record from the group editor. Only one record at a time can be removed from the group editor. Selecting multiple records is not supported in this mode.|
|<i class="fa fa-clipboard"> </i>|Copies the entries of the selected record to the template.|
|<i class="fa fa-thumb-tack"> </i>|Saves the template. Saved templates are then available in the group editor at this point in the selection menu for new operations. Templates can only be saved per user and mask. See also [Functions in the Editor](/en/webfrontend/datamanagement/search/editor) |
|Chunk size|By default, the data records in the group editor are processed in 1,000 packets. With very complex data models, a timeout can occur in exceptional cases. In this case, the packet size can be reduced to 100 data sets, so that easydb can process smaller packets one after the other. |
|Comment|Offers the possibility to enter a comment when saving. This is displayed in the change history of the data records. |


## Rights Lists

|Settings|Explanation|
|---|---|
|Add permissions|Add permissions adds the newly entered permissions rows per record. |
|Replace permissions|Replaces the specified permission rows per record. Only the user or group is compared. If the who attribute is empty, its rights will be appended to all existing ACL entries
|Remove permissions|Removes the specified permissions rows per record. Only the user or group is compared. If the who attribute is empty, its rights will be appended to all existing ACL entries
|Remove all permissions|Removes all rights lines on each record. |

## Tags

|Setting|Explanation|
|---|---|
|Set tag(s) will be set for each record. |
|Replace tag(s)|The specified tags replace the existing tags for each record. |
|Remove tag(s)|Remove the specified tags. |
|Remove all Tags|All tags in each record will be removed. |

## Multiple Fields

|Setting|Explanation|
|---|---|
|Add to End|Add multiple field rows at the end of each record. |
|Add at the beginning|Add multiple field rows at the beginning of each record. |
|Replace all|Add the multiple field rows to each record, delete all existing records first. |
|Remove when set|Removes multiple fields from the record if the set fields are identical. |
|Remove All|Remove all multiple fields on the record.|

## Boolean (Yes/No-Fields)

Booleans with Yes/No option are set by a checkbox. You can use masks to define how entries of this field type are displayed in the detail view. See the settings in [Options](../../../administration/datamodel/mask) for Yes/No fields.










