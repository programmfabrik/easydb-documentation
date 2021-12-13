---
menu:
  main:
    name: "5.93 (Anfang Dezember 2021)"
    identifier: "5.93"
    parent: "releases"
    weight: -593
---

> Diese Version **benötigt keinen neuen Index-Aufbau**

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
docker.easydb.de/pf/elasticsearch        sha256:4525a6ad2174fdceeef9fdf2672d60f66af678d7cfddcece6d1dd8a256512846
docker.easydb.de/pf/fylr                 sha256:8d14e6ae1d0dd3d49756221bac0f7f3ea6bd7f810a62ffaa81a5d75faa5ef0c9
docker.easydb.de/pf/postgresql-11        sha256:6452d22df1f49980a84dd246a6683bcc5e42bba0351f80fea2f8571223349dd4
docker.easydb.de/pf/server-base          sha256:4c57dc78ffef39b06cac1200e521cfcda1a28145dbd1ff11cedab503dba8e31e
docker.easydb.de/pf/webfrontend          sha256:00c5ef438fb109f6a7169f944e5ffbee517a22750f5fbf097f7f88ee868c4c71
```
