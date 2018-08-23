---
title: "47 - Logging"
layout: config
menu:
  main:
    name: "Logging"
    identifier: "sysadmin/konfiguration/easydb-server.yml/logging"
    parent: "sysadmin/konfiguration/easydb-server.yml"
easydb-server.yml:
  - logging.pf.base.config
  - logging.pf.base.transition
  - logging.pf.collection
  - logging.pf.database-schema.check
  - logging.pf.database-schema.enrich
  - logging.pf.database-schema.json
  - logging.pf.database-schema.manager
  - logging.pf.database-schema.upgrade
  - logging.pf.database-schema.xml
  - logging.pf.datamodel.base.mapping
  - logging.pf.datamodel.mask 
  - logging.pf.dbapi.export 
  - logging.pf.dbapi.import 
  - logging.pf.dbapi.simple 
  - logging.pf.dbapi.standard 
  - logging.pf.dirtyqueuer 
  - logging.pf.elasticsearch 
  - logging.pf.elasticsearch.index 
  - logging.pf.elasticsearch.request 
  - logging.pf.elasticsearch.response 
  - logging.pf.export.common 
  - logging.pf.exporter.csv2xml 
  - logging.pf.exporter.def_loader 
  - logging.pf.exporter.exporter 
  - logging.pf.exporter.main 
  - logging.pf.exporter.plan 
  - logging.pf.export.io 
  - logging.pf.export.scheduler 
  - logging.pf.export.worker 
  - logging.pf.ez5.index_manager 
  - logging.pf.ez5.jsonmaskio 
  - logging.pf.ez5.xmlmaskio 
  - logging.pf.frontend.get 
  - logging.pf.frontend.l10n 
  - logging.pf.frontend.post 
  - logging.pf.groupedit 
  - logging.pf.imexporter.annotate 
  - logging.pf.imexporter.eas_bridge 
  - logging.pf.imexporter.eas_bridge.request 
  - logging.pf.imexporter.eas_bridge.response 
  - logging.pf.imexporter.eas_supervisor 
  - logging.pf.imexporter.split 
  - logging.pf.imexporter.support 
  - logging.pf.importer.def_loader 
  - logging.pf.importer.importer 
  - logging.pf.indexer 
  - logging.pf.mailer 
  - logging.pf.maskio 
  - logging.pf.mask.standard 
  - logging.pf.metadata 
  - logging.pf.metadata.mapper 
  - logging.pf.preindexer 
  - logging.pf.search.fields 
  - logging.pf.search.request 
  - logging.pf.search.response 
  - logging.pf.server.asset_io 
  - logging.pf.server.config 
  - logging.pf.server.datamodel.manager 
  - logging.pf.server.deep_link.processor 
  - logging.pf.server.event_io 
  - logging.pf.server.groupio 
  - logging.pf.server.handler 
  - logging.pf.server.janitor 
  - logging.pf.server.mail_manager 
  - logging.pf.server.main 
  - logging.pf.server.maskio 
  - logging.pf.server.objecttype_io 
  - logging.pf.server.plugin 
  - logging.pf.server.plugin.process 
  - logging.pf.server.python 
  - logging.pf.server.right_io 
  - logging.pf.server.rights_manager 
  - logging.pf.server.rights_manager.check_acl 
  - logging.pf.server.rights_manager.check_right 
  - logging.pf.server.session 
  - logging.pf.server.tagio 
  - logging.pf.server.type_system 
  - logging.pf.server.upload 
  - logging.pf.server.userio 
  - logging.pf.suggest.request 
  - logging.pf.watermarkio 
  - logging.pf.xmlmapper 
  - logging.pf.xmlmapper.fieldparser 
  - logging.pf.xslt
---
# Logging-configuration

## Log-Datei

If you use docker, your log files are reachable at two places:

