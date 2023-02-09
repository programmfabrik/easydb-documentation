---
menu:
  main:
    name: "5.112 (Februar 2023)"
    identifier: "5.112"
    parent: "releases"
    weight: -612
---


> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.112.0

*Veröffentlicht am 08.02.2023*

# Webfrontend

## Neu

* **Änderungshistorie**: neue Option, die Änderungen zur vorherigen Version hervorhebt
* **Detailansicht**: Button im Asset-Browser, mit dem die gerade angezeigte Datei heruntergeladen werden kann

## Verbessert

* **Eingabefelder**: automatische Erkennung der Eingaberichtung
* **Detailansicht**: Deaktivierung aller Werkzeuge und Plugins, wenn die Änderungshistorie geöffnet ist
* **CSV-/JSON-Importer**: URLs mit unkodierten Sonderzeichen können importiert werden
* **Versions-Details**: neue Anzeige, ob Version ein Wasserzeichen enthält
* **Datenmodell-Editor**: Verwendung von Markdown ohne Debug-Modus möglich
* **Detailansicht**: einige Metadaten-Felder in Kurzansicht ausgeblendet

## Behoben

* Systemname aus der Basiskonfiguration wird korrekt verwendet
* Auswahl für verlinkten Pool nur sichtbar, wenn verlinkte Objekte mit Pools in der Maske verfügbar sind
* Method `getSiblingFromData` für Plugins korrigiert

# Server

## Neu

* neue Datensprachen "Katalanisch" ("ca"), "Okzitanisch" ("oc"), "Portugiesisch" ("pt") und "Ukrainisch" ("uk")

## Verbessert

* `/api/v1/objecttype`: beschleunigtes Kurzformat
* Ein-/Ausgabe für `collection.create_object.linked_object_pools`

## Behoben

* Pool-Wasserzeichen-Links in der Asset-Tabelle werden besser gepflegt, Fehler beim Aufräumen so vermieden
* Ablaufzeit von hochgeladenen Assets wird auch für `rput` und in der Basiskonfiguration gesetzt

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.112.0         sha256:bc43f3e689458a0fd4f91d7ad7a828da76c586d8a7fb0d63b08b74bd07a133b5
docker.easydb.de/pf/eas:5.112.0            sha256:8a93a759ef2ad04ceb1821080a38855d7de95a90d5dad5c91537604fa4e530e3
docker.easydb.de/pf/elasticsearch:5.112.0  sha256:f5d982e8a5463ac58e9c03f0aa107cf3588dea33f5bfc2c7d52bd127f853d215
docker.easydb.de/pf/fylr:5.112.0           sha256:cdc2d2352c63b590c095668c92100c595e806be101c4f3afce842bbc67260bf1
docker.easydb.de/pf/postgresql-11:5.112.0  sha256:90025affc266723073046d5d0ffa9d856095034cb9476a2d01eacfcd87bd923b
docker.easydb.de/pf/postgresql-14:5.112.0  sha256:253c5a26cbf18729933d1fe357b93fd5180181f11fb0b70cf4c992f11b9412f7
docker.easydb.de/pf/server-base:5.112.0    sha256:caff79d7bffca636bbe27b364df1232ea77e4b3de796bc6d15b0f5255429db78
docker.easydb.de/pf/webfrontend:5.112.0    sha256:f9c55cd1aa55e6dcc59bdf0c1109cfaba6f1110bc2b71f4bffa4315e62ccca86
```
