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

**In this basic yaml file you will find some placeholders that look like this: ```'[my-easydb-*]'```. These configurations must be changed manually to a valid value.** 

```yaml
# Includes

include_before:
  - ../../base/base.yml
  - /home/'[my-easydb-directory]'/easydb/5/plugins/base-plugins.yml

# Solution
solution:
  name: my-easydb-solution-name

schema:
  dsn: port=5432 user=postgres dbname=my-easydb-database-name
  base_dir: /home/'[my-easydb-directory]'/easydb/5/server/base/schema
  user_dir: /home/'[my-easydb-directory]'/easydb/schemas/my-database-name/schema/user-custom

# Logging

logging:
  pf: info
  pf.elasticsearch: debug
  pf.plugin.base.hotfolder: debug

suggest:
  document_chunksize: 95
  aggregation_chunksize: 1000
  fields_per_aggregation_chunksize: 1000
  max_context_map_size: 500000
  timestamps: ["00:00", "02:00", "04:00", "06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"]

plugins:
  enabled+:
    - base.custom-data-type-link
    - base.custom-data-type-gnd
    - base.custom-data-type-location
    - base.editor-tagfilter-defaults
    - base.drupal
    - base.custom-data-type-gazetteer
    - base.connector
    - base.example-plugin

server:
  directory:
    pflib:   /home/'[my-easydb-directory]'/easydb/5/server/pflib/src/pflib
    output:  /home/'[my-easydb-directory]'/easydb/5/server/output
    logfile: /home/'[my-easydb-directory]'/logs/imexporter.log
    imexporter:    /home/'[my-easydb-directory]'/easydb/5/server/src/imexporter
    server_errors: /home/'[my-easydb-directory]'/logs/imexporter-server-errors
    elasticsearch: /var/tmp/imexporter-'[my-easydb-directory]'-elasticsearch
    tmp: /home/'[my-easydb-directory]'/tmp
  exporter:
    num_workers: 1
  imexporter:
    num_services: 0
    socket: /tmp/imexporter-'[my-easydb-imexporter-socket-name]'.sock
  frontend:
    num_services: 1
    socket: /tmp/frontend-'[my-easydb-frontend-socket-name]'.sock
  upload:
    num_services: 1
    socket: /tmp/upload-'[my-easydb-upload-socket-name]'.sock
  indexer:
    num_processes: 1
    objects_per_batch: 1000
  external_url: http://'[my-easydb-external-url.tld]'
  api:
    settings:
      purgeall: true
      purgedata: true
      restart: true
      buildsuggest: true

eas:
  instance: '[my-easydb-eas-instance-name]'
  url: http://'[my-easydb-eas-url.tld]'/eas

hotfolder:
  directory: /home/'[my-easydb-directory]'/webdav
  upload_batches: 100
  upload_batches: true
  urls:
    - type: windows_webdav
      url: \\'[my-easydb-webdav-url.tld]'@80\upload\collection
      separator: \

default_client:
  watermark_configured: true
  datamodel:
      uid: [my-easydb-datamodel-uid]
      server: http://'[my-easydb-objectstore-url.tld:port]'/objectstore
      instance: '[my-easydb-objectstore-instance-name]'

sso:
  auth_method:
    client:
      login:
        visible: false
        show_errors: true
      autostart:
        visible: true
        show_errors: true
        anonymous_fallback: true

  ldap:
    machine_bind:
      url: ldap://'[my-easydb-ldap-url]'
      who: '[my-easydb-ldap-username]'@'[my-easydb-ldap-url]'
      cred: '[my-easydb-ldap-credentials]'
```