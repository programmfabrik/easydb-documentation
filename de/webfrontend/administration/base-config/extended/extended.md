# Erweiterte Funktionen {#design}

|Einstellung||Erläuterung|
|--|--|--|
|Logo & Kopfzeile|||
||Logo | Das Logo kann hochgeladen werden. Es wird in der Original-Auflösung und im Original-Format oben rechts angezeigt. Mit Mausrad + Move kann das Logo justiert werden. Über die .ini-Variable `[default-pics]logo` kann ein Pfad zu einem Standard-Bild festgelegt werden. |
||Hintergrundfarbe| Hintergrundfarbe für das Logo wählen. |
|Dokumentation|Link-Button|Aktiviert im Frontend den Link-Button zur easydb Dokumentation. Der Button erscheint oben rechts in der Zeile neben den Benutzereinstellungen.|
||URL|Bleibt diese Feld leer, führt der Link standardmäßig zur allgemeinen easydb-Dokumentation. Es kann ein eigener Link zu einer individuellen Dokumentation hinterlegt werden.|
|CSS-Dateien||Eigenes Design für easydb erstellen.|
|Karten-Einstellungen|[Karten im Detail](/webfrontend/datamanagement/search/detail/detail.html#geotag) anzeigen|Anzeige des Thumbnails in einer Karte, wenn die Datei Geokoordinaten enthält.|

Bei geladenem CSS-Plugin (Standard) erscheinen hier Eingabefelder zum modifizieren des geladenenen CSS. Das CSS-Plugin erkennt, wenn dsich die angegebenen URLs ändern und stellt ein neues CSS für die Applikation bereit. Benutzen Sie auch das Tool [CSS-Developer], um mehr Übersicht über die geladenenen SCSS-Dateien zu bekommen.

Das CSS der easydb ist in [SCSS](http://sass-lang.com/) erstellt.