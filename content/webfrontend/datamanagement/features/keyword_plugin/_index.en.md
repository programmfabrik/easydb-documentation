---
title: "88 - Auto Keyworder Plugin"
menu:
  main:
    name: "Auto Keyworder Plugin"
    identifier: "webfrontend/datamanagement/features/keyword_plugin"
    parent: "webfrontend/datamanagement/features"
---

# Auto Keyworder Plugin

> NOTE: This Plugin is licensed as a separate Module. Please check you license contract.

The Auto Keyworder Plugin is a process (background) plugin which periodically posts image data of objects to online AI services to detect the image content, and update objects with auto generated keywords and subjects.

Currently, the following AI services are implemented:

* Cloudsight: https://cloudsight.ai

A description of the options of the plugin "Cloudsight" can be found in the [base configuration](../../../administration/base-config/auto_keyworder/).



## Plugin API

The plugin provides a new endpoint for the easydb API: `api/plugin/base/auto-keyworder/start_now`.

This API can be called with a GET/POST request with an empty body. If the request is authenticated, the `start_now` flag in the base configuration is set to `true`. The next time the base configuration is loaded, this flag causes the worker loops to start immediatly. The behaviour is the same as if you enable the **Start update process after saving** checkbox in the base configuration in the frontend.

### Authentication

The api requires an authentication with a HMAC signature. The body of the request must be encrypeted with the HMAC secret using SHA1 and the signature must be supplied in hexadecimal format. The signature must be included in the request header `X-Hub-Signature`:

```
    -H 'X-Hub-Signature: sha1=69a026d1baf79cc241ca82ffc4d47a6ee7d01337'
```

The HMAC secret must be the same that is configured in the server configuration `system.auto_keyworder.webhook_hmac`. If this value is not set in the server configuration, the API can not be used.

### Using the API with an easydb transition (workflow)

To automatically call this API and start a background update process after objects with tags have been inserted/updated, you can configure a webhook that is registered as the action of a workflow.

1. In the base configuration, add a webhook configuration under "Tag & Workflow" with the following settings:
    * **URL**: `<easydb url>/api/plugin/base/auto-keyworder/start_now`
    * **HMAC secret**: Value of `system.auto_keyworder.webhook_hmac` from the [server configuration](/en/sysadmin/configuration/easydb-server.yml/plugins/auto-keyworder/)

2. See [easydb documentation: Workflows](/en/webfrontend/rightsmanagement/tags/#a-nameworkflows-a-workflows) how to setup a workflow. For each of the configuration blocks for services, a workflow should have the following settings:
    * **Operation**: Insert and Update
    * **Type**: NORMAL
    * **Object Types**: select the objecttypes that is configured in the service configuration
    * **Users/Groups**: select groups or users that should be able to trigger this workflow
        * **DO NOT** select the user that is configured in the base configuration for the API usage of the plugin! This can create an endless loop of updates of objects!
    * **Tags After saving**: the tagfilter should be the same as the tagfilter in the service configuration
    * **Actions**: one of the actions should be the webhook action with the webhook that is configured to call the plugin API endpoint `/start_now`
