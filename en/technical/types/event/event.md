# Event

Events are created automatically on the server and can be accessed using [/api/event](/technical/api/event/event.html).

## Attributes

| Parameter                 | Value    | Search | Included in Poll |  Description                |
|-------------------------  |----------|--------| -----------------| ---------------------------------------|
| `event`                   |          |        | yes |  Event definition |
| &#8614; `_id`             | Integer  | yes    | yes | ID of the Event. |
| &#8614; `timestamp`       | Timestamp | yes   | no | Timestamp of the event. |
| &#8614; `type`            | String   | yes    | yes | Event-Type. See below for a detailed description of the various event types. |
| &#8614; `ipv4_address`    | String   | yes    | no | Most of the time this information is stored inside the Session, but for some cases (e.g. Secret-Pass-Key Exports), this information is taken directly from the request. This is `null` for local events, like OBJECT_INDEX. |
| &#8614; `pollable`        | Boolean  | yes    | no | If set to true, this Event is exposed by /api/event/poll, if set to false, the event is only searchable and readable using [/api/event/](/technical/api/event/event.html)\<id\>. |
| &#8614; `session_self`    | Boolean  | no     | yes | event was created within the requesting session. |
| The following fields are used, <br/> depending on the Event type: | | | | |
| &#8614; `schema`          | BASE, USER | yes | yes | Defines if the given Objecttype is in Schema BASE or USER. |
| &#8614; `basetype`      | String   |        | yes | Base Objecttype associated with the event (only for BASE `schema`) |
| &#8614; `object_id`       | Integer  |        | yes | ID of the Object associated with the event (only for BASE `schema`) |
| &#8614; `global_object_id` | Integer  |        | yes | Global object ID (only for USER `schema`) |
| &#8614; `object_version`  | Integer  |        | yes | Version of the Object associated with the event. |
| &#8614; `info`            | JSON-Map |        | no | This JSON Map can contain additional information about the event. This is defined by the Event-Type, see below for a detailed description. |
| `_session`              | Session  | yes    | no | If available, Session information. |
| &#8614;  `token`  | String  | yes    | no | Session Token. |
| &#8614;  `created` | Timestamp  | yes    | no | Session Created Time. |
| &#8614;  `expired` | Timestamp  | yes    | no | Session Expired Time. |
| `_user`        | User Short Format  | no | yes | User information.      |
| &#8614; &#8614; `_generated_displayname` | String | yes | yes |  |
| &#8614; &#8614; `_id`    | Int | no | yes | |

## Event types

All event types share some common attributes. They may be NULL in some cases:

- pollable: whether this event is returned when polling - in the list below, the tag `pollable` shows which events are pollable
- schema: if the event is related to an object, this shows if it is a "user" or "base" object
- objecttype: if the event is related to an object, its objecttype (user schema) or base type (base schema)
- object_id: if the event is related to an object, its ID
- object_version: if the event is related to an object, its version
- session: if the event was triggered during a session, the session ID
- user: if the event was triggered during a session, the user ID

### API_CALL

The client makes an API call.
This event is only generated if it is enabled in the base configuration.
The administrator can set the following parameters:

- disabled, enabled for "write" operations, or enabled for all operations
- disable logging for certain API calls

The event contains the following extra information:

- method: HTTP method used
- url: request URL
- payload: request payload (except for file upload requests)

### API_PROGRESS `pollable`

The server generates API_PROGRESS events when processing long-running requests to offer some progress information.

- disabled, enabled for "write" operations, or enabled for all operations
- disable logging for certain API calls

The event contains the following extra information:

- uuid: request UUID, provided by the client, can be used to match the API_PROGRESS notification to a running request
- status: current status (free text, depends on the request)
- progress_info: progress information (free text with CSV keys, depends on the request)
- progress_info_parametes: CSV parameters for progress_info

