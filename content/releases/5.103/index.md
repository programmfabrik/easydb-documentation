---
menu:
  main:
    name: "5.103 (Juli 2022)"
    identifier: "5.103"
    parent: "releases"
    weight: -603
---

> Diese Version **benötigt keinen neuen Index-Aufbau**

# Version 5.103.0

*Veröffentlicht am 20.07.2022*

# Webfrontend

## Neu

* **Mitteilungen**: permanente Mitteilungen können mit Icon versehen werden
* **Allgemein**: Kundenlogo kann als Link auf eine Webseite konfiguriert werden

## Verbessert

* **Editor**: überall auf EAS-Spalten kann geklickt werden, wenn sie noch kein Asset enthalten
* **Rechtemanager**: beim Vergeben der Rechte wird angezeigt, für welchen Nutzer/welche Gruppe gerade Rechte vergeben werden
* **Druck-Dialog**: Feldauswahl für PDF-Templates und Standard-Layouts
* **CSV-Importer**: Metadaten-Mapping für `rput`-Option deaktiviert, da nicht anwendbar

## Behoben

* **Bildansicht**: Vorschaubilder mit Wasserzeichen werden wieder verwendet, wenn keine hinreichend großen Versionen ohne Wasserzeichen verfügbar sind
* **Suche**: Suche nach Seitenverhältnis korrigiert
* **Detail**: Panel wird wieder dargestellt, auch wenn es nur einen CustomFieldRenderer enthält
* **Editor**: Kalender ermöglichte Zeitauswahl, auch wenn das Feld nur ein Datum aufnehmen konnte, behoben
* **Editor**: fehlerhafte Maskenauswahl korrigiert

# Server

## Verbessert

* **Basiskonfiguration**: neuer Parameter `system.logo.external_url`
* **EAS**: Wasserzeichengröße wird auch als einfache Zahl akzeptiert
* **Messages**: `webfrontend_props` werden für `pending_tasks` ausgegeben, sofern vorhanden

## Behoben

* **Allgemein**: Cache-Invalidierung bei Änderung von Reverse-Links
* **Allgemein**: Unterstützung von langen Spaltennamen für einige Datentypen korrigiert
* **EAS**: Status verwendet End- statt Startzeit für kürzlich beendete Jobs (`recent-done`/`recent-failed`)
* **EAS**: Workaround für Schreiben von Metadaten in Dateien mit existierenden ungültigen Metadaten
* **Suche**: Wildcard-Suche sucht nicht in Tokens

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:fd0a83f7f0e2432c21689386e78b205a86466b6fbe8dfb48192c7c8e2b7c09be
docker.easydb.de/pf/eas                  sha256:d9ea068020505588b2dee54dd8a4b54cf20692a8d77384a5618d6defdb1fbbc7
docker.easydb.de/pf/elasticsearch        sha256:9a19a70271f3e09a4757bec670fc00f012d3b7185ed383e4c8d5cc7bc121fa4f
docker.easydb.de/pf/fylr                 sha256:b545f0227558d4e8b55d705127aa4cc418edea6c75e99ff64132b3aee33d2702
docker.easydb.de/pf/postgresql-11        sha256:30eb077d11e7a1e7185b3623bec46c6bae65e9d2156393490ec9322ebc673985
docker.easydb.de/pf/postgresql-14        sha256:308a7a809706fcd80e60aba523dba8adbd7609c0e606e08ea8083d22173c8890
docker.easydb.de/pf/server-base          sha256:378cd2acd51110398d8f25dd771fa8ce7f38c29a347475ed93fef0c9cb35c8c6
docker.easydb.de/pf/webfrontend          sha256:21100c6b40c67404f02523e1c02619ce4851f3fd6318e8b363ca7e57e51fb89d
```
