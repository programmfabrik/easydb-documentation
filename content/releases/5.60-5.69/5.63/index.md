---
menu:
  main:
    name: "5.63"
    identifier: "5.63"
    parent: "releases569"
    weight: -563
---

> Dieses Release bringt viele Neuerungen im Bereich des Webfrontends, eine neue Seitenansicht im Editor und eine Detailvorschau im CSV-Importer.
>
> Es ist kein Neu-Index nötig, so dass Updates nur einen Neustart erfordern.

# Version 5.63.2

*Veröffentlicht am 17.02.2020*

### Webserver

*Behoben*

* **Neue Objekte**: Fehlermeldung beim Schließen des Dialoges behoben.

### Server

*Behoben*

* **Rechtemanagement**: Pool-ACLs mit Tagfilter funktionieren jetzt auch für Objekte deren Objekttyp keine Tag-Verwaltung aktiviert hat.

# Version 5.63.1

*Veröffentlicht am 14.02.2020*

### Webserver

*Behoben*

* **Editor**: Das erstmalige Benutzen der Sidebar führt nicht mehr zur Überlappung des Dialogs.
* **CSV-Importer**:  **Vorbereiten** wird jetzt erst aktiv, wenn ein Pool ausgewählt wurde (wenn nötig).

### Server

*Behoben*

* **Janitor**: Ein Bug führte zur Nichtberücksichtigung der **Basis-Konfigurations-Einstellungen** und dazu, dass der Janitor alle 10 Minuten gestartet wurde. Das wiederum führte zu unnötiger Last bei größeren Datenbanken.

# Version 5.63.0

*Veröffentlicht am 12.02.2020*

### Webserver

*Neu*

* Ein neuer Reiter **Versionen** in der Dateinformation zeigt eine Übersicht über die Verfügbaren Versionen einer Datei. In der Übersicht lässt sich auch das angezeigte Vorschaubild auswählen.
* **Editor**: Im Vollbildmodus kann die Dateivorschau in eine Seitenansicht verschoben werden. Damit bleibt der Blick auf die Vorschauen frei, auch bei komplexeren gestapelten Eingabeformularen.
* **Editor**: Mit `ALT`-Klick auf `+` lassen sich gestapelte Eingabeformulare im Vollbild-Modus öffnen.
* **Maskenmanagement**: Eine neue Einstellung erlaubt das **Ausblenden eines Reitersystems**, wenn nur ein Reiter angezeigt wird.
* **Maskenmanagement**: Neue Option erlauben unterschiedliche **Ausgabe-Einstellungen** für verlinkte Objekte in Tabellen- und Textansicht.
* **Tabellenansicht**: Einstellungen für manuelle Breiten werden jetzt für den Nutzer gespeichert.
* **CSV-Importer**: Die Auswahl eines Pools für neu erzeugte verlinkte Objekte ist jetzt möglich.
* **CSV-Importer**: Neue Anzeige der Datensätze in einer Detailansicht.

*Verbessert*

* **JSON/CSV-Importer** sind jetzt im Hauptmenü **Werkzeuge** verfügbar.
* **Developer-Menü** ist jetzt im Hauptmenü **Werkzeuge** verfügbar.
* **Detailansicht**: Starke Performance-Verbesserungen in der Anzeige bei vielen Vorschaubildern, wenn diese aus verlinkten Objekten stammen.

*Behoben*

* **Gruppeneditor**: Speichern ist jetzt möglich, wenn nur die Nutzereinstellungen verändert wurden. 
* **Mac**: Im Ressourcen-Dialog lässt sich jetzt `META` (Schwedischer Campingplatz Taste) genau wie `CTRL` unter Windows / Linux benutzen. 
* **Editor**: Die Vorlagenfunktion für reine Zahlfelder wurde repariert. 
* **Domain+Path-Support**: Verbesserte Unterstützung für easydb 6.
* Kleinere Fehler im **CUI-Layer-Management** behoben.

### Server

*Neu*

* **Basis-Konfiguration**: Einzelne Werte der Konfiguration können mit einem System-Recht geschützt werden. Verfügbar für Server-Plugins.
* **Server-Konfiguration** ist in Custom-Datatype-Update-Plugins verfügbar.

*Verbessert*

* Transaktionslaufzeit beim Bauen des **Suggest-Index** wurde optimiert, so dass es weniger Blockaden bei Datenbank-Commits gibt.

*Behoben*

* **Löschen** von Objekttypen mit Dateien in Exporter wurde repariert.
* **Export** von Dezimalzahlen korrigiert.
* Das Setzen der **Nutzersprache** für anonyme Anmeldungen wurde korrigiert.
* **Indexer-Crash** bei inkonsistenten Mappeneinstellungen wurde korrigert.
