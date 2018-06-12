# Hotfolder einrichten

Der Hotfolder der easydb ist ein Verzeichnis, in dem abgelegte Dateien automatisch vereinnahmt werden. Basis bilden die [Arbeitsmappen](/webfrontend/datamanagement/search/quickaccess/collection/collection.html), die entsprechend konfiguriert werden können. Auf der administrativen Seite sind folgende Einstellungen vorzunehmen:

## Freigabe des Arbeitsverzeichnisses

Das Arbeitsverzeichnis, in dem für jede freigegebene Mappe ein Unterverzeichnis angelegt wird, muss mit Betriebssystemmitteln freigegeben werden. Im Normalfall erfolgt das über WebDAV, andere Optionen wie FTP oder SMB sind prinzipiell möglich, werden hier aber nicht beschrieben.

### Konfiguration von WebDAV

Für WebDAV ist ein vor die Docker-Container geschalteter Apache-Webserver notwendig, wie er auch schon bei der [Einrichtung von HTTPS](/sysadmin/konfiguration/https/https.html) beschrieben ist.

Zuerst sollte das passende Apache-Modul aktiviert werden:
~~~~
# a2enmod dav_fs
~~~~

Das Hotfolder-Verzeichnis muss existieren und für den Webserver schreibbar sein, das kann z.B. sichergestellt werden, wenn das Verzeichnis dem `www-data`-Nutzer gehört:
~~~~
# mkdir -p /media/hotfolder
# chown www-data. /media/hotfolder
~~~~

Folgende Einstellungen sind zusätzlich notwendig, das Arbeitsverzeichnis (`/media/hotfolder` im Beispiel) ist an die lokalen Gegebenheiten anzupassen. Einige Einstellungen im `VirtualHost`-Eintrag wurden aus Gründen der Übersichtlichkeit weggelassen.

~~~~
<VirtualHost *:443>
	AliasMatch ^/upload(.*)$ /media/upload$1
	<Location /upload>
		ProxyPass "!"
		Require all granted
		DAV on
		Options -MultiViews
		ErrorDocument 404 "Not Found"
		ErrorDocument 500 "Internal Server Error"
		ErrorDocument 502 "Bad Gateway"
	</Location>

	ProxyPass / http://127.0.0.1:80/
	ProxyPassReverse / http://127.0.0.1:80/
	…
</VirtualHost>
~~~~

## Konfiguration des easydb-Servers

Der easydb-Server legt für alle freigegebenen Mappen im o.g. Arbeitsverzeichnis entsprechende Unterverzeichnisse an. Außerdem ist die WebDAV-URL (bzw. andere URLs für andere, hier nicht dokumentierte Zugriffswege) im Frontend zugänglich, deren Basis muss konfiguriert werden (`easydb5-master.yml`). Da der Hotfolder als Plugin ausgeführt wird, muss dieses Plugin noch aktiviert werden.

~~~~
easydb-server:
  hotfolder:
    enabled: true
    urls:
      - type: windows_webdav
        url: \\easydb.example.com@SSL\upload\collection
        separator: \
      - type: webdav_http
        urls: https://easydb.example.com/upload/collection
        separator: /
  plugins:
    enabled+:
      - base.
~~~~

Die oben genannte URL ist die unter Windows gebräuchliche Form der WebDAV-URLs, unter der Annahme, dass die easydb unter `https://easydb.example.com` erreichbar ist.

Das Hotfolder-Arbeitsverzeichnis (`/media/hotfolder`) muss noch im `easydb-server`-Container unter `/hotfolder` verfügbar gemacht werden, das geschieht im [Start-Skript](/sysadmin/installation/installation.html):

~~~~
docker run -d -ti \
	--name easydb-server \
	…
	--volume=/media/hotfolder:/hotfolder \
	docker.easydb.de:5000/pf/server-$SOLUTION
~~~~
