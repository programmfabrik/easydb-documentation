---
menu:
  main:
    name: "5.98 (Anfang April 2022)"
    identifier: "5.98"
    parent: "releases599"
    weight: -598
---

> Diese Version **benötigt keinen neuen Index-Aufbau**

# Version 5.98.2

*Veröffentlicht am 19.04.2022*

## Webfrontend

### Behoben

* **CSV-Importer**: Problem bei verschachtelten Nested-Feldern korrigiert
* **Export**: Fehler bei Auswahl einzelner Felder korrigiert

## Server

### Behoben

* **Export**: Fehler bei gleichen Dateinamen korrigiert
* **EAS**: fehlschlagende Zoomer-Aufrufe behoben

# Version 5.98.1

*Veröffentlicht am 08.04.2022*

## Webfrontend

### Behoben

* **Filter**: Zähler bei Kombination mehrerer Filter behoben
* **Expertensuche**: Für Mehrfachfelder: falscher interner Check, um das 'Ohne' Label anzuzeigen, wurde entfernt
* **Mappenpresentation**: Probleme im CSS für den Hintergrund von Bildern und schwarzen Folien behoben

# Version 5.98.0

*Veröffentlicht am 06.04.2022*

> Mit diesem Release wurde ein Sicherheitsproblem gelöst. Details teilen wir auf Nachfrage an support@programmfabrik.de gerne mit.

## Webfrontend

### Verbessert

* **Allgemein**: durchgehende Verwendung von Tausender-Trennern für Zahlen
* **Filter**: Überschriften für verlinkte Objekte verbessert
* **Basis-Konfiguration**: Ace-Bibliothek wird nicht mehr von externen Ressourcen geladen

### Behoben

* **CSV-Importer**: Problem mit System Object ID in Hierarchien behoben
* **CSV-Importer**: Vorschau für verlinkte Objekte korrigiert
* **JSON-Importer**: Fehler bei Verwendung des Lookup-Features und mehr als 1000 IDs in der Suche behoben
* **Editor/Detail**: Masken-Optionen zur Anzeige von Objekttyp/Pool für verlinkte Objekte behoben
* **Suche**: Fehler bei Assets in verschachtelten verlinkten Objekten behoben
* **Editor**: Pool wird beim Ändern nicht für reverse-verlinkte Eltern-Elemente gesetzt
* **Metadaten-Mapping**: verfügbare Felder werden nicht fälschlicherweise durch Masken gefiltert

## Server

### Neu

* **/api/v1/event**: Leseanfragen außer Polling erfordern jetzt das Systemrecht `system.api.event.get`, das Löschen von Ereignissen `system.api.event.delete`.

### Verbessert

* **/api/v1/objecttype**: Geschwindigkeit bei vielen Objekttypen weiter optimiert
* **Pool**: Kommentar ermöglicht
* **Custom-Datatype-Updater**: Abbruch eines Batches, wenn dieser 10 mal fehlschlägt

### Behoben

* **Export**: Länge des Dateinamens beim Download auf 100 Zeichen beschränkt, um nicht an Grenzen von Dateisystemen zu stoßen
* **Export**: Fehler beim Holen von Dateien aus dem EAS brechen nicht den gesamten Export ab
* **Index**: Sortierung von `_standard.eas` im Zusammenhang mit Mehrfachfeldern behoben
* **Suggest**: bei Vervollständigung von verlinkten Objekten müssen alle Suchbegriffe vorkommen
* **Custom-Datatype-Updater**: Anzahl der Objekte im Batch bei erneutem Versuch nach Fehler korrigiert
* **Session**: String-Parameter von Systemrechten werden korrekt zusammengeführt, über Gruppen vergebene Rechte hatten teilweile keine Wirkung (nur Metadaten-Parameter)

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:451a6d6e05936ed704277c6842b4ad3119f25a2ed5631734f71049f3b8069cc4
docker.easydb.de/pf/eas                  sha256:aa78b6a8cc56b74b351e4d14b1b8cb51ec74e9ce9dfec23f3f142abb5909f852
docker.easydb.de/pf/elasticsearch        sha256:bac077eb81d38b8f6e6506ffea7a5c26e5043832e6747886b2e7b12484cc57d7
docker.easydb.de/pf/fylr                 sha256:b3bfa2edbaad51563d8165fd52c7c0ab8cdf78ac2f42cd62e511487bb5d5e279
docker.easydb.de/pf/postgresql-11        sha256:b3562998e544ca25271b15a46ca10cf53025798cf7b9707e758063252b936986
docker.easydb.de/pf/server-base          sha256:6037f74655fe928713b4b505fce26c8d590daadecd8ed3118b1e187e8cdbecb3
docker.easydb.de/pf/server-base-py3      sha256:ee5cc91b4f691fa4c6664cb96f13e80c802d44c213866e9e134ec6db9f74bb65
docker.easydb.de/pf/webfrontend          sha256:3d779d99b61d4e019009dc26662fb21f52e96a21ca66a6ed9116f3d37095e1e1
```
