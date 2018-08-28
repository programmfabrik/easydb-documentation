---
title: "46 - Plugin Configuration"
layout: config
menu:
  main:
    name: "Plugin Configuration"
    identifier: "sysadmin/konfiguration/easydb-server.yml/plugin"
    parent: "sysadmin/konfiguration/easydb-server.yml"
easydb-server.yml:
  - plugins.enable
  - plugins.enable.base.css
  - plugins.enable.base.presentation-pptx
  - plugins.enable.base.server
  - plugins.enable.base.eventmanager
  - plugins.enable.base.basemigration
  - plugins.enable.base.hotfolder
  - plugins.enable.base.export-transport-ftp
  - plugins.enable.base.oai
  - plugins.enable.base.detail-map
  - plugins.enable.base.editor-tagfilter-defaults
  - plugins.enable.base.remote-plugin
  - plugins.enable.base.easydb4migration
  - plugins.enable.base.connector
  - plugins.enable.base.a-frame
  - plugins.enable.base.custom-data-type-gazetter
  - plugins.enable.base.custom-data-type-link
  - plugins.enable.base.custom-data-type-getty
  - plugins.enable.base.custom-data-type-gvk
  - plugins.enable.base.custom-data-type-geonames
  - plugins.enable.base.custom-data-type-gn250
  - plugins.enable.base.custom-data-type-georef
  - plugins.enable.base.custom-data-type-gnd
  - plugins.enable.base.custom-data-type-tnadiscovery
  - plugins.enable.base.custom-data-type-location
---
# Plugin configuration

{{< getFileContent file="/content/sysadmin/konfiguration/easydb-server.yml/includes/available-plugins.en.md" markdown="true" >}}




The easydb 5 already contains several plugins, which are marked with "base" in the configuration.

Many of these plugins are enabled by default.

Changes can be made in the central configuration file `easydb5-master.yml`. Its location has been set during the [installation](/en/sysadmin/installation).

In this example, the *custom-data-type-link*, *custom-data-type-gnd*, *custom-data-type-location*, *editor-tagfilter-defaults* and *drupal* plug-in is configured as active:

```yaml
  plugins:
    enabled+:
      - base.custom-data-type-link
      - base.custom-data-type-gnd
      - base.custom-data-type-location
      - base.editor-tagfilter-defaults
      - base.drupal
```

In the same way it is also possible to deactivate a plugin that is activated by default:

```yaml
easydb-server:
  plugins:
    enabled-:
      - base.custom-data-type-link
```


After a reboot, the plugin can be found in the list "Plugins" on the page "Version Information".

You get there via the `i` button (far left in the bar) and then ->` About`.


# Extension Plugins

Before using Extension Plugins they need to be installed and activated.

Find more information in the chapter [Plugin-Installation](/en/sysadmin/plugin).


### Example configuration of plugins
In this example we will add the *hotfolder*, *gn250* and *tnadiscovery* plugin.
Also we will deactivate *presentation-pptx*, *remote-plugin* and *detail-map* plugin.


```yaml
plugins:
  enable+:
    - base.hotfolder
    - base.custom-data-type-gn250
    - base.custom-data-type-tnadiscovery
  enabled-:
    - base.presentation-pptx
    - base.remote-plugin
    - base.detail-map
```