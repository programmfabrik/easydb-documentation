---
menu:
  main:
    name: "5.129 (Ende Februar 2024)"
    identifier: "5.129"
    parent: "releases5120"
    weight: -629
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.129.2

*Veröffentlicht am 07.03.2024*

# Webfrontend

## Behoben

* **Editor**: Fehler beim Öffnen von Editor ohne Asset-Browser behoben

# Version 5.129.1

*Veröffentlicht am 05.03.2024*

# Webfrontend

## Behoben

* **Suche**: Fehler beim Hierarchie-Button behoben, Funktion erweitert und in Listen verfügbar gemacht

# Version 5.129.0

*Veröffentlicht am 28.02.2024*

# Webfrontend

## Verbessert

* **Suche**: Button "Nur oberste Ebene" ersetzt die Option "Flache Hierarchie"
* **CSV-Importer**: Status-Panel in eigenen Tab verschoben
* **Detail**: Verlinkte Objekte im Dropdown werden dynamisch nachgeladen, anfänglich bei max. 100.

## Behoben

* **Suche**: Bug behoben, der die Suche beim Tippen auslöste, wenn vorher ein Suchelement gelöscht wurde
* **Allgemein**: Mehrfacheingabefelder (z.B. im Datenmodell-Editor) konnten bei Änderung der Spracheinstellungen falsche Werte erhalten
* **Gruppeneditor**: Fehler bei Bearbeiten von Objekten, die bereits im Einzeleditor geöffnet waren, behoben
* **Textansicht**: Fehlerhafte Darstellung behoben
* **Mappen**: Fehler in "Doppelter Ansicht" behoben
* **Detail**: Zurücksetzen bei Auswahl in Hierarchie-Liste behoben
* **Änderungsanzeige**: Fehler bei Boolean-Felder behoben, wurden immer als gelöscht dargestellt
* **Rechte**: Anzeige der Asset-Namen wie an anderen Stellen

# Server

## Neu

* Neuer Parameter `changelog_with_user` im `frontend_features`-Systemrecht.

## Verbessert

* URL in `ASSET_DOWNLOAD`-Ereignissen.

## Behoben

* Aufräumen leerer Listen und Rechte bei `link`/`unlink`, wenn ein Pool entfernt wird
* korrekter Fehler, wenn im Import-Prozess eine Pool-ID in der Eingabe erwartet wird

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.129.0         sha256:d98c3c3e94d030d653d7a423565fe44484e1857a4f6a85e58b9730cd31c8b92c
docker.easydb.de/pf/eas:5.129.0            sha256:896e8eac41e75633625c1e1fe5fc5fe9183c09f8b097a46b253ccb47d2e2bf8c
docker.easydb.de/pf/elasticsearch:5.129.0  sha256:f1be13d659b310d39737f42a0d83c1b7284333f58a01731cf773906bca819a6e
docker.easydb.de/pf/fylr:5.129.0           sha256:d7bf98ef34ab8f596ab38221e2a01c2e4d0b732068e2ec7b09d527f512961722
docker.easydb.de/pf/postgresql-14:5.129.0  sha256:6ac8581884e16aa4b48ef9af07e050da0eb7e256409e9aa5c96aaac154093db4
docker.easydb.de/pf/server-base:5.129.2    sha256:5e2b036bc06a2b5cb7009a2d830a19e60496a20c88940ba50a7fc157f9c877b8
docker.easydb.de/pf/webfrontend:5.129.2    sha256:9d150b4bd1df77ef04d33178761ffbb429248117ae03a908c2a50a9006be4831
```
