---
title: "92 - Errors"
menu:
  main:
    name: "Errors"
    identifier: "technical/errors"
    parent: "technical"
---
# Errors

Errors are identified by their code and belong to one of three different realms:

| Name               | Description   |
|--------------------|---------------|
| `realm`            | error realm (string): **server**, **api**, **user** |
| `code`             | error code (string): identifier and CSV key for the error |
| `parameters`       | parameters for the error (map string &#8614; string, optional): only for user errors that require parameters |
| `description`      | error description (string, optional): only for server and API errors |
| `uuid`             | internal error UUID (string, optional): only for server errors |

# <a name="api"></a> API Errors

The requester made an error using the API. Normally it is a syntax error, such as a type mismatch or
something missing. The response HTTP status code is 400.

The error `code` begins with "error.api" and represents a specialized class of API errors.
The error `description` is a text in English.

Example:


{{< include_json "./example_api.json" >}}


Currently supported API errors are:

- error.api.generic: API errors that do not fit into the other categories
- error.api.invalid_request_method: API call does not support the request method
- error.api.invalid_content: The request content is invalid (bad content-type, empty body...)
- error.api.invalid_api: The API call is invalid (for example: /api/foo)
- error.api.attribute_expected: An attribute was expected in a JSON definition
- error.api.type_mismatch: The type of an attribute is wrong
- error.api.invalid_value: The value of an attribute is wrong
- error.api.positional_parameter_expected: A positional parameter is expected
- error.api.attribute_not_accepted: An attribute provided by the user is not accepted
- error.api.invalid_maskset: The provided maskset is malformed
- error.api.eas: A 400 error from EAS occurred
- error.api.suggest_lock_taken: API Call tried to rebuild the suggest index while it was already building





# <a name="server"></a> Server errors

An internal server error occurred which prevented the fulfilment of the request.
The response HTTP status code is 500.

The error `code` begins with "error.server" and the `description` is a text in English.
Server errors also provide the parameter `uuid`, which can be used to retrieve the error details using
[/api/server/error](/en/technical/api/server).

Example:


{{< include_json "./example_server.json" >}}


Currently supported server errors are:

- error.server.generic: for unexpected errors from inside easydb
- error.server.database: for unexpected errors caused by the database
- error.server.elasticsearch: for unexpected errors caused by Elasticsearch
- error.server.eas: for unexpected errors caused by EAS
- error.server.internal_file_error: for unexpected file operation errors




# User errors

User errors are errors that can be triggered by the user. The response HTTP status code is 400.
They are localized (the CSV key is the error code) and may have parameters to be used with the localized texts.

The `code` begins with "error.user". The different user errors are discussed in more detail below.

Example:


{{< include_json "./example_user.json" >}}





## Rights management

> <a name="not_authenticated"></a>Not Authenticated (error.user.not_authenticated)

The session is not authenticated.

> <a name="authentication_method_not_allowed"></a>Authentication Method Not Allowed (error.user.authentication_method_not_allowed)

The authentication method that was provided is nto allowed

- method: the authentication method

> <a name="tasks_not_confirmed"></a>Tasks Not Confirmed (error.user.tasks_not_confirmed)

There are pending tasks associated with this session that require confirmation.

> <a name="insufficient_rights"></a>Insufficient Rights (error.user.insufficient_rights)

The user lacks the right to perform a certain operation.

- operation: "create", "read", "update", "delete", "fill" (collection objects manipulation)
- type: the name of the objecttype or base type
- ids: affected IDs (a comma-separated list of IDs or "-")
- right: name of the right
- extra_info (optional): used for rights with parameters to specify parameter information

> <a name="insufficient_rights_after_transition"></a>Insufficient Rights After Transition (error.user.insufficient_rights_after_transition)

The user lost the right to perform a certain operation after a transition. It has the same parameters as "error.user.insufficient_rights".

> <a name="right_revoked"></a>Rights Revoked (error.user.right_revoked)

The user revokes a right he had before. It has the same parameters as "error.user.insufficient_rights".

> <a name="change_owner_on_creation"></a>Change Owner On Creation (error.user.change_owner_on_creation)

The user attempts to create a new base or user object with a different owner.

> <a name="invalid_owner_on_creation"></a>Invalid Owner On Creation (error.user.invalid_owner_on_creation)

The user attempts to create a new user object with an invalid owner.

> <a name="no_system_right"></a>No System Right (error.user.no_system_right)

The user lacks a system right in order to perform a certain operation

- right: name of the right
- extra_info: if the system right has any parameters and something is missing there will be information here

> <a name="no_grantable_right"></a>No Grantable Right (error.user.no_grantable_right)

Inserting an object into a collection would grant a right to it that the collection owner lacks (as "grantable").

- collection: id of the collection
- objecttype: objecttype of the affected object
- object\_id: id of the affected object
- right: name of the right
- extra_info (optional): used for rights with parameters to specify parameter information

> <a name="upload_limit_exceeded"></a>Upload Limit Exceeded (error.user.upload_limit_exceeded)

Upload limit exceeded

- filename: file name
- class: file class (including "other"), or "global" if the limit is the global updload limit
- limit: value of the limit

> <a name="upload_type_not_allowed"></a>Upload Type Not Allowed (error.user.upload_type_not_allowed)

Uploaded file type is not allowes

- filename: file name
- class: file class
- extension: the file extension detected for the file






## General data manipulation errors

These errors can occur in different API calls (user and base objects).

> <a name="version_mismatch"></a>Version Mismatch (error.user.version_mismatch)

The user tries to update an older version of an entity.

- provided: version provided by user
- expected: expected version

> <a name="integrity_constraint_violation"></a>Integrity Constraint Violation (error.user.integrity_constraint_violation)

The operation violates an integrity constraint, including: unique, restrict

- constraint: name of the constraint

> <a name="foreign_key_constraint_violation"></a>Foreign Key Constraint Violation (error.user.foreign_key_constraint_violation)

The operation violates a foreign key constraint

- constraint: name of the constraint

> <a name="check_constraint_violation"></a>Check Constraint Violation (error.user.check_constraint_violation)

The operation violates a check constraint

- constraint: name of the constraint

> <a name="not_null_violation"></a>Not Null Violation (error.user.not_null_violation)

The operation violates a not null constraint, i.e. a required attribute was not provided or was empty

- column: column name

> <a name="object_not_found"></a>Object Not Found (error.user.object_not_found)

The requested user object could not be found

- objecttype: objecttype name
- id: object ID

> <a name="instance_not_found"></a>Instance Not Found (error.user.instance_not_found)

The requested instance could not be found

- id: instance ID






## User management

> <a name="user_not_found"></a>User Not Found (error.user.user_not_found)

The server cannot find the given user

- id: the user ID

> <a name="group_not_found"></a>Group Not Found (error.user.group_not_found)

The server cannot find the given group

- id: the group ID

> <a name="bad_password"></a>Bad Password (error.user.bad_password)

Password is not accepted due to policy

- hint: a hint describing the policy (this is a l10n field provided in the base config and it is rendered in the session language)

> <a name="same_password"></a>Same Password (error.user.same_password)

Password is not accepted because it is repeated

> <a name="invalid_password"></a>Invalid Password (error.user.invalid_password)

Wrong password

> <a name="authentication_token_expired"></a>Authentication Token Expired (error.user.authentication_token_expired)

The user is using an authentication token that has expired. The authentication token is only used in the password reset process and should not be confused with the session token.

> <a name="authentication_token_used"></a>Authentication Token Used (error.user.authentication_token_used)

The user is using an authentication token that has already been used

> <a name="forgotten_password_process_disabled"></a>Forgotten Password Process Disabled (error.user.forgotten_password_process_disabled)

Forgotten password process disabled by frontend configuration

> <a name="user_has_no_email"></a>User Has No Email (error.user.user_has_no_email)

The user has no e-mail address

> <a name="primary_check_number"></a>Primary Check Number (error.user.primary_check_number)

The user has provided more than one primary e-mail addresses

> <a name="primary_check_active"></a>Primary Check Active (error.user.primary_check_active)

The user is trying to set an inactive e-mail to be primary

> <a name="intended_primary_check_number"></a>Intended Primary Check Number (error.user.intended_primary_check_number)

The user has provided more than one intended primary e-mail addresses

> <a name="intended_primary_check_requested"></a>Intended Primary Check Requested (error.user.intended_primary_check_requested)

The user is trying to set an e-mail to be intended primary without requesting confirmation

> <a name="email_confirmation_not_required"></a>Email Confirmation Not Required (error.user.email_confirmation_not_required)

The e-mail does not need confirmation

> <a name="email_already_confirmed"></a>Email Already Confirmed (error.user.email_already_confirmed)

The e-mail was already confirmed

> <a name="email_not_found"></a>E-Mail Not Found (error.user.email_not_found)

The server cannot find the given e-mail

- id: the e-mail

> <a name="email_confirmation_failed"></a>Email Confirmation Failed (error.user.email_confirmation_failed)

E-mail confirmation failed

> <a name="user_update_system_group"></a>User Update System Group (error.user.user_update_system_group)

The user tries to put a user in a system group

- user_id: the user ID
- group_id: the system group ID

> <a name="update_system_user"></a>Update System User (error.user.update_system_user)

Attribute cannot be updated because the user is a system user

- user_id: the system user ID
- attribute: the attribute that the user was trying to update

> <a name="delete_system_user"></a>Delete System User (error.user.delete_system_user)

User cannot be deleted because it is a system user

- user_id: the system user ID

> <a name="invalid_user_type_change"></a>Invalid User Type Change (error.user.invalid_user_type_change)

Invalid user type change: it is only possible to change the type of an "email" user to "easydb".

- user_id: the user ID, or "<new>" if the user is attempting to set the type of the user on creation.

> <a name="user_auto_disable"></a>User Auto Disable (error.user.user_auto_disable)

A user is attempting to disable its own login

> <a name="email_already_exists"></a>Email Already Exists (error.user.email_already_exists)

The provided e-mail already exists in the system

- address: the e-mail address

> <a name="delete_system_group"></a>Delete System Group (error.user.delete_system_group)

Group cannot be deleted because it is a system group

- group_id: the system group ID

> <a name="register_user_login_or_email_required"></a>Register User Login Or Email Required (error.user.register_user_login_or_email_required)

Attempting to register as new user without login nor e-mail address

> <a name="custom_type_required"></a>Custom Type Required (error.user.custom_type_required)

Attempting to assign the "system.user.create_new" right with type "custom" but without specifying the "custom_type"

> <a name="group_required"></a>Group Required (error.user.group_required)

Attempting to create a user without group when "require_group" was set

> <a name="login_change_not_allowed_for_email_user"></a>Login Change Not Allowed For Email User (error.user.login_change_not_allowed_for_email_user)

Attempting to change the login of an "email" user




## Schema and maskset manipulation

> <a name="invalid_table_name"></a>Invalid Table Name (error.user.invalid_table_name)

The user provided a table name that does not comply with the rules defined.

- name: the provided table name

> <a name="invalid_column_name"></a>Invalid Column Name (error.user.invalid_column_name)

The user provided a column name that does not comply with the rules defined.

- name: the provided column name

> <a name="invalid_mask_name"></a>Invalid Mask Name (error.user.invalid_mask_name)

The user provided a mask name that does not comply with the rules defined.

- name: the provided mask name

> <a name="no_preferred_mask"></a>No Preferred Mask (error.user.no_preferred_mask)

No preferred mask specified in the maskset for the given objecttype.

- objecttype: objecttype for which no mask was found

> <a name="more_than_one_preferred_masks"></a>More Than One Preferred Masks (error.user.more_than_one_preferred_masks)

More than one preferred masks specified in the maskset for the given objecttype.

- objecttype: objecttype for which more than one masks were found





## User object manipulation

> <a name="object_not_found"></a>Object Not Found (error.user.object_not_found)

The server cannot find the given object

- id: the object ID

Depending on how the user specified the object ID, it can be a global object ID  or a combination of objecttype and ID.

- If it is a global object ID, it will contain a "@"
- If not, it will have the form: "\<objecttype\>:\<id\>".

> <a name="object_owner_null"></a>Object Owner Null (error.user.object_owner_null)

The user provided an object without owner

> <a name="old_mask_missing"></a>Old Mask Missing (error.user.old_mask_missing)

The user requested an object using an old schema version and a mask that did not exist in that version.

- mask_name: requested mask name
- mask_id: mask id (in the current schema version)
- schema_version: requested schema version

> <a name="old_schema_missing"></a>Old Schema Missing (error.user.old_schema_missing)

The user requested an object version for which no old schema version could be found.

- objecttype: type of the requested object
- id: object id
- object_version: requested object version

> <a name="no_mask_defined_for_collection"></a>No Mask Defined For Collection (error.user.no_mask_defined_for_collection)

The user attempts to create objects in a collection using [/api/db](../api/db) with the `collection` parameter.
The collection has no mask defined for object creation.

- collection_id: collection id

> <a name="no_pool_defined_for_collection"></a>No Pool Defined For Collection (error.user.no_pool_defined_for_collection)

The user attempts to create objects in a collection using [/api/db](/en/technical/api/db) with the `collection` parameter.
The objecttype has a pool link, but the collection has no pool defined for object creation.

- collection_id: collection id

> <a name="bad_objecttype_for_collection"></a>Bad Objecttype For Collection (error.user.bad_objecttype_for_collection)

The user attempts to create objects in a collection using [/api/db](/en/technical/api/db) with the `collection` parameter.
The objecttype is not the one configured in the collection for object creation.

- collection_id: collection id
- expected_objecttype_id: expected objecttype id

> <a name="bad_mask_for_collection"></a>Bad Mask For Collection (error.user.bad_mask_for_collection)

The user attempts to create objects in a collection using [/api/db](/en/technical/api/db) with the `collection` parameter.
The provided mask is not the one configured in the collection for object creation.

- collection_id: collection id
- expected_mask_id: expected mask id

> <a name="bad_pool_for_collection"></a>Bad Pool For Collection (error.user.bad_pool_for_collection)

The user attempts to create objects in a collection using [/api/db](/en/technical/api/db) with the `collection` parameter.
The objecttype has a pool link, but the provided pool is not the one configured in the collection for object creation.

- collection_id: collection id
- expected_pool_id: expected pool id

> <a name="collection_is_not_under_user_collection"></a>Collection Is Not Under User Collection (error.user.collection_is_not_under_user_collection)

The user is trying to create or move a collection outside of the user collection tree.

> <a name="transition_reject"></a>Transition Reject (error.user.transition_reject)

The operation was rejected by a transition.

- message: a message describing the reason, if the transition defines it; else, a generic message containing the transition ID

> <a name="bad_confirm_code"></a>Bad Confirm Code (error.user.bad_confirm_code)

The confirm code for the operation is invalid.

> <a name="bad_mask_for_update"></a>Bad Mask For Update (error.user.bad_mask_for_update)

A mask with mask filter was provided for POST /api/db

- mask: mask name

> <a name="link_root_pool"></a>Link Root Pool (error.user.link_root_pool)

The user is trying to link an object to the root pool

- object_id: the object ID, or "<new>" if it is a new object


## Pool errors

> <a name="pool_not_found"></a>Pool Not Found (error.user.pool_not_found)

The server cannot find the given pool

- id: the pool ID

> <a name="pool_requires_parent"></a>Pool Requires Parent (error.user.pool_requires_parent)

The user is trying to create a pool but has not specified a parent

> <a name="system_pool_update_parent"></a>System Pool Update Parent (error.user.system_pool_update_parent)

The user is trying to change the parent of a system pool

- id: the pool ID

> <a name="system_pool_delete"></a>System Pool Delete (error.user.system_pool_delete)

The user is trying to delete a system pool

- id: the pool ID





## Collection errors

> <a name="collection_not_found"></a>Collection Not Found (error.user.collection_not_found)

The server cannot find the given collection

- id: the collection ID

> <a name="collection_does_not_allow_children"></a>Collection Does Not Allow Children (error.user.collection_does_not_allow_children)

The user is trying to create or move a collection under a collection that does not allow children

- id: the collection ID of the collection that does not allow children

> <a name="collection_requires_parent"></a>Collection Requires Parent (error.user.collection_requires_parent)

The user is trying to create a collection but has not specified a parent

> <a name="system_collection_update"></a>System Collection Update (error.user.system_collection_update)

The user is trying to change an attribute of a system collection which cannot be changed

- id: the collection ID

> <a name="system_collection_delete"></a>System Collection Delete (error.user.system_collection_delete)

The user is trying to delete a system collection

- id: the collection ID

> <a name="collection_user_secret_already_exists"></a>Collection User Secret Already Exists (error.user.collection_user_secret_already_exists)

There is a user associated with the secret provided for a new collection user

- secret: the text provided as secret

> <a name="collection_sharing_inactive"></a>Collection Sharing Inactive (error.user.collection_sharing_inactive)

The ACL entry that enables collection sharing for the provided credentials is not active

> <a name="collection_sharing_too_soon"></a>Collection Sharing Too Soon (error.user.collection_sharing_too_soon)

The ACL entry that enables collection sharing for the provided credentials is not valid yet

- timestamp: the "valid_from" field from the ACL entry

> <a name="collection_sharing_too_late"></a>Collection Sharing Too Late (error.user.collection_sharing_too_late)

The ACL entry that enables collection sharing for the provided credentials is no longer valid

- timestamp: the "valid_to" field from the ACL entry

> <a name="collection_name_repeated"></a>Collection Name Repeated (error.user.collection_name_repeated)

There already exists a collection with the given name under the same parent collection





## Export errors

> <a name="export_already_running"></a>Export Already Running (error.user.export_already_running)

The user is trying to start an export which is already running.

> <a name="export_name_required"></a>Export Name Required (error.user.export_name_required)

The user is trying to create a scheduled export with no name.





## Search/suggest errors

> <a name="search_no_mask_found"></a>Search: No Mask Found (error.user.search_no_mask_found)

The user provided an objecttype for which no mask was found

- objecttype: the objecttype name





## Session errors

> <a name="session_not_found"></a>Session Not Found (error.user.session_not_found)

The server cannot find the given session

- id: the session token

> <a name="session_invalid"></a>Session Invalid (error.user.session_invalid)

The session provided is invalid

> <a name="username_or_password_empty"></a>Username or Password Empty (error.user.username_or_password_empty)

The user provided an empty user or password when authenticating

> <a name="login_failed"></a>Login Failed (error.user.login_failed)

Login failed

> <a name="login_disabled"></a>Login Disabled (error.user.login_disabled)

Login failed because it was disabled

> <a name="login_disabled_from"></a>Login Disabled From (error.user.login_disabled_from)

Login failed because it was disabled in a certain datetime range: from

- from: datestamp from

> <a name="login_disabled_to"></a>Login Disabled To (error.user.login_disabled_to)

Login failed because it was disabled in a certain datetime range: to

- to: datestamp to






## Other errors

> <a name="tag_not_found"></a>Tag Not Found (error.user.tag_not_found)

The server cannot find the given tag

- id: the tag ID

> <a name="right_not_found"></a>Right Not Found (error.user.right_not_found)

The server cannot find the given right

- id: the right ID

> <a name="message_not_found"></a>Message Not Found (error.user.message_not_found)

The server cannot find the given message

- id: the message ID

> <a name="objecttype_not_found"></a>Objecttype Not Found (error.user.objecttype_not_found)

The server cannot find the given objecttype

- id: the objecttype name

> <a name="mask_not_found"></a>Mask Not Found (error.user.mask_not_found)

The server cannot find the given mask

- id: the mask name

> <a name="event_not_found"></a>Event Not Found (error.user.event_not_found)

The server cannot find the given event

- id: the event ID

> <a name="error_not_found"></a>Error Not Found (error.user.error_not_found)

The server cannot find the given error

- id: the error UUID

> <a name="language_not_found"></a>Language Not Found (error.user.language_not_found)

The server cannot find the given language

- id: the language

> <a name="asset_not_found"></a>Asset Not Found (error.user.asset_not_found)

EAS cannot find the given asset

- id: the asset ID

> <a name="wrong_value"></a>Wrong Value (error.user.wrong_value)

The provided value does not meet the expected form (i.e. a regex)

- variable: the name of the variable for which the value was set
- value: the provided value
- hint: a text explaining why the value is not accepted

> <a name="right_preset_not_found"></a>Right Preset Not Found (error.user.right_preset_not_found)

The server cannot find the given right preset

- id: the ID of the right preset

> <a name="no_masks_for_create"></a>No Masks For Create (error.user.no_masks_for_create)

There are no masks available for the objecttype / pool combination provided to /api/db_info/create

- objecttype: the objecttype provided
- pool: the pool provided
    - if the objecttype has no available pools, "-" is returned; this call should not have been made because the previous create call (without "objecttype" should not list this one)
    - if the objecttype has no pool link, "N/A" is returned

> <a name="event_type_disabled"></a>Event Type Disabled (error.user.event_type_disabled)

The user attempts to POST en event whose type has been disabled via base config

- event_type: the type of the event

> <a name="invalid_value"></a>Invalid Value (error.user.invalid_value)

The user provided an invalid value for an attribute

- attribute: the name of the attribute
- value: the value provided by the user
- expected_format: the format expected for the attribute

> <a name="objects_not_allowed"></a> Objects Not Allowed (error.user.objects_not_allowed)

Using /api/objects without the required base config parameter
