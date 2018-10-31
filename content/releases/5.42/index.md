---
menu:
  main:
    name: "5.42"
    identifier: "5.42"
    parent: "releases"
    weight: -542
---

# Version 5.42.0

*Veröffentlicht am 31.10.2018*



### Webfrontend

*Neu*

* Hochladen-Menü bei Rechtsklick und als Favorit für Mappen.
* Exporter: Eine neue Funktion ermöglicht das Auswählen eigener Masken je exportiertem Objekttyp. Bei Exporten kann dadurch die easydb-seitige Auswahl der besten Maske überschrieben werden.

*Verbessert*

* Anzeige von Mehrsprachigkeit: Im Editor und Detail werden grundsätzlich alle gesetzten Sprachen angezeigt. Die Einstellung des Benutzers zur Datensprache bestimmen die Eingabesprachen der Editoren die mindestens sichtbar sind.
* Exporter: Dialog öffnet sich schneller, in einigen Fällen wurden viel zu viel Daten vom Server geladen.
* Entwickler: Im Debug-Modus werden keine Session-Cookies vom Server gesetzt und überprüft. Das vereinfacht in Chrome den Request komplett im CURL-Format zu kopieren.
* Datenmodell: Das Laden von defekten Datenmodellen führt nicht mehr zu einem Absturz, sondern erlaubt es das wenigstens das defekte Datenmodell zu verwerfen.
* Datenmodell: Vergrößerte und informativere Anzeige von Informationen in der Übersicht. 
* CUI: Korrektes Berechnen von Anzeige-Positionen auch wenn `margin`, und ` border` für den `BODY` verwendet werden. Das betrifft die Verwendung von easydb mit eigenem CSS.
* Kleine Suchen und Editoren haben eine Vollbild-Funktion.
* Verbessertes Design von Ausdrucken.
* Pools: Anzeige im Administrationsbereich wurde dadurch beschleunigt, dass wir nur noch die erste Kinderebene automatisch öffnen.
* CSV-Importer: Mehr Informationen in der Log-Datei.

*Behoben*

* Suche: Verbessertes Setzen des Cursor beim Filtern in der Schnellanzeige.
* Basis-Konfiguration: Korrektes setzen der minimalen Anzeige von Listenelementen (wie beispielweise Sprachen).
* Suche: Korrigierte Anzeige von verlinkten Bildern aus anderen Objekttypen in der Text-Ansicht.
* CSV-Importer: Fehlerhaftes Importieren von verlinkten Objekten wurde behoben.
* Präsentation: Export von PPTX von ungespeicherten Änderungen wurde behoben.
* Anzeige eines Menüs für Dateien in Reverse Nested Objekten wurde behoben.
* Die Anzeige von mehr als 1000 Mappen eines Benutzers ist jetzt möglich.
* Datenmodell: Unterstützung von UNIQUE für Custom-Data-Types wurde behoben.

