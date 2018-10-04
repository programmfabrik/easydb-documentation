---
menu:
  main:
    name: "5.39"
    identifier: "5.39"
    parent: "releases"
    weight: -539
---

# Version 5.39.2

*Released Sep 10th 2018*

### Server

*Fixed*

* **/api/suggest** sends smaller packages to Elasticsearch during index building and avoids a previously invisible error which could lead to the index not being available in more complex data models and resulting in no suggestions being available.

### Web frontend

*Fixed*

* The **Pool Manager** ignores object types that are no longer assigned to a pool correctly and allows you to save the settings.

*New*

* The Custom Data Type plugin **gazetteer**(Beta) is enabled per default. For more information visit [iDAI.gazetteer](https://gazetteer.dainst.org/app/#!/home).

# Version 5.39.1

*Released Sep 5th 2018*

### Server

*Fixed*

* **/api/suggest** fixed errors with **fields** parameter
* **/api/search** fixed for users without explicitly defined search language
* Compiler Fix for older versions of GCC

*Improved*

* **/api/eas/rput** returns an error code, if the remote file was not found

### Webfrontend

*Fixed*

* Suggestions in expert search fixed for some case
* Improved design and quality of suggestions
* Search for **#SystemObjectId** was broken and is now fixed again
* File previews in the new objects dialog are displayed as soon as they are ready

# Version 5.39.0

*Released Aug 30th 2018*

#### Please note:

1. This release needs to a full re-index, please consider appropriate update times
2. Check you metadata mappings and correct them as needed. In some cases, you need to re-created the mapping in order for all fields to update properly.

### Server

* New implementation for **/api/suggest**: Previously, aggregations were used to find suggestions for the search. This procedure was too slow for large indexes and required too much memory. In the new procedure, a suggest-index is set up in parallel at fixed times in which word proposals are searched for. By default such an index is built every 2 hours in the background. 
* Fixed **/api/search** to search for self-linked objects.
* Fixed CSV export for custom data types
* **/api/mask**: New mask setting used_for_linked_object_display
* Fixed CSV export of many events
* Error when saving object rights fixed
* Error with special characters in Facet-Terms fixed

### Webfrontend

*Neu*

- Custom Data Type: New method **isPluginSupported** that specifies whether a plugin should be loaded in the detail view for this type or not
- New mask option: **Hide mask in detail view**
- New mask option: Display **tags** of linked objects
- Custom Data Type: If a custom data type has not been loaded, a JSON browser is displayed in the detail view to display the saved data
- Text fields: If a text field contains valid JSON, a JSON browser is output to display the data
- New system right **script_runner**. This allows to explicitly allow ScriptRunner for users, until now this was only visible for users with the **root** system right
- Connector: Support for download via Connector (Beta)
- Connector: Improved configuration for Connector (Beta)
- Developer menu: Support of a remote URL to load plugins from a foreign server
- Date picker: Display of week numbers and days

*Improved*

- Large folder trees (>100 folders) are now displayed in groups of 50 to improve loading times and provide a better overview
- JSONImporter: eas_type and eas_replace_url can be defined in Manifest.json
- Display of search results for missing previews has been accelerated
- Datamodel: Display of the current HEAD version after saving in the tooltip
- Metadata mappings: New profiles with improved mappings

*Fixed*

- Fixed mask preview in mask editor for email fields

- Fixed tag filter preview in many input masks
- Fixed performance problems when starting databases with many date fields in the filter