---
menu:
  main:
    name: "5.116 (Mai 2023)"
    identifier: "5.116"
    parent: "releases5110"
    weight: -616
---


> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.116.0

*Veröffentlicht am 10.05.2023*


# Webfrontend

## Verbessert

* **Suche**: Hauptsuche wird ausgeführt, wenn Optionen in der Expertensuche oder Autocomplete-Einträge aktiviert werden
* **Allgemein**: Verbesserte Namen für generierte CSV- und JSON-Dateien, z.B. beim Exportieren des Datenmodells
* **Basis-Konfiguration**: Darstellung von Passwort-Feldern verbessert
* **Hauptmenü**: Verbesserte Aktualisierung bei Änderungen an im Hauptmenü enthaltenen Objekttypen
* **Mappen**: Reihenfolge der Menüeinräge optimiert
* **Mappen**: Anlegen neuer Mappen beschleunigt, diese werden ohne Nachfrage direkt auf oberster Ebene angelegt
* **Read-Only-Modus**: Indikator für neuen Read-Only-Modus

## Behoben

* **Schnellzugriff**: Fehler beim Öffnen des Menüs behoben
* **detail-linked-plugin**: fehlende Darstellung korrigiert, wenn Plugin alleiniges Element in Mask Splitter ist
* **Mappeneinstellungen**: Fehler beim Aktivieren der Uploads verhinderte Speichern der getätigten Einstellungen
* **Objekt-Vorschau**: Darstellung korrigiert, wenn Objekte keine Assets enthalten können
* **Hauptmenü**: URL korrigiert bei Klick auf im Hauptmenü enthaltenen Objekttypen
* **CSV-Importer**: Fehler bei Verwendung auf Objekttypen mit display-field-value-mask-splitter korrigiert
* **Editor**: Validierung von Datumsbereichsfeldern verbessert

# Server

## Neu

* **Read-Only-Modus**: in der Basis-Konfiguration aktiviert, wird das Schreiben von Objekten und den meisten Base-Typen unterbunden.

## Verbessert

* `SESSION_INVALID`-Ereignisse werden nicht mehr gespeichert

## Behoben

* Laden von Benutzern mit archivierten Besitzern führt nicht mehr zu Fehlern
* Intranet-Check bricht nicht mehr ab, wenn einzelne Netzwerk-Masken ungültig sind

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.116.0         sha256:9b292c2407f3540c65bd7cf2662a4f3041050f5ba0cc185ce06b8b8ed0fe6505
docker.easydb.de/pf/eas:5.116.0            sha256:cf200ee1e48fa1748490287f74f42df76872f9ecaced3e4ee2902dcf6b3fe6c2
docker.easydb.de/pf/elasticsearch:5.116.0  sha256:a0035a635c38d61f0241cd9de6bbe2d4cbf0f4d072acf19041a77b8b1e67874a
docker.easydb.de/pf/fylr:5.116.0           sha256:a79ecc20278fb3ebd217e9231c409e9be4592b456c342eb21059f55521516336
docker.easydb.de/pf/postgresql-14:5.116.0  sha256:c5a6b41852aeec745bc2c945f282bd092988390a44d277e53e16c6a6d4bc2668
docker.easydb.de/pf/server-base:5.116.0    sha256:1a160b4c8fbe4ad26fb48a328d9589e9f4bbd139629946dc1463eb78a678dbd5
docker.easydb.de/pf/webfrontend:5.116.0    sha256:aefd5bae6bbfc7bc409c2682cefa9eeead354eeeb9133b81ed78907711d7cf69
```
