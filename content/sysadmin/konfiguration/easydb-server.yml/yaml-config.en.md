---
title: YAML-Configuration
layout: config
menu:
  main:
    name: "yaml-configuration"
    identifier: "sysadmin/konfiguration/easydb-server.yml/yaml-configuration"
    parent: "sysadmin/konfiguration/easydb-server.yml"
easydb-server.yml:
---

# Example configuration of easydb's server

------

***Hostnames for:***
 
- easydb-server
- postgresql
- eas
- elasticsearch
- fylr

***Postgresql settings:***

- **host**: where your postgresl server is running
- **port**: which port your postgresql server is unsing
- **database**: which database easydb5 should use

***Extensions:***

- **external-user-schema**: boolean, if easydb should use external user schema

***Easydb server settings:***

- External address (url for the client to connect to the server)
- **API settings**:
- * If it should be possible for the application root to restart the **server** via. *api (frontend included)*
- * If it should be possible for the application root to purge the **data** via. *api (frontend included)*
- * If it should be possible for the application root to purge **everything** via. *api (frontend included)*

- **mailer**: Setting, if the mailer should be active
- **Easydb-objectstore-configuration**:
- * **UID**: For this see: https://docs.easydb.de/en/sysadmin/konfiguration/fylr.yml/ **objectstore.uids[].uid**
- * **Server**: For this see: https://docs.easydb.de/en/sysadmin/konfiguration/fylr.yml/ **server.addr**
- * **Instance**: For this see: https://docs.easydb.de/en/sysadmin/konfiguration/fylr.yml/ **objectstore.uids[].id**
  
- **Exporter**:
- * **num_workers**: the amount of worker the export can use to calculate the exports

- **Imexporter**: 
- * **num_workers**: the amount of workers, the imexporter is allowed to use to calculate **(MISSING)**

- **Frontend**: 
- * **num_workers**: the amount of workers, the frontend is allowed to use

- **Upload**: 
- * **num_workers**: amount of workers for the upload task

- **Indexer**: 
- * **num_processes**: the amount of workers, the easydb is allowed to use for indexing
- * **objects_per_bath**: the amount of records, the easydb should index at once

***EAS***:

- **url** of the easydb-asset-server (eas)
- **instance** eas instance id the easydb-server should use

***Elasticsearch***:

- **url** of the elasticsearch server
- **default_tamplate** the elasticsearch server should

***Plugins***

- **enabled+** allows you, to enable easydb-plugins. For a list of available plugins see: http://localhost:1313/en/sysadmin/konfiguration/easydb-server.yml/plugin/

***Hotfolder***

- **directory**: path where the hotfolder should be placed
- **upload_batches**: amount of records the easydb should import at once
- **upload_batches**: boolean, if the easydb should bath the import
- **num_of_workers**: the amound of workers, the server should use for the hotfolder
- **urls**: 
- * * **type**: which type of hotfolder should be usen
- * * **url**: where the hotfolder should be accessible
- * * **separator**: 

***Docker***

- **docker-hostname**: docker url

***SMTP***

- **server**: relay mail server which easydb should use
- **hostname**: local easydb hostname
- **from-address**: address from which easydb will send mails (welcome messages etc.)

**SSO / Single sign on**

- auth_method:

- * client:

- * * login:
- * * * **visible**: boolean, if it should be possible to use single sing on
- * * * **show_errors**: boolean, if error should be shown
- * * autostart:
- * * * **visible**: boolean, if the autostart should be active
- * * * **show_errors**: boolean, if errors should be shown
- * * * **anonymous_fallback**: boolean, ?????????
- ldap:
- * machine_bind:
- * * **url**: url to the ldap server

- * * **who**: credentials which should be usen for ldap authentication

- * * **credentials**: credentials needed for login

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
  mailer:
    enabled: true
  default_client:
    datamodel:
      uid: objectstore-uuid
      server: http://objectstore.example.com
      instance: productive
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
    objects_per_batch: 1000

eas:
  url: eas.example.com
  instance: easy5

elasticsearch:
  url: elasticsearch.example.com
  default_template:

plugins:
  enabled+:
    - base.example-plugin

hotfolder:
  directory: /srv/easydb/webdav
  upload_batches: 100
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