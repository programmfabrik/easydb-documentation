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
* [Custom data types](./reference/webfrontend/custom-data-type/custom-data-type-plugin.html)
* [Detail sidebar plugin](./reference/webfrontend/detail-sidebar/detail-sidebar-plugin.html)
* [Export manager plugin](./reference/webfrontend/export-manager/export-manager-plugin.html)

## Server-Callbacks:
<!-- TODO improve docu, see #45444 -->

Server-Callbacks are Python scripts, that are run in specific situations in a standardized procedure. The plugin registers a function at the server. From then on everytime a certain event happens, the server calls this function.

The server calls the function with information to be processed and expects a response with altered content for further use. Alternatively, if the plugin is used to validate data, for example an `EasydbException` can be raised when data is invalid. This way a database transaction can be aborted so that no invalid data is saved in the database.

An `api_db_pre_update` callback for example receives the data entered by a user when a `POST api/db` call is made, alters the data if necessary, and passes it to the server. From here on the altered data is processed as it would have been without the plugin.

Server callbacks are able to throw easydb errors like "The user has insufficient rights for ..." It is also possible to define custom error types, which will be displayed in the frontend properly and localized.


### Overview of server callbacks:

* General callbacks: e.g. server start and stop
* API callbacks: API extensions defined in a plugin
* Extension points: On occurence of certain events the plugin can alter the outcome of an action, e.g after a `POST /api/db` call
* Transition extensions: Transition actions defined by a plugin are realised using this callback
* Export extensions: Allows plugins to define transport types and export extensions

Server callbacks have access to many of easydb's internal information and tools.
They may for example alter an open database transaction of a frontend request, read the base configuration, or request open sessions (which user, what rights?)


## Callback Types
<!-- TODO add description -->

### Process Callbacks
<!-- TODO add description -->

* `process`
<!-- TODO add description -->

### API Callbacks
<!-- TODO add description -->

* `api`
<!-- TODO add description -->

### Export Callbacks

Callbacks for Exports <!-- TODO add description -->

* `export_produce`
  * called after an export finished writing data to the file system. The saved data can be manipulated or checked, before the Export is finished.

* `export_transport`
<!-- TODO add description -->

### Database Callbacks

Callbacks that are called before and after database updates. The data can be validated and manipulated before it is saved in the database.

* `db_pre_update_one`
  * called before one object is saved in the database
  * called once for each object

* `db_pre_update`
  * called before objects is saved in the database
  * called for all objects at once

* `db_post_update_one`
  * called after one object was saved in the database
  * called for all objects at once

* `db_post_update`
  * called after objects were saved in the database
  * called once for each object

* `db_pre_delete_one`
  * called before one object is deleted from the database
  * called once for each object

* `db_pre_delete`
  * called before objects are deleted from the database
  * called for all objects at once

* `db_post_delete_one`
  * called after one object was deleted from the database
  * called once for each object

* `db_post_delete`
  * called after objects were deleted from the database
  * called for all objects at once

* `user_post_update`
<!-- TODO add description -->

### Transition Callbacks
<!-- TODO add description -->

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
