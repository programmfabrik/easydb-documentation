---
title: "46 - Plugin Configuration"
layout: config
menu:
  main:
    name: "Plugin Configuration"
    identifier: "sysadmin/konfiguration/easydb-server.yml/plugin"
    parent: "sysadmin/konfiguration/easydb-server.yml"
easydb-server.yml:
  - plugins.enable[]
  - plugins.enable[].base.custom-data-type-link
---
# Plugin configuration

## Available easydb5-plugins

| Pluginname | Description |
|:----------:|-------------|
| [custom-data-type-dante](https://github.com/programmfabrik/easydb-custom-data-type-dante) | References to entities of the DANTE-Vokabulary-Server (https://dante.gbv.de) |
| [custom-data-type-gazetter](https://github.com/programmfabrik/easydb-custom-data-type-gazetter) | Work in progress |
| [custom-data-type-link](https://github.com/programmfabrik/easydb-custom-data-type-link) | Allows you to configure fields as web-link |
| [custom-data-type-getty](https://github.com/programmfabrik/easydb-custom-data-type-getty) | References to entities of the Getty Vocabularys. |
| [custom-data-type-gvk](https://github.com/programmfabrik/easydb-custom-data-type-gvk) | References to entities of the Gemeinsamer Verbundkatalog (GVK) |
| [custom-data-type-geonames](https://github.com/programmfabrik/easydb-custom-data-type-geonames) | References to entities of the GeoNames geographical database |
| [custom-data-type-gn250](https://github.com/programmfabrik/easydb-custom-data-type-gn250) | References to entities of the gn250-Set of Bundesamt für Kartographie |
| [custom-data-type-georef](https://github.com/programmfabrik/easydb-custom-data-type-georef) | References to geoJSON-Objects |
| [custom-data-type-gnd](https://github.com/programmfabrik/easydb-custom-data-type-gnd) | References to entities of the Integrated Authority File (GND) |
| [custom-data-type-tnadiscovery](https://github.com/programmfabrik/easydb-custom-data-type-tnadiscovery) | References to entities of the Nationalarchives-Discovery-System |

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

~~~~
easydb-server:
  plugins:
    enabled-:
      - base.custom-data-type-link
~~~~


After a reboot, the plugin can be found in the list "Plugins" on the page "Version Information".

You get there via the `i` button (far left in the bar) and then ->` About`.


# Extension Plugins

Before using Extension Plugins they need to be installed and activated.

Find more information in the chapter [Plugin-Installation](/en/sysadmin/plugin).
