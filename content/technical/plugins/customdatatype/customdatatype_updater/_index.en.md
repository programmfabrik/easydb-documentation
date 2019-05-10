---
title: "Custom Data Type Updater"
menu:
  main:
    name: "Custom Data Type Updater"
    identifier: "technical/plugins/custom_datatype_updater"
    parent: "technical/plugins/customdatatype"
---

# Custom Data Type Updater

If a Custom Data Type plugin receives data from a repository on an external server, the server has the ability to check if the custom data in the repository has changed, and objects that contain the custom data are updated.

There are multiple requirements for the plugin to be able to automatically update the custom data.

## Plugin Configuration

The plugin needs to specify the settings for the update in the plugin configuration (YAML file). The following examples are taken from the [Gazetteer Plugin](https://github.com/programmfabrik/easydb-custom-data-type-gazetteer), which has the ability to update the custom data.

Under `custom_types.gazetteer.update` the following variables are defined:

```yaml
custom_types:
  gazetteer:
    update:
      script: build/scripts/gazetteer-update.js
      timeout: 10
      batch_size: 1000
      interval_base_config: update_interval_gazetteer.days
```

* `script`
    * string, mandatory
    * relative path to the [javascript file](#update-script) with the update functionality
    * if the script variable is not set, or the file can not be loaded, the server will not start
* `timeout`
    * integer, optional (default: `10`)
    * timeout in seconds that is used in the update script in case the repository should not be reachable
    * minimum value: `1`
* `batch_size`
    * integer, optional (default: `1000`)
    * object batch size that is used in the update script for updating custom data objects
    * minimum value: `1`, maximum value: `1000`
* `interval_base_config`
    * string, optional (default: `default_update_interval.days`)
    * key in the base configuration ([plugin base configuration](#base-configuration) or [server base configuration](../../../../webfrontend/administration/base-config/custom_datatype_update))
    * the base config value with this key will be used to load the interval in days between updates for this custom datatype plugin

## Base Configuration

The custom datatype plugin can define an own interval in days to wait between updates. If this value is not defined, the default value for all updates is used

The value must be an `int` and must correspond with the value of `custom_types.gazetteer.update.interval_base_config`: `"update_interval_gazetteer.days"` defines a parameter `days` for the base config entry `update_interval_gazetteer`.

```yaml
base_config:
  - name: update_interval_gazetteer
    group: update_custom_data_type
    parameters:
      days:
        type: int
        min: 0
        default: 1
        position: 0
```

The value should have a minimum value of `0`. If it is set to `0`, the server interpretes this as a disabling of all updates for this custom datatype.

<!-- ## Update Script -->

<!-- TODO: tutorial for update script -->