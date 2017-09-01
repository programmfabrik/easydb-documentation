
#  Installation des easydb-Asset-Servers

##  Paketinstallation

Die Installation der nötigen Software beschränkt sich nach Eintragen der Installationsquelle in `/etc/apt/sources.list` auf folgende Kommandos:

~~~
apt-get update
apt-get install easydb-asset-server
~~~


Durch die Abhängigkeiten des Pakets werden alle vom EAS benötigten Programme installiert, das umfasst vor allem ImageMagick (Bildverarbeitung), MPlayer/FFmpeg (Videoerkennung und -umrechnung), OpenOffice.org (Office-Konvertierung), den PostgreSQL-Datenbank-Server und den Apache-Webserver.


Datenbank
=========

Der EAS benötigt eine PostgreSQL-Datenbank.
Der EAS kann zusammen mit der easydb in einer Datenbank installiert werden, denn EAS
benutzt nur das Schema `eas`. Typisch ist jedoch eine eigene Datenbank.

Angebunden wird die Datenbank im EAS über die Variable `EAS_PG_DSN` in der
[Konfigurationsdatei](/sysadmin/eas/conf/conf.md).

Anlegen der EAS-Datenbank
-------------------------

Der EAS benötigt eine existierende Datenbank, das Anlegen und Pflegen
des Schemas geschieht automatisch. Für eine Standardinstallation
empfiehlt sich folgendes Kommando (erstellt eine leere Datenbank mit dem Namen `easydb` als Benutzer `postgres`):

createdb -U postgres easydb

&nbsp;

Konfiguration der Partitionen
=============================

Standardmäßig wird der EAS mit 2 [Partitionen](/sysadmin/eas/partitions/partitions.md)
ausgeliefert, die Assets werden in `/var/opt/easydb/lib/eas/assets/orig`
(hochgeladene Assets) und `/var/opt/easydb/lib/eas/assets/dest`
(erstellte Versionen) abgelegt. Diese Einstellung kann momentan nur in
der Datenbank geändert werden.

&nbsp;

EAS-Worker
==========

Zur asynchronen Berechnung der Asset-Versionen dient der EAS-Worker.
Dieser besteht aus einem oder mehreren Prozessen, die mit dem Skript
`/etc/init.d/easydb-asset-server` verwaltet werden.

Für eine genaue Analyse kann es hilfreich sein, den Worker nur mit

/etc/init.d/easydb-asset-server debug

aufzurufen, um evtl. Konfigurations- oder Installationsprobleme leichter
zu sehen. Hierbei wird ein Worker im Vordergrund gestartet, dieser kann
mit `Strg+C` wieder abgebrochen werden.

Der aktuelle Zustand der Worker-Prozesse kann mit

/etc/init.d/easydb-asset-server status

ermittelt werden. Dabei wird unter anderem die Zahl der erfolgreich und
fehlerhaft abgeschlossenen Aufträge angezeigt.

> Die Pfadangaben beziehen sich auf Pfade im Container, nicht auf Pfade direkt auf Ihrem Server, der den docker-Container ausführt.

&nbsp;

EAS-Service
===========

Zum Beantworten von Anfragen durch die easydb oder andere Dienste dient
der sogenannte EAS-Service. Dieser übernimmt Aufgaben die synchron
bearbeitet werden müssen.

Bereitgestellt wird eine Konfigurationsdatei, welche Makros für das
Apache-@mod_macro@-Modul bereitstellt. Diese Datei wird folgendermaßen
eingebunden:

Include /etc/opt/easydb/eas/apache-easydb-asset-server.inc

Die Makros sind zur Benutzung innerhalb einer `VirtualHost`-Definition
vorgesehen. Zwei Makros werden definiert: `EasydbAssetServer` und
`EasydbAssetServerAllowedHost`. Ersteres konfiguriert die
Basisverzeichnisse des EAS-Service und kann bei einer
Standardinstallation des EAS wie im Beispiel verwendet werden. Das
zweite Makro definiert die Hosts, die auf den EAS-Service zugreifen
dürfen. Hier muss die externe Adresse der easydb angegeben werden, auch
wenn die easydb und der EAS auf derselben Maschine laufen.

