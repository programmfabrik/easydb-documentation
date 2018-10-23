---
menu:
  main:
    name: "5.41"
    identifier: "5.41"
    parent: "releases"
    weight: -541
---

# Version 5.41.3

*Veröffentlicht am 18.10.2018*

Diese Version beinhaltet nur kundenspezifische Korrekturen.

# Version 5.41.2

*Veröffentlicht am 12.10.2018*

### Server
* Fehler in kundenspezifischen Modulen behoben (nicht in "base"-Solution integriert)

### Webfrontend

* Versionsnummer erhöht (fehlte im ersten Patch-Release)

# Version 5.41.1

*Veröffentlicht am 11.10.2018*

### Server

* Indizierung für bestimmte Objekttypen behoben

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

*Verbesserungen*

* Klick auf den Hintergrund schließt Modal-Dialoge (außer Vollbild)
* Detail/Export von einzelnen Objekten benutzt die ausgewählte Maske
* Connector: Unterstützung für Downloads und Freigaben verbessert
* Connector: Login- und Logout-Ereignisse werden entfernt geloggt
* Editor: Option "Tags anzeigen" wird für verlinkte Objekte beachtet
* Spalten-Filter werden auch für Nutzer mit dem `system.root`-Systemrecht beachtet
* Metadaten-Mapping intuitiver gestaltet
* JSON-Logs verbessert
* Benutzbarkeit beim Auswählen und Entfernen vieler Objekte verbessert
* bei Objekttypen und Masken wird neben dem Anzeigenamen nun auch der Datenbankname angezeigt

*behobene Fehler*

* Esc-Taste schließt Layer
* verschiedene Bug-Fixes im Metadaten-Mapping

### Fylr

* Zip-Fehlerbehandlung verbessert
