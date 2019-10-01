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

The server collects Custom Datatype values from fields in objects. A set of distinct Custom Datatype values is then sent to the [update script](#update-script), that should return (only!) the values which changed in the meantime. The server will then map the returned data using an unique identifier, and will update affected objects.

The Updater is set up to run once a day at a full hour. Alternatively, it can be started immediately using the API endpoint [`/api/v1/settings/updatecustomdata`](/en/technical/api/settings/#update-custom-datatypes).


## Plugin Configuration

The plugin needs to specify the settings for the update in the plugin configuration (YAML file).

Under `custom_types.<custom_type>.update` the following variables are defined:

```yaml
custom_types:
  <custom_type>:
    update:
      script: build/scripts/update.js
      timeout: 10
      batch_size: 1000
      interval_base_config: update_interval_<custom_type>.days
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

The value must be an `int` and must correspond with the value of `custom_types.<custom_type>.update.interval_base_config`: `"update_interval_<custom_type>.days"` defines a parameter `days` for the base config entry `update_interval_<custom_type>`.

```yaml
base_config:
  - name: update_interval_<custom_type>
    group: update_custom_data_type
    parameters:
      days:
        type: int
        min: 0
        default: 1
        position: 0
```

The value should have a minimum value of `0`. If it is set to `0`, the server interpretes this as a disabling of all updates for this custom datatype.

### Example Configuration

A working example of a plugin that supports the update functionality is the [Custom Datatype Plugin Gazetteer](https://github.com/programmfabrik/easydb-custom-data-type-gazetteer). The plugin defines the following configuration:

```yaml
custom_types:
  gazetteer:
    update:
      script: build/scripts/gazetteer-update.js
      timeout: 10
      batch_size: 1000
      interval_base_config: update_interval_gazetteer.days
    mapping:
      ...

base_config:
  - name: update_interval_gazetteer
    group: update_custom_data_type
    parameters:
      days:
        type: int
        min: 0
        default: 1
        position: 0
  - name: gazetteer_plugin_settings
    ...
```

## Update Payload

The update script has to receive and return data in a specific JSON structure. The requests always contain the following keys:

* `"action"`
    * mandatory
    * one of the distinct values `"start_update"` or `"update"`
    * used to define the type of action the update script has to perform

* `"plugin_config"`
    * mandatory
    * JSON representation of the plugin configuration YAML

* `"objects"`
    * optional (mandatory for action `"update"`)
    * payload (array of Custom Datatype Objects)
    * only used for action `"update"`

The returned JSON data has to have the following structure:

* `"status_code"`
    * mandatory
    * an integer value that resembles the HTTP status codes
    * `200` if the action was performed OK
    * `400` (or any other code) in case there was any error

* `"body"`
    * mandatory
    * JSON object with payload or information for errors
    * in case there is an error, it should have the structure of [Easydb Errors](/en/technical/errors)

### Received and returned data for action `"start_update"`

* This action should be called before starting the batch updates
    * The update script can check if the repository is responding
    * In case the updates would probably fail anyway, an error should be returned so the server will not start the batch update

#### Data received from the Custom Datatype Updater:

```json
{
    "action": "start_update",
    "plugin_config": {}
}
```

##### Mandatory fields

* `action` (= `"start_update"`)
* `plugin_config`
    * Server sends the JSON represantation of the YML configuration of the plugin

#### Data returned by the Update Script:

```json
{
    "status_code": 200,
    "body": {
        "state": {}
    }
}
```

##### Mandatory fields

* `status_code`
    * 200 in case the update of data was successful
* `body`
    * body should contain information in case of an error

##### Optional fields

* `body.state`
    * The state can contain any arbitrary data the update script wants to save until the first batch
    * The server will store the data as is, and will include the data in the next call of `update`

### Received and returned data for action `"update"`

#### Data received from the Custom Datatype Updater:

```json
{
    "action": "update",
    "plugin_config": {},
    "state": {},
    "batch_info": {
        "offset": 100,
        "total": 800
    },
    "objects" [
        {
            "identifier": "987654321abc",
            "data": {}
        }
    ]
}
```

##### Mandatory fields

* `action` (= `"update"`)
* `plugin_config`
    * Server sends the JSON represantation of the YML configuration of the plugin
* `batch_info.offset`
    * The offset of the current batch
* `batch_info.total`
    * The total number of objects in all batches
* `objects[]`
    * Array of custom datatype objects that will be checked and updated
* `objects[].identifier`
    * Each object has an unique identifier that is provided by the server and must be returned in updated objects
    * Otherwise the updated custom data can not be mapped to fields in affected objects
* `objects[].data`
    * Custom datatype value that is checked if it needs to be updated

##### Optional fields

* `body.state`
    * The server will include the state, in case the update script returned a state in the previous reponse (after `start_update` or `update`)

#### Data returned by the Update Script:

```json
{
    "status_code": 200,
    "body": {
        "state": {},
        "payload": [
            {
                "identifier": "987654321abc",
                "data": {}
            }
        ]
    }
}
```

##### Mandatory fields

* `status_code`
    * 200 in case the update of data was successful
* `body.payload[].identifier`
    * The provided identifiers of objects must be included
    * Otherwise the updated custom data can not be mapped to fields in affected objects
* `body.payload[].data`
    * Updated custom datatype value that will be used as the new value in objects

##### Optional fields

* `body.state`
    * The state can contain any arbitrary data the update script wants to save until the first batch
    * The server will store the data as is, and will include the data in the next call of `update`

If there were no updates, the script should return a status code of `200` and an empty JSON array as `"payload"`.

## Update Script

The update script is specific for each Custom Datatype plugin. It has to be able to receive and return the data in the JSON strucutures described above. It has to implement functions that can handle the actions `"start_update"` and `"update"`. It also should handle any error and return correctly formatted error messages. Errors will be logged as events, and should contain enough information to debug and reproduce errors.

The script also has to able to use the API of the repository server. This API communication can be implemented in any way and is completely independent of the easydb server.

A working example can be found in the [GazetteerUpdate.coffee](https://github.com/programmfabrik/easydb-custom-data-type-gazetteer/blob/master/src/script/GazetteerUpdate.coffee) file of the Gazetterr Plugin. This file must be compiled to a JavaScript file and must be provided at the path which is defined in the config variable `custom_types.gazetteer.update.script`.