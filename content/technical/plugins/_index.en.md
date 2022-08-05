---
title: "104 - Plugins"
menu:
  main:
    name: "Plugins"
    identifier: "technical/plugins"
    parent: "technical"
---
# Plugins

Plugins allow for an extension of easydb functionality. They are easily integratged into the Server through it's YAML and defined by [YAML files](#plugin-definition-in-yaml) themselves.

Plugin functionality includes:

- creating frontend apps
- defining system rights
- define or replace localization keys
- define server callbacks

Inside Plugins, callbacks can be used to execute functions inside the server. An overview over the callbacks and the contexts in which they can be used, as well as Exceptions that can be used to display different Error types, can be found [here](server/python).

### Examples
You can find an example for each type of plugin [in this repository](https://github.com/programmfabrik/easydb-example-plugin)

## Plugin Definition

### Configuration in YAML

Plugins are defined in a YAML configuration file. Because of a new naming convention and for future compatibility, this file *must* be named `manifest.yml`.

The naming convention includes the following rules:

* all plugins should be named `easydb-<pluginname>-plugin`
* all custom data types should be named `easydb-custom-data-type-<customtype>`
* the directory in which the plugin submodule is checked out should be the same as the plugin name
  * a different directory name can be set in the [Makefile](#makefile), but this is not recommended

The YAML configuration is used to define paths to frontend and server code, additional base configuration entries or elasticsearch mappings for [custom datatype plugins](customdatatype). See the [configuration of the public easydb-example-plugin](https://github.com/programmfabrik/easydb-example-plugin/blob/master/manifest.yml) as a reference.

#### `plugin`

Defines the necessary information about the plugin, like the `name` and the multilingual `displayname` and `info`, the `version` and a `url` to the plugin repository.

The `webfrontend` part of the plugin is defined under the `plugin` key. It defines the relative paths to the javascript file (`url`), the multilingual frontend translations (`l10n`) and the CSS stylesheets (`css`).

[`webhooks`](webhooks/webhook/) are also defined here.

#### `python-2`

This top level key defines the [server part](#server-callbacks) of the plugin which is written in Python. The relative path to the main python file is defined in `file`.

#### `custom_types`

[Custom Data Types](customdatatype) are defined at this top level key. The configuration includes optional information for the [Custom Data Type Updater](customdatatype/customdatatype_updater/).

#### Other top level keys

- `base_config`: This part can be used to extend the base configuration, so the plugin can be configured in the frontend
- `require_system_right`: Additional [system rights](/en/webfrontend/rightsmanagement/#aclsystem) that can be granted to users and groups, so that the usage of the plugin can be controlled in the rights management
- `custom_events`: List of own event types that can be logged during the runtime of the plugin

### Makefile

The Makefile is used to define the plugin name and path, the files that are installed, and how the frontend is built including the generating of language files. See the [Makefile of the public easydb-example-plugin](https://github.com/programmfabrik/easydb-example-plugin/blob/master/Makefile) as a reference.

* `PLUGIN_NAME`: internal name of the plugin, same as [`plugin.name` in `manifest.yml`](#plugin)
* `PLUGIN_PATH`: actual relative path to the directory where the plugin files are copied to for `make install` (requires [`easydb-library`](#including-the-easydb-library-submodule))
  * the path can be different from the `PLUGIN_NAME`, but should be the same as the `PLUGIN_NAME`
  * if the path is not different from the plugin name, this variable is not needed
* `INSTALL_FILES`: list of all files that need to be included when the plugin is installed
  * `manifest.yml`
  * python source files for server part
  * generated javascript files for frontend part
  * css files for frontend part
  * generated json files with language keys
* `L10N_FILES`: path to csv files with language keys
* `SCSS_FILES`: path to css files for frontend
* `COFFEE_FILES`: path to coffeescript files that are converted to javascript files for the frontend

## Including the `easydb-library` submodule

The submodule [`easydb-library`](https://github.com/programmfabrik/easydb-library) should be included inside the plugin submodule. It proveds tools to generate build information about the plugin, and is needed to install the plugin on the server.

## Web Front End

Frontend apps are Javascript applications that run client-side and can be integrated into the easydb Interface as top level apps in different parts of the web application, such as the sidebar, as popovers opened from within the user tray and more.

### Plugin types
- [Asset detail](webfrontend/types/asset-detail-plugin)
- [Custom data types](webfrontend/types/custom-data-type-plugin)
- [Custom mask splitter](webfrontend/types/custom-mask-splitter-plugin)
- [Detail sidebar](webfrontend/types/detail-sidebar-plugin)
- [Editor](webfrontend/types/editor-plugin)
- [Export manager](webfrontend/types/export-manager-plugin)

### Available plugins
- [HTML Editor](webfrontend/html-editor)
- [Pdf Creator](webfrontend/pdf-creator)
- [Barcode](webfrontend/barcode)
- [Display field values](webfrontend/display-field-values)


## Server-Callbacks

Server-Callbacks are Python scripts, that are run in specific situations in a standardized procedure. The plugin registers a function at the server. From then on everytime a certain event happens, the server calls this function.

The server calls the function with information to be processed and expects a response with altered content for further use. Alternatively, if the plugin is used to validate data, for example an `EasydbException` can be raised when data is invalid. This way a database transaction can be aborted so that no invalid data is saved in the database.

An `api_db_pre_update` callback for example receives the data entered by a user when a `POST api/db` call is made, alters the data if necessary, and passes it to the server. From here on the altered data is processed as it would have been without the plugin.

Server callbacks are able to throw easydb errors like "The user has insufficient rights for ..." It is also possible to define custom error types, which will be displayed in the frontend properly and localized.

Server callbacks have access to many of easydb's internal information and tools.
They may for example alter an open database transaction of a frontend request, read the base configuration, or request open sessions (which user, what rights?).

### Process Plugins

Register a Plugin as a process that runs inside the server.

- type: `process`

The Plugin process is started when the server calls the `run` method, and stops with the server. The `stop` method is used to clean up before the server and the Plugin process stop. In the `run` method, threads can be started to repeatedly execute tasks parallel to the server runtime.

#### Example

```python
def easydb_server_start(easydb_context):
    easydb_context.register_callback('process', {'name': 'process_example'})

# define a funtion that is repeatedly executed while the server runs
def process_function(parameter1):
    # do something
    pass

# start a simple thread in the run method
def run(easydb_context):
    t = Thread(target = process_function, args = (parameter1,))
    t.start()
    t.join()

# use the stop method to clean up plugin resources before the server stops
def stop(easydb_context):
    # do some cleanup
    pass
```

### API Callbacks

API Callbacks are used to extend the Server API. Registered Callbacks create new API Endpoints.

- type: `api`

The URL of an added Endpoint depends on how the plugin is included in the server:
* `base` Plugins: `<Server URL>/api/plugin/base/<Plugin Name>/<Callback Name>`
* [`extension` Plugins](/en/sysadmin/configuration/easydb-server.yml/plugins/#extension-plugin): `<Server URL>/api/plugin/extension/<Plugin Name>/<Callback Name>`

#### Example

To create an API Endpoint (for a `GET` request), that returns information about the Server Instance as a JSON Object, register a callback:

```python
def easydb_server_start(easydb_context):
    easydb_context.register_callback('api', { 'name': 'instance', 'callback': 'get_instance'})
```

This creates a new API Endpoint that is reachable at the URL `<Server URL>/api/plugin/base/example-plugin/instance`.

The method `get_instance` to be called would be:

```python
def get_instance(easydb_context, parameters):
    return {
        "status_code": 200,
        "body": json.dumps(easydb_context.get_instance(), indent = 4),
        "headers": {
            "Content-Type": "application/json; charset=utf-8"
        }
    }
```

In this case, the instance information that is returned from `easydb_context.get_instance()` is already a JSON object (`dict`), so it can be returned directly.

It is important to wrap the response body inside a HTTP response.

#### Request Parameters

The Request Parameters are stored in the method parameter `parameters`.

This `dict` contains information about the query URL, the HTTP method and headers and the body of a `POST / PUT` request. The `parameters` object of a call to `<Server URL>/api/plugin/base/<Plugin Name>/<Callback Name>?a=5&b=test` would have the following content:

```python
{
    "method": "GET",
    "path": "",
    "body": "",
    "query_string": "a=5&b=test",
    "query_string_parameters": {
        "a": [
            "5"
        ],
        "b": [
            "test"
        ]
    },
    "headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",
        ...
    }
}
```

### Export Callbacks

Callbacks for Exports. Allows plugins to define transport types and export extensions. After each export, the export callbacks are called, so each plugin has to check the export definition if the exported files should be manipulated.

- types:
    - `export_produce`
        - called after an export finished writing data to the file system. The saved data can be manipulated or checked, before the Export is finished.
    - `export_transport`
        - called after an export finished writing data to the file system. The saved data can be sent to a specified target (e.g. an FTP Server, upload to another System).

#### Example

The `export_produce` callback is used to manipulate the data or change the format of the exported files. This example reads the data that was exported in JSON format and converts it to YML format.

```python
def easydb_server_start(easydb_context):
	easydb_context.register_callback('export_produce', {'callback': 'export_as_yml'})

def export_as_yml(easydb_context, parameters):

	# get the exporter definition
	exporter = easydb_context.get_exporter()

	# (1)
	# get the produce options
	produce_options = get_json_value(exporter.getExport(), "export.produce_options", False)

	# check if the export definition fits to this plugin
	if str(get_json_value(produce_options, "plugin", False)) != "example_export":
		# the export specified a different plugin, so nothing has to be done
		return

	# (2)
	# load exported files
	files = exporter.getFiles()

	# get the export directory
	export_dir = exporter.getFilesPath()

	# iterate over the definitions of the exported files and parse the json content
	for f in files:
		if "path" in f:

			# check if this file is a json file
			file_path = f["path"]
			if file_path.lower().endswith(".json"):

				# format the filename of the new YML file, replace ".json" with ".yml"
				file_name = str(f["path"].split(".")[0] + ".yml")

				# parse the json file
				file = open(file_path, "r")
				content = json.loads(file.read().decode('utf-8'))
				file.close()

				# (3)
				# convert the list of objects to YML
				objects = get_json_value(content, "objects", False)

				# save the YML file in the temporary folder
				tmp_filename = os.path.abspath("%s/../tmp/tmp_objects.yml" % export_dir)

				with open(tmp_filename, "w") as yml_file:
					# define the final dict that will be converted to YML
					object_output = {
						"objects": objects
					}

					# dump the YML
					yaml.dump(object_output, yml_file, default_flow_style = False)
					yml_file.close()

					# (4)
					# add the new YML file to the export so it can be opened or downloaded from the frontend
					exporter.addFile(tmp_filename, file_name)

					# remove the old JSON file
					exporter.removeFile(f["path"])
```

**(1)**

The produce options define the name of the plugin that is used to handle the exported data, and other information that can be set in the frontend. By default, the value `"plugin"` is `"easydb"` for all exports. A plugin should always check if this value, and stop at the beginning when the plugin name does not fit.

The export definition has this structure:

```python
{
    "plugin": "example_export",
    "example_option_1": 123,
    "example_option_2": true
}
```

**(2)**

The exported files are defined in an array that is returned by `easydb_context.get_exporter().getFiles()`. The export file definition have the following structure:

```python
[
    {
        "eas_fileclass": null,
        "eas_version": null,
        "system_object_id": null,
        "date_created": null,
        "path": "2018-03-05 10_19 easydb FULL example_export_plugin/28919-28920@2f94d4fe-ec64-408e-8705-dd5f7da3e1a8.json",
        "eas_id": null,
        "size": 4612
    }
]
```

**(3)**

The objects are inside the array `"objects"` in the JSON definition of the exported objects. A JSON export has the following structure:

```python
{
    "aggregations": {},
    "format": "long",
    "type": "objects",
    "objecttypes": [
        "example_objecttype"
    ],
    "objects": [
		...
	],
    "language": "de-DE",
    "offset": 0,
    "limit": 1000,
    "count": 1,
    "took": 5,
    "request_time": {
        "elasticsearch": 5
    }
}
```

**(4)**

To display new or renamed files in the export dialog in the frontend, the new filenames have to be added to the export, and files that are not used anymore have to be removed. To add a file, the path to the file and the relative filename that will be shown in the frontend have to be passed to the server.

The server copies the original file into the export folder. The relative filename has to fit to the export folder. For example, if an export was saved as `plan-export-123`, and the plugin created a file in the temporary folder `tmp`, then the path to the temporary file has to passed to the server, as well as the target name of the new file relative to the directory `/home/.../plan-export-123/files/`:

```python
exporter.addFile(
	"/home/.../plan-export-123/tmp/tmp_objects.yml",
	"example_export_plugin/exported_objects.yml"
)
```

To remove a file, the path of the file relative to the `files` directory needs to be passed to the server:

```python
exporter.removeFile(
	"example_export_plugin/exported_objects.json"
)
```


### Database Callbacks (Extension Points)

Callbacks that are called before and after database updates. The data can be validated and manipulated before it is saved in the database.
Callback functions will be passed two arguments when invoked: An Object that represents the easydb context, providing direct access to the
easydb server and a dictionary that contains the data that is being handled. The content of the dict depends on the the action associated
with the callback: Pre update callbacks get passed the modified fields and post update callbacks get permission and display metadata.

Note that callbacks can be chained and always have to return something json serializeable. 

Also note that the info dict has to be unpacked. 

```python
import logging

def easydb_server_start(easydb_context):
    easydb_context.register_callback('db_post_update_one', {'callback': 'minimal_callback'})

    logging.basicConfig(filename="/var/tmp/plugin.log", level=logging.DEBUG)
    logging.info("Loaded plugin")

def minimal_callback(easydb_context, easydb_info):
    try:
        # unpack payload and do stuff:
        info = easydb_info['data']
        logging.info('Got info: ' + str(info))
    except Exception as exception:
        logging.error(str(exception))
    finally:
        return info
```

- **Callbacks before data is updated or deleted**.

    - Validate the content of the data before it is saved/deleted in the database. Manipulate data before it is saved in the database.

    - `db_pre_update_one`
        - called before one object is saved in the database
        - called once for each object

    - `db_pre_update`
        - called before objects are saved in the database
        - called for all objects at once

    - `db_pre_delete_one`
        - called before one object is deleted from the database
        - called once for each object

    - `db_pre_delete`
        - called before objects are deleted from the database
        - called for all objects at once

- **Callbacks after data was updated or deleted**

    - `db_post_update_one`
        - called after one object was saved in the database
        - called once for each object

    - `db_post_update`
        - called after objects were saved in the database
        - called once for each object

    - `db_post_delete_one`
        - called after one object was deleted from the database
        - called once for each object

    - `db_post_delete`
        - called after objects were deleted from the database
        - called for all objects at once


### User Callbacks

- `user_post_update`
<!-- TODO add description -->

### Transition Callbacks

Transition (or [Workflow](/en/webfrontend/rightsmanagement/tags/#workflows)) actions defined by a plugin are realised using this callback. Transition actions that are defined by a plugin can be selected in the frontend. When the transition is processed and the action is performed, the plugin function which is registered at this callback is executed.

#### Configuring a transition callback

Register a callback in the `server` part of the plugin by defining it as a `transition_action`:

```python
def easydb_server_start(easydb_context):
    easydb_context.register_callback('transition_action', {
        'action_type': 'example_transition_action',
        'callback': 'example_transition_action'
    })
```

* `action_type` is the key to register the callback in the frontend part
* `callback` is the function that is executed when the action is performed

In the `webfrontend` part of the plugin, add the transition action by defining it in a coffeescript file:

```javascript
class ExampleTransitionAction extends TransitionActionAction

	getListViewColumn: ->
		type: CUI.Output
		text: "Example Plugin Action: set timestamp in text field"

	getSaveData: ->
		sd =
			type: ExampleTransitionAction.getType()
			info: {}

	@getType: ->
		"plugin.base.example-plugin.example_transition_action"

	@getDisplayName: ->
		"Example Plugin Action"

TransitionAction.registerAction(ExampleTransitionAction)
```

* `"plugin.base.example-plugin.example_transition_action"` links to the callback with `'action_type': 'example_transition_action'` in the plugin `plugin.base.example-plugin`
* `"Example Plugin Action"` is the name for this action in the frontend

#### Implementing a transition callback function

The function runs in the [Base-Context](). It can use functions that are defined in the context.

The function receives an array of objects. The data can be manipulated and must be returned by the function. The data is then saved in the database. The purpose of the transition callback is to manipulate or check objects, which have triggered a transition, before the data is inserted or updated.

The following example sets the current timestamp in a field in the object:

```python
# write the current timestamp into a text field
# assume that the objects are of objecttype 'obj' and have a text field 'timestamp'
def example_transition_action(easydb_context, data):

    for i in range(len(data['data'])):
        data['data'][i]['obj']['timestamp'] = str(datetime.now())
    return data['data']
```

This action can be added to transitions on the objecttype `obj` by selecting **"Example Plugin Action"** in the action select menu of the transition.

Transition callbacks are useful for transitions that are triggered by an **INSERT** or an **UPDATE** operation on objects.

### User IO Callbacks
<!-- TODO add description -->

- `sso_get_user`
<!-- TODO add description -->


## Example (Server Callback)

### Python Plugin Code

Plugins are realised in the form of a python script

```python
# function called at server start
# register server callbacks
def easydb_server_start(easydb_context):
    easydb_context.register_callback('db_pre_update', {
      'callback': 'pre_update_function'})

def pre_update_function(easydb_context, easydb_info):
    logger = easydb_context.get_logger('loggername')
    logger.debug('pre_update_function')
    data = easydb_info['data']
    data['name'] = "TEST-PLUGIN"
    return data
```

The Function `easydb_server_start` is called once at startup. In this function, callbacks are registered on the server. Depending on their type, the registered callbacks are then called when certain events occure.

In the sample code the function `pre_update_function` is registered to be called at ever `db_pre_update` event. Each time an object is created or changed, this function will be called and change the objects `name` field, setting it's value to `"TEST-PLUGIN"`.

### YAML Configuration

In order for the Script to be executable by the server a YAML defining the plugin is necessary.

```yaml
plugin:
  name: example_plugin
  version: 1.0
  server:
    api-version:
      require: 1

custom_events:
  - EASYDB_EXAMPLE_PLUGIN_EVENT

base_config:
  - name: example_plugin
    group: example_plugin
    require_system_right: plugin.example_plugin.allow_use_of_plugin
    unauthenticated_visible: false
    parameters:
      enabled:
        type: bool
        default: true
        position: 0
      select_number:
        type: select
        label: "select one of the following options"
        default: one
        options:
          - one
          - two
          - three
      street_numbers:
        type: table
        fields:
          - name: street
            type: text
            position: 0
          - name: number
            type: int
            position: 1

python-2:
  file: example_plugin.py
```

In this case was assumed that the plugin is called `example_plugin` and it's python script lies within the same directory as the YAML. The YAML configuration shown here contains the bare minimum of entries.

#### Defining custom events

A list of custom events that are defined by this plugin and extend the list of default server events.

Each entry in the list `custom_events` defines a key that can be used to identify a custom event that occured during the runtime of a process plugin.

To raise a custom event, the [`log_event`](server/python) method can be used to log an event in the event history in the server.

#### Defining base configuration

The plugin can define its own parameters for the [Basic configuration
](/en/webfrontend/administration/base-config/).

Each entry in `base_config` defines a group of base configuration parameters:

* `name` (string, mandatory): name of this config part
* `group` (string, mandatory): config group where this config part is located inside the base configuration
* `require_system_right` (string, optional): to be able to see this config part, the user needs this system right
* `unauthenticated_visible` (bool, optional): allow not authenticated sessions to see this config part
* `parameters`
    * Name (string, mandatory): name of the parameter
        * `type`: (mandatory): type of the parameter value
            * `bool`: `true/false` (Checkbox)
            * `email`: string, valid mail address
            * `file`: string, valid file path
            * `int`: 32 bit integer , max value: `0x7FFFFFFF`
            * `uint64`: 64 bit unsigned long integer, max value: `0xFFFFFFFFFFFFFFFF`
            * `select`: dropdown list
                * `options`: (list, mandatory) list of selectable options
            * `string-list`, `string-list-sort`
            * `table`: structured rows of different parameter values
            * `text`, `text-multiline`: single language text
            * `text-l10n`, `text-l10n-multiline`: multi language text
        * `default` (optional): default value for this parameter if it is not set in the frontend
        * `lable` (string, optional): lable value for this parameter
        * `position` (int, mandatory): order of the parameter in the frontend


#### Enabling the plugin in the server

Besides defining the plugin YAML it is necessary to alter the server YAML.
It must be extended in the following way:

```yaml
solution:
  name: beispiel-instanz
  plugins:
    - name: example_plugin
      file: plugins/example_plugin/example_plugin.yml

plugins:
  enabled+:
    - solution.beispiel-instanz.example_plugin
```

The entries `"solution"` as well as `"solution.name"` are by default already set.

The solution directory which contains the plugin files is structured like this in the example described:

```
Solution-Folder
│   solution.yml
│
└─── plugins
     │
     └─── example_plugin
          │   example_plugin.yml
          │   example_plugin.py
```

<!-- TODO explain l10n keys -->
