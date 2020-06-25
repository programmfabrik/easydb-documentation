---
menu:
  main:
    name: "5.45"
    identifier: "5.45"
    parent: "releases549"
    weight: -545
---

> * **Version 5.45.0** benötigt einen Re-Index, planen Sie entsprechende Downtime des Systems beim Update ein. **Diese Version stellt intern die Indizierung der Assets um, das hat zur Folge das initial alle Assets neu from Easydb-Asset-Server angefragt werden müssen.** D.h. die Downtime ist bei diesem Update länger als bei vorherigen Releases.
> * Die Datenbankgröße ist seit dieser Version gewachsen da mehr Informationen über Assets in der easydb Datenbank vom EAS zwischengespeichert werden. Dadurch vergrößern sich die Backup-Dumps der Postgresql-Datenbank.
> * Durch eine sehr unglückliche Kombination von Cache-Problemen und neuen Templates konnte es zu einem Fehler **"Not all required elements were found for Template"** kommen. Dieser Fehler erscheint aufgrund veralteter Templates von easdb im Browser-Cache. Wir haben versucht das Problem in **5.45.1.** abzuschwächen indem der Nutzer einen **"Neu Laden"** Option angezeigt bekommt. Das hat das Problem nicht vollständig behoben, da der Fehler beim nächsten Login wieder erschien. In **5.45.2.** gehen wir noch einen Schritt weiter und versuchen die veralteten Templates automatisch zu aktualisieren. Sollte der Fehler dennoch weiterhin bestehen, muss der Cache der betroffenen Browser manuell gelöscht werden. Danach sollte easydb wie gewohnt starten und funktionieren.

# Version 5.45.4

*Veröffentlicht am 30.01.2019*

### Server

*Behoben*

* Fehler im Update der EAS-Versionen in der Datenbank behoben. Es wurden sehr viele unnötige Indizierungsaufträge geplant.

### Fylr

*Behoben*

* Endpoint **/zip** Verbessertes Verbindungsmanagement bei Timeouts und DNS-Fehlern.

# Version 5.45.3

*Veröffentlicht am 25.01.2019*

### Webfrontend

*Verbessert*

* Die Lokalisierung der Connector-Einstellungen und Connector-Meldungen wurde überarbeitet.

*Behoben*

* Robustere Verarbeitung von fehlender **technical_metadata** in der Detailansicht mit aktivierter Kartenansicht.
* Ein Fehler im Zoomer hat zu einer Fehlermeldung geführt, wenn man mit aktiviertem Zoom auf ein neues Objekt ohne Vorschaubild geklickt hat.

### Server

*Behoben*

* Ein fehlerhaftes Transaktionshandling konnte bei größeren  Batch-Prozessen zu einem Dead-Lock in der Datenbank führen.

# Version 5.45.2

*Veröffentlicht am 22.01.2019*

### Webfrontend

*Neu*

* Die Unterstützung des **Internet Explorer 11** endet mit diesem Release. easydb zeigt eine Warnmeldung an, so dass Benutzer dieses Browsers informiert werden.

*Verbessert*

* Die Fehlerbehandlung bei veralteten Templates im Cache des Browsers der Benutzer wurde weiter verbessert.

*Behoben*

* Fix für den Bild-Zoomer, der bei unvollständigen Metadaten (siehe **Server**) einen Javascript-Fehler angezeigt hat.

### Server

*Behoben*

* In Instanzen in die mit **/eas/rput** Dateien übertragen wurden, wurden Metadaten nicht vollständig aktualisiert, so dass der Zoomer für Bilder nicht funktionierte und einen Javascript-Fehler angezeigt hat. Dieser Fix behebt das Problem im Server und indiziert die fehlenden Metadaten automatisch neu.

# Version 5.45.1

*Veröffentlicht am 18.01.2019*

### Webfrontend

*Neu*

* Für **Panel** kann im Maskeneditor ein automatisches Aufklappen in der Textansicht festgelegt werden. 

*Verbessert*

* Bei Fehlern die aufgrund von fehlenden Templates in der Startseite auftreten wurde die Fehlerausgabe so geändert, dass Nutzer ein Neuladen der Seite durchführen können, was dann die fehlenden Templates vom Server lädt.
* Ein ungünstiges ständiges Nachladen von **Wartungsmeldungen** wurde verbessert, so dass weniger Anfragen an den Server geschickt werden müssen. 

*Behoben*

* Die Detailansicht von Connector-Objekten bei angeschaltetem Logging "Detail ansehen", führte zu einem Fehler.
* Bei eingerichteter **Wartungsmeldung** in Zusammenhang mit aktiviertem Connector, konnte es zu einem Fehler kommten.

### Server

*Behoben*

* Die Cache-Header für die Startseite wurden bisher zu agressiv im Cache gehalten und bei Änderungen nicht aktualisiert. Das führte in 5.45.0. bei einigen Nutzern in Verbindung mit Chrome zu einem Javascript-Fehler der nicht mehr weggeklickt werden konnte.

# Version 5.45.0

*Veröffentlicht am 17.01.2019*

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

### Server

*Neu*

- **/api/settings** gibt jetzt auch die easydb Version zurück.
- **/api/search** Objekte können nach Asset-Eigenschaften gesucht werden.
- **/api/search** Längenbeschränkung für Suchwerte auf 256 Zeichen.
- **/api/db** Abgewiesene Workflows können Tags setzen, E-Mails senden und Webhooks auslösen.
- Neue Systemgruppe für über LDAP angemeldete Nutzer.

*Verbessert*

- Zu aktivierende Plugins werden beim Start geprüft, bei Fehlkonfiguration startet der Server nicht.
- Hochauflösende Video-Version wird nur bei ausreichender Originalgröße berechnet.
- Content-Type kann im Deeplink über XSLT-Attribut gesetzt werden.
- Mehr Anforderungen an zu speichernde Nutzer (Login oder E-Mail müssen gesetzt sein).
- Verbesserungen im Suggest-Index.
- Fehlerbehandlung beim Löschen von Pools verbessert.
- Keine Ereignisse für leere zeitgesteuerte Exporte.
- Erweiterungen im Metadaten-Mapping.

*Behoben*

- Fehler beim Löschen von Events entfernt.
- Benutzung von ico-Datei als Favicon korrigiert.

### EAS

- Raw-Format **.raf** unterstützt
- Geogebra-Zip-Dateien erhalten .ggb-Endung
- Fixes für .wmf

### Fylr

*Neu*

* Ein neuer [Link-Shortener](https://fylr.io/docs/fylr/server/link-shortener/) erlaubt das Erzeugen von gekürzten easydb URLs.