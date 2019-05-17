---
title: "Node runner"
menu:
  main:
    name: "Node runner"
    identifier: "technical/node-runner"
    parent: "technical"
---

# Node runner

The node runner is a small node application that is used to invoke javascript code from the server.

At the moment it's used by two easydb features: [automatic updater for custom data types](/en/technical/plugins/customdatatype/customdatatype_updater/) and [webhooks](https://docs.easydb.de/en/technical/plugins/webhooks/webhook/#webhooks)

### Usage

The javascript code needs to export a `main` method that will be used as entry point by the *node-runner*.

The method `main` receives one parameter which is the **payload**, and its **structure** varies depending on the plugin.

To return data it's necessary to use the method `ez5.respondSuccess` or `ez5.respondError`, because those two methods wrap the data that you want to return and write it to the standard output because that's how the **easydb-server** communicates with the **node-runner**.

#### ez5.respondSuccess

Receives two parameters: `body` and `statusCode` (default value `200`)

#### ez5.respondError

Receives three parameters: `messageCode`, `parameters` (default value `{}`) and `statusCode` (default value `400`)

The parameters `messageCode` and `parameters` are explained [here](/en/technical/errors/)

#### Response

The node-runner's response have the following structure.

| key         | description                                                  |
| ----------- | ------------------------------------------------------------ |
| headers     | key, value Map with the HTTP-Headers to be set. There is only one value per key possible. |
| status_code | The status code for the HTTP response.                                                    |
| body        | Body used in ez5.respondSuccess and ez5.respondError. It could be any type since it will be converted into a string.|

### Dependencies

The node-runner provides a few dependencies that can be used via `required()`, but it is also possible to add own dependencies.

#### Own dependencies

It's necessary to have a `node_modules` directory (which should be created by using `npm`) in the build directory of the plugin.

The [Example webhook](https://github.com/programmfabrik/easydb-plugin-examples/blob/master/src/webhooks/Example.coffee) is a good example to see how to set it up correctly.

#### Provided dependencies
- [axios](https://github.com/axios/axios)
- [coffeescript-ui](https://github.com/programmfabrik/coffeescript-ui)
- ez5 (for now, it provides the two methods mentioned above)

It is not necessary to require the dependencies `coffeescript-ui` and `ez5` because they can be accessed globally via `CUI` and `ez5` respectively.

The dependency [coffeescript-ui](https://github.com/programmfabrik/coffeescript-ui) provides useful methods. For example [CUI.util.*](https://programmfabrik.gitbooks.io/coffeescript-ui/base/util.html)

### Examples

Basic coffeescript example
```javascript
class CoffeescriptExample
	main: (payload) ->
		return ez5.respondSuccess(payload)
		
module.exports = new CoffeescriptExample()
```

More examples:

- [Gazetteer custom data type](https://github.com/programmfabrik/easydb-custom-data-type-gazetteer/blob/master/src/script/GazetteerUpdate.coffee)
- [Example webhook](https://github.com/programmfabrik/easydb-plugin-examples/blob/master/src/webhooks/Example.coffee)


