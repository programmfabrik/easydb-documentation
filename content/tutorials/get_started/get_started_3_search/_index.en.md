---
title: "213 - How To Get Started"
menu:
  main:
    name: "3. Searching"
    identifier: "tutorials/get_started/get_started_3_search"
    parent: "tutorials/get_started"

---

[&lArr; 2. Structure of objects](../get_started_2_structure/)

[&rArr; 4. Rendering objects](../get_started_4_rendering/)

----

# 3. Searching for objects

Objects can be read and written over the database API using known IDs. To find objects by text which is included in fields in the objects, the [search API](/en/technical/api/search) can be used.

Searches are performed by `POST` requests to the `/api/v1/search` API endpoint. The search queries, filters and aggregations are defined in a JSON object in the request body:

{{< include_json "../samples/search_basic.jsonc" >}}

Objects are indexed for all masks of the objecttype. For objecttypes with more than one mask, the same object will be returned in all masks in the search result. If only certain masks are required, the masks can be [filtered](#filtered-searches).

It is highly recommended to use the option `"best_mask_filter": true`. It is `true` by default, so it should only be set to `false` if necessary. This returns each object in exactly one mask. Which mask is used is determined by the server, depending on rights management settings for the current user.

> **Note:** all searches are protected under the rights management. This means, the user who performs the search, can only find objects on which the user has at least read right. Also only masks which are enabled for the user to see are considered in the search.
>
> This can have significant influence on the search results.

## Fulltext search

The fulltext query searches for a term in the fulltext of objects. This is done by using a [`"match"` search with the mode `"fulltext"`](/en/technical/api/search/#search-element-match).

The fulltext terms are collected terms from different fields of each object. Which terms are copied to the fulltext is determined by the search option for each field in the masks. So for different masks, different terms are included in the fulltext, which means that the search results can be different depending on the mask(s).

```
{
    "search": [
        {
            "type": "match",
            "mode": "fulltext",
            "string": "berlin",
            "phrase": false,
            "bool": "must"
        }
    ]
}
```

This search will find all objects which include the term "Berlin" or "berlin" in the fulltext. This is limited to masks which enable at least one field for the fulltext search that include these terms.

The option `"phrase"` is used for search strings which include multiple terms. If this option is `false`, all terms are searched without any context. If the option is `true`, the terms must be found as a group in this order.

Example:

For `"phrase": false`, the search string `"berlin alexanderplatz"` will find all objects which include any of the terms `"berlin"` or `"alexanderplatz"` in the fulltext. This means, the objects with `"Berlin Alexanderplatz"` and `"The Alexanderplatz square is in central Berlin"` would be found.

For `"phrase": true`, the search string `"berlin alexanderplatz"` will *only* find objects which include these terms in the correct order in the fulltext. So, the object with `"Berlin Alexanderplatz"` would be found, but not the object with `"The Alexanderplatz square is in central Berlin"`.

## Searching in fields

The search for terms can be limited to [fields](/en/technical/api/search/#fields). Only fields for which the `"expert"` search option is enabled in the mask, can be included in the search.

To only search in specific fields, the `"fields"` array is added to the search query:

```
{
    "search": [
        {
            "type": "match",
            "mode": "fulltext",
            "string": "berlin",
            "phrase": false,
            "bool": "must",
            "fields": [
                "main.title"
            ]
        }
    ]
}
```

This array must include the paths to the fields in the objects, including the objecttype name. In this example, only objects are found where the term `"berlin"` is in the title, all terms in other fields are ignored.

## Filtered searches

In general, filters can be realized by combining multiple search queries. The most simple example would be to include two queries in the search. That means that only objects are found where both queries return a positive result:

{{< include_json "../samples/search_filtered.jsonc" >}}

This search finds all objects of the objecttype `"main"`, where the term `"berlin"` is found in the fulltext, **and** where the file extension of the file is a JPG or a BMP.

### Objecttype filter

A simple out-of-the-box filter is the top level field `"objecttypes"`. If this array is included in the search, the server generates an internal filter for the specified objecttypes. All other objects are ignored.

### Complex searches and filters

More complex combinations of multiple queries can be constructed using logical combinations. Since the syntax of the easydb search is based on the elasticsearch syntax, complex filters can be built according to the boolean logic. Please see the [external documentation of elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-bool-query.html#query-dsl-bool-query).

## Facetted searches (aggregations)

Data from search results can be aggregated to get facetted results. [Aggregations](/en/technical/api/search/#aggregations) are used to group values from different fields into named groups. Aggregations on fields are only possible if the field has the option `"facet": true` set in the search options of the current mask.

Each key below `"aggregations"` is a name of an aggregation. The names can be freely assigned and are used to find the corresponding grouped results (facets) in the search result. The groups can be counted and sorted by occurence.

There are different aggregation types:

### Aggregating on terms

The aggregation type `"term"` is used to group and count terms in specified text fields. It gives an overview over unique occurances of texts in the objects.

{{< include_json "../samples/search_aggr_3.jsonc" >}}

For more details, see [Aggregation type "term"](/en/technical/api/search/#aggregation-type-term)

### Aggregating on linked objects

The aggregation type `"linked_object"` is used to perfrom a term aggregation on the standard text(s) of linked objects or linked pools. The path to the `"field"` with the link can be specified directly, or the `"objecttype"` can be specified, and all linked objects of this objecttype are aggregated over all fields.

{{< include_json "../samples/search_aggr_1.jsonc" >}}

For more details, see [Aggregation type "linked_object"](/en/technical/api/search/#aggregation-type-linked-object)

### Aggregating on assets in objects

The aggregation type `"asset"` is used to aggregate on all assets in an object. The path to the asset can not be specified. All preferred assets in multiple fields are used for the aggregation.

{{< include_json "../samples/search_aggr_2.jsonc" >}}

For more details, see [Aggregation type "asset"](/en/technical/api/search/#aggregation-type-asset)

----

[&lArr; 2. Structure of objects](../get_started_2_structure/)

[&rArr; 4. Rendering objects](../get_started_4_rendering/)
