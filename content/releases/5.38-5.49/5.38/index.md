---
menu:
  main:
    name: "5.38"
    identifier: "5.38"
    parent: "releases549"
    weight: -538
---

# Version 5.38.2

*Veröffentlicht am 09.08.2018*

### Webfrontend

*Behoben*

- Custom Data Type Link: Fehler bei leeren Namen wurde behoben.
- Pool-Auswahl: Scrollbalken bei langen Listen war nicht sichtbar.

### Server

*Verbessert*

- Aktualisiertes **wkhtmltox** für bessere WebDVD Vorschauerzeugung.

# Version 5.38.1

*Veröffentlicht am 03.08.2018*

### Webfrontend

*Behoben*

- PowerPoint-Export: Es wurden keine Bilder in die erzeugten **pptx**-Dateien geschrieben.
- Custom Data Type Link: Verwendung mit Templates in Nested wurde behoben.
- CSV-Importer: Importfehler bei Reverse Hierarchy Nested mit Linked Objects wurde behoben.
- Benutzer-CSV-Importer: Fehler beim Hochladen einer **csv**-Datei behoben.

# Version 5.38.0

*Veröffentlicht am 01.08.2018*

### Webfrontend

*Neu*

* Basiskonfiguration: Download ohne Dateiverweise möglich.
* Selbstregistrierungsdialog: Es können Mitteilungen hinterlegt werden, die bestätigt werden müssen.
* Datenmodell: Im Maskeneditor können Felder per Button bewegt werden.
* Custom Data Type Link: Unterstützung von URL-Templates.

*Verbessert*

* CSV-Importer: Löschen von Mehrfachfeldern wird unterstützt.
* CSV-Importer: Wiederholgruppen (auch verschachtelt) werden besser unterstützt.
* CSV-Importer: Fehlermeldung bei doppeltem Mapping wurde verbessert, diese enthält nun einen Hinweis auf das doppelte Feld hin.
* Plugin-Manager: JavaScript wird jetzt mittels **\<script\>** importiert, nicht mehr mit **eval**.
* Präsentation: Performanceverbesserung durch Caching der letzten 10 Objekte.
* Auswahlmenüs: CUI.ItemList erlaubt jetzt *multiline* für lange Einträge. Das verbessert die Lesbarkeit mit langen Einträgen.
* CSV/JSON-Importer sind jetzt im Hauptdialog für neue Objekte verfügbar und in den Listen jetzt neben dem *Plus*-Button zu finden. Durch diese Änderungen sind sie für Nutzer ohne *create*-Recht nicht mehr erreichbar.
* Sortieren von Custom-Data-Types in Wiederholgruppen wird unterstützt.
* Suche: Im Expertenmenü werden jetzt Masken und Feldlisten auch dann angeboten, wenn nur ein Objekttyp zur Verfügung steht.
* Bildgrößen in Listenansichten verbessert.



*Behoben*

* Wiederholgruppen mit einem unausgefüllten Datum als erstes Feld führen beim Laden im Editor nicht mehr zu einem Fehler.
* Drag & Drop: Einige Timingprobleme führten zu falscher Anzahl markierter Objekte.
* Exportmanager: Nach Löschen wurde die Aktualisierung der Liste korrigiert.
* Neue Objekte: Speichern während des Abbrechenvorgangs wurde korrigiert.
* Detail: Bei der Anzeige von nicht erlaubten Objekten konnte es zu einem ständigen Wartesymbol kommen.
* Editor: Aktivierung des *Speichern*-Button nach Änderung in Datumsbereichsfelder wurde korrigiert.
* Datenmodell: Einige Aktualisierungs- und Speicherprobleme wurden behoben.
* Schnellanzeige: Bei sehr großen Objekten kam es zu Darstelungsproblemen in CUI.Layer.
* Datumsauswahl: Wochentage sind wieder sichtbar

### Server

*Neu*

* Unterstützung für Archivdateitypen: **tar**, **tgz**, **bz2**, **gz**.
* Unterstützung für Vector 2D: **dwg**, **dxf**.
* POST /api/config unterstützt verschachtelte **type: table** für Custom Data Types.

*Verbessert*

* Schnellere Suchanfragen bei vielen Pools.
* Rechte Voreinstellungen müssen nur noch per-Context eindeutig sein.
* Schnelleres Speichern von Pools mit vielen Rechten.
* Unterstützung für ZIP Dateien die mit DEFLATE64 komprimiert wurden.

*Behoben*

* CSV-Exporter: Bessere Unterstützung von verschachtelten Objekten, so dass der CSV-Importer diese 1:1 importieren kann.
* Metadata-Export: In einigen Fällen wurden Metadaten nicht korrekt in exportiere Dateien geschrieben.
