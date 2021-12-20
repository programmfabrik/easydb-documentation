---
menu:
  main:
    name: "5.93 (Anfang Dezember 2021)"
    identifier: "5.93"
    parent: "releases"
    weight: -593
---

> Diese Version **benötigt keinen neuen Index-Aufbau**

# Version 5.93.4

*Veröffentlicht am 20.12.2021*

Über die Änderung in 5.93.2 hinausgehend wurden die von den jüngsten Sicherheitslücken betroffene Klasse `JndiLookup.class` aus dem Elasticsearch-Image entfernt.

# Version 5.93.3

*Veröffentlicht am 16.12.2021*

## Server

### Verbessert

* Auf ein Schreiben der Datenbank wird bei lesenden Zugriffen weitestgrehend verzichtet. Die Anfragen werden dadurch beschleunigt.
* Die Suche nach Nichtexistenz eines Datumsfeld wurde optimiert. Das führt u.a. zur Beschleunigung der Suche nach Messages.
* Verzicht auf unnötige Sprachen im Mapping von in anderen Objekten eingebetteten Pool-Links. Diese Änderung greift erst beim Neuerstellen des Mappings, worauf im Rahmen des Patch-Releases verzichtet wird.

# Version 5.93.2

*Veröffentlicht am 13.12.2021*

Dieses Patch-Release beinhaltet eine zusätzliche Absicherung für die als `CVE-2021-44228` bezeichnete Sicherheitslücke in `log4j` (https://logging.apache.org/log4j/2.x/security.html). Laut Elasticsearch-Team wäre die Lücke aber auch bisher nicht ausnutzbar (https://discuss.elastic.co/t/apache-log4j2-remote-code-execution-rce-vulnerability-cve-2021-44228-esa-2021-31/291476).

# Version 5.93.1

*Veröffentlicht am 03.12.2021*

## Webfrontend

### Behoben

* **Assets hochladen**:
  * Falsches Session Token bei EAS Requests behoben

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
docker.easydb.de/pf/elasticsearch        sha256:3e036c545e8e5c87a64d5e673bf9e1e455eb218006f3c53d518efc8867299111
docker.easydb.de/pf/fylr                 sha256:8d14e6ae1d0dd3d49756221bac0f7f3ea6bd7f810a62ffaa81a5d75faa5ef0c9
docker.easydb.de/pf/postgresql-11        sha256:6452d22df1f49980a84dd246a6683bcc5e42bba0351f80fea2f8571223349dd4
docker.easydb.de/pf/server-base          sha256:c686164eba710465b70954db1398cf997fa656a08e1264925d7d83ded4d4909e
docker.easydb.de/pf/webfrontend          sha256:82b2c93daae750e6bf4344497aa61b8bb1bbc82364bf433f804f6de2afc2cfc7
```
