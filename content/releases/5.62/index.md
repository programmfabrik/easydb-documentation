---
menu:
  main:
    name: "5.62"
    identifier: "5.62"
    parent: "releases"
    weight: -562
---

# Version 5.62.1

*Veröffentlicht am 28.01.2020*

### Webserver

*Behoben*

* Login und Workflow-Popover wachsen wieder wenn sich deren Inhalt ändert.

### Server

*Behoben*

* Speichern von Pools in Datenbanken mit Objekttypen mit Namen von SQL-Commands wurde repariert.

# Version 5.62.0

*Veröffentlicht am 22.01.2020*

### Webfrontend

*Neu*

* Die **Single-Sign-On** Anmeldung hat neue Einstellungen für die Buttons in der Basiskonfiguration bekommen.
* Unterstützung von Nummern mit tausender-Trennzeichen im **CSV-Importer**.

*Verbessert*

* **Objekttypen/Pool-Auswahl** heisst jetzt **Ressourcen**.
* Ausführliche textuelle Anzeige der aktuellen **Ressourcen**.
* Anzeige der Objekte in einem Pool zeigt im zugeklappten Zustand die Anzahl inkl. aller Unterpools, im aufgeklappten Zustand nur die Anzahl im Pool selber an.
* **Popover**-Anzeige des Editor wurde verbessert.

*Behoben*

* Das Laden ungültiger **Vorlagen** führt nicht mehr zu einem Javascript-Error sondern wird in einer Fehlermeldung transparent gemacht.
* Der Import von Hierarchien im **CSV-Importer** wurde für einige Fälle repariert.
* Das Anlegen von Mehrfachfeldern und die Anzeige vom Pool-Namen und von **verlinkten Objekten** die beim Hochladen im **Neue-Objekte-Dialog** erzeugt werden, wurde repariert.
* Die **Editor-Vorschau** im Datenmodell wurde für einige Fälle repariert.

### Server

*Verbessert*

* Verbesserte **Indexer-Performance**.
* **Verschlankung** des **Index** für normale Reverse-Nested Objekte (**Re-Index** nötig, wird nicht automatisch gemacht).

*Behoben*

* Setzen der **Sprache** für einige **anonyme Nutzer** wurde repariert, in Folge funktionieren die Vorschläge in der Suche für betroffene Nutzer.
* **Voreinstellungen** mit Rechtemanagement für obsoleten Asset-Versionen werden beim Server-Start korrigiert und betroffene Versionen über die API nicht mehr ausgeliefert.
* **/api/event** funktioniert jetzt korrekt, wenn Nutzer in den Events gelöscht sind.
* Fix für **Hotfolder** und Umlautprobleme auf Installation mit nicht korrekt gesetzer Sprache in der Umgebung.