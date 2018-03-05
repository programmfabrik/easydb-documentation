# Plugins

Plugins allow for an extension of easydb functionality. They are easily integratged into the Server through it's YAML and defined by YAML files themselves.

Plugin functionality includes:

 * creating frontend apps
 * defining system rights
 * define or replace localization keys
 * define server callbacks

Inside Plugins, callbacks can be used to execute functions inside the server. An overview over the callbacks and the contexts in which they can be used, as well as Exceptions that can be used to display different Error types, can be found [here](python/python_callbacks.md).

## Client:

Frontend apps are Javascript applications that run client-side and can be integrated into the easydb Interface as top level apps in the sidebar or as popovers opened from within the user tray.

## Web frontend

### Available plugins
* [Custom data types](./webfrontend/custom-data-type/custom-data-type-plugin.html)
* [Detail sidebar plugin](./webfrontend/detail-sidebar/detail-sidebar-plugin.html)
* [Export manager plugin](./webfrontend/export-manager/export-manager-plugin.html)

## Server-Callbacks:
<!-- TODO improve docu, see #45444 -->

Server-Callbacks are Python scripts, that are run in specific situations in a standardized procedure. The plugin registers a function at the server. From then on everytime a certain event happens, the server calls this function.

The server calls the function with information to be processed and expects a response with altered content for further use. Alternatively, if the plugin is used to validate data, for example an `EasydbException` can be raised when data is invalid. This way a database transaction can be aborted so that no invalid data is saved in the database.

An `api_db_pre_update` callback for example receives the data entered by a user when a `POST api/db` call is made, alters the data if necessary, and passes it to the server. From here on the altered data is processed as it would have been without the plugin.

Server callbacks are able to throw easydb errors like "The user has insufficient rights for ..." It is also possible to define custom error types, which will be displayed in the frontend properly and localized.

Server callbacks have access to many of easydb's internal information and tools.
They may for example alter an open database transaction of a frontend request, read the base configuration, or request open sessions (which user, what rights?).

### Process Callbacks

Register a Plugin as a process that runs inside the server.

* type: `process`

The Plugin process is started when the server calls the `run` method, and stops with the server. The `stop` method is used to clean up before the server and the Plugin process stop. In the `run` method, threads can be started to repeatedly execute tasks parallel to the server runtime.

#### Example

```python
def easydb_server_start(easydb_context):
    easydb_context.register_callback('process', {'name': 'process_example'})

# define a funtion that is repeatedly executed while the server runs
def process_function():
    # do something
    pass

# start a simple thread in the run method
def run(easydb_context):
    t = Thread(target=process_function, args=(i,))
    t.start()

# use the stop method to clean up plugin resources before the server stops
def stop(easydb_context):
    # do some cleanup
    pass
```

### API Callbacks

API Callbacks are used to extend the Server API. Registered Callbacks create new API Endpoints.

* type: `api`

The URL of an added Endpoint is `<Server URL>/api/plugin/base/<Plugin Name>/<Callback Name>`.

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
        "body": json.dumps(easydb_context.get_instance(), indent=4),
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

* types:

  * `export_produce`

    * called after an export finished writing data to the file system. The saved data can be manipulated or checked, before the Export is finished.

  * `export_transport`
  <!-- TODO add description -->

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

* Callbacks before data is updated or deleted. Validate the content of the data before it is saved/deleted in the database. Manipulate data before it is saved in the database.

  * `db_pre_update_one`
    * called before one object is saved in the database
    * called once for each object

  * `db_pre_update`
    * called before objects is saved in the database
    * called for all objects at once

  * `db_pre_delete_one`
    * called before one object is deleted from the database
    * called once for each object

  * `db_pre_delete`
    * called before objects are deleted from the database
    * called for all objects at once

* Callbacks after data was updated or deleted.

  * `db_post_update_one`
    * called after one object was saved in the database
    * called for all objects at once

  * `db_post_update`
    * called after objects were saved in the database
    * called once for each object

  * `db_post_delete_one`
    * called after one object was deleted from the database
    * called once for each object

  * `db_post_delete`
    * called after objects were deleted from the database
    * called for all objects at once


### User Callbacks

* `user_post_update`
<!-- TODO add description -->

### Transition Callbacks

Transition actions defined by a plugin are realised using this callback

* `transition_action`
<!-- TODO add description -->

### User IO Callbacks
<!-- TODO add description -->

* `sso_get_user`
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
    data = easydb_context['data']
    data['name'] = "TEST-PLUGIN"
    return data
```

The Function `easydb_server_start` is called once at startup. In this function, callbacks are registered on the server. Depending on their type, the registered callbacks are then called when certain events occure.

In the sample code the function `pre_update_function` is registered to be called at ever `db_pre_update` event. Each time an object is created or changed, this function will be called and change the objects `name` field, setting it's value to `"TEST-PLUGIN"`.

### YAML Configuration

In order for the Script to be executable by the server a YAML defining the plugin is necessary.

```
plugin:
  name: example_plugin
  version: 1.0
  server:
    api-version:
      require: 1
python-2:
  file: example_plugin.py
```

In this case was assumed that the plugin is called `example_plugin` and it's python script lies within the same directory as the YAML. The YAML configuration shown here contains the bare minimum of entries.


Besides defining the plugin YAML it is necessary to alter the server YAML.
It must be extended in the following way:

```
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
