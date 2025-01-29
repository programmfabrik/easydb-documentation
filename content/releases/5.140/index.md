---
menu:
  main:
    name: "5.140 (Januar 2025)"
    identifier: "5.140"
    parent: "releases"
    weight: -640
---

> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.140.0

*Veröffentlicht am 29.01.2025*

# Webfrontend

## Neu

* **Metadaten-Mapping**: für das Import-Mapping können eigene Tags angegeben werden
* **Sortierung**: per Masken-Option können Felder bei der Sortierung ausgeblendet werden

## Verbessert

* **Editor-Templates**: verschiedene Verbesserungen, eine neue Vorschau-Möglichkeit
* **Expertensuche/Sortierung**: Systemfelder sind jetzt in einem einklappbaren Bereich
* **Gruppeneditor**: Button zum Abbruch hinzugefügt
* **Pool-Auswahl**: Verbesserungen
* **Lokalisierung**: Rückfall auf vorhandene Lokalisierung zur Darstellung von Fehlern, die vor dem Laden der Lokalisierung auftreten

## Behoben

* **Teilen**: Fehler beim Rechte-Check behoben
* **Datumsbereiche**: getrennte Validierung und Indikation der Fehler in von-/bis-Feldern
* **Hauptsuche**: fehlerhaftes "keine Ergebnisse" behoben beim Umschalten der Ansicht
* **Default-Tags**: Verhalten bei nicht erlaubten Tags in Objekt-Templates korrigiert
* **Export-Templates**: Speichern behoben
* **Editor**: Verhalten der Checks in verschachtelten Tabellen behoben
* **Changelog-Spalte**: Sichtbarkeit korrigiert
* **Datums-Facets**: Reihenfolge der Filter behoben
* **Editor**: fehlerhafte Maskenauswahl für verlinkte Objekte behoben
* **Pools**: Maskenauswahl behoben
* **Mappen-Upload-Einstellungen**: korrektes Zurücksetzen ausgewählter Pools beim Deaktivieren der Option
* **Autocomplete-Popup**: Fokus-Verhalten korrigiert
* **Tag-Darstellung**: Fehler bei Tags ohne Typ behoben
* **Editor**: Überwachung reverse-verlinkter Tabellen korrigiert, um falsche Meldungen zu verhindern

# Server

## Verbessert

* **/api/event/list**: neuer Parameter `skip_count`, um die langesame Berechnung der Gesamtzahl der Events zu überspringen

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.140.0            sha256:c1b44aa0f1dab4e2bc81f6a851d5d0622e20f87bd320365336af0f9e8bc439ee
docker.easydb.de/pf/elasticsearch:5.140.0  sha256:5e2ca062a092853c8694b8a4dfb5dcb1e0c98da429e214c0c9952eda8a3a8d18
docker.easydb.de/pf/fylr:5.140.0           sha256:4e76f1f1c63f914bc6e9b2714e33961084eef651974fc0c5500fc65bd57eef70
docker.easydb.de/pf/postgresql-14:5.140.0  sha256:73a17d2c461c1538ae30c73f76ade294f6a65566a031dfed4d5bbfaba55d8df0
docker.easydb.de/pf/server-base:5.140.0    sha256:b7479b4604161f086188d61b760aa1f173c0b57485d4ee737034d9afad01eeff
docker.easydb.de/pf/webfrontend:5.140.0    sha256:a645c3bbf73ec76a3dbc4500b93de1494e63144416e4d257d78abaadb85c3207
```
