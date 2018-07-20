---
title: "47 - Logging"
menu:
  main:
    name: "Logging"
    identifier: "sysadmin/konfiguration/logging"
    parent: "sysadmin/konfiguration"
---
# Logging-Konfiguration

## Log-Datei

Bei Verwendung der Docker-Container sind die Log-Meldungen an 2 Stellen verfügbar:

* über die Docker-Mechanismen (`docker logs …`, https://docs.docker.com/config/containers/logging/). Docker loggt in der Standardeinstellung in JSON-Dateien, Logging ist aber z.B. auch über `syslog` möglich. Die Logs sind zugänglich, solange der Container existiert. Beim Entfernen des Containers (`docker rm …`), z.B. beim Update, gehen diese Logs verloren.
* in die Datei `imexporter.log` im `var`-Verzeichnis des `easydb-server`-Containers. Dieses Verzeichnis wird beim [Start des Containers](/de/sysadmin/installation) konfiguriert. Es sollte sichergestellt werden, dass diese Log-Datei z.B. mit `logrotate` regelmäßig aufgeräumt und nach Bedarf gesichert wird.

## Log-Level

Der Log-Level bestimmt, welche Log-Meldungen ausgeben werden. Meldungen mit der konfigurierten oder höheren Wichtigkeit sind im Log sichtbar, unwichtigere Meldungen werden ausgeblendet. Folgende Log-Level sind verfügbar, absteigend sortiert nach Wichtigkeit:

| Log-Level | Beschreibung |
|-----------|--------------|
|**critical**|Fehler, die den Betrieb massiv stören, der Server kann sich üblicherweise nicht allein erholen.|
|**error**|Fehler, die den Betrieb stören. Der Server läuft aber im Normalfall weiter.|
|**warn**|Fehler, die gar nicht oder nur von wenigen Nutzern bemerkt werden.|
|**info**|Meldungen, die über den aktuellen Status informieren. Damit lässt sich grob die Aktivität auf dem Server abschätzen.|
|**debug**|Meldungen, die zur Behebung von Fehlern für die Entwickler hilfreich sind, ohne tieferen Einblick sind diese Meldungen meist unverständlich.|

Die Konfiguration in der `easydb5-master.yml` erfolgt so, um für fast alle Meldungen (siehe Log-Pfad weiter unten) den Log-Level auf `info` zu setzen. Folglich würden alle Meldungen mit den Wichtigkeiten `info`, `warn`, `error` und `critical` ausgegeben:

~~~~
easydb-server:
  logging:
    pf: info
~~~~

## Log-Pfad

Der Log-Level kann für die verschiedenen Komponenten der easydb separat konfiguriert werden. So kann für Teile der easydb die Anzahl der Meldungen erhöht oder verringert werden. Es handelt sich hierbei um ein hierarchisches System, am Ende wird der Log-Level verwendet, der am genauesten auf die Kompontente passt. Die Basis stellt wie oben schon gesehen `pf` dar, es kann aber z.B. Plugins geben, die sich nicht in diese Hierarchie einordnen.

Beispiel:
~~~~
easydb-server:
  logging:
    # als Basis ist der Log-Level "info" gesetzt
    pf: info
    # für den EAS-Supervisor nur Warnungen oder schlimmer
    pf.imexporter.eas_supervisor: warn
    # für Elasticsearch-Interaktion alle Debug-Meldungen...
    pf.elasticsearch: debug
    # ... außer den Antworten, die sind zu viel
    pf.elasticsearch.response: info
~~~~

Die folgende Liste gibt einen Überblick über die verwendeten Log-Pfade. Es besteht aber kein Anspruch auf Vollständigkeit:
~~~~
pf.base.config
pf.base.transition
pf.collection
pf.database-schema.check
pf.database-schema.enrich
pf.database-schema.json
pf.database-schema.manager
pf.database-schema.upgrade
pf.database-schema.xml
pf.datamodel.base.mapping
pf.datamodel.mask
pf.dbapi.export
pf.dbapi.import
pf.dbapi.simple
pf.dbapi.standard
pf.dirtyqueuer
pf.elasticsearch
pf.elasticsearch.index
pf.elasticsearch.request
pf.elasticsearch.response
pf.export.common
pf.exporter.csv2xml
pf.exporter.def_loader
pf.exporter.exporter
pf.exporter.main
pf.exporter.plan
pf.export.io
pf.export.scheduler
pf.export.worker
pf.ez5.index_manager
pf.ez5.jsonmaskio
pf.ez5.xmlmaskio
pf.frontend.get
pf.frontend.l10n
pf.frontend.post
pf.groupedit
pf.imexporter.annotate
pf.imexporter.eas_bridge
pf.imexporter.eas_bridge.request
pf.imexporter.eas_bridge.response
pf.imexporter.eas_supervisor
pf.imexporter.split
pf.imexporter.support
pf.importer.def_loader
pf.importer.importer
pf.indexer
pf.mailer
pf.maskio
pf.mask.standard
pf.metadata
pf.metadata.mapper
pf.preindexer
pf.search.fields
pf.search.request
pf.search.response
pf.server.asset_io
pf.server.config
pf.server.datamodel.manager
pf.server.deep_link.processor
pf.server.event_io
pf.server.groupio
pf.server.handler
pf.server.janitor
pf.server.mail_manager
pf.server.main
pf.server.maskio
pf.server.objecttype_io
pf.server.plugin
pf.server.plugin.process
pf.server.python
pf.server.right_io
pf.server.rights_manager
pf.server.rights_manager.check_acl
pf.server.rights_manager.check_right
pf.server.session
pf.server.tagio
pf.server.type_system
pf.server.upload
pf.server.userio
pf.suggest.request
pf.watermarkio
pf.xmlmapper
pf.xmlmapper.fieldparser
pf.xslt
~~~~
