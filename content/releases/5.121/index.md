---
menu:
  main:
    name: "5.121 (Ende August 2023)"
    identifier: "5.121"
    parent: "releases"
    weight: -621
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.121.0

*Veröffentlicht am 30.08.2023*
#
# Webfrontend

## Neu

* **Detail**: Tabellenansicht für Mehrfachfelder

## Verbessert

* **Ereignisse**: Deselektierung von Ereignissen in der Liste ermöglicht

## Behoben

* **Allgemein**: fehlende Übersetzungen ergänzt
* **Rechte-Migration**: Script-Fehler behoben
* **Pool-Editor**: Script-Fehler beim Bearbeiten von Berechtigungen behoben

# Server

## Behoben

* **XML-Export**: `_system_object_id` und `_id` fehlten für reverse-verlinkte Objekte
* **Metadaten-Mapping**: Profil "EMPTY EXPORT (ersetzen)" entfernt jetzt auch vorhandene Tags (wie bereits "EXPORT (ersetzen)")
* **DB-Upgrade**: Nachtragen von System-Object-IDs ignoriert jetzt Nested-Tabellen (nur für zukünftige Upgrades oder falls das letzte Update noch nicht eingespielt wurde)

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.121.0         sha256:12ec606e26a0a03c41421dd0410edef3f1214ebabf23455298c92f419d1ecf25
docker.easydb.de/pf/eas:5.121.0            sha256:acd256e6304b76c58202cb8aa5a491f7834c667ba219510d76dbbb37749ca39c
docker.easydb.de/pf/elasticsearch:5.121.0  sha256:36a4bf23d315ed9a709b1c914e5d5b65b468371589b535fea053a9963a2149dd
docker.easydb.de/pf/fylr:5.121.0           sha256:ff16e83208f29be0a422670b2c36804ebf58ae8e17602bd31f0d202e8ed4dde3
docker.easydb.de/pf/postgresql-14:5.121.0  sha256:ac2adbc20e0c7031879847515385f80ecc71874f432e1db3a0b165fcb9009c05
docker.easydb.de/pf/server-base:5.121.0    sha256:494f811ac33b4b3ab96422d2bd5fb6527f0383f01cab2a8149e627002f5ce057
docker.easydb.de/pf/webfrontend:5.121.0    sha256:3c9b66abaa37e28bbdc3bf3db52fff1520e79181ef12b62b11cb2aa4afc6b29e
```
