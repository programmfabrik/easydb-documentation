---
title: "210 - How To Get Started"
menu:
  main:
    name: "How To Get Started"
    identifier: "tutorials/get_started"
    parent: "tutorials"

---

# How To Get Started

This step by step guide is supposed to be a starting point for working with the basic architecture of the easydb objects and assets, as well as searching and parsing objects in search results.

It consists of the following parts:

1. [Datamodel](get_started_1_datamodel/)
  - [Objecttypes and fields](get_started_1_datamodel/#objecttypes-and-fields-in-the-schema)
  - [Masks for objecttypes](get_started_1_datamodel/#masks-for-objecttypes)
  - [Localization](get_started_1_datamodel/#localization)
2. [Structure of objects](get_started_2_structure/)
  - [JSON objects over API](get_started_2_structure/#json-objects-over-different-api-endpoints)
3. [Searching for objects](get_started_3_search/)
  - [Fulltext search](get_started_3_search/#fulltext-search)
  - [Searching in fields](get_started_3_search/#searching-in-fields)
  - [Filtered searches](get_started_3_search/#filtered-searches)
  - [Facetted searches](get_started_3_search/#facetted-searches-aggregations)
4. [Rendering objects based on masks](get_started_4_rendering/)
  - [Iterating over fields based on the mask](get_started_4_rendering/#iterating-over-fields-based-on-the-mask)

> **Note**: for all following API calls it is assumed that an [authenticated session token](/en/technical/api/session/) is included in the requests:
>
> * either in the HTTP header: `'x-easydb-token: <TOKEN>'`
> * or as an URL parameter: `?token=<TOKEN>`
