---
title: "40 - Installation"
menu:
  main:
    name: "Installation"
    identifier: "sysadmin/installation"
    parent: "sysadmin"
    weight: 1
---
# Installation

Bitte beachten Sie die [Voraussetzungen](/de/sysadmin/requirements) für die Installation schon im Vorfeld.

## easydb auf den Server laden

Sie erhalten von uns Kontoname, Passwort und den Namen Ihrer "Solution". Hier ein Beispiel:

    KONTONAME=zeus
    SOLUTION=pantheon
    docker login --username=$KONTONAME docker.easydb.de:5000

Der obige Befehl wird das Passwort abfragen. $KONTONAME ist dabei ein Platzhalter und wird inklusive des Dollarzeichens ersetzt. Danach sind folgende Befehle autorisiert:

    docker pull docker.easydb.de:5000/pf/server-$SOLUTION
    docker pull docker.easydb.de:5000/pf/webfrontend
    docker pull docker.easydb.de:5000/pf/elasticsearch
    docker pull docker.easydb.de:5000/pf/eas
    docker pull docker.easydb.de:5000/pf/postgresql

Ca. 4 bis 8 Gigabyte werden heruntergeladen, verteilt auf die Komponenten der easydb.
Bitte sorgen Sie für ausreichend Speicherplatz. Unter Debian und Ubuntu z.B. in /var/lib/docker.

Zur Aktualisierung der easydb verwenden Sie ebenfalls die obigen Befehle.

Bitte beachten Sie: Der Speicherbedarf wächst schnell an, falls alte docker-Daten nicht gelöscht werden.

## Datenablage bestimmen 

In diesem Beispiel verwenden wir das Verzeichnis "/srv/easydb" für alle anfallenden Daten. Bitte passen Sie zumindest die erste Zeile an Ihre Gegebenheiten an:

    BASEDIR=/srv/easydb
    mkdir -p $BASEDIR/config
    cd $BASEDIR
    mkdir -p webfrontend eas/{lib,log,tmp} elasticsearch/var pgsql/{etc,var,log,backup} easydb-server/{nginx-log,var}
    chmod a+rwx easydb-server/nginx-log elasticsearch/var eas/tmp; chmod o+t eas/tmp

## Anpassungen {#anpassungen}

Optionale Anpassungen erfolgen in `easydb5-master.yml`, im Verzeichnis BASEDIR/config. Legen Sie diese mit zumindest folgender Ausstattung an:

    easydb-server:
      docker-hostname: easydb-server
      pgsql:
        database: easydb
      server:
        external_url: http://hostname.as.seen.in.browser.example.com

Bitte beachten Sie Besonderheiten Ihrer Solution. Für die Solution "base" z.B. [hier dokumentiert](../../solutions/base).

## Abschluss der Installation

    docker network create easy5net

Damit wird die Kommunikation zwischen den Komponenten ermöglicht.


## Start

Die Komponenten der easydb werden mit je einem Befehl gestartet.

Bitte integrieren Sie diese Befehle in das jeweilige Init-System Ihres Servers.

    docker run -d -ti \
        --name easydb-pgsql \
        --net easy5net \
        --volume=$BASEDIR/config:/config \
        --volume=$BASEDIR/pgsql/etc:/etc/postgresql \
        --volume=$BASEDIR/pgsql/log:/var/log/postgresql \
        --volume=$BASEDIR/pgsql/var:/var/lib/postgresql \
        --volume=$BASEDIR/pgsql/backup:/backup \
        docker.easydb.de:5000/pf/postgresql

---

	sysctl -w vm.max_map_count=262144
	# ... oder statt dessen permanent via /etc/sysctl.conf.

    docker run -d -ti \
        --name easydb-elasticsearch \
        --net easy5net \
        --volume=$BASEDIR/config:/config \
        --volume=$BASEDIR/elasticsearch/var:/var/lib/elasticsearch \
        docker.easydb.de:5000/pf/elasticsearch

---

    docker run -d -ti \
        --name easydb-eas \
        --net easy5net \
        --volume=$BASEDIR/config:/config \
        --volume=$BASEDIR/eas/lib:/var/opt/easydb/lib/eas \
        --volume=$BASEDIR/eas/log:/var/opt/easydb/log/eas \
        --volume=$BASEDIR/eas/tmp:/tmp \
        docker.easydb.de:5000/pf/eas

---

    docker run -d -ti \
        --name easydb-server \
        --net easy5net \
        --volume=$BASEDIR/config:/config \
        --volume=$BASEDIR/easydb-server/var:/easydb-5/var \
        --volume=$BASEDIR/easydb-server/nginx-log:/var/log/nginx \
        docker.easydb.de:5000/pf/server-$SOLUTION

---

    docker run -d -ti \
        --name easydb-webfrontend \
        --net easy5net \
        --volume=$BASEDIR/config:/config \
        -p 80:80 \
        docker.easydb.de:5000/pf/webfrontend

---

Die Abhängigkeiten sind wie folgt:

* easydb-eas hängt von easydb-postgresql ab
* easydb-server hängt von easydb-postgresql und easydb-elasticsearch ab
* easydb-webfrontend hängt von easydb-server ab


Insbesondere beim ersten Start empfehlen wir eine Wartezeit von 20 Sekunden zwischen den Komponenten, damit die initialen Datenstrukturen angelegt werden können.

Auch jedes weitere Mal kann es notwendig sein zwischen den Starts von Elasticsearch und easydb-server Wartezeit einzuhalten, je nach Hardware und Datenlage.

Hier ein Auszug aus einem Init-Skript welches dies abbildet:

~~~~
MAXWAITCYCLE=24    # prevent hanging around in hopless cases
                   # prevent disturbing later (re)starts

waitforelastic(){  # sleep until elasticsearch is ready
    until
        /usr/bin/docker exec -ti easydb-elasticsearch cat /var/log/elasticsearch/docker-cluster.log 2>/dev/null |grep -q 'Cluster health status changed from .* to \[GREEN\]' 2>/dev/null
    do
        sleep 10
        MAXWAITCYCLE=$((MAXWAITCYCLE-1))
        [ $MAXWAITCYCLE -lt 1 ] && break
    done
}

case "$1" in
start|restart)
        $0 stop 2>&1 | sed '/No such container:/d; s/^/stopping: /'
        set -e
        run-easydb-elasticsearch
        run-easydb-pgsql
        sleep 10
        run-easydb-eas
        waitforelastic
        run-easydb-server
        sleep 10
        run-easydb-webfrontend
;;
stop)
        /usr/bin/docker stop  easydb-webfrontend
        /usr/bin/docker rm -v easydb-webfrontend
        /usr/bin/docker stop  easydb-server
        /usr/bin/docker rm -v easydb-server
        /usr/bin/docker stop  easydb-eas
        /usr/bin/docker rm -v easydb-eas
        /usr/bin/docker stop  easydb-elasticsearch
        /usr/bin/docker rm -v easydb-elasticsearch
        /usr/bin/docker stop  easydb-pgsql
        /usr/bin/docker rm -v easydb-pgsql
~~~~

---

# Resultat

An Port 80 Ihres Servers ist nun die easydb bereit für Anfragen von Web-Browsern.

---

# Weiterführendes

Weitere Befehle sind im Kapitel [Betrieb](../betrieb) aufgeführt, z.B. für Aktualisierungen und Sicherheitskopien.

Falls Sie auf einem Server mehr als eine easydb installieren, sehen Sie bitte die Ergänzungen im Kapitel [Instanziierung](../instances).

