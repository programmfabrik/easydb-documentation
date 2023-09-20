---
menu:
  main:
    name: "5.122 (September 2023)"
    identifier: "5.122"
    parent: "releases"
    weight: -622
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.122.0

*Veröffentlicht am 20.09.2023*

# Webfrontend

## Neu

* **Basiskonfiguration**: für Änderungen in bestimmten Werten (z.B. "E-Mail"-Einstellungen) muss der User diese Änderungen vor dem Speichern bestätigen
* **Plugins**: Plugins werden mit dem Wert von `name` angezeigt
  * der Wert `display-name` ist veraltet und wird ab sofort nicht mehr genutzt
* **Detailansicht**: in der Änderungshistorie wird immer der verantwortliche User angezeigt

## Verbessert

* **Druckmanager**: verbesserte Feldauswahl
* Korrekturen in der textuellen Darstellung von Datumsbereichsfeldern
* Standard-Sucheinstellungen für Mappen wurden geändert, um 100 Objekte statt 10 anzuzeigen
* **Display Field Values Plugin**: weitere Top-Level-Felder wurden hinzugefügt, die ausgewählt werden können

## Behoben

* **Ereignisse**: mehrere kleinere Fehlerkorrekturen
* **Detailansicht**: Fehler in Schaltflächen im Template-Manager (Vorlagen) wurden behoben
* **Json Importer**: Probleme beim Ersetzen von URLs behoben

# Server

## Neu

* **XML Export**: Exportieren von revers verlinkten Objekten: Ausgabe von `_version` und `_pool` hinzugefügt

## Verbessert

* **Performance**: kürzere Ladezeiten für (unverändertes) Schema und Maskset

## Behoben

* EAS URLs für Dateien, die von einer entfernten URL in die easydb5 eingefügt wurden, wurde der generierte Dateiname korrigiert
* **XML Export**: Exportieren von revers verlinkten Objekten: Ausgabe der `_id` korrigiert
* **Datenmodell**: `UNIQUE`-Constraints für Datumsbereich-Felder korrigiert

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.122.0         sha256:dbca3ff79c4853f2c6b683af8ecf48da05939923a44769062c37aa1e39caffb3
docker.easydb.de/pf/eas:5.122.0            sha256:2c50af6c3aac6136d81e1d4f4a2ff08359a89162cb45d770ebecdc109bdc3b82
docker.easydb.de/pf/elasticsearch:5.122.0  sha256:bd3f0199ae861484335ffa00be9e3d023cfd0a96066a8563b61a4077e19b4236
docker.easydb.de/pf/fylr:5.122.0           sha256:f1e2e6e68011e39b54627ab0efe74027cad5e9b23af2785f2807a4bcd882edf6
docker.easydb.de/pf/postgresql-14:5.122.0  sha256:ee1b5ab450b2fd1e3c0954009da188283db6215c83aad20daf65b77c81799793
docker.easydb.de/pf/server-base:5.122.0    sha256:a9a495c3a67082b143de74a583f5c98afb2d043413d1cd3c10b5cd46236788e1
docker.easydb.de/pf/webfrontend:5.122.0    sha256:641ef40f79309007619f0360490159762a42fa89b21c94eea2f5ef913bbedba0
```
