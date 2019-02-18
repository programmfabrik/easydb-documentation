---
title: "Asset detail plugin"
menu:
  main:
    name: "Asset detail plugin"
    identifier: "technical/plugins/reference/webfrontend/asset-detail-plugin"
    parent: "technical/plugins/reference/webfrontend"
---

# Asset detail plugin

Custom tools for the Asset Browser. 

Examples:

- [ExampleAssetDetailPDF](https://github.com/programmfabrik/easydb-plugin-examples/blob/master/src/webfrontend/ExampleAssetDetailPDF.coffee)
- [ExampleAssetDetail3D](https://github.com/programmfabrik/easydb-plugin-examples/blob/master/src/webfrontend/ExampleAssetDetail3D.coffee)


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

Returns `@outerDiv`, which is the container of the asset.

### createMarkup()

### start(@asset, @mouseWheelstart = false)
