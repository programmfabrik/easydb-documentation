# Installation

Bitte beachten Sie die [Voraussetzungen](/sysadmin/requirements/requirements.md) für die Installation schon im Vorfeld.

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

Ca. 4 bis 8 Gigabyte werden heruntergeladen, verteilt auf die fünf ausführbaren Komponenten der easydb.
Bitte sorgen Sie für ausreichend Speicherplatz. Unter Debian und Ubuntu z.B. in /var/lib/docker.

Zur Aktualisierung der easydb verwenden Sie ebenfalls die obigen Befehle. Dabei wächst der Speicherbedarf schnell an, falls alte docker-Daten nicht gelöscht werden.

## Datenablage bestimmen

In diesem Beispiel verwenden wir das Verzeichnis "/srv/easydb" für alle anfallenden Daten. Bitte passen Sie zumindest die erste Zeile an Ihre Gegebenheiten an:

    BASEDIR=/srv/easydb
    mkdir -p $BASEDIR/config
    cd $BASEDIR
    mkdir -p webfrontend eas/{lib,log} elasticsearch/var pgsql/{etc,var,log,backup} easydb-server/{nginx-log,var}
    chmod a+rwx easydb-server/nginx-log elasticsearch/var

## Anpassungen

Optionale Anpassungen erfolgen in `easydb5-master.yml`, im Verzeichnis BASEDIR/config. Legen Sie diese mit zumindest folgender Ausstattung an:

    easydb-server:
      docker-hostname: easydb-server
      pgsql:
        database: easydb
      server:
        external_url: http://hostname.as.seen.in.browser.example.com

Bitte beachten Sie Besonderheiten Ihrer Solution. Für die Solution "base" z.B. [hier dokumentiert](../../solutions/base/base.md).

## Abschluss der Installation

    docker network create easy5net

Damit wird die Kommunikation zwischen den Komponenten ermöglicht.


## Start

Die fünf Komponenten der easydb werden mit je einem Befehl gestartet.

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


Die hier gezeigte Reihenfolge der fünf Befehle erfüllt die Abhängigkeiten zwischen den Komponenten und muss daher eingehalten werden.

Insbesondere beim ersten Start empfehlen wir eine Wartezeit von 10 Sekunden zwischen den Komponenten, damit die initialen Datenstrukturen angelegt werden können.

Diese Anleitung wird noch kleine Veränderungen erfahren, passend zu Aktualisierungen der easydb.

---

# Resultat

An Port 80 Ihres Servers ist nun die easydb bereit für Anfragen von Web-Browsern.


---

# Weiterführendes

Die Befehle zum Beenden der easydb sind im Kapitel [Betrieb](../betrieb/betrieb.md) aufgeführt.

Falls Sie auf einem Server mehr als eine easydb installieren, sehen Sie bitte die Ergänzungen im Kapitel [Instanziierung](../instances/instances.md).

