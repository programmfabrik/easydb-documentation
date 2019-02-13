---
title: "41 - Instanziierung"
menu:
  mainWEG:
    name: "Instanziierung"
    identifier: "sysadmin/installation/instances"
    parent: "sysadmin/installation"
    weight: 1
---
# Instanzen

Falls Sie auf einem Server mehr als eine easydb installieren, dann ändern sich die Kommandos für Installation und Betrieb etwas.

Wir nehmen ein Beispiel mit zwei Instanzen an:

```
1. Instanz:

INSTANCE=olymp
DATABASE=olymp
SOLUTION=base

2. Instanz:

INSTANCE=atlantis
DATABASE=atlantis
SOLUTION=base
```

 

# Installation

In der [Datenablage](/de/sysadmin/installation) wird ein Verzeichnis angelegt für gemeinsame Daten, die sich alle Instanzen teilen:

```bash
mkdir common
cd config
mkdir -p eas/{lib,log} elasticsearch/var pgsql/{etc,var,log,backup} config
chmod a+rwx elasticsearch/var
echo "commonconfig: none" >> config/easydb5-master.yml
cd ..
```

Außerdem führen Sie bitte pro Instanz die folgenden Befehle aus:

```bash
mkdir $INSTANCE
cd $INSTANCE
mkdir -p webfrontend easydb-server/{nginx-log,var} config
chmod a+rwx easydb-server/nginx-log
cd ..
```

Legen Sie pro Instanz eine Konfigurationsdatei `$INSTANCE/config/easydb5-master.yml` an mit:

```bash
easydb-server:
  docker-hostname: easydb-server-$INSTANCE
  pgsql:
    database: $DATABASE
  eas:
    instance: $INSTANCE
  log-level: info
```

Anmerkungen:

* Die Platzhalter `$DATABASE` und `$INSTANCE` müssen Sie in jeder Konfigurationsdatei noch selbst ersetzen.
* Platzhalter werden inklusive des Dollarzeichens ersetzt. Daher wird aus `cd $INSTANCE` also nicht `cd $olymp` sondern `cd olymp`.

## Aufteilen des Standard http-ports

Dies ist zwar nicht mehr Teil der easydb aber wir möchten Ihnen trotzdem beispielhaft zeigen, wie Sie Browser-Anfragen an die richtige Instanz weiterleiten.

Als Kriterium nach außen dient dafür je ein Domainname pro Instanz, also z.B. olymp.example.com und atlantis.example.com.

Nach innen benötigt jede Instanz eine eigene Portnummer, z.B. 81 und 82. Nach außen ist jedoch nur Port 80 erreichbar.

Falls Sie einen Apache Webserver für diese Zweck einsetzen dann wäre die Konfiguration folgende:

```bash
<VirtualHost *:80>
    ServerName olymp.example.com
    ProxyPass / http://127.0.0.1:81/
    ProxyPassReverse / http://127.0.0.1:81/
</VirtualHost>

<VirtualHost *:80>
    ServerName atlantis.example.com
    ProxyPass / http://127.0.0.1:82/
    ProxyPassReverse / http://127.0.0.1:82/
</VirtualHost>
```

 

# Start

Der Start der ersten drei Komponenten der easydb ist identisch zur einfachen Installation, siehe dort den Abschnitt  "[Start](/de/sysadmin/installation)".

Die beiden letzten Komponenten jedoch, `easydb-server` und `easydb-webfrontend`, müssen ein Mal für jede Ihrer Instanzen gestartet werden.

Hier der Start von `olymp`. Die gleichen Befehle dann für `atlantis`, allerdings mit `INSTANCE=atlantis` und `PORT=82`:

```bash
INSTANCE=olymp
PORT=81
BASEDIR=/srv/easydb/$INSTANCE

docker run -d -ti \
    --name easydb-server-$INSTANCE \
    --net easy5net \
    --volume=$BASEDIR/config:/config \
    --volume=$BASEDIR/easydb-server/var:/easydb-5/var \
    --volume=$BASEDIR/easydb-server/nginx-log:/var/log/nginx \
    docker.easydb.de/pf/server-$SOLUTION

docker run -d -ti \
    --name easydb-webfrontend-$INSTANCE \
    --net easy5net \
    --volume=$BASEDIR/config:/config \
    -p 127.0.0.1:$PORT:80 \
    docker.easydb.de/pf/webfrontend
```

Wir nehmen in diesem Beispiel `/srv/easydb` als [Datenablage](/de/sysadmin/installation). Bitte passen Sie dies an Ihre Gegebenheiten an.

 

# Stop

Angenommen Sie wollen beide Instanzen - atlantis und olymp - beenden und ebenso alle gemeinsamen Komponenten der easydb:

```bash
docker stop  easydb-webfrontend-olymp
docker rm -v easydb-webfrontend-olymp

docker stop  easydb-server-olymp
docker rm -v easydb-server-olymp

docker stop  easydb-webfrontend-atlantis
docker rm -v easydb-webfrontend-atlantis

docker stop  easydb-server-atlantis
docker rm -v easydb-server-atlantis

docker stop  easydb-eas
docker rm -v easydb-eas

docker stop  easydb-elasticsearch
docker rm -v easydb-elasticsearch

docker stop  easydb-pgsql
docker rm -v easydb-pgsql
```

 

# Sicherung per pg\_dump

Die Datenbank `eas` wird [normal](../betrieb) gesichert. Dadurch ergibt sich im Beispiel olymp und atlantis:

```bash
docker exec -i -t easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/olymp.pgdump olymp

docker exec -i -t easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/atlantis.pgdump atlantis

docker exec -i -t easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/eas.pgdump eas
```

## Wiederherstellung einer Sicherung die mit pg\_dump gemacht wurde

Da in der Datenbank `eas` Daten zu allen Instanzen gespeichert werden empfehlen wir die gemeinsame Herstellung aller Datenbanken aus der selben Sicherung.

Am Beispiel von zwei Instanzen namens olymp und atlantis:

```bash
docker exec -i -t easydb-pgsql psql -U postgres -c 'DROP   DATABASE "eas"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'DROP   DATABASE "olymp"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'DROP   DATABASE "atlantis"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'CREATE DATABASE "eas"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'CREATE DATABASE "olymp"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'CREATE DATABASE "atlantis"'
docker exec -i -t easydb-pgsql pg_restore -U postgres -v -d eas      /backup/eas.pgdump
docker exec -i -t easydb-pgsql pg_restore -U postgres -v -d olymp    /backup/olymp.pgdump
docker exec -i -t easydb-pgsql pg_restore -U postgres -v -d atlantis /backup/atlantis.pgdump
```



