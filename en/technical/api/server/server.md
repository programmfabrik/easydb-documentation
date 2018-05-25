# Retrieve status information about the server
    GET /api/v1/plugin/base/server/status?token=<token>

Retrieves status information about a the server, including information about external components such as EAS and Elasticsearch.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Output

The status information is saved in a JSON object. It contains the current server time and four groups of information.

```json
{
  "info_groups": [
    {
      "name": "system",
      "info": [ ... ]
    },
  {
      "name": "index",
      "info": [ ... ]
    },
  {
      "name": "eas",
      "info": [ ... ]
    },
  {
      "name": "elasticsearch",
      "info": [ ... ]
    }
  ],
  "_server_time": "2018-05-25T02:28:00+02:00"
}
```

The information is saved in a map, with an array `data` that contains the values, and an optional object `headers` that contains the corresponding header names.

```json
{
  "type": "2d-map",
  "name": "indexer_stats_by_status",
  "headers": {
    "values": [
      "total"
    ],
    "name": "status"
  },
  "data": [
    {
      "values": [
        12
      ],
      "type": "integer",
      "name": "count"
    },
    {
      "values": [
        5.3
      ],
      "type": "string",
      "name": "percent"
    }
  ]
}
```

This map describes the content of a table, that is rendered in table form in the frontend:

|| Status | Count | `%` ||
||-|-|-||
|| total | `12` | `5.3` ||

### Info Group `system`

A collection of general server information:

- `general`
  - `uptime`
    - Server uptime in seconds
  - `api-version`
    - Version number of the API
  - `software-version`
    - Version number of the software
  - `os-version`
    - Description string of the Server Operation System

### Info Group `index`

#### Process

Values are grouped into `number_of_processes`, `objects_per_batch`, `keep_files`:

- `process_information`
  - `dirty_queuer`
    - information about currently running dirty queuer processes
  - `indexer`
    - information about currently running indexer processes
  - `preindexer`
    - information about currently running preindexer processes

#### Indexer stats by status

`indexer_stats_by_status`

Values are grouped into `count` (total number) and `percent`. Each data row contains information about the currently running indexer jobs, grouped by status.

#### Indexer stats by type

`indexer_stats_by_type`

Values are grouped into `schema`, `count` and `percent`. Each data row contains information about the currently running indexer jobs, grouped by the schema and name.

#### Indexer stats by priority

`indexer_stats_by_priority`

Values are grouped into `count` (total number) and `percent`. Each data row contains information about the currently running indexer jobs, grouped by priority.

### Info Group `eas`

#### General Information

- `general`
  - `server-url`
    - The URL of the easydb asser server (EAS)
  - `instance`
    - Name of the instance on the server

#### Supervisor-Jobs

Counts the EAS supervisor jobs:

- `produce_info`
  - `new`
  - `old`
  - `current`

#### Partitions

Overview over the partitions on the server.

Each partition is grouped into

- `partition-name`
  - Name of the partition
- `number`
  - Number of the partition
- `path`
  - Filepath to the partition
- `free`
  - Free space on the partition (in bytes)
- `total`
  - Total space on the partition (in bytes)
- `fill`
  - Relative space that is filled on the partition (in %)
- `disabled`
  - If the partition is currently disabled
- `auto-disabled-at`
  - Timestamp when the partition was automatically disabled

#### EAS-Jobs

Overview over the EAS jobs that are currently running. The jobs are grouped into `status` and `count`.

- `queue`
  - `failed`
    - total number of failed EAS jobs
  - `recent-failed`
    - total number of recently failed jobs
  - `recent-done`
    - total number of recently done jobs
  - `done`
    - total number of jobs that are done

### Info Group `elasticsearch`

Overview over the elasticsearch instance.

#### General Information

