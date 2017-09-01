# Export

This class defines an export job. Exports are user-bound (see [/api/export](/technical/api/export/export.md)).

An export defines:

- which data to export:
    - the data to export is based on a search, which is executed under the rights of the user (`search`)
    - it is possible to configure export options field by field (`fields`)
    - the assets to export are provided by field name (`eas_fields`)
    - if given, the preferred asset version is exported (unless stated otherwise in `assets`)
    - with each asset exported, a relative path is included in the CSV or XML export files
    - it is possible to configure export options by file class (`classes`) or even for specific assets (`assets`)
- how to map and present the data:
    - the data can be provided as CSV (`csv`) and/or XML (`xml`, `xml_one_file_per_object`)
    - it is possible to specify a specific mapping profile (`mapping`)
- when it should be launched
    - the export can be scheduled to run periodically using [schedules](/technical/types/schedule/schedule.md) (`_schedules`)
    - if no schedules are set, the export is launched immediately
- the transport mechanisms used to transport the export data (`_transports`)
    - if no transports are defined, the export is only available for download

The export is also used to track the job's progress:

- the attribute `_state` is used to know the current state of an export/transport

Finally, the export also provides information about the generated files and downloads:

- a list of generated files (`_files`) is provided, including their relative paths and sizes
- a list of available downloads (`_downloads`) is provided, including the URLs used to download the export

## Detailed information

Exports are stored on the server in their separate directories.
Exports can contain folders and files, depending on the export definition.
Exports are transported by the user using transport definitions.

After each sucessful Export an event is created (/api/event).

**Lifecycle**

The Export lifecycle looks as follows:

1. Inform frontends using /api/event about the starting Export
1. Log in the User of the Export, use the rights of that User
1. Create a unique Export directory, in case of an update, wipe the existing one
1. Execute the search of the Export
1. Collect all Objects and the corresponding files (Assets)
1. Copy all files into the Export filestructure
1. Link files to the Object Information (relative local URLs to the exported files)
1. Write XML and CSV files to the Export directory
1. Start all defined transports to send emails and copy files
1. Inform frontends using /api/event about the finished Export

## Attributes

