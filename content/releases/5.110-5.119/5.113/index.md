---
menu:
  main:
    name: "5.113 (Anfang März 2023)"
    identifier: "5.113"
    parent: "releases5110"
    weight: -613
---


> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.113.1

*Veröffentlicht am 03.03.2023*

# Webfrontend

## Behoben

* **Detailansicht**:
  * Probleme mit der Ausgabe der **UUID** des Objekts behoben

# Version 5.113.0

*Veröffentlicht am 01.03.2023*

# Webfrontend

## Neu

* **Detailansicht**:
  * alphabetisch Reihenfolge für verlinkte Objekte im Custom Mask Splitter
* **Präsentation**:
  * neues Format für Slides: Bild und freier Text nebeneinander
* Die **UUID** des Objekts wird in der Fußzeile der Detailansicht und des Editors sowie in der Expertensuche angezeigt

## Verbessert

* **Performance**:
  * Der Objekttyp-Manager lädt schneller, da jetzt das neue `short`-Format der `objecttype` Api genutzt wird
* **Eingabe von Emailadressen**:
  * Die Validierung von eingegebenen Emailadressen folgt jetzt dem `RFC5322` Standard

## Behoben

* **Suche**:
  * Fehler im Kontextmenü "Aus Mappe entfernen" behoben
* **Expertensuche**:
  * doppelter "Nicht enthalten"-Button neben Feld entfernt
* **Detailansicht**:
  * fehlerhafter Status der Checkbox in der Differenz-Ansicht in der Änderungshistorie wurde behoben
* **Mappen**:
  * Problem behoben, wenn Mappen ausgewählt werden, die zwischenzeitlich gelöscht wurden
* **Datenmodell**:
  * doppelte Maskennamen im Maskset werden geprüft bevor sie an den Server gesendet werden

# Server

## Neu

* Neues Format `short` für die `objecttype` Api, um die Übertragung von unnötigen Daten zu vermeiden

## Verbessert

* **Mappen**:
  * Mappen von gelöschten Nutzern werden aus dem Index entfernt
* **Datenmodell**:
  * verbesserte Unique Constraint Checks in Spalten, deren Typ geändert wurde

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.113.0         sha256:184d742babb22902ce3e8db124d04e99f7f20bfe1a752407617293e32a18685d
docker.easydb.de/pf/eas:5.113.0            sha256:46958db7d7af789ee62c9ba535af4e80bae450f29c0eddb8ab5ba161d4f55fa6
docker.easydb.de/pf/elasticsearch:5.113.0  sha256:ad2cf4201f3e46b7e42e0704f9f6382b3a0a45e69eaf8118f3c36d921938b890
docker.easydb.de/pf/fylr:5.113.0           sha256:2378b05ced5aa50ffd07b73b883c265e1f1510d80d3ad91f44a3351da35e5edf
docker.easydb.de/pf/postgresql-11:5.113.0  sha256:48ffbcc1bc716668bff83606434392fb5590406fcd33c643da2e496ee7d4af6d
docker.easydb.de/pf/postgresql-14:5.113.0  sha256:a35666b028a44dd581c582cf3fa5d563b165c5af053a0936e658ee98477ce64e
docker.easydb.de/pf/server-base:5.113.1    sha256:890f2dc7116f81360f3f83429ed81b28697b477ea0c1d39e44fd170153385659
docker.easydb.de/pf/webfrontend:5.113.1    sha256:4db53d12a63b81b86823f8ec4c433b7e53a9a814656fc9924a7c503d1d43d6dd
```
