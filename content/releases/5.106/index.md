---
menu:
  main:
    name: "5.106 (September 2022)"
    identifier: "5.106"
    parent: "releases"
    weight: -606
---

# Version 5.106.0

*Veröffentlicht am 21.09.2022*

> Dieses Update erfordert einen Re-Index, planen Sie entsprechende Downtime / Updatezeit ein

# Webfrontend

## Neu

* **Video-Player**: Untertitel-Dateien können hochgeladen und im Video verwendet werden

## Verbessert

* **Export**: Auswahl im Dialog, ob verlinkte Objekte exportiert werden

## Behoben

* **Login**: Beschriftung des SSO-Buttons korrigiert
* **Dubletten-Check**: durch Bild verdeckten Text wieder sichtbar gemacht
* **Upload**: Javascript-Fehler entfernt
* **Detail**: Fehler beim Öffnen des Details behoben
* **Neue Datensätze**: Auswahl für Pool verlinkter Objekte wird angezeigt, wenn nötig
* **CSV-Importer**: fehlerhaftes Parsing korrigiert
* **CSV-Importer**: mögliche Endlosschleife bei Verwendung vieler Felder korrigiert
* **Mappe teilen**: Vorschau verwendete existierende Session, was zum Ausloggen führte
* **Expertensuche**: Fehler bei Verwendung von Connectoren korrigiert
* **Vollbild-Ansicht**: Fehler beim Öffnen des Details behoben
* **Upload**: Anzeige der Vorschau behoben, z.B. bei Videos

# Server

## Behoben

* **Wildcard-Suche**: einzelne Begriffe werden jetzt UND-verknüpft gesucht, wie bei anderen Such-Modi auch
* **Vorschauberechnung**: unter Umständen wurde nicht erkannt, dass Berechnungen notwendig sind
* **Export**: Speichern von Transport-Definitionen an Exporten korrigiert
* **Hotfolder**: Behandlung des Pools für verlinkte Objekte korrigiert

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:6cfaac8df2e341c2fbe0b49d5cd6020c15fa39ee93f36348141f07c20b342bd0
docker.easydb.de/pf/eas                  sha256:74830079a85b7d557af066dcc4b11d5b9fa3262f6361361b5f7c3d9988e4eaad
docker.easydb.de/pf/elasticsearch        sha256:e4a937ea817ee833388103a7fb14650fd2973e4e989e43979610629cd35187c7
docker.easydb.de/pf/fylr                 sha256:88c997a80224d6210f946bf78272237e066c4426221527aec7c249578c767ff3
docker.easydb.de/pf/postgresql-11        sha256:db10bb134cdb452d71368b7a21b8aba6329a81e3ad85b8493f552075d475e2be
docker.easydb.de/pf/postgresql-14        sha256:37c049a62eada24218f13ec760d4b48f686b793d89622464d18bfc48693b2185
docker.easydb.de/pf/server-base          sha256:c88c59cf4f3e3c1b90a7a9b026ef7f9d6879c57d7d5c51ceb363ee0588c075f7
docker.easydb.de/pf/webfrontend          sha256:d129b8e46e260c66aa3948a03991a02924afddb501265188446d6fe31a55fde3
```
