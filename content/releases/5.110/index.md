---
menu:
  main:
    name: "5.110 (Dezember 2022)"
    identifier: "5.110"
    parent: "releases"
    weight: -610
---

> Dieses Update erfordert einen Re-Index, planen Sie entsprechende Downtime / Updatezeit ein

# Version 5.110.0

*Veröffentlicht am 14.12.2022*

# Webfrontend

## Neu

* **PDF-Creator**: Verwendung von Variablen-Ersetzungen in Feldern möglich

## Verbessert

* **Detail-Anzeige**: Bezeichner in Dateieigenschaften übersetzt
* **Tagfilter-Defaults-Plugin**: Pool-Filter jetzt möglich

## Behoben
* **Collection-Einstellungen**: Anzeige des falschen Felds zum Hochladen korrigiert
* **PDF-Creator**: unter bestimmten Umständen konnte die Erstellung von PDFs fehlschlagen, wenn Assets aus dem Standard-Feld verwendet wurden
* **PDF-Creator**: Feldauswahl funktionierte nur beim ersten Versuch
* **Export-Manager**: Anzeige des "Dateien"-Tabs behoben
* **Video-Player**: Anzeige der Qualitätsauswahl im Safari verbessert
* **Allgemein**: Laden des Logos korrigiert
* **Expertensuche**: API-Fehler beim Vervollständigen von Dateinamen behobeb

# Server

## Verbessert

* **Hotfolder/Collection-Upload**: Verwendung von Zielfeldern in Reverse-Nested-Tabellen möglich
* **Allgemein**: neue Datensprache "Hebräisch" hinzugefügt

## Behoben

* **Janitor**: Aufräumen von Assets korrigiert, es gab Fehler bei veralteten Pool-Wasserzeichen
* **EAS**: `target_size_min`-Option funktioniert jetzt auch bei Video-zu-Bild-Konvertierung korrekt

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:115035c8035906f90d7d6bacb52137f018c669b70274a364df05d112ad39bb6c
docker.easydb.de/pf/eas                  sha256:84866d95f5029327c6ca65cadcabb9185f820ea1495ac24a9cd2ea34099fb3d5
docker.easydb.de/pf/elasticsearch        sha256:88770255956de0170b45b02574201d0e8b1516dae5023b1ae6b268ff3c6af4d1
docker.easydb.de/pf/fylr                 sha256:e737f296f9839ec2c0ac56454ca9e23d0f39edc666725c423bdf16206eb9f992
docker.easydb.de/pf/postgresql-11        sha256:2d9cd4da24fd7bc4748b3ad9cacd9354783b7fc9c150f59525bb51f085e289af
docker.easydb.de/pf/postgresql-14        sha256:c208c18c792e6513b862c120da45948ac49aa87c83bbca9af3fab685e0124206
docker.easydb.de/pf/server-base          sha256:f35fd7c750da2771bbba59515f98e207dc29813bee362b070ec008d8627fdea7
docker.easydb.de/pf/webfrontend          sha256:1b9668287c8dc73e37f2e209ad3d8a92a509f2663f822b5aa6cf7bf0bb6fa585
```
