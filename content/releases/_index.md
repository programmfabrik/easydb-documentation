---
title: "6 - Releases"
menu:
  main:
    name: "Releases"
    identifier: "releases"
    weight: -980
---
# Releases

easydb wird in regelmäßigen Abständen um neue Funktionen erweitert, von Fehlern befreit und ständig verbessert.

> **Bitte beachten Sie, dass wir ab Juli 2018 unseren Release-Zyklus von zwei auf drei Wochen umstellen.**

* Der Zyklus für die Entwicklung von Versionen in easydb beträgt drei Wochen. Hierdurch stehen Kunden regelmäßig Aktualisierungen zur Verfügung. Die neuste Version wird bereitgestellt, sobald sie für die Verwendung durch den Kunden geeignet ist.
* Mängelbehebungen und Störungsbeseitigungen können zusätzliche Versionen erzeugen (auch "Patch" genannt).

### Aktualisieren

Das Aktualisieren entspricht den ersten Schritten der [Installation](/de/sysadmin/installation). Falls nicht anders vereinbart, liegt diese Aufgabe beim Kunden.

easydb-Instanzen auf unseren eigenen Servern, unter anderem für Tests und Präsentationen, werden durch uns aktualisiert.

# Versionen

## Version 5.37.0

*Veröffentlicht am 11.07.2018*

### Webfrontend

*Neu*

* Neuer Mitteilungstyp für Selbstregistrierung, damit lassen sich Anforderungen der DSGVO besser umsetzen.
* Connector: Neues Plugin zum Verbinden von easydbs. Das Plugin wird in einer ersten Alpha-Version ausgeliefert und kann in der Basis-Konfiguration und Systemrecht aktiviert werden. 
* Unterstützung von migrierten easydb 4: Objekte in Mappen und Präsentationen mit der Form ```<id>@easydb4``` werden erkannt und gesondert ausgewiesen. Solche Objekte können über den Connector mittels Kontexmenü gesucht werden.

*Verbessert*

* Speicher-Unterstützung für unbekannte (nicht geladenene) Custom Data Types, das Frontend sendet hier die Daten unverändert zurück an den Server, in vorhergehenden Versionen führte Speichern  zu Datenverlust.
* Verbesserte Statistik im Export und Download Dialog. Download ist jetzt beschränkt auf maximal 1000 Objekte, Export hat keine Begrenzung.
* Dateiauswahl für Typo3 und Drupal sendet jetzt alle verfügbaren IDs der verwendeten Objekte und Dateien aus easydb. Dieses Feature braucht noch Unterstützung durch die Plugins auf CMS Seite.
* Suchfilter unterstützen jetzt Wiederholgruppen korrekt.
* ALT/CTRL kann für Optionen und Formulare mit Checkboxen verwendet werden. Damit lassen sich lange Listen im Rechtemanagement schneller konfigurieren.

*Behoben*

* Bugfix für Internet Explorer 11 beim Download und Verwendung von Mitteilungen.
* Präsentationen mit Objekten ohne Dateien zeigen keinen Fehler mehr beim Drag & Drop.


### Server

*Verbessert*

* Beschleunigung von Suchanfragen bei Verwendung von vielen Pools.
* In Verlinkung editierbare Objekte können, wenn nicht verändert, schneller gespeichert werden. Das korrigiert auch gleichzeitig ein Speicherfehler der verursacht werden konnte, wenn Custom Data Types ihr JSON-Format geändert haben.
* Verbesserte Fehlerausgaben für Benutzer-Email und Rechte-Voreinstellungen.
* CSV Export für /api/event export maximal 100 Zeichen und hat korrigiertes Escaping.

*Behoben*

* Hierarchische Objekte werden mit allen übergordneten Objekten bei Änderungen neu indiziert.
* Fehler bei Überprüfung der Passwortmindestlänge korrigiert.

### Patch-Release 5.37.1

*Veröffentlicht am 18.07.2018*

### Server

* Fix für leere reguläre Ausdrücke beim Paßwort-Check, der Fehler führte dazu dass Paßwörter bei der Vergabe möglicherweise falsch geprüft wurden.

## Version 5.36.0

*Veröffentlicht am 20.06.2018*

*HINWEIS: Dieses Update erfordert eine Neuindizierung des Index, was einige Zeit in Anspruch nimmt. Bitte beachten Sie dies, wenn Sie das Update planen.*

### Webfrontend

*Neu*
* Masken-Editor: Neues Kontextmenü hinzugefügt, um die Position der Felder zu navigieren.
* Gruppen: Neuer [Reiter im Guppenmanager](../webfrontend/rightsmanagement/groups), der eine Übersicht der Benutzer anzeigt, die Mitglieder der Gruppe sind.
* [Script Runner](../webfrontend/datamanagement/search/find/script_runner): Skript kann über Browser gespeichert werden. Abbrechen Button hinzugefügt.

*Verbessert:*
* Präsentationen: Wenn Datensätze, die in Präsentationen verwendet werden, mehrere Bilder enthalten, erscheint nun eine Leiste, über die das gewünschte Bild ausgewählt werden kann.
* CSV Importer: Checkbox hinzugefügt, durch die wahlweise die interne Datenbankbezeichnung oder die Frontend-Übersetzung in der Feldauswahl für das Mapping angezeigt werden kann.
* Suche: Autovervollständigung und Eingabe für die einfache Suche und Expertensuche verbessert.
* Exportmanager: neue Checkbox, um alle Datenbanksprachen für den Export zu aktivieren. Standardmäßig werden nur alle aktiven Frontend-Sprachen exportiert.
* Detailansicht, Editor, Neu Datensätze: Die Maskenauswahl wird alphabetisch sortiert.
* Pool/Objekttyp-Auswahl in Recherche: Performance  verbessert, wenn viele Pools vorhanden sind.
* Custom Data Types: Anzeige in den Anzeigeoptionen Galerie, Text und Tabelle möglich, wenn es vom Custom Data Type unterstützt wird.

*Behoben:*
* CSV-Importer: Bei Updates werden keine Pool-Updates mehr gemacht.
* CSV Importer: Der "Neu einlesen"-Button setzt nun nicht mehr die Einstellungen für das Mapping zurück. 
* CSV Importer: Import von verlinkten Datensätzen repariert, wenn die Datensätze " " im Namen haben.
* Mappen: Es ist nun möglich, Dateien für Objekttypen ohne Poolmanagement in Mappen hochzuladen.
* Datenmodellserver: Fehler für einige spezielle Fälle bei der Synchronisation der Datenmodelle behoben.
* Editor: Beim Wechsel zwischen Sidebar-Editor und Vollbildeditor während des Editierens, werden bereits gemachte Eingaben nicht mehr verworfen.
* Neu-Editor: Felder die auf "nur lesen" gesetzt sind, werden im Neu-Editor nicht angezeigt.
* Filter: Anzeige für Jahrhunderte im Datumsfilter korrigiert.
* Basis-Konfiguration: Administrator-E-Mail Adresse wird nicht verwendet und wurde deshalb aus der Basis-Konfiguration entfernt.

### Server

* Wasserzeichen am Pool wird vererbt.	
	 Performanzverbesserung durch Batch-Verarbeitung im Hotfolder.	
* HTTP-HEAD-Unterstützung für /api/objects.
* Unterstützung für alle Sprachen im CSV-Export.
* Fehler bei _standard-Erzeugung aus L10N-Feldern behoben.
	 Pool-Sortierung benutzt implizit auch nicht aktive Frontend-Sprachen.	
* Erweiterung der Liste zugelassener Datei-Endungen.
* Vorschaubilder für einfache Text-Dateien deaktiviert.
* Administrator-E-Mail-Konfiguration entfernt, da sie nicht genutzt wurde.
* Reihenfolge von ACLs wird jetzt gespeichert.
* XML-Export von Dezimalzahlen korrigiert.
* Verbesserungen bei Fehlerbehandlung und Übersetzung.
	 Container: Abhängigkeiten der Container werden im Start-Skript behandelt. Reihenfolge und Wartezeiten zwischen Start der Container sind nun nicht mehr relevant.			

