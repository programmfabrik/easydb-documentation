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

**easydb** provides a simple callback mechanism to use the plugin registry of the frontend plugins to register a Javascript webhook, executed by the **[node-runner](/en/technical/node-runner/))**.

Webhooks can be used to execute webhooks configured in transitions.

With the **webhook** and **example** plugins loaded, a simple web hook is provided:

**http://\<easydb-server\>/api/v1/plugin/base/webhook-plugin/webhook/example-plugin/example**

In order for this webhook to work, it's necessary to do the following steps:

	1. Configure the webhook in the configuration.yml:

	* The example plugin config looks like this:

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
	      secret_base_config: "example_plugin.webhook_secret"
	```

	* All webhooks use the **name** as their identifier.
		* The URL constructed will use the name of the plugin and the name of the webhook as path.
		* The [response](/en/technical/node-runner/#response) of the webhook will be given by the node-runner

	* To define a [HMAC secret](https://tools.ietf.org/html/rfc2104) to validate the integrity of the body of **POST** requests, set **secret_base_config**
		* The value is the key in the base config of the plugin:

		```yml
		base_config:
		  - name: example_plugin
		    group: example
		    parameters:
		      webhook_secret:
		        type: text
		        default: ""
		```

		* In this example, the webhook plugin will search the value for the secret in the base config at the key `base.system.example_plugin.webhook_secret`
		* If the secret is not empty, it will check the integrity using the *HTTP Header* `X-Hub-Signature: sha1=<hashed body>`
		* The plugin will hash the body using *SHA1* and compare it to `<hashed body>`
		* If there is no match, an *403* error is thrown

2. Create a javascript file following the [node-runner guidelines](/en/technical/node-runner/) and put it in build/webhooks/%webhook-name%.js

### Runtime information

The runtime information is passed to the `main` method of the javascript file as payload.

```coffeescript
class MyWebhook
	main: (payload) ->
		response = doSomething(payload.request, payload.config)
		return ez5.respondSuccess(response)

module.exports = new MyWebhook()

```
The payload contains the following things:

| key     | description                                                  |
| ------- | ------------------------------------------------------------ |
| config  | The current config of the easydb.                            |
| env     | A bare environment of the Node process. Contains NODE_MODULES only at the moment. |
| paths   | The paths node modules are loaded from.                      |
| plugin  | The full plugin configuration .yml.                          |
| request | The full information about the request, including query_string, preparsed parameters, method, etc. |

## Example

[Example webhook](https://github.com/programmfabrik/easydb-plugin-examples/blob/master/src/webhooks/Example.coffee) is a working example which bounces back the whole payload received.

It also returns different things if some parameters are included in the request.

| parameter     | description                                                    |
| ------- | ---------------------------------------------------------------------|
| dump_request=%file-location%  | Dumps the payload's request body to any file |
| ascii=%some-text%  | Returns the same text using [ascii art](https://github.com/olizilla/asciify)                            |

## Transition Webhook

Webhooks can be triggered asynchronously from easydb using configuration in **Base-Config** and **Workflow**.

Configuration steps:

1. Configure a Webhook in the base config, give it a name and an URL for the callback. To secure the call you can use an HMAC secret to encrypt the body.
2. Reload the frontend
3. Configure a Workflow in **Tags & Workflows**

The script we are using is the [Example webhook](https://github.com/programmfabrik/easydb-plugin-examples/blob/master/src/webhooks/Example.coffee)

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

