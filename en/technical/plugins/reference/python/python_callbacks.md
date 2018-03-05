
# Python Plugin Callbacks

These Callbacks are registered in the Server. They can be called from Python Plugins and are executed in the Server.

The Callbacks belong to different Contexts and can only be called in the correct Context.

## Contexts

### Base

The general context from which most of the callback methods are executed.

The Base context contains information about the server configuration, the current session of the user that caused the callback, or e.g. information about the exporter, when an `export_produce` callback is executed. When objects are updated or deleted, the context contains information about the object data.

This context allows to perform tasks with the same session as the user, including performing elasticsearch requests or Postgres queries.

### Process

Process plugins, that run parallel to the server, get their own process context. It contains no session information.

This context allows to perform tasks without a session, or with a session that was created for the plugin, including performing elasticsearch requests or Postgres queries.

### Session
<!-- TODO explain -->

## Registered Callbacks

| Callback Name | Context | Used in method | Method implemented in Class |
|--|--|--|--|
| `'create_session'` | Process | [`create_session`](#createsession) | [EasydbProcessContext](#easydbprocesscontext) |
| `'create_unique_ids_type'` | Base | [`create_unique_ids_type`](#createuniqueidstype) | [EasydbContext](#easydbcontext) |
| `'db_close_connection'` | Process | [`close`](#close) | [EasydbProcessContext](#easydbprocesscontext) |
| `'db_commit'` | Process | [`commit`](#commit) | [EasydbConnection](#easydbconnection) |
| `'db_abort'` | Process | [`abort`](#abort) | [EasydbConnection](#easydbconnection) |
| `'db_connect'` | Process | [`db_connect`](#dbconnect) | [EasydbProcessContext](#easydbprocesscontext) |
| `'db_cursor'` | Base | [`get_db_cursor`](#getdbcursor) | [EasydbContext](#easydbcontext) |
| `'db_execute'` | Process | [`execute`](#execute) | [EasydbConnectionCursor](#easydbconnectioncursor) |
| `'db_fetchall'` | Process | [`fetchall`](#fetchall) | [EasydbConnectionCursor](#easydbconnectioncursor) |
| `'db_fetchmany'` | Process | [`db_fetchmany`](#dbfetchmany) | [EasydbConnectionCursor](#easydbconnectioncursor) |
| `'db_fetchone'` | Process | [`db_fetchone`](#dbfetchone) | [EasydbConnectionCursor](#easydbconnectioncursor) |
| `'db_open_txn'` | Process | [`open_txn`](#opentxn) | [EasydbConnection](#easydbconnection) |
| `'db_sequence'` | Base | [`sequence_create`](#sequencecreate), [`sequence_exists`](#sequenceexists), [`sequence_nextval`](#sequencenextval) | [EasydbContext](#easydbcontext) |
| `'dbapi_export'` | Base | [`dbapi_export`](#dbapiexport) | [EasydbContext](#easydbcontext) |
| `'dbapi_import'` | Process | [`dbapi_import`](#dbapiimport) | [EasydbProcessContext](#easydbprocesscontext) |
| `'delete_unique_id'` | Base | [`delete_unique_id`](#deleteuniqueid) | [EasydbContext](#easydbcontext) |
| `'drop_unique_ids_type'` | Base | [`drop_unique_ids_type`](#dropuniqueidstype) | [EasydbContext](#easydbcontext) |
| `'export_object_as_xml'` | Base | [`export_object_as_xml`](#exportobjectasxml) | [EasydbContext](#easydbcontext) |
| `'get_collection_json'` | Process | [`get_collection_json`](#getcollectionjson) | [EasydbContext](#easydbcontext) |
| `'get_config'` | Base, Process | [`get_config`](#getconfig) | [EasydbContext](#easydbcontext), [EasydbProcessContext](#easydbprocesscontext) |
| `'get_datamodel'` | Base, Process | [`get_datamodel`](#getdatamodel) | [EasydbContext](#easydbcontext) |
| `'get_environment_variables'` | Session | [`get_environment_variables`](#getenvironmentvariables) | [EasydbContext](#easydbcontext) |
| `'get_exporter'` | Session | [`get_exporter`](#getexporter) | [EasydbContext](#easydbcontext) |
| `'get_instance'` | Base, Process | [`get_instance`](#getinstance) | [EasydbContext](#easydbcontext) |
| `'get_plugins'` | Session | [`get_plugins`](#getplugins) | [EasydbContext](#easydbcontext) |
| `'get_session'` | Session | [`get_session`](#getsession) | [EasydbContext](#easydbcontext) |
| `'insert_unique_id'` | Base | [`insert_unique_id`](#insertuniqueid) | [EasydbContext](#easydbcontext) |
| `'log'` | Base, Process | [`_call`](#call) | [EasydbLogger](#easydblogger) |
| `'log_event'` | Process | [`log_event`](#logevent) | [EasydbProcessContext](#easydbprocesscontext) |
| `'next_unique_id'` | Base | [`next_unique_id`](#nextuniqueid) | [EasydbContext](#easydbcontext) |
| `'next_unique_id_prefixed'` | Base | [`next_unique_id_prefixed`](#nextuniqueidprefixed) | [EasydbContext](#easydbcontext) |
| `'put_asset_from_file'` | Process | [`put_asset_from_file`](#putassetfromfile) | [EasydbProcessContext](#easydbprocesscontext) |
| `'search'` | Base, Process | [`search`](#search) | [EasydbContext](#easydbcontext), [EasydbProcessContext](#easydbprocesscontext) |
| `'update_objects'` | Base | [`update_user_objects`](#updateuserobjects) | [EasydbContext](#easydbcontext) |


## Wrapper Classes

[EasydbException](#easydbexception) | [Errors](#errors) | [EasydbContext](#easydbcontext) | [EasydbProcessContext](#easydbprocesscontext) | [EasydbServerContext](#easydbservercontext) | [EasydbConnection](#easydbconnection) | [EasydbConnectionCursor](#easydbconnectioncursor) | [EasydbCursor](#easydbcursor) | [EasydbLogger](#easydblogger)

---

## EasydbException

*Constructor:*

```python
__init__(e_type, message)
```

| Name | Type | Description |
|--|--|--|
| `e_type` | String | Type of the Exception |
| `message` | JSON-String | Detailled information about the cause of the Exception. Must be parsable as valid JSON |

### `get_code`

```python
get_code()
```

Returns the value of the key `'code'` of the parsed `message`.

### `get_parameter`

```python
get_parameter(parameter)
```

Returns the value of the key `'parameters.{0}'.format(parameter)` of the parsed `message`.

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `parameter` | String | Name of the Parameter |

## Errors

The Wrapper methods can raise different Errors that correspond to the Errors in the Server. All of them extend the Python Exception `EasydbError`:

*Constructor:*
```python
__init__(kind, error_type, description)
```

| Name | Type | Description |
|--|--|--|
| `kind` | String | Scope of the Error (`server`, `api`, `user`) |
| `error_type` | String | Type of Error in the scope |
| `description` | String | Detailled Description of the Error |

The Exception contains two additional member variables, that can be accessed be extending classes:

| Name | Type | Description | Default |
|--|--|--|--|
| `parameters` | Dictionary / JSON | Named and structured Parameters | `{}` |
| `debug_info` | String | Debugging Information | `None` |

### `ServerError`

Extends `EasydbError`

*Constructor:*
```python
__init__(type, description, debug_info)
```

*Values:*

| Name | Value |
|--|--|
| `kind` | `server` |
| `error_type` | from constructor: `type` |
| `description` | from constructor |
| `parameters` | not set for all extending Exceptions |
| `debug_info` | from constructor |

#### `GenericServerError`

Extends `ServerError`

*Constructor:*
```python
__init__(type, description [, debug_info])
```

*Values:*

| Name | Value | Default |
|--|--|--|
| `kind` | `generic` |
| `error_type` | from constructor: `type` |
| `description` | from constructor |
| `debug_info` | from constructor | `''` |

### `APIError`

Extends `EasydbError`

*Constructor:*
```python
__init__(type, description)
```

*Values:*

| Name | Value |
|--|--|
| `kind` | `api` |
| `error_type` | from constructor: `type` |
| `description` | from constructor |
| `parameters` | not set for all extending Exceptions |
| `debug_info` | not set for all extending Exceptions |

#### `PositionalParameterExpectedError`

Extends `APIError`

*Constructor:*
```python
__init__(example)
```

*Values:*

| Name | Value |
|--|--|
| `kind` | `api` |
| `error_type` | `positional_parameter_expected` |
| `description` | `'Positional parameter expected: {0}'.format(example)` |

#### `TypeMismatchError`

Extends `APIError`

*Constructor:*
```python
__init__(what, expected_type)
```

*Values:*

| Name | Value |
|--|--|
| `kind` | `api` |
| `error_type` | `type_mismatch` |
| `description` | `'Expected {0} as {1}'.format(what, expected_type)` |

#### `InvalidValueError`

Extends `APIError`

*Constructor:*
```python
__init__(varname, value [, valid_range])
```

*Values:*

| Name | Value |
|--|--|
| `kind` | `api` |
| `error_type` | `invalid_value` |
| `description` | `'Value {0} is not valid for {1}{2}'.format(value, varname, ` [ optional: `valid_range` ] `)` |

#### `InvalidRequestMethodError`

Extends `APIError`

*Constructor:*
```python
__init__(request_method)
```

*Values:*

| Name | Value |
|--|--|
| `kind` | `api` |
| `error_type` | `invalid_request_method` |
| `description` | `'Invalid request method: {0}'.format(request_method)` |

#### `AttributeExpectedError`

Extends `APIError`

*Constructor:*
```python
__init__(attribute)
```

*Values:*

| Name | Value |
|--|--|
| `kind` | `api` |
| `error_type` | `attribute_expected` |
| `description` | `'Expecting attribute: {0}'.format(attribute)` |

### `UserError`

Extends `EasydbError`

*Constructor:*
```python
__init__(type [, parameters])
```

*Values:*

| Name | Value | Default |
|--|--|--|
| `kind` | `user` |
| `error_type` | from constructor: `type` |
| `description` | `None` for all extending Exceptions |
| `parameters` | from constructor | `{}` |
| `debug_info` | not set for all extending Exceptions |

#### `NoSystemRightError`

Extends `UserError`

*Constructor:*
```python
__init__(right [, extra_info])
```

*Values:*

| Name | Value |
|--|--|
| `kind` | `user` |
| `error_type` | `no_system_right` |
| `parameters` | `{'right': right, 'extra_info': ` [ optional: `extra_info`, default: `''` ] `}` |

#### `NotFoundError`

Extends `UserError`

*Constructor:*
```python
__init__(type, id)
```

*Values:*

| Name | Value |
|--|--|
| `kind` | `user` |
| `error_type` | `'{0}_not_found'.format(type)` |
| `parameters` | `{'id': id}` |

#### `ObjectNotFoundError`

Extends `UserError`

*Constructor:*
```python
__init__(objecttype, id)
```

*Values:*

| Name | Value |
|--|--|
| `kind` | `user` |
| `error_type` | `object_not_found` |
| `parameters` | `{'objecttype': objecttype, 'id': id}` |

---

## EasydbContext

### `call`

```python
call(method [, parameters [, returns_json]])
```

Executes the method that is registered under the given name. The Parameters are given as the String representation of a JSON-Object. Most of the following methods are convenient helper methods, which use this method and build the Parameter-Object from their parameters.

*Example Usage:*

```python
call ('dbapi_export', {'mask': '_all_fields', 'ids': [9, 24]})
```

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `method` | String | Name of the registered method |
| `parameters` | String | List of URL Parameters for the call in a JSON-Object | `None` |
| `returns_json` | Boolean | Should the call return a JSON Object? | `True` |

### `check_system_right`

```python
check_system_right(right [, session])
```

Checks if the User of the specified Session has the given Right (or if the User is Root). If not, a `NoSystemRightError` is raised. If no Session is given, the current Session is used.

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `right` | String | Name of the Right to check |
| `session` | String | JSON representation of a Session | `None` |

### `check_system_right_bool_parameter`

```python
check_system_right_bool_parameter(right, parameter [, session])
```

Checks if the User of the specified Session has the given parameterized Right and if the Right is set to `True` (or if the User is Root). If not, a `NoSystemRightError` is raised. If no Session is given, the current Session is used.

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `right` | String | Name of the Right to check |
| `parameter` | String | Name of the Parameter of the parameterized Right |
| `session` | String | JSON representation of a Session | `None` |

### `create_unique_ids_type`

```python
create_unique_ids_type(type)
```

<!-- `create_unique_ids_type` | Base | [EasydbContext](#easydbcontext) | `create_unique_ids_type` -->
Uses Callback `'create_unique_ids_type'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `type` | String |  |

### `dbapi_export`

```python
dbapi_export(mask, ids)
```

Starts an Export of the Objects with the given IDs. See [dbapi\_export](technical/internal/dbapi_export/dbapi_export.html)

<!-- `dbapi_export` | Base | [EasydbContext](#easydbcontext) | `dbapi_export` -->
Uses Callback `'dbapi_export'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `mask` | String | Mask Name |
| `ids` | String | JSON Array with Object IDs to export |

### `delete_unique_id`

```python
delete_unique_id(type, unique_id)
```

<!-- `delete_unique_id` | Base | [EasydbContext](#easydbcontext) | `delete_unique_id` -->
Uses Callback `'delete_unique_id'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `type` |  |  |
| `unique_id` |  |  |

### `drop_unique_ids_type`

```python
drop_unique_ids_type(type)
```

<!-- `drop_unique_ids_type` | Base | [EasydbContext](#easydbcontext) | `drop_unique_ids_type` -->
Uses Callback `'drop_unique_ids_type'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `type` |  |  |

### `export_object_as_xml`

```python
export_object_as_xml(obj, mapping_type, mapping, user_id, language)
```

Export the given JSON Object as an XML Document. An [XML Mapping Profile](../../api/xmlmapping/xmlmapping.html) is applied.

<!-- `export_object_as_xml` | Base | [EasydbContext](#easydbcontext) | `export_object_as_xml` -->
Uses Callback `'export_object_as_xml'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `obj` | String | JSON Object to export |
| `mapping_type` | String | Type of the XML Mapping |
| `mapping` | String | Name of the XML Mapping Profile |
| `user_id` | String | ID of the User Profile |
| `language` | String | Language of the User that is used to export multilanguage Fields |

### `get_collection_json`

```python
get_collection_json(collection_id, connection_id)
```

Returns JSON Object of the requested Collection.

<!-- `get_collection_json` | Process | [EasydbContext](#easydbcontext) | `get_collection_json` -->
Uses Callback `'get_collection_json'` in Context [*Process*](#process).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `collection_id` | String, Integer | ID of the requested Collection |
| `connection_id` | String, Integer | ID of the Connection that is used |

### `get_config`

```python
get_config([path [, expected]])
```

Returns a JSON-Representation of the Configuration, or a Subobject if a path is specified. If `expected` is `True` and the requested Configuration does not exist, an `EasydbException` is raised.

<!-- `get_config` | Base | [EasydbContext](#easydbcontext) | `get_config` -->
Uses Callback `'get_config'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `path` | String | The path to a JSON-Subobject in the Configuration Object | `None` |
| `expected` | Boolean | If this Configuration must exist | `False` |

Top Level of the result:

```json
{
  "base": { },
  "extensions": { },
  "system": { },
  "defaults": { }
}
```

### `get_datamodel`

```python
get_datamodel()
```

Returns a JSON object with information about the current data model. Example:

```json
{
  "user": {
    "tables": [
      {
        "name": "table_foo"
      }
    ]
  }
}
```

<!-- `get_datamodel` | Base | [EasydbContext](#easydbcontext) | `get_datamodel` -->
Uses Callback `'get_datamodel'` in Contexts [*Base*](#base) and [*Process*](#process).

### `get_db_cursor`

```python
get_db_cursor()
```

Returns an [`EasydbCursor`](#EasydbCursor) object.

<!-- `db_cursor` | Base | [EasydbContext](#easydbcontext) | `get_db_cursor` -->
Uses Callback `'db_cursor'` in Context [*Base*](#base).

### `get_environment_variables`

```python
get_environment_variables()
```

<!-- `get_environment_variables` | Session | [EasydbContext](#easydbcontext) | `get_environment_variables` -->
Uses Callback `'get_environment_variables'` in Context [*Session*](#session).

### `get_exporter`

```python
get_exporter()
```

Returns a wrapped `PyObject` of the current export worker context.

<!-- `get_exporter` | Session | [EasydbContext](#easydbcontext) | `get_exporter` -->
Uses Callback `'get_exporter'` in Context [*Session*](#session).

### `get_instance`

```python
get_instance()
```

Returns a JSON object with information about the current **easydb** instance. Example:

```json
{
  "api": "1",
  "solution": "Solution Name",
  "name": "0123abcd-1234-cdef-1919-9f8e7d6c5b4a",
  "db-name": "Database Name",
  "eas_produce_md5": "0e1e6a8063793bcbad3d1824b6433199",
  "server_start_time": "1506520840"
}
```

<!-- `get_instance` | Base | [EasydbContext](#easydbcontext) | `get_instance` -->
Uses Callback `'get_instance'` in Contexts [*Base*](#base) and [*Process*](#process).

### `get_logger`

```python
get_logger(name)
```

Returns an instance of `EasydbLogger` with the given name.

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `name` | String | Name of the [Logger](#easydblogger) |

### `get_plugins`

```python
get_plugins()
```

Returns the JSON-Representations of the available Plugins.

<!-- `get_plugins` | Session | [EasydbContext](#easydbcontext) | `get_plugins` -->
Uses Callback `'get_plugins'` in Context [*Session*](#session).

### `get_plugin`

```python
get_plugin(name)
```

Returns the JSON-Representation of the Plugin with the given Name, if it exists in the result of `get_plugins()`.

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `name` | String | Name of the Plugin |

### `get_remote_user`

```python
get_remote_user()
```

Returns the value of `REMOTE_USER` from the result of `get_environment_variables()`. Raises a `GenericServerError` if this key is not found.

### `get_kerberos_user`

```python
get_kerberos_user()
```

Returns the Result of `get_remote_user()`

### `get_session`

```python
get_session()
```

Returns the JSON-Representation of the current Session.

<!-- `get_session` | Session | [EasydbContext](#easydbcontext) | `get_session` -->
Uses Callback `'get_session'` in Context [*Session*](#session).

### `insert_unique_id`

```python
insert_unique_id(type, unique_id)
```

<!-- `insert_unique_id` | Base | [EasydbContext](#easydbcontext) | `insert_unique_id` -->
Uses Callback `'insert_unique_id'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `type` |  |  |
| `unique_id` |  |  |

### `ldap_bind`

```python
ldap_bind([url [, who [, cred]]])
```

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `url` |  |  | `None` |
| `who` |  |  | `None` |
| `cred` |  |  | `None` |

### `ldap_search`

```python
ldap_search(base, scope [, filterstr [, attrlist [, filter_output]]])
```

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `base` |  |  |
| `scope` |  |  |
| `filterstr` | String |  | `(objectClass=*)` |
| `attrlist` |  |  | `None` |
| `filter_output` | Boolean |  | `True` |

### `ldap_unbind`

```python
ldap_unbind()
```

### `next_unique_id`

```python
next_unique_id(type)
```

<!-- `next_unique_id` | Base | [EasydbContext](#easydbcontext) | `next_unique_id` -->
Uses Callback `'next_unique_id'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `type` |  |  |

### `next_unique_id_prefixed`

```python
next_unique_id_prefixed(type, length, prefix)
```

<!-- `next_unique_id_prefixed` | Base | [EasydbContext](#easydbcontext) | `next_unique_id_prefixed` -->
Uses Callback `'next_unique_id_prefixed'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `type` |  |  |
| `length` |  |  |
| `prefix` |  |  |

### `search`

```python
search(session_type, session_identifier, query [, include_sets [, include_eas_urls]])
```

Performs a search request to the Elasticsearch Instance of the Server. The search result is returned as a JSON Object. See [api/search](../../api/search/search.html).

<!-- `search` | Base | [EasydbContext](#easydbcontext) | `search` -->
Uses Callback `'search'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `session_type` | String | Type of the Session (e.g. `"user"`) |
| `session_identifier` | String | User ID or `"deep_link"`, `"oai_pmh"` |
| `query` | String | Elasticsearch Search Query |
| `include_sets` | Boolean | Should sets be included in the search? | `False` |
| `include_eas_urls` | Boolean | Should EAS URLs be included in the search? | `False` |

### `sequence_create`

```python
sequence_create(name [, minvalue [, maxvalue [, if_exists]]])
```

<!-- `db_sequence` | Base | [EasydbContext](#easydbcontext) | `sequence_create` -->
Uses Callback `'db_sequence'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `name` | String | Name of the Sequence |
| `minvalue` |  | Minimal Value of the Sequence | `None` |
| `maxvalue` |  | Maximal Value of the Sequence | `None` |
| `if_exists` | Boolean |  | `True` |

### `sequence_exists`

```python
sequence_exists(name)
```

<!-- `db_sequence` | Base | [EasydbContext](#easydbcontext) | `sequence_exists` -->
Uses Callback `'db_sequence'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `name` | String | Name of the Sequence |

### `sequence_nextval`

```python
sequence_nextval(name)
```

<!-- `db_sequence` | Base | [EasydbContext](#easydbcontext) | `sequence_nextval` -->
Uses Callback `'db_sequence'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `name` | String | Name of the Sequence |

### `update_user_objects`

```python
update_user_objects(type, ids)
```

<!-- `update_objects` | Base | [EasydbContext](#easydbcontext) | `update_user_objects` -->
Uses Callback `'update_objects'` in Context [*Base*](#base).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `type` | String | (internal) Name of the Objecttype |
| `ids` |  |  |

## EasydbSession

*Member Variables:*

| Name | Type | Description |
|--|--|--|
| `session_id` | Integer | The ID of this Session |
| `token` | String | The token for this Session |

See [types/Session](../../types/session/session.html).

## EasydbProcessContext

Extends `EasydbContext`

### `call`

```python
call(method [, parameters [, returns_json]])
```

Wrapper method for locked `call` from `EasydbContext`:
```python
with self.lock:
    return EasydbContext.call(method, parameters, returns_json)
```

### `create_session`

```python
create_session(connection, user_id)
```

Returns an `EasydbSession` instance for the User with the given ID.

<!-- `create_session` | Process | [EasydbProcessContext](#easydbprocesscontext) | `create_session` -->
Uses Callback `'create_session'` in Context [*Process*](#process).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `connection` | `EasydbConnection` | The `EasydbConnection` instance |
| `user_id` | Integer | The ID of the User |

### `db_connect`

```python
db_connect(application_name)
```

Returns an [`EasydbConnection`](#EasydbConnection) instance that represents the connection to the **easydb** with the given name `application_name`.

<!-- `db_connect` | Process | [EasydbProcessContext](#easydbprocesscontext) | `db_connect` -->
Uses Callback `'db_connect'` in Context [*Process*](#process).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `application_name` | String | Name of the Database to connect to |

### `dbapi_import`

```python
dbapi_import(connection, session, mask, objects [, collection_id])
```

<!-- `dbapi_import` | Process | [EasydbProcessContext](#easydbprocesscontext) | `dbapi_import` -->
Uses Callback `'dbapi_import'` in Context [*Process*](#process).

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `connection` | `EasydbConnection` | The `EasydbConnection` instance |
| `session` | `EasydbSession` | The Session to use for this connection |
| `mask` | String | Name of the Mask |
| `objects` |  |  |
| `collection_id` |  |  | `None` |

### `get_config`

```python
get_config(connection)
```

Returns a JSON object with the configuration of the given `EasydbConnection`.

<!-- `get_config` | Process | [EasydbProcessContext](#easydbprocesscontext) | `get_config` -->
Uses Callback `'get_config'` in Context [*Process*](#process).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `connection` | `EasydbConnection` | The `EasydbConnection` instance |

### `get_logger`

```python
get_logger(name)
```

Returns an instance of `EasydbLogger` with the given name.

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `name` | String | Name of the [Logger](#easydblogger) |

### `log_event`

```python
log_event(connection, event_type [, event_info])
```

Helper method to write a log output for this specific connection.

<!-- `log_event` | Process | [EasydbProcessContext](#easydbprocesscontext) | `log_event` -->
Uses Callback `'log_event'` in Context [*Process*](#process).

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `connection` | `EasydbConnection` | The `EasydbConnection` instance |
| `event_type` |  |  |
| `event_info` |  |  | `None` |

### `put_asset_from_file`

```python
put_asset_from_file(session, filename, original_filename, mapping_name, mask, objecttype, pool_id)
```

<!-- `put_asset_from_file` | Process | [EasydbProcessContext](#easydbprocesscontext) | `put_asset_from_file` -->
Uses Callback `'put_asset_from_file'` in Context [*Process*](#process).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `session` | `EasydbSession` | The Session to use for this connection |
| `filename` | String | Filename of the uploaded File |
| `original_filename` | String | Path to the original File |
| `mapping_name` | String | Name of the Mapping that will be applied |
| `mask` | String | Name of the Mask |
| `objecttype` | String | (internal) Name of the Objecttype |
| `pool_id` |  | ID of the target Pool |

### `search`

```python
search(connection, session_type, session_identifier, query [, include_sets [, include_eas_urls]])
```

Performs a search request to the Elasticsearch Instance of the Server using the current connection. The search result is returned as a JSON Object. See [api/search](../../api/search/search.html).

<!-- `search` | Process | [EasydbProcessContext](#easydbprocesscontext) | `search` -->
Uses Callback `'search'` in Context [*Process*](#process).

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `connection` | `EasydbConnection` | The `EasydbConnection` instance |
| `session_type` | String | Type of the Session (e.g. `"user"`) |
| `session_identifier` | String | User ID or `"deep_link"`, `"oai_pmh"` |
| `query` | String | Elasticsearch Search Query |
| `include_sets` | Boolean | Should sets be included in the search? | `False` |
| `include_eas_urls` | Boolean | Should EAS URLs be included in the search? | `False` |

## EasydbServerContext

Extends `EasydbContext`.

### `register_callback`

```python
register_callback(callback_type, callback_parameters)
```

Register a callback method that can be called from the server.

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `callback_type` | String | Type of the callback |
| `callback_parameters` | JSON-String | Definition of the callback method |

*Example:*

```python
easydb_context.register_callback('api', { 'name': 'config', 'callback': 'config'})
```

`name` is the name of this callback in the server. To execute the method in the plugin, the server references this name. `callback` is the name of the python method that is executed for the callback.

## EasydbConnection

### Constructor

```python
__init__(easydb_context, connection_id)
```

| Name | Type | Description |
|--|--|--|
| `easydb_context` | `EasydbContext` | The `EasydbContext` for this connection |
| `connection_id` | Integer | The ID of this connection (internally generated in [`db_connect`](#dbconnect)) |

This Constructor is internally called in the wrapper method [`db_connect`](#dbconnect). It should not be called on its own.

### `open_txn`

```python
open_txn()
```

Opens a new transaction, internally identified by `connection_id`.

<!-- `db_open_txn` | Process | [EasydbConnection](#easydbconnection) | `open_txn` -->
Uses Callback `'db_open_txn'` in Context [*Process*](#process).

### `close`

```python
close()
```

Closes this transaction, internally identified by `connection_id`.

<!-- `db_close_connection` | Process | [EasydbProcessContext](#easydbprocesscontext) | `close` -->
Uses Callback `'db_close_connection'` in Context [*Process*](#process).

### `abort`

```python
abort()
```

Aborts this transaction, internally identified by `connection_id`.

<!-- `db_abort` | Process | [EasydbConnection](#easydbconnection) | `abort` -->
Uses Callback `'db_abort'` in Context [*Process*](#process).

### `commit`

```python
commit()
```

Commits this transaction, internally identified by `connection_id`.

<!-- `db_commit` | Process | [EasydbConnection](#easydbconnection) | `commit` -->
Uses Callback `'db_commit'` in Context [*Process*](#process).

### `cursor`

```python
cursor()
```

Returns an instance of [`EasydbConnectionCursor`](#EasydbConnectionCursor) for this connection.

## EasydbCursor

Using an `EasydbCursor` instance, PostgreSQL statements can be executed on the database that is connected to the **easydb** instance.

The following example shows how to execute a `SELECT` statement and log the result:

```python
# Parameter 'context': instance of EasydbContext
def easydb_cursor_example(context, logger):

    # get the EasydbCursor instance
    cursor = context.get_db_cursor()

    # get some rows of a table
    cursor.execute('SELECT text_a, int_b, bool_c FROM table WHERE int_b IN (1, 2, 3)')
    # the number of rows in the result is saved in cursor.rowcount
    logger.info('Statement returned {0} rows'.format(cursor.rowcount))

    # iterate over the rows
    for i in range(cursor.rowcount):
        # get the current row as a dict
        row = cursor.fetchone()
        # get the content of the columns
        logger.info('Row {0}: text_a: {1}'.format(i, row['text_a']))
        logger.info('Row {0}: int_b: {1}'.format(i, row['int_b']))
        logger.info('Row {0}: bool_c: {1}'.format(i, row['bool_c']))
```

### `execute`

```python
execute(statement)
```

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `statement` | String | Valid Postgresql Statement that will be executed using the current Connection and Transaction |

### `fetchone`

```python
fetchone()
```

Fetch the next row from the result. Returns a `dict` that contains the content of the result row.

The keys of the dictionary are the names of the database columns. The values are represented with a python data type according to the database type. For example:

| Database Type | Python Type |
|--|--|
| `text` | `str` |
| `int8` | `int` |
| `bool` | `bool` |
| `NULL` | `None` |

### `fetchall`

```python
fetchall()
```

Fetch all rows from the result. Returns a `list` which contains a `dict` for each row.

### `fetchmany`

```python
fetchmany([size])
```

Fetch the next rows from the result. If `size` is set, fetch this many rows. Returns a `list` which contains a `dict` for each row.

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `size` | Integer | Number of rows to fetch from the result | `None` |

### `commit`

```python
commit()
```

Commit the current Transaction.

### `abort`

```python
abort()
```

Abort the current Transaction.

## EasydbConnectionCursor

### Constructor

```python
__init__(connection)
```

| Name | Type | Description |
|--|--|--|
| `connection` | `EasydbConnection` | The `EasydbConnection` instance for this cursor |

This Constructor is called in the wrapper method [`cursor`](#cursor).

### `execute`

```python
execute(statement)
```

<!-- `db_execute` | Process | [EasydbConnectionCursor](#easydbconnectioncursor) | `execute` -->
Uses Callback `'db_execute'` in Context [*Process*](#process).

*Parameters:*

| Name | Type | Description |
|--|--|--|
| `statement` | String | Valid Postgresql Statement that will be executed using the current Connection and Transaction |

### `fetchall`

```python
fetchall()
```

Fetch all rows from the result.

<!-- `db_fetchall` | Process | [EasydbConnectionCursor](#easydbconnectioncursor) | `fetchall` -->
Uses Callback `'db_fetchall'` in Context [*Process*](#process).

### `fetchmany`

```python
fetchmany([size])
```

Fetch the next rows from the result. If `size` is set, fetch this many rows.

<!-- `db_fetchmany` | Process | [EasydbConnectionCursor](#easydbconnectioncursor) | `db_fetchmany` -->
Uses Callback `'db_fetchmany'` in Context [*Process*](#process).

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `size` | Integer | Number of rows to fetch from the result | `None` |

### `fetchone`

```python
fetchone()
```

Fetch the next row from the result.

<!-- `db_fetchone` | Process | [EasydbConnectionCursor](#easydbconnectioncursor) | `db_fetchone` -->
Uses Callback `'db_fetchone'` in Context [*Process*](#process).

## EasydbLogger

<!-- `log` | Base | [EasydbLogger](#easydblogger) | `_call` -->
Prints Log Messages, using the `Logger` class in the Server. Uses Callback `'log'` in Context [*Base*](#base).

The following methods are Wrapper methods for the log levels `DEBUG`, `INFO`, `WARN`, `ERROR` and print the String `message`:

### `debug`

```python
debug(message)
```

### `info`

```python
info(message)
```

### `warn`

```python
warn(message)
```

### `error`

```python
error(message)
```

