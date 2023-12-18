---
title: "47 - Logging"
layout: config
menu:
  main:
    name: "Logging"
    identifier: "sysadmin/configuration/easydb-server.yml/logging"
    parent: "sysadmin/configuration/easydb-server.yml"
    weight: -997
easydb-server.yml:
  - logging."pf"
  - logging."pf.base"
  - logging."pf.base.config"
  - logging."pf.base.transition"
  - logging."pf.collection"
  - logging."pf.database-schema"
  - logging."pf.database-schema.check"
  - logging."pf.database-schema.enrich"
  - logging."pf.database-schema.json"
  - logging."pf.database-schema.manager"
  - logging."pf.database-schema.upgrade"
  - logging."pf.database-schema.xml"
  - logging."pf.databaseschema"
  - logging."pf.databaseschema.main"
  - logging."pf.datamodel"
  - logging."pf.datamodel.base"
  - logging."pf.datamodel.base.mapping"
  - logging."pf.datamodel.mask"
  - logging."pf.db"
  - logging."pf.db.prepared"
  - logging."pf.dbapi"
  - logging."pf.dbapi.export"
  - logging."pf.dbapi.import"
  - logging."pf.dbapi.simple"
  - logging."pf.dbapi.standard"
  - logging."pf.dirtyqueuer"
  - logging."pf.elasticsearch"
  - logging."pf.elasticsearch.index"
  - logging."pf.elasticsearch.request"
  - logging."pf.elasticsearch.response"
  - logging."pf.export"
  - logging."pf.export.common"
  - logging."pf.export.io"
  - logging."pf.export.scheduler"
  - logging."pf.export.worker"
  - logging."pf.exporter"
  - logging."pf.exporter.csv2xml"
  - logging."pf.exporter.def_loader"
  - logging."pf.exporter.exporter"
  - logging."pf.exporter.main"
  - logging."pf.exporter.plan"
  - logging."pf.ez5"
  - logging."pf.ez5.admin"
  - logging."pf.ez5.collection"
  - logging."pf.ez5.db"
  - logging."pf.ez5.dbdebug"
  - logging."pf.ez5.eas"
  - logging."pf.ez5.event"
  - logging."pf.ez5.export"
  - logging."pf.ez5.index_manager"
  - logging."pf.ez5.jsonmaskio"
  - logging."pf.ez5.xmlmaskio"
  - logging."pf.ez5.l10n"
  - logging."pf.ez5.mapping"
  - logging."pf.ez5.metadata"
  - logging."pf.ez5.objects"
  - logging."pf.ez5.plugin"
  - logging."pf.ez5.right"
  - logging."pf.ez5.search"
  - logging."pf.ez5.session"
  - logging."pf.ez5.settings"
  - logging."pf.ez5.suggest"
  - logging."pf.frontend"
  - logging."pf.frontend.get"
  - logging."pf.frontend.l10n"
  - logging."pf.frontend.post"
  - logging."pf.groupedit"
  - logging."pf.imexporter.annotate"
  - logging."pf.imexporter.eas_bridge"
  - logging."pf.imexporter.eas_bridge.request"
  - logging."pf.imexporter.eas_bridge.response"
  - logging."pf.imexporter.eas_supervisor"
  - logging."pf.imexporter.split"
  - logging."pf.imexporter.support"
  - logging."pf.importer"
  - logging."pf.importer.def_loader"
  - logging."pf.importer.importer"
  - logging."pf.importer.main"
  - logging."pf.indexer"
  - logging."pf.mailer"
  - logging."pf.maskio"
  - logging."pf.mask"
  - logging."pf.mask.standard"
  - logging."pf.metadata"
  - logging."pf.metadata.mapper"
  - logging."pf.preindexer"
  - logging."pf.search"
  - logging."pf.search.fields"
  - logging."pf.search.request"
  - logging."pf.search.response"
  - logging."pf.server"
  - logging."pf.server.asset_io"
  - logging."pf.server.config"
  - logging."pf.server.datamodel.manager"
  - logging."pf.server.deep_link.processor"
  - logging."pf.server.event_io"
  - logging."pf.server.groupio"
  - logging."pf.server.handler"
  - logging."pf.server.handler.s"
  - logging."pf.server.janitor"
  - logging."pf.server.mail_manager"
  - logging."pf.server.main"
  - logging."pf.server.maskio"
  - logging."pf.server.objecttype_io"
  - logging."pf.server.plugin"
  - logging."pf.server.plugin.process"
  - logging."pf.server.python"
  - logging."pf.server.right_io"
  - logging."pf.server.rights_manager"
  - logging."pf.server.rights_manager.check_acl"
  - logging."pf.server.rights_manager.check_right"
  - logging."pf.server.session"
  - logging."pf.server.tagio"
  - logging."pf.server.type_system"
  - logging."pf.server.upload"
  - logging."pf.server.userio"
  - logging."pf.server.datamodel"
  - logging."pf.server.dirtyqueuer"
  - logging."pf.server.preindexer"
  - logging."pf.server.indexer"
  - logging."pf.server.worker"
  - logging."pf.suggest"
  - logging."pf.suggest.indexer"
  - logging."pf.suggest.request"
  - logging."pf.watermarkio"
  - logging."pf.xmlmapper"
  - logging."pf.xmlmapper.fieldparser"
  - logging."pf.xslt"
  - logging."pf.ic"
  - logging."pf.ic.exception"
  - logging."pf.ic.exception.affected_rows_mismatch_too_few"
  - logging."pf.ic.exception.affected_rows_mismatch_too_many"
  - logging."pf.ic.exception.result_rows_mismatch_too_few"
  - logging."pf.ic.exception.result_rows_mismatch_too_many"
  - logging."pf.ic.imagehandler"
  - logging."pf.ic.manager"
  - logging."pf.ic.parse_url"
  - logging."pf.imexporter"
  - logging."pf.run"
  - logging."pf.run.child_group"
  - logging."pf.run.request_child_group"
  - logging."pf.test"
  - logging."pf.translation"
  - logging."pf.plugin.base.hotfolder"
