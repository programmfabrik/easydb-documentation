---
title: "Web frontend"
menu:
  main:
    parent: "technical/plugins/reference"
    identifier: "technical/plugins/reference/webfrontend"
---

# Web frontend Plugins

This overview shows all possible hooks for register custom code inside the Web frontend. Each section mentions at least one example Plugin where such custom code is used and can be found.

### ez5.rootMenu.registerApp

* Server-Status

### ez5.tray.registerApp

* ExportManagerList

### TransportsEditor.registerPlugin

* FTP

### BaseConfig.registerPlugin

* Example

### Presentation.registerDownloadManager

* Presentation-PPTX

### DetailSidebar.plugins.registerPlugin

* HierarchyDetail

### AssetBrowser.plugins.registerPlugin

* Example

### TransitionAction.registerAction

* TransitionActionEmail

### ExportManager.registerPlugin

* EasydbExport

### MaskSplitter.plugins.registerPlugin

This plugin allows custom code to be injected into the fields rendering in Detail, Editor, and Text-Result. Two kinds of plugins are provided, one is simple content without inner fields, the other can be used to wrap inner fields (think `<fieldset>`). The design and output of the injected DOM Nodes are entirely up to the plugin. The method `renderFields(opts)` gets all relevant render environment information inside `opts`, e.g. the current `data`which is rendered, or the instance of the `Editor`or `Detail`. 

- Example

#### Classes

* **CustomMaskSplitter.coffee**
* CustomMaskSplitterEnd.coffee
* CustomFieldsRenderer.coffee

### Callbacks

* ez5.load_defaults
* ez5.session_ready

