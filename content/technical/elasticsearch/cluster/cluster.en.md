---
title: "87 - cluster"
menu:
  main:
    name: "cluster"
    identifier: "technical/elasticsearch/cluster/cluster"
    parent: "technical/elasticsearch"
---
# Elasticsearch cluster

## Installation

The following is installed on each node:

- Java 7: better memory management (Garbage Collector)
- ES: newest version (gerade: 0.90.3)
- ES-Plugins:
  - ICU: Support for Unicode (`plugin -install elasticsearch/elasticsearch-analysis-icu/1.11.0`)
  - Monitoring Plugins (seee below)

The monitoring plug-ins can be installed or removed at any time, but ICU must be installed
before easydb starts.

## Configuration

All variables are configured in `/etc/elasticsearch/elasticsearch.yml`, if not otherwise stated.

### Nodes and shards

When the nodes are started, they automatically form a cluster if all of them share the same `cluster.name`. `node.name` is the ID for the respective node.

You can specialize the nodes. The configuration runs via the variables in `node.master`
and `node.data`:

| Typ | node.master | node.data | Bedeutung |
|-----|-------------|-----------|-----------|
| Master node | true | false | Koordiniert die anderen Nodes, speichert keine Shards |
| Data node | false | true | Speichert Shards und macht die Suchoperationen |
| Load balancer | false | false | Verteilt die Anfragen zu den Data Nodes |
| Nicht spezialisiert | true | true | Macht alles |

ES automatically selects a master node from all those who can. In the beginning, we will exclusively
have non-specialized nodes, because it's only worth it if you have a large cluster.

The nodes distribute the documents of an index in shards. Unfortunately, the number of shards can't be determined.
when an index is created. This means that you have to think in advance how large the cluster will be
can. The configuration variable is `index. number_of_shards`. You can also use it for mapping for
but in our case, it probably doesn't make any sense.

### memory

Lucene relies heavily on file system cache. That means you shouldn't allocate too much memory for Elasticsearch. The website says you should use about half of the available memory
assigned. Afterwards, you can use the monitoring tools to see whether to change this value.

Elasticsearch can be configured to lock the memory allocated to it, so that
the operating system does not swap it.

You should configure the following environment variables:

- `ES_HEAP_SIZE=...`: z.B. "6g"
- `MAX_LOCKED_MEMORY=unlimited`

And in the configuration file:

- `bootstrap.mlockall: true`

### Other configuration variables

You can configure a list of plugins in `plugin. mandatory`. Elasticsearch will not be used
if a plugin from the list is missing. Easydb requires "analysis-icu".

Depending on the cluster's network architecture, you may also need to configure settings for Network,
Gateway, Recovery and Discovery. For Amazon EC2 there are special plugins and settings.

## Monitoring and Control

There are many monitoring plug-ins:

- [Elastic HQ](http://www.elastichq.org/)
- [kopf](https://github.com/lmenezes/elasticsearch-kopf)
- [Bigdesk](https://github.com/search?q=bigdesk)
- [head](https://mobz.github.io/elasticsearch-head/)
- [paramedic](https://github.com/karmi/elasticsearch-paramedic)
- [segmentspy](https://github.com/polyfractal/elasticsearch-segmentspy)

During operation, you can change certain routing properties of an index, such as how many
Shards can be stored in a node (`routing. allocation. total_shards_per_node`). A list
of possible variables is here: http://www.elasticsearch.org/guide/reference/api/admin-indices-update-settings/

The number of replicas can also be changed during operation (`index.number_of_replicas`). Pay attention while Elasticsearch often tries to keep the replica shards in a different node than the primary shards
 If this is not possible the cluster status becomes red.

Otherwise you can use the logs. They can be configured via `/etc/elasticsearch/logging.yml`.
Elasticsearch uses log4j (http://logging.apache.org/log4j/2.x/manual/configuration.html).

