---
menu:
  main:
    name: "5.119 (Juli 2023)"
    identifier: "5.119"
    parent: "releases5110"
    weight: -619
---


> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.119.1

*Veröffentlicht am 19.07.2023*

Alle Images wurden neu generiert, um aktuelle Sicherheits-Updates zu einzuspielen. Besonders [CVE-2023-36664](https://nvd.nist.gov/vuln/detail/CVE-2023-36664) wurde durch Update des Ghostscript-Pakets behandelt.

# Webfrontend

## Behoben

* **Start**: langsame Such-Anfrage wird vermieden

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
docker.easydb.de/pf/chrome:5.119.1         sha256:3897719774c5d49d06666b1e057a2eff53e8fec0d4fede7f2d6ad5f744ede7de
docker.easydb.de/pf/eas:5.119.1            sha256:a330e408fa83835912cb73cc6e026e432b5b5371ceef7d24d2a55a912508edad
docker.easydb.de/pf/elasticsearch:5.119.1  sha256:c0ff7ea49dacff828684df73ed9373911c5c65187e651234cfa51da8f02879b5
docker.easydb.de/pf/fylr:5.119.1           sha256:4bf9bee704a51c2ce69dfab3e45b841e70aed9ddddf9548b3788e59ad020cda2
docker.easydb.de/pf/postgresql-14:5.119.1  sha256:28aecee9c57724a9e25342f55c345fb5135b0439935b9228731c92cb5aed120b
docker.easydb.de/pf/server-base:5.119.1    sha256:c44da8b6466d63eb88daeb4200501c0c0bbdac3880bd0d144310b3913771ccfc
docker.easydb.de/pf/webfrontend:5.119.1    sha256:1ea14ce8e391881e514a560f0e7ff56072c50642e6ec5a4585f660e312236f85
```
