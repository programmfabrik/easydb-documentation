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

## Configuration

The configuration is split into two parts. For the server configuration, see [Auto Keyworder configuration](/en/sysadmin/configuration/easydb-server.yml/plugins/auto-keyworder/). The configuration in the [base configuration](/en/webfrontend/administration/base-config/) is described here:

### Base Configuration

All AI services are configured in the base config in the "Auto Keyworder" tab.

The Plugin checks the base config for changes with a delay of `baseconfig_poll_interval_sec` seconds after any currently running worker has finished. This value is defined in the server configuration.

* **Service active**
    - Enable/disable the complete Auto-Keyworder process

* **Start update process after saving**
    - Enable this to ignore the calculated next run time of the workers. Instead, start as soon as possible after the base configuration was saved
    - Internal representation: value `start_now` , which can also be set by an API call (see below)
    - This value is **not persistent** but only valid once. Every time it is set to `True` , the plugin sets this value to `False` after it is read

* **easydb API user** and **easydb API user password**
    - _mandatory_ (if **easydb API Session Token** is not set)
    - Login and password of a special user which can perform searches and object updates in easydb
    - This plugin uses the easydb API endpoints `/api/v1/search` and `/api/v1/db`
    - The user needs at least the following rights on objecttypes (or pools repectively):
        - `write` right on all objecttypes that are configured for updating
        - `mask` right on a mask that allows editing of all fields that are updated
        - `asset_show` right on the selected asset fields, so the plugin can transfer the image data to the AI service
        - `bag_read` on the pool if the objects are pool managed
        - if the keywords are stored in linked objects, the user needs the following rights on the linked objecttype(s):
            - `read` to be able to search for existing linked objects
            - `mask` right on a mask that allows reading and writing the value of the keyword text field
            - `create` right to be able to create new linked objects

* **easydb API Session Token**
    - _mandatory_ (if **easydb API user** and **easydb API user password** are not set)
    - Authenitcated token of the user which can perform searches and object updates in easydb
    - If this is set, **easydb API user** and **easydb API user password** are ignored

### Configurations for different services

Configurations for different services and objecttype setups are saved in multiple configuration blocks:

* **Enable this configuration** ( `true/false` )
    - Enable/disable this configuration block

* **Name of this configuration**
    - _optional_
    - To help debugging, you can give a specific name for this configuration

* **Service**
    - The AI service provider
    - Currently, only Cloudsight.ai is implemented

* **API Key**
    - The API Key for the service provider
    - Depending on the API, this can be mandatory
    - Cloudsight.ai requires an API Key

* **Objecttype**
    - _mandatory_
    - Objecttype for updating keywords
    - Only objecttypes with the following requirements can be selected:
        - At least one asset (image)
        - At least one text field (on top level, in a nested table or in a linked object in a nested table) where the generated keywords are saved
        - At least one datetime field where the timestamp of the last successful update of the object is saved

* **Target field for image subject**
    - _optional_
    - Text field where the image subject is saved

* **Target field for keywords**
    - _mandatory_
    - Text field where keywords are saved
    - If the field is in a nested table, each keyword is saved in a new row, else the keywords are comma separated
    - If the field is a multi language field, the keywords are saved for the specified language (see below)
    - If the field is in a linked object, the plugin searches if a linked object with the keyword already exisits. If not, a new object is created before linking it to the updated object

* **Target field for timestamp**
    - _mandatory_
    - must be a datetime field to store a complete timestamp
    - After a object was successfully updated, the timestamp is saved in this field
    - Only objects are searched where this field is unset, or where the timestamp is older than the specified max age (see below)

* **Tagfilter to mark objects for auto keyword generation**
    - _mandatory_
    - Define a tag filter to mark objects that should be updated
    - Only objects are searched where the specfified tags are set / unset respectively

* **Minimal age since the last keyword generating**
    - _mandatory_
    - Time since this object was last updated, in days
    - Only objects are searched where the timestamp field is unset, or where the timestamp is older than this age
    - Minimum: `1`
    - Defaults to `7`
    - If you want to overwrite data in objects that were updated too recently, you have to delete this timestamp in the objects

* **Language for Keywords**
    - _mandatory_
    - Language in which the keywords are requested
    - Depending on the AI service, the language can be used
    - The following languages are usable:
        - german: `de-DE`
        - english: `en-US`
        - spanish: `es-ES`
        - italian: `it-IT`
        - arabic: `ar`
        - czech: `cs-CZ`
        - farsi (persian): `fa`
        - french: `fr-FR`
        - japanese: `ja-Jpan`
        - georgian: `ka-GE`
        - korean: `ko-Kore`
        - dutch: `nl-NL`
        - polish: `pl-PL`
        - russian: `ru-RU`
        - chinese: `zh-Hans`
    - Language settings for Cloudsight.ai:
        - The language is sent via the API
        - The subject ( `name` ) of the analyzed image is returned in this language
        - The keywords are returned in the language that is configured in the Cloudsight project for the given API key. **This configuration is separate and independant from easydb**.
        - For best results, the language in which the Cloudsight project is configured should be selected, so that the keywords and the subject are saved in the same language

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