- `general`
  - `Server URL`
    - URL of the elasticsearch server
  - `Index Name`
    - Name of the elasticsearch index
  - `Cluster Name`
    - Name of the elasticsearch cluster
  - `Cluster Status`
    - Status of the elasticsearch cluster (green, yellow, red)
  - `Index Docs`
    - Number of index documents
  - `Index Size`
    - Total file size of the index (in bytes)
  - `Nodes Count`
    - Number of nodes

#### Node

For each node, the information is grouped into one map.

- `node`
  - `Node #`
    - Number of the node
  - `Node UID`
    - Unique ID of the node
  - `Node Name`
    - Name of the node
  - `Index Docs`
    - Number of index documents
  - `Index Size`
    - Total file size of the index (in bytes)
  - `HTTP Connections`
    - Active HTTP connections to the node
  - `File System Free`
    - Free space on the file system of the server (in bytes)
  - `Load Average`
    - Average load on the server (for the last 1, 5 and 15 minutes)
  - `CPU Idle`
    - Total percentage of the CPU that is idling
  - `Memory Used`
    - Total percentage of memory that is used
  - `Memory Free`
    - Total percentage of memory that is free

## Permissions

The user needs the "system.server.error" right (see [rights management](/technical/rightsmanagement/rightsmanagement.html)).

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 400 | [No System Right](/technical/errors/errors.html#no_system_right): user lacks the required "system.server.error" right |
| 400 | [Error Not Found](/technical/errors/errors.html#error_not_found): the error `uuid` was not found |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |





# Retrieve detailed information about a server error
    GET /api/v1/plugin/base/server/error/<uuid>?token=<token>

Retrieves detailed information about a server error, identified by its <uuid>.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Path parameters

|   |   |
|---|---|
| `uuid` | UUID of the server error (see [server errors](/technical/errors/errors.html#server)) |

## Output

A JSON object containing:

|   |   |
|---|---|
| `code`            | Error code (string), see [server errors](/technical/errors/errors.html#server) |
| `description`     | Error description (string) |
| `timestamp`       | Timestamp (string) |
| `request`         | Information about the request that provoked the error |
| &#8614; `method`  | Request method (string) |
| &#8614; `url`     | Request URL (string): the request URL will use the host provided in the headers, or "localhost" if none was provided |
| &#8614; `body`    | Request body (string) |
| &#8614; `headers` | Request headers (string) |
| `session`         | Information about the session (null, if there was no session) |
| &#8614; `token`   | Session Token (string) |
| &#8614; `created` | Timestamp of session creation (string) |
| &#8614; `user`    | Authenticated user (user in short format): this is only given if the session was successfully authenticated |
| `log`             | Additional information (string): this may be multiline, using the line separator `\n` |

## Permissions

The user needs the "system.server.error" right (see [rights management](/technical/rightsmanagement/rightsmanagement.html)).

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 400 | [No System Right](/technical/errors/errors.html#no_system_right): user lacks the required "system.server.error" right |
| 400 | [Error Not Found](/technical/errors/errors.html#error_not_found): the error `uuid` was not found |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |





# Generate an error
    POST /api/v1/plugin/base/server/error/<type>?token=<token>

Returns an error of the requested `type`.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html) |

## Path parameters

|   |   |
|---|---|
| `type` | Type of error to be generated (string): **user**, **server** or **api** |

## Permissions

The user needs the "system.root" right (see [rights management](/technical/rightsmanagement/rightsmanagement.html)).

## HTTP status codes

Notice that this call never returns 200. The requested errors are:

- API error: error.api.type_mismatch
- User error: error.user.user_not_found
- Server error: error.server.generic

|   |   |
|---|---|
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed, or the requested API error |
| 400 | [Not Authenticated](/technical/errors/errors.html#not_authenticated): session is not authenticated |
| 400 | [No System Right](/technical/errors/errors.html#no_system_right): user lacks the required "system.root" right |
| 400 | [User Not Found](/technical/errors/errors.html#user_not_found): the requested user error |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error, or the requested server error |
