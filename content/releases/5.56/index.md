---
menu:
  main:
    name: "5.56"
    identifier: "5.56"
    parent: "releases"
    weight: -556
---

# Version 5.56.0

*Veröffentlicht am 04.09.2019*

### Webfrontend

*Neu*

* **Expertensuche**: Angezeigte Masken und Felder werden jetzt nach der aktuellen **Objekttypen/Pool-Auswahl** gefiltert, und nicht mehr nach allen verfügbaren Objekttypen und Pools. 
* **Datenmodell**: Eine neue Option erlaubt die Frontend-Eingabeüberprüfung auf *Nicht leer* jetzt auch für **Custom-Data-Type**-Felder. 
* **Mehrzeilige Textfelder** werden bei der Eingabe nicht mehr automatisch in der Höhe angepasst. Der Code des verwendeten Frameworks hat nicht korrekt mit Chinesischen Tastaturen unter Windows 10 zusammengearbeitet, so dass wir uns entschieden haben vorerst auf dieses Feature zu verzichten. Textfelder sind jetzt 100px hoch und können mit einem Draghandle manuell in der Höhe verstellt werden.

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

*Kommt noch*