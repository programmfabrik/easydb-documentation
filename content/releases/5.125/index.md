---
menu:
  main:
    name: "5.125 (Ende November 2023)"
    identifier: "5.125"
    parent: "releases"
    weight: -625
---

> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.125.0

*Veröffentlicht am 22.11.2023*


# Webfrontend

## Neu

* **Schnell-Ansicht**: Asset-Browser bei Ansicht verlinkter Objekte verfügbar
* **Asset-Browser**: animierte GIFs können abgespielt werden

## Verbessert

* **PDF-Druck**: Änderungshistorie kann optional am Ende der Seite angezeigt werden
* **Datenmodell-Editor**: verbesserte Fehlerbehandlung bei Verwendung des Objectstores
* **CSV-Importer**: Überprüfung auf nicht vorhandene Eltern-Objekte
* **Vollbild-Ansicht**: beim Wechsel des Objekts wird die Auswahl in der Hauptsuche entsprechend aktualisiert
* **Masken-Editor**: verschiedene Verbesserungen
* **Standard-Ansicht**: passendere Asset-Version wird verwendet

### Behoben

* **Hauptsuche**: Korrekturen für die Filter-Leiste
* **Geteilte Suchen**: alle Parameter werden per URL übermittelt
* **JSON-Importer**: Fehler bei Verwendung von ID-Lookups in Objekten mit URL-Assets behoben
* **Vollbild-Ansicht**: Multimedia-Wiedergabe stoppte nicht korrekt, wenn Objekt gewechselt wurde


# Server

## Behoben

* Seitenverhältnis für Versionen rotierter Videos korrigiert
* Laden von Bildern mit undefinierter Auflösung behoben


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.125.0         sha256:c9edf7be3cf068ce9558344ab6efdc7d9e6f65647cdfa99832b309909348c225
docker.easydb.de/pf/eas:5.125.0            sha256:108dd4864af5cfd32f5dee4ffef044f1363bd8db208a0782de7ab8e9dc4a1ce3
docker.easydb.de/pf/elasticsearch:5.125.0  sha256:f34eb6e02820efbf9db5a175d080a200a536307349f4a6a411cefcc79b7a1b08
docker.easydb.de/pf/fylr:5.125.0           sha256:0576800ac4b9f8fcd69a627d87ed34252e03ba3851e9eda24d22bf2aab158df3
docker.easydb.de/pf/postgresql-14:5.125.0  sha256:b7f6984ce0ae1ae85bfa5af2063086a4308a9ec119ddb988d646432442f31dfd
docker.easydb.de/pf/server-base:5.125.0    sha256:59b1e9df7b1abcbbf5bf2c33934c4026791c27cdfe20ec5d276e450b053cc015
docker.easydb.de/pf/webfrontend:5.125.0    sha256:7f95b7ba14c5e9881b2fd56ec630798c8de52897273ebf2feb196ff75f7f71e6
```
