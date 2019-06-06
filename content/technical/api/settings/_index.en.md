---
title: "76 - settings"
menu:
  main:
    name: "settings"
    identifier: "technical/api/settings"
    parent: "technical/api"
---
# Retrieve server settings

    GET /api/v1/settings

Return server settings


## Permissions

No session or authentication is required.


## Output

The output is given as a JSON object.  The JSON object contains the following attributes:

| Name			        | Description                            |
|-----------------------|----------------------------------------|
| `name`		        | Name of easydb instance                |
| `api`			        | API version                            |
| `server_version`	    | Server version                         |
| `easydb_version`	    | easydb version                         |
| `user-schema`		    | User schema version                    |
| `solution`		    | Solution name                          |
| `db-name`		        | Database name                          |
| `startup_time`	    | Time when server started in ISO format |
| `server_time`		    | Time in the server in ISO format       |
| `external_eas_url`	| EAS server URL                         |


## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 500 | [Server error](/en/technical/errors): internal server error |

# Restart server

    POST /api/v1/settings/restart

Restarts the server.

## Permissions

An authenticated session with the `system.root` privilege is required to perform this request

## HTTP status codes

|   |   |
|---|---|
| 400 | [API error](/en/technical/errors): `error.api.invalid_api` in case this endpoint is deactivated (the [easydb-server.yml](../../../sysadmin/konfiguration/easydb-server.yml) entry `api.settings.restart` is not set to `true`) |
| 500 | [Server error](/en/technical/errors): the server always returns an error as it is shutting down to perform the request |

# Recreate database

    POST /api/v1/settings/purgedata

Restarts the server, deletes and recreates the database. Use this call with extreme care, there is no way to recover the removed data without a current backup.

## Permissions

An authenticated session with the `system.root` privilege is required to perform this request

## HTTP status codes

|   |   |
|---|---|
| 400 | [API error](/en/technical/errors): `error.api.invalid_api` in case this endpoint is deactivated (the [easydb-server.yml](../../../sysadmin/konfiguration/easydb-server.yml) entry `api.settings.purgedata` is not set to `true`) |
| 500 | [Server error](/en/technical/errors): the server always returns an error as it is shutting down to perform the request |

# Reset whole application

    POST /api/v1/settings/purgeall

Restarts the server, deletes the entire user schema and the database. Use this call with extreme care, there is no way to recover the removed data without a current backup.

## Permissions

An authenticated session with the `system.root` privilege is required to perform this request

## HTTP status codes

|   |   |
|---|---|
| 400 | [API error](/en/technical/errors): `error.api.invalid_api` in case this endpoint is deactivated (the [easydb-server.yml](../../../sysadmin/konfiguration/easydb-server.yml) entry `api.settings.purgeall` is not set to `true`) |
| 500 | [Server error](/en/technical/errors): the server always returns an error as it is shutting down to perform the request |

# Rebuild elasticsearch index

    POST /api/v1/settings/reindex

Restarts the server, drops and rebuilds the elasticsearch index. Use with care, as the complete index will be rebuilt after the server start. This may take a long time!

## Permissions

An authenticated session with the `system.root` privilege is required to perform this request

## HTTP status codes

|   |   |
|---|---|
| 400 | [API error](/en/technical/errors): `error.api.invalid_api` in case this endpoint is deactivated (the [easydb-server.yml](../../../sysadmin/konfiguration/easydb-server.yml) entry `api.settings.reindex` is not set to `true`) |
| 500 | [Server error](/en/technical/errors): generic server error in case something unexpected happens while handling the request|

# Rebuild suggest index

    POST /api/v1/settings/buildsuggest

Rebuild the suggest index now.

> This request is synchronous and will block until the process is finished. Depending on the number of objects and complexity of the system, this might take several hours!

## Input

The input is given as a JSON object.

| Name | Type | Description |
|---|---|---|
| `ngram_min_length` | Integer | `1`, `2` or `3`: the minimum length of the n-grams (optional) |

If the attribute `ngram_min_length` is not set, the current value in the [Base Config](/en/webfrontend/administration/base-config/general/#autocompletion) (`system.search.suggest.autocompletion.autocomplete`) is used.

If this value is not one of `"one"`, `"two"` or `"three"`, an API error is thrown.

## Output

The output (in case of success) is given as a JSON object.  The JSON object contains the following attribute:

| Name | Type | Description |
|---|---|---|
| `success` | Boolean | `true` in case of a successful rebuild |
| `start_at` | String | Minimum length of n-grams (`"one"`, `"two"` or `"three"`) |

## Permissions

An authenticated session with the `system.root` privilege is required to perform this request

## HTTP status codes

|   |   |
|---|---|
| 400 | [API error](/en/technical/errors): `error.api.invalid_api` in case this endpoint is deactivated (the [easydb-server.yml](../../../sysadmin/konfiguration/easydb-server.yml) entry `api.settings.restart` is not set to `true`) |
| 400 | [API error](/en/technical/errors): `error.api.suggest_lock_taken` in case that a different process already builds the suggest index|
| 400 | [API error](/en/technical/errors): `error.api.generic` in case that something unexpected happens while building the suggest index|
| 500 | [Server error](/en/technical/errors): generic server error in case something unexpected happens while handling the request|

# Send test email

    POST /api/v1/settings/sendmail

Sends a test email to any email address that is registered as a valid user email address. [Email settings](../../usermanagement/#e-mail-management) are ignored, and the email is sent right away.

The mail contains information about who sent the email at which time, as well as the server settings as a JSON object (same output as for [Retrieve server settings](#retrieve-server-settings)).

## Input

The input is given as a JSON object. The JSON object must contain the following attribute:

| Name | Type | Description |
|---|---|---|
| `to` | String | Email address of the recipient |

## Output

There is not output for this request.

## Permissions

An authenticated session with the `system.root` privilege is required to perform this request

## HTTP status codes

|   |   |
|---|---|
| 400 | [API error](/en/technical/errors): `error.api.invalid_api` in case the session has no `system.root` privilege |
| 400 | [API error](/en/technical/errors): `error.api.invalid_email_address` in case the mail address is unknown |
| 400 | [API error](/en/technical/errors): `error.api.[attribute_expected,type_mismatch]` in case `to` is missing or not a string |
| 500 | [Server error](/en/technical/errors): generic server error in case something unexpected happens while handling the request |

# Update Custom Datatypes

    POST /api/v1/settings/updatecustomdata

Instead of waiting for the daily run of the [Custom Datatype Updater](/en/technical/plugins/customdatatype/customdatatype_updater), start the update process immediately.

> This request is synchronous and will block until the process is finished. Depending on the number of objects and complexity of the system, this might take several hours!

## Output

The output is given as a JSON object. The JSON object contains the following attribute:

| Name | Type | Description |
|---|---|---|
| `success` | Boolean | `true` in case of a successful update of Custom Datatype Data |

## Permissions

An authenticated session with the `system.root` privilege is required to perform this request

## HTTP status codes

|   |   |
|---|---|
| 400 | [API error](/en/technical/errors): `error.api.invalid_api` in case the session has no `system.root` privilege |
| 400 | [API error](/en/technical/errors): `error.api.update_customdata` in case the update failed |
| 500 | [Server error](/en/technical/errors): generic server error in case something unexpected happens while handling the request |