| Name                        | Description                                                                                               |
|-----------------------------|-----------------------------------------------------------------------------------------------------------|
| `_basetype`                 | Name of the base type (string, r): **export**                                                             |
| `_date_created`             | Timestamp when this export was created ([timestamp](/technical/types/timestamp/timestamp.md), r)                            |
| `_state`                    | State of the export (string, r): see [state](#state) for a list of possible values                        |
| `_schedules`                | Configure when to launch the export (array of [schedules](/technical/types/schedule/schedule.md), rw, optional, nullable)  |
|                             | - if not set or set to *null*, the export is executed as soon as possible                                 |
| `_transports`               | Transports defined for this export (array of [transport export attributes](#transport), rw, optional)     |
| `_log`                      | Export log (array of [log events](/technical/types/event/event.md), r), possible types:                                 |
|                             | - **EXPORT_INSERT**: export is created                                                                    |
|                             | - **EXPORT_START**: export is started                                                                     |
|                             | - **EXPORT_FINISH**: export is finished                                                                   |
|                             | - **EXPORT_FAILED**: export aborted due to an error                                                       |
|                             | - **EXPORT_STOPPED**: export aborted by user                                                              |
| `_files`                    | List of files created in this export (array of [files](#file), r)                                         |
| `export`                    | Export attributes:                                                                                        |
| &#8614; `_id`               | Export ID (integer, unique, r)                                                                            |
| &#8614; `_version`          | Export version (integer, rw)                                                                              |
| &#8614; `type`              | Type of export (string, rw, optional, defaults to `export`). Allowed values are `export`, `export_incremental` and `download`. |
| &#8614; `name`              | Export name (string, rw, optional): required if `_schedules` is set; defaults to "easydb-\<type\>-\<\_id\>" |
| &#8614; `search`            | The [search definition](/technical/api/search/search.md) to find the objects (json, rw)                                  |
| &#8614; `fields`            | Export configuration for specific fields. Map keys are the field names, map values are described in [field export attributes](#field_attr), rw, optional, nullable) |
|                             | If set, only export the given fields. Otherwise, export all fields with standard configuration            |
| &#8614; `eas_fields`        | Export configuration for EAS fields. Map keys are the field names, map values are described in [EAS field export attributes](#eas_field_attr)(rw, optional, nullable)) |
| 		  					  | If unset, or set to *null* or empty map no files will be exported. |
| &#8614; `classes`           | Version attributes for each file class (map "\<class\>": Array of [version export attributes](#version_attr), rw, optional) |
|                             | \<class\> is one of *image*, *audio*, *video*, *office*, or *other*                                       |
| &#8614; `assets`            | Specific asset configuration (map: "\<asset\_id\>": \<value\>, rw, optional) - \<value\> can be: |
|                             | - **true**: the corresponding Class Export Attributes are used to export this asset. This can be used to explicitly export a non-preferred version of an asset |
|                             | - **false**: this asset will not be included in the export. This can be used to not export preferred versions of an asset |
|                             | - [asset export attribute](#asset_export_attr). This can be used to explicitly export a non-preferred version of an asset |
| &#8614; `csv`               | CSV output configuration (rw, optional) - its value can be: |
|                             | - **false**: don't include the object data as CSV (default value) |
|                             | - [CVS export attributes](#csv_attr): CSV attributes |
| &#8614; `xml`               | Include the data as XML (boolean, rw, optional): defaults to **false** |
| &#8614; `xml_one_file_per_object` | Generate one XML file per object (boolean, rw, optional): defaults to **false** |
| &#8614; `json`              | Include data as JSON (boolean, rw, optional): defaults to **false** |
| &#8614; `json_one_file_per_object` | Generate one JSON file per object (boolean, rw, optional): defaults to **false** |
| &#8614; `xslt_xml_post_processing`        ||
| &#8614;&#8614; `_id`        | Asset ID to fetch XSLT stylesheet. Expected is an asset of mime type `text/xsl` which is used to post-process the generated XML files. |
| &#8614; `mapping`           | Mapping profile used to process the XML and CSV (string, rw, optional): defaults to the standard mapping "easydb", "easydb" generates a hierarchical standard XML according to the objecttype definition (filtered by the mask), "easydb_flat" generates a flattened standard XML according to the objecttype definition (filtered by the mask). |
| &#8614; `batch_size`        | Export-specific batch size (integer, rw, optional). If unset, system-wide configuration is used. **0** indicates unlimited batch size, positive integers may be used to set the batch size. |
| &#8614; `filename_original` | Use original filename (boolean, rw, optional). If set to **true**, the original filename base is used for exported assets. |
| &#8614; `filename_template` | Filename template (string, rw, optional). If a string is supplied, it is used as filename base template for the exported assets. The string may contain variables as in [per-objecttype filenames](../objecttype/objecttype.md#export_asset_filenames). (*`filename_original=true` and `filename_template="..."` can't be set at the same time*) |
| &#8614; `produce_options`   | Options to be passed to export produce plugins (object, rw, optional). |
| &#8614; `flat`              | If set, no directory structure is used for exported files (boolean, rw, optional, defaults to **false**) |

\* Fields are provided in the ES format (the one used by /api/search)

### <a name="field_attr"></a>Field Export Attributes

The field export attributes is a JSON object with the following optional arguments.

| Parameter         | Value        |   Description   |
|-------------------|--------------|------------------|
| `display_name`    | String       | If set, replace the name of the field by this value in the export CSV and XML. |



### <a name="eas_field_attr"></a>EAS Field Export Attributes

The field export attributes is a JSON object with the following optional arguments. Some of them are only meaningful for certain EAS fields:

| Parameter         | Value        |   Description   |
|-------------------|--------------|-------------------|
| `display_name`    | String       | If set, replace the name of the field by this value in the export CSV and XML. |
| `files`			| Boolean	   | If set, copy or produce export files for the assets found in the search result. |
| `data`			| Array	of Maps| One element for each version. |
| &#8614; `type` | *"original"*   | Export Link to the original. |
|                | *"current"*   | Link to the current original. |
|                | *"version"*   | Link to a given version. |
| &#8614; `format` | *"long"*   | A more verbose format is used for export the URL and accompanying data. |
|                | *"short"*   | A less verbose format is used for export the URL and accompanying data. |


#### type "version"

| Parameter         | Value             |   Description   |
|-------------------|-------------------|-----------------|
| `version`  | *"\<class\>.\<version_name\>"*  | Selects the given *\<version_name\>* in class *\<class\>* to export.|


### <a name="asset_export_attr"></a>Asset Export Attributes

| Parameter         | Value             |   Description   |
|-------------------|-------------------|-----------------|
| `versions`        | Array of [version export attributes](#version_attr) | Version export information for the asset. |
| `eas_parent_id`   | Integer | For temporarily produced version, the link to the parent EAS id. |
| `json`            | Boolean | If set, per-export `json` option is overridden for this asset. If there are multiple assets per object, JSON output is enabled if at least one asset has `json` set to `true`.|



### <a name="version_attr"></a>Version Export Attributes

The version export attributes is a JSON object with the following optional arguments. Some of them are only meaningful for certain asset classes:

| Parameter         | Value             | Classes        |   Description   |
|-------------------|-------------------|----------------| -----------------|
| `type` | *"original"*       | All     | Selects the original. |
|        | *"current"*       | All      | Selects the current original, that is the rotateted version. |
|        | *"version"*       | All      | Selects a version of the current original. |
|        | *"custom"*        | All      | Produces a custom version of the current original. |
| `metadata` | *"standard"*        | *image*,*audio*,*video* |  The selection for the metadata mapping is used from the Pool or Objecttype setting. If `metadata` is unset, *"standard"* is assumed.|
|  			| *"keep"*          | *image*,*audio*,*video*  |  The metadata is kept as it is. It is possible that elsewhere versions already got a Metatda-Profile written.  |
|           | *"remove"*        | *image*,*audio*,*video*  |  The metadata is removed. |
|           | *\<profile-id\>*   | *image*,*audio*,*video*  |  The metadata is mapped using the Profile with id *\<profile-id\>*. |

#### type "version"

| Parameter         | Value             | Classes        |   Description   |
|-------------------|-------------------|----------------| -----------------|
| `version`  | *"\<version_name\>"*  | All        | Selects the given *\<version_name\>* to export. Available version names depend on the class.|

#### type "custom"


| Parameter         | Value             | Classes        |   Description   |
|-------------------|-------------------|----------------| -----------------|
| `custom`          |                   |                |                  |
| &#8614; `watermark`    |  Boolean         | *image*   | *true* produces a custom version including a watermark, this works only if `version` is *unset*, *false* does not include a watermark. |
| &#8614; `format`  | *"keep"*          | *image*   |  The format of the image is unchanged to its *current* version format.|
|           | *"jpeg"*          | *image*   |  The format of the produced image will be JPEG. |
|           | *"tiff"*          | *image*   |  The format of the produced image will be TIFF. |
|           | *"png"*          | *image*   |  The format of the produced image will be PNG. |
|           | *"bmp"*          | *image*   |  The format of the produced image will be BMP. |
| &#8614; `jpeg_quality`    | *"maximum"*<br/>*"medium"*<br/>*"small"*    | *image*   |  The quality of the JPEG, if format is JPEG. |
| &#8614; `colorspace`    | *"keep"*<br/>*"rgb"*<br/>*"cmyk"*<br/>*"gray"*    | *image*   |  The colorspace of the image. |
| &#8614; `size`    | *"keep"*     | *image*   |  The size of the produced version is the same as the *current* version (unchanged). |
|           | *"custom"*   | *image*   | The size of the produced version is given by the `custom_size` parameters. |
| &#8614; `custom_size` | *"dimension_max"*  | *image* | The size of the long edge is set by `custom_size_pixel`. |
|               | *"dimension_min"*  | *image* | The size of the short edge is set by `custom_size_pixel`. |
|               | *"width"* | *image* | The width is set by `custom_size_pixel`. |
|               | *"height"* | *image* | The height is set by `custom_size_pixel`. |
| &#8614; `custom_size_pixel` | Integer    | *image* | The size of the `custom_size` value in pixels. |
| &#8614; `transform` | Array of transformation Info | *image*  | See in /eas/produce for more information. This parameter is allowed only when used in *assets*. |



### <a name="field_attr"></a>Field Export Attributes

Array of [version export attributes](#version_attr): version attributes for the asset.



### <a name="csv_attr"></a> CSV Export Attributes

The CSV Export always includes a header with the field names. Values can include Newlines.

| Parameter         | Value        |   Description   |
|-------------------|--------------|-----------------|
| `delimiter`       | Char         | Use this character as the delimiter between columns. |
| `quote`           | Char         | Use this character to quote values. Values are always quoted, even if they wouldn't have to be quoted. |
| `escape`          | Char         | Use this character to escape the quote character within values. |
| `use_bom`         | Boolean      | Use byte-order mark in file. `false` if not set. |

### <a name="transport"></a> Transport Export Attributes

A Transport is used to send exports after they are finished.

| Parameter    | Description |
|--------------|-------------|
| `type`       | Transport type (string, rw): currently **email**, **rsync** and **download** are supported |
| `packer`     | Packer to be used (string, rw, optional): defaults to **null** |
|              | - **"zip"**: ZIP archive, unlimited size |
|              | - **"zip_10mb"**: ZIP archive(s), 10 MB limit per file (_see below_) |
|              | - **"zip_2gb"**: ZIP archive(s), 2 GB limit per file (_see below_) |
|              | - **"tar_bz2"**: TAR archive using BZip2 compression |
|              | _size limits are not very reliable and should be taken as a hint only:_ |
|              | - splitting is done by input file size, compression or archiving overhead is ignored, archives can be smaller or even larger than input files |
|              | - single files greater than size limit are not splitted, resulting archive file is larger than given size limit |
| `email`      | Configuration for sending e-mails (object, rw): |
| &#8614; `recipients` | Array of recipients, which can be [user(short)](/technical/types/user/user.md#short), [group(short)](/technical/types/group/group.md#short) or an ad-hoc user based on an e-mail |
| &#8614; `message` | Optional message to attach to the standard e-mail text |
| `_state`     | State of the transport (string, r): see [state](#state) for a list of possible values |
| `_download`  | Available download ([download](#download), r)                                          |
| `options`    | Transport attributes (object, rw, optional): depending on the type, additional attributes can be configured; see below |

Ad-hoc users are provided as in [/api/collection](/technical/api/collection/collection.md).

**Transport type "download"**

This type of transport has no attributes, a list of downloads will be available in the read-only attribute `_download`.

**Transport type "rsync"**

RSYNC can be used to copy files away from the Export directory to a backup directory or a remote server using the SSH, RSH, or RSYNC as transport protocol.

| Parameter     | Description |
|---------------|-------------|
| `destination` | The rsync destination (string) |
| `options`     | Additional rsync options (object, optional) |

### <a name="file"></a> File

For each file, the following attributes are provided:

| Value  | Description |
|--------|-------------|
| `path` | Relative path of the file (string) |
| `size` | File size, in bytes (integer) |
| `eas_id` | Asset ID of file (integer, optional) |
| `eas_version` | Asset version of file (string, optional) |
| `eas_fileclass` | Asset file class of file (string, optional) |

### <a name="download"></a> Download

For each download, the following attributes are provided:

| Parameter      | Description |
|----------------|-------------|
| `_files`       | List of files, **zip32** has a 2GB filesize limit which might yield to multiple files for the donwload |
| &#8614; `url`  | Relative URL of the file, starting with a *Secret-Passkey* for direct access to the file (string) |
| &#8614; `size` | If available, the size of the download (integer, optional) |

> The *url* is persistent for the lifetime of the export's transport. So that after a scheduled update of the export, the URL does not change.

### <a name="state"></a> State

These values are always possible for `_state`:

| Value          | Description |
|----------------|-------------|
| *new*          | Created, not processed |
| *pending*      | Export has been started but is not processed, yet |
| *processing* 	 | In progress |
| *failed*       | Failed |
| *done*         | Completed without errors |

## Related operations

- [/export](/technical/api/export/export.md): CRUD operations on exports

## Example

```json
[include](./export.example.json)
```

**Note:** `state` has been implemented as `_state` directly in export and transport.