### Patch-Release 5.36.1

*Veröffentlicht am 28.06.2018*

#### Webfrontend

* CSV-Importer: Bei Updates werden nun keinen Pool-Update mehr gemacht.
* Suche: Begrenzung auf 100 Zeichen entfernt.

### Patch-Release 5.36.2

*Veröffentlicht am 29.06.2018*

#### Webfrontend

* Editor: Tag-Änderungen können wieder gespeichert werden, ohne das weitere Änderungen am Datensatz erforderlich sind. 

### Patch-Release 5.36.3

*Veröffentlicht am 04.07.2018*

#### Webfrontend

* Editor: Falsche "Ungespeicherte Änderungen"-Meldung beim Wechsel zu einem anderen Datensatz im Editor behoben.



---------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Patch-Release für Version 5.35

*Veröffentlicht am 12.06.2018*

### Server

* Fehler im Dateigrößen-Check vor XSL-Transformation behoben.
* Fehler bei langen Tabellen-/Feldnamen mit Datei-Spalten behoben.


## Version 5.35

*Veröffentlicht am 06.06.2018*

### Webfrontend

*Neu:*
* Kopieren ist jetzt auch aus dem Kontextmenü für einzelne Datensätze möglich.
* ScriptRunner: Einfache Scripts zum Download von Suchergebnissen als CSV oder JSON
* Drupal-CMS Schnittstelle

*Verbessert:*

* Aktualisiertes Download-Format für Datenmodelle, ältere Formate werden nicht mehr unterstützt.
* Besseres Zusammenspiel mit dem Datenmodellserver [(Objectstore)](/de/webfrontend/administration/datamodel), falls eingerichtet.
* Textansicht wurde beschleunigt.
* Vorausfüllen von Feldern im Neu-Editor durch Metadaten und Vorlagen verbessert.
* Neues Design für Basis-Konfiguration.
* CSV-Importer: Der Import von Bildern über URL wird unterstützt.
* CSV-Importer: Reverse verlinkte Objekttypen werden unterstützt.
* Gruppenmanager: Neuer Reiter (Tab), in dem angezeigt wird, welche Nutzer zu der Gruppe gehören.
* Benutzereinstellungen: Benutzer sehen nun in Ihren Einstellungen, zu welchen Gruppen sie gehören.
* Kleinere Verbesserungen für JSON-Importer.
* Usability für Zoom im Vollbild verbessert. Zoom-Navigation wird ausgeblendet, wenn der Mauszeiger nicht bewegt wird.
* Exportmanager: Neue Felder für den Export von CSV.

*Behoben:*

* STRG-Z in dynamischen Textareas führt nicht mehr zu einem Javascript-Fehler.
* Typo3 Schnittstelle hat in einigen Fällen nicht korrekt funktioniert.
* Teilen-Dialog: Eingabefeld für URL erweitert.
* Timing-Problem beim Suchen im Schnellzugriff für Adhoc-Mappe "Heute bearbeitet" behoben
* Laden eines Datensatzes über Deep Link, wenn eine Mitteilung auf der Startseite eingerichtet ist, behoben.
* Detailausdruck überarbeitet.

### Server

> WICHTIGER HINWEIS:  Der Namensraum des XML-Exports hat sich geändert. Sofern Sie diesen z.B. in der automatischen Nachbearbeitung per XSLT nutzen, müssen Sie den alten Wert `http://schema.programmfabrik.de/easydb-data/1.0` in den neuen Wert `https://schema.easydb.de/EASYDB/1.0/objects/` ändern.

> WICHTIGER HINWEIS:  Viele der mitgelieferten Plugins werden jetzt standardmäßig aktiviert. Wenn Sie eines dieser Plugins bereits als [Extension-Plugin](/de/sysadmin/plugin) aktiviert haben, wird das Probleme beim Server-Start hervorrufen. Sie haben in diesem Fall folgende Möglichkeiten:
> * Deaktivieren des mitgelieferten Base-Plugins mit [plugins/enabled-](/de/sysadmin/konfiguration/plugin). Wenn z.B. das Plugin `extension.custom-data-type-link` verwendet werden soll, muss `base.custom-data-type-link` deaktiviert werden.
> * Deaktivieren des konfigurierten Extension-Plugins. Sofern dieses Extension-Plugin nur verwendet wird, weil es von der easydb bisher nicht mitgeliefert wurde, so ist diese Option die beste Wahl.

* Ersatzausgabe der Objekt-ID in `_standard` wird nur noch für die erste Datensprache ausgegeben.
* `ez-standard-missing`-Klasse aus `_standard` entfernt.
* Unterstützung des Typs `elasticsearch` in Suche/Aggregation entfernt.
* Highlighten für verlinkte Objekte in Autovervollständigung entfernt. In speziellen Konfigurationen kam es dadurch zu Geschwindigkeitseinbrüchen.
* Metadaten-Import: Leerzeichen am Anfang und Ende von Werten werden entfernt. Leere Werte werden nicht weitergegeben.
* Leere Spalten im CSV-Export werden nicht mit ausgegeben.
* Im CSV-Export werden nun mehr Informationen für verlinkte Datensätz ausgegeben.
* `_format` in `GET /api/v1/db` korrigiert, wenn `long` angefordert wurde.
* Konfiguration eigener Datentypen in der Plugin-Beschreibung hat sich geändert.  Plugins müssen ggfs. angepasst werden.
* Eigene Events können in der Plugin-Beschreibung definiert werden. Die allgemeine Möglichkeit, Server-Konfiguration in der Plugin-Beschreibung zu definieren (`yaml_config`), wurde entfernt und erzeugt einen Fehler bei Verwendung.
* Bei Neuinstallation dürfen jetzt standardmäßig alle Dateitypen hochgeladen werden.
* In Fehlermeldungen können nun übersetzte Tabellen- und Spaltennamen angezeigt werden.
* Behandlung von eigenen Datentypen im CSV-Export verbessert.
* Fehlerbehebung verbessert.
* Autovervollständigung für Tokens beschleunigt.
* Übersetzungen werden für die korrekten Sprachen geladen. Entfernt falsche Warnungen.
* Schema und Namensraum sind jetzt für OAI/PMH-Export in der Konfiguration definierbar.

---------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Version 5.34

*Veröffentlicht am 23.05.2018*

### Webfrontend

* Über Gruppen können Voreinstellungen für Benutzereinstellungen vergeben werden. Diese sind bei neuen Benutzern der Gruppe dann als Standard aktiv.
* Erweiterung des Filters für Datumsbereiche: nach Jahrtausenden, Jahrhunderten, Jahrzehnten und v. Chr.
* Neuer Datentyp: Geokoordinaten. Ermöglicht am Datensatz eigene Koordinaten in einer Karte zu setzen.
* Überschrift "Alle Mappen" aus Schnellzugriff entfernt.
* Auswahl für Pools/Objekttypen mit SHIFT und ALT für Firefox verbessert.
* Erweiterung für XML Exporte: Custom Data Types können für den XML Export ausgewählt werden. Wird ein Standard vom Plugin unterstützt, kann dieser für den Export gewählt werden. Andernfalls wird der gesamte Dateninhalt exportiert.
* Bugfix für das Laden des Editors in der Sidebar
* Bugfix für das Markieren & Kopieren von Text in Wiederholgruppen
* Bugfixes für Anmeldedialog
* Custom Data Types können für Filter aktiviert und für das Frontend ausgeblendet werden, um sie nur über API anzusprechen.
* Bugfix für Änderungen in Datumsfeldern über die Kalenderfunktion

