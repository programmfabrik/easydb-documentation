# Installation eines Plugins

Die easydb bringt eine Reihe von Plugins bereits mit, die so genannten Base-Plugins.

Davon abgesehen können Sie Plugins selbst entwickeln oder solche Plugins aus anderen Quellen installieren. Die Installation eines solchen Plugins beschreiben wir weiter unten bei [Extension-Plugin](#extension-plugin).

Die Plugins unter https://github.com/programmfabrik funktionieren sowohl als Base-Plugin als auch als Extension-Plugin. Wir empfehlen diese als Base-Plugin einzubinden, denn das ist deutlich einfacher.

## Liste der aktiven Plugins

Welche Plugins derzeit aktiv sind sehen Sie im Web-Frontend der easydb, ganz links über den "i"(nfo) Knopf und dann mit dessen Unterpunkt "Über".

---

# Base-Plugin

Base-Plugins sind bereits bei der easydb-Installation mit installiert worden und müssen daher nur noch aktiviert werden.

Ergänzen Sie, soweit die Zeilen fehlen, in die Konfigurationsdatei `config/easydb5-master.yml`, deren [Speicherort](/sysadmin/installation/installation.html#datenablage-bestimmen) bei der Installation festgelegt wurde:

    easydb-server:
      plugins:
        enabled+:
          - base.custom-data-type-link
          - base.custom-data-type-geonames

... für z.B. die beiden Plugins custom-data-type-link und custom-data-type-geonames.

Danach sollten Sie noch die easydb neu starten.

---

# Extension-Plugin

Extension-Plugins werden typischerweise von Entwicklern außerhalb der Programmfabrik erstellt, und auch nicht im Auftrag der Programmfabrik sondern als Erweiterung nach eigenen Zielsetzungen.

Daher kann die Installation von dem hier gezeigten Fall abweichen. Wenden Sie sich dann an den jeweiligen Entwickler für weitere Informationen.

Für das Beispiel "custom-data-type-geonames" richten Sie Ihre Fragen bitte an den sogenannten Issue-Tracker des Plugins: https://github.com/programmfabrik/easydb-custom-data-type-geonames/issues

Am Beispiel easydb-custom-data-type-geonames:

Ergänzen Sie, soweit die Zeilen fehlen, in die Konfigurationsdatei `config/easydb5-master.yml`, deren [Speicherort](/sysadmin/installation/installation.html#datenablage-bestimmen) bei der Installation festgelegt wurde:

    easydb-server:
      extension:
        plugins:
          - name: easydb-custom-data-type-geonames
            file: plugin/easydb-custom-data-type-geonames/CustomDataTypeGeonames.config.yml
      plugins:
        enabled+:
          - extension.easydb-custom-data-type-geonames

Befehle zur Installation: (Auszuführen in der [Datenablage](/sysadmin/installation/installation.html#datenablage-bestimmen), also dem Verzeichnis dessen Ort bei der Installation festgelegt wurde)

    mkdir config/plugin
    cd config/plugin
    git clone https://github.com/programmfabrik/easydb-custom-data-type-geonames easydb-custom-data-type-geonames
    cd easydb-custom-data-type-geonames
    git submodule init
    git submodule update
    make

Falls "make" per Fehlermeldung anzeigt, dass das Programm "coffee" benötigt wird aber fehlt, dann installieren Sie dies bitte in der Version 1.10 . Beispielhaft hier:

~~~~
apt-get install npm
npm install -g coffee-script@1.10
cd /usr/bin
ln -s nodejs node
~~~~

Als letztes sollten Sie noch die easydb neu starten.

---

# Solution-Plugin

Falls wir ein Plugin für Sie entwickeln, dann liefern wir dieses evtl. als Solution-Plugin aus.

In diesem Fall erstellen wir auch Dokumentation, die auf das Plugin zugeschnitten ist. Den Link zu dieser Dokumentation bekommen Sie dann von uns.

---

# CMS Plugins

## Wordpress Plugin {#wordpressplugin}

Plugin für den Transfer von Mediendateien zu Wordpress CMS [Wordpress Plugin](/webfrontend/datamanagement/features/plugins/plugins.html#wordpress).

Aktuell unterstützt dieses Plugin das Erstellen von neuen Medien als auch das Aktualisieren von dazugehörigen Metadaten. Wenn ein neuer Datensatz in easydb angelegt wird, wird auch ein neues in Wordpress angelegt. Es existiert keine Unterstützung für das Löschen von Medien.

### Voraussetzungen

* Unterstützung ab Wordpress 4.7
* Für die Verwendung im Frontend muss die JSON-Rest-API aktiviert (ist Default) und die Authentifizierung eingerichtet sein

### Setup (Wordpress)

* easydb unterstützt **JSON Basic Authentication** und **WP REST API - OAuth 1.0a Server**
 * Plugin(s) für Authentifizierung installieren
 * Plugin(s) für Authentifizierung einschalten
 * Benutzer für das oauth-Plugin einrichten. Callback URL: http:// **easydb-server** /api/v1/plugin/base/easydb-wordpress-plugin/oauth1

### Plugin in easydb aktivieren

* Stellen Sie sicher, dass das Plugin korrekt installiert ist (Pfade relativ zum .yml angegeben):

Fügen Sie die folgenden Zeilen zu Ihrer server.yml hinzu:

```
base:
  plugins+:
    - name: wordpress
      file: easydb-wordpress-plugin/wordpress.yml

plugins:
  enabled+:
    - base.sso
    - base.simple-example
    - base.wordpress
```

## Falcon.io Plugin {#falconio}

Plugin für den Transfer von Mediendateien zum Falcon.io CMS [Falcon.io Plugin](/webfrontend/datamanagement/features/plugins/plugins.html#falconio).

Aktuell unterstützt dieses Plugin das Senden von ausgewählten Medien nach Falcon.io. Aktualisieren wird nicht unterstüzt. Es werden statt dessen neue Dateien in Falcon.io angelegt.

### Setup (Falcon.io)

* Es wird en registrierter Falcon.io-Account benötigt
* Es muss mindestens ein  **Channel** registriert werden, so dass das Feature "Content Pool" benutzt werden kann
* Einen API-Key für die easydb generieren - under Settings->Integration & APIs

### Plugin in easydb aktivieren

* Stellen Sie sicher, dass das Plugin korrekt installiert ist (Pfade relativ zum .yml angegeben):

Fügen Sie die folgenden Zeilen zu Ihrer server.yml hinzu:

```
base:
  plugins+:
    - name: falconio
      file: easydb-falconio-plugin/falconio.yml

plugins:
  enabled+:
    - base.falconio
```








