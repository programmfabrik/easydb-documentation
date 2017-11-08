# Retrieve objects as deep links
    GET /api/v1/objects/...

Returns a user object or asset in the specified format

If an authorized session is provided, the search will be performed using it. Else, the search will be conducted
on behalf of the system user "deep_link".

## Path parameters

The path parameters specify which object or asset is being accessed. It is organized in "path parts", consisting of one
or more path entries.

The path parts can be given in any particular order.

### Path part: object selection

Objects can be accessed in one of three ways. One and only one of the following has to be provided:

|URL path|description|
|---|---|
|**id**||
|*system\-object\-id*| `_system_object_id` of the object |

|URL path|description|
|---|---|
|**uuid**||
|*uuid*| `_uuid` of the object |

|URL path|description|
|---|---|
|**column**||
|*column*| name of the column used to search the object, it has to be unique |
|*value*| value to search for |

### Path part: mask selection

If not specified, the object will be returned in the best mask.

|URL path|description|
|---|---|
|**mask**||
|*mask-name*| name of the mask to use |

### Path part: version selection

> This is only a concept and not yet implemented!

These parameters allow to ask for a specific version of the object. The object will be rendered in the schema version that was current when the object version was created. It is not possible to combine them:

Latest version (default):

|URL path|description|
|---|---|
|**latest**||

A specific version, by version number:

|URL path|description|
|---|---|
|**version**||
|*version*|version of the object|

A specific version, by date:

|URL path|description|
|---|---|
|**date**||
|*date*| Date (+ time) in ISO 8601 format. Returns the latest version at the given time, accepted combinations of date and time are:<br>**date:** `YYYY`, `YYYY-MM`, `YYYY-MM-DD`<br>**date + time:** `YYYY-MM-DD%20HH`, `YYYY-MM-DD%20HH:MM`, `YYYY-MM-DD%20HH:MM:SS`, `YYYY-MM-DD%20HH:MM:SSZ`,<br>`YYYY-MM-DDTHH`, `YYYY-MM-DDTHH:MM`, `YYYY-MM-DDTHH:MM:SS`, `YYYY-MM-DDTHH:MM:SSZ` |

### Path part: file selection

If specified, an asset will be returned.
There are several options:

|URL path|description|
|---|---|
|**file**||
|**standard**||
|*n*| nth file in `_standard` |

|URL path|description|
|---|---|
|**file**||
|**all**||
|*n*| nth file in object: the order is determined by the mask |

|URL path|description|
|---|---|
|**file**||
|**column**||
|*name*| column name |
|*n*| nth position (only for nested) |

|URL path|description|
|---|---|
|**file**||
|**id**||
|*n*| file ID (EAS-ID) |

### Path part: file version selection

Only valid in combination with **file**. Defaults to "preferred".
There are two options:

|URL path|description|
|---|---|
|**file_browser**||
|**preferred**| preferred version |

|URL path|description|
|---|---|
|**file_browser**||
|*n*| nth version |

### Path part: asset version selection

Only valid in combination with **file**. Defaults to version "original".
This setting is ignored if the file is accessed directly through `id`.
There are two options:

|URL path|description|
|---|---|
|**file_version**||
|**name**||
|*name*| name of the version (depending on the asset type), for values see configuration in<br>*Administration* - *Base Configuration* - *Server-Config* under key *eas*.<br>standard values are:<br> for *Image*: **small, preview, preview_watermark, huge, full**<br>for *Video*: **small, preview, preview_watermark, huge, 360p, 720p, 1920p**<br>for *Audio*: **small, preview, preview_watermark, aac**<br>for *Office*: **small, preview, preview_watermark, pages**<br>for *Archive*: **small, preview, directory**|

|URL path|description|
|---|---|
|**file_version**||
|**group**||
|*name*| name of the version group, for values see configuration in<br>*Administration* - *Base Configuration* - *Server-Config* under key *eas*.<br>standard values are: **thumbnail, preview, huge** |

### Path part: format

This setting is only used for objects. The format of files is defined by the files themselves.

The default format is JSON.

|URL path|description|
|---|---|
|**format**||
|*format*| one of the following: **json, xml_easydb, xslt, csv**|
|*option*| only for format **xslt**: the stylesheet to apply|

### Path part: disposition

Sets the content disposition header. Defaults to:

- unset for objects
- "attachment" for files

|URL path|description|
|---|---|
|**disposition**||
|*value*| one of the following: **inline, attachment**|

## Query String

The query string specifies formatting, as well as the session used to access the object.

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.html), optional |
| `auth`  | System user that is used for retrieving information, optional. Possible values are: "deep_link" (default) and "oai_pmh" |

## Output

If **file** is provided, the output is a redirect to the requested file.

Else, the output is an [object](/technical/types/object/object.html) in the requested format.

## Permissions

The user (provided through `token` or `auth`) needs the "read" right for the requested object and the "mask" right for the given mask
(see [rights management](/technical/rightsmanagement/rightsmanagement.html)).

If the `token` is not provided, the following base config parameters are checked:

- **system.deep_link_access.enabled** is required for any operation
- **system.deep_link_access.allow_access_by_ids** is required when using the **id** object selection parameter
- **system.deep_link_access.allow_access_by_unique_columns** is required when using the **column** object selection parameter

## HTTP status codes

|   |   |
|---|---|
| 200 | Success, object |
| 302 | Success, redirect to file |
| 400 | [API error](/technical/errors/errors.html#api_error): something is malformed |
| 400 | [Object Not Found](/technical/errors/errors.html#object_not_found): object not found |
| 400 | [Objects Not Allowed](/technical/errors/errors.html#objects_not_allowed): the base configuration does not allow the operation: see "Permissions" |
| 500 | [Server error](/technical/errors/errors.html#server_error): internal server error |
