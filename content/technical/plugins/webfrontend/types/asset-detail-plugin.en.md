---
title: "Asset detail plugin"
menu:
  main:
    name: "Asset detail plugin"
    identifier: "technical/plugins/webfrontend/types/asset-detail-plugin"
    parent: "technical/plugins/webfrontend/types"
---

# Asset detail plugin

Custom tools for the Asset Browser. 

Example: [360 image viewer plugin](https://github.com/programmfabrik/easydb-360-viewer-plugin)

### getButtonLocaKey(asset)

Returns the loca key of the button.

If it returns **undefined**, the tool button won't be rendered.

### startOnMousewheel() : Boolean

If it returns **true** the method `start` is triggered after the event `wheel` is triggered in the Asset browser.

It returns **false** as default.

### startAutomatically() : Boolean

If it returns **true** the method `start` is triggered after the AssetBrowser is loaded.

It returns **false** as default.

### getAsset()

Returns `@asset`

### getOuterDiv()

Returns `@outerDiv`, which is the container of the asset browser.

### start(@asset, @mouseWheelstart = false)

This is the most important method that needs implementation and it is invoked when the user clicks on the plugin's button.

Use the `@outerDiv` as container to add all the necessary implementation. 

### createMarkup()

It can be implemented optionally and it can be used to prepare something before starting the view.