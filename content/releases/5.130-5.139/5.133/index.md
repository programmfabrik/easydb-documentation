---
menu:
  main:
    name: "5.133 (Ende Mai 2024)"
    identifier: "5.133"
    parent: "releases5130"
    weight: -633
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.133.0

*Veröffentlicht am 29.05.2024*


# Webfrontend

## Verbessert

* **Standard-Ansicht**: Konfiguration der Ansichtsmodi verbessert, Option zum Ausblenden der Info
* **CSV-Importer**: es ist jetzt möglich, dasselbe verlinkte Objekt in verschiedenen Mappings zu verwenden
* **Tag-Editor**: Design verbessert
* **Mitteilungen**: Ständige Hinweise (Hauptmenü/Kopfzeile) öffnen nur den Link statt eines Popups, wenn nur ein Link angegeben wird

## Behoben

* **PDF-Druck**: Felder wurden nicht korrekt ausgeblenden, obwohl sie in den Einstellungen abgewählt wurden
* **Metadaten-Mapping**: Zuordnung der Daten zum korrekten verschachtelten Element
* **PDF-Druck**: jetzt kompatibel mit der Tabellenansicht bei verschachtelten Feldern

# Server

## Behoben

* Fehler beim Ändern der Reihenfolge von verschachtelten Feldern mit Assets korrigiert

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.133.0         sha256:0355b3149203cd65a9400299b0ec32e8fe488125481b0d65bb67519570e75164
docker.easydb.de/pf/eas:5.133.0            sha256:7f0dd427f3a2db7c858d9b67bba6ac96eedf7c8c06e0e8579b84140b97759d60
docker.easydb.de/pf/elasticsearch:5.133.0  sha256:2b836e1442365416b2924a4496cfe324385469e28d339fdd50d231c5071534b1
docker.easydb.de/pf/fylr:5.133.0           sha256:ce77c10c357c976b3711baa7ea7b99754335058d90a660fa3ad6de2e678bdc5a
docker.easydb.de/pf/postgresql-14:5.133.0  sha256:004542d0d9555b9d02195597b1844d93b8a80ce2777e4a1476764f74ced048f2
docker.easydb.de/pf/server-base:5.133.0    sha256:a8318066c65ac134f69d5f2db0a8ba4270cc3125e175b0e7cafce4d10c67a9b0
docker.easydb.de/pf/webfrontend:5.133.0    sha256:e3111d6815a09fd578c83d2a37828c3cb6ab0db811dc581c8e2e440a22ac165f
```