### ASSET_DOWNLOAD / ASSET_EXPORT_DOWNLOAD / ASSET_EXPORT_TRANSPORT_DOWNLOAD / ASSET_EXPORT_TRANSPORT_COPY / ASSET_EXPORT_TRANSPORT_COPY_SCHEDULED

Event is created when an Asset was downloaded from the server. It contains the following information: `schema=user`, `objecttype=asset`, `object_id=<asset ID>`. It may contain a `_session` and `_user`.

differences:

* `ASSET_DOWNLOAD` is used if export type is @download@ and download is not from transport
* `ASSET_EXPORT_DOWNLOAD` is used if export type is not @download@ and download is not from transport
* `ASSET_EXPORT_TRANSPORT_DOWNLOAD` is used if download is from transport
* `ASSET_EXPORT_TRANSPORT_COPY` is used if asset is copied by a transport, e.g. FTP
* `ASSET_EXPORT_TRANSPORT_COPY_SCHEDULED` is the same as `ASSET_EXPORT_TRANSPORT_COPY` but used if the export was started on schedule

| Parameter               | Type          | Description |
|-------------------------|---------------|-------------|
| `version`               | String        | Version name of downloaded asset             |
| `export`                |               | Information for containing export            |
| &#8614; `_id`           | Integer       | ID of export                                 |
| &#8614; `_version`      | Integer       | Version of export                            |
| &#8614; `_transport_id` | Integer       | ID of containing transport (optional)        |

### COLLECTION_OWNER_RIGHTS_ERROR

This event is created when an operation ends with a "Collection Owner Rights Revoked" 202 code.
It contains detailed information for debugging purposes:

- collection_id: the ID of the collection that caused the error
- owner_id: the ID of the collection's owner
- items: an array of objects that violate the collection policy, with:
    - objecttype
    - object_id
    - right

### EMAIL_SENT

Event is created, when an Email was sent. The event has always a `_user`, but only a `_session` if it is a non-batchable e-mail.

| Parameter    | Type             | Searchable | Description |
|--------------|------------------|--------| -----------|
| `type`       | string           | - | Type describing the origin of the email (template name). |
| `recipients` | array of strings | - | The "To" recipients of the email. |
| `subject`    | string           | - | The subject of the email. |
| `message`    | string           | - | The complete mime-encoded email message. |

### EXPORT_ASSET

Event is created when an Object-Asset is exported using an Export.

### EXPORT_FAILED

Export has been interrupted by an error.

| Parameter   | Type   | Description |
|-------------|--------|-------------|
| `state`     | String | State of export |
| `exception` | Object | Error record as returned from API calls |
| `protocol`  | String | Informal protocol of warnings and others messages during export |

### EXPORT_FINISH

Export processing finished.

| Parameter   | Type   | Description |
|-------------|--------|-------------|
| `state`     | String | State of export |
| `exception` | Object | Error record as returned from API calls |
| `protocol`  | String | Informal protocol of warnings and others messages during export |

### EXPORT_OBJECT

Event is created when Object-Data is exported using an Export. It contains the following information: `schema=user`, `objecttype`, `object_id`, `object_version`, `_user`.

### EXPORT_STOPPED

Export has been stopped manually.

| Parameter   | Type   | Description |
|-------------|--------|-------------|
| `state`     | String | State of export |
| `protocol`  | String | Informal protocol of warnings and others messages during export |

### LOGIN_FAILED

Each failed login is logged as an event with the following extra information:

- method: authentication method
- login: login used
- reason: reason for failure

### SCHEMA_COMMIT `pollable`

Event is created when a new USER schema was comitted. It contains the following information: `_session`, `_user`.

| Parameter | Value  | Description |
|-----------|--------|-------------|
| `schema`   | Integer   | The new Schema ID. |

### SERVER_SHUTDOWN

The event is created when the server stops.
It doesn't have any extra information.

### SERVER_START

Event is created when the server was stopped. There is no further information.

