---
menu:
  main:
    name: "5.93 (December 2021)"
    identifier: "5.93"
    parent: "releases"
    weight: -593
---

> > Diese Version **benötigt keinen neuen Index-Aufbau**

# Version 5.93.0

*Veröffentlicht am 01.12.2021*

## Webfrontend

### Neu

* **Suche**:
  * `without` Suche für Felder in Mehrfachfeldern
  * Sortierung nach *date, datetime, daterange* für Felder in Mehrfachfeldern
* Neuer Deeplink für `#detail/<id>`
* Neue Größe für den Standard in der Ergebnisansicht: `huge`
* Dialog zum Hochladen von Objekten: neue `RPUT` Option
* **Rechtemanagement**:
  * optionalen Hinweis für `list`-Parameter hinzugefügt

### Verbessert

* **Suche**:
  * Ausblenden des Finders, wenn der Sammlungsmanager keinen Inhalt hat
* Schaltfläche *'Teilen'* nicht anzeigen, wenn Deeplink in den Info-Versionen des Assets deaktiviert ist

### Behoben

* **CSV Importer**:
  * Fix für column id & system object id für verlinkte Objekte
* Nur Objekttypen mit Datei-Feldern in der Hotfolder-Konfiguration von Mappen anzeigen
* Bugfixes für den Filter bei verlinkten Objekten
* Fix in der Bestätigungsmeldung von Transitionen (Workflows)

## Server

### Neu

* **Suche**:
  * Sortierung nach *date, datetime, daterange* für Felder in Mehrfachfeldern

### Verbessert

* **Performance**:
  * **XML Export**: Verbesserte Leistung beim Zusammenführen von verknüpften Objekten
  * Verbesserte Leistung von `api/v1/objecttype`

### Behoben

* **Suche**:
  * Sortierung nach vollständigen Pfaden von hierarchischen verlinkten Objekten
  * Verbesserte Handhabung von Standards in den Suchergebnissen: Verwendung von Fallbacks für Sprachen, die nicht in den Suchergebnissen enthalten sind
* **Gruppeneditor**:
  * Aktualisierung der gespiegelten Pool-ID von revers verlinkten Objekten
* **Deeplink**:
  * Asset-Auswahl aus dem Standard vereinfacht und verbessert (`api/v1/objects/.../file/standard/...`)
* **Datenmodell Editor**:
  * Mögliches Problem in der Datenbank behoben, wenn ein Datentyp eines Feldes innerhalb eines Mehrfachfelds geändert wird

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:94e5539d1e2ca44c798f6f84227ec06d513029e2e4e2912020827fd9e37848f6
docker.easydb.de/pf/eas                  sha256:2e3ed5ac9e6d2813260679eec3dda2b4a1ce1b48bec489a9cf06f4d45d620353
docker.easydb.de/pf/elasticsearch        sha256:044ff57d7d46f67ce89d6f952f146a2ecb3d4b193b93369c1d3f63f50d6c0a0f
docker.easydb.de/pf/fylr                 sha256:8d14e6ae1d0dd3d49756221bac0f7f3ea6bd7f810a62ffaa81a5d75faa5ef0c9
docker.easydb.de/pf/postgresql-11        sha256:6452d22df1f49980a84dd246a6683bcc5e42bba0351f80fea2f8571223349dd4
docker.easydb.de/pf/server-base          sha256:fe6ba2bb59bf2f050a1ac549f05406ecaa667d9c1fb350924b17b6877d308c11
docker.easydb.de/pf/webfrontend          sha256:d3c8dd2552a2dd95a685501eafd93f2f5f63e2595f6caabb7d2d39cffa276a8b
```
