---
menu:
  main:
    name: "5.41"
    identifier: "5.41"
    parent: "releases"
    weight: -541
---

# Version 5.41.0

*Veröffentlicht am 10.10.2018*

> Dieses Release hat einen Re-Index zur Folge, entsprechende Update-Zeit sollte eingeplant werden.

### Server

* Alle E-Mails suchbar über API
* Optimierungen bei Erstellung des Suggest-Indexes
* Verschlankung der Suchergebnisse für Basis-Typen
* Ablaufzeit von Login-Sperren verfügbar gemacht
* `/api/buildsuggest`-Endpunkt für die Test-Integration
* Indizierung aller Kinder und Elternobjekte bei Änderungen
* XSLT-Probleme beim Export mit neu hochgeladenen XSL-Dateien behoben
* verbesserte Fehlerbehandlung

### EAS

* UTF-8 für alle ausgelieferten JS-Dateien angenommen
* Nullwerte in Metadaten werden beim Einlesen entfernt, um Datenbank-Fehlern vorzubeugen

### Webfrontend

