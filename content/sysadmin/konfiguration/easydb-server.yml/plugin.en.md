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

## Available base plugins

| Pluginname | Description |
|:-----------|-------------|
| [css](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/css) | Allows to modify easydb's css files. |
| [presentation-pptx](/en/sysadmin/konfiguration/easydb-server.yml/plugin/presentation-pptx) | Allows to create powerpoint presentations in easydb5 |
| [server](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/server) |  |
| [eventmanager](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/eventmanager) | Allows you to see all events in easydb5 frontend |
| [basemigration](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/basemigration) |  |
| [hotfolder](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/hotfolder) | Allows you to configure the [hotfolder](/en/sysadmin/konfiguration/hotfolder) |
| [export-transport-ftp](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/export-transport-ftp) | Allows you to export your files via ftp |
| [oai](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/oai) |  |
| [detail-map](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/detail-map) |  |
| [editor-tagfilter-defaults](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/editor-tagfilter-defaults) |  |
| [remote-plugin](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/remote-plugin) | Allows you to connect your frontend to another easydb5 |
| [easydb4migration](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/easydb4migration) |  |
| [connector](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/connector) | Allows you to connect your easydb5 to other instances |
| [a-frame](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/a-frame) |  |

## Available extension plugins

| Pluginname | Plugin website | Description |
|:-----------|----------------|-------------|
| [custom-data-type-dante](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/dante) | [dante](https://github.com/programmfabrik/easydb-custom-data-type-dante) | References to entities of the DANTE-Vokabulary-Server (https://dante.gbv.de) |
| [custom-data-type-gazetter](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/gazetter) |  | Work in progress |
| [custom-data-type-link](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/link) | [link](https://github.com/programmfabrik/easydb-custom-data-type-link) | Allows you to configure fields as web-link |
| [custom-data-type-getty](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/getty) | [getty](https://github.com/programmfabrik/easydb-custom-data-type-getty) | References to entities of the Getty Vocabularys. |
| [custom-data-type-gvk](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/gvk) | [gvk](https://github.com/programmfabrik/easydb-custom-data-type-gvk) | References to entities of the Gemeinsamer Verbundkatalog (GVK) |
| [custom-data-type-geonames](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/geonames) | [geonames](https://github.com/programmfabrik/easydb-custom-data-type-geonames) | References to entities of the GeoNames geographical database |
| [custom-data-type-gn250](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/gn250) | [gn250](https://github.com/programmfabrik/easydb-custom-data-type-gn250) | References to entities of the gn250-Set of Bundesamt für Kartographie |
| [custom-data-type-georef](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/georef) | [georef](https://github.com/programmfabrik/easydb-custom-data-type-georef) | References to geoJSON-Objects |
| [custom-data-type-gnd](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/gnd) | [gnd](https://github.com/programmfabrik/easydb-custom-data-type-gnd) | References to entities of the Integrated Authority File (GND) |
| [custom-data-type-tnadiscovery](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/tnadiscovery) | [tnadiscovery](https://github.com/programmfabrik/easydb-custom-data-type-tnadiscovery) | References to entities of the Nationalarchives-Discovery-System |
| [custom-data-type-location](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/location) | | Allows you to configure gps data in easydb5 |

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