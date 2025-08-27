---
menu:
  main:
    name: "5.147 (Ende August 2025)"
    identifier: "5.147"
    parent: "releases"
    weight: -647
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.147.0

*Veröffentlicht am 27.08.2025*

# Server

## Behoben

* **Suche**: inkompatible Änderung an der Phrasensuche in String-Feldern zurückgesetzt
* **Docker-Container**: hohe UIDs/GIDs einiger Dateien ersetzt

# Webfrontend

## Behoben

* **Nested- und Reverse-Nested-Tabellen**: bei Verwendung der "readonly"-Option in den Masken kam es dazu, dass Daten beim Speichern nicht korrekt gesendet wurden.
* **Print-Manager**: es wird sichergestellt, dass alle Bilder geladen sind, bevor der Browser-Druck aufgerufen wird.
* **Nested-Einträge**: Lösch-Knopf verbessert, sodass immer eine leere Zeile angezeigt wird, wenn das so konfiguriert ist.
* **CSS**: verschiedene Anpassungen und Fixes

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.147.0            sha256:60d835e6afa49690ae5b8f91c056070751044b3a4678fdc5a8fb932b2bc45501
docker.easydb.de/pf/elasticsearch:5.147.0  sha256:2afe7cb91c3ba1d36d80e2929e84904cbf694fab5e9fba60004fa44eeb21125c
docker.easydb.de/pf/fylr:5.147.0           sha256:289c4c1c6418636ed6b7735e31296fb9967ee45e0ac67264ac78a76972d8e782
docker.easydb.de/pf/postgresql-14:5.147.0  sha256:7440d687452800694b86db7aa3627a07d3505d0c21e605dc1f5d25a9f0693702
docker.easydb.de/pf/server-base:5.147.0    sha256:6dbb178e20d095ea743f1ff7c6a17fef6b192fc04a2cbbc024763d31b5c3432b
docker.easydb.de/pf/webfrontend:5.147.0    sha256:00d732e5f7bf227605c0128c389904f68d332bfb8a49654346045a2e615480f4
```
