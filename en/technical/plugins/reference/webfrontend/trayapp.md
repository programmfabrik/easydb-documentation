# Tray apps

Tray apps can be used to put functionality inside the easydb tray in the upper right corner.

getDisplay

getSortValue

is_allowed

```coffeescript

class TestTray extends TrayApp
  is_allowed: =>

  getDisplay: =>
    new CUI.Button
      icon: "fa-question"
      onClick: =>
        CUI.alert(text: "Hello")

ez5.session_ready ->
  ez5.tray.registerApp(new TestTray())

```
