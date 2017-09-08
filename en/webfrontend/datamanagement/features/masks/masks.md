# Masks

Masks are used to control the changeability and visibility of fields and data sets. A detailed description can be found under [Administration > Masks](../../../administration/datamodel/datamodel.md#mask).

At least one mask must be defined for displaying fields and records. This is the **default mask**. It is possible to define several different masks and to assign them to an object type.

## Mask filter

If additional masks and tags are assigned to an object type next to the default mask, it is possible to control their availability via filters. The setting for this is made under object type configuration in the "input and output" tab.

Application example: The "Internal" form (defined as the default mask) and "External" are assigned to the "Document" object type. Tags are also defined for the object type. A tag is called "released". This day receives a filter function and activates the mask "External". Only if an object type is marked with this tag, it can be displayed with the "External" form. Without the tag, the object type is only displayed with the default mask "Internal".

## Mask preference

For masks, a **sequence** can be defined. This expresses the preference of the masks.

For object types that are not managed via pools, the order in the setting area for the data model is set in the "Input and output" tab.

For object types managed by pools, this configuration can be performed at pool level. This can be done on the left in the navigation at the parent level for "All pools" or per pool by selecting a pool. The list of object types can be found in the "Masks" tab. The masks are also listed for each object type. By activating the checkbox, the configuration of the higher-level pool is accepted. If the checkbox is not active, you can overwrite it. The order of the masks can be changed or even masks can be completely blown out. Below each mask list is a horizontal line. Also the position of this line can be changed. Masks that are above the line are indexed and displayed to the user for the pool. Masks that are below the line are not indexed and the user is not displayed for the pool.

## Administration and preferred mask

The availability of the masks for users can be controlled via the [Computer management](../../../rightsmanagement/rightsmanagement.md).

However, the control over tag filters and mask configurations for pools has priority over the correct management. This means that the assignment of the availability of a mask to a user remains ineffective if the tag mask or mask configurations are active on the pool with which the mask is not displayed.

In the case of the above- Example of the "Internal" and "External" masks for the "Document" object type can be as follows:

    User "Guest" has `mask` right for 'External'
    User "Agent" has `mask` right for 'External' and 'Internal'

If the tag "released" is set for record A and not for record B, the following is the case:

    "Guest" only sees A (mask "External")
    "Processor" sees A (both masks) and B (only "Internal")

If several masks are available to a user, the preferred mask is placed first in the selection. The preference, and thus the order of the mask selection, is performed by the configuration on the object types and pools (see "Mask preference"). If the sequence is not adjusted, the default mask is placed at the preferred location.

The "Default Mask" assignment is a property for masks, which is assigned via the management of the rights. This feature is not singular, but can apply simultaneously to multiple masks. If a user who has access to several object types / pools is assigned the right "standard mask", this means that he sees the respective preferred form for an object type or pool. It is a dynamic right. If the configuration of the mask is changed to the object type or pool, the user sees a different mask even though his right "standard mask" has not changed.

The search results are displayed with the preferred form. In the detail view, the user can switch between the different masks available to him.