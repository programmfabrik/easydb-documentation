# Collections

## Create and delete collections

A folder can be created in the quick display via the <code class="button">+</code>. Marked records can then be dragged from the hit display into the folder by drag & drop. A folder can also be created from the hit display. The context menu for selected records is called. With <code class="button">-</code> a marked collection can be removed again.


## Detail view for collections

![](finder_context_en.jpg)

Below the dynamic searches you find your own collections and collections shared by other users. By clicking on <i class = "fa fa-chevron-right"> </i> *My collections* or <i class = "fa fa-chevron-right"> </i> *Shared collectins* you can hide or show all collections. Hold the `Ctrl` key at the same time, than also all hierarchically subordinate collectiona open. By clicking on a collection, the records in this collection are displayed on the right in the detail view for collections. Double-clicking on a record opens the detail view for the record to the right. Above the detail view for the collection you finde a toolbar. With the split button <i class="fa fa-columns"></i>, the main [search](../../find/find.html) opens next to the detail view for the collection.

> NOTE: The sequence of the records in the collection can be changed with drag & drop.

### Functions {#functions}

Right-clicking on a collections opens the context menu with functions, which can be used to modify the collection. If you select one or more records from the collection and than right-click on the mouse, you will access a context menu with functions to modify the marked records. This functions can also be accessed via the toolbar above the detail view for the collection.

![](collectionsplit_context_en.jpg)

The following functions are available for records ij collections using the context menu:

