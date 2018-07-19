---
title: "121 - Asset"
menu:
  main:
    name: "Asset"
    identifier: "technical/types/asset"
    parent: "technical/types"
---
# Asset

Assets are uploaded to the EAS using one of the following calls:

- [POST /api/eas/put](/en/technical/api/eas): upload a file
- [POST /api/eas/produce](/en/technical/api/eas): produce an asset based on another one (setting `eas_parent_id` accordingly)

These calls return an asset record. The asset record is linked to an object using
[POST /api/db]. The call must provide the asset `_id` and can also set or update the fields
marked as writable in the table below.

## Attributes

| Name                        | Description                                                                                               | Search       |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|--------------|
| `_id`                       | Asset ID (integer, unique for an EAS, rw)                                                                 | Number       |
| `eas_parent_id`             | Asset ID of this asset's "parent" (integer, rw): the client can override this value                       |              |
| `preferred`                 | Whether this is the preferred version (boolean, rw) (\*)                                                  | Boolean      |
| `name`                      | Name for the asset (string, rw)                                                                           |              |
| `class_extension`           | Asset class and extension, separated by a point (string, r): for example, "image.jpg"                     | String       |
| `compiled`                  | Compiled information about the asset (string, r)´: for example, "jpg image, 800 x 600 @ 24 bit, 154.8 kB" |              |
| `original_filename`         | Original filename (string, r)                                                                             | String (\*)  |
| `upload_date`               | Upload date (timestamp, r)                                                                                | Timestamp    |
| `upload_user`               | User that uploaded this asset ([user (short)](/en/technical/types/user), r)                                 | Number (\*)  |
| `insert_date`               | When this asset was linked with its object (timestamp, r)                                                 | Timestamp    |
| `filesize`                  | File size, in bytes (integer, r)                                                                          | Number       |
| `technical_metadata`        | Technical metadata (based on the original version)                                                        |              |
| &#8614; `width`             | Width, in pixels (integer, r) - for class "image"                                                         | Number       |
| &#8614; `height`            | Height, in pixels (integer, r) - for class "image"                                                        | Number       |
| &#8614; `max_dimension`     | Max dimension (width or height), in pixels (integer, r) - for class "image"                               | Number       |
| &#8614; `format`            | Image format (string, r): "landscape", "square" or "portrait" - for class "image"                         | NotAnalyzed  |
| &#8614; `dpi`               | DPI (integer, r) - for class "image"                                                                      | Number       |
| &#8614; `aspect_ratio`      | Aspect ratio (width/height) (decimal, r) - for class "image"                                              | Number       |
| &#8614; `camera_scanner`    | Camera/Scanner model (string, r) - for class "image"                                                      | String       |
| &#8614; `colordepth`        | Color depth (integer, r) - for class "image"                                                              | Number       |
| &#8614; `colorprofile`      | Color profile name (string, r) - for class "image"                                                        | String       |
| &#8614; `colorspace`        | Color space (string, r) - for class "image"                                                               | NotAnalzed   |
| &#8614; `duration`          | Duration, in seconds (integer, r) - for classes "audio" and "video"                                       | Number       |
| &#8614; `audio_codec`       | Audio codec (string, r) - for classes "audio" and "video"                                                 | NotAnalyzed  |
| &#8614; `video_codec`       | Video codec (string, r) - for class "video"                                                               | NotAnalyzed  |
| &#8614; `pages`             | Number of pages (integer, r) - for class "office"                                                         | Number       |
| `versions`                  | Information about the versions of this asset ([versions](#versions), r)                                   |         |
| `_duplicates`               | List of [duplicate](#duplicate) assets (\*)                                                               |         |

(\*) `preferred` is only present in [Objects](/en/technical/types/object), where the assets are stored as an array. It marks the preferred version.
(\*) `upload_user.user._id` is searchable as Number
(\*) `original_filename` is searchable in "all" if the field is marked as fulltext in the mask.
(\*) `_duplicates` is only present in [POST /api/eas/put and GET /api/eas](/en/technical/api/eas) if `check_for_duplicates` is requested.

*The following fields are not implemented yet:*

| Name                        | Description                                                                                               | Search       |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|--------------|
| `create_date`               | When this asset was created (timestamp, r)                                                                | Timestamp    |
| `modified_date`             | When this asset was modified (timestamp, r)                                                               | Timestamp    |
| `camera`                    | Camera (string, r)                                                                                        | String       |

### <a name="versions"></a> Versions

Versions are specified as a map. The EAS rights management configuration specifies which versions are visible:

- if the asset is linked to an object, the versions are filtered by their asset rights
- if the asset is not linked to an object, all known versions are visible

For each version, there is an attribute with the following properties (read-only):

| Name                        | Description |
|-----------------------------|-------------|
| `status`                    | Processing status (string): **pending**, **processing** or **done** |
| `filesize`                  | File size, in bytes (integer) |
| `height`                    | Height, in pixels (integer) |
| `width`                     | Width, in pixels (integer) |
| `class`                     | File class (string) |
| `extension`                 | File extension (string) |
| `url`                       | URL (string) |
| `zoom_url`                  | Zoom URL (string) |

### <a name="duplicate"></a> duplicate

Each duplicate is a map with the following properties:

| Name                        | Description |
|-----------------------------|-------------|
| `_id`                       | Asset ID    |
| `certainty`                 | currently always `1.0` |
| `linked_system_objects`     | list of objects linking this asset, currently at most one object |
| &#8614; `_system_object_id` | system object ID of linking object |
| &#8614; `_column_id`        | ID of column the asset is linked from |

