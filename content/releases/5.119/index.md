---
menu:
  main:
    name: "5.119 (Juli 2023)"
    identifier: "5.119"
    parent: "releases"
    weight: -619
---


> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.119.0

*Veröffentlicht am 12.07.2023*

# Webfrontend

## Verbessert

* **Suche**: Suche wird automatisch ausgeführt, wenn die Anfrage bearbeitet wird
* **easydb-editor-tagfilter-defaults-Plugin**: Datumseingaben werden unterstützt
* **Allgemein**: Indikator, wenn Bereiche im Schnellzugriff leer sind

## Behoben

* **CSV-Importer**: Problem bei Auswahl eines Reverse-Link-Felds als Ziel behoben
* **Allgemein**: Datumsformate für einige Sprachen ergänzt (fi, sv, fr)
* **Druck**: CSS-Problem behoben, bei dem alle Sprachen in Mehrfacheingabefeldern angezeigt wurden
* **Downloads**: Darstellung von Meldungen vor dem Asset-Download korrigiert
* **Linked-Object-Filter**: Fehler behoben
* **Tooltips**: Problem mit offen bleibenden Tooltips behoben
* **Suche**: Verhalten des Ressourcen-Buttons bei neuen Instanzen korrigiert

# Server

## Verbessert

* Server-seitige Nested-Sortierung: Unterstützung für Asset-Spalten (Sortierung nach Originaldateiname).
* neue Datensprache Nepali (`ne`).

## Behoben

* EAS-Supervisor versucht nicht mehr, fehlgeschlagene Originale zu behandeln.
* Zuschneiden von Raw-Bildern behoben, Zielformat wird JPEG statt des nicht unterstützten Quellformats.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.119.0         sha256:ba585893b5bc343f2c03e08ffe7e2074c564abc18bc6ee7460910b5050766e4f
docker.easydb.de/pf/eas:5.119.0            sha256:205eadef7b37677ad70e8069a9f4a381bd507b1bc8e06f185bfe463a316a49d5
docker.easydb.de/pf/elasticsearch:5.119.0  sha256:bb4053497f821b524aae9624f7a019059c8a242d8c761b64488994cdfa2fec7c
docker.easydb.de/pf/fylr:5.119.0           sha256:fd595fcc78aa7f078a11577dae20de87939dd9151b5633e967b4482ef56512f6
docker.easydb.de/pf/postgresql-14:5.119.0  sha256:a9f76cf58c9ab60d3b940892dd12133095ca7885c119d5d186defc538118d7b2
docker.easydb.de/pf/server-base:5.119.0    sha256:fafc9352252c00a37dba6e671c6fccfc2700b7ea6958ff3e99d57e568520bd11
docker.easydb.de/pf/webfrontend:5.119.0    sha256:f5ab8176317b84064866a684169f11ad56e90e3d0d6d1d853c7fcf141c69403d
```