### Server

* Leere Unterpools werden beim Löschen von Pools automatisch gelöscht
* Verbesserte Fehlerbehandlung beim Speichern von Pools
* Aufrufe für POST /api/settings können nun einzeln aktiviert werden (purgeall, purgedata, restart)
* Indizierung hierarchischer Objekte korrigiert
* Fehlerbehandlung im Gruppeneditor verbessert
* Suche: Changelog nicht mehr in "long"-Format, dafür neues "full"-Format
* Suche: mehr Daten im "long"-Format
* Fehlerbehandlung beim Löschen von Tags verbessert
* Frontend-Info für Gruppen in Session-Daten
* Komplexe _standard-Ausgabe (z.B. aus verlinkten Objekten) in Transition-E-Mails implementiert
* "_standard" für Custom-Typen aus Plugins unterstützt
* Sortierung nach verlinkten Objekten korrigiert

---------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Version 5.33

*Veröffentlicht am 09.05.2018*

### Webfrontend

* Beim Start wird die Benutzer-Frontend-Sprache nicht mehr automatisch gesetzt, wenn der Browser andere Einstellungen in einem Cookie gespeichert hat.
* Verbessert: Neuer Volltext Typ in der Suche. Mit einfachen Anführungszeichen ('wort') kann nun exakt gesucht werden.
* Verbessert: Ist Mehrsprachigkeit für die Datenbank aktiviert, werden die Mappen alphabetisch entsprechend der aktiven Anwendungssprache sortiert
* Verbessert: Einträge für Datumsfelder müssen zwischen 0 und 9999 liegen
* Bugfix für den Upload von Datenmodellen im json-Format.
* Bugfix für Memory-Leaks im Detail und Editor gefixt
* Bugfix für Vorbelegungen im Editor Plugin
* Bugfix für Vollbild und Zoom in der Dateivorschau für Internet Explorer 11
* Bugfix für JSON Importer
* Bugfix für Mappen: Kleiner Korrekturen für Mappen

### Server

* ArtworkCreator und ArtworkContentDescription für XMP-iptcExt werden im Profil für den Metadaten-Import bereitgestellt.
* Verbesserte Nachfrage beim Löschen noch verwendeter Datensätze
* API-Erweiterung: GET /api/l10n/user/<version> & /api/mask/<version>
* Angabe für Dauer einer Arbeitsmappen-Freigabe in E-Mail-Template hinzugefügt
* Zu strenge E-Mail-Adressvalidierung in Basiskonfiguration gelockert
* mehrere Suchbegriffe in /api/suggest werden jetzt UND-verknüpft
* _relative_filename im Export jetzt relativ zur XML-/CSV-Datei
* Benutzer mit root-Recht können jetzt alle Rechte an Arbeitsmappen vergeben
* Limit für _objects (1000) in /api/collection
* Fehlerbehandlung beim Löschen von Tags korrigiert
* "login" wird für archivierte Nutzer nicht mehr geleert, constraints angepasst
* Arbeitsmappen von archivierten Nutzern werden gelöscht

---------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Version 5.32

*Veröffentlicht am 26.04.2018*

*HINWEIS: Dieses Update erfordert eine Neuindizierung des Index, was einige Zeit in Anspruch nimmt. Bitte beachten Sie dies, wenn Sie das Update planen.*

### Webfrontend

* Neu: [Kategoriebrowser](../webfrontend/datamanagement/search/quickaccess/category) - Hierarchien- und Listen in der Schnellanzeige anzeigen
* Verbessert: Detail/Editor - Horizontaler Teiler und Block werden für verlinkte Datensätze vom Mode "Text" gerendert
* Verbesserte Anzeige von Horizontalen Teilern und Blöcken in verlinkten Datensätze
* Bugfix: Objekt-ID kann über Masken-Einstellungen auch für Reverse-Nested im Detail und Editor eingeblendet werden
* Bugfix für Datumseingabe von BC Daten
* Bugfix für die Anzeige von Mappen bei eingeschränkten Rechten
* Bugfix für Uploads in Nesteds. Update erzeugt jetzt keine neue Reihe.
* Bugfix für Suche und Anzeige von Datensätzen, deren Sprache abweicht von den gesetzten Einstellungen in Datenspracheinstellungen
* Verbessert: Upload von Verzeichnissen wird jetzt auch von Internetexplorer 11 und Edge unterstüzt
* Verbessert: Die Maskenauswahl wird jetzt auch im Editor Popover angezeigt
* Verbessert: Die Suche im Benutzermanager unterstützt jetzt auch die Suche nach Benutzer-ID
* Verbessert: Die Filter für die Suche können nun als Präferenz gespeichert werden und werden bei neuen Aufrufen standardmäßig angezeigt
* Bugfixes für [Editor-Plugin](../webfrontend/administration/base-config/editor)
* Bugfix für Export-Manager
* Bugfix: Die Anzeige von Pflichtfeldern innerhalb von Panels wurde korrigiert
* Bugfix: Die alphabetische Sortierung der Mappen entspricht jetzt der präferierten Datensprache des Benutzers


### Server

* Größe von XML-Dateien wird vor XSL-Transformation geprüft, Vorgabe max. 10 MB
* Fehlermeldung bei doppelten Export-Namen verbessert
* Der Linkabgleich mit dem EAS ist nun standardmäßig aktiviert. Assets, die nicht in der easydb verlinkt sind, werden vom EAS automatisch gelöscht.
* show_in_collections in /api/v1/objecttype für [Kategoriebrowser](../webfrontend/datamanagement/search/quickaccess/category)
* Bugfix für falschen Besitzer in Änderungshistorie
* Rechte "link"/"unlink"/"create_in_collection" in Mappen werden vererbt
* Neues Export-Profil: Metadaten können optional ersetzt oder erhalten werden
* Fehler bei Anmeldung mit vormals gelöschtem SSO- oder LDAP-Nutzer behoben
* Suchsprache für Pool-Aggregationen korrigiert (Frontend-Sprache notwendig)
* Für alle aktivierten Sprachen wird nun _standard zurückgegeben
* Indizierung von reverse-verlinkten EAS-Feldern korrigiert
* /api/v1/settings liefert jetzt aktuelle Schema-Version zurück

---------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Version 5.31

*Veröffentlicht am 12.04.2018*

*HINWEIS: Dieses Update erfordert eine Neuindizierung des Index, was einige Zeit in Anspruch nimmt. Bitte beachten Sie dies, wenn Sie das Update planen.*

### Webfrontend

* Verbesserungen und Bugfixes für JSON Importer

