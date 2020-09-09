---
title: "73 - search"
menu:
  main:
    name: "search"
    identifier: "technical/api/search"
    parent: "technical/api"
---

# Search

    POST /api/v1/search?token=<token>

Search user objects and base objects.

## Query String

|   |   |
|---|---|
| `token` | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `pretty` | Set if resulting JSON output is prettified. Defaults to "1" (enabled). |

## Input

The input is provided as a JSON object with the following attributes:

| Name                  | Description                                                                     |
|-----------------------|---------------------------------------------------------------------------------|
| `type`                | Type of element to search (string, optional): see below, defaults to **object** |
| `objecttypes`         | Object types to search (array of strings, optional): only for search type "objects" (ref [schema-table](/en/technical/types/schema).name), defaults to all |
| `search`              | Search elements (see below, optional)                                           |
| `offset`              | Start index (integer, optional): defaults to 0                                  |
| `best_mask_filter`    | Return at max only one object per objecttype,	rendered in for the user best available mask (boolean, optional): defaults to `true` |
| `generate_rights`     | Generate the rights that the user has for the result objects (boolean, optional): defaults to `true`, only for types with `_generated_rigths` |
| `limit`               | Maximum number of elements to return (integer, optional). Maximum and default: [`elasticsearch/max_limit`](/en/sysadmin/configuration/easydb-server.yml/#base) (`1000`) |
| `format`              | Format for the objects (string, optional): only for `type` **object**, see allowed values under "Output: format", defaults to **long** |
| `language`            | Language used for standard rendering and as default for sorting and aggregating (string, optional): defaults to: |
|                       | - the first search language of the user, if `type` is **object** |
|                       | - the frontend language of the user, if `type` is not **object** |
| `sort`                | Sort elements (array of sorting defintions, optional): see [Sorting](#sort)     |
| `aggregations`        | Aggregation element (map of aggregation definitions, optional): see [Aggregations](#aggregations)     |
| `highlight`           | Highlight specification (highlight defintion, optional): see [Highlighting](#highlight) |
| `fields`              | Fields specification (fields definition, optional): see [Fields](#fields) |
| `include_fields`      | The only fields to be included in the output (array of fields, optional): see [notes](#includeexclude), [field names](#fieldnames) |
| `exclude_fields`      | Fields to be excluded from the output (array of fields, optional): see [notes](#includeexclude), [field names](#fieldnames) |

The parameters `offset` and `limit` can be used to scroll through large amount of results. Use the response
attribute `count` to control the total number of hits. `limit` can also be set to 0 if only aggregations are needed.

`best_mask_filter` is only meaningful for search type "object". It prevents retrieving duplicate objects rendered in different masks.

- the corresponding base config variable (system.log.search, system.log.detail) is set to `true`

<a name="includeexclude"></a>

The option `exclude_fields` exclude parts of the output.

The option `include_fields` include object's fields to the output and it is processed after `exclude_fields`. Excluded fields could be returned if they are present in `include_fields`.

The `format` as described [below](#format) is the basis for the field list. It predefines the list of fields returned, which can be further refined with `exclude_fields` and `include_fields`. There is no guarantee that all fields in `exclude_fields` are actually missing. If a fields is required for internal use (e.g. `_id`) it may be returned anyway.

### Search type

The following search types are supported:

- **object** (default): search user-defined objects (see [object](/en/technical/types/object)) with `read` and `mask`
- **pool**: search [pools](/en/technical/types/pool) with `bag_read`
- **pool_management**: search [pools](/en/technical/types/pool) with `bag_write`
- **collection**: search collections (see [collection](/en/technical/types/collection))
- **message**: search messages (see [message](/en/technical/types/message))
- **user**: search users (see [user](/en/technical/types/user)) with `read` and type "easydb", "system" or "email"
- **group**: search groups (see [group](/en/technical/types/group)) with `bag_read`
- **acl**: search users and groups simultaneously

### Search elements

The search elements act like filters over the search. The parameter "bool" determines if the
search element has to be true ("must") or false ("must_not") for an object to be found.
If there are several search elements marked as "should" it means that at least one of them must
apply for an object to be found.

If no search elements are given, all elements of the given type(s) are returned.

The common parameters for a search element are:

| Parameter | Value |
|-----------|-------|
| `type`    | one of the search types described below (string) |
| `bool`    | how this search element is considered (string, optional): **must** (default), **must_not** or **should**  |
| `boost`   | increase the relative weight of the search element. A higher boost values results in a higher `_score` for objects matching the clause. (float, optional).  Default: 1.

#### Example:

{{< include_json "./example1.json" >}}

Example using boost:

Objects matching "house" will have a higher `_score` than those matching "appartment".

{{< include_json "./example2.json" >}}

#### search element "match"

This search element allows to match a given text. It can be used with all search types. Match ignores
case and diacritical marks, and detects some writing variants. For instance, "fusse" will match "Füße".

| Parameter   | Value |
|-------------|-------|
| `mode`      | search mode (string, optional): **fulltext** (default), **token** or **wildcard** |
| `string`    | text to match (string). Maximal length: 256 charcaters [(\*)](#f1) |
| `fields`    | fields to match against (array of fully qualified field names, optional): defaults to all. See [Field Names](#fieldnames) |
| `languages` | languages to match against (array of strings, optional): defaults to all search languages of the user |
| `phrase`    | phrase search (boolean, optional): defaults to `false` |

This search element can only be applied to Text, String and L10n fields. The `languages`
restrict the languages L10n fields are searched for.  If no `fields` parameter is set, every searchable field
of the required types will be considered.

The search mode "token" matches whole words, whereas "fulltext" matches parts of words. Notice that
Text and L10n fields only match words beginning with a particular token. String fields will also match inside the text.
The "wildcard" mode allows to specify `*` and `?` wildcards to match the text in more complex forms. This kind of search
is slower though, especially when using `*` at the beginning.

For String fields, the `string` is matched against the whole field.

For Text and L10n fields, the `string` is divided into words and then matched against the words contained in the field.
If `phrase` is set to `true`, the words must be found in the same order as given, and may not include other words in between.
`phrase` is ignored when using wildcards.

##### Examples:

{{< include_json "./match1.json" >}}

#### search element "in"

Search for specific values in one or more fields.

| Parameter      | Value |
|----------------|-------|
| `in`           | values (array of `<type>`): `<type>` depends on field type. For `<type>` text/string: maximal length: 256 charcaters [(\*)](#f1) |
| `fields`       | fields to consider for the search (array of fully qualified field names).  See [Field Names](#fieldnames) |
| `objecttype`   | objecttype (string): name of a linked objecttype or `_pool` |
| `include_path` | include all objects in the path (boolean, optional, defaults to `false`): only with `objecttype` (see below) |
| `eas_field`    | EAS field (string) |
| `languages`    | languages to use (array of strings, optional): defaults to all search languages of the user |

One of `fields`, `objecttype` or `eas_field` has to be provided.

If a single field is given, the type of `in` will depend on the field type. Allowed types are:

| class      | field type                                        | value type (JSON)            |
|------------|---------------------------------------------------|------------------------------|
| `number`   | Number, Id                                        | `integer`, `decimal`, `null` |
| `boolean`  | Boolean                                           | `boolean`, `null`            |
| `text`     | Text, String, L10n **[(\*\*)](#f2)**, NotAnalyzed | `string`, `null`             |
| `nullable` | Nullable, Nested, Date, Datetime                  | `null`                       |

Notice that `null` is always allowed, in order to be able to search entries with no value.

If more than one field are given, all of them must be of the same class.
A [dis_max query](http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/query-dsl-dis-max-query.html)
is used.

If `objecttype` is used, all fields linking to an element of that objecttype are considered. The special
name `_pool` is used to search in all pool fields. The value type of `in` will be a number and it represents
the ID of that objecttype / pool.

If `objecttype` is used, the attribute `include_path` can be used to search also by the objects contained in the path.
This has no effect on non hierarchical objecttypes, but it can be used for them, too.

If `eas_field` is used, all assets linked by the object considered. The `eas_field` is the asset field searched
(for example: `"class"`), and `in` contains the values (for example `"image"` and `"video"`).

**<a name=f1>(\*)</a>** All text and string values are truncated at 256 characters in elasticsearch. Every text and string input value that is longer than 256 characters will cause an UserError (`error.user.search_query_too_long`).

**<a name=f2>(\*\*)</a>** L10n fields will be expanded to the given languages.

##### Examples:

{{< include_json "./in.json" >}}

#### search element "range"

This search element allows to match numeric (Number, Id), date/time (Date, Timestamp) or string (String) fields using a range.

| Parameter | Value |
|-----------|-------|
| `field`   | field to consider for the search (string): fully qualified field name |
| `from`    | lower end of the range (number/string, optional): inclusive |
| `to`      | upper end of the range (number/string, optional): inclusive |

Dates are given in ISO 8601 format. Both `from` or `to` or one of them must be given.

#### Example:

{{< include_json "./range.json" >}}

#### search element "changelog_range"

This is a special search element that allows to search for a objects that were changed by a specific user in a given period of time.

| Parameter   | Value |
|-------------|-------|
| `user`      | ID of the user (integer, optional) |
| `operation` | Changelog operaion (string, optional): **insert**, **update** or empty/null |
| `from`      | lower end of the range (number/string, optional): inclusive |
| `to`        | upper end of the range (number/string, optional): inclusive |
| `comment`   | text in user's comments (string, optional) |

Dates are given in ISO 8601 format, in UTC, and may be provided as a date prefix. Both `from` or `to` or one of them must be given.

#### search element "nested"

This search element allows to retreive documents that match against a query for their
nested documents. It is like a complex search that is performed at a certain path inside
the main object type and returns objects from the main object type, but is run against the
nested object type.

| Parameter | Value |
|-----------|-------|
| `path`    | path to a field of nested elements (string): the field must be of type Nested |
| `search`  | search elements for the sub-query (array of search elements) |

#### Example:

{{< include_json "./nested.json" >}}

#### search element "complex"

This search element allows to specify more complex search expressions by nesting
them in the global search. The normal search already allows some combinations,
like "A or B or C":

#### Example:

{{< include_json "./complex1.json" >}}

But other combinations are not covered, like "(A and B) or C". For that, you can
use the "complex" search type:

| Parameter | Value |
|-----------|------ |
| `search`  | array of search elements |

#### Example:

{{< include_json "./complex2.json" >}}

#### <a name="fieldnames"></a> Field names

##### Name of generic fields used for searching and sorting.

| Top level object | Format |
|---|---|
| `_objecttype` | string |
| `_mask` | number |
| `_tags._id` | number |
| `_collections._id` | number |
| `_owner.user._id` | number |
| `_owner.group._id` | number |
| `_linked._asset._id` | number |
| `_linked._asset.class` | string |
| `_linked._asset.extension` | string |
| `_linked._asset.filesize` | number |
| `_linked._asset.class_extension` | string |
| `_linked._asset.class_version_status` | string |
| `_linked._asset.class_version_extension` | string |
| `_linked._asset.class_version_filesize` | string |
| `_linked._asset.name` | string |
| `_linked._asset.date_uploaded` | timestamp |
| `_linked._asset.date_inserted` | timestamp |
| `_linked._asset.date_created` | timestamp |
| `_linked._asset.upload_user.user._id` | number |
| `_linked._asset.technical_metadata.camera_scanner` | string |
| `_linked._asset.technical_metadata.colorprofile` | string |

| Changelog | Format |
|---|---|
| `_changelog.date_create` | timestamp |
| `_changelog.date_last_updated` | timestamp |
| `_changelog.user_created` | number |
| `_changelog.user_last_updated` | number |
| `_changelog.comment` | string |
| `_last_modified` | timestamp |

| EAS column | Format |
|---|---|
| `_id` | number |
| `original_filename` | string |
| `original_filename_basename` | string |
| `class` | string |
| `extension` | string |
| `filesize` | number |
| `class_extension` | string |
| `class_version_status` | string |
| `class_version_extension` | string |
| `class_version_filesize` | string |
| `name` | string |
| `date_uploaded` | timestamp |
| `date_inserted` | timestamp |
| `date_created` | timestamp |
| `upload_user.user._id` | number |
| `technical_metadata.width` | number |
| `technical_metadata.height` | number |
| `technical_metadata.max_dimension` | number |
| `technical_metadata.aspect_ratio` | number |
| `technical_metadata.format` | string |
| `technical_metadata.duration` | number |
| `technical_metadata.pages` | number |
| `technical_metadata.colordepth` | number |
| `technical_metadata.colorspace` | string |
| `technical_metadata.audio_codec` | string |
| `technical_metadata.video_codec` | string |
| `technical_metadata.camera_scanner` | string |
| `technical_metadata.colorprofile` | string |

| Main tables | Format |
|---|---|
| `_global_object_id` | number |
| `_system_object_id` | number |
| `_uuid` | number |
| `_standard.1.text` | string |
| `_standard.2.text` | string |
| `_standard.3.text` | string |

| Hierarchical linked tables | Format |
|---|---|
| `_path.**object` | `type**._id` | number |
| `_level` | number |
| `_has_children` | `bool` |
| `_path._global_object_id` | number |

| Linked tables at top level | Format |
|---|---|
| `[object_type_name]._pool.pool._id` | number |
| `[object_type_name]._pool.pool.name` | string |
| `[object_type_name]._pool._level` | number |
| `[object_type_name]._pool._path.pool._id` | number |

##### Object fields

| Top level fields						|
|-----------------------------------|
| `[object_type_name].[field_name]`	|
| Example: `people.name`				|

| Fields in nested top level field					|
|-----------------------------------------------------------------------|
| `[object_type_name].__nested:[object_type_name]__[nested_field_name].[nested_field_field_name]` - Example: `people.__nested:people__cars.brand` |

| Fields in hierarchical reverse nested field				|
|-----------------------------------------------------------------------|
| `[object_type_name]._reverse_nested:[object_type_name]:_id_parent.[nested_field_field_name]` - Example: `people._reverse_nested:people:_id_parent.name` |

### <a name="sort"></a> Sorting

It is possible to define sorting fields by arranging sorting definitions in an array. Each sorting definition
will be taken into account in the order they are given. A sorting definition is composed of:

| Parameter       | Value |
|-----------------|------ |
| `field`         | field to sort by (string): fully qualified field name. See [Field Names](#fieldnames) |
| `language`      | language used for L10n fields (string, optional) |
| `order`         | sort order (string, optional): `"ASC"` (ascending, default) / `"DESC"` (descending) |
| `mode`          | sort mode for fields with multiple values (string, optional): `"min"` (minimum value), `"max"` (maximum value), `"sum"` (sum of all values), `"avg"` (average value) |
| `nested_filter` | filter for nested objects (map, optional): see below |
| `with_path`     | include path when sorting hierarchical linked objects (bool, optional, defaults to `true`): see below |
| `numeric`       | only effective for strings: enable alphanumeric sorting (bool, optional, defaults to `false`): see [String sorting](/en/webfrontend/datamanagement/search/find/#string-sorting-alphabetical-alphanumeric) |

All fields present in the index are sortable. L10n fields will be expanded to the given `lang`.

The default value for `language` is:

* the "language" defined at top level, for regular fields
* the frontend language of the user, for the special field `_pool` (see below)

#### Example:

{{< include_json "./sort.json" >}}

Additionally, the field `_pool` allows to sort by pool hierarchy. At each level, the pools are ordered by name (l10n).
Then, the children pools are ordered recursively, depth-first. The objects are ordered depending on the pool they
are in. Objects without pool come at the beginning.

See the following example:

- Pool "Animals" (1)
	- Pool "Cats" (2)
	- Pool "Zebras" (3)
- Pool "Trees" (4)
	- Pool "Oaks" (5)

The numbers in parentheses are the numbers used for sorting. Notice that "Oaks" come after "Zebras" because
the parent pools are "Trees" (second place) and "Animals" (first place), respectively.

#### Example:

{{< include_json "./sort_pool.json" >}}

Fields that are marked as Nested can use a `nested_filter` when sorting that defines which values are picked
for sorting the objects. Only fields of numeric, boolean or string/text types can be used.

The specification of the `nested_filter` is a map from fields (using only the field name, not the whole
field path) to an array of terms.

When sorting by linked objects, the whole hierarchy is considered by default. By using `with_path: false`, you can override this behaviour.

Also it is possible to use the field `_score` which allows to sort by the relevance of the object in the search. The more should clauses that match, the more relevant the object.

#### Output: sort

When sorting fields are defined each object will includes an attribute `_sort` with an array of values used to sort, one value per sorting field. Sort values are in a binary format and can be used for per-byte based sorting.

### <a name="aggregations"></a> Aggregations

It is possible to aggregate data based on the search query using so-called "aggregations".
Field's data is aggregated only if one (or both) of the options "Advanced Search" or "Filter" is enabled in mask's search settings for the field.

The requests accepts several aggregations, which are applied independently to the result set.
They are identified by an arbitrary name which is used as key for the "aggregations" object.

#### Example:

{{< include_json "./facets.json" >}}

The aggregation definition has the following common properties:

| Parameter  | Value |
|------------|-------|
| `type`     | Type of the aggregation (string, optional): [**term**](#aggregation-type-term) (default), [**term\_stats**](#aggregation-type-term-stats), [**linked\_object**](#aggregation-type-linked-object), [**asset**](#aggregation-type-asset) or [**date_range**](#aggregation-type-date-range) |
| `limit`    | Number of aggregation objects to return (integer, optional): defaults to 10 |
| `offset`   | Offset for aggregation scrolling (integer, optional): defaults to 0 |
| `sort`     | Property to sort by (string, optional): highest count (**count**, default) or term (**term**) |
| `include`  | Regular expression of elements to be included (string, optional): if given, filter aggregations by this regular expression |
| `language` | Language used for L10n fields (string, optional): defaults to: |
|            | - the "language" defined at top level, for regular fields |
|            | - the frontend language of the user, for the **linked\_object** aggregations for the special field `_pool` (see below) |

Other properties depend on the aggregation type:

#### Aggregation type "term"

| Parameter | Value |
|-----------|------ |
| `field`   | Field used for aggregating (string): fully qualified field name. See [Field Names](#fieldnames) |
| `fields`  | Fields used for aggregating (array of strings). See [Field Names](#fieldnames) |

This aggregation type returns the most frequent terms along with the document count for each one.
If any of the given fields is an L10n field, it will be expanded by `languages`.

##### Example:

The following example gets the top 5 genres along with the book count for each one of them:

{{< include_json "./facet_term.json" >}}

Notice that any indexed field can be given, including fields that are not marked for aggregations in the mask definition.

#### Aggregation type "term\_stats"

| Parameter | Value |
|-----------|------ |
| `field`       | Field used for aggregating (string): fully qualified field name |
| `value_field` | Field used for extracting values (string): fully qualified field name |

This aggregation operates over a `field` in the same way that the aggregation type "term" does, but instead of document counts, it gives
statistical information about the values taken from another field (`value_field`).

##### Example:

The following example returns statistical information about the readers' age by book genre:

{{< include_json "./facet_term_stats.json" >}}

Notice that `field` can be any indexed field, including fields that are not marked for aggregations in the mask definition.

#### Aggregation type "linked\_object"

| Parameter | Value |
|-----------|------ |
| `field`         | Field used for aggregating (string): fully qualified field name |
| `objecttype`    | Objecttype used for aggregating (string): objecttype name |
| `filter_parent` | Allows to filter the returned aggregations by parent (integer, optional): parent ID |

This aggregation type can be used in two different ways. The first one is by providing a `field`. The field may be any
linking field (i.e. "person.birth_place"). For objecttypes with pool link, `_pool` is also available.

The second way is by providing a linked object type (`objecttype`).
The aggregation will take into account all objects of that type that a document links.

Notice that `field` and `objecttype` cannot be combined.

An additional parameter `filter_parent` can be set for hierachical objects (pools are always hierarchical) to filter by
parent ID. It can be set to `null` to obtain only top level elements. The result aggregations contain the hierarchy path.

##### Example:

{{< include_json "./facet_linked_object.json" >}}

Notice that in this case the mask definition matters: only if a linked object is marked for aggregations in the mask definition,
it will be taken into account for aggregating.

#### Aggregation type "asset"

| Parameter | Value |
|-----------|------ |
| `field`   | Field used for aggregating (string): asset field name |

This aggregation type uses all preferred assets of a document and lets perform a term aggregation over them.

Allowed values for `field` are:

* `"class_extension"`
  * aggregate over combinations of `class` and `extension` of assets
  * result example: `["image.jpg", "image.png"]`

* `"class_version_status"`
  * aggregate over combinations of `class`, `version` and `status` of assets
  * result example: `["image.original.done", "image.preview.done"]`

* `"class_version_extension"`
  * aggregate over combinations of `class`, `version` and `extension` of assets
  * result example: `["image.original.jpg", "image.preview.jpg"]`

* `"class_version_filesize"`
  * aggregate over combinations of `class`, `version` and `filesize` of assets
  * result example: `["image.original.4096", "image.preview.1024"]`

##### Example:

{{< include_json "./facet_asset.json" >}}

> Notice that in this case the mask definition matters: only if an asset field is marked for aggregations in the mask definition, it will be taken into account for aggregating.

#### Aggregation type "date_range"

| Parameter | Value |
|-----------|------ |
| `field`   | Field used for aggregating (string): `date` or `date_range` field name |
| `ranges`  | Array of pairs of `to` and `from` timestamp values |
| `format`  | Timestamp format used in the date ranges (string): `"date"`, `"date_time_simple"` or `"date_time"` |

This aggregation type uses `date` or `date_range` fields to aggregate over date ranges.

Per default, if a daterange field is used for aggregating, the internal sub field `_from` is used (the start date of the date range). The sub fields `_to` (end date of the daterange) and `_from` can be specified in the request by adding the suffix `.to` or `.from` respectivly to the field.

The aggregation results will contain the number of objects (`doc_count`). This information can be used to generate searches for these objects or date histograms.

##### `ranges`

In the array `ranges` multiple (at least one!) ranges can be defined. For each range all field values that can be parsed as valid datetime strings, and are inside the range limits, are grouped.

For `date` fields, the date value (`_value`) will be used for the aggregation. For `date_range` fields, the start value (`_from`) will be used for the aggregation.

##### `format`

Valid timestamp formats are:

* `date`
    * requires date values in the format `YYYY-MM-DD`
    * Example: `2019-01-01`

* `date_time_simple`
    * requires datetime values in the format `YYYY-MM-DDTHH:mm:SS`
    * Example: `2019-01-01T23:59:00`

* `date_time` (ISO 8601 format)
    * requires datetime values in the format `YYYY-MM-DDTHH:mm:SS.000Z`
    * Example: `2019-01-01T23:59:00.000Z`

If any other value is used as the format, the server will throw an API error.

> The format of the timestamps used in `ranges` must match the specified `format`. Otherwise, Elasticsearch will throw an error.

##### Request:

Aggregate the date field `publish_date` of `book`, group by 19th and 20th century.

{{< include_json "./facet_daterange.json" >}}

##### Response:

The value of `field` from the request will be used as the key for the aggregation in the response.

For each element in `ranges`, there will be a corresponding object in the array `buckets`.

The value `doc_count` returns the number of objects where there is a date or date range field, where the value is in the range.

The values `from` and `to` are the same that have been given in the request.

They can be used to perform a [range search](#search-element-range) to get the actual objects. The search should return the same number of objects as is indicated by `doc_count`.

{{< include_json "./facet_daterange_response.json" >}}

### <a name="highlight"></a> Highlighting

It is possible to generate highlighted versions on the fields that match the search
request. The highlight definition can be just an empty object.

| Parameter | Value |
|-----------|------ |
| `pre_tag`     | Opening tag for the highlighted text (string, optional): defaults to `"<em>"` |
| `post_tag`    | Closing tag for the highlighted text (string, optional): defaults to `"</em>"` |
| `escape_html` | Whether the text will be HTML-escaped (boolean, optional): defaults to `true` |

The tags can be anything, not only HTML tags.

#### Example:

{{< include_json "./highlight.json" >}}

The results will now contain extra fields
called `<field>:highlight` with the highlighted text (see "Output").

### <a name="fields"></a> Fields

It is possible to select specific fields from the object to be returned. This is particularly interesting when
using a format different than **full**, although it can also be used in combination with it.

The fields specification is given as an array of objects with the following attributes:

| Parameter | Value |
|-----------|-------|
| `field`   | Field name (string) |
| `key`     | Key to use in the output (string, optional): defaults to `field` |
| `mode`    | Aggregate values using a function (string, optional): `"min", "max", "sum", "avg"`, see Sorting |

As field name, the following is accepted:

- a fully qualified regular field
- the path to a linked object
- the path to a pool link
- the special field `_pool`, which expands to all available pool links for the given objecttypes

The `key` can be used to group fields.

`mode` can only be used with numerical fields and it cannot be different for the same `key`. If `mode` is not
provided, all values are returned.

#### Example:

{{< include_json "./fields.json" >}}

## Output

The output is given as a JSON object. The following attributes are provided as a copy of the input:

| Attribute                    | Type     |
|------------------------------|----------|
| `type`                       | string   |
| `objecttypes`                | str-list |
| `language`                   | string; if not set in the input this defaults to: |
|                              | - the first search language of the user, if `type` is **object** |
|                              | - the frontend language of the user, if `type` is not **object** |
| `offset`                     | integer  |
| `limit`                      | integer  |
| `format`                     | string   |

The rest is the real output of the search:

| Attribute                    | Type     | Meaning |
|------------------------------|----------|---------|
| `request_time`               |          |         |
| &#8614; `total`              | integer  | Time this request took (in milliseconds) |
| &#8614; `elasticsearch`      | integer  | Time the Elasticsearch query/queries took (in milliseconds) |
| `count`                      | integer  | Number of hits |
| `objects`                    | obj-list | List of found objects (depending on search type) |
| `aggregations`               | object   | See below "Output: aggregations" |

For each object, the `_source` is returned unless `format` is different from `full`, see below. Additionally, the object will be annotated with highlights, if
the request specified them. See "Output: highlights" below.

If `best_mask_filter` is set to `false`, each object contains a `_best_mask` field (`true` or `false`, on the same level as `_mask`) which indicates whether the object is rendered using the "best mask".
The `_best_mask` field is not present in "short" objects.

If `generate_rights` is `true`, the objects will be rendered with the parameter `_generated_rights` (see [object](/en/technical/types/object)).

For user objects, several l10n fields are given in just one language, following this rule:

- if the user has specified a preferred frontend language and the field has a non-empty value for that language, this is the chosen language
- if not, do the same for the first database language among the preferred user database languages
- if not, do the same for the first database language among the configured database languages
- if not, take the first language with a non-empty value
- if not, return the first language

This affects the `_standard` fields, as well as the pool names.

### Output: format

<a name="format"></a>
The `format` option only applies to user objects. See the [object](/en/technical/types/object) for a description of the formats.

> Notice that for the search, the **short** and **standard** format also imply that linked and nested objects are not rendered at all.
The `_standard` field is provided in the selected `language`.

* The **full** format returns all object's attributes, including `_changelog`. The **full** parameter exists since release 5.34.

* The **long** format returns all object's attributes, except for `_changelog`. Note that this was included until release 5.33.

* The **short** format returns minimal attributes for refering to an object.

#### Example for the **short** format:

{{< include_json "./format_short.json" >}}

* The **standard** format returns attributes needed to have a preview of the objects.

#### Example for the **standard** format:

{{< include_json "./format_standard.json" >}}

Linked objects are always provided in the "standard" format.

### Output: fields

The fields are given for each object under `_fields`. For each provided key, an array of values is given.
The values are gathered from all fields associated with the key. For pool or hierarchical linked objects,
the values represent the hierarchy.

> Notice that the value is always an array: if there is only one value, or if a `mode` was provided to
aggregate values to a single one, search will still return an array (of one element).

#### Example:

Objects returned by the example query in [Fields](#fields):

{{< include_json "./fields_response.json" >}}

### Output: aggregations

The aggregation results are provided with the same structure as the requests: the aggregation name is the
key, and the aggregation result the value.

### Output: highlights

The highlights results are given as extra fields that appear inside the object responses, as siblings of the original fields.
The highlighted field name is the field name plus `":highlight"`.

> *Note*: The highlighted text will be HTML encoded as to avoid confusion with the highlight tags. This will only happen in `"*:highlight"` fields

#### Example:

{{< include_json "./highlight_output.json" >}}

## HTTP status codes

|   |   |
|---|---|
| 200 | Success |
| 400 | Error parsing request: attribute expected, incorrect type or value |
| 403 | Unauthorized session |
| 404 | Objecttype or field not found |
| 409 | Conflict error: cannot search for user objects without user schema |

# Search by object ID

    POST /api/v1/search?token=<token>&system_object_ids=<ids>&format=<format>&best_mask_filter=<best_mask_filter>
    POST /api/v1/search?token=<token>&global_object_ids=<ids>&format=<format>&best_mask_filter=<best_mask_filter>

Search user objects by ID

## Query String

|   |   |
|---|---|
| `token`             | Session token acquired with [/api/v1/session](/en/technical/api/session) |
| `system_object_ids` | Comma-separated list of system object IDS |
| `global_object_ids` | Comma-separated list of global object IDS |
| `format`            | Format, defaults to "long" |
| `best_mask_filter`  | Best mask filter, defaults to `true` |

## Input, Output, HTTP status code

This request behaves as if a regular search with the following input was performed:

{{< include_json "./search-by-id.json" >}}
