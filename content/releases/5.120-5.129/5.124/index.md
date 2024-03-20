---
menu:
  main:
    name: "5.124 (Anfang November 2023)"
    identifier: "5.124"
    parent: "releases5120"
    weight: -624
---

> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.124.0

*Veröffentlicht am 01.11.2023*


# Webfrontend

## Neu

* **Mappenansicht**: Die Liste von geteilten Mappen ist in Seiten unterteilt, mit höchstens 100 Mappen pro Seite
* **Detailansicht**: für jeden Objekttyp wird die Maske gespeichert, mit der die Objekte zuletzt dargestellt wurden

## Verbessert

* **Benutzerimport per CSV**: Import von Passwörtern hinzugefügt
* **Suche**: das Wildcard-Symbol wird in der Liste der Vorschläge bei der Autovervollständigung deutlicher dargestellt
* **Schnellzugriff**: verlinkte Objekte, bei denen in der Maskeneinstellung für die Suche `Filter` aktiviert ist, werden ebenfalls dargestellt
* **CSV Importer**:
  * Import von Spalten mit Zahlenwerten verbessert
  * Import von Datumsbereich-Feldern verbessert
  * Tags können anhand von `shortname` und `reference` importiert werden
  * Mehr Filteroptionen für CSV-Zeilen: filtern nach Warnungen und Operationen ist möglich

## Behoben

* **Filter**: Fehler beim Filtern nach hierarchischen verlinkten Objekten behoben
* Fehler beim Laden von Transitionen/Workflows behoben


# Server

## Verbessert

* **Hotfolder-Plugin**
  * Erkennung und Verlinkung von Seriendateien (Dateien mit Dateinamensuffixen wie `-1`, `-2` etc.) wurde verbessert
  * Import mit Metadatenmapping: verbessertes Pool-Handling für verlinkte Objekte


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.124.0         sha256:88a93e887dc95b48f03fa0fb3c16cc3c90722914e3c797a07c8784fa23d8c904
docker.easydb.de/pf/eas:5.124.0            sha256:6fcdcb1a2032aaf0c478b4b418719dc7f3c88ebf3532f2b69bba70cd170da520
docker.easydb.de/pf/elasticsearch:5.124.0  sha256:e2de1132d7d569ac20250cb9e7e2ba15079d4e422a2e558ce5cd4225cdb8c74a
docker.easydb.de/pf/fylr:5.124.0           sha256:3507a1fe66d21e0e208f3a51758b83ed67379693ad231db5038bb3ff0414496b
docker.easydb.de/pf/postgresql-14:5.124.0  sha256:2e0f69218239ac4f3cadf5b3bd1fc871ea2306c0877f96b0ebeba967e98183f0
docker.easydb.de/pf/server-base:5.124.0    sha256:051e8108ce6beccc3a22519f0da892cb4fa5c1eaa2da582c3aad5942b976b03e
docker.easydb.de/pf/webfrontend:5.124.0    sha256:e242f10dfa4e544ec16148aabef274e877529ffdfe9289343ed37fa888a17a76
```
