---
menu:
  main:
    name: "5.138 (November 2024)"
    identifier: "5.138"
    parent: "releases5130"
    weight: -638
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.138.2

*Veröffentlicht am 27.11.2024*

# Webfrontend

## Behoben

* **Editor**: Javascript-Fehler beim Anlegen von Objekten mit Reverse-Link-Feldern behoben

# Version 5.138.1

*Veröffentlicht am 18.11.2024*

# Webfrontend

## Behoben

* **Editor**: fehlende Speicherung mehrfach reverse-verlinkter Objekte behandelt
* **ACL-Editoren**: Anzahl möglicher Gruppen und Benutzer in der Auswahl zur ACL-Konfiguration erhöht
* **Templates**: Speicherung in den Benutzereinstellungen behoben

# Server

## Behoben

* **PDF-Druck**: Proxy-Einstellungen via Umgebungsvariablen werden an Chromium-Prozess weitergereicht

# Version 5.138.0

*Veröffentlicht am 06.11.2024*

# Webfrontend

## Behoben

* **Pool-Manager**: Speicherleck behoben.
* **Detail-Linked-Mask-Splitter**: Rendering der Objekt-Referenzen behoben und verbessert. Problem mit fehlenden Elementen behoben.
* **Editor**: Speicherung der Optionen in den Benutzer-Einstellungen korrigiert.
* **Datumsbereichssuche**: Fehler bei Suche mit Textrepräsentation behoben.


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.138.0            sha256:04e036fce52a69fb25b47736e100126dc9401ac1f049a61feb422a0df4e61b79
docker.easydb.de/pf/elasticsearch:5.138.0  sha256:93298312e5a634377feb2db6a4ae77e13c392bed9a3533532b7012c7f32711c4
docker.easydb.de/pf/fylr:5.138.1           sha256:c12fd029749c4a48e8ff056a02730ed229217c3ecf6e16c55f0622257c3ea856
docker.easydb.de/pf/postgresql-14:5.138.0  sha256:b85f6f77513e4324e4e70fb76c6d03d18612ec90d8715a6f6642ac3fa3930bfc
docker.easydb.de/pf/server-base:5.138.2    sha256:043258e27121ba57f3888375a6f49f9a0b48174597b04284ce1e8c331f52d03a
docker.easydb.de/pf/webfrontend:5.138.2    sha256:f6e3014f2e647489d7528c39be60e00fa2da70e7d8bccedff3ea8f8fb4a8ea68
```
