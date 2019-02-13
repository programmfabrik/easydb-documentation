---
menu:
  main:
    name: "5.46"
    identifier: "5.46"
    parent: "releases"
    weight: -546
---

> Die Versionen ab **5.45.0** haben ein neues Indizierverfahrung für Assets eingeführt. Im Zuge dieser Einführung kam es teilweise zu einem **sehr erhöhten Speicherplatzbedarf** für die Postgres-Datenbank. Das lag an einer History-Tabelle die über die Maßen gefüllt wurde. 5.46.0. verzichtet auf diese Tabelle und sollte speichermäßig nur etwa 10% über der Version 5.44.0. liegen.

# Version 5.46.1

*Veröffentlicht am 12.02.2019*

### Webfrontend

*Neu*

* ScriptRunner: Auswahlmöglichkeit wie im Exporter, um nicht mit der Standard-Maske zu arbeiten.
* Sortierung nach Original Dateiname.

*Verbessert*

* Hirji-Gregorian Datumsumrechnung arbeitet auf Wunsch auch ohne Tag & Monat.

*Behoben*

* Vorschauen ohne Länge und Breite verursachen jetzt keinen Fehler mehr im Zoomer.
* Sortierung nach Dateieigenschaften wurde repariert.

### Server

* Erkennung von Duplikaten bei verlinkten Objekten ignoriert nicht gesetzte Spalten
* Workaround für Performance-Problem im Rechtemanagement
* Fix für teilweise fehlenden Parameter in der Basiskonfiguration

# Version 5.46.0

*Veröffentlicht am 07.02.2019*

### Webfrontend

*Neu*

* Beta: Neues Plugin **FieldMigrator**. Mit diesem Plugin für den **ScriptRunner** können Feldinhalte von einem in ein anderes Feld massenhaft kopiert werden.
* Die Spracheinstellungen für Benutzer bieten jetzt die Option nicht angeschaltete aber im Objekt vorhandene Sprachen in der Detailanzeige auszublenden.
* JSON-Importer: Neue Checkbox um bereits existierende beim Import Objekte ohne Fehler zu überspringen.
* CSV-Importer: Einstellungen können gespeichert und geladen werden.
* Detailanzeige (Vollbild): Unterstützung von Cursor-Tasten zum Blättern.

*Verbessert*

* CSV-Importer: Für die Suche nach verlinkten Objekten werden keine Begriffe mehr benutzt die länger als die Wortgrenze von 256 Zeichen sind. Das vermeidet einen Server-Fehler. 
* Der Link zur Dokumentation (angezeigt oben rechts, wenn konfiguriert) fügt nun nicht mehr automatisch die Sprache des Frontends an die URL.
* CustomMaskSplitter sind nun auch Panels und Reitern verfügbar.
* Viele kleinere grafische Verbesserungen.

*Behoben*

* Editor: Bei besonderen Konstellationen von voreingestellten Tags in Zusammenhang mit dem neue Objekte Dialog und Feldrechten die Karteireiter an- und ausschalten, kam es zu Sichtbarkeitsproblemen mit den Reitern.
* Detailanzeige: Die Darstellung verlinkter Objekte im Modus Text erfolgte fälschlicherweise bei Einstellung **Standard** in der Maske mit dem Standard aus dem Datenmodell und nicht mit der Standard (Best-Mask) Maske des Benutzers. 
* Datenmodell: Die Vorschau für neue noch nicht übernommene Objekttypen wurde repariert.
* Editor: Der Warndialog der anzeigt das ein anderer Benutzer das geöffnete Objekt neu gespeichert hat, wurde repariert.
* Gruppeneditor: Das automatische anlegen neuer verlinkter Objekte direkt im Gruppeneditor wurde repariert.

### Server

* Cache für ES-Analyze-Anfragen
* Batch-Verarbeitung für Wert-Laden, z.B. im Rechtemanagement und der Basiskonfiguration
* Unterstützung von Intranet-Rechtemanagement beim Export
* Nur ausgewählte Sprachen werden exportiert
* Mehr Informationen in Asset- und Download-Ereignissen
* Interne Informationen aus den Suchergebnissen entfernt
