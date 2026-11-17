---
title: "Postgres Upgrade (17)"
menu:
  main:
    name: "Postgres Upgrade (17)"
    identifier: "sysadmin/installation/postgres_upgrade17"
    parent: "sysadmin/installation"
    weight: -993
---

# PostgreSQL Upgrade

From release **5.157** on we will recommend to upgrade PostgreSQL from version **14** to **17**. Depending on the size of your databases, this may consume a lot of time.

On each of your servers (typically just one) which uses the docker-image `docker.easydb.de/pf/postgresql-14` but not yet `docker.easydb.de/pf/postgresql-17`, do all the following steps.

Get our docker image for PostgreSQL 17:

```bash
docker pull docker.easydb.de/pf/postgresql-17
```

Get the list of your databases:

```bash
docker exec easydb-pgsql psql -U postgres -l
```

From this list, ignore `postgres`, `template0` and `template1`. In our example we then have the databases `eas` and `easydb5`.

### stop data input

We assume that the names of your docker containers are as following... (adjust to your situation, but these names are typical)

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
You need to remove or move the old Cluster from the following folders, otherwise PostgreSQL will use another Port for the new Cluster.

We assume that `/srv/easydb` is the directory of your easydb installation.

```bash
rm -rf /srv/easydb/pgsql/var/14
rm -rf /srv/easydb/pgsql/etc/14
```
If you omit the deletion above, then restoring the database may fail with 'role "docker" does not exist' or startup may fail even earlier with 'psql: error: connection to server'.  


### make the new PostgreSQL version the default
In the file defining the container `easydb-pgsql`, e.g. `/srv/easydb/run-pgsql.sh`, use the new docker image:

Before: (showing only the relevant part of the file)

```bash
docker.easydb.de/pf/postgresql-14
```

After:

```bash
docker.easydb.de/pf/postgresql-17
```

Please also take care to adjust other scripts and init-mechanisms that refer to the PostgreSQL image. For example, in installations made by Programmfabrik, `/srv/easydb/maintain` also uses `/pf/postgresql-14` and now needs to use `/pf/postgresql-17`.

### create the docker container with the new PostgreSQL version

```bash
/srv/easydb/run-pgsql.sh
```

### migrate custom PostgreSQL config
If you did PostgreSQL tuning in the old version, e.g. inside `/srv/easydb/pgsql/etc/14/main/postgresql.conf`, then now also do these changes in the new PostgreSQL version, e.g. in `/srv/easydb/pgsql/etc/17/main/postgresql.conf`.

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
docker image rm docker.easydb.de/pf/postgresql-14
```

Also left over directories from the old version can be deleted now:

```bash
rm -rf /srv/easydb/pgsql/etc/14 /srv/easydb/pgsql/var/14
```

... assuming your data storage is `/srv/easydb`.
