---
menu:
  main:
    name: "5.38"
    identifier: "5.38"
    parent: "releases"
---

# Version 5.38.0

*Veröffentlicht am 01.08.2018*

### Webfrontend

*Neu*

* Basiskonfiguration: Download ohne Dateiverweise möglich
* Selbstregistrierungsdialog: Es können Mitteilungen hinterlegt werden, die bestätigt werden müssen.
* Datenmodell: Im Maskeneditor können Felder per Button bewegt werden.



*Verbessert*

* CSV-Importer: Löschen von Mehrfachfeldern wird unterstützt.
* CSV-Importer: Wiederholgruppen (auch verschachtelt) werden besser unterstützt.
* CSV-Importer: Fehlermeldung bei doppeltem Mapping wurde verbessert, diese enthält nun einen Hinweis auf das doppelte Feld hin.
* Plugin-Manager: Javascript wird jetzt mittels Script-Tag und nicht mehr mit *eval* geladen.
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