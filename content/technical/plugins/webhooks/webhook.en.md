---
title: "Webhooks"
menu:
  main:
    name: "Webhooks"
    identifier: "technical/plugins/webhooks"
    parent: "technical/plugins"
---

# Webhooks

## Javascript / Coffeescript Plugin

**easydb** provides a simple callback mechanism to use the plugin registry of the frontend plugins to register a Javascript web hook, executed by **[Node.js](https://nodejs.org/en/)**.

Webhooks can be used to execute webhooks configured in transitions.

With the example plugin loaded, a simple web hook is provided:

**http://\<easydb-server\>/api/v1/plugin/base/webhook-plugin/webhook/example-plugin/example**

In order for this webhook to work, the plugin needs to do the following things:

* Configure the webhook in the configuration.yml
* Put a .js file in build/webhooks/<name of hook>.js

The example plugin config looks like this:

```yml
plugin:
  name: example-plugin
  version: 1.0
  url: https://github.com/programmfabrik/easydb-plugin-examples
  displayname:
    de-DE: Example Plugin
    en-US: Example Plugin
  info:
    de-DE: "Das Beispiel Plugin für **easydb**."
    en-US: "An example plugin for **easydb**."
  webhooks:
    - name: example
```

All webhooks use the **name** as their identifier.

The URL constructed will use the name of the plugin and the name of the webhook as path.

The webhook needs to a Json map to the console. That map will be used to build the response.

| key         | description                                                  |
| ----------- | ------------------------------------------------------------ |
| headers     | key, value Map with the HTTP-Headers to be set. There is only one value per key possible. |
| status_code | The status code for the HTTP response.                       |
| body        | The body of the respsone.                                    |

For json output a convenience method **ez5.returnJsonBody(body)** is provided. This needs the **ez5** module to be required.

### Runtime information

The runtime information is passed to the Node and can be retrieved using

```coffeescript
info = JSON.parse(process.argv[2])
```

There is plenty of information available:

| key     | description                                                  |
| ------- | ------------------------------------------------------------ |
| config  | The current config of the easydb.                            |
| env     | A bare environment of the Node process. Contains NODE_MODULES only at the moment. |
| paths   | The paths node modules are loaded from.                      |
| plugin  | The full plugin configuration .yml.                          |
| request | The full information about the request, including query_string, preparsed parameters, method, etc. |

### Example script

```coffeesript
ez5 = require('ez5')

class Example
	sayHello: ->
		info = JSON.parse(process.argv[2])

		info.paths = module.paths
		info.env = process.env

		ez5.returnJsonBody(info)
(->
	new Example().sayHello()
)()
```

This script bounces back all information which is passed to the node process.

All information about the request can be found in 

## Transition Webhook

Webhooks can be triggered asynchronously from easydb using configuration in **Base-Config** and **Workflow**.

Configuration steps:

1. Configure a Webhook in the base config, give it a name and an URL for the callback. To secure the call you can use an HMAC secret to encrypt the body.
2. Reload the frontend
3. Configure a Workflow in **Tags & Workflows**

The script we are using is the Example webhook. 

Use the URL **http://\<easydb-server\>/api/v1/plugin/base/webhook-plugin/webhook/example-plugin/example?dump_request=/tmp/dump_to_file** to append the transition request to any file.

The information provided by the callback includes the system_object_id and version of the changed object.

### INSERT

```json
{
    "action": "transition",
    "operation": "INSERT",
    "objects": [
        {
            "_system_object_id": 6,
            "_uuid": "4e276553-ac87-4dc5-9832-ef2e0c83c1c8",
            "_objecttype": "thing",
            "thing": {
                "_id": 4,
                "_version": 1
            }
        }
    ]
}
```

### UPDATE

```json
{
    "action": "transition",
    "operation": "UPDATE",
    "objects": [
        {
            "_system_object_id": 5,
            "_uuid": "45460c4e-e7a1-4452-94f3-fdd8c90b638d",
            "_objecttype": "thing",
            "thing": {
                "_id": 3,
                "_version": 10
            }
        }
    ]
}
```

### DELETE

```json
{
    "action": "transition",
    "operation": "DELETE",
    "objects": [
        {
            "_system_object_id": 6,
            "_uuid": "4e276553-ac87-4dc5-9832-ef2e0c83c1c8",
            "_objecttype": "thing",
            "thing": {
                "_id": 4,
                "_version": 0
            }
        }
    ]
}

```

A webhook for a transition can now use the API of easydb to retrieve information about the object and start a publishing process using **/api/publish**.

