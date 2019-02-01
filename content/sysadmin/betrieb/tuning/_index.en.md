---
title: "10 - Leistung Optimieren"
menu:
  main:
    name: "Leistung Optimieren"
    identifier: "sysadmin/betrieb/tuning"
    parent: "sysadmin/betrieb"
---
# Leistung optimieren

# easydb-server

Falls die Konfiguration nichts anderes sagt, dann gelten folgende Einstellungen:

~~~
easydb-server:
  server:
    frontend:
      num_services: 1
    upload:
      num_services: 1
    indexer:
      num_services: 1
    preindexer:
      num_services: 1
    exporter:
      num_workers: 1
~~~

Wenn Sie diese Werte in der Konfiguration überschreiben, dann bedenken Sie bitte dass die easydb für mehr Prozesse auch mehr Hardware benötigt.

Die Konfiguration findet wie immer in der zentralen Datei `easydb5-master.yml` statt, deren Speicherort bei der [Installation](/de/sysadmin/installation) festgelegt wurde.

## Szenarien

Durch parallele Verarbeitung können viele Wartezeiten vermieden werden. Die Zahl der entsprechenden Prozesse sollte auch dem Produktivsystem erhöht werden, allerdings ist dabei auf den Ressourcenverbrauch zu achten. Im Auslieferungszustand ist die easydb für relative kleine Anforderungen konfiguriert, um auch auf ressourcenarmen Testsystemen direkt lauffähig zu sein.

### Mehr Mitarbeiter sollen parallel Daten erfassen können

Erhöhen Sie schrittweise den folgenden Wert, z.B. als erstes auf 2.

~~~
easydb-server:
  server:
    frontend:
      num_services: 2
~~~

Es besteht auch die Möglichkeit, die Anfragen je nach Typ in 3 verschiedene Gruppen aufzuteilen. Diese werden im Folgenden `fast` (nur Event-Polling-Anfragen), `slow` (Downloads) und `medium` (alles Andere) genannt. Wenn nicht konfiguriert, gibt es nur eine Gruppe, die alle Anfragen abhandelt. Bei Änderungen an der Gruppenkonfiguration müssen sowohl der `server`- als auch der `webfrontend`-Container neugestartet werden.

Der RAM-Verbrauch pro Prozess hängt vom Datenmodell und den Objektgrößen ab, bei mindestens 16G RAM könnte eine sinnvolle Konfiguration aber so aussehen:

~~~
easydb-server:
  server:
    frontend:
      slow:
        num_services: 2
      medium:
        num_services: 4
      fast:
        num_services: 3
~~~

### Viele neue Daten sollen schneller in den Suchergebnissen erscheinen

Erhöhen Sie schrittweise den folgenden Wert, z.B. als erstes auf 2.

~~~
easydb-server:
  server:
    preindexer:
      num_services: 2
~~~

### Exporte oder Downloads dauern lange, auch bei kleineren Dateien

Downloads und Exporte werden asynchron vorbereitet, dafür steht eine begrenzte Zahl an Prozessen zur Verfügung. Wenn gerade ein größerer Export vorbereitet wird, müssen anstehende Downloads und Exporte gegebenenfalls darauf warten. Es sollten also mehrere Prozesse zur gleichzeitigen Vorbereitung konfiguriert werden:

~~~
easydb-server:
  server:
    exporter:
      num_workers: 3
~~~

# elasticsearch

Elasticsearch profitiert vor allem von mehr RAM. Der für den Java-Prozess verwendete RAM muss fest konfiguriert werden und ist dann gebunden. In der Standardkonfiguration sind 2 Gigabyte RAM vorgesehen. Folgende Empfehlungen gibt [die Elasticsearch-Dokumentation](https://www.elastic.co/guide/en/elasticsearch/reference/5.6/heap-size.html):

* nicht mehr als 50% des physikalischen Speichers verwenden, der Rest ist für Caches auf OS-Ebene besser investiert. Die Dokumentation geht hier auch davon aus, dass Elasticsearch allein auf dem System läuft. Wird der komplette easydb-Stack auf einer Maschine betrieben, sollte also eher nur ein Viertel für ES fest verplant werden.
* für eine ES-Node deutlich unter 32G RAM zuteilen. Durch verschiedene Java-Interna kann RAM in dieser Größenordnung schlecht genutzt werden und wäre verschwendet.

In der Konfiguration (`easydb5-master.yml`) kann die RAM-Größe speziell und weitere Elasticsearch-Optionen allgemein angegeben werden. Im Beispiel wird der RAM auf 4G und die Elasticsearch-Konfiguration `node.name` wird ebenfalls gesetzt.

~~~
elasticsearch:
  memory-size: 4g
  config:
    node.name: example
~~~
