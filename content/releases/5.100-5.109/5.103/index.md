---
menu:
  main:
    name: "5.103 (Juli 2022)"
    identifier: "5.103"
    parent: "releases5100"
    weight: -603
---

> Diese Version **benötigt keinen neuen Index-Aufbau**

# Version 5.103.2

*Veröffentlicht am 29.07.2022*

# Webfrontend

## Behoben

* **Listen**: Objekttypen, bei denen nur Lesen, aber nicht Anlegen erlaubt ist, werden wieder angezeigt

# Server

* **Suche**: Systemrecht `system.group[global_custom_bag_read]` funktioniert wieder für `acl`-Suche

## Behoben

# Version 5.103.1

*Veröffentlicht am 27.07.2022*

# Webfrontend

## Behoben

* **Export**: automatisches Anwenden des ersten Templates unterbunden
* **Drucken**: Fehler beim Aufruf des Druck-Dialogs behoben

# Server

## Behoben

* **Wordpress-Plugin**: OAuth-Konfiguration behoben

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
docker.easydb.de/pf/server-base          sha256:9a768a503d73fa5ee07d56a5eb713885687d312c9d7211387ec960f78ff2ed68
docker.easydb.de/pf/webfrontend          sha256:802dd582c392aac237f063ec4050225f0e06dda22b63f581435cb4013a598660
```
