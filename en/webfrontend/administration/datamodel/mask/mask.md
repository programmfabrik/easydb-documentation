# Masks {#masks}

Masks are used to modify and visibility of fields in data records. A mask is the central tool in easydb for field-related computer management. This is both about the setting which data fields can be changed as well as displayed. Masks can be used to change the order of the displayed fields. You can also specify whether fields are displayed in riders, panels, or grouped for the detailed view and for the editor.

For each object type, at least one mask must be created (the first one is created automatically) and must be defined as the default mask. Only one mask can be defined as the default mask for each object type. The default mask is used to determine which mask is used for display in the search result and detail, in situations where a user has rights for more than one mask (e.g., across different group memberships). If several masks are available, the user can switch between the masks in the detail and in the editor.

## Input and output

![*Mask definition editor*](mask.png)

| Setting | | Explanation |
| - | - | - |
| Name | | Name of the mask. This name is used for communication between client and server and as a fallback if no ad name was assigned
| Description | | Is the display name for the mask, multilingual. Under this name, the user sees the displayed records|
|Comment (internal) || Comment, is only displayed here|
| Standard Mask | | If set, this mask is the default mask. |
| Comment on the <bR> Save or Delete question | | A comment is entered by the user and appears in the change history for others |
| | Off | The user can not enter a comment when saving and deleting |
| | Optional- No | The user can enter a comment, the default is "off". |
| | Optional - Yes | The user can enter a comment, the default is "on", but the user can do without. |
| | Always | The user must enter a comment and can not turn it off
| System Fields: *Hierarchy* | | Only for hierarchical object types
| | Editor | *Modify* - The parent record can be changed in the editor <br> *Show only* - The father record is displayed in the editor but can not be changed <br> *Not displayed* - The father record Is not displayed
| | Output | *Display* - The father record is displayed in detail and in the text view <br> *Not displayed* - Father record is not displayed
| | Mask | The mask is used to determine which fields are taken into account for the parent data record *- unchanged -* The father record is displayed with the same mask we the record itself <br> *Default mask* The default mask is used <br> *<mask>* the specified mask is used
| | Display type | *Standard* - Display in standard view <br> *Text* - Display in text view <br> *Short* - Display in minimal view
| System Fields: *Tags* | | Determines whether tags are displayed in the editor or detail
| | Editor | *Change* tags can be changed in the editor <br> * Show only * tags are only displayed <br> *Do not show* tags do not appear in the editor
| | Output | *Ads* tags are displayed in Detail and Text View <br> *Do not show* tags are not displayed |
| System Fields: *Owner* | | Like Tags. Show the owner. |
| System Fields: *Permissions* | | Like Tags. View the permissions on the record. Permissions are only available if authorizations are set for the object type |
| System Fields: *Maps* | | Like Tags. This is used to determine whether the data records are contained in which folders. A change in the editor is not possible. Only available if the object type is displayed in the main search|
| System Fields: *Pool* | | Like Tags. However, the pool membership is always displayed in the editor and is always changeable (as far as the rights of the user allow). Only available if pool management is enabled for the object type |

## Definition {#definition}

![*Definition of a mask*](mask_definition.png)

