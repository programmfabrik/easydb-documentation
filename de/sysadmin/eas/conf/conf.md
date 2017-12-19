> Die Pfadangaben beziehen sich auf Pfade im Container, nicht auf Pfade direkt auf Ihrem Server, der den docker-Container ausführt.

Konfigurationsvariablen
=======================

Die Konfigurationsdatei des easydb-Asset-Servers liegt unter
/etc/opt/easydb/eas/easydb-asset-server.conf.

Einstellungen für den Start und die Umgebung des EAS sind in
[/etc/default/easydb-asset-server](../initconf/initconf.html).

Systemeinstellungen
===================

Anzahl der Worker
-----------------

### EAS\_NUM\_WORKERS

Der EAS kann gleichzeitig mehrere sogenannte Worker-Prozesse starten, um
die verfügbaren Ressourcen gut auszunutzen. Es sollten jedoch nicht mehr
Worker gestartet werden, als der Server Prozessorkerne hat, besser noch
weniger, um dem EAS-Service und der easydb genug Ressourcen zu lassen.

Worker-Prozesse sind für die eigentliche Berechnung der
Vorschauversionen und anderer potentiell zeitintensiver Arbeiten wie dem
Erstellen von ZIPs und PowerPoint-Präsentationen zuständig.

    EAS_NUM_WORKERS=1

Die Variable “EAS\_NUM\_SOFFICE” (unten) muss immer auf einen höheren
Wert gesetzt werden als EAS\_NUM\_WORKERS.

Anzahl der EAS-Service-Prozesse (ab Version 4.2)
------------------------------------------------

### EAS_NUM_SERVICES

Die Service-Prozesse nehmen Anfragen von der easydb entgegen und
beantworten diese entweder direkt oder legen Arbeitsaufträge für die
Worker-Prozesse in die Warteschlange. Es sollten immer ausreichend
Service-Prozesse zur Verfügung stehen, da sonst die auch die Interaktion
mit der easydb blockiert wird. Für viele Installation ist der
Vorgabewert von 5 ausreichend, zumal Verbindungen erst abgelehnt werden,
wenn die Anzahl der gleichzeitigen Verbindungen eine gewisse Grenze
überschreitet (`3 × n + 10`).

    EAS_NUM_SERVICES=5

FastCGI-Socket für EAS-Service (ab Version 4.2)
-----------------------------------------------

### EAS_FCGI_SOCKET

    EAS_FCGI_SOCKET=/var/run/easydb/fcgi-socket

Anzahl der OpenOffice.org-Services (ab Version 4.2)
---------------------------------------------------

### EAS_NUM_SOFFICE

    EAS_NUM_SOFFICE=2

Basisport für OpenOffice.org-Services (ab Version 4.2)
------------------------------------------------------

### EAS_SOFFICE_BASEPORT

    EAS_SOFFICE_BASEPORT=2002

Benutzerkonfiguration
---------------------

### EAS_EUID

### EAS_EGID

Der EAS-Worker ändert beim Starten seinen Nutzer und seine Gruppe, um
die Aufgaben mit weniger Rechten zu erfüllen. Momentan muss das der
gleiche Nutzer sein, mit dem auch der EAS-Service, also der
Apache-Webserver läuft. Unter Debian ist das der Nutzer `www-data` mit
der Gruppe `www-data`, UID und GID sind `33`.

    EAS_EUID=33
    EAS_EGID=33

Datenbank-Konfiguration
=======================

### EAS\_PG\_DSN

Der DSN (Data Source Name) bestimmt die Verbindung zur
PostgreSQL-Datenbank. Folgende Werte sind (leerzeichengetrennt) möglich:

-   `host`: Hostname des Datenbank-Servers oder lokales
    Socket-Verzeichnis
-   `port`: Port des DB-Servers, auch für Socket-Verbindung notwendig
-   `user`: Benutzername
-   `dbname`: Name der Datenbank
-   `password`: (optional) Passwort bei entsprechender Konfiguration des
    DB-Servers

<!-- -->

    EAS_PG_DSN=host=/var/run/postgresql port=5432 user=postgres dbname=easydb

Verzeichniseinstellungen
========================

Einschränkungen der Quellverzeichnisse
--------------------------------------

### EAS\_SAFE\_PATHS

