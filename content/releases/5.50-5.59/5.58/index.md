---
menu:
  main:
    name: "5.58"
    identifier: "5.58"
    parent: "releases559"
    weight: -558
---

> * Dieses Update benötigt eine **Neuindizierung**, planen Sie eine entsprechende Zeit für das Update ein.

# Version 5.58.1

*Veröffentlicht am 24.10.2019*

### Webfrontend

*Verbessert*

* **Kopieren von Rechtezeilen** funktioniert stabiler und erlaubt wieder das Kopieren einzelner Zeilen.

*Behoben*

* **Maskenauswahl** im Exporter funktioiert mit mehr als einem Objekttyp korrekt.
* Fehlermeldungen in der Druckvorschau bei einigen Mausklicks erscheinen nicht mehr.
* Verschwinden des Cursors in Suchvorschlägen sind behoben.

### Server

*Verbessert*

* Erkennung von **Emailadressen** beim Speichern ist erweitert und verbessert.
* **Peformanceverbesserung** für den XML-Exporter, auch für OAI/PMH.
* XML-Exporter exportiert für Linked Objects und Reverse Objects alle Systemfelder.
* **Rotieren und Zuschneiden** von Bilder ist repariert.

# Version 5.58.0

*Veröffentlicht am 17.10.2019*

### Webfrontend

*Neu*

* **Rechte** eines Typs lassen sich jetzt komplett kopieren.
* **Mehrzeilige Eingabefelder** werden automatisch in der Höhe angepasst.

*Verbessert*

* Anzeige von Standard A, B und C ist in den einzelnen Ansichten verfeinert und konsistenter gestaltet.
* Die Anzeige von Pool und Objekttype bei verlinkter Objekten (Anzeigeart *Text*) und in der Tabellenanzeige ist jetzt optional einstellbar und ist standardmäßig aus.
* **Nutzermanager**: Die Gruppen sind jetzt alphabetisch sortiert.
* Filter: Die **Suche in Filtern** erlaubt jetzt eine Groß- und Kleinbuchstaben unabhängige Suche und Platzhalter.

*Behoben*

* Die Anzeige der Dateitypen ist für einige Fälle repariert.
* **CSV-Importer**: Das Hochladen von Mappings ist jetzt stabiler wenn sich Datenmodelle geändert haben.
* **Gruppenmanager**: Der Reiter zur Anzeige der Benutzer ist für neu angelegte Gruppen ausgeblendet.
* **Voreinstellungen**: Für Mappen wird der Reiter Tagfilter nicht mehr angeboten. Tagfilter werden für Mappenrechte nicht unterstützt.
* **Usermanager**: Speichern wird jetzt aktiv, wenn nur der Zeitplan verändert wird.

### Server

*Neu*

* **/api/event/poll**: Neuer Parameter `limit`.

*Verbessert*

* **Performanceverbesserungen** für viele Operationen, inbesondere bei hierarchischen Objekttypen.
* **/api/search**: Es werden nur noch die Datenbanksprachen des Nutzers in `_standard`zurückgegeben, nicht mehr alle konfigurierten Sprachen.
* Beim Löschen von Objekten wird nachgefragt ob verlinkte Objekte mitgelöscht werden sollen oder nicht.

*Behoben*

* **/api/pool**: Maskenrecht ohne Masken in _acl wird jetzt korrekt gelesen und geschrieben 
* **Filter**: Das Inidizieren ist für einige Fälle repariert, z.B. abgeschnittene erste Buchstaben. Diese Änderung erfordert ein Neuindizieren des Index.
* **/api/db**: `skip_reverse_nested` gibt Vorwärtslinks jetzt korrekt aus, auch wenn dieser als Reverselink verwendet wird. 
* **/api/search**: Absteigende Sortierung nach Pool wurde repariert.