* about the docker-mechanism (`docker logs …`, https://docs.docker.com/config/containers/logging/). Docker loggs the default systemconfiguration in json-files. If you wish to log docker to `syslog`, this is also possible. Logs are reachable solong the container exist. If you remove the docker container (`docker rm ..`) or update, all loggs will be lost.

* inside `imexporter.log` in your `var`-directory inside your `easydb-server` container. This directory will be configured after [turn-on of the container](/en/sysadmin/installation). We recommend you to clean up this file regularly with a `logrotate` and save it if needed. 

## Log-Level

The log-level decides which log-messages are displayed. Messages with the same level or higher priority will be shown, all other will be not displayed. Following log-level are configurable (descending sorted).

| Log-Level | Description |
|-----------|--------------|
|**critical**| Error, which Massively disrupt operation. Usually the server is not able to get alive without help.|
|**error**| Error which disrupt operation. Usually the server should still run.|
|**warn**| Errors that are not noticed at all or only by a few users.|
|**info**| Messages which inform about the current state. This can roughly estimate the activity on the server.|
|**debug**| Messages for developer which helps to fix bugs. Without 
deeper insight, those messages are mostly incomprehensible.|

Normaly `info` is choosen inside the `easydb5-master.yml` to log every message with `info` or higher (`warn`, `error`, `critical`) level:

| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `logging.pf`                                   | log-level | no | Contains a log level for a specific path | info |

#### Example:
```yaml
easydb-server:
  logging:
    pf: info
```

## Log-path

For each component in easydb the log-level can be choosen seperatly. With this option it's possible to increase/decrease the logging for a specified process. The used log-level depends on the hierarchical logging system and which log path where choosen. This is a hierarchical system, and at the end it uses the log level that best suits the topic. The base is `pf` as shown above, but it may be e.g. Give plugins that do not rank themselves in this hierarchy.

As example:
```yaml
easydb-server:
  logging:
    pf: info
    pf.elasticsearch: debug
    pf.plugin.base.hotfolder: warn
```

**The following list gives a short overview about the used log-pathes. There is no claim to completeness:**

| Log-path variable                              | Type           | Description |
|------------------------------------------------|----------------|-------------|
| `pf.base.config`                                   | log-level      | Contains a log level for a specific path |
| `pf.base.transition`                                   | log-level      | Contains a log level for a specific path |
| `pf.collection`                                   | log-level      | Contains a log level for a specific path |
| `pf.database-schema.check`                                   | log-level      | Contains a log level for a specific path |
| `pf.database-schema.enrich`                                   | log-level      | Contains a log level for a specific path |
| `pf.database-schema.json`                                   | log-level      | Contains a log level for a specific path |
| `pf.database-schema.manager`                                   | log-level      | Contains a log level for a specific path |
| `pf.database-schema.upgrade`                                   | log-level      | Contains a log level for a specific path |
| `pf.database-schema.xml`                                   | log-level      | Contains a log level for a specific path |
| `pf.datamodel.base.mapping`                                   | log-level      | Contains a log level for a specific path |
| `pf.datamodel.mask`                                   | log-level      | Contains a log level for a specific path |
| `pf.dbapi.export`                                   | log-level      | Contains a log level for a specific path |
| `pf.dbapi.import`                                   | log-level      | Contains a log level for a specific path |
| `pf.dbapi.simple`                                   | log-level      | Contains a log level for a specific path |
| `pf.dbapi.standard`                                   | log-level      | Contains a log level for a specific path |
| `pf.dirtyqueuer`                                   | log-level      | Contains a log level for a specific path |
| `pf.elasticsearch`                                   | log-level      | Contains a log level for a specific path |
| `pf.elasticsearch.index`                                   | log-level      | Contains a log level for a specific path |
| `pf.elasticsearch.request`                                   | log-level      | Contains a log level for a specific path |
| `pf.elasticsearch.response`                                   | log-level      | Contains a log level for a specific path |
| `pf.export.common`                                   | log-level      | Contains a log level for a specific path |
| `pf.exporter.csv2xml`                                   | log-level      | Contains a log level for a specific path |
| `pf.exporter.def_loader`                                   | log-level      | Contains a log level for a specific path |
| `pf.exporter.exporter`                                   | log-level      | Contains a log level for a specific path |
| `pf.exporter.main`                                   | log-level      | Contains a log level for a specific path |
| `pf.exporter.plan`                                   | log-level      | Contains a log level for a specific path |
| `pf.export.io`                                   | log-level      | Contains a log level for a specific path |
| `pf.export.scheduler`                                   | log-level      | Contains a log level for a specific path |
| `pf.export.worker`                                   | log-level      | Contains a log level for a specific path |
| `pf.ez5.index_manager`                                   | log-level      | Contains a log level for a specific path |
| `pf.ez5.jsonmaskio`                                   | log-level      | Contains a log level for a specific path |
| `pf.ez5.xmlmaskio`                                   | log-level      | Contains a log level for a specific path |
| `pf.frontend.get`                                   | log-level      | Contains a log level for a specific path |
| `pf.frontend.l10n`                                   | log-level      | Contains a log level for a specific path |
| `pf.frontend.post`                                   | log-level      | Contains a log level for a specific path |
| `pf.groupedit`                                   | log-level      | Contains a log level for a specific path |
| `pf.imexporter.annotate`                                   | log-level      | Contains a log level for a specific path |
| `pf.imexporter.eas_bridge`                                   | log-level      | Contains a log level for a specific path |
| `pf.imexporter.eas_bridge.request`                                   | log-level      | Contains a log level for a specific path |
| `pf.imexporter.eas_bridge.response`                                   | log-level      | Contains a log level for a specific path |
| `pf.imexporter.eas_supervisor`                                   | log-level      | Contains a log level for a specific path |
| `pf.imexporter.split`                                   | log-level      | Contains a log level for a specific path |
| `pf.imexporter.support`                                   | log-level      | Contains a log level for a specific path |
| `pf.importer.def_loader`                                   | log-level      | Contains a log level for a specific path |
| `pf.importer.importer`                                   | log-level      | Contains a log level for a specific path |
| `pf.indexer`                                   | log-level      | Contains a log level for a specific path |
| `pf.mailer`                                   | log-level      | Contains a log level for a specific path |
| `pf.maskio`                                   | log-level      | Contains a log level for a specific path |
| `pf.mask.standard`                                   | log-level      | Contains a log level for a specific path |
| `pf.metadata`                                   | log-level      | Contains a log level for a specific path |
| `pf.metadata.mapper`                                   | log-level      | Contains a log level for a specific path |
| `pf.preindexer`                                   | log-level      | Contains a log level for a specific path |
| `pf.search.fields`                                   | log-level      | Contains a log level for a specific path |
| `pf.search.request`                                   | log-level      | Contains a log level for a specific path |
| `pf.search.response`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.asset_io`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.config`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.datamodel.manager`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.deep_link.processor`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.event_io`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.groupio`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.handler`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.janitor`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.mail_manager`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.main`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.maskio`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.objecttype_io`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.plugin`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.plugin.process`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.python`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.right_io`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.rights_manager`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.rights_manager.check_acl`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.rights_manager.check_right`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.session`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.tagio`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.type_system`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.upload`                                   | log-level      | Contains a log level for a specific path |
| `pf.server.userio`                                   | log-level      | Contains a log level for a specific path |
| `pf.suggest.request`                                   | log-level      | Contains a log level for a specific path |
| `pf.watermarkio`                                   | log-level      | Contains a log level for a specific path |
| `pf.xmlmapper`                                   | log-level      | Contains a log level for a specific path |
| `pf.xmlmapper.fieldparser`                                   | log-level      | Contains a log level for a specific path |
| `pf.xslt`                                   | log-level      | Contains a log level for a specific path |