---
title: "elasticsearch.yml"
layout: config
menu:
  main:
    name: "elasticsearch.yml"
    identifier: "sysadmin/configuration/elasticsearch.yml"
    parent: "sysadmin/configuration"
    weight: 20
elasticsearch.yml: []
---
# elasticsearch.yml

## Variables

| variable                                           | type          | mandatory | default value | description |
|---|---|---|---|---|
|`cluster-name`                                      | String        | no        | `docker-cluster` | Name of ElasticSearch cluster. |
|`config`                                            | Map           | no        | _empty_       | Key/value configuration to be directly set in elasticsearch configuration. |
|`discovery-type`                                    | String        | no        | `single-node` | If the Elasticsearch installation consists of multiple nodes, this value has to be changed to `zen`. (since 5.73) |
|`docker-hostname`                                   | String        | no        | `easydb-elasticsearch` | Name of Docker container. Currently unused. |
|`memory-size`                                       | String        | no        | `2g`          | Size of memory statically allocated by ElasticSearch. See [ElasticSearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/5.6/heap-size.html) for some hints how much memory to use. |
|`network-host`                                      | String        | no        | `0.0.0.0`     | Bind address for ElaticSearch service. Should not be changed, it only applies to the networking inside the docker network. |

## Example configuration

```yaml
cluster-name: example-cluster
memory-size: 16g
config:
  indices.fielddata.cache.size: 20%
```
