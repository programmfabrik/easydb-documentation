---
title: "11 - Database access"
menu:
  main:
    name: "Database access"
    identifier: "sysadmin/operations/dbaccess"
    parent: "sysadmin/operations"
---
# Database access

In the default setup, the communication of the easydb asset server and the easydb server with the PostgreSQL server is carried out with a fixed user with a fixed password (named `docker`) with superuser permissions. This poses no increased risk as the PostgreSQL server is not publically reachable and is used exclusively by the easydb components.

It is possible to harden this setup by using a more secure password.

## Change password of user `docker`

### PostgreSQL

Log into PostgreSQL cluster (the `postgres` account is only possible with direct access, no via network):
```
docker exec -ti easydb-pgsql psql -U postgres
```

Generate a secure password, for these examples, `SECUREGENERATEDPASSWORD` is used. Update the password of the already existing `docker` user. While still in `psql` prompt, use:
```
\password docker
```
and enter the password twice.

### easydb server

Now it is required to configure the changed password for the running services. For easydb server, set `pgsql/password` in `easydb-server.yml`:
```
pgsql:
  password: "SECUREGENERATEDPASSWORD"
```
The password will be part of the connection DSN. You might have to encode special characters according to [PgSQL keyword/value connection string rules](https://www.postgresql.org/docs/11/libpq-connect.html#id-1.7.3.8.3.5) and the outer YAML file rules.

### easydb asset server

For the easydb asset server, set `pgsql/password` in `eas.yml`:
```
pgsql:
  password: "SECUREGENERATEDPASSWORD"
```

Finally, restart the `easydb-server` and `easydb-eas` containers to reload the configuration.
