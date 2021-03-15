---
title: "Backup and restore"
menu:
  main:
    name: "Backup and restore"
    identifier: "sysadmin/backupandrestore"
    parent: "sysadmin"
    weight: -944
---

# Backup and restore

## Securing the assets

Backup the directory that you specified for the data store during the [installation](../installation). There we use `/srv/easydb/` as an example (in the placeholder `$BASEDIR`).

This includes everything (e.g. `config/`, assets in `eas/`, sql in `pgsql/`) except the login information for the download of the easydb software. It is typically stored into `/root/.docker/` but you can also always get this information from us.

If you splitted the storage into several mount points, which is not unusal, then backup all of them, of course.

You do not have to but should exclude the directory `elasticsearch/var/` and - if you backup the databases as recommended below - exclude `pgsql/var/`.

This means you have saved everything, including your assets.

But the metadata information needs special care - it is stored in SQL databases, which could change even during the backup process.

## Backup the databases

The easydb internally uses two PostgreSQL databases. To copy them consistently, you have two options:

_Either - very simple:_

__A.__ Stop the easydb while backing up the data store.

_Or - our recommendation:_

__B.__ Use the PostgreSQL-specific tool `pg_dump`.

pg_dump saves in a format which is still compatible after software updates. pg_dump does not need the easydb to be stopped.

The space requirement is also lower than with method A - if you exclude `pgsql/var/` while saving the data storage.

## Backup using pg_dump

```bash
DATABASE=easydb5

docker exec easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/$DATABASE.pgdump $DATABASE

docker exec easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/eas.pgdump eas
```

Remarks:

- The easydb can and should run during this backup method. At least the component "easydb-pgsql" has to run.
- You will then find the backup files in the subdirectory `pgsql/backup/` of the data store defined during the [installation](../installation).
- If you first run pg_dump and then backup the data store, then you also include the dump files automatically.

To display the database names you use, use the following:

```bash
docker exec easydb-pgsql psql -U postgres -l
```

They are typically `eas` and `easydb5` (or `eas` and `easydb`).

&nbsp;

## maintenance contract

If you have a maintenance contract with us, we will let the linux host make dumps of the databases each night.

You can choose how many of them will be kept and at which time they are made. By default 7 dumps (one week) will be kept and the dump will be made each night at a time specified in a cron job file inside the directory `/etc/cron.d/`.

The dumps will be placed in the subdirectory `pgsql/backup/` of the data store defined during the [installation](../installation) (default: `/srv/easydb/`).

Many customers who host easydb themselves on premise create backups of the whole virtual machine. If you instead want access to Linux to create your backups, we can arrange SSH access, for e.g. rsync. You can then initiate the connection whenever you see fit and pull the files.

## hosting contract

If you have a hosting contract with us, we will copy all data to one of our separate backup servers each night.

In case you additionally want to retrieve copies, we can arrange SSH access to your hosted easydb server, for e.g. rsync. You can then initiate the connection whenever you see fit and pull the files.

&nbsp;

# Restore a backup copy

1. Stop the easydb. (Described at the [Operations](/en/sysadmin/operations/#stop) page)
2. Replace the contents of the data store with the backup copy. You have defined the data store at the [installation](../installation).
3. Start the first part of easydb - the component "easydb-pgsql". This is the first start command in the section "[Start](../installation#start)" of the installation.
4. If available, use the backup created by pg_dump:

```bash
DATABASE=easydb5
docker exec -i -t easydb-pgsql psql -U postgres -c 'DROP   DATABASE "eas"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'DROP   DATABASE "'$DATABASE'"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'CREATE DATABASE "eas"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'CREATE DATABASE "'$DATABASE'"'
docker exec -i -t easydb-pgsql pg_restore -U postgres -v -d eas    /backup/eas.pgdump
docker exec -i -t easydb-pgsql pg_restore -U postgres -v -d $DATABASE /backup/$DATABASE.pgdump
```

5. Now start the remaining components. To do this, use the remaining start commands in the [Start](../installation#start) section.
