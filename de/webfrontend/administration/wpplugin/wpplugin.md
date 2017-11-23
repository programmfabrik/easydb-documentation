# Wordpress plugin

Plugin um Mediendateien ins Wordpress CMS zu transferieren. Aktuell unterstützt dieses Plugin sowie das Erstellen von neuen Medien als auch das Aktualisieren von deren Metdaten. Wenn ein neues Medium in easydb angelegt wird wird auch ein neues in Wordpress angelegt. Es existiert keine Unterstützung für das Löschen von Medien.

## Voraussetzungen

* Wordpress 4.7
* Wordpress benötigt die JSON-Rest-API aktiviert (ist Default) und Authentifizierung eingerichtet.

## Setup (Wordpress)

* easydb unterstützt **JSON Basic Authentication** undand **WP REST API - OAuth 1.0a Server**
 * Plugin(s) für Authentifizierung installieren
 * Plugin(s) für Authentifizierung einschalten
 * Benutzer für das oauth-Plugin einrichten. Callback URL: http://**easydb-server**/api/v1/plugin/base/easydb-wordpress-plugin/oauth1

## Plugin in easydb aktivieren

* Stellen Sie sicher, dass das Plugin korrekt installirt ist (Pfade sind relativ zum .yml angegeben):

Fügen Sie doe folgenden Zeilen zu Ihrer server.yml hinzu:

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

(see FIXME)

### HTTP-Authentifizierung

Verbinden Sie sich mit einem Administrator-Login und -Passwort.

### OAuth 1.0a

* Kopieren Sie den Client Key und das Client Secret vom (vorbereiteten) Applikations-Benutzer aus Wordpress
* Klicken Sie "Generate Key" um sich mit Wordpress zu verbinden, sich zu authentifizieren und ein Token bzw. Token Secret zu erhalten.
* Nicht vergessen die base-Konfiguration zu speichern.

## easydb-Benutzer authentifizieren

Benutzen Sie die Systemberechtigungen "Wordpress" & "Wordpress transport" und autorisieren Sie jeden, der easydb Wordpress Transport benutzen können darf.

## Benutzung in easydb

* In jedem Export können Sie "Transport Wordpress" benutzen um alle zu exportierenden Dateien nach Wordpress zu transferieren.
* Wählen Sie die vorbereitete und konfigurierte Wordpress-Instanz dafür aus.
* Wählen Sie Optional einen Plan bzw. inkrementelle Updates für regelmässige Aktualisierungen auswählen.

