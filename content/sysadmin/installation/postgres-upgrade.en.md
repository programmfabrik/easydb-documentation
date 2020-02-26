---
title: "Postgres Upgrade (11)"
menu:
  main:
    name: "Postgres Upgrade (11)"
    identifier: "sysadmin/installation/postgres_upgrade"
    parent: "sysadmin/installation"
    weight: -990
---

# PostgreSQL Upgrade

Since release **5.62** we recommend to upgraded PostgreSQL from version **9** to **11**. Keep in mind that upgrades of such container consumes a lot of time.

On each of your servers (typically just one) which uses the docker-image `docker.easydb.de/pf/postgresql` but not yet `docker.easydb.de/pf/postgresql-11`, do all the following steps.

Get our docker image for PostgreSQL 11:

```bash
docker pull docker.easydb.de/pf/postgresql-11
```

Get the list of your databases:

```bash
docker exec easydb-pgsql psql -U postgres -l
```

From this list, ignore `postgres`, `template0` and `template1`. In our example we then have the databases `eas` and `easydb5`.

### stop data input

We assume that the names of your docker containers are as following... (adjust to your situation)

```bash
docker stop easydb-webfrontend easydb-server easydb-eas
```

Note that the container easydb-pgsql is not stopped. It is needed for the following step.

### export the data to files

```bash
docker exec -ti easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/eas.pgdump eas
docker exec -ti easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/easydb5.pgdump easydb5
```

### stop the old PostgreSQL version

```bash
docker stop easydb-pgsql
docker rm easydb-pgsql
```

### remove the old postgres data directory
If you have enough free storage, you may delay this step

```bash
rm -rf /srv/easydb/pgsql/var/9.4
```

### make the new PostgreSQL version the default
In the file defining the container `easydb-pgsql`, e.g. `/srv/easydb/run-pgsql.sh`, use the new docker image:

Before: (showing only the relevant part of the file)

```bash
docker.easydb.de/pf/postgresql
```

After:

```bash
docker.easydb.de/pf/postgresql-11
```

### create the docker container with the new PostgreSQL version

```bash
/srv/easydb/run-pgsql.sh
```

### migrate custom postgrs config
If you have custom PostgreSQL configuration inside `/srv/easydb/pgsql/etc/*`, then integrate them into the new PostgreSQL version,
e.g. from `/srv/easydb/pgsql/etc/9.4/main/postgresql.conf` to `/srv/easydb/pgsql/etc/11/main/postgresql.conf`.

Some of our customers do PostgreSQL tuning there. But apart from that, configuration defaults are fine and nothing needs to be done.

### import the data into the new PostgreSQL version

```bash
docker exec -ti easydb-pgsql psql -U postgres -c 'CREATE DATABASE "eas"'
docker exec -ti easydb-pgsql pg_restore -U postgres -v -d eas /backup/eas.pgdump

docker exec -ti easydb-pgsql psql -U postgres -c 'CREATE DATABASE "easydb5"'
docker exec -ti easydb-pgsql pg_restore -U postgres -v -d easydb5 /backup/easydb5.pgdump
```

The error message `ERROR:  schema "public" already exists` can be safely ignored.

### start the rest of the easydb

We assume that the names of your docker containers are as following... (adjust to your situation)

```bash
docker start easydb-eas easydb-server easydb-webfrontend
```

### cleanup
After a few days and after your tests you should finally delete the exported files and the obsolete docker image:

```bash
docker exec easydb-pgsql rm /backup/eas.pgdump /backup/easydb5.pgdump
docker image rm docker.easydb.de/pf/postgresql
```

Also left over directories from the old version can be deleted now:

```bash
rm -rf /srv/easydb/pgsql/etc/9.4 /srv/easydb/pgsql/var/9.4
```

... assuming your data storage is `/srv/easydb`.