| Settings | | Explanation |
| - | - | - |
| Field | | Display name of the field, in the case of separators the display name of the corresponding separator can be defined here |
| Data type | | Data type of the field, only for the overview, no setting can be made here|
| Input and Output | | Only for forward links. Forward links are always displayed as a record. The forward-linked data record can not be modified directly. Data of the linked data record is written to the main data record with the specified mask. Regarding the management of the law, only the right management of the main data record counts. The user automatically gets the right to see the linked data record (within the selected mask) completely |
| | Default mask | The default mask of the linked object type is used for the display |
| | *&lt;Mask&gt;* | Use the specified mask for the linked object type. |
| **Editor** | | |
| Display | | The field is only displayed in the editor and can not be changed |
| Change | | The field is displayed and can be changed |
| Only Attach | | The multiple field allows only one supplement, delete is not allowed. *Only for multiple fields* |
|As Table | | If set, the multiple field is displayed in a horizontal table. If not set, the multiple field is displayed in the main table. *Only for multiple fields* |
| User Notice | | Displayed in the editor and used to help the user how this field is used. |
| **Output** | | |
| Detail | | The field is visible in the detail view and in the expert search|
| Text | | The field is visible in the text view |
| Table | | The field is visible in the table view |
| Default | | Different fields can be included in the standard output. The settings in the pop-up can be used to determine the importance and the design of the fields. Standard output is used wherever records are displayed in an overview (e.g., the "standard" search result), or not much space is required, and overview (e.g., the forward link data sets) |
| | Position | *Do not show* - The field is not displayed in the standard view <br> *Title* - The field is the most important standard field <br> *Subtitle* - The field belongs to the title but is not so Important <br> *Description* - The field has the third highest priority for the display
| | Design of the Text | *normal* - The field will output normally <br> *bold* - The field will be output more fat *thin* -The field will be thinner
| | Separator after output | If several fields use the same position, they are connected or formatted by the specified separator. <br> *space* - space <br> *comma* - comma <br> *semicolon* - semicolon <br> *newline* - new line <br> *brackets* - text is output in {...} < Br> *round-parentheses* - text is output in (...), *square-brackets* - text is output in[...]
| **Search** | | |
| Full Text | | The field is searched in the full text, i. Word suggestions for this field are generated and it is searched in a general full-text search
| Expert Search | | The field is considered in the expert search
| Faceting | | The field is considered in the faceting
| Nested Index | | In a form based on an object type, fields from other object types are included. These are then "nested". A block of a field, which is repeatable, that is, several times. Or a block of several fields that are repeatable together. |
| **Options** | | Advanced options for output in the editor
|| Display in editor | *- Default -* as configured <br> *Hide* - not displayed in the frontend <br> *Read-only* - Read only in the frontend <br> NOTE: To write the field via the API , it must be activated for *Editor*. With the *hide* option, the field is only hidden for the user in the easydb frontend |
||Appearance|*Default* <br>*Text* <br>*Short*|
||Sortierung|*Ascending* <br>*Descending*|
||Condensed output|This Option can be activated to shorten the output of multiple fields. |
||Show in map|Option for fields with files which contain GPS coordinates. The displayof thumpnails on a map can be deactivated/activated for each mask in the detailed view. In general this function needs to be activated in the [Basic Configuration](/webfrontend/administration/base-config/base-config.html#design) first.|
||Always show in detail|This checkbox controls how entries for Yes/No fields (Boolean) are displayed in the detail view. If the checkbox is not activated, the field is only displayed in detail if a value has been set. If the checkbox is activated, the value always appears in detail and indicates whether yes or no is set.|


The mask can be formatted for input and output with so-called separators. Separators can be created or deleted using <code class="button">+</code> and <code class="button">-</code>.

### Separator {#separator}

### Trenner {#separator}

![](seperator_and_detail_de.jpg)
_Left: Seperators in data model, Right: Seperators displayed in detail view_

Separators can be added and removed in a mask via <code class="button">+</code> and <code class="button">-</code>. Some separators consist of two lines that mark the beginning and the end. Corresponding fields are placed between the start and the end line.

|Trenner|Erläuterung|
|--|--|
|Header| The header consists of the system fields, which can be activated for masks via the "Input and output" tab. The header is always displayed at the top of the editor and the detail view. This position cannot be changed. In addition, an info bar appears in the detailed view, which displays the asset ID or optionally a title defined as short information as well as set tags. This info bar is fixed and does not scroll when the detail view creates a scroll bar.  |
|Reitersystem|Felder können in einem Reitersystem angezeigt werden. Für das Reitersystem kann ein Anzeigename vergeben werden, der über den Reitern angezeigt wird. Im Reitersystem muss mindestens ein Reiter angelegt werden, der mit dem Trenner *Reiter* hinzugefügt wird. Es können beliebig viele Reiter in dem Reitersystem angelegt werden. Felder, die unterhalb des Reitersystems angelegt werden, behalten ihre Position über alle Reiter hinweg.|
|Tab|Several tabs can be defined within a *tab system*. The fields for a tab are then placed below the "*tab* separator.|
|Panel|Fields can be grouped within a panel and can be opened and closed as a unit. Panels can be used to organise complex field models. Like the tab system, a panel consists of a header and an end line. The name of the panel is entered in the header line. The fields are created between the header and the end line. By default, the panels are displayed closed. Using the options, the panel for detail view, the editor and the expert search can be set to open by default.|
|Block| Similar to the panel, fields can be grouped as a unit within a block. Blocks cannot be closed, but are dynamic. Several blocks are displayed one below the other in the sidebar. If the sidebar is stretched to the width or the full screen is selected, the blocks glide next to each other. Unklike the other separators, blocks cannot be created within a tab system. | 
| Horizontal seperator| This seperator can be used as a simple subtitle between fields.|
|Without seperator | If not using seperators, all fields are displayed in a block. Unlike panels or blocks, these blocks are not dynamic and are always displayed completely in the editor.|

> NOTE: The position of all separators and fields in masks can be changed by drag & drop. Both the beginning and the end of the separator can be shifted so as to vary the range that the separator defines. This allows the column widths for the input areas to be individually adapted.


## Preview editor

The tab (Tab) shows the preview of the output of the mask in the editor.

## Preview search

The tab (Tab) provides a preview of the output of the records in this mask in different contexts.

Note that for hierarchical object types, several preview options are shown, since these records are displayed partially as paths.

## Preview detail

The tab (Tab) shows the preview of the output of the records in detail.