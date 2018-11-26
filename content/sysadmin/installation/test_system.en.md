---
title: "Setting up a test system"
menu:
  main:
    name: "Test system"
    identifier: "sysadmin/installation/test_system"
    parent: "sysadmin/installation"
    weight: 2
---
# Setting up a test system

Scope of this tutorial is to set up a copy of the easydb web application using data already entered in the production. It is no solution to do any kind of live migration from one easydb instance to another one. The steps below may be repeated from time to time to get more current data, but than means to throw away the test system and set it up again.

The clone can be done on multiple levels. Given the easydb is hosted in a virtual machine it might be the easiest way to just clone the virtual machine and adjust some settings to be able to run both VMs in parallel. There is a short but incomplete introduction given in the paragraph [Complete Clone](#complete-clone).

If you don't have the resources to clone the virtual machine (especially RAM might be the limiting factor due to multiple instances of ElasticSearch running), there is a more complete description to set up a [Test system on the same machine](#test-system-on-the-same-machine).

In addition to the possibilities described here there are more options, reusing more or less resources of the production system. For the sake of simplicity they are deliberately not described any further.

**For both options described: please check your backup first. There always is a possibility for data loss due to accidential misconfiguration or corner cases ignored by this tutorial.**

## Complete clone

### Pros

* may be easier to set up
* less likely to interfere with production system

### Cons

* depends on an easy way to clone a running system, so it's most likely only useful when the easydb is running inside a virtual machine
* requires more physical resources as the operating system, the ElasticSearch server and the database server are not shared

### Instructions

There are no instructions given when something has to be done in virtual machine hypervisor (e.g. VMware or libvirt) or the operating system (most likely Debian, but others are possible). Consult the vendor manual where required.

* shut down the production system
* clone the virtual machine, no storage should be shared between these machines
* set up newly created clone to get a different IP address
  * change the hardware address (MAC) for the clone's network interface (hypervisor)
  * when the IP address is hard-coded in the operating system, the clone should be started, the IP address changed
* start the clone if not already started in step before
* change the external URL given in `easydb-server.server.external_url` (in file `easydb5-master.yml`, see [Installation](/en/sysadmin/installation)) to the new URL
* if there is a web server running inside the virtual machine (e.g. when [HTTPS](/en/sysadmin/konfiguration/recipes/https) is in use), the virtual host configuration must be checked and updated, too
* start the production system again, check everything

## Test system on the same machine

### Pros

* reuses same machine (physical or virtual) and some server processes, so it requires less resources
* less data has to be copied, so it may be faster to set up even if more steps are involved

### Cons

* more complex to set up
* runs on shared resources like the production system, so it can interfere with the production system (may slow down when shared resources are limited and on misconfiguration there can be even data lost)

### Instructions

It is assumed the server is running using the `pf/server-base` image. This ensures an external user schema is used.

To not always repeat path names and other values which might differ depending on values chosen at installation time, there will be used shell-like variables in these instructions. When something like `$EXAMPLE` is mentioned, the value from the table below has to be used. The shell commands are given as an example and should only be used if understood.

| variable | default or recommended value | notes |
|----------|---------------|-------|
|`SRC_BASEDIR`         | `/srv/easydb`                             | |
|`SRC_RUN_PGSQL`       | `$SRC_BASEDIR/run-pgsql.sh`               | no real default given in [Installation](/en/sysadmin/installation) |
|`SRC_RUN_EAS`         | `$SRC_BASEDIR/run-eas.sh`                 | no real default given in [Installation](/en/sysadmin/installation) |
|`SRC_RUN_SERVER`      | `$SRC_BASEDIR/run-server.sh`              | no real default given in [Installation](/en/sysadmin/installation) |
|`SRC_RUN_WEBFRONTEND` | `$SRC_BASEDIR/run-webfrontend.sh`         | no real default given in [Installation](/en/sysadmin/installation) |
|`SRC_CNT_PGSQL`       | `easydb-pgsql`                            | value for `--name` in `$SRC_RUN_PGSQL` |
|`SRC_CNT_EAS`         | `easydb-eas`                              | value for `--name` in `$SRC_RUN_EAS` |
|`SRC_CNT_SERVER`      | `easydb-server`                           | value for `--name` in `$SRC_RUN_SERVER` |
|`SRC_CNT_WEBFRONTEND` | `easydb-webfrontend`                      | value for `--name` in `$SRC_RUN_WEBFRONTEND` |
|`SRC_DIR_EAS_CONFIG`  | `$SRC_BASEDIR/config`                     | usually the same for all containers, depends on `--volume` mapping for `/config` in `$SRC_RUN_EAS`
|`SRC_DIR_EAS_LIB`     | `$SRC_BASEDIR/eas/lib`                    | depends on `--volume` mapping for `/var/opt/easydb/lib/eas` in `$SRC_RUN_EAS` |
|`SRC_DIR_EAS_LOG`     | `$SRC_BASEDIR/eas/log`                    | depends on `--volume` mapping for `/var/opt/easydb/log/eas` in `$SRC_RUN_EAS` |
|`SRC_DIR_EAS_TMP`     | `$SRC_BASEDIR/eas/tmp`                    | depends on `--volume` mapping for `/var/opt/easydb/lib/eas` in `$SRC_RUN_EAS` |
|`SRC_DIR_SERVER_CONFIG`  | `$SRC_BASEDIR/config`                  | usually the same for all containers, depends on `--volume` mapping for `/config` in `$SRC_RUN_SERVER` |
|`SRC_DIR_SERVER_VAR`  | `$SRC_BASEDIR/easydb-server/var`          | usually the same for all containers, depends on `--volume` mapping for `/easydb-5/var` in `$SRC_RUN_SERVER` |
|`SRC_DIR_SERVER_NGLOG`| `$SRC_BASEDIR/easydb-server/nginx-log`    | usually the same for all containers, depends on `--volume` mapping for `/var/log/nginx` in `$SRC_RUN_SERVER` |
|`SRC_DIR_WEBFRONTEND_CONFIG`  | `$SRC_BASEDIR/config`             | usually the same for all containers, depends on `--volume` mapping for `/config` in `$SRC_RUN_WEBFRONTEND` |
|`SRC_DB_NAME`         | `easydb`                                  | may be overwritten by `easydb-server.pgsql.database` in `$SRC_DIR_SERVER_CONFIG/easydb5-master.yml` |
|`SRC_DB_NAME_EAS`     | `eas`                                     | may be overwritten by `eas.pgsql.database` in `$SRC_DIR_EAS_CONFIG/easydb5-master.yml` | |
|`DST_DIR_EAS_CONFIG`  | `$SRC_DIR_EAS_CONFIG-clone`               | |
|`DST_DIR_EAS_LIB`     | `$SRC_DIR_EAS_LIB-clone`                  | |
|`DST_DIR_EAS_LOG`     | `$SRC_DIR_EAS_LOG-clone`                  | |
|`DST_DIR_EAS_TMP`     | `$SRC_DIR_EAS_TMP-clone`                  | |
|`DST_DIR_SERVER_CONFIG`| `$SRC_DIR_SERVER_CONFIG-clone`           | |
|`DST_DIR_SERVER_VAR`  | `$SRC_DIR_SERVER_VAR-clone`               | |
|`DST_DIR_SERVER_NGLOG`| `$SRC_DIR_SERVER_NGLOG-clone`             | |
|`DST_DIR_WEBFRONTEND_CONFIG`| `$SRC_DIR_WEBFRONTEND_CONFIG-clone` | |
|`DST_DB_NAME`         | `$SRC_DB_NAME-clone`                      | |
|`DST_DB_NAME_EAS`     | `$SRC_DB_NAME_EAS-clone`                  | |
|`DST_RUN_EAS`         | `$SRC_BASEDIR/run-eas-clone.sh`           | |
|`DST_RUN_SERVER`      | `$SRC_BASEDIR/run-server-clone.sh`        | |
|`DST_RUN_WEBFRONTEND` | `$SRC_BASEDIR/run-webfrontend-clone.sh`   | |
|`DST_CNT_EAS`         | `$SRC_CNT_EAS-clone`                      | |
|`DST_CNT_SERVER`      | `$SRC_CNT_SERVER-clone`                   | |
|`DST_EXTERNAL_URL`    | http://clone.example.com                  | |
|`DST_PORT`            | 82                                        | public port of cloned webfrontend container, may be limited to IP by prefixing it, e.g. `127.0.0.1:82` |

stop the EAS, server and webfrontend containers:

```
docker stop $SRC_CNT_EAS $SRC_CNT_SERVER $SRC_CNT_WEBFRONTEND
```

#### Databases

copy databases for EAS & server:
```
docker exec -ti $SRC_CNT_PGSQL psql -U postgres -c \
	"CREATE DATABASE \"$DST_DB_NAME\" TEMPLATE \"$SRC_DB_NAME\""
docker exec -ti $SRC_CNT_PGSQL psql -U postgres -c \
	"CREATE DATABASE \"$DST_DB_NAME_EAS\" TEMPLATE \"$SRC_DB_NAME_EAS\""
```

#### EAS container clone

copy `lib` and `config` directory for EAS:
```
rsync -av $SRC_DIR_EAS_CONFIG/ $DST_DIR_EAS_CONFIG/
rsync -av $SRC_DIR_EAS_LIB/ $DST_DIR_EAS_LIB/
```

create empty `log` & `tmp` directories like during [Installation](/en/sysadmin/installation):
```
mkdir -p $DST_DIR_EAS_LOG $DST_DIR_EAS_TMP
chmod a+rwx $DST_DIR_EAS_TMP
chmod o+t $DST_DIR_EAS_TMP
```

Ensure the configuration (`$DST_DIR_EAS_CONFIG/easydb5-master.yml`) contains the following values, replacing or extending the configuration which is already there after this file was copied:
```
eas:
  pgsql:
    database: $DST_DB_NAME_EAS
```

Create the EAS container clone start script (`$DST_RUN_EAS`):
```
cat >$DST_RUN_EAS <<EOD
docker run -d -ti \
	--name $DST_CNT_EAS \
	--net easy5net \
	--volume=$DST_DIR_EAS_CONFIG:/config \
	--volume=$DST_DIR_EAS_LIB:/var/opt/easydb/lib/eas \
	--volume=$DST_DIR_EAS_LOG:/var/opt/easydb/log/eas \
	--volume=$DST_DIR_EAS_TMP:/tmp \
	docker.easydb.de:5000/pf/eas
EOD
chmod +x $DST_RUN_EAS
```

Run the EAS clone container:
```
$DST_RUN_EAS
```

#### Server container clone

Copy `config` and `var` directory for server (only copy if `$DST_DIR_SERVER_CONFIG` if it is different from `$DST_DIR_EAS_CONFIG`, otherwise it would overwrite the EAS configuration changed above!)
```
rsync -av $SRC_DIR_SERVER_CONFIG/ $DST_DIR_SERVER_CONFIG/ # if not yet done
rsync -av $SRC_DIR_SERVER_VAR/ $DST_DIR_SERVER_VAR/
```

Create nginx log directory for server (like in [Installation](/en/sysadmin/installation)):
```
mkdir -p $DST_DIR_SERVER_NGLOG
chmod a+rwx $DST_DIR_SERVER_NGLOG
```

Ensure the configuration (`$DST_DIR_SERVER_CONFIG/easydb5-master.yml`) contains the following values, replacing or extending the configuration which is already there after this file was copied:
```
easydb-server:
  docker-hostname: $DST_CNT_SERVER
  server:
    external-url: $DST_EXTERNAL_URL
  pgsql:
    database: $DST_DB_NAME
  eas:
    url: http://$DST_CNT_EAS/eas
eas:
  docker-hostname: $DST_CNT_EAS
```

Create the server container clone start script (`$DST_RUN_SERVER`):
```
cat >$DST_RUN_SERVER <<EOD
docker run -d -ti \\
    --name $DST_CNT_SERVER \\
    --net easy5net \\
    --volume=$DST_DIR_SERVER_CONFIG:/config \\
    --volume=$DST_DIR_SERVER_VAR:/easydb-5/var \\
    --volume=$DST_DIR_SERVER_NGLOG:/var/log/nginx \\
    docker.easydb.de:5000/pf/server-base
EOD
chmod +x $DST_RUN_SERVER
```

Run the server clone container:
```
$DST_RUN_SERVER
```

#### Webfrontend container clone

If not yet done (`$DST_DIR_WEBFRONTEND_CONFIG` is different from `$DST_DIR_EAS_CONFIG` and `$DST_DIR_SERVER_CONFIG`), `config` directory for webfrontend:
```
rsync -av $SRC_DIR_WEBFRONTEND_CONFIG/ $DST_DIR_WEBFRONTEND_CONFIG/ # if not yet done
```

Ensure the configuration (`$DST_DIR_WEBFRONTEND_CONFIG/easydb5-master.yml`) contains the following values, replacing or extending the configuration which is already there after this file was copied:
```
easydb-server:
  docker-hostname: $DST_CNT_SERVER
eas:
  docker-hostname: $DST_CNT_EAS
```

Create the webfrontend container clone start script (`$DST_RUN_WEBFRONTEND`):
```
cat >$DST_RUN_WEBFRONTEND <<EOD
docker run -d -ti \\
    --name $DST_CNT_WEBFRONTEND \\
    --net easy5net \\
    --volume=$DST_DIR_WEBFRONTEND_CONFIG:/config \\
    -p $DST_PORT:80 \\
    docker.easydb.de:5000/pf/webfrontend
EOD
chmod +x $DST_RUN_WEBFRONTEND
```

Run the webserver clone container:
```
$DST_RUN_WEBFRONTEND
```

#### Start production system again

restart the eas, server and webfrontend containers:
```
docker start $SRC_CNT_EAS $SRC_CNT_SERVER $SRC_CNT_WEBFRONTEND
```

