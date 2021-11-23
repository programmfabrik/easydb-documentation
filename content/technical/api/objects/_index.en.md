---
title: "67 - objects"
menu:
  main:
    name: "objects"
    identifier: "technical/api/objects"
    parent: "technical/api"
---
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

#### Object Selection by System Object ID

|URL path|description|
|---|---|
|**id**||
|*system\-object\-id*| `_system_object_id` of the object |

    GET /api/v1/objects/id/1

#### Object Selection by System Object UUID

|URL path|description|
|---|---|
|**uuid**||
|*uuid*| `_uuid` of the object |

    GET /api/v1/objects/uuid/12345678-abcd-1234-5678-abcdef123456

#### Object Selection by searching for an unique column value

|URL path|description|
|---|---|
|**column**||
|*objecttype*| objecttype of the object that is searched |
|*column*| name of the column used to search the object, it has to be unique |
|*value*| value to search for |

    GET /api/v1/objects/column/example_object/reference/ref123

### Path part: mask selection

If not specified, the object will be returned in the best mask.

|URL path|description|
|---|---|
|**mask**||
|*mask-name*| name of the mask to use |

    GET /api/v1/objects/id/1/mask/mask-name

    GET /api/v1/objects/uuid/12345678-abcd-1234-5678-abcdef123456/mask/mask-name

    GET /api/v1/objects/column/example_object/reference/ref123/mask/mask-name

### Path part: version selection

These parameters allow to ask for a specific version of the object. The object will be rendered in the schema version that was current when the object version was created. A mask specification is not possible and will be ignored.

The object is rendered in the `_all_fields` mask of the old version. This means the object will be rendered with all fields of the old schema version. This means especially, that old field names and types will be used. Schema changes since this object version was created will not be visible.

The version can only be requested in combination with `/api/v1/objects/id` and `/api/v1/objects/uuid`, it is not allowed for `/api/v1/objects/column`.

It is not possible to combine them:

#### Latest (current) version

|URL path|
|---|
|**latest**|

This is the default behaviour.

    GET /api/v1/objects/id/1/latest

    GET /api/v1/objects/uuid/12345678-abcd-1234-5678-abcdef123456/latest

    GET /api/v1/objects/column/example_object/reference/ref123/latest

will return the same object version as

    GET /api/v1/objects/id/1

    GET /api/v1/objects/uuid/12345678-abcd-1234-5678-abcdef123456

    GET /api/v1/objects/column/example_object/reference/ref123

#### A specific version by version number:

|URL path|description|
|---|---|
|**version**||
|*version*|version of the object|

    GET /api/v1/objects/id/1/version/1

    GET /api/v1/objects/uuid/12345678-abcd-1234-5678-abcdef123456/version/1

> **Note:** The version selection can not be combined with `/api/v1/objects/column/`!

#### A specific version by date:

|URL path|description|
|---|---|
|**date**||
|*date*| Date (+ time) in ISO 8601 format. Returns the latest version at the given time, accepted combinations of date and time are:<br>**date:** <ul><li>`YYYY`<li>`YYYY-MM`<li>`YYYY-MM-DD`</ul>**date + time:**<ul><li>`YYYY-MM-DD%20HH`<li>`YYYY-MM-DD%20HH:MM`<li>`YYYY-MM-DD%20HH:MM:SS`<li>`YYYY-MM-DD%20HH:MM:SSZ`<li>`YYYY-MM-DDTHH`<li>`YYYY-MM-DDTHH:MM`<li>`YYYY-MM-DDTHH:MM:SS`<li>`YYYY-MM-DDTHH:MM:SSZ`</ul> |

    GET /api/v1/objects/id/1/date/2018-12-10

    GET /api/v1/objects/uuid/12345678-abcd-1234-5678-abcdef123456/date/2018-12-10

> **Note:** The selection by date can not be combined with `/api/v1/objects/column/`!

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

> Note: This setting is ignored if the file is accessed directly through `id`.

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

> Note: This setting is ignored if the file is accessed directly through `id`.

There are two options:

|URL path|description|
|---|---|
|**file_version**||
|**name**||
|*name*| name of the version (depending on the asset type), for values see configuration in<br>[*Administration* - *Base Configuration* - *Server-Config* under key *eas*](/en/webfrontend/administration/base-config/export/#eas).<br>standard values are:<br> for *Image*: **small, preview, preview_watermark, huge, full**<br>for *Video*: **small, preview, preview_watermark, huge, 360p, 720p, 1920p**<br>for *Audio*: **small, preview, preview_watermark, aac**<br>for *Office*: **small, preview, preview_watermark, pages**<br>for *Archive*: **small, preview, directory**|

|URL path|description|
|---|---|
|**file_version**||
|**group**||
|*name*| name of the version group, for values see configuration in<br>[*Administration* - *Base Configuration* - *Server-Config* under key *eas*](/en/webfrontend/administration/base-config/export/#eas).<br>standard values are: **thumbnail, preview, huge** |

### Path part: format

This setting is only used for objects. The format of files is defined by the files themselves.

The default format is JSON.

|URL path|description|
|---|---|
|**format**||
|*format*| one of the following: **json, xml_easydb, xslt, csv**|
|*option*| only for format **xslt**: the stylesheet to apply (`<xslt-name>` as defined in the [*Administration* - *Base Configuration* - *Export, deep links and XSLT*](/en/webfrontend/administration/base-config/export/#xslt-formats)) |

    GET /api/v1/objects/id/1/format/json

    GET /api/v1/objects/id/1/format/xml_easydb

    GET /api/v1/objects/id/1/format/csv

    GET /api/v1/objects/id/1/format/xslt/<xslt-name>

#### Content-Type in Header for XSLT format

If a XSLT format is selected, the HTTP Header `Content-Type` is set depending on the content of the XSLT file. The attributes `"media-type"` and `"method"` of the `<xsl:ouput>` tag (see https://www.w3schools.com/xml/ref_xsl_el_output.asp) are analyzed to determine the best `Content-Type` for the response:

* if `"media-type"` is set:
    * use attribute value as is

* if `"media-type"` is not set:
    * check `"method"` to determine a fallback:
        * `"xml"`: `"text/xml"`
        * `"html"`: `"text/html"`
        * `"text"`: `"text/plain"`
        * `"name"`: `"text/plain"`
        * `"json"`: `"application/json; charset=utf-8"`

    * if method was none of the above:
        * use `"text/plain"`

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
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session), optional |
| `auth`  | System user that is used for retrieving information, optional. Possible values are: "deep_link" (default) and "oai_pmh" |

## Output

If **file** is provided, the output is a redirect to the requested file.

Else, the output is an [object](/en/technical/types/object) in the requested format.

## Permissions

The user (provided through `token` or `auth`) needs the "read" right for the requested object and the "mask" right for the given mask
(see [rights management](/en/technical/rightsmanagement)).

If the `token` is not provided, the following base config parameters are checked:

- **system.deep_link_access.enabled** is required for any operation
- **system.deep_link_access.allow_access_by_ids** is required when using the **id** object selection parameter
- **system.deep_link_access.allow_access_by_unique_columns** is required when using the **column** object selection parameter

## HTTP status codes

|   |   |
|---|---|
| 200 | Success, object |
| 302 | Success, redirect to file |
| 400 | [API error](/en/technical/errors): something is malformed |
| 400 | [Object Not Found](/en/technical/errors): object not found |
| 400 | [Objects Not Allowed](/en/technical/errors): the base configuration does not allow the operation: see "Permissions" |
| 500 | [Server error](/en/technical/errors): internal server error |