---
# Logging Configuration

## Log File

If you use docker, log messages are reachable by two methods:

* via the docker-mechanism (`docker logs …`, https://docs.docker.com/config/containers/logging/ ). Logs are reachable as long as the container exists. If you remove the docker container (`docker rm ..`) or update, all logs will be lost. Alternatively yuo can configure docker to log to `syslog`.

* via filesystem: `easydb-server/var/imexporter.log` in the directory chosen during [Installation](/en/sysadmin/installation). We recommend to clean up this file regularly with a `logrotate`. 

## Log Rotation

This is an exmple configuration of the program logrotate:
```
/srv/easydb/easydb-server/var/imexporter.log /srv/easydb/easydb-server/nginx-log/error.log /srv/easydb/easydb-server/nginx-log/access.log /srv/easydb/pgsql/log/postgresql-9.4-main.log /srv/easydb/eas/log/eas-janitor.log /srv/easydb/eas/log/eas-exception.log /srv/easydb/eas/log/eas-job.log /srv/easydb/eas/log/eas-worker.log /srv/easydb/eas/log/apache.error.log /srv/easydb/eas/log/apache.access.log
{
    copytruncate
    missingok
    size 20M
    dateext
    maxage 62
    rotate 62
    su root www-data
}
```

Not only `imexporter.log` but more or less all possible log files of the easydb are listed. As base directory we assume the default `/srv/easydb`. Adjust to your needs. We recommend copytruncate though, which omits the need for container restarts. Also, we reccomend ths `size` directive as most of the listed logfiles will stay very small for a long time. We do not recommend the compress directive as it may prevent log rotation after one interruption (by a full hard disk).

## Log Level

The log-level decides which log-messages are displayed. Messages with the same level or higher priority will be shown, all other will be not displayed. Following log-level are configurable (descending sorted).

| Log-Level | Description |
|-----------|--------------|
|**critical**| Error, which Massively disrupt operation. Usually the server is not able to get alive without help.|
|**error**| Error which disrupt operation. Usually the server should still run.|
|**warn**| Errors that are not noticed at all or only by a few users.|
|**info**| Messages which inform about the current state. This can roughly estimate the activity on the server.|
|**debug**| Messages for developer which helps to fix bugs. Without deeper insight, those messages are mostly incomprehensible.|

When for example `info` is chosen, every message with `info`, `warn`, `error`, `critical` level are logged:

#### Example:
```yaml
logging:
  pf: info
```

## Component Logging

For each component in easydb the log level can be choosen seperatly. The configuration is structured as a hierarchy. The root is `pf`, but there may be plugins which create their own root.

Another example:
```yaml
logging:
  pf: info
  pf.elasticsearch: debug
  pf.plugin.base.hotfolder: warn
  pf.base.config: info
```

**List of paths in the configuration hierarchy. There is no guarantee for completeness.**

#### logging

| Log-path variable                               | Description |
|-------------------------------------------------|-------------|
| `"pf"` | Log-level definition for pf |
| `"pf.base"` | Log-level definition for pf.base |
| `"pf.base.config"` | Log-level definition for pf.base.config |
| `"pf.base.transition"` | Log-level definition for pf.base.transition |
| `"pf.collection"` | Log-level definition for pf.collection |
| `"pf.database-schema"` | Log-level definition for pf.database-schema |
| `"pf.database-schema.check"` | Log-level definition for pf.database-schema.check |
| `"pf.database-schema.enrich"` | Log-level definition for pf.database-schema.enrich |
| `"pf.database-schema.json"` | Log-level definition for pf.database-schema.json |
| `"pf.database-schema.manager"` | Log-level definition for pf.database-schema.manager |
| `"pf.database-schema.upgrade"` | Log-level definition for pf.database-schema.upgrade |
| `"pf.database-schema.xml"` | Log-level definition for pf.database-schema.xml |
| `"pf.databaseschema"` | Log-level definition for pf.databaseschema |
| `"pf.databaseschema.main"` | Log-level definition for pf.databaseschema.main |
| `"pf.datamodel"` | Log-level definition for pf.datamodel |
| `"pf.datamodel.base"` | Log-level definition for pf.datamodel.base |
| `"pf.datamodel.base.mapping"` | Log-level definition for pf.datamodel.base.mapping |
| `"pf.datamodel.mask"` | Log-level definition for pf.datamodel.mask |
| `"pf.db"` | Log-level definition for pf.db |
| `"pf.db.prepared"` | Log-level definition for pf.db.prepared |
| `"pf.dbapi"` | Log-level definition for pf.dbapi |
| `"pf.dbapi.export"` | Log-level definition for pf.dbapi.export |
| `"pf.dbapi.import"` | Log-level definition for pf.dbapi.import |
| `"pf.dbapi.simple"` | Log-level definition for pf.dbapi.simple |
| `"pf.dbapi.standard"` | Log-level definition for pf.dbapi.standard |
| `"pf.dirtyqueuer"` | Log-level definition for pf.dirtyqueuer |
| `"pf.elasticsearch"` | Log-level definition for pf.elasticsearch |
| `"pf.elasticsearch.index"` | Log-level definition for pf.elasticsearch.index |
| `"pf.elasticsearch.request"` | Log-level definition for pf.elasticsearch.request |
| `"pf.elasticsearch.response"` | Log-level definition for pf.elasticsearch.response |
| `"pf.export"` | Log-level definition for pf.export |
| `"pf.export.common"` | Log-level definition for pf.export.common |
| `"pf.export.io"` | Log-level definition for pf.export.io |
| `"pf.export.scheduler"` | Log-level definition for pf.export.scheduler |
| `"pf.export.worker"` | Log-level definition for pf.export.worker |
| `"pf.exporter"` | Log-level definition for pf.exporter |
| `"pf.exporter.csv2xml"` | Log-level definition for pf.exporter.csv2xml |
| `"pf.exporter.def_loader"` | Log-level definition for pf.exporter.def_loader |
| `"pf.exporter.exporter"` | Log-level definition for pf.exporter.exporter |
| `"pf.exporter.main"` | Log-level definition for pf.exporter.main |
| `"pf.exporter.plan"` | Log-level definition for pf.exporter.plan |
| `"pf.ez5"` | Log-level definition for pf.ez5 |
| `"pf.ez5.admin"` | Log-level definition for pf.ez5.admin |
| `"pf.ez5.collection"` | Log-level definition for pf.ez5.collection |
| `"pf.ez5.db"` | Log-level definition for pf.ez5.db |
| `"pf.ez5.dbdebug"` | Log-level definition for pf.ez5.dbdebug |
| `"pf.ez5.eas"` | Log-level definition for pf.ez5.eas |
| `"pf.ez5.event"` | Log-level definition for pf.ez5.event |
| `"pf.ez5.export"` | Log-level definition for pf.ez5.export |
| `"pf.ez5.index_manager"` | Log-level definition for pf.ez5.index_manager |
| `"pf.ez5.jsonmaskio"` | Log-level definition for pf.ez5.jsonmaskio |
| `"pf.ez5.xmlmaskio"` | Log-level definition for pf.ez5.xmlmaskio |
| `"pf.ez5.l10n"` | Log-level definition for pf.ez5.l10n |
| `"pf.ez5.mapping"` | Log-level definition for pf.ez5.mapping |
| `"pf.ez5.metadata"` | Log-level definition for pf.ez5.metadata |
| `"pf.ez5.objects"` | Log-level definition for pf.ez5.objects |
| `"pf.ez5.plugin"` | Log-level definition for pf.ez5.plugin |
| `"pf.ez5.right"` | Log-level definition for pf.ez5.right |
| `"pf.ez5.search"` | Log-level definition for pf.ez5.search |
| `"pf.ez5.session"` | Log-level definition for pf.ez5.session |
| `"pf.ez5.settings"` | Log-level definition for pf.ez5.settings |
| `"pf.ez5.suggest"` | Log-level definition for pf.ez5.suggest |
| `"pf.frontend"` | Log-level definition for pf.frontend |
| `"pf.frontend.get"` | Log-level definition for pf.frontend.get |
| `"pf.frontend.l10n"` | Log-level definition for pf.frontend.l10n |
| `"pf.frontend.post"` | Log-level definition for pf.frontend.post |
| `"pf.groupedit"` | Log-level definition for pf.groupedit |
| `"pf.imexporter.annotate"` | Log-level definition for pf.imexporter.annotate |
| `"pf.imexporter.eas_bridge"` | Log-level definition for pf.imexporter.eas_bridge |
| `"pf.imexporter.eas_bridge.request"` | Log-level definition for pf.imexporter.eas_bridge.request |
| `"pf.imexporter.eas_bridge.response"` | Log-level definition for pf.imexporter.eas_bridge.response |
| `"pf.imexporter.eas_supervisor"` | Log-level definition for pf.imexporter.eas_supervisor |
| `"pf.imexporter.split"` | Log-level definition for pf.imexporter.split |
| `"pf.imexporter.support"` | Log-level definition for pf.imexporter.support |
| `"pf.importer"` | Log-level definition for pf.importer |
| `"pf.importer.def_loader"` | Log-level definition for pf.importer.def_loader |
| `"pf.importer.importer"` | Log-level definition for pf.importer.importer |
| `"pf.importer.main"` | Log-level definition for pf.importer.main |
| `"pf.indexer"` | Log-level definition for pf.indexer |
| `"pf.mailer"` | Log-level definition for pf.mailer |
| `"pf.maskio"` | Log-level definition for pf.maskio |
| `"pf.mask"` | Log-level definition for pf.mask |
| `"pf.mask.standard"` | Log-level definition for pf.mask.standard |
| `"pf.metadata"` | Log-level definition for pf.metadata |
| `"pf.metadata.mapper"` | Log-level definition for pf.metadata.mapper |
| `"pf.preindexer"` | Log-level definition for pf.preindexer |
| `"pf.search"` | Log-level definition for pf.search |
| `"pf.search.fields"` | Log-level definition for pf.search.fields |
| `"pf.search.request"` | Log-level definition for pf.search.request |
| `"pf.search.response"` | Log-level definition for pf.search.response |
| `"pf.server"` | Log-level definition for pf.server |
| `"pf.server.asset_io"` | Log-level definition for pf.server.asset_io |
| `"pf.server.config"` | Log-level definition for pf.server.config |
| `"pf.server.datamodel.manager"` | Log-level definition for pf.server.datamodel.manager |
| `"pf.server.deep_link.processor"` | Log-level definition for pf.server.deep_link.processor |
| `"pf.server.event_io"` | Log-level definition for pf.server.event_io |
| `"pf.server.groupio"` | Log-level definition for pf.server.groupio |
| `"pf.server.handler"` | Log-level definition for pf.server.handler |
| `"pf.server.handler.s"` | Log-level definition for pf.server.handler.s |
| `"pf.server.janitor"` | Log-level definition for pf.server.janitor |
| `"pf.server.mail_manager"` | Log-level definition for pf.server.mail_manager |
| `"pf.server.main"` | Log-level definition for pf.server.main |
| `"pf.server.maskio"` | Log-level definition for pf.server.maskio |
| `"pf.server.objecttype_io"` | Log-level definition for pf.server.objecttype_io |
| `"pf.server.plugin"` | Log-level definition for pf.server.plugin |
| `"pf.server.plugin.process"` | Log-level definition for pf.server.plugin.process |
| `"pf.server.python"` | Log-level definition for pf.server.python |
| `"pf.server.right_io"` | Log-level definition for pf.server.right_io |
| `"pf.server.rights_manager"` | Log-level definition for pf.server.rights_manager |
| `"pf.server.rights_manager.check_acl"` | Log-level definition for pf.server.rights_manager.check_acl |
| `"pf.server.rights_manager.check_right"` | Log-level definition for pf.server.rights_manager.check_right |
| `"pf.server.session"` | Log-level definition for pf.server.session |
| `"pf.server.tagio"` | Log-level definition for pf.server.tagio |
| `"pf.server.type_system"` | Log-level definition for pf.server.type_system |
| `"pf.server.upload"` | Log-level definition for pf.server.upload |
| `"pf.server.userio"` | Log-level definition for pf.server.userio |
| `"pf.server.datamodel"` | Log-level definition for pf.server.datamodel |
| `"pf.server.dirtyqueuer"` | Log-level definition for pf.server.dirtyqueuer |
| `"pf.server.preindexer"` | Log-level definition for pf.server.preindexer |
| `"pf.server.indexer"` | Log-level definition for pf.server.indexer |
| `"pf.server.worker"` | Log-level definition for pf.server.worker |
| `"pf.suggest"` | Log-level definition for pf.suggest |
| `"pf.suggest.indexer"` | Log-level definition for pf.suggest.indexer |
| `"pf.suggest.request"` | Log-level definition for pf.suggest.request |
| `"pf.watermarkio"` | Log-level definition for pf.watermarkio |
| `"pf.xmlmapper"` | Log-level definition for pf.xmlmapper |
| `"pf.xmlmapper.fieldparser"` | Log-level definition for pf.xmlmapper.fieldparser |
| `"pf.xslt"` | Log-level definition for pf.xslt |
| `"pf.ic"` | Log-level definition for pf.ic |
| `"pf.ic.exception"` | Log-level definition for pf.ic.exception |
| `"pf.ic.exception.affected_rows_mismatch_too_few"` | Log-level definition for pf.ic.exception.affected_rows_mismatch_too_few |
| `"pf.ic.exception.affected_rows_mismatch_too_many"` | Log-level definition for pf.ic.exception.affected_rows_mismatch_too_many |
| `"pf.ic.exception.result_rows_mismatch_too_few"` | Log-level definition for pf.ic.exception.result_rows_mismatch_too_few |
| `"pf.ic.exception.result_rows_mismatch_too_many"` | Log-level definition for pf.ic.exception.result_rows_mismatch_too_many |
| `"pf.ic.imagehandler"` | Log-level definition for pf.ic.imagehandler |
| `"pf.ic.manager"` | Log-level definition for pf.ic.manager |
| `"pf.ic.parse_url"` | Log-level definition for pf.ic.parse_url |
| `"pf.imexporter"` | Log-level definition for pf.imexporter |
| `"pf.run"` | Log-level definition for pf.run |
| `"pf.run.child_group"` | Log-level definition for pf.run.child_group |
| `"pf.run.request_child_group"` | Log-level definition for pf.run.request_child_group |
| `"pf.test"` | Log-level definition for pf.test |
| `"pf.translation"` | Log-level definition for pf.translation |
| `"pf.plugin.base.hotfolder"` | Log-level definition for pf.plugin.base.hotfolder |
