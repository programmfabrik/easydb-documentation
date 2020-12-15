---
menu:
  main:
    name: "5.77 (Dezember 2020)"
    identifier: "5.77"
    parent: "releases"
    weight: -577
---

> Dieses Release bringt eine Erweiterung des Nutzermanagements mit sich. Es lassen sich Nutzer nun wahlweise Löschen oder Archivieren. In einem späteren Release kann der Nutzer für der Archivierung pseudonomisiert werden.

# Version 5.77.1

*Veröffentlicht am 15.12.2020*

## Webfrontend

*Verbessert*

* Suche: **Beschleunigte Anzeige** von aufwendigen Textansichten.
* **Suche / Detail**: Verlinkte Objekte ohne Datei werden jetzt **ohne Datei-Platzhalter** angezeigt.
* Suche: **Überschriften im Filter** sind jetzt alle einheitlich.
* Kleinere Verbesserungen am Design (Neue Objekte, Pool-Informations-Button)

*Behoben*

* **CSV-Importer**: Das Importieren von Dateien mit Metadaten in ein Mehrfachfeld wurde repariert.

# Version 5.77.0

*Veröffentlicht am 09.12.2020*

## Webfrontend

*Neu*

* **Plugin (Beta)**: Das neue **custom-mask-splitter-detail-linked** kann im Detail automatische Suchen nach Objekten durchführen und diese Anzeigen die auf das angezeigt Objekt verweisen.
* **Plugin (Beta)**: Das neue **custom-data-type-html-editor** stellt einen Datentyp mit einem Rich-Text-Editor ([Tiny](https://www.tiny.cloud/)) bereit.
* **Datenmodell**: Neue Option "Nicht leer" für Felder mit Bereichen.
* **Suche**: Boolsche Felder im Filter.
* **Download**: Automatisches Herunterladen von mehreren Dateien per Browser und ohne ZIP.

*Verbessert*

* **CSV-Importer**: Verbesserte Markierung von Pflichtfeldern.

*Behoben*

* **PPTX-Exporter**: Ein Fehler im Zusammenhang mit dem Ein- / Ausblenden der Standard-Info wurde behoben.

* **Datenmodell**: Fehler bei der Anzeige der Editor-Vorschau behoben.
* **Drucken**: Die Sortierung beim Ausdruck folgt jetzt der Sortierung des Suchergebnisses.
* **Suche**: Fehler bei der Anzeige des **Mehr**-Buttons wurde behoben.
* **Editor**: Die Vorlage heisst jetzt wieder **#Vorlage**.

## Server

*Neu*

* **Usermanagement**: Archivierung oder Löschen von Nutzern.
* **Download**: Pool-Name kann in dem Dateinamen konfiguriert werden.
* Datenmodel: Der Range-Check wurde erweitert und kann jetzt ein Client-seitiges ausgefüllt sein erzwingen.
* **/api/search**: Aggregation für Boolean-Felder.
* **SSO**: Erweiterungen in der Mappingkonfiguration.

*Behoben*

* **/api/suggest**: Aufbereitung der Datei-URL mit vollständigem Domain-Namen.
* **/api/suggest**: Ein mehrfachem Datenmodell-Update konnte zu dublizierten Rückgaben von verlinkten Objekten führen.
* Verbesserte Fehlerbehandlung im **PPTX-Exporter**.
* **Hotfolder**: Fehler im Zusammenhang mit verlinkten Objekten behoben.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:3b0d0e3b97be2fc7129f29f56434608f6fcb3a213b2f7cfe042eccd6adbe6d0b
docker.easydb.de/pf/eas                  sha256:9b6e0c97187f681416f07e75e13a5641785f1649d569d5c4e81364fde56535d4
docker.easydb.de/pf/elasticsearch        sha256:2c61c8d9096a741cadaa496861ae13bdc4ce808995710a2849c29e25160350c3
docker.easydb.de/pf/fylr                 sha256:07246271f67c95532b44fa962eabe08eb4d0cf33fa58c96d046dc18d51b8dfc2
docker.easydb.de/pf/postgresql-11        sha256:98756185f6e1995f6cf64f46d1190968f771311967187dd5bf5c433157517290
docker.easydb.de/pf/server-base          sha256:362f6af8ad3f2e361434b242ce1abc444d7fb80d4eae7c5699ca210e0ffd7c90
docker.easydb.de/pf/webfrontend          sha256:c738040a461dc4b910f8b80e90727a3116d6aea2cc7ad0afcbbe3dd8b74823fd
```

