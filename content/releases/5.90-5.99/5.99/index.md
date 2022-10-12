---
menu:
  main:
    name: "5.99 (April 2022)"
    identifier: "5.99"
    parent: "releases599"
    weight: -599
---

> Diese Version **benötigt keinen neuen Index-Aufbau**

# Version 5.99.0

*Veröffentlicht am 27.04.2022*

## Webfrontend

### Verbessert

* **Tabellenansicht**: Felder reverse-verknüpfter Objekte wieder sichtbar
* **Allgemein**: anderer Dialog-Typ bei Server-Nachfragen
* **Datenmodell-Editor**: Markierung für Standardmaske
* **Datenmodell-Editor**: Masken-Option zur Anzeige der System-Object-ID verlinkter Objekte in der Textanzeige

### Behoben

* **Gruppeneditor**: Verwendung von Vorlagen korrigiert
* **Editor**: Pool an reverse-verknüpften Objekten wird nicht geändert, wenn Haupt-Pool aktualisiert wird
* **Suche**: Anzeige der ausgewählten Expertensuche korrgiert
* **Filter**: Zählung bei mehreren ausgewählten Filtern korrigiert
* **Suche**: Fehler bei "Ohne"-Suche nach Boolean-Feldern korrigiert
* **Editor**: Vorlage beim Erstellen von Objekten enthält reverse-verknüpfte Felder (nicht im Gruppeneditor)
* **Detail**: Fehler bei Anzeige untergeordneter Objekte korrigiert
* **Arbeitsmappen**: Fehler bei Upload mehrere Assets behoben

## Server

### Neu

* **Suche**: Suchtypen `user` & `group` benötigen keine zusätzlichen Systemrechte mehr
* **Allgemein**: neuer Sprachcode `smi` (Samisch)
* **Event-Polling**: `info`- und `pollable`-Felder nicht mehr in `/api/v1/event/poll` verfügbar

### Behoben

* **EAS**: Fehlerkennung von nxs-/nxz-Dateien korrigiert
* **Suggest**: Highlighting korrigiert
* **objects-API**: Check für Datei-Index korrigiert
* **Suche**: Suchtyp `acl` erlaubt immer Lesen des anfragenden Nutzers
* **Custom-Datatype-Updater**: Indizierung geänderter Objekte auch im Fehlerfall sichergestellt

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:0937c04eb4377979bd6c88a53c8031677335b8dd00e5a374465f335b01410e3d
docker.easydb.de/pf/eas                  sha256:5ce17eabb860e340a1f7fe5fb3a9c5cc988ebd8916f4a794dd1ef160bcbd03e0
docker.easydb.de/pf/elasticsearch        sha256:c4fe3bd00d884cc8f9a03dedb924a18c65218a16f04b141cdcb0e1a39d699492
docker.easydb.de/pf/fylr                 sha256:3c62bdd33fdd3b6c2cfc339baf817ca989058eb4c2bc1401f2ecd9667c00734d
docker.easydb.de/pf/postgresql-11        sha256:1bc3449abc2511c5445af5088f4bb15f6f8baa05feb53aba9304aa1929f784ad
docker.easydb.de/pf/server-base          sha256:95b5002f574710844096c935507113b1bbd0b5e6115c3bdc12bfa0518ef6f9c2
docker.easydb.de/pf/server-base-py3      sha256:ee5cc91b4f691fa4c6664cb96f13e80c802d44c213866e9e134ec6db9f74bb65
docker.easydb.de/pf/webfrontend          sha256:fb11c50387a45e73758b8f9b65758b23cb2efea0ea2984dee06c2ab88bd09ed7
```
