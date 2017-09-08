# Operation
To **update** the easydb software, use the "[load easydb on the server](../installation/installation.md#Load easydb on the server)"  section of the installation.

However, the most recent version will not be used until the easydb has been stopped and restarted.

To **stop** the easydb, use the following commands:

~~~~
    docker stop  easydb-webfrontend
    docker rm -v easydb-webfrontend

    docker stop  easydb-server
    docker rm -v easydb-server

    docker stop  easydb-eas
    docker rm -v easydb-eas

    docker stop  easydb-elasticsearch
    docker rm -v easydb-elasticsearch

    docker stop  easydb-pgsql
    docker rm -v easydb-pgsql
~~~~

We also recommend that you integrate these commands into the init-system of your server, at least for the automated continuous operation.

&nbsp;

If you are running more than one easydb on a server, please note the additions in chapter [instantiation](../instances/instances.md#stop).

&nbsp;

The easydb **start** commands are listed in the "[Start](../installation/installation.md#start)" section of the installation.

&nbsp;

# Status

Which components of the easydb just can run it u.a. Display with `docker ps`. Here is an example display while all components are running:

~~~~
CONTAINER ID        IMAGE                                       COMMAND             CREATED             STATUS              PORTS                   NAMES
efe480718a0e        docker.easydb.de:5000/pf/webfrontend        "/startup.sh"       9 days ago          Up 9 days           0.0.0.0:80->80/tcp      easydb-webfrontend
cdfe24889c0c        docker.easydb.de:5000/pf/server-base        "/startup.sh"       9 days ago          Up 9 days           80/tcp, 3451-3452/tcp   easydb-server
8a17a2a5ea26        docker.easydb.de:5000/pf/eas                "/startup.sh"       10 weeks ago        Up 10 weeks         80/tcp                  easydb-eas
19bf53e50287        docker.easydb.de:5000/pf/elasticsearch      "/startup.sh"       10 weeks ago        Up 10 weeks         9200/tcp, 9300/tcp      easydb-elasticsearch
1a51017ae36e        docker.easydb.de:5000/pf/postgresql         "/startup.sh"       10 weeks ago        Up 10 weeks         5432/tcp                easydb-pgsql
~~~~

To display dormant components, use `docker ps -a`.

&nbsp;

# Backup copies

## Securing the assets
Back up the directory that you specified for the data store during the [installation](../installation/installation.md#datastorage).

This means you have saved everything, not least your assets.

But the information about the assets needs special care - they are stored in PostgreSQL databases, which could also change during backup.

## Backup the databases

The easydb internally uses two PostgreSQL databases. To ensure this consistently, you have two options:

_Entweder - very simple: _

__A .__ Stop the easydb while backing up the data store.

_Oder - our recommendation: _

__B .__ Use the PostgreSQL-specific tool pg_dump to back up.

Pg_dump saves in a format which is still compatible with software updates.

The space requirement is also lower than with method A - if you now save `pgsql/var` when saving the data storage.

## Backup using pg_dump

~~~~
DATABASE=easydb

docker exec -i -t easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/$DATABASE.pgdump $DATABASE

docker exec -i -t easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/eas.pgdump eas
~~~~

Remarks:

- The easydb can and should run during this backup method. The component "easydb-pgsql" must even run.
- You will then find the backup files in the subdirectory `pgsql/backup` of the data store whose location you have defined during the [installation](../installation/installation.md).
- If you first run pg_dump and then save the data store, then you also record these pg_dump files.
- Possibly. You will get the name of your database. Otherwise use the default value "easydb".
- For automated operation, remove the `-i -t` options.

&nbsp;


# Restore a backup copy

1. Exit the easydb. (Described [top](#Operation) on this page)

2. Replace the contents of the data store with the backup copy. You set the data store at the [installation](../installation/installation.md#datastorage).

3. Start the first part of easydb - the component "easydb-pgsql". This is the first start command in the section "[Start](../installation/installation.md#start)" of the installation.

4. If available, use the backup created by pg_dump:

~~~~
DATABASE=easydb
docker exec -i -t easydb-pgsql psql -U postgres -c 'DROP   DATABASE "eas"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'DROP   DATABASE "'$DATABASE'"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'CREATE DATABASE "eas"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'CREATE DATABASE "'$DATABASE'"'
docker exec -i -t easydb-pgsql pg_restore -U postgres -v -d eas    /backup/eas.pgdump
docker exec -i -t easydb-pgsql pg_restore -U postgres -v -d $DATABASE /backup/$DATABASE.pgdump
~~~~

5. Now start the remaining four components. To do this, use the four remaining start commands in the [Start](../installation/installation.md#start) section.

Remarks:

- Possibly. You will get the name of your database. Otherwise use the default value "easydb".
- If you want to display the database names you use, use the following:

~~~~
docker exec -i -t easydb-pgsql psql -U postgres -l
~~~~


&nbsp;