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

| Name			| Description					|
|-----------------------|-----------------------------------------------|
| `name`		| Name of easydb instance.			|
| `api`			| API version.					|
| `server_version`	| Server version.				|
| `user-schema`		| User schema version				|
| `solution`		| Solution name.				|
| `db-name`		| Database name.				|
| `startup_time`	| Time when server started in ISO format.	|
| `server_time`		| Time in the server in ISO format.		|
| `external_eas_url`	| EAS server URL.				|


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
| 500 | [Server error](/en/technical/errors): the server always returns an error as it is shutting down to perform the request |

# Recreate database

    POST /api/v1/settings/purgedata

Restarts the server, deletes and recreates the database. Use this call with extreme care, there is no way to recover the removed data without a current backup.

## Permissions

An authenticated session with the `system.root` privilege is required to perform this request

## HTTP status codes

|   |   |
|---|---|
| 500 | [Server error](/en/technical/errors): the server always returns an error as it is shutting down to perform the request |

# Reset whole application

    POST /api/v1/settings/purgeall

Restarts the server, deletes the entire user schema and the database. Use this call with extreme care, there is no way to recover the removed data without a current backup.

## Permissions

An authenticated session with the `system.root` privilege is required to perform this request

## HTTP status codes

|   |   |
|---|---|
| 500 | [Server error](/en/technical/errors): the server always returns an error as it is shutting down to perform the request |

# Rebuild suggest index

    POST /api/v1/settings/buildsuggest

Blockingly rebuilds the suggest index

## Input

The input is given as a JSON object.  The JSON object must contain the following attribute:

| Name			| Description					|
|-----------------------|-----------------------------------------------|
| `start_at`		| String; "one" or "two"; the minimum length of the n-grams|

## Output

The output is given as a JSON object.  The JSON object contains the following attribute:

| Name			| Description					|
|-----------------------|-----------------------------------------------|
| `success`		| Boolean; True in case of a successful rebuild|

## Permissions

An authenticated session with the `system.root` privilege is required to perform this request

## HTTP status codes

|   |   |
|---|---|
| 400 | [API error](/en/technical/errors):  error.api.suggest_lock_taken in case that a different process already builds the suggest index|
| 400 | [API error](/en/technical/errors):  error.api.generic in case that something unexpected happens while building the suggest index|
| 500 | [Server error](/en/technical/errors): generic server error in case something unexpected happens while handling the request|

