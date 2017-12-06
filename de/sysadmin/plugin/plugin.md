# Installation eines Plugins

Die easydb bringt eine Reihe von Plugins bereits mit, die so genannten Base-Plugins.

Davon abgesehen können Sie Plugins von z.B. https://github.com/programmfabrik laden oder selbst entwickeln. Die Installation eines solchen Plugins beschreiben wir weiter unten bei [Extension-Plugin](#extension-plugin).

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
          - base.custom-data-type-gnd

... für z.B. die beiden Plugins custom-data-type-link und custom-data-type-gnd.

Danach sollten Sie noch die easydb neu starten.

---

# Extension-Plugin

Am Beispiel easydb-custom-data-type-geonames:

Ergänzen Sie, soweit die Zeilen fehlen, in die Konfigurationsdatei `config/easydb5-master.yml`, deren [Speicherort](/sysadmin/installation/installation.html#datenablage-bestimmen) bei der Installation festgelegt wurde:

    easydb-server:
      extension:
        plugins:
          - name: easydb-custom-data-type-geonames
            file: plugin/easydb-custom-data-type-gnd/CustomDataTypeGeonames.config.yml
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

Als letztes sollten Sie noch die easydb neu starten.

## Bei Problemen

Bitte beachten Sie dass Probleme mit Extension-Plugins vom Entwickler des Plugins zu beantworten sind. Richten Sie Ihre Fragen daher bitte an den sogenannten Issue-Tracker des Plugins. Für das Beispiel easydb-custom-data-type-geonames wäre das: https://github.com/programmfabrik/easydb-custom-data-type-geonames/issues

---

# Solution-Plugin

Falls wir ein Plugin für Sie entwickeln, dann liefern wir dieses evtl. als Solution-Plugin aus.

In diesem Fall erstellen wir auch Dokumentation, die auf das Plugin zugeschnitten ist. Den Link zu dieser Dokumentation bekommen Sie dann von uns.

---

# CMS Plugins

## Wordpress Plugin

Plugin für den Transfer von Mediendateien zu Wordpress CMS [Wordpress Plugin](../../datamanagement/features/plugins/plugins.html#wordpress). 

Aktuell unterstützt dieses Plugin das Erstellen von neuen Medien als auch das Aktualisieren von dazugehörigen Metadaten. Wenn ein neuer Datensatz in easydb angelegt wird, wird auch ein neues in Wordpress angelegt. Es existiert keine Unterstützung für das Löschen von Medien.

### Voraussetzungen

* Unterstützung ab Wordpress 4.7
* Für die Verwendung im Frontend muss die JSON-Rest-API aktiviert (ist Default) und die Authentifizierung eingerichtet sein

### Setup (Wordpress)

* easydb unterstützt **JSON Basic Authentication** und **WP REST API - OAuth 1.0a Server**
 * Plugin(s) für Authentifizierung installieren
 * Plugin(s) für Authentifizierung einschalten
 * Benutzer für das oauth-Plugin einrichten. Callback URL: http://**easydb-server**/api/v1/plugin/base/easydb-wordpress-plugin/oauth1

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

(siehe auch webfrontend/administration/wpplugin/wpplugin.html)

#### HTTP-Authentifizierung

Verbinden Sie die Wordpress Instanz mit einem Administrator-Login und -Passwort.

#### OAuth 1.0a

* Kopieren Sie den Client Key und das Client Secret vom (vorbereiteten) Applikations-Benutzer aus Wordpress
* Klicken Sie "Generate Key" um sich mit Wordpress zu verbinden, sich zu authentifizieren und ein Token bzw. Token Secret zu erhalten.
* Alle Einstellungen in der base-Konfiguration speichern.

### easydb-Benutzer authentifizieren

Benutzen Sie die [Systemberechtigungen](../webfrontend/rightsmanagement/rightsmanagement.html) "Wordpress" & "Wordpress transport" und Benutzer für die Verwendung des Wordpress Transport in easydb zu autorisieren.

### Benutzung in easydb

* In jedem Export können Sie "Transport Wordpress" benutzen um alle zu exportierenden Dateien nach Wordpress zu transferieren.
* Wählen Sie die vorbereitete und konfigurierte Wordpress-Instanz dafür aus.
* Wählen Sie Optional einen Plan bzw. inkrementelle Updates für regelmässige Aktualisierungen auswählen.





