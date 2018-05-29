# Configuration

The configuration of an easydb plugin is written in YAML and put into the server loading path.

```yaml
base:
  plugins+:
    - name: remote-plugin
    - file: remote-plugin/RemotePlugin.config.yml

plugins:
  enabled+:
    - base.remote-plugin

```


The file uses different blocks to configure different aspects of the server support:

* **plugin**, this is a generic header with plugin information
* **base_config**, block to extend the base config with configuration
* **custom_types**, block to register custom data types with the server


## plugin

Here is an example from the Remote Plugin:

```yaml
plugin:
  name: remote-plugin
  version: 1.0
  url: https://github.com/programmfabrik/easydb-remote-plugin
  displayname:
    de-DE: Remote Plugin
    en-US: Remote Plugin
  info:
    de-DE: Das Remote Plugin erlaubt die Einbindung von externen Javascript-Quellen in das Webfrontend.
    en-US: The remote plugin allows to embed external Javascript-Sources and CSS files into the webfrontend.
  webfrontend:
    url: remote-plugin.js
    l10n: l10n/
    css: remote-plugin.css
    type_extension:
      mask:
        <datatype>:
          - name: <field>
            type: text


````

### name

This is the name of the plugin as it is used throughout the server. Mostly for prefixing URLs and localization keys.

### version

This is version string which is shown in the webfrontend in the about info menu.

### displayname

This is the displayname used in the webfrontend in the about info menu. It needs a map with per language properties.

### info

This is is shown inside a tooltip in the webfrontend. You can use Markdown here.

### webfrontend

This block uses some properties which are used inside the webfrontend for enhanced functionality. It can be extended with custom information.

```coffeescript
ez5.pluginManager("your-plugin").getWebfrontend()
```

#### url

The path the plugin code is found, when loaded in the webfrontend. It is prefixed with /api/v1/plugin/static/**\<plugin-realm\>**/**\<plugin-name\>**/.

**plugin-realm** is "base", "solution", or "extension", depending on the loading path of the plugin.

**plugin-name** is the name of the plugin.

Usually you don't have to worry about the prefix, simply add a filename here which can be found in the "build/webfrontend" path of the installation.

> We need more info here! Whats with extensions etc.?

#### l10n

The path where the webfrontend will load the language keys from. This is only necessary, if your plugin uses localized keys.

#### css

The path where the CSS file for the plugin should be loaded from. Use

```coffeescript
ez5.pluginManager.getPlugin("remote-plugin").loadCss()
```

to load the CSS. This appends the CSS to **document.head**.

### type_extension

Use this to add custom option to the mask editor in datamodel. You can extend the easydb default datatypes with this feature, however you cannot extend a custom data type with it.

The format looks as follows:

```yaml
type_extension:
  mask:
    <datatype>:
      - name: <field>
        parameters:
          <param>:
            <type-config-definition>
```

The **datatype** is the datatype of the easydb, one of

 * text_oneline
 * text_l10n_oneline
 * text
 * text_l10n
 * string
 * date
 * daterange
 * datetime
 * number
 * integer.2
 * eas
 * boolean

 **\<field\>** is the name of the custom setting attribute.

 The custom setting attribute can be accessed with

 ```coffeescript
 fieldInstance.FieldSchema.custom_settings["<field>"]
 ```

 The **\<type-config-definition\>** uses the same definitions as **base_config**. See below for more details.


## base_config

List of configurations which are added to the base configation of easydb.

```yaml
base_config:
  - name: webfrontend_remote_plugin
    group: remote
    parameters:
      instances:
        type: table
        fields:
          - name: js_url
            type: text
            position: 0
          - name: css_url
            type: text
            position: 1
```
### name

The name of the base config. It is accessible in the webfrontend within

```coffeescript
ez5.session.getBaseConfig().system.<name>
````

### parameters

This is the map of parameters for the given base config. The key for the map is the name of the parameter. In the above example, the name is **instances**.

Each parameter gets a parameter definition map. The map must define a **type** and an optional **position**. Each type may define additional properties for the parameter definition map. See the type descriptions for details.

Supported types are **bool**, **text*, **int**, **email**, **text-multiline**, **text-l10n**, **string-list**, **string-list-sort**, **select**, **file**, **table**, **tag-select**, **tagfilter-select**.

#### plugin_type

The types **text** and **int** support an optional key **plugin_type**. With this key given, plugins can use there on types to fill base configuration with data. Some types are hardocded in the webfrontend code.

Plugins can implement there own type, see [Base-Config](reference/webfrontend/base-config/baseconfig.html) for details.

The type **text** supports hardcoded:

* plugin type **date** to input and store a date

The type **int** supports hardcoded:

* plugin type **profile_mapping_select** to select a mapping profiles
* plugin type **group_easydb_select** to select an easydb group
* plugin type **right_preset_collection** to select a right preset for collections

### bool

This type outputs a simple checkbox.

### text

This type outputs a simple text input. Currently we don't have server support for **json**, so we use a frontend workaround to store arbitrary **json** inside the input type **text**.

Add an optional **regexp** key to the parameter definition map to restrict the input to the given regular expression.

Together with a plugin type you may need to use **store_as_json** to save and load the text as **json**.

### int

This type outputs a number input.

### email

This type outputs an email input.

### text-multiline

Output a textarea.

### text-l10n

Output a localized one line input.

### text-l10n-multiline

Output a localized textarea.

### string-list, string-list-sort

Output a CUI.Options with the given **choices** as options. A **label_choice** key can be set to use the localization system to translate the choices in the frontend.

**string-list-sort** uses the sort capability of CUI.Options to output a list of choices which can be sorted.

### select

Outputs a CUI.Select with the given **options**.

### files

Outputs a upload possibility for a file. The standard easydb asset server system is used to manage the file.

### tag-select

Outputs a tag selector.

### tagfilter-selector

Outputs a tagfilter selector.


## custom_types

Custom types are defined in the .yml so the server can deal with them at startup time. The type can define a search mapping as well as configuration for datamodel and mask customization.

```yaml
link:
  mapping:
    url:
	  type: text_oneline
  config:
    schema:
      - name: title
        parameters:
          type:
            type: select
            options: ["none", "text", "text-l10n"]
      - name: add_timestamp
        parameters:
          value:
            type: bool
    mask:
      - name: editor_style
        parameters:
          value:
            type: select
            options: ["inline",  "popover"]
```

## system_rights

This is an Array of additional system rights, needed for the Plugin.

### name

Name of the system right. This will be accessible by

```coffeescript
ez5.session.getSystemRight("plugin.<plugin-name>.<system-right-name>")
```

or

### comment

Comment for the system right, this is only available over the API.

## custom_events

A list of custom events that are defined by this plugin and extend the list of default server events.

```yaml
custom_events:
  - WORDPRESS_SYNC
```
