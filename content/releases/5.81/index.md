---
menu:
  main:
    name: "5.81 (März 2021)"
    identifier: "5.81"
    parent: "releases"
    weight: -581
---

> Für dieses Release ist ein **Re-Index nötig**, bitte planen Sie entsprechende Zeit für das Einspielen des Updates ein. 

# Version 5.81.1

*Veröffentlicht am 24.03.2021*

# Webfrontend

### Repariert

- **Mappen**: Fehler beim Umgang mit Usern beim Teilen von Mappen per externem Link behoben
- **Plugins**: Fehler im `custom-mask-splitter-detail-linked` Plugin bei Mehrfachtabellen innerhalb von Mehrfachtabellen wurde behoben
- **Gruppeneditor**: fehlende Standardinformationen und Vorschaubilder wurden repariert

## Server

### Repariert

- **Hotfolder**: internes Datenbankhandling wurde verbessert, um Fehler mit offenen Datenbankverbindungen zu vermeiden

# Version 5.81.0

*Veröffentlicht am 17.03.2021*

## Webfrontend

### Neu

* **Export**: **cover** für Bilder wird jetzt unterstützt (Bild wird in einen festen Viewport gezoomt).
* **Suche**: Zusätzliche Möglichkeiten zur Suche in hierarchischen Objekten.
* **Editor**: Datumsbereiche werden automatisch geschlossen wenn nur ein Wert eingegeben ist.

### Verbesssert

* **CSV-Importer**: Tags sind jetzt immer sichtbar.
* **Tags**: Farben werden ausschliesslich im Frontend bestimmt, nicht mehr in einer Server-Konfiguration.

### Repariert

* **Usermanager**: Bei neuen Nutzer wird kein "undefined" mehr angezeigt.
* Suche: Sichtbarkeit von Tags wurde korrigiert.
* Grafische Korrekturen im CSS.
* **Editor**: Wechsel von Masken bei Tagveränderungen korrigiert.
* **Suche**: In Suchvorschlägen wurden fälschlicherweise auch hierarchische Objekte der Hauptobjekttypen durchsucht.
* **Reverse Nested**: Bei Verändung der Reihenfolge werden jetzt auch ungeänderte Objekte korrekt umsortiert.
* **Video**: In einigen Browser konnten nicht alle Buttons erreicht werden (CSS-Fix).

## Server

### Neu

* Neue Datenbank-Sprache Türkisch.

* Logging zusätzlicher Nutzerdaten kann für die Ereignisse in der Basis-Konfiguration eingestellt werden.

* Bilder können mit dem Modus **cover** beschnitten werden.

* Metadaten-Mapping für Bildformat (portrait / landscape).

### Verbessert

* Server kann ohne root-Rechte laufen (Systemadministrations-Eingriff erforderlich).
* Generierung von Dateinamen wurde verbessert.
* Mehr Felder im Typo3-Mapping verfügbar.
* **/api/pool**: Die Ausgabe von allen Pools ist nur für Nutzer mit dem `system.root`-Recht erlaubt. Das kann mit der Server-Konfiguration `server.api.pool.allow_non_root_list: true` auf das alte Verhalten zurückgestellt werden.

### Repariert

* Drehen und Spiegeln von Bildern wurde stabilisiert.
* Suche nach Nichtexistenz verschachtelter Daten funktioniert jetzt auch bei "nested index".
* E-Mails des Nutzer werden nicht mehr über die API im Kurzformat ausgegeben.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:7db0f038b92acb57d6628463035cbdec90d0fc7d89b207d5c8847db047d026d4
docker.easydb.de/pf/eas                  sha256:2dd23df39081a280d76255cae50f151a698e79b7bc1fce8a0898601e67851f19
docker.easydb.de/pf/elasticsearch        sha256:907b198deb124f06e6c825f94ee83e118494fdf5cfbe3ceb3b72f0e86d76c359
docker.easydb.de/pf/fylr                 sha256:72ce9843fe74f446712119231ec0f720cb8beebec9178c7aa453cda783f1a73b
docker.easydb.de/pf/postgresql-11        sha256:336ef532e4d215b264118a6d3a055035c8793e8f1f7daffe237688a6db723df8
docker.easydb.de/pf/server-base          sha256:d88804ef359114cce900534ea54cba6ea9afb4c0703cd674209d9eae3cc30ad4
docker.easydb.de/pf/webfrontend          sha256:d4b9c336054f794ab894d827e7256698a0157c4f3038c700d38a6758cdac2bed
```