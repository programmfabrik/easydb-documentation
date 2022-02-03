---
menu:
  main:
    name: "5.95 (Anfang Februar 2022)"
    identifier: "5.95"
    parent: "releases"
    weight: -595
---

> Für dieses Release ist eine **Neuindizierung nötig**, bitte planen Sie entsprechende Zeit für das Einspielen des Updates ein. 

# Version 5.95.0

*Veröffentlicht am 02.02.2022*

## Webfrontend

### Neu

* **Vorschau**: Anzeige von SVG-Dateien direkt im Browser
* **Editor**: direkte Erstellung von Kindern bei hierarchischen Objekten möglich

### Verbessert

* **Asset-Teilen-Dialog**: neuer Tab, der alle möglichen Versionen zeigt
* **Accessibility**: Verbesserungen an den Tooltips
* **Event-Manager**: Ändern der Spaltenbreite ermöglicht
* **Drucken**: korrekte Anzeige des Maximums für Druck des Suchergebnisses

### Behoben

* **Tabellen-Ansicht**: fehlerhafte Suche korrigiert
* **Suchergebnis**: Anzeige der Hierarchie bei Sortierung nach Pool korrigiert
* **Connector**: Korrekturen bei den Events
* **Editor**: verbesserter Umgang mit zirkulär verknüpften Daten

## Server

### Verbessert

* Die Vorgabe für die Client-Konfiguration `default_client.print_limit` wurde von 250 auf 1000 erhöht
* Die Markierung für aufzuräumende Assets wurde wieder standardmäßig aktiviert

### Behoben

* Die Verlangsamung von `GET /api/v1/db` durch zu viele Cache-Einträge wurde behoben
* Die Suche nach leeren Feldern innerhalb verschachtelter Tabellen funktioniert jetzt auch bei "nested index"
* Bei Assets in mehrfach verschachtelten Nested-Tabellen wird auch die Pool-Referenz gepflegt (wichtig für Wasserzeichen)
* Fehlende SHA2-Checksummen der Assets werden in der Datenbank nachgepflegt (Fehler war bei `rput` aufgetreten, wurde bereits korrigiert)

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:cee0518bdf9ffcd5590b339326586af671bca47d16f74f4231017dc88faef939
docker.easydb.de/pf/eas                  sha256:3242292f7994c6901564430c3915d31cbc3759a4b83bcda8e0b5e0875ea995b7
docker.easydb.de/pf/elasticsearch        sha256:d616f0924d38e5594968243718f395e8fd9aab6b1151f23b8cf27f23903ef9fb
docker.easydb.de/pf/fylr                 sha256:999f2bfc6dcd8393f96ca80c626c7e1d9fe403f3e4323e3ebe4d97cb127d8484
docker.easydb.de/pf/postgresql-11        sha256:ea09de013916050d997f14c4ebde8976160850ade022b68d53359a5021eb5de3
docker.easydb.de/pf/server-base          sha256:add26b73e0706e7bc8b87b435d46a3da7ba5329bb4525f8c959879d6c3ef66e8
docker.easydb.de/pf/webfrontend          sha256:4d0da06ed26de76692776fb6f5fa93fbfab9691e098be645ee65bb3eb553c743
```
