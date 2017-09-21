# Input


The input, modification, re-creation etc. of data sets is done in easydb in the so-called **Editor**. Depending on where the editor is called from, it is displayed in different sizes. The different sizes differ only slightly in terms of function.

|Editor|Call|File Preview|History|
|--|--|--|--|
|Sidebar|Click on a record from the search result or from the folder preview. |X|-|
|Fullscreen|When using the context menu from the search result and *Lists* in the admin area. |X|X|
|Group Editor|Context menu after selecting multiple records in the search result. |-|-|
|Popover|Little editor accessible from expert search and other editors when searching linked records. |-|-|

The file preview in the editor can be activated and deactivated via <i class="fa fa-picture-o" aria-hidden="true"></i>. It presents all files of a data set (if specified in the mask) in a preview browser. It provides [Zoomer](../../features/datatypes/datatypes.md#tools) and [Office-Viewer](../../features/datatypes/datatypes.md#tools) .

> NOTE: Depending on the data type, there are different types of input fields. More information about this can be found [here](../../features/datatypes/datatypes.md).

Functions in the editor

|Button|Explanation|
|--|--|
|<code class="button">Save</code>|Save the records (New) or updates the records (Group Editor). |
|Mandatory Fields | must be filled in to save. If a mandatory field consists of several fields for multilingualism, it is sufficient to fill in one language (=field). |
|Comment (Checkbox)|If set, a comment is requested before saving, which is then displayed in the history. If provided in the mask, the comment can be obligatory and you cannot uncheck the checkbox. |
|<code class="button">Copy</code>|Open an unsaved copy of the current record for editing as a new record. |
|<code class="button">Delete</code>|Deletes the current record. Note that deleted data records cannot be found in the current easydb version. easydb stores all old versions of the deleted record. |
|<code class="button"> < </code> & <code class="button"> > </code>|Browse to the previous or next hit. When you make a new entry, this jumps back or forth in the left bar. |
|<code class="button">File Preview</code>|Turns the file preview on or off. |
|<code class="button">Change History</code>|Hide the modification history (see below). |
|<code class="button">Mask</code>|Turns the mask, you may have to save it first to avoid losing your data. |


## <a name="history"></a> Change History

![Change History in Full Screen Editor](historie.png)

In the change history, you can display earlier versions of the data record. The system displays who changed the data record and when and the comment, if one has been created.


# <a name="group"></a>Group Editor

In the group editor, you can update up to 1000 data records for an object type at the same time. You can select one or more fields for this purpose. The update per data record is then limited to the specified fields, other fields remain unaffected by the action.

![Group-Editor](editor gruppen.png)

On the left-hand side, you will see the first item in the list, the *Template*. Entries for updates are made in this template. The individual records below the template show the records in the detail view with current data without taking into account the update.

Marked records can be removed from the list with <i class="fa fa-minus"></i>.

Each field has a checkbox on the left. This must be enabled to update this field in the record.

If you click <code class="button">Save</code>, the update process starts.

The input of the fields follows the same rules as for individual data records. For some data types, there are special functions in the group editor:

## Rights Lists

|Settings|Explanation|
|--|--|
|Add permissions|Add permissions adds the newly entered permissions rows per record. |
|Replace permissions|Replaces the specified permission rows per record. Only the user or group is compared. If the who attribute is empty, its rights will be appended to all existing ACL entries
|Remove permissions|Removes the specified permissions rows per record. Only the user or group is compared. If the who attribute is empty, its rights will be appended to all existing ACL entries
|Remove all permissions|Removes all rights lines on each record. |

## Tags

|Setting|Explanation|
|--|--|
|Set tag(s) will be set for each record. |
|Replace tag(s)|The specified tags replace the existing tags for each record. |
|Remove tag(s)|Remove the specified tags. |
|Remove all Tags|All tags in each record will be removed. |

## Multiple Fields

|Setting|Explanation|
|--|--|
|Add to End|Add multiple field rows at the end of each record. |
|Add at the beginning|Add multiple field rows at the beginning of each record. |
|Replace all|Add the multiple field rows to each record, delete all existing records first. |
|Remove when set|Removes multiple fields from the record if the set fields are identical. |
|Remove All|Remove all multiple fields on the record.|

