---
menu:
  main:
    name: "5.131 (April 2024)"
    identifier: "5.131"
    parent: "releases5130"
    weight: -631
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.131.0

*Veröffentlicht am 10.04.2024*


# Webfrontend

## Neu

* **Listen-Ansicht**: Filter-Manager ist jetzt in den Listen verfügbar.

## Verbessert

* **Filter-Manager**: Mitteilung statt leerer Seite, wenn keine Filter verfügbar sind.
* **Asset-Browser**: Name der gerade dargestellten Asset-Variante wird angezeigt.
* **Benutzer-Konfiguration**: Anpassung der notwendigen Felder bei Konfiguration des eigenen Benutzers.
* **System-Meldungen**: Verbesserungen der Nutzbarkeit.

## Behoben

* **Allgemein**: zahlreiche Korrekturen im CSS.
* **Vollbild-Ansicht**: Auswahl der dargestellten Asset-Variante korrigiert.
* **Pool-Auswahl**: für die Struktierung notwendige, aber nicht verwendbare Pools werden nicht mehr auswählbar dargestellt.
* **CSV-Importer**: zahlreiche Korrekturen bei der Suche verlinkter Objekte.
* **Masken-Editor**: Darstellung der Option "Feldname ausblenden" für verschachtelte Felder korrigiert.
* **Hauptsuche**: Darstellung in der Suche nach Kopieren eines Objekts behoben.
* **CSV-Importer**: Metadaten-Mapping bei Verwendung von RPUT zum Hochladen eines Assets korrigiert.
* **Filter-Sortierung**: Sortierung für Custom-Typ-Felder korrigiert.
* **Suche**: Verhalten bei Doppelklick zum Editieren eines Such-Tags behoben.

# Server

## Verbessert

* **Webhooks**: Server-Antwort wird zur Diagnose in `WEBHOOK_ERROR`-Ereignis gespeichert.

## Behoben

* **/api/objects**: besserer Fehler bei unbekannter UUID, es wird keine Fehlerdatei erstellt, wie es bei unerwarteten Server-Fehlern geschieht.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.131.0         sha256:c4c775d6986e532ec47076206c2d14d55e159bfe6014535fac1ccbe6a43d2963
docker.easydb.de/pf/eas:5.131.0            sha256:d2b08de3d9a65b7adfedd30ff4624c3cf7c3798144d59670fb554545fffb759c
docker.easydb.de/pf/elasticsearch:5.131.0  sha256:7274934dd0a1f827d3427f1305915ccdf7e5d84b5b647df60183f9e60747171e
docker.easydb.de/pf/fylr:5.131.0           sha256:1a18e12b4181a457bb1072f08a97a8029cb99afd04484a9109ab8f9eca3c1751
docker.easydb.de/pf/postgresql-14:5.131.0  sha256:eac1d8c752478c05aba4f599c42f42be48990df69c278d74456c1992a77a77da
docker.easydb.de/pf/server-base:5.131.0    sha256:0dafc1a150bc4493896d6d44b9334bae4172f16c959fdf39260d4246645cd702
docker.easydb.de/pf/webfrontend:5.131.0    sha256:a726e01fee390da4052033bd90caa819228337951c6fe56d40b71d9dfbe76e32
```
