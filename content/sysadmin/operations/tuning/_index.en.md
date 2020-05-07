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
    num_services: 1
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

The configuration takes place in the file `config/easydb-server.yml', whose parent directory was specified during [Installation](/en/sysadmin/installation).

## Scenarios

Many waiting times can be avoided by parallel processing. The number of corresponding processes should also be increased in the production system, but you should pay attention to resource consumption. In the delivery state, easydb is configured for relatively small requirements in order to be able to run directly on low-resource test systems.

### More employees should be able to enter data in parallel

Gradually increase the following value, e.g. first to 2.

```yaml
server:
  frontend:
    num_services: 2
```

It is also possible to divide the requests into 3 different groups depending on the type. These are referred to as `almost` in the following (event polling requests only), `low` (Downloads) and `medium` (everything else). If not configured, there is only one group that handles all requests. If the group configuration changes, both the `server` and `webfrontend` containers **must be restarted**.

The RAM consumption per process depends on the data model and the object sizes, but with at least 16G RAM a reasonable configuration could look like this

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

### Many new data should appear faster in the search results

Gradually increase the following value, e.g. first to 2.

```yaml
server:
  preindexer:
    num_processes: 2
```

### Exports or downloads take a long time, even with smaller files

Downloads and exports are prepared asynchronously, a limited number of processes are available for this purpose. If a large export is being prepared, downloads and exports may have to wait. Several processes should therefore be configured for simultaneous preparation:

```yaml
server:
  exporter:
    num_workers: 3
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

* `num-workers` should not exceed the number of CPU cores.

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

As an example, for the container `easydb-server` (from the [installation instructions](../../installation/#start)), this would be:

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

