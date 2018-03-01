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
````

### name

This is the name of the plugin as it is used throughout the server. Mostly for prefixing URLs and localization keys.

### version

This is version string which is shown in the webfrontend in the about info menu.

### displayname

This is the displayname used in the webfrontend in the about info menu. It needs a map with per language properties.

### webfrontend

#### url

The path the plugin code is found, when loaded in the webfrontend. It is prefixed with /api/v1/plugin/static/**\<plugin-realm\>**/**\<plugin-name\>**/.

**plugin-realm** is "base", "solution", or "extension", depending on the loading path of the plugin.

**plugin-name** is the name of the plugin.

Usually you don't have to worry about the prefix, simply add a filename here which can be found in the "build/webfrontend" path of the installation.

> We need more info here! Whats with extensions etc.?

#### l10n

The path where the webfrontend will load the language keys from. This is only necessary, if your plugin uses localized keys.


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





## custom_type



*henk*


```yaml
plugin:
  name: easydb4migration
  version: 1.0
  server:
    api-version:
      require: 1
  webfrontend:
    url: easydb4migration.js
    l10n: l10n/

base_config:
  - name: easydb4migration
    group: css
    parameters:
      fylr_url:
        position: 0
        type: text
      fylr_uid:
        position: 1
        type: text
      fylr_inst:
        position: 2
        type: text
```
