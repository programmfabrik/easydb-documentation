---
menu:
  main:
    name: "5.134 (Juni 2024)"
    identifier: "5.134"
    parent: "releases5130"
    weight: -634
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.134.1

*Veröffentlicht am 05.07.2024*

# Webfrontend

## Behoben

* **Suche**: Fehler bei der Sortierung nach der Änderungshitorie behoben

# Server

## Behoben

* **Easydb Asset Server (EAS)**: Kodierung von Dateinamen in EAS-Redirect-URLs behoben


# Version 5.134.0

*Veröffentlicht am 19.06.2024*


# Webfrontend

## Verbessert

* **Filter**: Kombination mehrerer Werte mit `AND` oder `OR`, auswählbar in der Filter-Ansicht
* **Asset-Browser**: `vector2d`-Vorschau im Zoomer ermöglicht
* **Hauptsuche**: Menüeintrag zum Aufheben der Auswahl hinzugefügt
* **CSV-Importer**: Mapping mehrerer Spalten zur Befüllung der selben verschachtelten Tabelle ermöglicht
* **Listen-Popover**: Hierarchiemodusauswahl ermöglicht

## Behoben

* **Tabellenansicht**: Update-Verhalten bei Events korrigiert
* **CSV-Importer**: Zuordnung numerischer Daten bei verschachtelten Tabellen korrigiert
* **CSV-Importer**: Position leerer Zeilen bei Import verschachtelter Einträge mit Index korrigiert
* **CSV-Importer**: Suche nach verlinkten Objekten korrigiert, wenn mehr als ein Identifier angegeben wurde
* **Tags**: Anzeige verfügbarer Tags korrigiert
* **Filepicker-Plugins**: leeren Fehler entfernt, falls das CMS bei erfolgreicher Anfrage keine Rückmeldung liefert
* **Editor**: Anzeige der Platzhalter bei Datumsbereichsspalten korrigiert
* **Suche**: Sortierung nach Changelog behoben
* **Listen-Popover**: Öffnen des gesamten Baums beim Laden unterbunden

# Server

## Behoben

* **EAS**: Darstellung von eingebetteten Grafiken in WebDVD-Vorschaubildern korrigiert
* **Rechtemanagement**: Benutzung von Tag-Filtern bei Vergabe von `link`/`unlink` auf Pools behoben

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.134.0         sha256:e0a7ba0e456deddaf7f6e3d2f45d541729372584b5cad3ff52bf0ccf849e7767
docker.easydb.de/pf/eas:5.134.0            sha256:6c7a82834b8a0de3817df864d20346a9e47e4a9a52a0d6ea4c3fc0690d944bc7
docker.easydb.de/pf/elasticsearch:5.134.0  sha256:69b78bf26196f74011c5b5cd4a3415a1f8a5e33b758829fa60570a27a3581831
docker.easydb.de/pf/fylr:5.134.0           sha256:36964511e3a522a1d59a375d52f073dffbef1333687077065dd063a7d6f16fc6
docker.easydb.de/pf/postgresql-14:5.134.0  sha256:d705d451b0ffb5b6f6cf2f3bc11ae862df1f6c82c098c8aba684d9211e7f969d
docker.easydb.de/pf/server-base:5.134.1    sha256:30000ecb75b5a5526de24e079212f1a7a65044693a4030b26b8d7027d8abb904
docker.easydb.de/pf/webfrontend:5.134.1    sha256:46ef361d1aede63c96239127733d88b8173d6790009f37297fe98ea4fd60d999
```
