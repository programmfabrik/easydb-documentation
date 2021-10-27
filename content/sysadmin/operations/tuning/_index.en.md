---
title: "10 - Tuning"
menu:
  main:
    name: "Tuning"
    identifier: "sysadmin/operations/tuning"
    parent: "sysadmin/operations"
---
# Performance tuning

## easydb-server

By default, the server uses the following settings, which will remain in effect until you reconfigure them.

```yaml
server:
  frontend:
    slow:
      num_services: 1
    medium:
      num_services: 3
    fast:
      num_services: 2
  upload:
    num_services: 1
  indexer:
    num_processes: 1
  preindexer:
    num_processes: 1
  exporter:
    num_workers: 1
```

If you overwrite these values in the configuration, please keep in mind that the easydb needs more hardware for more processes.

The configuration takes place in the file `config/easydb-server.yml`, whose parent directory was specified during [Installation](/en/sysadmin/installation).

## Scenarios

Many waiting times can be avoided by parallel processing. The number of corresponding processes should also be increased in the production system, but you should pay attention to resource consumption. In the delivery state, easydb is configured for relatively small requirements in order to be able to run directly on low-resource test systems.

### More employees should be able to enter data in parallel

In that case you can try to increase the number of frontend processes.

Frontend tasks are divided into 3 different groups depending on the type of requests they answer. These types are referred to as `fast` (events: browser polling requests for updates), `slow` (e.g. zipping files together for downloads) and `medium` (everything else). If their configuration changes, both the `server` and `webfrontend` containers should be restarted.

The RAM consumption per process depends on the data model and the object sizes, but with at least 16G RAM a reasonable configuration could look like this:

```yaml
server:
  frontend:
    slow:
      num_services: 2
    medium:
      num_services: 4
    fast:
      num_services: 3
```

### A lot of new data should appear faster in the search results

Gradually increase the number of preindexer processes, e.g. first to 2.

```yaml
server:
  preindexer:
    num_processes: 2
```

After each increment, watch the effect on the system under heavy load, especially if there still is enough memory left for some disk cache (25% is good). If on the other hand, memor is so low that swap (memory on disk) is used a lot, then it is more efficient to use less processes but with faster (non-swap) memory.

As a general maximum we recomend to use not more preindexer processes than half of your cores. So for example, on a system with 8 cores, do not use more than 4 preindexer processes.

### Exports or downloads take a long time, even with smaller files

Downloads and exports are prepared asynchronously; a limited number of processes are available for this purpose. If a large export is being prepared, downloads and exports may have to wait. Several processes should therefore be configured for simultaneous preparation:

```yaml
server:
  exporter:
    num_workers: 3
```

## interval between rebuilding the suggest index

In an easydb with default settings, the suggest index is recreated every two hours. In the log of a small easydb you would find that it takes for example `22737 ms`, by using a command like:

```
grep 'suggest.* rebuilding index done, total' /srv/easydb/easydb-server/var/imexporter.log
```

If you instead find values much greater, or even more than two hours long, than this tasks puts your system under too much (constant) load.

To only rebuild the suggest index twice a day, you could configure:

```yaml
suggest:
  timestamps: [ "00:30","12:30" ]
```

# eas

### Preview images should be calculated faster

The Easydb Asset Server (EAS) precautionarily calculates small images ("versions") of your assets so that they can be quickly displayed on the web interface when needed. If you have a large number of assets that need to be uploaded to easydb in a short period of time, there may be a noticeable delay.

You can increase the value of the parallel calculated versions in e.g. `config/eas.yml`. The `config` directory was set during [installation](/en/sysadmin/installation), default: `/srv/easydb/config`. Example for the settings:

```yaml
num-workers: 2
num-soffice: 3
```

The higher 'num-workers' is the more calculations of thumbnails can be started at the same time. Remarks: 

* Increasing these values can lead to RAM bottlenecks.

* `num-workers` should be less than the number of CPU cores.

* `num-soffice` should always be larger than `num-workers`. In case of doubt, simply `num-workers + 1`.

* More about this [here](/en/sysadmin/eas/conf/#eas-num-workers).

# elasticsearch

Elasticsearch benefits above all from more RAM. The RAM used for the Java process must be configured permanently and is then bound. In the standard configuration, 2 gigabytes of RAM are provided. The following recommendations are given by [the Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/5.6/heap-size.html):

* do not use more than 50% of the physical memory, the rest is better invested for caches at OS level. The documentation here also assumes that Elasticsearch runs on the system alone. If the complete easydb stack is run on one machine, it is better to schedule only a quarter for ES.
* for an ES node significantly below 32G RAM. Due to various Java internals, RAM of this size can be badly used and would be wasted.

The RAM size can be specified directly in the configuration file 'config/elasticsearch.yml' and further Elasticsearch options can be specified generically under 'config'. In the example the RAM is set to 4 GByte and two cache sizes are set.

```yaml
memory-size: 4g
config:
  "indices.fielddata.cache.size": 10%
  "indices.queries.cache.size": 10%
```

# docker

## seccomp

On some systems (for example seen on Debian 9 with docker-ce 18.09.1), docker uses the Linux kernel option "seccomp" and thus will increase the time easydb needs to answer. If you have performance problems, it may be worth a try to turn it off. Recreate your containers with an additional option:

```bash
--security-opt seccomp=unconfined
```

In context, for the container `easydb-server` (from the [installation instructions](../../installation/#start)), this would look like:

```bash
docker run -d -ti \
    --name easydb-server \
    --security-opt seccomp=unconfined \
    --net easy5net \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/easydb-server/var:/easydb-5/var \
    --volume=$BASEDIR/easydb-server/nginx-log:/var/log/nginx \
    docker.easydb.de/pf/server-$SOLUTION
```

# Dangers

## Too many indexers

We have not yet seen any advantage in setting indexer processes to more than 1. But we have seen disadvanteges in values higher than 1 (slowed down indexing). So please do not increase this value:

```yaml
server:
  indexer:
    num_processes: 1
```

We merely keep this as a variable to test effects of future changes and special scenarios. If you are tempted to increase it, we advise to closely watch the system for obvious benefits of this increase - and if there are none, to immediatly set it back to 1.

