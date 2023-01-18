---
menu:
  main:
    name: "5.111 (Januar 2023)"
    identifier: "5.111"
    parent: "releases"
    weight: -611
---


> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.111.0

*Veröffentlicht am 18.01.2023*

# Webfrontend

## Neu

* Neue Schaltfläche zur Anzeige der Eltern eines Datensatzes in der Hauptsuche für hierarchische und polyhierarchische Objekte hinzugefügt
**Maskeneinstellungen**:
  * Neue Tooltips für Ein-und Ausgabe-Einstellungen hinzugefügt
  * Der Pfad von hierarchisch verknüpften Objekten wird im Textmodus angezeigt, dies kann in den Maskeneinstellungen der verknüpften Objektfelder gesteuert werden
  * Es ist möglich, einen Datensatz auszuwählen, um eine Vorschau der Maskeneinstellungen im Maskenkonfigurationsfenster anzuzeigen

## Verbessert

* **PDF Creator**:
  * Neue Schaltflächen zum Auf- und Abwärtsbewegen von Elementen in der Liste hinzugefügt
  * Weitere Tiefen für den Feldknoten hinzugefügt, jetzt können Felder bis zur Tiefe 3 ausgewählt werden
  * Fehler behoben, bei dem die Vorschau nach dem Ändern eines Feldknotens nicht gerendert wurde
* **Suche**: Verbessertes Rendering der Hauptsuche, um die Anzahl der Renderaufrufe zu verringern und die Leistung zu verbessern
* Die Kalender-Schaltfläche wird deaktiviert, wenn ein Datum vor Christus in das Datumsfeld eingefügt wird
* Die Farbe der Links in den Pool-Tooltips wurde geändert, um den Kontrast zu erhöhen

## Behoben

* Fehler im Filter für verknüpfte Objekte bei Objekttypen behoben, wenn alte Datenmodellfelder zur Erstellung eines Filters verwendet wurden
* Mehrere Fehler im Tag Management Tool in der Hauptsuche behoben
* Fehler bei Ersetzungen für Download-Nachrichten behoben
* Ein Problem mit Feldern, die in der Metadaten-Mapping-Konfiguration als Liste markiert sind, wurde behoben
* Das Verhalten der Schließen-Schaltfläche im Vollbild-Detailmodus wurde behoben
* Fehler mit Vorschlags- und Verbindungsfeldern behoben
* Der Vorschau-Platzhalter für `processing` Datensätze in der Hauptsuche wurde korrigiert
  * Die Größenangabe des Bildes wird nicht mehr im Assetbrowser angezeigt, wenn das Bild noch in Bearbeitung ist


# Server

## Neu

* **Plugins**: Übersetzungen in finnischer und schwedischer Sprache in verschiedenen Plugins

## Behoben

* **Datenmodell**: Mögliche Fehler beim Aktivieren von mehrsprachigen Feldern behoben
* **XML Metadatenmapping**: Fehler beim Im/Export von Daten in Listen behoben


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.111.0         sha256:ef7e8117c83253351f51a408ef0707a306db5779a5f3bfeca7fd63b6abb4aac7
docker.easydb.de/pf/eas:5.111.0            sha256:2f9396e47c51545f3ba0b05b3addf9ff866b1c218cd2d7e255c1dc3ecefcca0f
docker.easydb.de/pf/elasticsearch:5.111.0  sha256:59959716bbe807afe86fb0c58d46599c87d77aaa130b0a489b064b1156cfdab8
docker.easydb.de/pf/fylr:5.111.0           sha256:2b471ace6ae7df7f79e76c32f841aa9eaba090da70ae187124905b0e3ddaf2da
docker.easydb.de/pf/postgresql-11:5.111.0  sha256:ae69be481c062daf7dfb37578ff006b0ba8ef9a3c56dfdff4984711ce3c59b16
docker.easydb.de/pf/postgresql-14:5.111.0  sha256:ca05b4ee6affd68d680fbbed9c7a28368eb26ec5b637d814cd52a17d9c9885c6
docker.easydb.de/pf/server-base:5.111.0    sha256:38959b7a70ce0a62e91a8dd3ae068f8d6aa4d7d82f4723675804933afcdbcc2b
docker.easydb.de/pf/webfrontend:5.111.0    sha256:5702c41510feb83b81231858ba404a6dc062f3c867095c97419d214fd94e55e8
```
