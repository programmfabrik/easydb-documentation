# Preferences for Share

The easydb administrator can pre-define profiles for permissions using the **Preferences** settings. Users have these predefined permissions to share *records* and *folders*.

> NOTE: Users who do not have the system privilege *allow_custom_enabled_in_preset_enabled_acl* or *root* can access access privileges for *folders* and *records* from only these predefined permissions and grant them to other users. It is therefore important that these users are set up preferences.

Presets include *permissions* and, if necessary, *tag filters*. Which permissions and tags are available depends on the context (*folder* or *record*) and after the individual configuration of your easydb.

[Overview of possible rights settings in easydb](../#rights)

## Set up preferences for sharing (easydb admin)

![Preferences](voreinstellungen allgemein.png)

Select *Presets* from the menu under Compute Management. Then select the context (*folder* or *record*) for which a profile with predefined authorizations should be created.

Already created presets are displayed in a *list*. Use <code class="button">+</code> and <code class="button">-</code> to add new presets or delete existing ones. You can change the order of the presets in the list by drag & drop. The new order is saved immediately, and users are sorted accordingly.

## Editor

In the *Editor* (as in the screenshot above), the newly added or selected existing preset for editing appears.

### General

| Field | Description |
| - | - |
| ID | Automatically assigned by saving easydb. |
| Name | The name of the preset as it appears in the pull-down menu. Multilingual. |
|Description |A description of what the default is. The user sees this description as a tooltip|

> NOTE: Note that the <code class="button">Save</code> of a new default must have at least the name and an authorization under the *Permissions* tab.


### rights

In the *Permissions* tab you will find the rights configured for the default setting. You can find the list of rights [here](../#rights).

![Permissions](voreinstellungen rechte.png)

### Tag filter

In the *Tag filter* tab you will find the tag filters configured for the default setting. You can find an explanation of the tag filters[here](../#tagfilter).

> NOTE: Note that here you have access to all tags, but if necessary, by configuring in the [object type](./objecttypes/objecttypes.md) or [pool](./pools/pools.md), fewer tags are available to the Tagfilter apply.

![Tagfilter](voreinstellungen tagfilter.png)