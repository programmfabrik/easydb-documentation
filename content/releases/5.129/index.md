---
menu:
  main:
    name: "5.129 (Ende Februar 2024)"
    identifier: "5.129"
    parent: "releases"
    weight: -629
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.129.0

*Veröffentlicht am 28.02.2024* (noch nicht)

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
* 

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
```