|Function|Context Menu| Description |
|---|---|---|
|**For collection**|||
|![Select](select_all_button.png)|Select all|Selects all records in the collection|
|<i class="fa fa-search"></i>|Show in search | Creates a search element in the search and displays the contents of the collection as a hit. The search can be further extended by further search elements.|
|<i class="fa fa-arrows-alt"></i>|Activate full screen | Displays the content of the collection in easydb fullscreen mode.|
|<i class="fa fa-expand"></i>||Available in full screen mode. Opens the view as a full screen browser.|
|<i class="fa fa-download"></i>| Download...|Save the data from the collection locally. This opens the selection menu dialogue to choose the download settings. |
|<i class="fa fa-sign-out"></i>|Export...|Open the  [Export-Menu](../../../features/export/export.html) to export the collection.|
|<i class="fa fa-print"></i>| Print...|Opens the print dialogue for all of records in the collection. For printing, the detail view or text view and a high or low resolution can be selected. |
|<i class="fa fa-share"></i>|Share...|Open the [Share-Menu](#share) for the collection. This may allow other easydb users to interact with the collection. Shared either through email of hyperlink.|
|<i class="fa fa-newspaper-o"></i>|Presentation...|All the data from the collection will be loaded.|
|<i class="fa fa-files-o"></i>|Copy collection|Content is copied including presentation, if attached. Share and upload settings are not copied.|
|<i class="fa fa-plus"></i>|New collections| Create a new collection. When currently in a collection, this will create a sub collection.|
|<i class="fa fa-cogs"></i>|Settings... |Open the [Settings](#settings) for the collection.|
|<i class="fa fa-pencil-square-o"></i>|Rename|Change the name of the collection.|
|<i class="fa fa-minus"></i>|Delete collection...|Delete the  collection. The records in the collection will not be deleted, and remain searchable in easydb.|
|**For selections**||This options appear if records in the collections are selected.|
|<i class="fa fa-arrows-alt"></i>|Activate full screen | Displays the selected records in full screen mode.|
|<i class="fa fa fa-folder-open-o"></i>|Selection in collection | Create a new collection with the marked records.|
|<i class="fa fa fa-minus-circle"></i>|Remove %(count)s record(s)|Removes the selectod records from the collection. Records are still available in easydb.|
|<i class="fa fa-download"></i>| Download...|Opens a menu to choose the download settings and to save the selected records from the collection locally. |
|<i class="fa fa-sign-out"></i>|Export...|Opens the  [Export-Menu](../../features/export/export.html) to export the selected records from the collection.|
|<i class="fa fa-print"></i>| Print...|Opens the print dialogue for the selected records in the collection. For printing, the detail view or text view and a high or low resolution can be selected. |
|<i class="fa fa-pencil"></i>| Group editor |Opens the group editor to modify the selected records. |
|<i class="fa fa-trash-o"></i>| Delete records... |Removes the records from easydb permanently. The records won't be available anymore. |


## Share collections {#sharecollection}

A collection can be shared with other users. This includes:

* Users with an easydb login
* A whole easydb group
* Users who do not have their own easydb login can be invited by e-mail
* Anonymous sharing via hyperlink

![Share collection](share_collection_en.jpg)

> NOTE: Shared collections also have an effect on all subordenate collections, if the option *Ignore superordinate permissions* is not activated.


| Function | | Description |
| - | - | - |
|<i class="fa fa-plus"> </i>  |"User / Group / E-mail| Creates a new release for this collection. Select the user, group, or email for which you want to release the collection. If you enter an e-mail that is not yet stored in the easydb, you have the option to create a new user for this e-mail. In that case, you must also define the language for this user. |
|||Share a collection with the system group *Anonymous User* for unauthenticated access to the released content. This user group must be configured in the rights management. Using this option the content is displayed for users without log in. The link can be used for passing on. The content is also accessible without the link.|
| | Create link for external access | For this type of sharing content a pseudo-user with a cryptic ID is created and a link is generated. The released records can only be accessed via this link. Unauthenticated access to this folder enables the user to access the shared data without having to log in or registered email. The link must be forwarded manually, e. g. by email or otherwise, to the addressee. Click <i class="fa fa-share"> </i> to display the link and copy it for distribution. |
| <i class = "fa fa-minus"> </i> || Removes the share. You must first select the appropriate line. |
| Permission presets|| The pull-down offers a list of permissions, which is granted for this release. These permissions are set by the easydb administrator in [presets](../../../rightsmanagement/presets/presets.html). The name of the permission is displayed, but the detailed settings are not visible. For each permission preset, the administrator can define an explanatory text that appears as a *tooltip*, if you hold the mouse pointer a little bit longer over the respective permission.|
| End || Schedule for releases. Enter the date on which you want the release to end. The date can also be specified with a time. The input is made without separators in the format dd.mm.yyyyy & hh:mm (00:00-23:59), e. g. *12.12.2012 12:12*. |
| E-Mail || If set, the user or the group is informed by e-mail about the release. You can add a personal message in the expert menu. Note that this e-mail is sent after you have saved. When the *Sharing-Popover* is called again, the checkbox will be blank. So you have the possibility to send an e-mail again |
| <i class="fa fa-share"> </i> || Generated link. For releases of the type "Generate link for external access", the shared records can only be accessed via this link. For other types of sharing, the link can be used optionally. The share settings must always be saved before the link is copied. |
| <i class="fa fa-bars"> </i> || Access to expert popover (see next section) for individual permissions. |


> HINT: Releases also affect all subordinate collections if *Ignore permissions of superordinate collections.* is not activated. The release settings must be saved before copiing the link for further use.


### Expert pop-up for releases

You can add custom permissions in the expert pop-up. Click <i class = "fa fa-bars"></i> to open the expert pop-up.

![](sharecoll_permissions_en.jpg)

| Setting | Description |
| - | - |
| Active | If set, the enable is active. Use this checkbox to de-activate a share temporarily. Users are not informed about this process
| Users / Group / E-Mail / Anonymous | This is where the share applies. In the case of anonymous releases, a hash key appears which has no further meaning and is used to secure the access
| Start | Time when a share becomes active. If not set, the enable is active immediately after saving. |
| End | Time to when a release remains active. If not set, the enable is always active
| Persistent | Mappings can be ignored with the * Ignore right-hand lines of superordinate folders * Declare your own releases. If you set * Persitent *, this setting can not be de-activated in subordinate folders even by this setting
| Link to Share | For anonymous releases, a link will be displayed here. Click on <code class="button">Goto</code> to try the link in a new browser window
| Right | Select the right here (see[Share])


> NOTE: If you have the system right *root* or *allow_custom_enabled_in_preset_enabled_acl*, the [Rights](../../../rightsmanagement/rightsmanagement.html#rights) are displayed in detail.


## Settings

The settings dialog is the same as for sharing, only the tab *General* is active.

### General

General settings for the folder are available on this tab.

| Setting | Description |
| - | - |
| Display name | Ad name of the folder. Multilingual. |
|Description | Description of the portfolio. Multilingual. Displayed to user when viewing folder in folder view|
| Link to this folder | The deep link to this folder. Use the link if you want to create a bookmark for yourself on this folder or give someone a link which also has access to this folder


### Uploading (Hotfolder)

Collections can be used to load files directly into the easydb. To do this, you can configure a collection as a **hot folder**. The settings here affect all subordinate folders. They can be changed in the subordinate folders but can not be switched off.

> NOTE: Files can be dragged from your computer to the collection (within the overview) or to the detail display of the collection. The files are copied to the easydb during this process. The original file remains on your computer.

Since the easydb works with a flexible data model, you must configure in which object type, pool, and in which field the uploaded files should land. An import mapping can be configured. In order to start a workflow, you can also assign the predefined tags to the data records.

> NOTE: One record is created for each uploaded file. Collections that are configured for the upload appear with an upload icon <i class = "fa fa-upload"></i>.

| Setting | Description |
| - | - |
| Object type | The object type for which the record is created. |
| Pool | The pool to which the record is linked. |
| Mask | Select the mask to specify a field to link the file to
| Field | Select the field to which the file is linked. This also supports the import of [serial images and versions](../../new_objects/new_objects.html#batch)
| Mapping | The mapping used for the import. |
|Tags |Specify the *tags* that are set for the newly generated record |



