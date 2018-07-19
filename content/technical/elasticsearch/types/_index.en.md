---
title: "91 - types"
menu:
  main:
    name: "types"
    identifier: "technical/elasticsearch/types"
    parent: "technical/elasticsearch"
---
# Types

An Easydb index consist of the following types:

| Type             | Used by         | Description | Documentation |
|------------------|-----------------|-------------|---------------|
| `metadata`       | indexer         | metadata information about the index | [metadata](/en/technical/elasticsearch/types/metadata) |
| `mask-<mask_id>` | search, suggest | for each mask, there is a type with a document for each object rendered with it | [mask](/en/technical/elasticsearch/types/mask) |
| `users`          | search | | **TODO** |
| `groups`         | search | | **TODO** |
| `pools`          | search | | **TODO** |
| `collections`    | search | | **TODO** |
| `messages`       | search | | **TODO** |