<VirtualHost eas.example.org>
Use EasydbAssetServer /opt/easydb/eas /var/opt/easydb/lib/eas/partitions /var/run/easydb/fcgi-socket
Use EasydbAssetServerAllowedHost 192.0.2.10
</VirtualHost>

Ab Version 4.2 des EAS hat `EasydbAssetServer` noch einen dritten
Parameter. Dieser bestimmt den Socket, über den der Apache-Webserver per
FastCGI auf den EAS-Service zugreift. Mit diesem Makro wird der Name des
Sockets dem Apache bekannt gemacht, der EAS erhält die Konfiguration
über den Parameter `EAS_FCGI_SOCKET` in der
[Konfigurationsdatei](../conf/conf.md) .

Soll der Zugriff von mehreren Hosts erlaubt sein, muss die Konfiguration
in etwa so aussehen:

<VirtualHost eas.example.org>
Use EasydbAssetServer /opt/easydb/eas /var/opt/easydb/lib/eas/partitions /var/run/easydb/fcgi-socket
Use EasydbAssetServerAllowedHost "192.0.2.10 192.0.2.11"
</VirtualHost>

> Die Pfadangaben beziehen sich auf Pfade im Container, nicht auf Pfade direkt auf Ihrem Server, der den docker-Container ausführt.

Einrichtung des EAS-Service für verschiedene virtuelle Hosts
------------------------------------------------------------

> HTTPS wird außerhalb von docker eingerichtet und nicht mit der hier beschriebenen Methode. Das folgende Beispiel soll nur die Erfordernisse des EAS in besonderen Konstellationen verdeutlichen.

Soll der EAS-Service über mehrere virtuelle Hosts verfügbar sein, werden
meist mehrere VirtualHost-Sektionen in der Apache-Konfiguration
verwendet.

Ab **Version 4.2.40** ist dies ohne Probleme mit dem Makro
`EasydbAssetServerExt` möglich. Zusätzich zu `EasydbAssetServer` muss
für jeden VirtualHost-Eintrag noch ein eindeutiger Bezeichner gewählt
werden (der 2. Parameter):

~~~~
<VirtualHost eas.example.org:80>
Use EasydbAssetServerExt /opt/easydb/eas "default" /var/opt/easydb/lib/eas/partitions /var/run/easydb/fcgi-socket
Use EasydbAssetServerAllowedHost 192.0.2.10
</VirtualHost>

<VirtualHost eas.example.org:443>
Use EasydbAssetServerExt /opt/easydb/eas "ssl" /var/opt/easydb/lib/eas/partitions /var/run/easydb/fcgi-socket
Use EasydbAssetServerAllowedHost 192.0.2.10
</VirtualHost>
~~~~

Die weiteren für SSL notwendigen Einstellungen wurden in den
VirtualHost-Beispielen der Übersichtlichkeit halber weggelassen.
Natürlich ist auch weiterhin eine Kombination der easydb und des EAS in
einem VirtualHost-Eintrag möglich.

Vor **Version 4.2.40** (Sie haben eine neuere Version) war das nur umständlich realisierbar, da der
erste Parameter des Makros `EasydbAssetServer` (der Pfad zum EAS) für
jeden VirtualHost-Eintrag eindeutig sein muss. In diesem Fall muss im
Dateisystem ein symbolischer Link auf `/opt/easydb/eas` erstellt werden
(z.B. mit dem Namen `eas-ssl`) und der erste Parameter für
`EasydbAssetServer` wäre dann `/opt/easydb/eas-ssl`.

Dieses Beispiel ist auch in folgendem Verzeichnis zu finden:

/etc/opt/easydb/eas/apache-easydb-asset-server-virtual-host.inc.example

> Die Pfadangaben beziehen sich auf Pfade im Container, nicht auf Pfade direkt auf Ihrem Server, der den docker-Container ausführt.

&nbsp;

Freie Software
==============

Viele Aufgaben des EAS werden mit quell-offener freier Software durchgeführt,
vor allem mit ImageMagick (Bildverarbeitung), MPlayer/FFmpeg (Videoerkennung und -umrechnung),
OpenOffice.org (Office-Konvertierung), den PostgreSQL-Datenbank-Server und Apache-Webserver.
