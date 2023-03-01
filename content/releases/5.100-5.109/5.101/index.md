---
menu:
  main:
    name: "5.101 (Juni 2022)"
    identifier: "5.101"
    parent: "releases5100"
    weight: -601
---

> Diese Version **benötigt keinen neuen Index-Aufbau**

# Version 5.101.0

*Veröffentlicht am 08.06.2022*

## Webfrontend

### Neu

* **Expertensuche**: Filter für Datei-Datum

### Verbessert

* **Editor**: Ausgabe von Objekt-ID, etc. in der Fußzeile
* **Pools**: Kommentarfeld hinzugefügt

### Behoben

* **Datenmodell**: Prüfung des Wertebereichs von Dezimalzahlen korrigiert
* **Autovervollständigung**: gesamte Eingabe wird vervollständigt
* **Editor**: Limit von 1000 Objekten im Editor wird auch bei Uploads forciert
* **Collections**: Darstellungsproblem bei Suche ohne Ergebnis behoben
* **CSV-Importer**: Problem bei leeren Werten für verlinkte Objekte behoben
* **PDF-Anzeige**: keine Annahme, dass das Original lesbar ist

## Server

### Verbessert

* **/api/v1/db**: Check der Collection-Rechte seltener und kann übersprungen werden
* **XML-Export**: Option für Ausgabe von Nebenobjekten sowie Hauptobjekten, die über einen Reverse-Link verknüpft sind
* **Suche/XML-Mapping**: Standard-Feld von Custom-Datentypen suchbar
* **API-Logging**: Events auch für `/api/v1/objects` konfigurierbar
* **Datenbank**: neuer Index, um EAS-Supervisor bei Verwendung vieler Objekte mit Wasserzeichen zu beschleunigen
* **/api/v1/db**: Verbesserungen für `all_versions=true` (Bulk-API in Vorbereitung für Migrationszwecke)

### Behoben

* **XML-Export**: rekursives Laden verlinkter Objekte korrigiert
* **Gruppeneditor**: Entfernen von Nested-Objekten auch bei mehreren Vorkommen
* **POST /api/v1/user**: leere Sprach-Listen erlaubt
* **Plugin-Schnittstelle**: Fixes für im Hotfolder verwendete Callbacks
* **EAS**: Erkennung von WMF-Dateien behoben

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:8b0849bbb05834e0b273caf2d345f3635b7b61c74bc571960a5b70e5042ff869
docker.easydb.de/pf/eas                  sha256:1d78dbffc7ed68195799320876b86bb005840cc5c4ba99db9c05a95572d76c9b
docker.easydb.de/pf/elasticsearch        sha256:cfd775500615b26d4285fee1ff1914a85b51b4c54ed65972f92576cf212f66f0
docker.easydb.de/pf/fylr                 sha256:9e92b063deb5b4b44258eb669392fe6f4165e55e6fc4fad312037e72d04af8aa
docker.easydb.de/pf/postgresql-11        sha256:3b7fedc8dfa5fb4238005d7e859ec1e0b13173854b8a84490b2b9d0f20e60494
docker.easydb.de/pf/postgresql-14        sha256:14671871594cb6a62e506852ee3339e93d02c808918ee860f602f675d251c53d
docker.easydb.de/pf/server-base          sha256:1d6ad542d8eed44a3f1868ea5a4db01e52777957871d789e022c79a488f1c004
docker.easydb.de/pf/webfrontend          sha256:025b38c8f2292e791bcac6052b45c45c54eaf6a1ddea8c1cd47b9bbb6a7085c7
```
