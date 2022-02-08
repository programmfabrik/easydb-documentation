---
title: "Export manager plugin"
menu:
  main:
    name: "Export manager plugin"
    identifier: "technical/plugins/webfrontend/types/export-manager-plugin"
    parent: "technical/plugins/webfrontend/types"
---
# Export manager plugin

Export manager plugins are a kind of template where it is possible to create an own form with different options to make the export feature simpler or complex, depending on our needs.

To create a new export manager plugin, it is necessary to extends the class **ExportManagerPlugin**, implement the following methods and register it.

```coffeescript
class MyExportManagerPlugin extends ExportManagerPlugin
    # ... methods implementations

ez5.session_ready =>
    ExportManager.registerPlugin(new MyExportManagerPlugin())
```

After the plugin is implemented and registered, an option will be shown in a dropdown at top right of the export manager modal.

### Methods to implement

- name() : `String`
    - An unique string to indicate the name of the implementation.
- nameLocalized() : `String`
    - This is the name that will be shown.
- renderForm() : `HTMLElement` / `CUI.DOMElement`
    - This is the element that will be rendered in the middle of the modal, it's supposed that this element has to contain a form.

### Optional methods available to override

- getExportData() : `PlainObject`
    - This object contains the data that will be saved as 'export data' when the *Export button* is clicked. It returns *@_export.getExportData()* as default.
- saveAllowed() : `Boolean`
    - This value indicates whether it's allowed to export or not. It returns *true* as default.

### Available attributes
- exportManager `ExportManager`
    - This is the instance of `ExportManager` which is using the plugin.
- export `Export`
    - This is the instance of `Export` which is being used.
- EASColumnsInfo `PlainObject`
- onClose `Function`
