# Insert an asset

    POST /api/v1/eas/put?token=<token>

Upload a new asset.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |
| `mapping` | use given metadata mapping to populate record with metadata from asset (optional, requires `mask`) |
| `mask` | mask to use when preparing record from metadata (optional, see `mapping`) |
| `objecttype` | object type to use if `mask` is `_all_fields` (optional, see `mask`) |
| `check_for_duplicates` | if set to "1" or "true", assets with the same checksum are returned in the `_duplicates` array |
| `skip_extension_check` | if set to "1" or "true", the check for file extensions is skipped |

## Input

The asset is provided in the request body (`multipart/form-data`).
The request is redirected to EAS [/api/v1/put](http://docs.easydb.de/latest-stable/system/eas/api/put/).

The name of form parameter containing the file does not matter, only a `filename` option in the enclosed `Content-Disposition` header is expected. One request must not contain more than one file upload form fields.

## Output

An array containing [Asset](/technical/types/asset/asset.md) objects is returned. For now there is exactly one object in response.

```js
[
  {
    "_id": 1000481951,
    "compiled": "png image, 300 x 90 @ 8 bit, 8.5 kB",
    "class": "image",
    "extension": "png",
    "class_extension": "image.png",
    "filesize": 8714,
    "technical_metadata": { … },
    "versions": { … }
  }
]
```

## Permissions

The user must be authenticated. The base config defines restrictions for asset upload:

- a global file size limit (optional)
- a file size limit per class (optional)
- a whitelist of allowed file extensions per class (except for the class "other")
- a flag "allow_all": when set, all extensions are allowed, regardless of the "extensions" list

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Session Not Found](/technical/errors/errors.md#session_not_found): session not found fot `token` |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Upload Limit Exceeded](/technical/errors/errors.md#upload_limit_exceeded): a file size limit has been exceeded |
| 400 | [Upload Type Not Allowed](/technical/errors/errors.md#upload_type_not_allowed): the file type is not allowed |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |





# Get asset information

    GET /api/v1/eas?token=<token>&ids=<ids>[&format={status|short|long}][&metadata_profile=<...>|&metadata_objecttype=<...>]

Get information available and accessible for an asset / several assets.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |
| `ids` | A JSON integer list containing the asset ids  |
| `format` | This arguments controls how much information is retrieved. It defaults to `long` |
| `mapping` | use given metadata mapping to populate record with metadata from asset (optional, requires `mask`) |
| `mask` | mask to use when preparing record from metadata (optional, see `mapping`) |
| `objecttype` | object type to use if `mask` is `_all_fields` (optional, see `mask`) |
| `check_for_duplicates` | if set to "1" or "true", assets with the same checksum are returned in the `_duplicates` array |

## Output

A JSON object containing entries for each requested ID. Each entry contains different data depending on the chosen format:

*All formats:*

| Property | Description |
|----------|-------------|
| `id` | The asset ID |
| `versions` | An object: `"<version>": { <version-information> }`. If the format is "status", only the status of each version is given |

*Short / Long:*

| Property | Description |
|----------|-------------|
| `compiled` | Information about the asset type and basic data as string |
| `class_extension` | String containing "\<asset-class\>.\<file-extension\>" |
| `original_filename` | Original filename (not present in "long" format!) |
| `zoomer` | Information needed to retrieve the zoomer version of this asset (object) |

*Only long:*

| Property | Description |
|----------|-------------|
| `asset_date` | Timestamp for asset date (string in ISO 8601 format) |
| `pages` | Number of pages (integer) |
| `metadata` | Metadata information (*) |

(*) Example of representation of metadata:

~~~~json
@@include:get.json@@
~~~~

## Permissions

If the asset is linked by a user object, the user must have the permissions required to see
that user object (see [GET /api/v1/db](/technical/api/db/db.md)).

If the asset is a user picture, the user must have the permissions required to see the
user picture (see [/api/v1/user](/technical/api/user/user.md). For versions other than "standard", the user
requires the permissions needed to update the user picture.

If the asset is a pool watermark, the user must have the "bag_read" right.
For versions other than "standard", the "bag_write" right is required.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Insufficient Rights](/technical/errors/errors.md#insufficient_rights): no "read" or "mask" right (the error parameters explain which) |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |





# Produce asset

    POST /api/v1/eas/produce?token=<token>

Produces a new asset based on a given one. This call can change the file format, as well as transform the
asset using rotations and cropping.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/technical/api/session/session.md) |

## Input

The input is a JSON object with the following attributes:

| Name            | Description                                                                       |
|-----------------|-----------------------------------------------------------------------------------|
| `eas_parent_id` | Asset parent ID (integer): ID of the asset that will be used to produce a new one |
| `description`   | Asset description ([l10n](/technical/types/l10n/l10n.md), optional): Description               |
| `format`        | Target format (string, optional). If omitted, the source format is kept           |
| `transform`     | Transformations (array of transformations, see below, optional): if given, transformations to be applied to `eas_parent_id` in the given order |

The transformations are defined as a JSON object with **one** of the following parameters:

| Name             | Description                                  |
|------------------|----------------------------------------------|
| `rotate-z`       | Z-Rotation (integer): 90,180,270 are allowed |
| `rotate-x`       | X-Rotation (integer): 180 is allowed         |
| `rotate-y`       | Y-Rotation (integer): 180 is allowed         |
| `crop`           | Crop (object)                                |
| &#8614; `top`    | Top position (integer): >= 0                 |
| &#8614; `left`   | Left position (integer): >= 0                |
| &#8614; `width`  | Width (integer): >= 1                        |
| &#8614; `height` | Height (integer): >= 1                       |

## Output

The response of a status request (`GET /api/v1/eas&format={status}`) for the new asset.

## Permissions

The same restrictions apply as for GET /api/v1/eas, referring in this case to the `eas_parent_id`.

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | [API error](/technical/errors/errors.md#api_error): something is malformed |
| 400 | [Not Authenticated](/technical/errors/errors.md#not_authenticated): session is not authenticated |
| 400 | [Asset Not Found](/technical/errors/errors.md#asset_not_found): asset `eas_parent_id` not found |
| 400 | [Insufficient Rights](/technical/errors/errors.md#insufficient_rights): no "read" or "mask" right (the error parameters explain which) |
| 500 | [Server error](/technical/errors/errors.md#server_error): internal server error |
