---
menu:
  main:
    name: "5.65"
    identifier: "5.65"
    parent: "releases569"
    weight: -565
---

> Für dieses Release ist ein Re-Index nötig, bitte planen Sie entsprechende Zeit für das Einspielen des Updates ein. 

# Version 5.65.1

*Veröffentlicht am 06.04.2020*

### Webfrontend

*Neu & Verbessert*

* **Mitteilungen**: Die Vorschau hat jetzt einen **Schließen**-Button. 

*Behoben*

* **CSV-Importer**: Detail-Vorschau wurde für verlinkte Objekte in einigen Fällen repariert.
* **CSV-Importer**: Fehlerbehebung für einen Fehler beim Hochladen.
* **CSV-Importer**: Der CSV-Importer für Benutzer wurde repariert.
* **Mappen**: Die Einstellungen für Mappen zum Hochladen mit Pools zeigt jetzt den korrekten Pool an.
* **Suche**: Die Anzeige von Systemfeldern in der Tabellenansicht wurde repariert.
* Download: Der **Download von Dateien** die über verlinkte Objekte in den Standard gezogen werden wurde für den Fall repariert, dass das Dateifeld nicht im Detail sichtbar war.

### Server

*Behoben*

* Die Anzeige der **Standard-Informationen** in verlinkten Objekten die über Reverse-Objekte angezeigt werden wurde repariert.
* Fehler im **Preindexer** konnte zu Absturz in einigen Fällen führen.
* Fehler im **Datenmodell-Editor** beim Anlegen von Tabellen mit Verschachtelungen korrigiert.

# Version 5.65.0

*Veröffentlicht am 25.03.2020*

### Webfrontend

*Neu & Verbessert*

* Datenmodell: **Mehrfachfelder** können nach **beliebigen Sortierkriterien** automatisch sortiert werden. Diese Sortierung erfolgt nur im Webfrontend und wird vor dem Speichern und vor der Anzeige automatisch durchgeführt.
* Exporte können für XML und CSV für verlinkte Objekte jetzt auch Objekttypen einbetten, die in der Hauptsuche erscheinen.
* **Mitteilungen**: Verbesserte Darstellung im Formular für Bestätigungen.

*Behoben*

* **CSV-Importer**: Korrekturen beim Setzen von hierarchischen Informationen.

### Plugins

* Das **Geonames-** und **GN250-Plugin** wurden auf [Mapbox](https://www.mapbox.com/) umgestellt. Für Mapbox muss zwingend ein API-Key in der Basis-Konfiguration eingetragen werden, sonst werden keine Karten angezeigt.

### Server

*Neu & Verbessert*

* **Export**: Im CSV-Format wurde der Export von sprachabhängigen Feldern verbessert.
* **Export**: `export.merge_linked_object=all`  erlaubt das einbetten von verlinkten Objekten im Export die in der Hauptsuche angezeigt werden. 
* **Export**: `mapping` wird nur noch unterstützt wenn `xml_one_file_per_object=true`gesetzt ist.

*Behoben*

* **Index**: Das Pool-Facetting wurde korrigiert für Objekte die mit Objekten aus anderen Pools verlinkt waren. Eine Neu-Indizierung ist hierfür erforderlich und wird automatisch zum Server-Start angestossen.
* Export: Die Ausgabe von **Assets im XML** war fehlerhaft und wurde korrigiert
* Export: Das **Speichern von ZIP-Dateien** über FTP wurde korrigiert.

# Prüfsummen

* Hier die Prüfsummen unserer Docker-Images (neueste Version)

  ```ini
  docker.easydb.de/pf/chrome               sha256:c1bdb8ed51116804abd49cc25d9bc13be5bbfe43d4f8c834c7d45c9ab0b673b2
  docker.easydb.de/pf/eas                  sha256:83d907500311166f28201c29d2663900f5c5fb61fbba66f6ddb64ba77e2eefff
  docker.easydb.de/pf/elasticsearch        sha256:3e7cd67fb1a4ee2e5cb2e78d79ee38661a98e99bb824413f2bbaa4238af6c60e
  docker.easydb.de/pf/fylr                 sha256:a90fc81cd5a2ce970f6a4fe13e674ded87b22cea3703201db6bdc0f42b95a81d
  docker.easydb.de/pf/postgresql-11        sha256:d7bca85db245478934ef3f8ccaaf3c13fcd6e7ff26728e344f70b0370c9d051b
  docker.easydb.de/pf/postgresql           sha256:c5de3a34289459f0d098bc64e36cb3308eaebbccab563ff5efb0667b8b539c0f
  docker.easydb.de/pf/server-base          sha256:36253e157703def337a6ea2e53671d414f7de071b449e3d28bb3dfcabbe85c13
  docker.easydb.de/pf/webfrontend          sha256:1d35dbf1292cbba778aa913e431e60d4326be90cf0a82d2133fe347a2896a0a5
  ```

