---
menu:
  main:
    name: "5.47"
    identifier: "5.47"
    parent: "releases549"
    weight: -547
---

> - Versions **5.47.0** or higher require re-indexing, schedule the time for the update accordingly.
> - Performance optimizations for selection, detail and editor. The **Edit** button has been moved to the three-point menu.
> - The call parameters for **fylr** have been changed. Please have a look at **fylr -help** for more information.
>

# Version 5.47.3

*Published on 06.03.2019*

### web frontend

*Improved*

- **Presentations**: It is now possible to move slides from one page to another (context menu). New slides are inserted before the currently selected slide.

*Fixed*

- Editor: **Copying of objects** was repaired. This has been broken by performance improvements in 5.47.0.
- Search: The expert search for **failed versions** (previews) did not work correctly in all cases.
- Data model: Deletion of rows in read-only mode was disabled (saving was not possible).
- Exporter: In some complex searches the export menu could not be opened.

### Server

*Fixed*

- **Single sign-on** (e.g. with Shibboleth) has not removed the user from the anonymous user group if the user was previously in this group through an automatic or manual anonymous sign-on.

# Version 5.47.2

*Published on 04.03.2019*

### Web frontend

*Improved*

- Select all is now disabled for search results with more than 1000 hits.
- Printing under Chrome has been improved for some cases.

*Fixed*

- Copying from the editor was repaired.
- Reset in modal searches was repaired.
- Export with more than 1000 hits was repaired.
- The search for file types in the expert search was restored.
- Switching of masks in export has been improved, so that you don't have to load twice anymore.

# Version 5.47.1

*Published on 28.02.2019*

### Web frontend

*Fixed*

- Calling the group editor in the context menu was broken in some cases after the performance improvements.

### Version 5.47.0

*Published on 27.02.2019*

### Web frontend

*New*

- Search: Sort by original filename added.
- Series & version recognition also in folders & hotfolders.
- Quick display: Display in detail for objects is now possible via the context menu.
- Plugins: An **AssetDetailPlugin** can now start automatically.
- Connector: Support for sorting.
- New option for option to embed linked records in deeplink.
- New basic configuration to not store personal data in some events.

*Improved*

- Performance improvements in selection, display in detail, and loading in the editor for objects. We had to remove the **Edit** button in detail. This button is now hidden in the three-point menu. The necessary rights checks are now only performed when clicking on this menu and also when clicking on the context menu.
- Zoomer: Displays the current zoom level in percent.
- Print: More setting options in the print menu. 
- Folders are now expanded in the tree when they are displayed.
- Improved keyboard support for menus and other selections.
- Performance when building presentations has been improved.

*Fixed*

- Poolmanager: The removal of the contact was repaired.
- Full screen display: Fixed jumping to the correct preview.
- Search by preview status was repaired for some combinations.
- Search: Entering spaces after quotation marks no longer causes an error.
- Detail/Editor: The selection of the mask for displaying linked objects was not correct in some cases, especially with newly created objects.
- When selecting objects, the detail is now updated only if there is currently only one object in the selection.
- Connector: Fixed several searches.

### Server

*New*

- New basic configuration not to store personal data in some events.
- New option for option to embed linked records in deeplink.
- `_created` metadata field in objects.

*Improved*

- Output of `_system_object_id` for reverse-linked objects in XML export
- Non-configured languages are no longer output in the export.
- Blacklist for table names in the data model to prevent index problems.
- Serial image support in the hotfolder analogous to the web frontend.
- Verification of custom type data when saving according to mapping.

*Fixed*

- Saving in group mode now uses database logic to check UNIQUE.

- System right `system.datamodel` with level `commit` also allows level `development`.
- Fixed confirmation process when deleting linked objects.
- Download filename corrected in some cases.
- The position field in basic configuration description is enforced. This has
  Effects on plugins that extend the configuration.
- ID & default info for linked assets always in XML export.

### Fylr

*New*

- GZIP support for **/objectstore.**
- *fylr apitest* is now a [**standalone tool**](https://github.com/programmfabrik/fylr-apitest/) under open source license.
- TLS/SSL support. 

*Improved*

- **/zip** now works faster (parallel) when checking if all URLs are reachable.

*Fixed*

- A cache header problem related to ETag has been fixed.

*Translated with www.DeepL.com/Translator*