### USER_LOGIN `pollable`

For each new user login, this event is created. It contains the following information: `schema=base`,`objecttype=user`, `object_id`, `_session`, `_user`.

### OBJECT_INDEX

This event is triggered when an object is indexed, and therefore available for searching.

### OBJECT_INSERT

For each PUT on a BASE or USER object, this event is created. It contains the following information: `schema`, `objecttype`, `object_id`, `object_version`, `_session`, `_user`.

| Parameter | Value  | Searchable | Description |
|-----------|--------|---------|---------|
| `batch_id`    | Integer    | no | The Batch-ID of INSERT. Each API request gets a unique batch ID. |

### OBJECT_UPDATE `pollable`

For each POST on a BASE or USER object, this event is created. It contains the following information: `schema`, `objecttype`, `object_id`, `object_version`, `_session`, `_user`.


| Parameter | Value  | Searchable | Description |
|-----------|--------|---------|---------|
| `batch_id`    | Integer    | no | The Batch-ID of INSERT. Each API request gets a unique batch ID. |


### OBJECT_DELETE `pollable`

For each DELETE on a BASE or USER object, this event is created. It contains the following information: `schema`, `objecttype`, `object_id`, `object_version`, `_session`, `_user`.

| Parameter | Value  | Searchable | Description |
|-----------|--------|---------|---------|
| `batch_id`    | Integer    | no | The Batch-ID of INSERT. Each API request gets a unique batch ID. |

### USER_LOGOUT `pollable`

Same as USER_LOGIN, but created at the event of a user logout or a session expire.

### DOWNLOAD_EXPORT

Event is created when a file (directly or via "download" transport) is downloaded from the server. It contains the following information: `schema=user`, `objecttype=export` or `objecttype=export:transport`, `object_id=<export id>` or `object_id=<transport id>`. It may contain a `_session` and `_user`.

| Parameter               | Type          | Description |
|-------------------------|---------------|-------------|
| `asset_id`              | String        | ID of downloaded asset (optional)  |
| `asset_version`         | String        | Version name of downloaded asset (optional)  |
| `bytes_loaded`          | Integer       | Number of bytes actually downloaded (currently equals `bytes_total`) |
| `bytes_total`           | Integer       | Size of file in bytes                        |
| `export`                |               | Information for containing export            |
| &#8614; `_id`           | Integer       | ID of export                                 |
| &#8614; `_version`      | Integer       | Version of export                            |
| &#8614; `_transport_id` | Integer       | ID of containing transport (optional)        |
| `url`                   | String        | unqualified URL of download                  |

### EXPORT_INSERT

Export has been created.

### EXPORT_START

Export processing has been started.

### EXPORT_UPDATE

Export has been updated.

### USER_ACCEPTED_MESSAGE

Event is created when a User accepts a message. It contains the following information: `schema=base`, `objecttype=message`, `object_id`, `object_version`, `_session`, `_user`.

### SEARCH, DETAIL_VIEW

These events are created when a user performs a search (using [/api/search](/technical/api/search/search.html)) and the following conditions are met:

- the base config variable system.log.search is set to **true** and the search request contains `event_log: SEARCH` (the event type will be "SEARCH")
- the base config variable system.log.detail is set to **true** and the search request contains `event_log: DETAIL_VIEW` (the event type will be "DETAIL_VIEW")

The frontend will pass to the search request the event type depending on what the user did to trigger it: a search or access to the
detail view of an object.

The event has always a `_session` and a `_user`. The `info` is the search request as received by the API.

### SESSION_INVALID

The session provided is invalid.

- token: the session token
- reason: the reason why the session is invalid: expired / not found

### RESOURCE_NOT_AVAILABLE

A user attempted to access a resource that is not available.

- schema: user|base
- type: objecttype or base type
- id: identifier
- reason: "not found" or "not allowed"

### BASE_CONFIG_UPDATE

Base configuration was updated.
