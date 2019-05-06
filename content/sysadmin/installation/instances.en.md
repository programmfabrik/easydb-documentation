---
title: "40 - Instances"
menu:
  main:
    name: "Instances"
    identifier: "sysadmin/installation/instances"
    parent: "sysadmin/installation"
    weight: 1
---
# Instances

If you install more than one easydb on one server, the installation and operation commands will change.

We will look at an example with two instances:

```
1st instance:

INSTANCE=olymp
DATABASE=olymp
SOLUTION=base

2nd instance:

INSTANCE=atlantis
DATABASE=atlantis
SOLUTION=base
```

&nbsp;

# Installation

In the [Data Store](../), a directory is created for shared data accessible by all instances:

```bash
mkdir common
cd common
mkdir -p eas/{lib,log} elasticsearch/var pgsql/{etc,var,log,backup} config
chmod a+rwx elasticsearch/var
echo "commonconfig: none" >> config/easydb5-master.yml
cd ..
```

In addition, run the following commands for each instance:

```bash
mkdir $INSTANCE
cd $INSTANCE
mkdir -p webfrontend easydb-server/{nginx-log,var} config
chmod a+rwx easydb-server/nginx-log 
cd ..
```

Create a configuration file `$ INSTANCE/config/easydb5-master.yml` for each instance with:

```yaml
easydb-server:
  docker-hostname: easydb-server-$INSTANCE
  pgsql:
    database: $DATABASE
  eas:
    instance: $INSTANCE
  log-level: info
```

Remarks:

- You must replace the placeholders `$ DATABASE` and` $ INSTANCE` yourself in each configuration file.
- Placeholders are replaced, including the dollar sign. Therefore, `cd $INSTANCE` does not become `cd $olymp` but `cd olymp`.


## Splitting the default http-ports

While this is no longer part of easydb, we would like to show you how to forward browser queries to the correct instance.

One domain name per instance is used as a criterion to the outside, that is, e.g. Olymp.example.com and atlantis.example.com.

Inward, each instance requires its own port number, e.g. 81 and 82. To the outside, however, only port 80 is accessible.

If you are using an Apache web server for this purpose, the configuration would be:

```bash
<VirtualHost *:80>
    ServerName olymp.example.com
    ProxyPass / http://127.0.0.1:81/
    ProxyPassReverse / http://127.0.0.1:81/
</VirtualHost>

<VirtualHost *:80>
    ServerName atlantis.example.com
    ProxyPass / http://127.0.0.1:82/
    ProxyPassReverse / http://127.0.0.1:82/
</VirtualHost>
```

&nbsp;

# Start

The first three components of the easydb are identical to the simple installation, see "[Start](/en/sysadmin/installation)".

However, the last two components, `easydb-server` and` easydb-webfrontend`, must be started once for each of your instances.

Here is the start of `olymp`. The same commands for `atlantis`, but with` INSTANCE = atlantis` and `PORT = 82`:

```bash
INSTANCE=olymp
PORT=81
BASEDIR=/srv/easydb/$INSTANCE

docker run -d -ti \
    --name easydb-server-$INSTANCE \
    --net easy5net \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/easydb-server/var:/easydb-5/var \
    --volume=$BASEDIR/easydb-server/nginx-log:/var/log/nginx \
    docker.easydb.de/pf/server-$SOLUTION

docker run -d -ti \
    --name easydb-webfrontend-$INSTANCE \
    --net easy5net \
    --volume=$BASEDIR/config:/config \
    -p 127.0.0.1:$PORT:80 \
    docker.easydb.de/pf/webfrontend
```

In this example, we use `/srv/easydb` as [data store](/en/sysadmin/installation). Please change this to your requirements.

&nbsp;

# Stop

Suppose you want to terminate both instances - atlantis and olympics - as well as all common components of easydb:


```bash
docker stop  easydb-webfrontend-olymp
docker rm -v easydb-webfrontend-olymp

docker stop  easydb-server-olymp
docker rm -v easydb-server-olymp

docker stop  easydb-webfrontend-atlantis
docker rm -v easydb-webfrontend-atlantis

docker stop  easydb-server-atlantis
docker rm -v easydb-server-atlantis

docker stop  easydb-eas
docker rm -v easydb-eas

docker stop  easydb-elasticsearch
docker rm -v easydb-elasticsearch

docker stop  easydb-pgsql
docker rm -v easydb-pgsql
```

&nbsp;

# Backup by pg_dump

The `eas` database is backed up [normal](../../betrieb). This results in the example of olympic and atlantis:

```bash
docker exec -i -t easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/olymp.pgdump olymp

docker exec -i -t easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/atlantis.pgdump atlantis

docker exec -i -t easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/eas.pgdump eas
```


## Restore a backup made with pg_dump

Since the database `eas` stores data for all instances, we recommend the joint production of all databases from the same backup.

The example of two instances named olympic and atlantis:

```bash
docker exec -i -t easydb-pgsql psql -U postgres -c 'DROP   DATABASE "eas"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'DROP   DATABASE "olymp"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'DROP   DATABASE "atlantis"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'CREATE DATABASE "eas"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'CREATE DATABASE "olymp"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'CREATE DATABASE "atlantis"'
docker exec -i -t easydb-pgsql pg_restore -U postgres -v -d eas      /backup/eas.pgdump
docker exec -i -t easydb-pgsql pg_restore -U postgres -v -d olymp    /backup/olymp.pgdump
docker exec -i -t easydb-pgsql pg_restore -U postgres -v -d atlantis /backup/atlantis.pgdump
```
