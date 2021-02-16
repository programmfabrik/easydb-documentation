---
title: "205 - Events"
menu:
  main:
    name: "Events"
    identifier: "webfrontend/administration/base-config/event_logging"
    parent: "webfrontend/administration/base-config"
---
# Events

Select which [event types](../../../../technical/types/event/#event-types) should be logged, and wether logged events can save personal data.

## Log user activity

These are general events and event groups that log user activity. If a event group is not enabled, none of the events is logged, even if the event is activated (see below).

| Settings | Explanation | Event types |
|---|---|---|
| Log search requests | Records user search request. | `SEARCH` |
| Log detail view | Records the calls for detail views. | `DETAIL_VIEW` |
| Log file uploads | Records the upload of an asset by a user. | `UPLOAD_ASSET` |
| Log export events | Records creating, updating, finishing of exports. | `EXPORT_ASSET`, `EXPORT_FINISH`, `EXPORT_INSERT`, `EXPORT_OBJECT`, `EXPORT_START`, `EXPORT_STOPPED`, `EXPORT_UPDATE` |
| Log export downloads | Records the download of an export by a user. | `DOWNLOAD_EXPORT` |
| Log export file downloads | Records the download of a file from an export by a user. | `ASSET_DOWNLOAD`, `ASSET_EXPORT_DOWNLOAD`, `ASSET_EXPORT_TRANSPORT_DOWNLOAD`, `ASSET_EXPORT_TRANSPORT_COPY`, `ASSET_EXPORT_TRANSPORT_COPY_SCHEDULED` |
| Log login/logout | Records a user's login and logout events. | `USER_LOGIN`, `USER_LOGOUT` |
| Log webfrontend problems | Records frontend problems while using easydb. | `FRONTEND_ERROR` |

## Log personal data

For any of the following event groups you can set if user specific data is included in the event details (**Log personal data**).

An event is not logged if it is part of any of the user activity groups (see above) and the group is not enabled.

If saving of personal data is disabled for an event, the Session ID and the User ID is removed from the event before it is saved, as well as specific user data from the optional JSON object with additional information.

### Events during search

Enable or disable the logging of personal data for the events `SEARCH` and `DETAIL_VIEW`.

### Export and Download Events

Enable or disable the logging of personal data for the group of the following events:

* `EXPORT_OBJECT`
* `EXPORT_ASSET`
* `EXPORT_STOPPED`
* `EXPORT_FINISH`
* `EXPORT_START`
* `EXPORT_INSERT`
* `EXPORT_UPDATE`
* `ASSET_EXPORT_DOWNLOAD`
* `ASSET_EXPORT_TRANSPORT_DOWNLOAD`
* `ASSET_DOWNLOAD`
* `ASSET_EXPORT_TRANSPORT_COPY`
* `ASSET_EXPORT_TRANSPORT_COPY_SCHEDULED`
* `DOWNLOAD_EXPORT`



## Log additional user account data in events. 

By default, only links to users who have performed the logged action are logged in the events. If a user is deleted, it is no longer possible to draw conclusions about the user in the events. When users are archived, the user remains in the system and is still visible in the events. However, if selected data has been pseudonymized, the original values can no longer be found in the events. To ensure that information on users is still retained in the events despite deletion or pseudonymization of users, selected fields can be activated here which are copied as text into the respective event and thus remain in the events even after deletion or pseudonymization.



## API-Call

Event type: `API_CALL`

| Settings | Explanation |
|---|---|
| enabled | Options to choose for logs in easydb: "none", "only write operations", "all" |
| log the following calls | Specification of calls, which are supposed to be logged. |

> **Notes:**
>
> - More detailed information on the logs can be found in the [technical documentation](https://docs.easydb.de/en/technical/api) beneath the chapter API.
