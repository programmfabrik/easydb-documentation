# Types

An Easydb index consist of the following types:

| Type             | Used by         | Description | Documentation |
|------------------|-----------------|-------------|---------------|
| `metadata`       | indexer         | metadata information about the index | [metadata](/technical/elasticsearch/types/metadata/metadata.md) |
| `mask-<mask_id>` | search, suggest | for each mask, there is a type with a document for each object rendered with it | [mask](/technical/elasticsearch/types/mask/mask.md) |
| `users`          | search | | **TODO** |
| `groups`         | search | | **TODO** |
| `pools`          | search | | **TODO** |
| `collections`    | search | | **TODO** |
| `messages`       | search | | **TODO** |


