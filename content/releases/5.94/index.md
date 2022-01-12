---
menu:
  main:
    name: "5.94 (Januar 2022)"
    identifier: "5.94"
    parent: "releases"
    weight: -594
---

> Diese Version bringt **beschleunigte Ladezeit** der Applikation. In einigen Tests lädt **easydb** nun bis zu **5x schneller** als zuvor. Diese Beschleunigung konnte erreicht werden durch massive Parallelisierung beim initialem Laden der benötigten Resourcen. 

# Version 5.94.0

*Veröffentlicht am 12.01.2022*

## Webfrontend

### Neu

* **Vollbild**: Anzeige der Detailinformation ist in neuem Design und rechts neben der Vollbilddarstellung.
* **Editor**: Beim Kopieren kann nun ausgewählt werden ob Reverse Nested Objekte mitkopiert werden oder nicht.

### Verbessert

* **Optimierung** der Ladezeit der Applikation.
* **Filtertree**: Ausgabe von doppelten Bezeichnungen bei Mehrfachfeldern wurde unterdrückt.
* **Suche**: Anzeige hierarchischer Objekte mit langen Namen wurde verbessert 

### Behoben

* **Detail**: Info > Version hatte teilweise Probleme komplexere Versionshierarchien anzuzeigen.
* **PDF-Druck**: Es konnte passieren, dass einige Bilder im PDF nicht angezeigt wurden.
* **Accessibility-Attribute** für einige Inputs wurden korrigiert.

## Server

### Neu

* **Easdb-Asset-Server**: SVG-Support in `vector2d`.
* **Group Edit Mode**: Aktualisierung des Pool in Reverse Nested Objekten.
* **Transitions**: Email vom Pool-Ansprechpartner kann für **Transition-Emails** genutzt werden.

### Verbessert

* **Performance**-Verbesserungen bei **Session-Requests**. 
* **Performance**-Verbesserungen bei der Suche von Type `message`.
* Optimierungen beim Elastic-Mapping mit vielen konfigurierten Sprachen und Custom-Data-Types.

### Behoben

* Ein **Indizierungsproblem** beim Import hierarchischer Objekte wurde behoben.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version): 