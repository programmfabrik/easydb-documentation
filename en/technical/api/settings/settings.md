# Server Settings

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
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |

