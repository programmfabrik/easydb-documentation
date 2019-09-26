---
menu:
  main:
    name: "5.40"
    identifier: "5.40"
    parent: "releases550"
    weight: -540
---

# Version 5.40.2

*Veröffentlicht am 27.09.2018*

### Server

*Behoben*

- Der Dateiname in der **download_url** wurde nicht richtig gesetzt, was zu vereinzelten Problemen bei ZIP-Dateierstellung über den Connector oder kundenspezifischen Anwendungen führen konnte

### Fylr

*Behoben*

- Mozilla Firefox Unterstützung für ZIP Downloads mit ZIP-Dateinamen die ein Leerzeichen enthalten

# Version 5.40.1

*Veröffentlicht am 26.09.2018*

### Asset-Server

*Behoben*

- Unterstützung von UTF8 in Javascript-Dateien
- MP4 mit YUV402p Pixel Format, zur besseren Unterstützung in Mozilla Firefox



# Version 5.40.0

*Veröffentlicht am 19.09.2018*

> Das Update erfordert keinen neuen Index, so dass mit keinen langen Wartezeiten nach dem Update zu rechnen ist.

### Server

*Neu*

- Original Filepath wurde ins Mapping aufgenommen

*Behoben*

- Suche nach *ohne* wurde für einige Felder behoben
- Original Filebase wird jetzt ohne Pfad gespeichert.

### Webfrontend

*Neu*

- Metadaten-Mapping: Neue Eingabemaske mit Suchfilter und Ausgabe der Mapping-Tags
- JSON-Importer: Unterstützung von Updates durch **_id:lookup** und **_version:autoincrement** notation
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