Hier kann eingeschränkt werden, aus welchen Verzeichnissen der EAS
Assets vereinnahmen darf. Aus Sicherheitsgründen sollte diese
Einstellung natürlich möglichst restriktiv sein, muss aber auf jeden
Fall das Upload-Verzeichnis der easydb (eine PHP-Einstellung) umfassen.

    EAS_SAFE_PATHS=/var:/home:/tmp

Protokoll-Verzeichnis
---------------------

### EAS\_LOG\_DIR

Alle Meldungen des EAS werden in diesem Verzeichnis abgelegt. Sollten
sehr früh Warnmeldungen und Fehler auszugeben sein, können diese auch in
`/tmp` liegen.

    EAS_LOG_DIR=/var/opt/easydb/log/eas

Verzeichnis für Laufzeitdaten
-----------------------------

### EAS\_VAR\_DIR

In dieses Verzeichnis legt der EAS-Worker Statusinformationen und
PID-Dateien ab.

    EAS_VAR_DIR=/var/run/easydb

Verzeichnis für temporäre Dateien
---------------------------------

### EAS\_TMP\_DIR

Unterhalb dieses Verzeichnisses werden temporäre Dateien, die bei der
Erstellung von Versionen notwendig sind, abgelegt. Die Vorgabe ist
`/tmp`, es wird jeweils ein Verzeichnis für jede Aufgabe angelegt und
nach Abschluss wieder gelöscht.

    # EAS_TMP_DIR=/tmp

Verzeichnis für temporäre Dateien des Zoomers (ab EAS 4.2.36)
-------------------------------------------------------------

### EAS\_ZOOMER\_TMP\_DIR

