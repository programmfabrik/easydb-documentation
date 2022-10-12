---
menu:
  main:
    name: "5.91 (Oktober 2021)"
    identifier: "5.91"
    parent: "releases599"
    weight: -591
---

> Diese Version **benötigt keinen neuen Index-Aufbau**, das neue Elastic-Image arbeitet mit den vorhandenen Index-Dateien.

# Version 5.91.1

*Veröffentlicht am 26.10.2021*

## Server

### Behoben

* **XML-Export / Typo3-Expor**t: Beim Export von Listen kam es zu XML-Nodes mit dem Text `VALUE_SEPARATOR`.
* **Indexer**: Fehler im Zusammenhang mit gelöschten Assets behoben.

# Version 5.91.0

*Veröffentlicht am 20.10.2021*

## Webfrontend

### Neu

* **CSV-Importer**:`system_object_id` kann für verlinkte Objekttypen und hierarchische Felder zum Mapping benutzt werden.
* **CSV-Importer**: Unterstützung von Datemseingaben als Text.
* **Plugins**: Unterstützung von zentralem Laden (easydb 6) aller Dateien.

### Verbessert

* **Detail**: Verlinkte Objekte mit Assets zeigen jetzt grafisch an, wenn sie mehr als ein Asset haben.
* **IUCN-Plugin**: Verwendung der Bulk-API für beschleunigte Abfragen.
* **Suche**: Anzeige von Filternamen bei fehlender Lokalisierung verbessert.

### Behoben

* **Suche**: Beim Filtern von leeren Suchen mit hierarchischen Objekttypen wird jetzt bei reiner Top-Level-Suche der Top-Level-Filter nicht mehr automatisch entfernt.
* **ScriptExecuter**: Fields-Migrator hat für Masken mit Splitter nicht funktioniert.
* **Datamodel**: Reverse-Edit wurde im Datenmodell "Aktuell" immer als de-aktiviert angezeigt, auch wenn es aktiviert war.
* **Datenmodel**: Anzeige des lokalisierten Namen bei Reverse-Objekttypen war unter Umständen inkorrekt.
* **Editor**: Das Senden von Zeitzonen wurde beim Speichern korrigiert (easydb 6).
* **Neue Objekte**: Die Anzeige vom Pool war unter Umständen nicht sichtbar.
* **Suche**: Filter für Tags wurde repariert.

## Server

### Neu

* **Neue Sprache**: `fi-FI` (Frontend Vorbereitung & Datenbank).

### Verbessert

* **XML-Export**: Kein automatisches Semikolon zwischen Einträgen, das kann mit einem festen Wert manuell eingerichtet werden.
* **Hierarchische Objekte** können im Standard Werte von übergeordneten Objekten nutzen (in Reverse).
* Beschleunigte Verarbeitung von **/api/event/poll**.
* **XML-Export**: Ergänzung des Asset-Namens beim Export.
* **Schema-Update**: Verbesserungen bei der Umstellung von Text auf lokalisierten Text.
* **Beschleunigte Authentifzierung** von anonymen Benutzern.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:c7a06bca14634f897e8b300fb5e3f624d89adb0dd8cfb746e92975a81868974b
docker.easydb.de/pf/eas                  sha256:33d981b6e54af916e03f38f299c546e053e348cdf5541fc0cdf61cb14d3a8e3f
docker.easydb.de/pf/elasticsearch        sha256:9caf333392a56946bc28e68251c4c146e017b901920ff3042054cd2e14f577b2
docker.easydb.de/pf/fylr                 sha256:fbb1b412cfc82477393ec65c2135d261e3de26507f589c1141d952db8e333d05
docker.easydb.de/pf/postgresql-11        sha256:29114c653a20bafbf505864b0fc1fe3b85b276656620cddd36a65a4dc90b4284
docker.easydb.de/pf/server-base          sha256:cd9bd83925faef33d1703cf2354f362d66b63e5452894315da91ed8bc5b193ce
docker.easydb.de/pf/webfrontend          sha256:73c8cbf7c8649846d1ca58e0b359b809b097875a24aaa22f6481dc0965bc33ad
```
