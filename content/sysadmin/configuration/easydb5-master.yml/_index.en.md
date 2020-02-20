---
title: "easydb5-master.yml"
layout: config
menu:
  main:
    name: "easydb5-master.yml"
    identifier: "sysadmin/configuration/easydb5-master.yml"
    parent: "sysadmin/configuration"
    weight: 10
---

# easydb5-master.yml

## Obsolete

In earlier versions of easydb5 everything was configured in this configuration file. Since version [5.44](../../../releases/5.38-5.50/5.44/) we recommend the new method with the different configuration files per container.

If you use such a configuration file, you can still do so. Please note that there are no more examples for easydb5-master.yml in all manuals. 

## Migration from easydb5-master.yml to new version:

Example of ```easydb5-master.yml```:
```yml
easydb-server:
  docker-hostname: easydb-server
  pgsql:
    database: easydb
  server:
    external_url: http://hostname.as.seen.in.browser.example.com
  extension:
    external-user-schema: true
  smtp:
    server: mail
    from-address: root@localhost
    hostname: localhost

eas:
  docker-hostname: easydb-eas
  canonical-name: easydb-eas
  log-level: info
  pgsql:
    host: easydb-pgsql
    port: 5432
    username: ****
    password: ****
    database: eas
  num-workers: 1
  num-soffice: 2
  trusted-net: 172.0.0.0/12
  smtp:
    server: relay.example.com
    hostname: easydb-system.example.com
    from-address: noreply@easydb-system.example.com
```

***New version style:***

**easydb-server.yml:**
```yml
docker-hostname: easydb-server

pgsql:
  database: easydb

server:
  external_url: http://hostname.as.seen.in.browser.example.com

extension:
  external-user-schema: true

smtp:
  server: relay.example.com
  hostname: easydb-system.example.com
  from-address: noreply@easydb-system.example.com
```

**eas.yml:**
```yml
docker-hostname: easydb-eas
canonical-name: easydb-eas
log-level: info
pgsql:
  host: easydb-pgsql
  port: 5432
  username: ****
  password: ****
  database: eas
num-workers: 1
num-soffice: 2
trusted-net: 172.0.0.0/12
smtp:
  server: relay.example.com
  hostname: easydb-system.example.com
  from-address: noreply@easydb-system.example.com
```

If you need help with those variables and what they do, please refer to [server](../easydb-server.yml/variables)