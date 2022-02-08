---
title: "Custom data types"
menu:
  main:
    name: "Custom data types"
    identifier: "technical/plugins/webfrontend/types/custom-data-type-plugin"
    parent: "technical/plugins/webfrontend/types"
---
# Custom data types

With custom data types is possible to create new data types and they are 100% customizable depending on what we need to do.

To use them It's necessary to extends the class **CustomDataType**, implement the following methods and register it.

```coffeescript
class MyCustomDataType extends CustomDataType
    # ... methods implementations

CustomDataType.register(MyCustomDataType)
```

### Methods to implement

- getCustomDataOptionsInDatamodelInfo(customSettings `PlainObject`) : `String ArrayList`
    - The strings in this array will be the labels that will be shown below the 'Check' button in the datamodel.
- getCustomDataTypeName() : `String`
    - Unique name to identify the data type.
- renderEditorInput(data `PlainObject`) : `HTMLElement` / `CUI.DOMElement`
    - It is the content that will be shown in the editor.
- renderDetailOutput(data `PlainObject`) : `HTMLElement` / `CUI.DOMElement`
    - It is the content that will be shown in the detail.
- getSaveData(data `PlainObject`, saveData `PlainObject`) : `PlainObject`

### Optional methods available to override

- getCustomDataTypeNameLocalized() : `String`
    - It is the name that will be shown in the data types list.
- getCustomSchemaSettingNameLocalized() : `String`
- getCustomMaskSettingNameLocalized() : `String`
- getCustomSchemaSettings() : `PlainObject`
- getCustomMaskSettings() : `PlainObject`
- isVisible(mode `String`, options `PlainObject`) : `Boolean`
    - It returns a boolean that indicates whether the field has to be shown or not.
- renderFieldAsGroup() : `Boolean`
    - It returns a boolean that indicates whether the field has to be rendered as a group or not.
- renderCustomDataOptionsInDatamodel(customSettings `PlainObject`) : `HTMLElement` / `CUI.DOMElement`
- hasUserData(data `PlainObject`) : `Boolean`
