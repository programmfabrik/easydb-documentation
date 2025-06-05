---
menu:
  main:
    name: "5.144 (June 2025)"
    identifier: "5.144"
    parent: "releases"
    weight: -644
---

> This version **does not require** a new index build

# Version 5.144.0

*Released on 2025-06-04*


# Webfrontend

## Improved
- **Date Fields**: Date fields will now display a placeholder using a format that matches the instance configuration.
- **Detail Sidebar**: Improved the organization of some tool buttons in the detail sidebar.
- **Event Manager**: Improved how object references are displayed in events.
- **Text View Options**: Added display options for the text view in the main search.
- **Default Tags in New Popover Editor**: Improved how tags set in the template object behave in the new popover editor.
- **Not Allowed Object in Hierarchies**: Improved the display of hierarchy levels that the user does not have permission to view.

## Fixed
- **ACL Manager**: Fixed a bug where `undefined` could be shown as a group name in a user/group selector field.
- **Mask Editor**: Fixed an issue with displaying the `condensed_output` option.
- **Read Only Mode**: Fixed an error when trying to open the editor in list view on an instance configured as read-only.
- **Linked Object Expert Search**: Fixed an issue rendering the selection of linked objects when using expert search.
- **Textual Date Ranges**: Fixed issues with date ranges that use textual representation in the editor.
- **Filter Panel**: Fixed a bug that prevented custom data types using the `easydb-library` from working correctly with AND/OR modes in the filter panel. All plugins using this library have been updated.
- **Linked Object Filters**: Fixed a bug that prevented linked object filters from working properly in the linked object search.
- **Linked Object Creation in Metadata Mapping**: Improved the creation of linked objects via metadata mapping.
- **PDF Viewer**: Fixed errors in the PDF viewer within the asset browser.
- **Before Download Message**: Fixed a bug that could prevent file downloads, even when no messages were present to display.
- **Full Screen Detail Zoomer**: Fixed an issue where the zoomer could not be initialized in fullscreen mode using the mouse wheel, if the fullscreen detail sidebar was opened.

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.144.0            sha256:00a801ba9b0f849e49af33991de947b394c19703f4ee993355679e66062825b3
docker.easydb.de/pf/elasticsearch:5.144.0  sha256:ed71b5fdb392b2d920e0305aee8b4e17f68ceb360960abb250fcb166131e03aa
docker.easydb.de/pf/fylr:5.144.0           sha256:71f7fff54cc94a259b826f684909ba94a272bce542e1ba2d25a04106ed5b83c9
docker.easydb.de/pf/postgresql-14:5.144.0  sha256:3be5f7992b463ac4aa6f2a06ea91d9337163e509ee7c60ddb900c070e85992f8
docker.easydb.de/pf/server-base:5.144.0    sha256:e6bb39b78bb166aa0ea77d7cbbdb039507b65e4a899156079188b73007cf8832
docker.easydb.de/pf/webfrontend:5.144.0    sha256:79841286dde3a97c2129f4a29b4948c0fc57bccc2f97f872c89bd3b3a45aa7a7
```
