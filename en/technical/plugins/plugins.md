# Plugins


Plugins allow for an extension of easydb functionality. They are easily integratged into the Server through it's YAML and defined by YAML files themselves.

Plugin functionality includes:

 * creating frontend apps
 * defining system rights
 * define or replace localization keys
 * define server callbacks

## Client:


Frontend apps are Javascript applications that run client-side and can be integrated into the easydb Interface as top level apps in the sidebar or as popovers opened from within the user tray.

## Server-Callbacks:


Server-Callbacks are Python scripts, that are run in specific situations in a standardized procedure. The plugin registers a function at the server. From then on everytime a certain event happens, the server calls this function.
The server calls the function with information to be processed and expects a response with altered content for further use.
An "api_db_pre_update" callback for example receives the data entered by a user when a POST api/db call is made, alters the data if necessary, and passes it to the server. From here on the altered data is processed as it would have been without the plugin.

Server callbacks are enabled to throw easydb errors like "The user has insufficient rights for ..." It is also possible to define custom error types, which will be displayed in the frontend properly and localized.


This is an overview of server callbacks:

* General callbacks: e.g. server start and stop
* API callbacks: API extensions defined in a plugin
* Extension points: On occurence of certain events the plugin can alter the outcome of an action, e.g after a POST /api/db call
* Transition extensions: Transition actions defined by a plugin are realised using this callback
* Export extensions: Allows plugins to define transport types and export extensions


Server callbacks have access to many of easydb's internal information and tools.
They may for example alter an open database transaction of a frontend request, read the base configuration, or request open sessions (which user, what rights?)


## Callback Typen/Callback Types

* register_callback "process"

* register_callback "api"

* register_callback "export_transport"

* register_callback "export_produce"

* register_callback "db_pre_update_one"

* register_callback "db_pre_update"

* register_callback "db_post_update"

* register_callback "db_pre_delete"

* register_callback "db_post_delete"

* register_callback "user_post_update"

* register_callback "transition_action"

* register_callback "sso_get_user"

##Example (Server Callback) 

### Plugin Code
#### Python

Plugins are realised in the form of a python script

```python
def easydb_server_start(easydb_context):
    easydb_context.register_callback('db_pre_update', {'callback': 'pre_update_function'})


def pre_update_function(easydb_context, easydb_info):
    logger = easydb_context.get_logger('helmsmuseum')
    logger.debug('pre_update_function')
    data = easydb_context['data']
    data['name']="TEST-PLUGIN"
    return data
```

The Function "easydb_server_start" is called once at startup. In this function,
callbacks are registered on the server. Depending on their type, the registered callbacks are then called when certain events occure.
In the sample code the function "pre_update_function" is registered to be called at ever "db_pre_update" event. Each time an object is created or changed, this function will be called and change the objects "name" field, setting it's value to "TEST-PLUGIN"

#### YAML

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

In this case was assumed that the plugin is called "example_plugin" and it's python script lies within the same directory as the YAML. The YAML configuration shown here contains the bare minimum of entries.


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

The entries "solution" as well as "solution.name" are by default already set.

The solution directory which contains the plugin files is structured like this in the example described:

```
Solution-Folder
│   solution.yml
│
└───plugins
    │
    └───example_plugin
        │   example_plugin.yml
        │   example_plugin.py


```