* Verbesserung in der Pool-Auswahl: Enthält ein nicht aktiver Pool einen aktiven untergeordneten Pool, wird der übergeordnete Pool mit einem Minus markiert
* Verbesserung für hierarchische Objekttypen: Hierarchien verhalten sich jetzt in der Tabellenansicht entsprechend wie in der Standard- und Textansicht
* Verbesserung für Ausgabe bei Mehrsprachigkeit: In der Detailansicht werden nun alle Sprachen (nicht mehr nur die bevorzugte Sprache) angezeigt, für die Einträge vorhanden sind
* Neue Option für Masken im Datenmodell: In Wiederholgruppen (Nested Fields) können die Feldnamen ausgeblendet werden.
* Erweiterung für Mitteilungen: neue Option für einen [ständigen Hinweis für Benutzer](/de/webfrontend/administration/messages). Hinweis erscheint als Button neben den Benutzereinstellungen in der Kopfzeile.
* Sortierung für Suchergebnisse berücksichtigt jetzt auch Custom Data Types (aus Plugins)
* Pool-Management: Verfeinerung des Rechtemanagement durch Zuweisung eines [Verantwortlichen](/de/webfrontend/rightsmanagement/pools)
* Datenmodell: [JSON-Download/Upload](/de/webfrontend/administration/datamodel) für Schema, Masken und Lokalisierung
* Anzeige von Objekt-ID über Maskeneinstellung in Detail und Editor
* Mit STRG-Rechtsklick wird jetzt das Browser-Menü erreicht
* STRG-ALT-Klick aktiviert die gewählte Checkbox und alle nachfolgenden Checkboxen (nicht die, die davor liegen) (z.B. Datenmodell > Masken oder Basis-Konfiguration Dateitypen für Upload)
* Benutzer-Management: Gruppen-Namen werden mit ins CSV exportiert
* Benutzer-Management: Excel-UTF-8 Kompatibilität für CSV
* Benutzer-Management: Verbesserte Ladezeit
* Bugfix: mehrere Fixes für Probleme bei schellen Klicks
* Bugfix: für Mehrsprachigkeit in Eingabefeldern: Bei Einträgen in verborgenen Sprachen werden die Eingabefeld der nicht belegten Sprachen nicht mehr als Pflichtfelder markiert
* Bugfix: Editor hat nicht geladen, wenn ein unkorrekter Weblink über API in ein Datenfeld geladen wurde
* Bugfix für Mappen: Bugfixes für Rechte-Check bei "Erzeugen in Mappe"
* Bugfix für Mappen: *Alle auswählen* funktioniert wieder
* Bugfix für Login: Link und Link-Text für SSO-Anmeldung kann über Basis-Konfiguration für Login-Maske aktiviert und angepasst werden
* Bugfix: Anzahl in der Objektliste wurde nicht korrekt aktualisiert, nachdem neue Datensätze hinzugefügt oder welche gelöscht wurden.
* Bugfix für Mitteilungen: Mitteilung für Startseite in der Suche wurde nicht korrekt angezeigt
* Bugfix für Pool-Management: Wechsel zwischen Pools hat falsche Fehlermeldung ausgegeben
* Weitere kleinere Bugfixes

### Server

* Entfernen von Dateien in der Basiskonfiguration ermöglicht (z.B. Logo)
* Nicht ausgefüllte Sprachen bei lokalisierten Feldern werden für Base-Typen in der API nicht mehr ausgegeben
* Objekt-ID als Option in Maskendefinition
* Übersetzte Spaltennamen im CSV-Export
* Referenzfeld für Mappen wird bei Änderungen durch Benutzer aktualisiert
* Besitzerrechte für Pools wieder eingeführt
* /api/eas/rput beschleunigt
* Es werden nur noch aktivierte Datenbanksprachen in den Index übernommen. Das Hinzufügen neuer Sprachen erfordert ein Neuerstellen des Index, was nicht durch die Konfigurationsänderung erzwungen wird. Das Aktivieren einer neuen Schema-Version ist dazu erforderlich.
* Link in Workflow-E-Mail korrigiert
* Fehler bei Indizierung komplexer Masken behoben
* Neuindizierung von Mappen bei Änderung einer übergeordneten Mappe
* generate_rights für Mappensuche behoben

## Version 5.30

*Veröffentlicht am 14.03.2018*

### Webfrontend

