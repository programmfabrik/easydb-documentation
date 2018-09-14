---
title: "easydb-master.yml"
layout: config
menu:
  main:
    name: "easydb-master.yml"
    identifier: "sysadmin/konfiguration/easydb-master.yml"
    parent: "sysadmin/konfiguration"
    weight: 10
---

# easydb5-master.yml

The **easydb5-master.yml** combines different configurations into one file. This file is read at startup time of the docker images of easydb and split into pieces.

```
eas:
  docker-hostname: easydb-eas       # user
  canonical-name: easydb-eas
  log-level: info                   # critical, error, warning, info, debug
  pgsql:                            # database configuration
    host: easydb-pgsql
    port: 5432
    username: ****
    password: ****
    database: eas
  num-workers: 1                    # can be set, but there are constraints with
                                    # EAS_NUM_SOFFICE (must be greater than EAS_NUM_WORKERS)
  trusted-net: 172.0.0.0/8

common:
  email:
    server: mail
    from-address: root@localhost
    hostname: localhost

```
