---
menu:
  main:
    name: "5.83 (Mai 2021)"
    identifier: "5.83"
    parent: "releases589"
    weight: -583
---

> Für dieses Release ist **kein Re-Index** nötig.

# Version 5.83.2

*Veröffentlicht am 18.05.2021*

## Webfrontend

* Ausblenden des Pools über Maskenoption korrigiert
* Unterstützung für ältere Browser verbessert
* Probleme bei CSV-Import hierarchischer Objekte behoben

## Plugins

* Optimierung im custom-mask-splitter-detail-linked-Plugin, um Problemen bei Elasticsearch vorzubeugen

# Version 5.83.1

*Veröffentlicht am 10.05.2021*

## Webfrontend

* Gruppeneditor erlaubt Batch-Größe 1 zur Umgehung von Fehlern bei gegenseitigen Verknüofungen
* falscher Objekttyp in Tabellenansicht behoben
* falsche Typen beim Export behoben
* Fehler bei Asset-Feldern in Expertensuche behoben

## Plugins

* Blockade des Auto-Keyworders beim Datenbank-Updates behoben
* Fehler bei unbestätigten Tasks im Connector behoben

# Version 5.83.0

*Veröffentlicht am 05.05.2021*

## Webfrontend

*Neu*

* **Export**: Unterstützung von Vorlagen für den Export.
* **Editor**: Option für hierarchische Listen zum Verlinken von nur Objekten ohne Kinder (nur Blätter).

*Verbessert*

* **Barrierefreiheit**: Platzhalter und Annotationen für einige Feldern ergänzt.
* **Datumsbereich**: Anzeige der textuellen Represenation verbessert.

*Behoben*

* **Custom-Data-Type-Location**: Automatische Korrktur von alten Daten im Rahmen der regelmäßiges Aktualisierungen.
* **Upload**: Bei bestimmten Kombinationen von verlinkten Objekten und Metadaten-Profilen konnte es zu einem Javascript-Fehler kommen.
* **CSV-Importer**: Support von Zeilenumbrüchen in Mehrfachfeldern.
* **CSV-Importer**: Re-Import von Spalten mit *easydb|* Prefix wurde korrigiert.
* **User-CSV-Importer**: Einfügen von Nutzern wurde repariert.
* **Editor**: Boolsche Werte aus Vorlagen wurde nicht korrekt befüllt.
* **Editor**: Fehler bei aktiviertem Pool-Management in Reverse verlinkten Objekten behoben.
* **Suche**: Auswahl von hierarchischen Objekten in der Tabellenansicht hat in einigen Fällen nicht korrekt funktioniert.
* **Export / Download**: Unterstützung von sehr komplexen Datenmodellen bei denen zuvor ein Limit der Anzahl der Felder in der Elasticsearch erreicht wurde.
* **Export / Download**: Maskeneinstellungen ohne aktivierte *Filter*-Spalte führten dazu, dass Dateien von verlinkten Objekten nicht exportiert wurden.

## Server

*Verbessert*

* Verbesserungen im **XML-Export** bei der Einbindung verlinkter Objekte
* Verbesserter Fehler beim Versuch, einen bereits archivierten Nutzer erneut zu archivieren
* Verbesserter Fehler beim Versuch, bidirektional verknüpfte Objekte mit dem Gruppeneditor zu bearbeiten
* Archivierte LDAP- und SSO-Nutzer werden beim erneuten Anmelden wieder aktiviert
* IP-Adressen werden aus den Ereignissen entfernt und werden in Zukunft dort nicht mehr gespeichert (betraf nur einen kleinen Teil der Ereignis-Typen)
* Serverseitige Sortierung nach "Standard" von verlinkten Objekten implementiert

*Behoben*

* Angabe der Version in EXPORT_OBJECT-Ereignissen korrgiiert
* Fehler bei Angabe ungültiger Felder in exclude_fields der Suche korrigiert

## Plugins

### Hotfolder

- Encoding-Probleme behoben
- Problem bei der Vereinnahmung ohne Metadaten-Profil behoben
- Anhängen von Assets in verschachtelten Feldern korrigiert

### Auto-Keyworder

- Update im Auto-Keyworder korrigiert

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:61f854f622586be9bcd7cb68d31d56b7578421ac5352a7cbaa00b39011f376b2
docker.easydb.de/pf/eas                  sha256:61702fe554b6b1dc57adfa35ef148e8b821058fd5fd0566fe355f805b38350ad
docker.easydb.de/pf/elasticsearch        sha256:e62e8c0a3b299c15f2d8c3f134e5d5f6123bf109d931bdf58c647e48663d36df
docker.easydb.de/pf/fylr                 sha256:a851233526c2fe3d063672e2ebb598fdd166e2d0eaf55b002312ae6af85271c1
docker.easydb.de/pf/postgresql-11        sha256:ef5daf3bad0933736b4f41a5f98e9b9c0e47738a8e01708683972b00fe8da7ce
docker.easydb.de/pf/server-base          sha256:623e36d2ea15e0e5b3ce28a3e168f5ebb373fef72b46b523114cfbeb00f34c73
docker.easydb.de/pf/webfrontend          sha256:adbaba7229e7132596d0ad84f20dff0dc02136c89b2ea7c2e153d5c65ec89d68
```

