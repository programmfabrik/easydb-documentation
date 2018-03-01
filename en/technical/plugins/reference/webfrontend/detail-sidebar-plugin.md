# Detail sidebar plugin

Detail sidebar plugins are useful to add new features inside the detail sidebar.

To create a new one, it's necessary to extends the class **DetailSidebarPlugin**, implement the following methods and register it.

```coffeescript
class MyDetailSidebarPlugin extends DetailSidebarPlugin
    # ... methods implementations
 
ez5.session_ready =>
    DetailSidebar.plugins.registerPlugin(MyDetailSidebarPlugin)
```

After the plugin is implemented and registered, a **button** will appear next to the button of the **Asset Browser**. 

### Methods to implement

- isAvailable() : `Boolean`
    - Indicates whether the **button** will be shown or not.
- showDetail()
    - This method is invoked when the **button** is activated.
- hideDetail()
    - This method is invoked when the **button** is deactivated.
- prefName() : `String`
    - An unique string to save the user preference.
- getButtonLocaKey() : `String`
    - A localisation key that indicates the icon and tooltip of the **button**.

### Optional methods available to implement

- render()
    - This method is invoked once, after *DetailSidebar* is rendered.
- renderObject()
    - This method is invoked whenever *DetailSidebar's renderObject()* method is invoked.  
- getCenterContent() : `HTMLElement` / `CUI.DOMElement`
    - Via this method is possible to return an extra element that will be rendered above other elements of the *center* pane. 

### Optional methods available to override

- setButton(button `CUI.Button`)
    - Plugin's **button** setter.
- getButton() : `CUI.Button`
    - Plugin's **button** getter. 
- isDisabled() : `Boolean`
    - It is used to disable the **button**. It returns *false* as default.
- getPane() : `String`
    - It is possible to use two plugins at the same time by changing this method, because they are divided in "top" and "left" plugins. It returns "top" as default.

Usage of getPane():
```coffeescript
# "top"
render: ->
  @_detailSidebar.mainPane.replace(@__pluginMainElement, "top")
 
# "left"
getPane: ->
  "left"
 
render: ->
  @_detailSidebar.browserLayout.replace(@__pluginMainElement, "left")

```        

### Available attributes

- detailSidebar `DetailSidebar`
    - It is the instance of **DetailSidebar** class which is using the plugin.