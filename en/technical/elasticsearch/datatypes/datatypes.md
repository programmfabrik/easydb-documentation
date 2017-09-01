# Datatypes

## Elasticsearch core types

Elasticsearch types are provided in lowercase:

- object: unless otherwise stated, objects are not included in parent nor root
- long
- date
- bool

## Text, Text-sort

Fields of type Text are mapped as follows:


[include](./text.json)


Fields of type Text-sort have an additional "sort" field that helps sorting them according to the first backend language.


[include](./text.json)


## String, String-sort

Fields of type String are mapped as follows:


[include](./string.json)


Fields of type String-sort have an additional "sort" field that helps sorting them according to the first backend language.

## L10n

L10n fields are a structure holding a Text field for each language. Additionally, they have a "sort" field
in order to sort them according to the rules of each language:


[include](./l10n.json)


## L10n-sort

L10n-sort fields are like regular L10n fields, but they only have the "sort" field. They only allow a verbatim
search but they allow sorting.


[include](./l10n-sort.json)


## Token-Text

**TODO**

## Token-String

**TODO**

## Date

**TODO**

## DateRange

**TODO**

## Changelog

The changelog contains an array of entries. That means that most search queries will only be meaningful as nested search elements.
However, a direct search is also possible because it is mapped with `include_in_parent`.
See [here](/technical/types/cl_entry/cl_entry.md) for a description of the fields:

| Field             | Datatype     |
|-------------------|--------------|
| `batch_id`        | long         |
| `operation`       | string       |
| `schema_version`  | long         |
| `time`            | date         |
| `version`         | long         |
| `current_version` | bool         |
| `user`            | object       |
| &#8614; `_id`     | long         |
| `groups`          | long         |
| `comment`         | Text         |

## Asset

**TODO**

## FacetInfo

**TODO**
