---
menu:
  main:
    name: "5.40"
    identifier: "5.40"
    parent: "releases"
    weight: -540
---

# Version 5.40.0

*Veröffentlicht am 19.09.2018*

### Webfrontend

*Neu*

- Metadaten-Mapping: Neue Eingabemaske mit Suchfilter und Ausgabe der Mapping-Tags
- JSON-Importer: Unterstützung von Updates durch **_id:lookup** notation
- JSON-Importer: Einstellung zum automatischen ignorieren von Upload-Fehlern während des Imports
- JSON-Importer: Ausgabe des Logs als CSV-Datei mit strukturierten Informationen

*Verbessert*

- Konfiguration: Neues Design für die Anzeige
- Editor: Beim Kopieren von Objekten werden "UNIQUE"-Einträge nicht mehr kopiert
- Verlinkte Objekte werden im Detail und Editor nicht mehr angezeigt
- Nur noch das erste ausgewählte Objekt einer Auswahl wird automatisch in der Detailansicht angezeigt
- Ausgabe von "Original Filepath" in Detail-Info für hochgeladene Dateien
- Ausgabe der tatsächlichen Dateitypen im Download-Dialog

*Behoben*

- User-CSV-Importer: **_groups#find** Funktionalität wurde repariert
- Ereignis-Manager: Anzeige hierarchischer Informationen von Ergeignissen wurde repariert
- Expertensuche: In seltenen Fällen wurden Eingabe nach Übernahme nicht aus dem Formular entfernt
- Filter: Die Anzeige von **Mehr..** in tieferen Hierarchiestufen wurde repariert





