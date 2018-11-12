---
title: "68 - Erweiterte Funktionen"
menu:
  main:
    name: "Erweiterte Funktionen"
    identifier: "webfrontend/administration/base-config/extended"
    parent: "webfrontend/administration/base-config"
---
# Erweiterte Funktionen {#design}

|Einstellung||Erläuterung|
|---|---|---|
|Logo & Kopfzeile|Logo|Hier kann ein Logo hochgeladen werden. Es wird in der Original-Auflösung und im Original-Format oben rechts angezeigt. Mit Mausrad + Move kann das Logo justiert werden. Über die .ini-Variable `[default-pics]logo` kann ein Pfad zu einem Standard-Bild festgelegt werden.|
||Hintergrundfarbe| Hintergrundfarbe das Logo wählen. Die Farbe betrifft die gesamte Kopfzeile, in welcher sich das Benutzermenü befindet. |
|Favicon|Favicon| Laden Sie hier ein kleines Icon / Symbol hoch, welches im Browser bei den Registerkarten (Tabs) und in der Lesezeichenleiste (Favoriten) angezeigt wird. |
|Dokumentation|Link-Button|Aktiviert im Frontend den Link-Button zur easydb Dokumentation. Der Button erscheint oben rechts in der Kopfzeile neben den Benutzereinstellungen.|
||URL|Bleibt dieses Feld leer, führt der Link standardmäßig zur allgemeinen easydb-Dokumentation. Es kann ein eigener Link zu einer individuellen Dokumentation hinterlegt werden.|
|CSS-Dateien|Eigenes Design für easydb erstellen.|Bei geladenem CSS-Plugin (Standard) erscheinen hier Eingabefelder zum modifizieren des geladenenen CSS. Das CSS-Plugin erkennt, wenn sich die angegebenen URLs ändern und stellt ein neues CSS für die Applikation bereit. Benutzen Sie auch das Tool [CSS-Developer], um mehr Übersicht über die geladenenen SCSS-Dateien zu bekommen. <br> Das CSS der easydb ist in [SCSS](http://sass-lang.com/) erstellt.|
||Header| Hier können URLs zu SCSS-Dateien angegeben werden, die vor dem Header-SCSS der easydb geladen werden. |
||Body| Hier können URLs zu SCSS-Dateien angegeben werden, die nach dem Body-SCSS der easydb geladen werden. |
|Connector||Über den Connector können andere easydb Instanzen angebunden und über die eigene Instannz durchsucht werden.|
||Alle aktivieren|Alle eingetragenen Instanzen aktivieren.|
||Instanz hinzufügen:|*Diese Feature befindest sich noch in Entwicklung*|
|Karten-Einstellungen|[Karten im Detail](/de/webfrontend/datamanagement/search/detail) anzeigen|Anzeige des Thumbnails in einer Karte, wenn die Datei Geokoordinaten enthält.|
||Anzeigen mit|- [OpenStreetMaps](https://www.openstreetmap.org/) <br> - [Mapbox](https://www.mapbox.com/)|
||Mapbox Token| Muss nur gesetzt werden, wenn die Anzeige mit Mapbox gewählt wird.|