* Verbesserungen für JSON Importer
* Erste Version für Sortierung von custom-data-types verfügbar
* Neue Code Dokumentation: Alphabetischer Index verwendeter Klassen in easydb5. Befindet sich aktuell noch im Entwicklungsstadium > [Preview](https://programmfabrik.github.io/easydb-code-documentation)
* Neues github Repository für easydb Plugin Beispiele > [easydb-plugin-examples](https://github.com/programmfabrik/easydb-plugin-examples)

### Server

* Bugfix: Volltextsuche in rückwärts-verlinkten hierarchischen Objekttypen korrigiert
* Bugfix: Fehler im CSV-Export behoben
* Bugfix: Fix für Lookup-Feature in POST /api/db
* Pool-Rechte haben jetzt Auswirkungen auf untergeordnete Pools
* Ausgabe von Asset-Informationen in Mehrfachfeldern korrigiert, sodass Suche nach Asset-Attributen aus Mehrfachfeldern jetzt möglich ist
* /api/eas/rput-Anfrage zur Beschleunigung der Migration eingebaut. Diese API befindet sich momentan noch im Entwicklungsstadium (Änderungen vorbehalten).
* Neue Datensprache "und" (="unbestimmt") für nicht identifizierbare Sprachen hinzugefügt
* Mapping wird aktualisiert, wenn "Pool-Verwaltung" für einen Objekttyp aktiviert wird
* API: Collection-API erweitert, um beim Speichern von Mappe enthaltene Objekte angeben zu können
* API: API toleriert jetzt Null-Bytes in JSON-Eingaben


## Version 5.29

*Veröffentlicht am 28.02.2018*

### Webfrontend

* Speichern und Laden der Basis-Konfigurationseinstellung in und aus einer Datei.
* Einstellung "Versionen erkennen" im Datei-Uploader wird für Benutzer gespeichert.
* Unterstützung von Sortieren von verlinkten Objekten in Wiederholgruppen.
* Bugfix: Bei manchen Sprach-Einstellungen im Browser kam es zu einem Ladeloop beim Login, wenn die easydb mit Mitteilungen konfiguriert war.
* Bugfix: Autovervollständigung wurde im Internet Explorer teilweise überlappend dargestellt.

### Server

* API: Filter für Benutzer_ID hinzugefügt
* API: Limit & Offset als URL Parameter für collection/list-API implementiert
* API: Limit für collection/list-API auf 1000 Datensätze begrenzt
* Kleinere Bugfixes


## Version 5.28

*Veröffentlicht am 14.02.2018*

*HINWEIS: Dieses Update erfordert eine Neuindizierung des Index, was einige Zeit in Anspruch nimmt. Bitte beachten Sie dies, wenn Sie das Update planen.*

### Webfrontend

* Verbessertes Block-Rendering: Das Nebeneinander-Anordnen von Feldern ist jetzt auch außerhalb von Blöcken, innerhalb von Panels und Reitern und innerhalb von nicht einfachen Mehrfachfeldern möglich.
* Datenmodell: Download und Upload von Datenmodellen als CSV (nur für Objekttypen).
* Datenmodell: Verbesserter Support für Objectstore zum Verteilten Entwickeln von Datenmodellen.
* Server-Manager (Plugin): Neues Menü zum Neustart des Servers, Löschen aller Daten und Löschen des Datenmodells.
* Bugfix für Google Chrome: Testlink für Freigabe-URL startete eine neue Benutzer-Session.
* Bugfix: CSS-Developer hat sich nicht geöffnet.
* Bugfix: Sprachauswahl im Collection-Setting zeigt jetzt die richtige Sprachliste an.
* Bugfix: Collection Alle-Auswählen funktioniert wieder korrekt.
* Verbesserung: Such-Autocompletion bei schnellem Tippen verbessert.

### Server
* Locking für /api/user zur Verbesserung der Performance entfernt
* USER_LOGIN-Event für Authentifizierung per LDAP/SSO ergänzt
* "IPTC:Caption-Abstract" als Quelle für "Beschreibung" beim Metadaten-Import hinzugefügt
* API zum Zurücksetzen der Datenbank und des benutzerdefinierten Datenbank-Schemas hinzugefügt
* Fehler bei der Behandlung von Namensräumen im XSLT behoben
* "Latein" als neue Datensprache ("la") ergänzt


## Version 5.27

*Veröffentlicht am 31.01.2018*

#### Webfrontend

* Block-Rendering in Masken (Nebeneinander Ordnen von Feldern) möglich, wobei die Breite der Felder auf 25%, 50%, 75% bzw. 100% (Standard) gesetzt werden kann
* Bugfix für Wasserzeichenversionen:  existiert eine gleichwertige Version ohne Wasserzeichen wird Benutzern diese bevorzugt angezeigt
* Highlighting ist deaktiviert, um Suchanfragen für komplexe Datenmodelle zu beschleunigen
* Eigene Felder Auswahl zeigt jetzt den Datenbanknamen und den lokalisierten Feldnamen (Exporter)
* Die Vergabe von Namen für Mappen ist jetzt mehrsprachig
* Bugfix für Custom Data Type Suche innerhalb von Mehrfachfeldern
* Bugfix für den Auswahldialog von Objekttypen und Pools in der Suche

#### Server

* Benutzer werden mit allen für sie hinterlegten E-Mail-Adresse gefunden (nicht nur mit der bevorzugten)
* Laden von Dublin-Core-Mapping für OAI/PMH-Export korrigiert
* E-Mail-Absender-Name (Anzeigename) kann in Konfiguration gesetzt werden
* Vorgabe-Typ für XSLT-Ausgabe wiederhergestellt (XML), entsprechende Direktiven in der XSL-Datei wieder optional
* Beschleunigung des Server-Starts
* Hotfolder-Prozess ist weniger CPU-intensiv
* LDAP-Plugin erlaubt jetzt auch Gruppensuche mit mehrwertigem Attribut
* Passwort-Vergessen-Link im Textteil der entsprechenden E-Mail korrigiert


## Version 5.26

*Veröffentlicht am 18.01.2018*

*HINWEIS: Dieses Update erfordert eine Neuindizierung des Index, was einige Zeit in Anspruch nimmt. Bitte beachten Sie dies, wenn Sie das Update planen.*

#### Webfrontend

* Datenmodell (Entwicklung): Für Objekttypen können mehrere Felder auf einmal erstellt werden
* Datenmodell (Entwicklung): Objekttypen können mit dazugehörigen Masken kopiert werden
* Datenmodell: Sortierung für Objekttypen (Alphabetisch und nach Haupt-/Neben-Objekttyp)
* Ereignisse können jetzt nach ID durchsucht werden

#### Server

* _last_updated_date zur JSON-Repräsentation des Exports hinzugefügt
* Pool-Rechte werden beim Download von Assets aus Wiederholgruppen beachtet
* E-Mail mit generiertem Passwort korrigiert
* Mehrere Ereignisse können mit einer Server-Anfrage gelöscht werden
* Felder für einige neue Sprachen und Schriften wurden hinzugefügt. Die Suche ist noch nicht auf die einzelnen Sprachen abgestimmt.


## Version 5.25

*Veröffentlicht am 20.12.2017*

#### Webfrontend

* Pool-Info Anzeige im Detail
* User-Agent (Name des Browsers) wird bei Frontend Fehlern mit gespeichert
* Benutzer / Gruppen-Auswahl mit Icon
* System-Recht zum Abschalten der Column-Filter
* Experten-Suche nach Hierarchie-Status eines Objektes
* SSO-Login: Support für "window_open=self"
* Mitteilungen für die Startseite der Suche
* Erweiterte Login-Mitteilung im Login-Dialog
* Feld-Attribut "ez5-field-name" im Detail / Editor
* Vorlagen "Ergänzen" funktioniert für mehrzeilige Textfelder und Mehrfachfelder
* Download-Manager zeigt Anzahl im Titel
* CSV-Hierarchy Option im Exporter
* Zum Überwachen Ihrer easydb können Sie nun unser freies [Plugin](https://github.com/programmfabrik/check-easydb5) nutzen, mit Nagios oder Icinga.

#### Server

* der Export kann jetzt für CSV und easydb-XML mit unlimitierter Batch-Größe arbeiten
* easydb-4-Passwort-Hashes können in der Migration übernommen werden
* Ablaufdatum der E-Mail-Bestätigungslinks entfernt
* Jahre vor Chr. funktionieren jetzt korrekt in Datumsbereichen
* Mappen werden neu indiziert, wenn untergeordnete Mappen verschoben werden
* Gruppen aus LDAP können bei SSO-Authentifizierung übernommen werden
* Referenz- und Kurznamenfelder in Basis-Typen müssen jetzt eindeutig sein
* Meldung für den Benutzer beim Löschen von noch verwendeten Tags
* Verbesserte Fehlermeldung bei Verletzung von UNIQUE-Constraints


## Version 5.24

*Veröffentlicht am 06.12.2017*

#### Webfrontend

* Info über die letzte Aktualisierung des Datensatzes in Detail und Editor
* Vorlagen für Eingaben werden in allen Editoren unterstützt.
* Platzhalter Objekte-Icons (und Text) kann über CSV konfiguiert werden.
* Einstellungen für Druck-Qualität und -Stil.
* Rechte-Zeilen können kopiert werden.
* Mappen können kopiert werden.
* Bedienbarkeit der Präsentationen verbessert.
* Fehlerbehebungen u.a. in CSV-Importer, Detail, Mappen-Suche, Datenmodell-Editor

#### Server

* Bereinigung beim Löschen von Tags
* Mapping von Farbtiefe und Auflösung (DPI) für Bilder ermöglicht.
* Unicode-Normalisierung für die Suche.
* Verhalten der `unique_id`-Plugin-Funktionen mehr an PostgreSQL-Sequences angepasst, lange Locking-Zeiten werden vermieden.
* Referenz-Felder für Base-Typen werden geladen/gespeichert.
* Bestätigungslink für E-Mails läuft nicht mehr ab.
* Bug-Fixes und interne Verbesserungen.

## Version 5.23

*Veröffentlicht am 22.11.2017*

#### Webfrontend

* Reiter in Masken können jetzt Überschriften haben
* Pool-Deep-Link /pool/<shortname> ergänzt, funktioniert für alle Pools mit gesetzem Shortname
* Shift zum Erweitern der Markierung wird unterstützt
* Drucken von Text-Ansicht und verschiedene Qualitäten
* Anzeige alter Versionen auch im Detail
* Link im Tray zur Dokumentation, konfigurierbar in der Basis-Konfiguration
* Datensätze können als Vorlage im Gruppen-Editor verwendet werden
* Navigation in Gruppen-Editor, dadurch lädt der Editor viel schneller mit vielen Objekten
* Automatischer Kommentar im Gruppen-Editor
* SSO: Logout kann konfiguriert werden
* Plugins: Custom Settings für Masken erweitert
* Bugfix: Speichern von Reverse-Nested die nicht sichtbar sind ist wieder möglich
* Bugfix: Sortierung in der Objekttypen/Pool-Auswahl ist jetzt lokalisiert
* Bugfix: Suche Dateinamen erlaubt jetzt alle Such-Funktionen

#### Server

* Über Plugins (z.B. pro Solution) können kundenspezifische E-Mails bereitgestellt werden.
* Im Gruppeneditor kann ein Kommentar für alle Änderungen angegeben werden.
* Tag-Updates lösen User-Objekt-Indizierungen aus.
* Systemrechte können nur weitergegeben werden, wenn man sie selbst besitzt.
* Remote-Objekte in Collections.
* Aufräumen nicht bestätigter E-Mails deaktiviert.
* Besitzer reverse-verlinkter Objekte wird erhalten.
* Changelog-Suche erweitert.
* Bug-Fixes und interne Verbesserungen.

## Version 5.22

*Veröffentlicht am 08.11.2017*

#### Webfrontend

* Maskeneinstellung für Boolsche Werte um den Status "false" im Detail zu zeigen
* Maskeneinstellung um Karten-Anzeige auf bestimmte Werte zu beschränken
* Unterstützung von v. Chr. Daten in Datumsfeldern
* Exporter-Erweiterung zum Exportieren von verlinkten Datensätzen
* Suche: Anzeige von untergeordneten Datensätzen in hierarchischen Datensätzen
* Suche: Erweiterung der Änderungssuche auf alle Änderungen, nicht nur die letzte
* Editor: Fehler beim Verschieben von Mehrfachfeldern behoben
* SSO: Unterstützung von Logout für Single-Sign-On (wie beispielsweise Shibboleth)

#### Server

* Alte Datensatzversionen liefern nun auch alte Tag-Verknüpfungen
* Bessere Fehlermeldungen und Nutzerentscheidungen beim Löschen von hierarchischen Datensätzen
* Exporter-Erweiterung zum Exportieren von verlinkten Datensätzen
* Parameter für die Bearbeitung von ACLs/Systemrechten an Nutzern und Gruppen vom Schreibrecht zum Systemrecht verschoben
* Optimierung der Indizierung alter Datensatzversionen
* Möglichkeiten zur Suche im Changelog verbessert
* Weitere kleinere Fehlerbehebungen und Verbesserungen

## Version 5.21

*Veröffentlicht am 25.10.2017*

#### Webfrontend

* Detail: Plugin-Schnittstelle für Detail Anzeige in der Sidebar
* Karte: [Darstellung von GPS-Koordinaten](/de/webfrontend/datamanagement/search/detail) von Bildern auf einer Karte (OpenStreetMap), dieses Plugin ist [Open-Source](https://github.com/programmfabrik/easydb-detail-map-plugin)
* Custom Data Types: NULL und Unique sind im Datenmodell verfügbar
* Verbesserte Navigation in der Event-Anzeige
* Fix für einen Bug beim Login für anonyme Nutzer
* Nutzermanager: Anlegen von LDAP und SSO Nutzern bevor diese sich angemeldet haben
* Option zum Verändern des Link-Textes für SSO-Logins
* Ausgabe von IDs für Objekttypen, Masken und Pools zur Vereinfachten Benutzung der API

#### Server

* GPS-Informationen sind in den ausgegebenen Asset-Metadaten enthalten.
* Pfad-Informationen für hierarchische Objekte im XML-Export wurden erweitert.
* XML-Namensraum für "easydb"-XML-Export, besonders für OAI/PMH-Schnittstelle.
* Checks im Datenmodell ("not_empty", "email", "regexp", "range") werden nicht mehr in der Datenbank forciert.
* Speicherlecks im Exporter wurden entfernt.
* Nachfrage (HTTP 202) beim Löschen von hierarchischen Objekten mit Kindern.
* Löschen von im Changelog referenzierten Gruppen ermöglicht.
* Weitere kleinere Fehlerbehebungen und Verbesserungen.

## Version 5.20

*Veröffentlicht am 12.10.2017*

#### Webfrontend

* Präsentationen können gelöscht werden, ohne die ganze Mappe zu löschen.
* Neu-Anmelden repariert für Benutzer mit unerledigten Aufgaben.
* Uploader: Race-Kondition repariert für große Bulk-Uploads bei zu schnellem Klicken.
* Datenmodell: Masken-Optionen für EAS-Standard repariert.
* Tabellen-Ansicht mit einer Spalte in einigen Konfigurationen repariert.
* Window-Compat und jQuery-CUI-Compat Layer wurden entfernt.
* Powerpoint-Export von Präsentationen repariert.
* Detail / Editor: Render-Verbesserungen für kleine Listen.
* Plugin-Interface für Export-Dialog.

#### Server

* Willkommens-E-Mail kann mehrfach an Nutzer verschickt werden.
* Exporte werden auf "fehlgeschlagen" gesetzt, wenn sich der Exporter unerwartet beendet.
* ungültige Maskenkonfiguration (unterschiedliche Verschachtelungseinstellungen für das selbe Feld) wird erkannt und abgelehnt.
* Erweiterung der Plugin-API (Zugriff auf Pseudo-Session beim Export).
* Fehler beim Index-Update nach Änderung von Verschachtelungseinstellungen behoben.
* Korrekturen in der Such-API.

## Version 5.19

*Veröffentlicht am 27.09.2017*

Mit diesem Release steigt die easydb auf eine neue Version der verwendeten Elasticsearch-Software um. Der Umstieg erfolgt bei Update der Docker-Container automatisch, jedoch gibt es eine Einstellung, die auf systemadmistrativer Ebene zu ändern ist, was nicht durch aktualisierte Docker-Images machbar ist:

Der Wert für den [sysctl](https://en.wikipedia.org/wiki/Sysctl)-Schlüssel [vm.max_map_count](https://www.elastic.co/guide/en/elasticsearch/reference/current/vm-max-map-count.html) muss erhöht werden:
```
sysctl -w vm.max_map_count=262144
```
Das kann im [Start-Skript für den Elasticsearch-Container](../sysadmin/installation) oder über die Mittel der verwendeten Linux-Distribution (`sysctl.conf`) gesetzt werden.

Das Update auf die neue Elasticsearch-Version erfordert außerdem eine Neuindizierung, weshalb es bei größeren Datenbank zu einer mehrstündigen Unterbrechung des Betriebs kommen kann.

#### Webfrontend

* Umbau und Redesign von Editor, Detail, Text-Ansicht, Tabellen-Ansicht und Experten-Suche
* Auswahl einzelner Masken in der Experten-Suche
* Optionale Serien- Und Versions-Erkennung von Dateien beim manuellen Hochladen
* Verbesserungen in der Speicher-Verwaltung
* Masken-Option zum Start-Zustand von Panels (offen / zu)
* Panels können gleichzeitig geöffnet sein
* Masken-Option für verkürze Ausgabe von Mehrfach-Feldern
* Besseres Design für die Ein- und Ausgabe von Custom-Data-Types (wie z.B. Weblink und GND)
* Verwendung der NPM-Version von Coffeescript-UI
* "Alle Selektieren" in Mappen

#### Server

* Portierung auf Elasticsearch 5
* mehr Verbesserungen im E-Mail-Handling
* Suche nach User-Typ ermöglicht
* Events vom Typ OBJECT_INDEX und API_PROGRESS werden nach einer Woche gelöscht
* Zustand "expired" für aufgeräumte Exporte
* generelles "bag_read"-Recht über "system.group"-Systemrecht möglich
* Zurücksetzen der Standard-Masken auf Objekttyp-Vorgabe in /api/objecttype möglich
* Ausgabe mehrerer Objekte in /api/db möglich
* Überarbeitung der Suche
* Fehler bei paralleler Ausführung von /api/collection behoben
* Löschen von Pools aktualisiert ACLs
* /api/event/list beschleunigt
* XML-Export von mehr Typen ermöglicht (Datumsbereiche, Fixkommazahlen)

## Version 5.18

*Veröffentlicht am 06.09.2017*

Beim Update auf dieses Release muss sowohl ein neuer Datenbank-Index erstellt als auch eine Neuindizierung in Elasticsearch vorgenommen werden. Bei größeren Datenbank ist daher mit einer mehrstündigen Unterbrechung des Betriebs zu rechnen.

#### Webfrontend

* CSV Importer: Unterstützung von Mehrfach-Feldern für EAS-Spalten
* Tag & Workflows werden neu geladen, wenn das Speichern fehlschlägt
* Bugfix: Anzeigen von Mappen aus der Detail-Anzeige in manchen Fällen
* Bugfix: Esc wenn Tooltip is aktiv über einem aktiven Layer
* Bugfix: Suche nach mehreren Worten hat die Reihenfolge der Wörter vertauscht

#### Server

* E-Mail-Templates & darin verwendbare Variablen korrigiert und erweitert
* Georgische Sprache für Daten hinzugefügt (ka-GE)
* Tag-Namen im XML-Export
* Verbesserte Fehlerbehandlung, z.B. beim Löschen von Tags
* Beschleunigung u.a. des Exports bei Existenz von vielen Ereignissen

## Version 5.17

*Veröffentlicht am 23.08.2017*

#### Webfrontend

* Neue Objekte: Verbesserungen für den Uploader bei größeren Datenmengen.
* Suche: Die automatische Suche der neuen Objekte wurde überarbeitet.
* Unterstützung für [Vivaldi-Browser](https://vivaldi.com/), Testplattformen sind aber nachwievor Mozilla Firefox, Chrome + MS Edge.
* Verbessertes Fehlermanagement für CMS-Plugins.
* Verbesserungen in der Speicher-Verwaltung.

#### Server

* Deeplink: API unterstützt Versionen von Objekten (nach Versionsnummer oder Datum)
* CSV Exporter: Fehler beim Export wurden behoben
* CSV Exporter: CSV-Header wurden angepasst
* XML Exporter: Objekte werden mit Namespace Attribut `xmlns` exportiert
* XML Exporter: Feld `_standard` von verlinkten Objekten wird exportiert
* XML Exporter: URLs zu Assets werden um `disposition/inline` erweitert um Anzeige im Browser zu ermöglichen
* Fehler beim Generieren von EAS-Dateipfaden wurde behoben
* OAI PMH: Deeplink URLs erhalten beim exportieren den Parameter `auth=oai_pmh`
* Fehler beim Passwort zurücksetzen wurde behoben

## Version 5.16

*Veröffentlicht am 09.08.2017*

#### Webfrontend

* Gruppen-Manager: Anzeige der internen ID, Kopieren-Button.
* CSV-Exporter: Excel-kompatible Ausgabe für UTF-8 (BOM)
* Code Support für Term Boosting in QueryElementToken und QueryElementFulltext
* Performance: Mappen laden schneller
* Performance: Speicherbedarf der Applikation wurde optimiert
* Bugfix: Lasso bei Zoom > 100%
* Bugfix: Anzeige der Vorschauen im Datenmodell ging für einige Masken nicht

#### Server

* Byte Order Mark wird beim CSV-Export ausgegeben
* Zeit-Werte im CSV-Export werden ISO 8601-konform exportiert
* Internes Handling von ISO 8601-Zeit-Werten wurde vereinheitlicht
* Collection Post Processing in `api/search` wurde verbessert
* Fehlende Einträge in mehrsprachigen Feldern werden nicht mehr mit einer falschen Sprache überschrieben
* Deeplink `.../file_version/group/<group>` wurde gefixt
* Pool-Rechte werden alphabetisch sortiert


## Version 5.15

*Veröffentlicht am 26.07.2017*

#### Webfrontend

* ExportManager: Mit ALT-Click können Downloads angeschaut werden
* Logout führt jetzt immer wieder zur Startseite, nicht zum Login
* CSS Classes für Designbarkeit von Detail + Editor
* Unterstützung für Phrasen-Suche bei Benutzer, Gruppen, Pool und Mappen
* Verbessertes Mappen-Laden bei Datenbanken mit vielen Rechten
* Bugfix: Beim Speichern mit unsichtbaren Feldern wurden die Pflichtfelder nicht korrekt überprüft
* Bugfix: Auswahl eines Vater-Eintrages bei neuangelegten Einträgen in kleinen Popover-Editor
* Bugfix: Hochladen von XSLT-Dateien in der Konfiguration ist erlaubt, auch wenn sonst verboten

#### Server

* CSV-Export erweitert
* CSV-Ausgabe von Ereignissen erweitert
* Auswahl der Ersatzversion beim Export korrigiert
* Versionen, die nicht dem Rechtemanagement unterliegen, können jetzt heruntergeladen werden
* Metadaten-Mapping für Typo3-Plugin aktiviert
* Datei-Upload für spezielle Dateien korrigiert
* E-Mail-Vorlagen aktualisiert
* E-Mail-Adressvalidierung verbessert

## Version 5.14

*Veröffentlicht am 12.07.2017*

#### Server

* E-Mail-Adressen mit Großbuchstaben sind jetzt erlaubt
* Umstrukturierung der Rechte-Liste
* Korrekturen im Export
* Fehler beim Laden von mehreren Produce-Plugins korrigiert

#### Webfrontend

* Unterstützung für verschiedenfarbige Tags
* Datei-Versionen: Direkte Namens-Eingabe vorm Erzeugen neuer Versionen
* Suche nach "#<system-id>" im Haupt-Suchfeld
* Detail / Editor: Unterstützung von alphabetisch sortierten Mehrfach-Feldern
* Bugfixes im CSV-Importer, Metadaten-Tool, Detail, Suche, Collections


## Version 5.13

*Veröffentlicht am 28.06.2017*

Änderungen am Suchindex erfordern eine Neuindizierung. Das kann je nach Datenbankgröße zu einer mehrstündigen Einschränkung der Benutzbarkeit führen.

#### Server

* Suchindex berücksichtigt Volltext-Einstellung an verschachtelten Tabellen
* Fix für Download-Transport ohne Packer
* Erweiterung der Informationen zu Download-Transport-Dateien in der Export-API
* Korrektur der EAS-Links im Export
* Vorbereitung für Hotfolder-Import in verlinkte Tabellen
* Suche mit Akzenten korrigiert
* Verbesserung bei `exclude_fields` in der Such-API
* Optimierung bei Generierung von `ALL_FIELDS`-Links

#### Webfrontend

* Download und Export von entfernt verlinkten Dateien, die im Detail-Viewer angezeigt werden
* Eine robots.txt sorgt dafür dass Suchmaschinen nicht indizieren
* Experten-Suche: Verbesserter Tokenizer für Autocompletion in Text-Feldern
* CSVImporter: Bugfixes beim Import von verlinkten Objekten
* Weitere kleinere Bugfixes

## Version 5.12

*Veröffentlicht am 14.06.2017*

#### Webfrontend

* Unterstützung für Einzel-Feld-Rechtemanagement.
* Unterstützung für Serien-Bilder, Versionen (RAW, Jpeg) und entfernte Datensätze beim Upload.
* Verbessertes Drag & Drop in Mappen.
* Datums-Auswahl ohne Zeit möglich.
* CSV-Importer: Unterstützung von mehrsprachigen Link-Feldern bei der Suche und Erzeugung.
* Fehlerbehebung bei der Gruppierung im Filtertree.
* Bugfixes und Performance-Verbesserungen.

#### Server

* Alle-Felder-Maske referenziert für Links auch die Maske mit allen Feldern
* Feldfilter-I/O
* Update-Datum für User-Änderungen
* Hotfolder-Erweiterungen
* `OBJECT_DELETE`-Event für archivierte Nutzer
* Wildcard-Suche korrigiert, Groß-/Kleinschreibung muss nicht berücksichtigt werden
* LDAP- und SSO-Nutzer bekommen jetzt Arbeitsmappen. Um davon zu profitieren, muss der in der easydb hinterlegte Nutzer vom Typ "ldap" bzw. "sso" gelöscht werden. Dieser wird bei der nächsten Anmeldung wieder angelegt.
* Auswahl der zu exportierenden Felder für den CSV-Export korrigiert

## Version 5.11

*Veröffentlicht am 31.05.2017*


#### Webfrontend

* Objectstore zum Verwalten von Datenmodell auf einen zentralen Server
* Suche: Verbesserungen bei der Eingabe
* Editor: Tag editieren repariert
* Editor: Hochladen von Verzeichnissen in Chrome gefixt
* Editor: Verbesserungen für den Status des Speichern-Button
* CSV-Importer: Fix für Multi-Column-Datenimport

#### Server

* Einschränkung der Felder nach Maskeneinstellung (Volltext-Suche) für Phrasensuche
* Neuer API-Request `settings`
* Filter für `/api/user`
* `OBJECT_INDEX`-Events werden für Assets immer generiert, auch bei niedriger Priorität
* Bugfixes

## Version 5.10

*Veröffentlicht am 17.05.2017*

#### Webfrontend

* Hierarchie-Browser im Detail (bei hierarchischen Objekttypen).
* In der Tabellen-Ansicht lassen sich die Spaltenbreiten manuell anpassen.
* Hierarchie-Checkbox aus dem Objekttyp/Pool-Selektor entfernt.
* Hierarchie-Checkboxen in jeder Ansicht als Option ergänzt.
* Verbessertes Markieren von Pflichtfeldern, insbesondere im Gruppen- und Neu-Editor.
* CSV-Importer: Unterstützung für Dezimal-Felder, Import von MS-Access-Daten (YYYMMDD-Format).
* Bugfixes und Performance-Verbesserungen.

#### Server

* Download von großen Dateien korrigiert.
* Caching-Policy wird gemäß der Plugins berücksichtigt.
* Custom-Settings in Schema/Masken für mehr Feldtypen.
* Fehlenden Fremdschlüssel im Datenmodell angelegt.
* Links im XML-Export korrigiert.
* Import von bidirektionalen Daten mit dem Gruppeneditor korrigiert.
* Fehler bei Erstellung von Indizes mit langen Namen behoben.

## Version 5.9

*Veröffentlicht am 03.05.2017*

#### Webfrontend

* Zeitplan mit Voreinstellungen bei E-Mails und Export-Transport
* Unterstützung für optionale Trennzeichen in Feldbezeichnern.
* Drucken funktioniert jetzt auch im Internet Explorer.
* Markieren aller Treffer auch in der Nebensuche.
* CSV-Importer: Verbesserungen und Fixes.
* Plugin: Wordpress-CMS Transport (Beta).
* Plugin: Export-Transport FTP ist jetzt ein Plugin.
* Fehlerbeseitigungen und Geschwindigkeitsoptimierungen

#### Server

* Login-Namen und E-Mail-Adressen sind müssen jetzt unabhängig von der Groß-/Kleinschreibung eindeutig sein.
* Gruppenzuordnung für LDAP- und SSO-Authentifizierung hat nur noch für die Session Gültigkeit und ist nicht mehr persistent.
* Index-Fehler beim Import mit Maske "\_all\_fields" behoben.
* Parallelität beim Export entfernt, um die Zuverlässigkeit zu erhöhen.
* Minuten-Genauigkeit für Scheduler hinzugefügt.


## Version 5.8

*Veröffentlicht am 19.04.2017*

#### Webfrontend

* CSV-Importer: Unterstützung für Mehrsprachige-Felder (Hierarchie + Updates)
* Neue System-Rechte um Gruppen- und Nutzer-Manager zu verbergen, den Zugriff über die API aber weiterhin zu erlauben
* Verbesserter Dialog für Selbstregistrierung
* Datei-Download von verlinkten Datensätzen, die Dateien enthalten, die im Standard angezeigt werden (nur Einzel-Download)
* "Änderungen verwerfen?"-Dialog in Profil & Tag-Manager
* Grafische Verbesserungen
* Fehlerbehebung: Sprachauswahl bei Neustart war immer "en-GB".
* Weitere Fehlerbehebungen

#### Server

* mehr Felder im XML-Export
* neuer Parameter "hide_frontend_app" für Systemrechte "system.user" & "system.group"
* Suche & Suggest in mehr Feldern ermöglicht
* Fehler bei den Mappenrechten behoben
* Fehler bei Auswertung der Plugin-Konfiguration behoben
* DB-Fehler im Export-Scheduler behoben

## Version 5.7

*Veröffentlicht am 05.04.2017*

#### Webfrontend

* Anzeige von verlinkten Datensätzen aus dem Detail in der Suche.
* CSV-Exporter für Benutzer
* Unterstützung von Mehrsprachigkeit, Datum und ID-Spalten im CSV-Importer
* Single-Sign-On unterstützt die Authentifizierung in einem separaten Browser-Fenster.
* Bugfixes

#### Server

* User-Blocking bei mehreren Fehlversuchen auf Client-Blocking umgestellt
* Unterstützung für Custom-Typen in der Suche
* max. Länge für ngram-Suche von 30 auf 50 erhöht
* Suggest für Dateieigenschaften korrigiert
* archivierte Nutzer werden nicht über die API ausgegeben
* XML-Namensraum im Export-Metadatenmapping korrigiert
* keine persistente DB-Verbindung im Janitor mehr
* Thread-Leck im Exporter behoben
* Fehler beim Speichern von E-Mail-Adressen behoben

## Version 5.6

*Veröffentlicht am 20.03.2017*

#### Webfrontend

* Anbindung von [cloudsight.ai](https://cloudsight.ai/).
* Verbesserte Sprachauswahl beim erstmaligen Start der easydb.
* Bugfixes & Performance-Verbesserungen

#### Server

* Ausgabe von alten Datensatz-Versionen beschleunigt
* Objekt-URLs im XML-Export
* Indizierung von bidirektionalen Links verbessert
* Behandlung von Tags im Gruppeneditor ohne andere Änderungen korrigiert
* Ausgabe von Standard-EAS-Block für Datensätze ohne Assets vereinheitlicht

## Version 5.5

*Veröffentlicht am 08.03.2017*

#### Webfrontend

* CSV-Importer für Benutzer und Listen
* Performance-Verbesserungen & Bugfixes
* Support für eigene Farben in Basis-Konfiguration.
* Ein Markdown-Link öffnet jetzt in einem separaten Browser-Fenster.
* Fix für das Beibehalten der sichtbaren Reihenfolge beim Umsortieren in Collections.

#### Server

* neues Ereignis `USER_CREATED`
* LDAP-Unterstützung
* zusätzliche Spalten bei bidirektionalen Links werden kopiert
* Entfernen von Tag-Filtern an Objekttypen ermöglicht
* Fehler bei Collections-Operationen behoben
* Fehler bei Metadaten mit NULL-Bytes behoben
* Verbesserung der Geschwindigkeit bei Collection-Requests

## Version 5.4

*Veröffentlicht am 22.02.2017*

#### Webfrontend

* Umstellung auf neues Design
* Performance-Verbesserungen & Bugfixes

#### Server

Neu:

* ZIP64-Support für Exporte.
* Zeitliche Sperre von Nutzern (z.B. bei zu vielen Fehlversuchen beim Anmelden).
* Systemname ohne Anmeldung sichtbar.
* Root-Recht nicht mehr für Nicht-Root-Nutzer sichtbar.
* Event für Base-Config-Update.
* UNIQUE-Contraints für Datumsbereiche.
* Plugins können eigene Events erstellen.

Ergänzt:

* Deeplink-Erweiterungen.
* "AOContentDescription" für Export-Profil.
* Bessere Fehlermeldungen und Übersetzungen ("L10N").

Repariert:

* Export der kompletten Suche.
* Alle Berechtigungen (ACLs) entfernen.
* Passwort-Vergessen-Link.
* Das Setzen von "inaktiv" an Berechtigungen (ACLs).
* Geschwindigkeit der Behandlung von Berechtigungen (ACLs) verbessert.


## Version 5.3

*Veröffentlicht am 31.01.2017*

#### Server

* Custom Data Types: umfangreichere Unterstützung für Suche und Aggregations. Achtung: diese Änderung erfordert eine Anpassung der Konfiguration der Custom Data Type Plugins.
* Suche: /api/search arbeitet nur noch mit "aggregations", "facets" werden nicht mehr unterstützt.

## Version 5.2

*Veröffentlicht am 02.12.2016*

#### Webfrontend

* Umstellung von Mappen, Suchen und Finder.
* Selektionsparadigmen überarbeitet.
* Direkt erreichbare Flyout-Buttons als Ergänzung zum Kontextmenü.

#### Server

* OAI/PMH-Schnittstelle.
* Deep-Link-Schnittstelle.
* Erweiterung bei den Custom-Data-Types.

## Version 5.1.1

*Veröffentlicht am 10.11.2016*

Bugfix #39365: - dbapi_import: fix UPDATE: insert dirty job for deleted reverse nested objects

## Version 5.1

*Veröffentlicht am 06.11.2016*
