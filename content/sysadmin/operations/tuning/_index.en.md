---
title: "10 - Tuning"
menu:
  main:
    name: "Tuning"
    identifier: "sysadmin/operations/tuning"
    parent: "sysadmin/operations"
---
# Tune easydb performance

# easydb-server

These are the defaults:

~~~
server:
  frontend:
    num_services: 1
  upload:
    num_services: 1
  indexer:
    num_processes: 1
  preindexer:
    num_processes: 1
  exporter:
    num_workers: 1
~~~

Wenn Sie diese Werte in der Konfiguration überschreiben, dann bedenken Sie bitte dass die easydb für mehr Prozesse auch mehr Hardware benötigt.

Die Konfiguration findet in der Datei `config/easydb-server.yml` statt, deren Eltern-Verzeichnis bei der [Installation](/en/sysadmin/installation) festgelegt wurde.

## Scenarios

Durch parallele Verarbeitung können viele Wartezeiten vermieden werden. Die Zahl der entsprechenden Prozesse sollte auch dem Produktivsystem erhöht werden, allerdings ist dabei auf den Ressourcenverbrauch zu achten. Im Auslieferungszustand ist die easydb für relative kleine Anforderungen konfiguriert, um auch auf ressourcenarmen Testsystemen direkt lauffähig zu sein.

### Mehr Mitarbeiter sollen parallel Daten erfassen können

Erhöhen Sie schrittweise den folgenden Wert, z.B. als erstes auf 2.

~~~
server:
  frontend:
    num_services: 2
~~~

Es besteht auch die Möglichkeit, die Anfragen je nach Typ in 3 verschiedene Gruppen aufzuteilen. Diese werden im Folgenden "`fast`" (nur Event-Polling-Anfragen), "`slow`" (Downloads) und "`medium`" (alles Andere) genannt. Wenn nicht konfiguriert, gibt es nur eine Gruppe, die alle Anfragen abhandelt. Bei Änderungen an der Gruppenkonfiguration müssen sowohl der `server`- als auch der `webfrontend`-Container neugestartet werden.

Der RAM-Verbrauch pro Prozess hängt vom Datenmodell und den Objektgrößen ab, bei mindestens 16G RAM könnte eine sinnvolle Konfiguration aber so aussehen:

~~~
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
server:
  preindexer:
    num_processes: 2
~~~

### Exporte oder Downloads dauern lange, auch bei kleineren Dateien

Downloads und Exporte werden asynchron vorbereitet, dafür steht eine begrenzte Zahl an Prozessen zur Verfügung. Wenn gerade ein größerer Export vorbereitet wird, müssen anstehende Downloads und Exporte gegebenenfalls darauf warten. Es sollten also mehrere Prozesse zur gleichzeitigen Vorbereitung konfiguriert werden:

~~~
server:
  exporter:
    num_workers: 3
~~~

# eas

### Vorschaubilder sollen schneller berechnet werden

Der Easydb Asset Server (EAS) berechnet kleine Bilder ("Versionen") Ihrer Assets vorsorglich, damit diese dann bei Bedarf auf der Web-Oberfläche schnell angezeigt werden können. Falls Sie viele Assets in kurzer Zeit in die easydb einspeisen dann kann hier merkliche Wartezeit entstehen.

Sie können den Wert der parallel berechneten Versionen erhöhen in z.B. `config/eas.yml`. Das Verzeichnis `config` wurde bei der [Installation](/en/sysadmin/installation) festgelegt, Standard: `/srv/easydb/config`. Beispiel für die Einstelllungen:

~~~
num-workers: 2
num-soffice: 3
~~~

Je höher `num-workers` ist desto mehr Berechnungen von Vorschaubildern können gleichzeitig gestartet werden. Anmerkungen: 

* Erhöhung dieser Werte kann zu Engpässen beim RAM führen.

* `num-workers` sollte nicht die Anzahl der CPU-Kerne übersteigen.

* `num-soffice` sollte immer größer sein als `num-workers`. Im Zweifelsfall einfach `num-workers + 1`.

* Mehr dazu [hier](/en/sysadmin/eas/conf/#eas-num-workers).

# elasticsearch

Elasticsearch profitiert vor allem von mehr RAM. Der für den Java-Prozess verwendete RAM muss fest konfiguriert werden und ist dann gebunden. In der Standardkonfiguration sind 2 Gigabyte RAM vorgesehen. Folgende Empfehlungen gibt [die Elasticsearch-Dokumentation](https://www.elastic.co/guide/en/elasticsearch/reference/5.6/heap-size.html):

* nicht mehr als 50% des physikalischen Speichers verwenden, der Rest ist für Caches auf OS-Ebene besser investiert. Die Dokumentation geht hier auch davon aus, dass Elasticsearch allein auf dem System läuft. Wird der komplette easydb-Stack auf einer Maschine betrieben, sollte also eher nur ein Viertel für ES fest verplant werden.
* für eine ES-Node deutlich unter 32G RAM zuteilen. Durch verschiedene Java-Interna kann RAM in dieser Größenordnung schlecht genutzt werden und wäre verschwendet.

In der Konfigurationsdatei `config/elasticsearch.yml` kann die RAM-Größe direkt angegeben werden und weitere Elasticsearch-Optionen können unter `config` generisch angegeben werden. Im Beispiel wird der Arbeitsspeicher auf 4 GByte festgelegt und zwei Cache-Größen werden gesetzt.

~~~
memory-size: 4g
config:
  "indices.fielddata.cache.size": 10%
  "indices.queries.cache.size": 10%
~~~

# docker

## seccomp

On some systems (for example seen on Debian 9 with docker-ce 18.09.1), docker uses the Linux kernel option "seccomp" and thus will increase the time easydb needs to answer. If you have performance problems, it may be worth a try to turn it off. Recreate your containers with an additional option:

~~~
--security-opt seccomp=unconfined
~~~

As an example, for the container `easydb-server` (from the [installation instructions](../../installation/#start)), this would be:

```bash
docker run -d -ti \
    --name easydb-server \
    --security-opt seccomp=unconfined \
    --net easy5net \
    --restart=always \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/easydb-server/var:/easydb-5/var \
    --volume=$BASEDIR/easydb-server/nginx-log:/var/log/nginx \
    docker.easydb.de/pf/server-$SOLUTION
```

