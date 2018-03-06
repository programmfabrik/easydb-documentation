# Betrieb
Zur **Aktualisierung** der easydb-Software dienen ein weiteres Mal die Befehle des Abschnitts "[easydb auf den Server laden](/sysadmin/installation/installation.html#easydb-auf-den-server-laden)" der Installation.

Die aktuellere Version wird allerdings erst benutzt, nachdem die easydb gestoppt und wieder gestartet wurde.

Um die easydb zu **stoppen** verwenden Sie folgende Befehle:

~~~~
    docker stop  easydb-webfrontend
    docker rm -v easydb-webfrontend

    docker stop  easydb-server
    docker rm -v easydb-server

    docker stop  easydb-fylr
    docker rm -v easydb-fylr

    docker stop  easydb-eas
    docker rm -v easydb-eas

    docker stop  easydb-elasticsearch
    docker rm -v easydb-elasticsearch

    docker stop  easydb-pgsql
    docker rm -v easydb-pgsql
~~~~

Wir empfehlen auch hier, dass Sie diese Befehle in das Init-System Ihres Servers integrieren, zumindest für den automatisierten Dauerbetrieb.

&nbsp;

Falls Sie auf einem Server mehr als eine easydb betreiben, beachten Sie bitte die Ergänzungen im Kapitel [Instanziierung](/sysadmin/instances/instances.html#stop).

&nbsp;

Die Befehle zum **Starten** der easydb sind im Abschnitt  "[Start](/sysadmin/installation/installation.html#start)" der Installation aufgeführt.

&nbsp;

# Status

Welche Komponenten der easydb gerade laufen können sie u.a. anzeigen lassen mit `docker ps`. Hier eine Beispiel-Anzeige während alle Komponenten laufen:

~~~~
CONTAINER ID        IMAGE                                       COMMAND             CREATED             STATUS              PORTS                   NAMES
efe480718a0e        docker.easydb.de:5000/pf/webfrontend        "/startup.sh"       9 days ago          Up 9 days           0.0.0.0:80->80/tcp      easydb-webfrontend
cdfe24889c0c        docker.easydb.de:5000/pf/server-base        "/startup.sh"       9 days ago          Up 9 days           80/tcp, 3451-3452/tcp   easydb-server
2a77e387f88a        docker.easydb.de:5000/pf/fylr               "/startup.sh"       2 days ago          Up 2 days           4000/tcp                easydb-fylr
8a17a2a5ea26        docker.easydb.de:5000/pf/eas                "/startup.sh"       10 weeks ago        Up 10 weeks         80/tcp                  easydb-eas
19bf53e50287        docker.easydb.de:5000/pf/elasticsearch      "/startup.sh"       10 weeks ago        Up 10 weeks         9200/tcp, 9300/tcp      easydb-elasticsearch
1a51017ae36e        docker.easydb.de:5000/pf/postgresql         "/startup.sh"       10 weeks ago        Up 10 weeks         5432/tcp                easydb-pgsql
~~~~

Um auch ruhende Komponenten anzuzeigen verwenden Sie `docker ps -a`.

&nbsp;

## Überwachung

Zum Überwachen Ihrer easydb können Sie unser freies [Plugin](https://github.com/programmfabrik/check-easydb5) nutzen, mit Nagios oder Icinga.

&nbsp;

# Sicherungskopien

## Sicherung der Assets
Sichern Sie das Verzeichnis welches Sie bei der [Installation](/sysadmin/installation/installation.html#datenablage-bestimmen) zur Datenablage bestimmt haben.

Damit haben Sie eigentlich alles gesichert, nicht zuletzt Ihre Assets.

Doch die Informationen _über_ die Assets brauchen besondere Sorgfalt - sie sind in PostgreSQL-Datenbanken gespeichert, die sich auch während der Sicherung ändern könnten.

## Sicherung der Datenbanken

Die easydb verwendet intern zwei PostgreSQL-Datenbanken. Um diese konsistent zu sichern haben Sie zwei Möglichkeiten:

_Entweder - sehr einfach:_

__A.__ Die easydb während der Sicherung der Datenablage stoppen.

_Oder - unsere Empfehlung:_

__B.__ Verwenden Sie zur Sicherung das PostgreSQL-eigene Werkzeug pg_dump.

pg_dump sichert in einem Format was auch nach Software-Aktualisierungen noch kompatibel ist.

Auch der Platzbedarf ist geringer als bei Methode A - sofern Sie nun `pgsql/var` bei der Sicherung der Datenablage aussparen.

## Sicherung per pg_dump

~~~~
DATABASE=easydb

docker exec -i -t easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/$DATABASE.pgdump $DATABASE

docker exec -i -t easydb-pgsql pg_dump -U postgres -v -Fc -f /backup/eas.pgdump eas
~~~~

Anmerkungen:

- Die easydb kann und sollte während dieser Sicherungsmethode laufen. Die Komponente "easydb-pgsql" muss sogar laufen.
- Sie finden die Backup-Dateien danach im Unterverzeichnis `pgsql/backup` der Datenablage, deren Speicherort Sie bei der [Installation](/sysadmin/installation/installation.html) festgelegt haben.
- Falls Sie zuerst pg_dump ausführen und danach erst die Datenablage sichern dann erfassen sie somit auch diese pg_dump-Dateien.
- Evtl. erhalten Sie von uns den Namen Ihrer Datenbank. Ansonsten verwenden Sie den Standardwert "easydb".
- Für den automatisierten Betrieb entfernen Sie die Optionen `-i -t`.

&nbsp;


# Wiederherstellung einer Sicherungskopie

1. Beenden Sie die easydb. (Beschrieben [oben](#betrieb) auf dieser Seite)

2. Ersetzen Sie den Inhalt der Datenablage durch die Sicherungskopie. Die Datenablage haben Sie bei der [Installation](/sysadmin/installation/installation.html#datenablage-bestimmen) festgelegt.

3. Starten Sie den ersten Teil der easydb - die Komponente "easydb-pgsql". Dazu dient der erste Startbefehl m Abschnitt "[Start](/sysadmin/installation/installation.html#start)" der Installation.

4. Falls vorhanden nutzen Sie nun die Sicherung, die per pg_dump erstellt wurde:

~~~~
DATABASE=easydb
docker exec -i -t easydb-pgsql psql -U postgres -c 'DROP   DATABASE "eas"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'DROP   DATABASE "'$DATABASE'"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'CREATE DATABASE "eas"'
docker exec -i -t easydb-pgsql psql -U postgres -c 'CREATE DATABASE "'$DATABASE'"'
docker exec -i -t easydb-pgsql pg_restore -U postgres -v -d eas    /backup/eas.pgdump
docker exec -i -t easydb-pgsql pg_restore -U postgres -v -d $DATABASE /backup/$DATABASE.pgdump
~~~~

5. Starten Sie nun die restlichen vier Komponenten. Dazu dienen die vier restlichen Startbefehle des Abschnitts "[Start](/sysadmin/installation/installation.html#start)".

Anmerkungen:

- Evtl. erhalten Sie von uns den Namen Ihrer Datenbank. Ansonsten verwenden Sie den Standardwert "easydb".
- Falls Sie die bei Ihnen benutzten Datenbanknamen anzeigen lassen wollen verweden Sie:

~~~~
docker exec -i -t easydb-pgsql psql -U postgres -l
~~~~

&nbsp;

