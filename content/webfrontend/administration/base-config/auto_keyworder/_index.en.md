---
title: "152 - Auto Keyworder"
menu:
  main:
    name: "Auto Keyworder"
    identifier: "webfrontend/administration/base-config/auto_keyworder"
    parent: "webfrontend/administration/base-config"
---

# Auto Keyworder

> **Please note:** This Plugin is licensed as a separate Module. Please check you license contract.

The Auto Keyworder Plugin is a process (background) plugin which periodically posts image data of objects to online AI services to detect the image content, and update objects with auto generated keywords and subjects.

Currently, wrappers for the following AI services are implemented:

|  | Homepage | External API Documentation |
|---|---|---|
| **Cloudsight** | https://cloudsight.ai | https://cloudsight.docs.apiary.io |
| **DeepVA** | https://deepva.ai | https://docs.deepva.com |
| **Imagga** | https://imagga.com | https://docs.imagga.com |


## Base Configuration

All AI services are configured in the base config in the 'Auto Keyworder' tab.

The Plugin checks the base config for changes with a delay `baseconfig_poll_interval_sec` after any currently running worker has finished.

| Configuration | Mandatory | Default | Description |
|---|---|---|---|
| Service active | yes | `False` | Enable/disable the complete Auto-Keyworder process |
| Start update process after saving | | `False` | <ul><li>Enable this to ignore the calculated next run time of the workers. Instead, start as soon as possible after the base configuration was saved</li><li>Internal representation: value `start_now`, which can also be set by an API call (see [Plugin API](/en/webfrontend/datamanagement/features/plugins/autokeyworder/#plugin-api))</li><li>This value is **not persistent** but only valid once. Every time it is set to `True`, the plugin sets this value to `False` after it is read</li><li>This checkbox will still be enabled after saving until the base config is reloaded in the frontend</li></ul> |
| easydb API user</br></br>easydb API user password | yes | | <ul><li>Login and password of a special user which can perform searches and object updates in easydb</li><li>This plugin uses the easydb API endpoints `/api/v1/search`, `/api/v1/db` and `/api/v1/event`</li><li>The user needs at least the following rights on objecttypes (or pools respectively):</li><ul><li>`write` right on all objecttypes that are configured for updating</li><li>`mask` right on a mask that allows editing of all fields that are updated</li><li>`asset_show` right on the selected asset fields, so the plugin can transfer the image data to the AI service</li><li>`bag_read` on the pool if the objects are pool managed</li><li>if the keywords are stored in linked objects, the user needs the following rights on the linked objecttype(s):<ul><li>`read` to be able to search for existing linked objects</li><li>`mask` right on a mask that allows reading and writing the value of the keyword text field</li><li>`create` right to be able to create new linked objects</li></ul></li></ul> |
| Status request repitions | yes | `3` | maximum number of requests of the status of the analyzing of an image before the keywording for the image is discarded |
| Status request delay | yes | `5` | minimum delay in seconds between repeated status requests for an image |


### Configurations for each service

Configurations for different services and objecttype setups are saved in multiple configuration blocks. These settings are the same for all services, but each service has more different settings.

| Configuration | Mandatory | Default | Description |
|---|---|---|---|
| Enable this configuration | yes | `False` | Enable/disable this configuration block |
| Name of this configuration | | | To help debugging, you can give a specific name for this configuration |
| API URL | yes | | <ul><li>The base URL of the API of the service</li><li>It should not be different from the default URL that is given</li><li>If there should be another URL for this service, there might also be other breaking changes in the API and this service **might not work at all**!</li></ul> |
| API Key | Depending on the API, this can be mandatory | | The API Key for the service provider |
| Objecttype | yes | | <ul><li>Objecttype for updating keywords</li><li>Only objecttypes with the following requirements can be selected:</li><ul><li>At least one asset (image)</li><li>At least one text field (on top level, in a nested table or in a linked object in a nested table) where the generated keywords are saved</li><li>At least one datetime field where the timestamp of the last successful update of the object is saved</li></ul></li><li>Tag management should be activated if a tag filter is used (see below)</li></ul> |
| Asset field | yes | | <ul><li>Asset field from which the image is taken and uploaded</li><li>**Please note:** it is important that this field is enabled for the expert search in the standard mask</li></ul> |
| Asset version | yes | `original` | <ul><li>Asset Version that is uploaded, can be any existing version, but needs to be a valid image format</li><li>a minimum size per side is recommended, smaller images can cause errors in detection due to lower resolution, so the "preview" or "small" version should be avoided</li><li>**Please note:** the asset versions are protected under rights management. Make sure that the plugin user has at least `read` rights on the selected asset version. Otherwise, the plugin can **not** upload the asset in this version to the service provider</li></ul> |
| Target field for timestamp | yes | | <ul><li>Must be a datetime field to store a complete timestamp</li><li>After a object was successfully updated, the timestamp is saved in this field</li><li>Only objects are searched where this field is unset, or where the timestamp is older than the specified max age (see below)</li><li>**Please note:** it is important that this field is enabled for the expert search in the standard mask</li></ul> |
| Tagfilter to mark objects for auto keyword generation | optional but recommended | | <ul><li>Define a tag filter to mark objects that should be updated</li><li>Only objects are searched where the specfified tags are set / unset respectively</li></ul> |
| Minimal age since the last keyword generating | yes | `7` | <ul><li>Time since this object was last updated, in days</li><li>Only objects are searched where the timestamp field is unset, or where the timestamp is older than this age</li><li>If you want to overwrite data in objects that were updated too recently, you have to delete this timestamp in the objects</li></ul> |


### Configurations for different services

#### Configurations for Cloudsight

| Configuration | Mandatory | Default | Description |
|---|---|---|---|
| Target field for image subject | | | Text field where the image subject is saved |
| Target fields for keywords:<ul><li>similar objects</li><li>category</li><li>quantity</li><li>gender</li><li>material</li><li>color</li></ul> | | | <ul><li>Fields where different parts of structured output from responses from the Cloudsight API are saved</li><li>If any of these structured outputs is present in the response, these special fields are filled</li><li>If the field is in a nested table, each keyword is saved in a new row, else the keywords are comma separated</li><li>If the field is a multi language field, the keywords are saved for the specified language (see below)</li><li>If the field is in a linked object, the plugin searches if a linked object with the keyword already exisits, else a new object is created before linking it to the updated object</li></ul> |
| Language | | english | <ul><li>Language in which the keywords are requested</li><li>The language parameter is sent via the API</li><li>The subject (`name`) of the analyzed image is returned in this language</li><li>The keywords are returned in the language that is configured in the Cloudsight project for the given API key. **This configuration is separate and independant from easydb5!**.</li><li>For best results, the language in which the Cloudsight project is configured should be selected, so that the keywords and the subject are saved in the same language</li><li>The following languages are available:<ul><li>german: `de-DE`</li><li>english: `en-US`</li><li>spanish: `es-ES`</li><li>italian: `it-IT`</li><li>arabic: `ar`</li><li>czech: `cs-CZ`</li><li>farsi (persian): `fa`</li><li>french: `fr-FR`</li><li>japanese: `ja-Jpan`</li><li>georgian: `ka-GE`</li><li>korean: `ko-Kore`</li><li>dutch: `nl-NL`</li><li>polish: `pl-PL`</li><li>russian: `ru-RU`</li><li>chinese: `zh-Hans`</li></ul></li></ul> |

#### Configurations for DeepVA

| Configuration | Mandatory | Default | Description |
|---|---|---|---|
| Target field | | | <ul><li>Field where labels from responses from the DeepVA API are saved</li><li>If the field is in a nested table, each keyword is saved in a new row, else the keywords are comma separated</li><li>If the field is a multi language field, the keywords are saved in the default response language (`en-US`)</li><li>If the field is in a linked object, the plugin searches if a linked object with the keyword already exisits, else a new object is created before linking it to the updated object</li></ul> |
| Maximum number of keywords | | `5` | If there are more labels in the response, only use the first `n` labels |
| Modules and Models | | | <ul><li>DeepVA offers different pre-trained models to label images</li><li>At least one module and model must be specified</li><li>All models and modules are applied to an uploaded image</li><li>Use this to control the content of the labels</li><li>**Different models are pre-trained for different purposes, make sure to choose the correct models depending on the expected content of the images!**</li><li>Please refer to the external documentation: <a href="https://docs.deepva.com/core-resources/model/#pre-trained-models">https://docs.deepva.com/core-resources/model/#pre-trained-models</a> </li></ul> |

#### Configurations for Imagga

| Configuration | Mandatory | Default | Description |
|---|---|---|---|
| API Secret | yes | | Additionaly to the API Key, the Imagga API also requires an API Secret |
| Target field | | | <ul><li>Field where tags from responses from the Imagga API are saved</li><li>If the field is in a nested table, each keyword is saved in a new row, else the keywords are comma separated</li><li>If the field is a multi language field, the keywords are saved for the specified language (see below)</li><li>If the field is in a linked object, the plugin searches if a linked object with the keyword already exisits, else a new object is created before linking it to the updated object</li></ul> |
| Maximum number of keywords | | `5` | If there are more labels in the response, only use the first `n` labels |
| Minimum Confidence | yes | `75` | <ul><li>The API returns a confidence value for each keyword (percentage: `1` - `100`)</li><li>Keywords which do not reach this confidence value are ignored.</li></ul> |
| Language | | english | <ul><li>Language in which the keywords are requested</li><li>The language parameter is sent via the API</li><li>The tags of the analyzed image are returned in this language</li><li>The following languages are available:<ul><li>english: `en-US`</li><li>german: `de-DE`</li><li>arabic: `ar`</li><li>catalan: `ca`</li><li>czech: `cs-CZ`</li><li>spanish: `es-ES`</li><li>farsi (persian): `fa`</li><li>finnish: `fi-FI`</li><li>french: `fr-FR`</li><li>hebrew: `he`</li><li>hindi: `hi`</li><li>italian: `it-IT`</li><li>japanese: `ja-Jpan`</li><li>korean: `ko-Kore`</li><li>dutch: `nl-NL`</li><li>polish: `pl-PL`</li><li>portuguese: `pt`</li><li>russian: `ru-RU`</li><li>swedish: `sv-SE`</li><li>turkish: `tr-TR`</li><li>ukrainian: `uk`</li><li>urdu: `ur`</li><li>chinese simplified: `zh-Hans`</li><li>chinese traditional: `zh-Hant`</li></ul></li></ul> |

