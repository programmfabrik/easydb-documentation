---
menu:
  main:
    name: "5.146 (Ende Juli 2025)"
    identifier: "5.146"
    parent: "releases"
    weight: -646
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.146.1

*Veröffentlicht am 31.07.2025*

# Webfrontend

## Behoben

* **Export**: Fehler beim Export des Suchergebnisses behoben

# Version 5.146.0

*Veröffentlicht am 30.07.2025*


# Server

## Verbessert

* **/api/db?all_versions**: `_child_idx` & `_parent_child_idx` hinzugefügt, um in einigen Fällen die korrekte Sortierung von migrierten Daten zu ermöglichen

## Behoben

* **/api/db?all_versions**: Auswahl von doppelt verschachtelten Einträgen korrigiert; Duplikat-Erkennung verbessert

# Webfrontend

## Behoben

* **Event-Manager**: verschiedene Probleme mit einigen Ereignissen korrigiert
* **Gruppierung**: Problem mit Kopfzeilen bei Sortierung behoben
* **Gruppeneditor**: Update des "Speichern"-Buttons bei manchen Änderungen korrigiert
* **Tags**: unerwünschte Icons in manchen Tags korrigiert, wenn deren Namen gleich einem System-Icon ist
* **Vollbild-Detail**: Fehler behoben, wenn Hierarchie-Liste in der Detail-Seitenleiste im Vollbild geöffnet war

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.146.0            sha256:b203fa1bc898a57d8ba67e4b1f82593d4bbdc53241f0024925734e55bc5ddfad
docker.easydb.de/pf/elasticsearch:5.146.0  sha256:07a0ff763ba5029769b9686dce16a8830e3510ef37202584b94270d91273b67a
docker.easydb.de/pf/fylr:5.146.0           sha256:5de5a8f90a3e27eb6bf506b44b5b17ff7dcd2903d9697fdb723aca4f9f052710
docker.easydb.de/pf/postgresql-14:5.146.0  sha256:298cd7ec49ee09f66b254cae39504cdbed5ddeec5e889c0ddb3785ddea9f2d1a
docker.easydb.de/pf/server-base:5.146.1    sha256:52c59c85c2366e4e16d85a94086021815132de26cddecf60fbb34eb9e14ab35d
docker.easydb.de/pf/webfrontend:5.146.1    sha256:4b7382fffd9c8953920ff092baf9b6bd4e4f58c81dd36c7e78a90055e66e0988
```
