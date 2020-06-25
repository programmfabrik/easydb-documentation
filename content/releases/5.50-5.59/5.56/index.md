---
menu:
  main:
    name: "5.56"
    identifier: "5.56"
    parent: "releases559"
    weight: -556
---

> Es gibt eine kleine API-Änderung in diesem Release bei GET **/api/collection/list**. Siehe unten.

# Version 5.56.1

*Veröffentlicht am 06.09.2019*

### Server

*Verbessert*

* **OAI/PMH**: Version 5.56.0. wurde mit einer Seitegröße von 5 ausgeliefert (**verb=ListRecords**). Wir haben aus der Seitengröße eine Basis-Konfiguration gemacht, voreingestellt sind 100.

# Version 5.56.0

*Veröffentlicht am 04.09.2019*

### Webfrontend

*Neu*

* **Expertensuche**: Angezeigte Masken und Felder werden jetzt nach der aktuellen **Objekttypen/Pool-Auswahl** gefiltert, und nicht mehr nach allen verfügbaren Objekttypen und Pools. 
* **Datenmodell**: Eine neue Option erlaubt die Frontend-Eingabeüberprüfung auf *Nicht leer* jetzt auch für **Custom-Data-Type**-Felder. 
* **Mehrzeilige Textfelder** werden bei der Eingabe nicht mehr automatisch in der Höhe angepasst. Der Code des verwendeten Frameworks hat nicht korrekt mit chinesischen Tastaturen unter Windows 10 zusammengearbeitet, so dass wir uns entschieden haben vorerst auf dieses Feature zu verzichten. Textfelder sind jetzt 100px hoch und können mit einem Draghandle manuell in der Höhe verstellt werden.

Verbessert

* **Listen**: In der Tabellenansicht ist jetzt auch der `+`Button verfügbar (CSV-Importer, Neues Objekt anlegen).
* **CSV-Importer**: Bei der Dateiauswahl wird nach **.csv** und **.txt** gefiltert.
* Verbesserte Fehlerbehandlung im **WebDVD**-Player.
* Verbesserte Darstellung von **Markdown-Feldern** in der Detailansicht.
* **Druckausgabe**: Die Seiten haben jetzt 1cm Rand, so dass kein Text mehr abgeschnitten wird, wenn die Seiten gedruckt werden.
* Kleinere grafische Verbesserungen.

*Behoben*

* **Connector**: Das Laden von Dateien von Connector easydb wurde auch dann erlaubt, wenn der Nutzer für die Connector easydb nicht über das **System-Recht zum Download** verfügte.  
* Beim **Hinzufügen von Dateien in Mehrfachfeldern** (auch Reverse), wird jetzt überprüft ob bereits Daten im aktuell angezeigten Mehrfacheintrag vorhanden sind oder nicht. Abhängig davon, werden neue Einträge erzeugt (Dateiauswahl erlaubt die Auswahl von mehreren Dateien) oder ob die Datei in den aktuellen Eintrag geladen wird (Dateiauswahl erlaubt nur die Auswahl von genau einer Datei).
* **Tabellenüberschriften** bekommen jetzt keinen Browser-Fokus mehr.
* Ein Anzeigeproblem bei der **Textanzeige für Datumsbereichsfelder** wurde behoben.
* In **Nutzer- und Gruppenauswahl** werden jetzt keine Collection-Nutzer mehr angezeigt (Nutzer die zum Teilen mit Link angelegt werden).
* **Gruppeneditor**: In Fällen bei denen Mehrfachfelder in einem Panel versteckt waren, hat die Vorlagenfunktion nicht korrekt funktioniert.
* **Gruppeneditor**: Der Pool in der Vorlage wird nicht mehr vorausgefüllt.
* **CSV-Importer**: Der Import von Mehrfachfeldern bei denen die Zelle mit einer Leerzeile beginnt, wurde repariert. Die Leerzeile wurde fälschlicherweise ignoriert, was in Folge zu Fehlzuordnungen mit anderen Spalten für dasselbe Mehrfachfeld führen konnte.
* **Versionen**: Beim Hochladen eigener Versionen für eine Datei wurde die neu hochgeladene Datei fälschlicherweise automatisch als bevorzugte Datei gespeichert.

### Server

*Neu*

* **GET /api/pool** und **GET /api/collection** geben nun den **_path** in den Objekten aus. 
* **GET** **/api/collection/list** gibt jetzt alle Collections zurück, das alte Verhalten, nur die Top-Level-Collection auszugeben kann mit **GET /api/collection/list/null** erreicht werden.

*Verbessert*

* **Custom-Data-Type-Updater** kann per Konfiguration deaktiviert werden.
* **Custom-Data-Type-Updater** kann nun auch in **Mehrfachfeldern** arbeiten. Die **Version** der betroffenen Objekte werden bei Aktualisierungen **nicht mehr erhöht**. 
* Nutzer die zum **Teilen per Link** automatisch angelegt werden werden nun auch automatisch gelöscht, wenn die Collection gelöscht wird.

*Behoben*

* Beim **Umbennen eines Pools** werden alle Objekte die in dem Pool und darunter liegen neu indiziert. Damit erscheinen Sie nun korrekt im Filter und in der Objekttypen/Pool-Auswahl.
* Einige **Indizierungen für sprachabhängige Daten** wurden verbessert. Bei Problemen bitte manuell einen Reindex durchführen.
* Beim **Löschen von Mappings** werden Verlinkungen in Pools und Objekttypen ebenfalls gelöscht.
* **Rechtemanagement in Mehrfachfelder** für Dateien repariert.
* Die **Reihenfolge der Rechte** bei Objekttypen wird jetzt korrekt gespeichert. Das hat keine Relevanz für die Vergabe der Rechte, da die Reihenfolge an der Stelle keine Beachtung findet.