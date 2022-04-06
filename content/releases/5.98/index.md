---
menu:
  main:
    name: "5.98 (April 2022)"
    identifier: "5.98"
    parent: "releases"
    weight: -598
---

> Diese Version **benötigt keinen neuen Index-Aufbau**

# Version 5.98.0

*Veröffentlicht am 06.04.2022*

## Webfrontend

### Verbessert

* **Allgemein**: durchgehende Verwendung von Tausender-Trennern für Zahlen
* **Filter**: Überschriften für verlinkte Objekte verbessert
* **Basis-Konfiguration**: Ace-Bibliothek wird nicht mehr von externen Ressourcen geladen

### Behoben

* **CSV-Importer**: Problem mit System Object ID in Hierarchien behoben
* **CSV-Importer**: Vorschau für verlinkte Objekte korrigiert
* **JSON-Importer**: Fehler bei Verwendung des Lookup-Features und mehr als 1000 IDs in der Suche behoben
* **Editor/Detail**: Masken-Optionen zur Anzeige von Objekttyp/Pool für verlinkte Objekte behoben
* **Suche**: Fehler bei Assets in verschachtelten verlinkten Objekten behoben
* **Editor**: Pool wird beim Ändern nicht für reverse-verlinkte Eltern-Elemente gesetzt
* **Metadaten-Mapping**: verfügbare Felder werden nicht fälschlicherweise durch Masken gefiltert

## Server

**TODO**

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:451a6d6e05936ed704277c6842b4ad3119f25a2ed5631734f71049f3b8069cc4
docker.easydb.de/pf/eas                  sha256:0235560e53e26085e639bf616733b6eea311a3ca68e70332bec4f69356281d17
docker.easydb.de/pf/elasticsearch        sha256:bac077eb81d38b8f6e6506ffea7a5c26e5043832e6747886b2e7b12484cc57d7
docker.easydb.de/pf/fylr                 sha256:b3bfa2edbaad51563d8165fd52c7c0ab8cdf78ac2f42cd62e511487bb5d5e279
docker.easydb.de/pf/postgresql-11        sha256:b3562998e544ca25271b15a46ca10cf53025798cf7b9707e758063252b936986
docker.easydb.de/pf/server-base          sha256:528d06b51d69d541e718c4342dd72d8c9c9dc5f2dcdbe11ad46ffe006cfda70f
docker.easydb.de/pf/server-base-py3      sha256:ee5cc91b4f691fa4c6664cb96f13e80c802d44c213866e9e134ec6db9f74bb65
docker.easydb.de/pf/webfrontend          sha256:7c320085c309f2fc42efab133d836dc71f7cc598a8710b4a4ea509f0d2689421
```