Der easydb-Zoomer legt unkomprimierte Bilder für den schnellen Zugriff temporär ab. Dies geschieht normalerweise in einem Verzeichnis namens “zoomer” im temporären Verzeichnis ("/tmp" bzw. `EAS_TMP_DIR`). In diesem Verzeichnis wird bei [aktiviertem Janitor](#Janitor) automatisch aufgeräumt, es sollte also ausschließlich für diesen Zweck verwendet werden.

    EAS_ZOOMER_TMP_DIR=/var/tmp/zoomer-eas

Basisverzeichnis für Partitionen
--------------------------------

### EAS\_PARTITION\_BASE\_DIR

Dieses Verzeichnis enthält symbolische Links auf die eigentlichen EAS-Partitionsverzeichnisse. Die Links werden durch die Datenbank-ID der Partition bestimmt und vom EAS-Worker selbst verwaltet. Ein gemeinsames Verzeichnis ist notwendig, um den Konfigurationsaufwand in Grenzen zu halten, da der Apache die Dateien in den einzelnen Partitionen ausliefern muss und diese dem Webserver nicht einzeln bekannt sind.

    EAS_PARTITION_BASE_DIR=/var/opt/easydb/lib/eas/partitions

Mindestgröße für Partitionen
----------------------------

### EAS\_PARTITION\_MIN\_FREE {#eas-partition-min-free}

Stellt der EAS fest, dass die Mindestgröße in Bytes auf einer EAS-Partition unterschritten wird, wird diese deaktiviert. Der Standardwert beträgt 1 Gigabyte.

    # EAS_PARTITION_MIN_FREE=1073741824

Code-Verzeichnis
----------------

### EAS\_EXEC\_DIR

Der Code aus diesem Verzeichnis wird ausgeführt. Im Normalfall sollte diese Einstellung nicht geändert werden.

    EAS_EXEC_DIR=/opt/easydb/eas

Automatische EAS-Migration
==========================

### EAS\_MIGRATE\_ASSETS

### EAS\_ORIGINAL\_STORE

### EAS\_VERSIONS\_STORE

Der EAS kann Assets vom alten, dateibasierten Typ während des Zugriffs in die Datenbank migrieren. Damit ist eine schrittweise Umstellung auf das neue System möglich. Standardmäßig ist dieses Verhalten aber deaktiviert, da es bei vielen Anfragen auf nicht vorhandene Assets zu Leistungseinbußen kommen kann.

    # EAS_MIGRATE_ASSETS=1
    # EAS_ORIGINAL_STORE=/home/eas40/orig
    # EAS_VERSIONS_STORE=/home/eas40/dest


E-Mail-Konfiguration
====================

### EAS\_EMAIL\_SMTP\_SERVER

### EAS\_EMAIL\_FROM\_ADDRESS

### EAS\_EMAIL\_ENVELOPE\_SENDER

Zum E-Mail-Versand von Assets ist ein funktionierender SMTP-Server nötig. Momentan können der Servername und die `From:`-Adresse der ausgehenden E-Mails konfiguriert werden.

    EAS_EMAIL_SMTP_SERVER=localhost
    EAS_EMAIL_FROM_ADDRESS=root@localhost

Zusätzlich kann ab **EAS 4.2.30** noch die Envelope-Sender-Adresse angegeben werden. Ist diese nicht gesetzt, wird auf `EAS_EMAIL_FROM_ADDRESS` zurückgegriffen.

    EAS_EMAIL_ENVELOPE_SENDER=admin@example.com

Zoomer-Konfiguration (ab EAS 4.2.36)
====================================

Der EAS enthält ab **Version 4.2.36** eine neue Implementierung für den Zoomer.

Janitor-Einstellungen des Zoomers
---------------------------------

### EAS\_ZOOMER\_MAX\_CACHE\_TIME

### EAS\_ZOOMER\_MIN\_FREE\_SPACE

Der EAS-Janitor räumt regelmäßig die temporären Dateien des Zoomers auf
(siehe dazu auch `EAS_ZOOMER_TMP_DIR`). Einige Parameter können an die
zur Verfügung stehenden Ressourcen angepasst werden:

Das maximale Alter der temporären Dateien, die Vorgabe ist hier eine
Stunde.

    EAS_ZOOMER_MAX_CACHE_TIME=2D

Es können folgende Suffixe für Zeiteinheiten verwendet werden: s
(Sekunden), m (Minuten), h (Stunden), D (Tage).

Zusätzlich werden die ältesten temporären Dateien gelöscht, bis der
verfügbare Platz auf dem Laufwerk wieder einen gewissen Wert erreicht,
sofern notwendig. Die Vorgabe ist hier ein GB.

    EAS_ZOOMER_MIN_FREE_SPACE=24G

Verfügbare Suffixe sind K, M, G, T für die entsprechenden
Multiplikatoren für Bytes (1K steht für 1024 Bytes).

Da der Janitor standardmäßig nur alle 60 Minuten läuft, kann es trotzdem
sein, dass der verfügbare Platz unterschritten wird, der temporäre Platz
und der Speicher-Grenzwert sollten also großzügig dimensioniert werden.

weitere Parameter
=================

### EAS\_JANITOR

Der Aufräum-Prozess des EAS kann deaktiviert werden, standardmäßig ist
dieser aktiv. Dazu ist folgende Option zu setzen:

    EAS_JANITOR=false

### EAS\_JSON\_INDENT

Das Datenaustauschformat des EAS ist hauptsächlich
JSON (JavaScript Object Notation). Ist diese Option aktiv (die
Voreinstellung), so werden die Daten in formatierter, besser lesbarer
Form ausgeben.

    EAS_JSON_INDENT=1

### EAS\_EXIFTOOL\_PATH

Exiftool wird als zentraler Bestandteil für die Metadatenbehandlung
benötigt. Da die Distributionsversion dieser Software teilweise zu alt
ist, liefert die easydb eine neuere Version aus, deren Pfad hier
konfiguriert ist. Normalerweise sollte diese Einstellung nicht geändert
werden.

    EAS_EXIFTOOL_PATH=/opt/easydb/common/exiftool/exiftool

### EAS\_CONVERT\_LIMIT\_\*

Für ImageMagick-Aufrufe können mit `EAS_CONVERT_LIMIT_*` diverse
Beschränkungen angegeben werden (siehe [ImageMagick-Documentation zu
-limit](http://www.imagemagick.org/script/command-line-options.php#limit)),
z.B.:

    EAS_CONVERT_LIMIT_THREAD=1
    EAS_CONVERT_LIMIT_MAP=512MB

### EAS\_SOFFICE\_MAX\_WAIT (ab EAS 4.2.48.7)

Maximale Wartezeit auf Office-Prozesse in Sekunden. Die Vorgabe sind 30
Minuten. Ist die Zeit abgelaufen, werden alle Office-Prozesse
abgebrochen und neugestartet.

    EAS_SOFFICE_MAX_WAIT=900

&nbsp;

> Die Pfadangaben beziehen sich auf Pfade im Container, nicht auf Pfade direkt auf Ihrem Server, der den docker-Container ausführt.
