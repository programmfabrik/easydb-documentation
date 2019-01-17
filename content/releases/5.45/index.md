---
menu:
  main:
    name: "5.45"
    identifier: "5.45"
    parent: "releases"
    weight: -545
---

> * **Version 5.45.0** benötigt einen Re-Index, planen Sie entsprechende Downtime des Systems beim Update ein. Diese Version stellt intern die Indizierung der Assets um, das hat zur Folge das initial alle Assets neu from Easydb-Asset-Server angefragt werden müssen. D.h. die Downtime ist bei diesem Update höher als bei vorherigen Releases.

# Version 5.45.0

*Veröffentlicht am 17.01.2019*

### Server

* **/api/settings** gibt jetzt die easydb Version zurück.
* Zu aktivierende Plugins werden beim Start geprüft, bei Fehlkonfiguration startet der Server nicht.
* Hochauflösende Video-Version wird nur bei ausreichender Originalgröße berechnet.
* Objekte können nach Asset-Eigenschaften gesucht werden.
* Fehler beim Löschen von Events entfernt.
* Abgewiesene Workflows können Tags setzen, E-Mails senden und Webhooks auslösen.
* Content-Type kann im Deeplink über XSLT-Attribut gesetzt werden.
* Neue Systemgruppe für über LDAP angemeldete Nutzer.
* Benutzung von ico-Datei als Favicon korrigiert.
* Mehr Anforderungen an zu speichernde Nutzer (Login oder E-Mail müssen gesetzt sein).
* Verbesserungen im Suggest-Index.
* Fehlerbehandlung beim Löschen von Pools verbessert.
* Keine Ereignisse für leere zeitgesteuerte Exporte.
* Erweiterungen im Metadaten-Mapping.
* Längenbeschränkung für Suchwerte auf 256 Zeichen.

### EAS

* Raw-Format .raf unterstützt
* Geogebra-Zip-Dateien erhalten .ggb-Endung
* Fixes für .wmf

### Webfrontend

*Neu*

* Die Expertensuche erlaubt jetzt die **Suche nach dem Status für die Vorschauberechnung** in den Dateieigenschaften. Dadurch lassen sich Dateien finden deren Vorschau nicht erzeugt werden konnte.
* Die Expertensuche erlaubt jetzt die **Suche nach Asset-ID**.
* Auswahl **Ganze Seite** wurde zur Suche hinzugefügt.
* Bei Objekte mit mehreren Dateien in der Standardansicht können die Vorschauen auch im Suchergebnis durchgeblättert werden.
* Neues Custom-Mask-Splitter [Plugin](https://github.com/programmfabrik/easydb-hijri-gregorian-converter) zur Umrechnung von **Hijri** in **Gregorianische**- Kalenderdaten (Beta).
* Separatoren **Horizontaler Teiler** und **Block** sind jetzt innerhalb von **Reitern** und **Panels** erlaubt.
* Zwei neue Mitteilungstypen **Wartungsarbeiten Ankündigung** und **Wartungsarbeiten** im Administrationsbereich erlauben das Einrichten von Meldungen für Nutzer. Die Meldungen werden als Dialog präsentiert und können im Anschluss im Bereich oben rechts beim Klick auf ein Warndreieck erneut eingesehen werden. 

*Verbessert*

- Seperatoren im Maskeneditor haben verbesserte Farben.
- Die Änderungshistorie in der Detailansicht wird für Objekte nur noch dann angezeigt wenn der Benutzer mindestens ein Schreibrecht (**WRITE**) auf dem Objekt hat. Zuvor reichte ein Leserecht (**READ**) aus.
- Der Dialog zum Anlegen neuer Objekte speichert jetzt die Einstellungen.
- Suchen werden grundsätzlich nach 256 Zeichen beschränkt. Die Einschränkung ist die maximale Länge eines Suchbegriffs.
- Die Interaktion im Videoplayer beim Umschalten in Vollbild wurde verbessert.
- In der Basis-Konfiguration sind die vertikalen Reiter jetzt alphabetisch sortiert.
- Experensuche nach Begriffen in einem Stringfeld wurde verbessert. Der Suchbegriff wird jetzt komplett gesucht, nicht nur das Anfang des Suchbegriffs.
- Das Ereignis **Detailansicht ansehen** (DETAIIL_VIEW) speichert jetzt mehr IDs und den Pool des angesehenen Objektes.

*Behoben*

* Der Speichernbutton im Maskeneditor wurde nicht aktiv, wenn Einstellungen in **Custom-Data-Type**-Optionen verändert wurden.
* Bei Objekten mit mehreren Dateien,  war die Auswahl der Datei im Detail in einigen Fällen falsch.
* Herunterladen im **Connector** bei einer Auswahl von Connector-Objekten ohne Dateien wurde repariert.
* Anzeige des aktuellen Datenmodells bei aktivertem **Connector** wurde repariert.
* Beim Hochladen von Dateien mit aktiviertem Metadatenmapping werden bei Reverse-Nested-Relationen die Metadaten korrekt den Dateien zugeordnet.
* Das Hochladen von gleichzeitig mehreren Dateien per **Drag & Drop** in eine Arbeitsmappe wurde repariert.
* Die Anzeige der Änderunghistorie für Objekte mit bereits gelöschten verlinkten Objekten wurde repariert.

### Fylr

*Neu*

* Ein neuer [Link-Shortener](https://fylr.io/docs/fylr/server/link-shortener/) erlaubt das Erzeugen von gekürzten easydb URLs.