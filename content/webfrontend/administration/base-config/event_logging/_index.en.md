---
title: "205 - Event logging"
menu:
  main:
    name: "Event logging"
    identifier: "webfrontend/administration/base-config/event_logging"
    parent: "webfrontend/administration/base-config"
---
# Event Logging

Select which [event types](../../../../technical/types/event/#event-types) should be logged, and wether logged events can save personal data.

## Log user activity

These are general events and event groups that log user activity. If a event group is not enabled, none of the events is logged, even if the event is activated (see below).

| Settings | Explanation | Event types |
|---|---|---|
| Log detail view | Records the calls for detail views. | `DETAIL_VIEW` |
| Log export file downloads | Records the download of a file from an export by a user. | `ASSET_DOWNLOAD`, `ASSET_EXPORT_DOWNLOAD`, `ASSET_EXPORT_TRANSPORT_DOWNLOAD`, `ASSET_EXPORT_TRANSPORT_COPY`, `ASSET_EXPORT_TRANSPORT_COPY_SCHEDULED` |
| Log file uploads | Records the upload of an asset by a user. | `UPLOAD_ASSET` |
| Log search requests | Records user search request. | `SEARCH` |
| Log export downloads | Records the download of an export by a user. | `DOWNLOAD_EXPORT` |
| Log login/logout | Records a user's login and logout events. | `USER_LOGIN`, `USER_LOGOUT` |
| Log webfrontend problems | Records frontend problems while using easydb. | `FRONTEND_ERROR` |

## Logging of specific events, settings for user data

For any of the following event types you can set if it will be logged (**Activated**), and if it is logged, if user specific data is included in the event details (**Save User Data**).

An event is not logged if it is part of any of the user activity groups (see above) and the group is not enabled.

If saving of user data is disabled for an event, the Session ID and the user ID is removed from the event before it is saved, as well as specific user data from the optional JSON object with additional information (see below).

### Log API calls

Event type: `API_CALL`

| Settings | Explanation |
|---|---|
| enabled | Options to choose for logs in easydb: "none", "only write operations", "all" |
| log the following calls | Specification of calls, which are supposed to be logged. |
| Save User Data | Include user data in the event details (default: `true`) |

> NOTE: More detailed information on the logs can be found in the [technical documentation](https://docs.easydb.de/en/technical/api) beneath the chapter API.

### Base configuration updated

Event type: `BASE_CONFIG_UPDATE`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Detail view opened

Event type: `DETAIL_VIEW`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Connector Asset Download

Event type: `ASSET_CONNECTOR_DOWNLOAD`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

User data that is deleted from the additional information:

- `user_id`
- `user_displayname`
- `user_email`

### Connector Login

Event type: `CONNECTOR_LOGIN`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

User data that is deleted from the additional information:

- `connector_user_id`
- `connector_user_displayname`

### Connector Logout

Event type: `CONNECTOR_LOGOUT`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

User data that is deleted from the additional information:

- `user_id`
- `user_displayname`
- `user_email`

### Asset download

Event type: `ASSET_DOWNLOAD`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Download from export

Event type: `ASSET_EXPORT_DOWNLOAD`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Asset copy by transport

Event type: `ASSET_EXPORT_TRANSPORT_COPY`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Asset copy by scheduled transport

Event type: `ASSET_EXPORT_TRANSPORT_COPY_SCHEDULED`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Asset export

Event type: `EXPORT_ASSET`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Export information

Event type: `EXPORT_OBJECT`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Datamodel commited

Event type: `SCHEMA_COMMIT`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Record updated

Event type: `OBJECT_UPDATE`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Record inserted

Event type: `OBJECT_INSERT`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Record deleted

Event type: `OBJECT_DELETE`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Record indexed

Event type: `OBJECT_INDEX`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Export downloaded

Event type: `DOWNLOAD_EXPORT`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Download via transport

Event type: `ASSET_EXPORT_TRANSPORT_DOWNLOAD`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Drupal file copy

Event type: `DRUPAL_FILE_COPY`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Drupal file copy error

Event type: `DRUPAL_FILE_COPY_ERROR`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Email sent

Event type: `EMAIL_SENT`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

User data that is deleted from the additional information:

- `recipients`
- `subject`
- `message`

### Export finished

Event type: `EXPORT_FINISH`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Export updated

Event type: `EXPORT_UPDATE`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Export stopped

Event type: `EXPORT_STOPPED`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Export inserted

Event type: `EXPORT_INSERT`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Export failed

Event type: `EXPORT_FAILED`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Export started

Event type: `EXPORT_START`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Falcon.io file copy

Event type: `FALCONIO_FILE_COPY`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Falcon.io file copy error

Event type: `FALCONIO_FILE_COPY_ERROR`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Progress information

Event type: `API_PROGRESS`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Frontend error

Event type: `FRONTEND_ERROR`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Login failed

Event type: `LOGIN_FAILED`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

User data that is deleted from the additional information:

- `login`

### Message accepted

Event type: `USER_ACCEPTED_MESSAGE`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### New user created

Event type: `USER_CREATED`

> **Note:** This Event type is the only exception where user specific data is always included.

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |

### User login

Event type: `USER_LOGIN`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

User data that is deleted from the additional information:

- `root_login`

### User logout

Event type: `USER_LOGOUT`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Collection rights error

Event type: `COLLECTION_OWNER_RIGHTS_ERROR`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Resource not available

Event type: `RESOURCE_NOT_AVAILABLE`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Server started

Event type: `SERVER_START`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Server stopped

Event type: `SERVER_SHUTDOWN`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Session invalid

Event type: `SESSION_INVALID`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Search

Event type: `SEARCH`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Suggest Index ready

Event type: `SUGGEST_INDEX_DONE`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Suggest Index Progress

Event type: `SUGGEST_INDEX_PROGRESS`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Suggest Index failed

Event type: `SUGGEST_INDEX_FAILED`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Suggest Index is newly created

Event type: `SUGGEST_INDEX_START`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### TYPO3 file copy

Event type: `TYPO3_FILE_COPY`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### TYPO3 file copy error

Event type: `TYPO3_FILE_COPY_ERROR`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |

### Wordpress syncronisation

Event type: `WORDPRESS_SYNC`

| Settings | Explanation |
|---|---|
| Activated | Log events of this type (default: `true`) |
| Save User Data | Include user data in the event details (default: `true`) |
