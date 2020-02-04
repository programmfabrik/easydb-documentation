---
title: Example yaml configuration
layout: config
menu:
  main:
    name: "example-configuration"
    identifier: "sysadmin/configuration/easydb-server.yml/example"
    parent: "sysadmin/configuration/easydb-server.yml"
    weight: -993
easydb-server.yml:
---

# Example configuration of easydb's server

In this example we will configure following options:

**easydb server:**

- external url (where the easydb should listen on)
- mailer (if easydb should send mails to your clients)
- default_client (configuration of fylr's objectstore)
- exporter [worker\] (performance setting)
- imexporter [worker\] (performance setting)
- frontend [worker\] (performance setting)
- upload [worker\] (performance setting)
- indexer [worker\] (performance setting)

Please keep following rules for workers in mind:

- Total amount of workers should be not greater than the amount of cpu cores (as rule: total amount of cores -1 = amount of workers you can set)
- If you don't set those options, easydb will will use a default set of workers

Default set of workers:
```yml
exporter:
  num-workers: 1
frontend:
  num-services: 1
  medium:
    num-services: 3
  fast:
    num-services: 2
upload:
  num-services: 1
indexer:
  num-processes: 1
```

**postgresql:**

- host
- port
- database

**easydb asset server (eas):**

- url
- instance

**elasticsearch:**

- url
- default_template

**plugins:**

- custom-data-type-link
- custom-data-type-gnd
- custom-data-type-location
- editor-tagfilter-defaults
- custom-data-type-gazetteer
- connector
- example-plugin

**hotfolder:**

- directory
- upload_batch_size
- upload_batches
- number_of_workers
- urls

**docker-hostname**

**sso:**

- authentication method
- ldap

## easydb-server.yml

```yaml
hostnames:
  server: easydb.example.com:80
  pgsql: postgresql.example.com:5432
  eas: eas.example.com:80
  elasticsearch: elasticsearch.example.com:9200
  fylr: fylr.example.com:4000

pgsql:
  host: postgresql.example.com
  port: 5432
  database: easy5

extension:
  external-user-schema: true

server:
  external_url: http://easydb.example.com
  enable_post_settings: true
  api:
    settings:
      restart: true
      purgedata: true
      purgeall: false
      reindex: true
  mailer:
    enabled: true
  exporter:
    num_workers: 1
  imexporter:
    num_services: 1
    socket: /tmp/easydb/socket/imexporter.sock
  frontend:
    num_services: 1
    socket: /tmp/easydb/socket/frontend.sock
  upload:
    num_services: 1
    socket: /tmp/easydb/socket/upload.sock
  indexer:
    num_processes: 1
  preindexer:
    num_processes: 2

default_client:
  datamodel:
    uid: example-objectstore-uuid
    server: http://objectstore.example.com
    instance: productive

eas:
  url: eas.example.com
  instance: easy5

elasticsearch:
  url: elasticsearch.example.com
  default_template:

plugins:
  enabled+:
    - base.custom-data-type-link
    - base.custom-data-type-gnd
    - base.custom-data-type-location
    - base.editor-tagfilter-defaults
    - base.custom-data-type-gazetteer
    - base.connector
    - base.example-plugin

hotfolder:
  directory: /srv/easydb/webdav
  upload_batch_size: 100
  upload_batches: true
  number_of_workers: 1
  urls:
    - type: windows_webdav
      url: webdav.example.com
      separator: /

docker-hostname: docker.example.com

smtp:
  server: mail.example.com
  hostname: easydb.example.com
  from-address: easydb@example.com

sso:
  auth_method:
    client:
      login:
        visible: true
        show_errors: true
      autostart:
        visible: true
        show_errors: true
        anonymous_fallback: true
  ldap:
    machine_bind:
      url: ldap://ldap.example.com
      who: example@ldap.example.com
      cred: example-credentials
```