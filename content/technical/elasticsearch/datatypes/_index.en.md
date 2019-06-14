---
title: "88 - datatypes"
menu:
  main:
    name: "datatypes"
    identifier: "technical/elasticsearch/datatypes"
    parent: "technical/elasticsearch"
---
# Datatypes

## Elasticsearch core types

Elasticsearch types are provided in lowercase:

- `object`: unless otherwise stated, objects are not included in parent or root
- `long`
- `date`
- `bool`

## Text

Fields of type Text are mapped as follows:


{{< include_json "./text.json" >}}

<!--
TODO does this still exist?

Fields of type Text-sort have an additional "sort" field that helps sorting them according to the first backend language.


{{< include_json "./text.json" >}}
-->


## String

Fields of type String are mapped as follows:


{{< include_json "./string.json" >}}

<!--
TODO does this still exist?

Fields of type String-sort have an additional "sort" field that helps sorting them according to the first backend language.
 -->

## L10n

L10n fields are a structure holding a Text field for each language. Additionally, they have a "sort" field
in order to sort them according to the rules of each language:


{{< include_json "./l10n.json" >}}

<!--

## L10n-sort

L10n-sort fields are like regular L10n fields, but they only have the "sort" field. They only allow a verbatim
search but they allow sorting.


{{< include_json "./l10n-sort.json" >}}

 -->

<!--
TODO does this still exist?

## Token-Text

**TODO**

## Token-String

**TODO**

## Date

**TODO**

## DateRange

**TODO**

 -->

## Changelog

The changelog contains an array of entries. That means that most search queries will only be meaningful as nested search elements.
However, a direct search is also possible because it is mapped with `include_in_parent`.

See [here](/en/technical/types/cl_entry) for a description of the fields:

| Field             | Datatype     |
|-------------------|--------------|
| `batch_id`        | `long`       |
| `operation`       | `string`     |
| `schema_version`  | `long`       |
| `time`            | `date`       |
| `version`         | `long`       |
| `current_version` | `bool`       |
| `user`            | `object`     |
| &#8614; `_id`     | `long`       |
| `groups`          | `long`       |
| `comment`         | `Text`       |

<!--

## Asset

**TODO**

## FacetInfo

**TODO**

 -->
