# Editor {#editorplugin}

This function is a plugin, which can be added to the basic configuration. Here you can define text that is set as default values when creating new data records or updating existing data records. The plugin is freely available via [GitHub](https://github.com/programmfabrik/easydb-editor-tagfilter-defaults).

![](editorplugin_en.jpg)

| Setting | Detail | Explenation |
| --- | --- | --- |
| Action | Update | The value is set on existing data records. The option only becomes active if a mask has been selected for which tags are defined and at least one tag is set. |
|  | Insert | The value is set for new data records. |
| Masks |  | Selections of masks for which the value from the default is to be set. |
| Show Replacement |  | Selection of possible replacements which can be used in the default text to refer to a specific value. Example: If the field Copy Rights is supposed to reference on the photographer, it is possible to set a default value for the photographer using a replacment. |
| Tag filter |  | The default value can be linked to tags and is set when a data record receives the corresponding tag. The prerequisite is that tags are defined for the object type. For updates to existing records, a tag is mandatory. For new records a tag is optional. Note: If you want a default value to apply to an object type with several masks, this setting must be made individually for each mask. |
| Default | Type | Default values wich are set automatically in a field when a data record is created or updated. Currently only the type _Default_ is available. |
|  | Field | Field to the value applies. Depending on the selection of the mask, corresponding  fields appear in the selection. |
|  | Value | Here you can enter a text, a replacement or a combination of both. |



