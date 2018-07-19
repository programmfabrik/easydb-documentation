---
title: "59 - db"
menu:
  main:
    name: "db"
    identifier: "technical/api/db_info"
    parent: "technical/api"
---
# Get information about objects to be created
    POST /api/v1/db_info/create?token=<token>

Retrieves information about what kind of objects is the session user allowed to create.

Usually, this call is executed twice:

1. without parameters, to obtain the list of allowed objecttypes and pools
2. with an objecttype (and a pool), to obtain the available tags and masks

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Input

A JSON object with the following attributes

|   |   |
|---|---|
| `objecttype` | Object type of the object (string, optional) |
| `pool_id`    | Pool ID the new object will be in (integer, optional), this is ignored if the `objecttype` was not provided |
| `tag_ids`    | Tag IDs for the new object (array of integers, optional, nullable), this is ignored if the `objecttype` was not provided |

If `tag_ids` is not given and the objecttype supports tags, the server will use the default tags. In this case, if the objecttype has a pool link
the `pool_id` is required. Otherwise, no tags will be used.

If `tag_ids` is set to **null**, tag filters will be ignored.

## Output

The output format is described below. The following rules apply:

- If the user did not provide an `objecttype`, the output contains the `_available_objecttypes`
- If the user provided an `objecttype` with pool link, but did not provide a pool:
    - if there is not pool/mask combination available, the call will return an error (***)
    - if there are available combinations, the call will return the `_available_objecttypes`, filtered by `objecttype` and available pools
- If the user provided an `objecttype` without pool, or an `objecttype` / `pool_id` combination:
    - if the objecttype lacks the `create` right, the call returns an empty `_available_objecttypes`
    - if there are no masks available, the call will return a NoMasksForCreateError
    - else, the call will return the `_available_objecttypes`, `_available_tags` and `_available_masks`

If the `tag_ids` parameter is provided, the tag filters will be checked against the given tags. If no `tag_ids` are provided, the tag filters will be ignored.
If the creation is not allowed for the given combination, an error is returned.

The output is a JSON object:

| Parameter | Description |
|---|---|
| `_available_objecttypes` | Available objecttypes for which the user has a "create" right (list), optionally filtered (see above) |
| &#8614; `_id`            | Objecttype ID (integer) |
| &#8614; `name`           | Objecttype name (string) |
| &#8614; `pool_ids`       | Pool IDs for which the user has a "create" right (list of integers) |
| `_available_tags`        | Available tags |
| &#8614; `_id`            | Tag ID (integer) |
| &#8614; `_is_default`    | Tag is default (boolean) |
| `_available_masks`       | Available masks |
| &#8614; `_id`            | Mask ID (integer): the mask "\_all\_fields" has no ID |
| &#8614; `name`           | Mask name (string) |

The `_available_masks` are sorted by preference, according to the rules stated in [mask management](/en/technical/maskmanagement).

## Permissions

The user has to be authenticated.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 400 | [No Masks For Create](/en/technical/errors): no masks available |
| 500 | [Server error](/en/technical/errors): internal server error |





# Get information about objects to be updated
    POST /api/v1/db_info/update?token=<token>

Retrieves information about permissions, available masks and available tags for existing objects.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |

## Input

A JSON object with the following attributes

|   |   |
|---|---|
| `objecttype` | Object type of the object (string) |
| `object_ids` | Object IDs of existing objects (array of integers) |
| `pool_id`    | New pool for the objects (integer, optional) |
| `tag_ids`    | Tag IDs for the new objects (array of integers, optional) |

## Output

The output is a JSON object with the following attributes:

|   |   |
|---|---|
| `_generated_rights` | Effective rights for the objects (map) |
| `_available_pools`  | Pools the user is allowed to link the objects to (list of integers) |
| `_available_tags`   | Available tags for the objects (array of [tag entries](/en/technical/types/tag_entry)): only provided if "write" is in `_generated_rights` |
| `_available_masks`  | Available masks for the objects (array of entries: see below): only provided if "write" is in `_generated_rights` |

All fields are calculated as the intersection of the values for each object. That means that if only one object in the list
does not have the "unlink" right, it will not appear in the list, for instance. Conversely, every right that appears in the
`_generated_rights` is available for each object. The same applies to the other attributes.

The generated rights taken into account are: "read", "write", "delete" and "unlink". If the user has no "write" right, "unlink"
will not be tested, since they would not to be able to modify the object anyway. So, the possible values are:

```
{ [ "read", ["write", ["delete"], ["unlink"]] ] }
```

The `_available_tags` are only rendered with the attributes `_id` and `_is_default`.

The `_available_masks` are sorted by preference, according to the rules stated in [mask management](/en/technical/maskmanagement). Each entry
contains the mask name as `name` (string) and the mask ID as `_id` (integer). The mask "_all_fields" has no ID.

If the `pool_id` parameter is provided, the `available_tags` and `available_masks` will take into account this ID instead of
the current pool IDs of the objects.

If the `tag_ids` parameter is provided, the `available_tags` and `available_masks` will take into account these tags instead of
the current tags of the objects.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Not Authenticated](/en/technical/errors): session is not authenticated |
| 500 | [Server error](/en/technical/errors): internal server error |
