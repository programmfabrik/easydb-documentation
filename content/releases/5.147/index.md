---
menu:
  main:
    name: "5.147 (Ende August 2025)"
    identifier: "5.147"
    parent: "releases"
    weight: -647
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.147.2

*Veröffentlicht am 03.09.2025*

# Webfrontend

## Behoben

* **Detail**:
  * Fehler in der Maskenvorschau behoben, der auftrat wenn im Objekt kein Standard "A" existiert
  * Dadurch war der Upload von Dateien über das Frontend nicht möglich
* **Editor**:
  * Probleme bei der Darstellung von Tags in verlinkten Objekten behoben
  * Die Tags wurden nur als Text dargestellt

# Version 5.147.1

*Veröffentlicht am 28.08.2025*

# Webfrontend

## Behoben

* **Detail-Ansicht**: Fehler behoben, der u.U. das Öffnen der Detail-Ansicht verhinderte

# Version 5.147.0

*Veröffentlicht am 27.08.2025*

# Server

## Behoben

* **Suche**: inkompatible Änderung an der Phrasensuche in String-Feldern zurückgesetzt
* **Docker-Container**: hohe UIDs/GIDs einiger Dateien ersetzt

# Webfrontend

## Behoben

* **Nested- und Reverse-Nested-Tabellen**: bei Verwendung der "readonly"-Option in den Masken kam es dazu, dass Daten beim Speichern nicht korrekt gesendet wurden.
* **Print-Manager**: es wird sichergestellt, dass alle Bilder geladen sind, bevor der Browser-Druck aufgerufen wird.
* **Nested-Einträge**: Lösch-Knopf verbessert, sodass immer eine leere Zeile angezeigt wird, wenn das so konfiguriert ist.
* **CSS**: verschiedene Anpassungen und Fixes

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.147.0            sha256:60d835e6afa49690ae5b8f91c056070751044b3a4678fdc5a8fb932b2bc45501
docker.easydb.de/pf/elasticsearch:5.147.0  sha256:2afe7cb91c3ba1d36d80e2929e84904cbf694fab5e9fba60004fa44eeb21125c
docker.easydb.de/pf/fylr:5.147.0           sha256:289c4c1c6418636ed6b7735e31296fb9967ee45e0ac67264ac78a76972d8e782
docker.easydb.de/pf/postgresql-14:5.147.0  sha256:7440d687452800694b86db7aa3627a07d3505d0c21e605dc1f5d25a9f0693702
docker.easydb.de/pf/server-base:5.147.2    sha256:b56b3c4ea7193453de43b7bec196850dac2237576a3d4069774becf77cf7f735
docker.easydb.de/pf/webfrontend:5.147.2    sha256:0c8d9591d7903f8e7b5f88c3485dff4572869350e8a0b522bdc86e61feb4a96c
```
