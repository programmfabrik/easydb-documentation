---
menu:
  main:
    name: "5.92 (November 2021)"
    identifier: "5.92"
    parent: "releases"
    weight: -592
---

> Diese Version **benötigt keinen neuen Index-Aufbau**, das neue Elastic-Image arbeitet mit den vorhandenen Index-Dateien.

# Version 5.92.0

*Veröffentlicht am 10.11.2021*

## Webfrontend

### Neu

* Share-Button an den Asset-Versionen

### Verbessert

* Schnellzugriff: mehrzeilige Ansicht für gruppierte Objektlisten
* CSV-Import: Name der hochgeladenen Mapping-Datei wird angezeigt
* `_all_fields`-Maskendefinitionen werden nur geladen, wenn notwendig
* redundante System-ID in Druckansicht entfernt

### Behoben

* Javascript-Fehler bei unerwarteter Server-Antwort korrigiert
* verschachtelte manuelle Sortierung korrigiert
* CSV-Import: Fix für Default-Tags
* CSV-Import: Fix für fehlerhaftes/fehlendes Mapping
* Objekttypen von Connector-Instanzen werden nicht mehr im Rechtemanager angezeigt
* Hotfolder: Senden fehlerhafter Mapping-Konfiguration korrigiert
* Deeplink auf Messages korrigiert

## Server

### Neu

* `webp`-Bildformat unterstützt
* Unterstützung für schwedische Lokalisierung (`sv-SE`)

### Verbessert

* Fehlerbehandlung beim Import verlinkter Objekte verbessert
* keine Spezialbehandlung für Sortierfeld in `fields`-Antworten

### Behoben

* Berechnung der SHA224-Prüfsumme bei Import von Assets via `rput`
* fehlende SHA224-Prüfsummen der Assets werden nachberechnet
* Vermeidung falscher Trigger bei Spaltentyp-Änderungen

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version): 

```ini
docker.easydb.de/pf/chrome               sha256:29b9cbc9d8a53a263b2f995588fffe323cafad67d70307f92d51c8eedda4da7a
docker.easydb.de/pf/eas                  sha256:0078e914d8a9ec4cfae6e813c61c3d746974b835bf9a154b0fda77f116b97e9e
docker.easydb.de/pf/elasticsearch        sha256:db2b1a10642527d6f319356552aa7d63e69ea086dc8b6f61a25455462acab201
docker.easydb.de/pf/fylr                 sha256:879881269be708e8f1d0d4a274ba83f21a5cd4adcc10abae098f0340a816f514
docker.easydb.de/pf/postgresql-11        sha256:47e9c630cbca425e43cf00c6a0bc17831bf152811f7f3963dcfd1ed84620f4e6
docker.easydb.de/pf/server-base          sha256:0ad1bc46eb4f779f493b6c91c2277727cc0ec0910b1e816eccae63dcdb501f9e
docker.easydb.de/pf/webfrontend          sha256:6be72be56ea5c16c4395a3e0fa6784e14ec2c4973285f98b0eaa221b1d093589
```

