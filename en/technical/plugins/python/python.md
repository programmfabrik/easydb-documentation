# Python Plugins

The `EasydbContext` Class that is used in the Python Plugins, and its Helper Classes, provide various Wrapper Methods to perform API Calls to the easydb-Server. The following Methods are available and can be accessed using an Instance of `EasydbContext`:

[EasydbContext](#easydbcontext)

[EasydbProcessContext](#easydbprocesscontext)

[EasydbServerContext](#easydbservercontext)

[EasydbConnection](#easydbconnection)

[EasydbConnectionCursor](#easydbconnectioncursor)

[EasydbCursor](#easydbcursor)

[EasydbLogger](#easydblogger)

[EasydbException](#easydbexception)


## EasydbContext

### `call`

```python
call(self, method [, parameters[, returns_json]])
```

*Description:*

Executes an API Call for the given method. The Parameters are given as the String representation of a JSON-Object. Most of the following methods are convenient helper methods, which use this method and build the Parameter-Object from their parameters.

*Example Usage:*

```python
call ('dbapi_export', {'mask': '_all_fields', 'ids': [9, 24]})
```

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `method` | String | Name of the API method to be called |
| `parameters` | String | List of URL Parameters for the call in a JSON-Object | `None` |
| `returns_json` | Boolean | Should the call return a JSON Object? | `True` |

### `check_system_right`

```python
check_system_right(self, Right [, session])
```

*Description:*

Checks if the User of the specified Session has the given Right (or if the User is Root). If not, a `NoSystemRightError` is raised. If no Session is given, the current Session is used.

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `right` | String | Name of the Right to check |
| `session` | String | JSON representation of a Session | `None` |

### `check_system_right_bool_parameter`

```python
check_system_right_bool_parameter(self, right, parameter [, session])
```

*Description:*

Checks if the User of the specified Session has the given parameterized Right and if the Right is set to `True` (or if the User is Root). If not, a `NoSystemRightError` is raised. If no Session is given, the current Session is used.

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `right` | String | Name of the Right to check |
| `parameter` | String | Name of the Parameter of the parameterized Right |
| `session` | String | JSON representation of a Session | `None` |

### `create_unique_ids_type`

```python
create_unique_ids_type(self, type)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` | String |  |

### `dbapi_export`

```python
dbapi_export(self, mask, ids)
```

*Description:*

Call to API method `dbapi_export`. See [dbapi\_export](technical/internal/dbapi_export/dbapi_export.md)

*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `mask` | String | Mask Name |
| `ids` | String | JSON Array with Object IDs to export |

### `delete_unique_id`

```python
delete_unique_id(self, type, unique_id)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |
| `unique_id` |  |  |

### `drop_unique_ids_type`

```python
drop_unique_ids_type(self, type)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |

### `export_object_as_xml`

```python
export_object_as_xml(self, obj, mapping_type, mapping, user_id, language)
```

*Description:*

Export the given JSON Object as an XML Document. An [XML Mapping Profile](../../api/xmlmapping/xmlmapping.md) is applied.

*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `obj` | String | JSON Object to export |
| `mapping_type` | String | Type of the XML Mapping |
| `mapping` | String | Name of the XML Mapping Profile |
| `user_id` | String | ID of the User Profile |
| `language` | String | Language of the User that is used to export multilanguage Fields |

### `get_collection_json`

```python
get_collection_json(self, collection_id, connection_id)
```

*Description:*

Calls API Method `get_collection_json`. Returns JSON Object of the requested Collection.


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `collection_id` | String, Integer | ID of the requested Collection |
| `connection_id` | String, Integer | ID of the Connection that is used |

### `get_config`

```python
get_config(self [, path[, expected]])
```

*Description:*

Returns a JSON-Representation of the Configuration, or a Subobject if a path is specified. If `expected` is `True` and the requested Configuration does not exist, an `EasydbException` is raised.

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `path` | String | The path to a JSON-Subobject in the Configuration Object | `None` |
| `expected` | Boolean | If this Configuration must exist | `False` |

### `get_datamodel`

```python
get_datamodel(self)
```

*Description:*

Returns a JSON Representation of the current Datamodel. Uses API method `get_datamodel`.

### `get_db_cursor`

```python
get_db_cursor(self)
```

*Description:*

Returns a `EasydbCursor` object. Uses API method `db_cursor`.

### `get_environment_variables`

```python
get_environment_variables(self)
```

*Description:*

Returns a JSON Representation of the current environment variables. Uses API method `get_datamodel`.

### `get_exporter`

```python
get_exporter(self)
```

*Description:*

Returns the current Exorter. Uses API method `get_exporter`.

### `get_instance`

```python
get_instance(self)
```

*Description:*

Returns the Name of the current instance.

### `get_logger`

```python
get_logger(self, name)
```

*Description:*

Returns an instance of `EasydbLogger`.

*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `name` | String | Name of the Logger |

### `get_plugins`

```python
get_plugins(self)
```

*Description:*

Returns the JSON-Representations of the available Plugins. Uses API Method `get_plugins`.

### `get_plugin`

```python
get_plugin(self, name)
```

*Description:*

Returns the JSON-Representation of the Plugin with the given Name, if it exists in the result of `get_plugins()`.

*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `name` | String | Name of the Plugin |

### `get_remote_user`

```python
get_remote_user(self)
```

*Description:*

Returns the value of `REMOTE_USER` from the result of `get_environment_variables()`. Raises a `GenericServerError` if this key is not found.

### `get_kerberos_user`

```python
get_kerberos_user(self)
```

*Description:*

Returns the Result of `get_remote_user()`

### `get_session`

```python
get_session(self)
```

*Description:*

Returns the JSON-Representation of the current Session. Uses API Method `get_session`.

### `insert_unique_id`

```python
insert_unique_id(self, type, unique_id)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |
| `unique_id` |  |  |

### `ldap_bind`

```python
ldap_bind(self [, url[, who[, cred]]])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `url` |  |  | `None` |
| `who` |  |  | `None` |
| `cred` |  |  | `None` |

### `ldap_search`

```python
ldap_search(self, base, scope [, filterstr[, attrlist[, filter_output]]])
```

*Description:*


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
ldap_unbind(self)
```

*Description:*


### `next_unique_id`

```python
next_unique_id(self, type)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |

### `next_unique_id_prefixed`

```python
next_unique_id_prefixed(self, type, length, prefix)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |
| `length` |  |  |
| `prefix` |  |  |

### `search`

```python
search(self, session_type, session_identifier, query [, include_sets[, include_eas_urls]])
```

*Description:*

Performs a search request to the Elasticsearch Instance of the Server. The search result is returned as a JSON Object. See [api/search](../../api/search/search.md).

*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `session_type` |  |  |
| `session_identifier` |  |  |
| `query` | String | Elasticsearch Search Query |
| `include_sets` | Boolean | Should sets be included in the search? | `False` |
| `include_eas_urls` | Boolean | Should EAS URLs be included in the search? | `False` |

### `sequence_create`

```python
sequence_create(self, name [, minvalue[, maxvalue[, if_exists]]])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `name` |  |  |
| `minvalue` |  |  | `None` |
| `maxvalue` |  |  | `None` |
| `if_exists` | Boolean |  | `True` |

### `sequence_exists`

```python
sequence_exists(self, name)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `name` |  |  |

### `sequence_nextval`

```python
sequence_nextval(self, name)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `name` |  |  |

### `update_user_objects`

```python
update_user_objects(self, type, ids)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |
| `ids` |  |  |

## EasydbProcessContext

### `call`

```python
call(self, method [, parameters[, returns_json]])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `method` |  |  |
| `parameters` |  |  | `None` |
| `returns_json` | Boolean |  | `True` |

### `check_system_right`

```python
check_system_right(self, Right [, session])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `right` |  |  |
| `session` |  |  | `None` |

### `check_system_right_bool_parameter`

```python
check_system_right_bool_parameter(self, right, parameter [, session])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `right` |  |  |
| `parameter` |  |  |
| `session` |  |  | `None` |

### `create_session`

```python
create_session(self, connection, user_id)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `connection` |  |  |
| `user_id` |  |  |

### `create_unique_ids_type`

```python
create_unique_ids_type(self, type)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |

### `db_connect`

```python
db_connect(self, application_name)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `application_name` |  |  |

### `dbapi_export`

```python
dbapi_export(self, mask, ids)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `mask` |  |  |
| `ids` |  |  |

### `dbapi_import`

```python
dbapi_import(self, connection, session, mask, objects [, collection_id])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `connection` |  |  |
| `session` |  |  |
| `mask` |  |  |
| `objects` |  |  |
| `collection_id` |  |  | `None` |

### `delete_unique_id`

```python
delete_unique_id(self, type, unique_id)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |
| `unique_id` |  |  |

### `drop_unique_ids_type`

```python
drop_unique_ids_type(self, type)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |

### `export_object_as_xml`

```python
export_object_as_xml(self, obj, mapping_type, mapping, user_id, language)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `obj` |  |  |
| `mapping_type` |  |  |
| `mapping` |  |  |
| `user_id` |  |  |
| `language` |  |  |

### `get_collection_json`

```python
get_collection_json(self, collection_id, connection_id)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `collection_id` |  |  |
| `connection_id` |  |  |

### `get_config`

```python
get_config(self, connection)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `connection` |  |  |

### `get_datamodel`

```python
get_datamodel(self)
```

*Description:*


### `get_db_cursor`

```python
get_db_cursor(self)
```

*Description:*


### `get_environment_variables`

```python
get_environment_variables(self)
```

*Description:*


### `get_exporter`

```python
get_exporter(self)
```

*Description:*


### `get_instance`

```python
get_instance(self)
```

*Description:*


### `get_kerberos_user`

```python
get_kerberos_user(self)
```

*Description:*


### `get_logger`

```python
get_logger(self, name)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `name` |  |  |

### `get_plugin`

```python
get_plugin(self, name)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `name` |  |  |

### `get_plugins`

```python
get_plugins(self)
```

*Description:*


### `get_remote_user`

```python
get_remote_user(self)
```

*Description:*


### `get_session`

```python
get_session(self)
```

*Description:*


### `get_temp_dir`

```python
get_temp_dir(self)
```

*Description:*


### `insert_unique_id`

```python
insert_unique_id(self, type, unique_id)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |
| `unique_id` |  |  |

### `ldap_bind`

```python
ldap_bind(self [, url[, who[, cred]]])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `url` |  |  | `None` |
| `who` |  |  | `None` |
| `cred` |  |  | `None` |

### `ldap_search`

```python
ldap_search(self, base, scope [, filterstr[, attrlist[, filter_output]]])
```

*Description:*


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
ldap_unbind(self)
```

*Description:*


### `log_event`

```python
log_event(self, connection, event_type [, event_info])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `connection` |  |  |
| `event_type` |  |  |
| `event_info` |  |  | `None` |

### `next_unique_id`

```python
next_unique_id(self, type)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |

### `next_unique_id_prefixed`

```python
next_unique_id_prefixed(self, type, length, prefix)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |
| `length` |  |  |
| `prefix` |  |  |

### `put_asset_from_file`

```python
put_asset_from_file(self, session, filename, original_filename, mapping_name, mask, objecttype, pool_id)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `session` |  |  |
| `filename` |  |  |
| `original_filename` |  |  |
| `mapping_name` |  |  |
| `mask` |  |  |
| `objecttype` |  |  |
| `pool_id` |  |  |

### `search`

```python
search(self, connection, session_type, session_identifier, query [, include_sets[, include_eas_urls]])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `connection` |  |  |
| `session_type` |  |  |
| `session_identifier` |  |  |
| `query` |  |  |
| `include_sets` | Boolean |  | `False` |
| `include_eas_urls` | Boolean |  | `False` |

### `sequence_create`

```python
sequence_create(self, name [, minvalue[, maxvalue[, if_exists]]])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `name` |  |  |
| `minvalue` |  |  | `None` |
| `maxvalue` |  |  | `None` |
| `if_exists` | Boolean |  | `True` |

### `sequence_exists`

```python
sequence_exists(self, name)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `name` |  |  |

### `sequence_nextval`

```python
sequence_nextval(self, name)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `name` |  |  |

### `update_user_objects`

```python
update_user_objects(self, type, ids)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |
| `ids` |  |  |

## EasydbServerContext

### `call`

```python
call(self, method [, parameters[, returns_json]])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `method` |  |  |
| `parameters` |  |  | `None` |
| `returns_json` | Boolean |  | `True` |

### `check_system_right`

```python
check_system_right(self, Right [, session])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `right` |  |  |
| `session` |  |  | `None` |

### `check_system_right_bool_parameter`

```python
check_system_right_bool_parameter(self, right, parameter [, session])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `right` |  |  |
| `parameter` |  |  |
| `session` |  |  | `None` |

### `create_unique_ids_type`

```python
create_unique_ids_type(self, type)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |

### `dbapi_export`

```python
dbapi_export(self, mask, ids)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `mask` |  |  |
| `ids` |  |  |

### `delete_unique_id`

```python
delete_unique_id(self, type, unique_id)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |
| `unique_id` |  |  |

### `drop_unique_ids_type`

```python
drop_unique_ids_type(self, type)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |

### `export_object_as_xml`

```python
export_object_as_xml(self, obj, mapping_type, mapping, user_id, language)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `obj` |  |  |
| `mapping_type` |  |  |
| `mapping` |  |  |
| `user_id` |  |  |
| `language` |  |  |

### `get_collection_json`

```python
get_collection_json(self, collection_id, connection_id)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `collection_id` |  |  |
| `connection_id` |  |  |

### `get_config`

```python
get_config(self [, path[, expected]])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `path` |  |  | `None` |
| `expected` | Boolean |  | `False` |

### `get_datamodel`

```python
get_datamodel(self)
```

*Description:*


### `get_db_cursor`

```python
get_db_cursor(self)
```

*Description:*


### `get_environment_variables`

```python
get_environment_variables(self)
```

*Description:*


### `get_exporter`

```python
get_exporter(self)
```

*Description:*


### `get_instance`

```python
get_instance(self)
```

*Description:*


### `get_kerberos_user`

```python
get_kerberos_user(self)
```

*Description:*


### `get_logger`

```python
get_logger(self, name)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `name` |  |  |

### `get_plugin`

```python
get_plugin(self, name)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `name` |  |  |

### `get_plugins`

```python
get_plugins(self)
```

*Description:*


### `get_remote_user`

```python
get_remote_user(self)
```

*Description:*


### `get_session`

```python
get_session(self)
```

*Description:*


### `get_temp_dir`

```python
get_temp_dir(self)
```

*Description:*


### `insert_unique_id`

```python
insert_unique_id(self, type, unique_id)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |
| `unique_id` |  |  |

### `ldap_bind`

```python
ldap_bind(self [, url[, who[, cred]]])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `url` |  |  | `None` |
| `who` |  |  | `None` |
| `cred` |  |  | `None` |

### `ldap_search`

```python
ldap_search(self, base, scope [, filterstr[, attrlist[, filter_output]]])
```

*Description:*


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
ldap_unbind(self)
```

*Description:*


### `next_unique_id`

```python
next_unique_id(self, type)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |

### `next_unique_id_prefixed`

```python
next_unique_id_prefixed(self, type, length, prefix)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |
| `length` |  |  |
| `prefix` |  |  |

### `register_callback`

```python
register_callback(self, callback_type, callback_parameters)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `callback_type` |  |  |
| `callback_parameters` |  |  |

### `search`

```python
search(self, session_type, session_identifier, query [, include_sets[, include_eas_urls]])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `session_type` |  |  |
| `session_identifier` |  |  |
| `query` |  |  |
| `include_sets` | Boolean |  | `False` |
| `include_eas_urls` | Boolean |  | `False` |

### `sequence_create`

```python
sequence_create(self, name [, minvalue[, maxvalue[, if_exists]]])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `name` |  |  |
| `minvalue` |  |  | `None` |
| `maxvalue` |  |  | `None` |
| `if_exists` | Boolean |  | `True` |

### `sequence_exists`

```python
sequence_exists(self, name)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `name` |  |  |

### `sequence_nextval`

```python
sequence_nextval(self, name)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `name` |  |  |

### `update_user_objects`

```python
update_user_objects(self, type, ids)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `type` |  |  |
| `ids` |  |  |

## EasydbConnection

### `close`

```python
close(self)
```

*Description:*


### `commit`

```python
commit(self)
```

*Description:*


### `cursor`

```python
cursor(self)
```

*Description:*


### `open_txn`

```python
open_txn(self)
```

*Description:*


## EasydbConnectionCursor

### `_call`

```python
_call(self, operation)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `operation` |  |  |

### `execute`

```python
execute(self, statement)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `statement` |  |  |

### `fetchall`

```python
fetchall(self)
```

*Description:*


### `fetchmany`

```python
fetchmany(self [, size])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `size` |  |  | `None` |

### `fetchone`

```python
fetchone(self)
```

*Description:*


## EasydbCursor

### `_call`

```python
_call(self, operation)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `operation` |  |  |

### `abort`

```python
abort(self)
```

*Description:*


### `commit`

```python
commit(self)
```

*Description:*


### `execute`

```python
execute(self, statement)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `statement` |  |  |

### `fetchall`

```python
fetchall(self)
```

*Description:*


### `fetchmany`

```python
fetchmany(self [, size])
```

*Description:*


*Parameters:*

| Name | Type | Description | Default |
|--|--|--|--|
| `size` |  |  | `None` |

### `fetchone`

```python
fetchone(self)
```

*Description:*


## EasydbLogger

### `_call`

```python
_call(self, level, message)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `level` |  |  |
| `message` |  |  |

### `debug`

```python
debug(self, message)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `message` |  |  |

### `error`

```python
error(self, message)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `message` |  |  |

### `info`

```python
info(self, message)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `message` |  |  |

### `warn`

```python
warn(self, message)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `message` |  |  |

## EasydbException

### `get_code`

```python
get_code(self)
```

*Description:*


### `get_parameter`

```python
get_parameter(self, parameter)
```

*Description:*


*Parameters:*

| Name | Type | Description |
|--|--|--|--|
| `parameter` |  |  |