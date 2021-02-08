---
title: "152 - Auto Keyworder"
menu:
  main:
    name: "Auto Keyworder"
    identifier: "webfrontend/administration/base-config/auto_keyworder"
    parent: "webfrontend/administration/base-config"
---
# Auto Keyworder

#### Base Configuration
All AI services are configured in the base config in the "Auto Keyworder" tab.

The Plugin checks the base config for changes with a delay of `baseconfig_poll_interval_sec` seconds after any currently running worker has finished. This value is defined in the server configuration.

| Option                                               |  Description                                                  |
| ---------------------------------------------------- | ------------------------------------------------------------ |
| **Service active**                                   | Enable/disable the complete Auto-Keyworder process                                   |
| **Start update process after saving**                | Enable this to ignore the calculated next run time of the workers. Instead, start as soon as possible after the base configuration was saved <br> <ul> <li>Internal representation: value `start_now` , which can also be set by an API call </li> <li> This value is **not persistent** but only valid once. Every time it is set to `True` , the plugin sets this value to `False` after it is read </ul>|
| **easydb API user** and **easydb API user password** | <ul><li> _mandatory_ (if **easydb API Session Token** is not set) </li><li> Login and password of a special user which can perform searches and object updates in easydb</li><li> This plugin uses the easydb API endpoints `/api/v1/search` and `/api/v1/db` </li><li> The user needs at least the following rights on objecttypes (or pools repectively):<ul><li> `write` right on all objecttypes that are configured for updating </li><li> `mask` right on a mask that allows editing of all fields that are updated </li><li> `asset_show` right on the selected asset fields, so the plugin can transfer the image data to the AI service </li><li> `bag_read` on the pool if the objects are pool managed </li><li> if the keywords are stored in linked objects, the user needs the following rights on the linked objecttype(s): <ul><li> `read` to be able to search for existing linked objects </li><li> `mask` right on a mask that allows reading and writing the value of the keyword text field </li><li> `create` right to be able to create new linked objects </ul></ul></ul>                          |
| **easydb API Session Token**                         | <ul><li> _mandatory_ (if **easydb API user** and **easydb API user password** are not set)</li><li> Authenitcated token of the user which can perform searches and object updates in easydb</li><li> If this is set, **easydb API user** and **easydb API user password** are ignored</ul>             |

### Configurations for different services

Configurations for different services and objecttype setups are saved in multiple configuration blocks:

| Option                                                    | Description                                                  |
| --------------------------------------------------------- | ------------------------------------------------------------ |
| **Enable this configuration** ( `true/false` )            | Enable/disable this configuration block                      |
| **Name of this configuration**                            | To help debugging, you can give a specific name for this configuration (_optional_) |
| **Service**                                               | The AI service provider - currently, only Cloudsight.ai is implemented |
| **Objecttype**                                            | <ul><li>_mandatory_</li><li> Objecttype for updating keywords</li><li> Only objecttypes with the following requirements can be selected:<ul><li> At least one asset (image)</li><li> At least one text field (on top level, in a nested table or in a linked object in a nested table) where the generated keywords are saved</li><li> At least one datetime field where the timestamp of the last successful update of the object is saved</ul></ul> |
| **Target field for image subject**                        | Text field where the image subject is saved (_optional_)     |
| **Target field for keywords**                             | <ul> <li>_mandatory_</li> <li>Text field where keywords are saved</li><li> If the field is in a nested table, each keyword is saved in a new row, else the keywords are comma separated</li><li> If the field is a multi language field, the keywords are saved for the specified language (see below)</li><li> If the field is in a linked object, the plugin searches if a linked object with the keyword already exisits. If not, a new object is created before linking it to the updated object</ul> |
| **Target field for quantity**                             | Text field where the quantity is saved                       |
| **Target field for gender**                               | Text field where genders are saved                           |
| **Target field for material**                             | Text field where materials are saved                         |
| **Target field for color**                                | Text field where colors are saved                            |
| **Target field for timestamp**                            | <ul><li>_mandatory_</li><li> must be a datetime field to store a complete timestamp</li><li> After a object was successfully updated, the timestamp is saved in this field</li><li> Only objects are searched where this field is unset, or where the timestamp is older than the specified max age (see below)</ul> |
| **Tagfilter to mark objects for auto keyword generation** | <ul><li> _mandatory_</li><li> Define a tag filter to mark objects that should be updated</li><li> Only objects are searched where the specfified tags are set / unset respectively</ul> |
| **Minimal age since the last keyword generating**         | <ul><li>_mandatory_</li><li> Time since this object was last updated, in days</li><li> Only objects are searched where the timestamp field is unset, or where the timestamp is older than this age</li><li> Minimum: `1`</li><li> Defaults to `7`</li><li> If you want to overwrite data in objects that were updated too recently, you have to delete this timestamp in the objects</ul> |
| **Language for Keywords**                                 | <ul><li>_mandatory_</li><li> Language in which the keywords are requested</li><li> Depending on the AI service, the language can be used</li><li> The following languages are usable:<ul><li> german: `de-DE`</li><li> english: `en-US`</li><li> spanish: `es-ES`</li><li> italian: `it-IT`</li><li> arabic: `ar`</li><li> czech: `cs-CZ`</li><li> farsi (persian): `fa`</li><li> french: `fr-FR`</li><li> japanese: `ja-Jpan`</li><li> georgian: `ka-GE`</li><li> korean: `ko-Kore`</li><li> dutch: `nl-NL`</li><li> polish: `pl-PL`</li><li> russian: `ru-RU`</li><li> chinese: `zh-Hans`</ul><li> Language settings for Cloudsight.ai:<ul><li> The language is sent via the API</li><li> The subject ( `name` ) of the analyzed image is returned in this language</li><li> The keywords are returned in the language that is configured in the Cloudsight project for the given API key. **This configuration is separate and independant from easydb**.</li><li> For best results, the language in which the Cloudsight project is configured should be selected, so that the keywords and the subject are saved in the same language</ul></ul> |






