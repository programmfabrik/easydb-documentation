---
title: "Custom mask splitter"
menu:
  main:
    name: "Custom mask splitter"
    identifier: "technical/plugins/webfrontend/types/custom-mask-splitter-plugin"
    parent: "technical/plugins/webfrontend/types"
---

# Custom mask splitter

Mask splitters are extra separators or groupers for masks. They work like `Tabs` or `Panels` and they can be `Simple` and `Block`.

The `Simple` mask splitters does not contain fields within (like the `Horizontal separator`), `Block` ones do (like `Panels`).

Examples:
- [Block](https://github.com/programmfabrik/easydb-example-plugin/blob/master/src/webfrontend/ExampleMaskSplitterBlock.coffee)
- [Simple](https://github.com/programmfabrik/easydb-example-plugin/blob/master/src/webfrontend/ExampleMaskSplitterSimple.coffee)

### isSimpleSplit() : Boolean

It needs to return **true** if the custom mask splitter is `Simple`, otherwise it will be `Block`. Default is **false**

### isEnabledForNested() : Boolean

It needs to return **true** when inner fields can be nested, otherwise return **false**. The custom mask splitter needs to be `Block`. Default is **false** 

### getOptions() : Array<DataField>

It is possible to return options that can be used to change the behaviour of the mask splitter. Each option needs to be a DataField object (of CUI). The default is **[]**

### getDefaultOptions() : PlainObject

Return a PlainObject with default options' values for the custom options. Default returns `{}`

### renderField(opts) : DOMElement

This method is called when rendering the field. The **opts** object contains the `mode` which is being used, so it is possible to know where the field is being rendered (**detail**, **editor** or **expert**)

If the custom mask splitter is `Block`, it is necessary to invoke the method `@renderInnerFields(opts)`, it returns a dom element with all the already rendered fields within the custom mask splitter. Append your custom dom element to that dom element or wrap it, then return it.

If the custom mask splitter is `Simple`, it is possible to return any dom element you want.
 