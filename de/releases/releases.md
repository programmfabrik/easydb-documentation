# Releases

easydb wird in regelmäßigen Abständen um neue Funktionen erweitert, von Fehlern befreit und ständig verbessert.

* Der Zyklus für die Entwicklung von Versionen in easydb beträgt zwei Wochen. Hierdurch stehen Kunden regelmäßig Aktualisierungen zur Verfügung. Die neuste Version wird bereitgestellt, sobald sie für die Verwendung durch den Kunden geeignet ist.
* Mängelbehebungen und Störungsbeseitigungen können zusätzliche Versionen erzeugen (auch "Patch" genannt).

### Aktualisieren

Das Aktualisieren entspricht den ersten Schritten der [Installation](/sysadmin/installation/installation.md). Falls nicht anders vereinbart, liegt diese Aufgabe beim Kunden.

easydb-Instanzen auf unseren eigenen Servern, unter anderem für Tests und Präsentationen, werden durch uns aktualisiert.

# Versionen

## Version 5.18

*Veröffentlicht am 06.09.2017*

Beim Update auf dieses Release muss sowohl ein neuer Datenbank-Index erstellt als auch eine Neuindizierung in Elasticsearch vorgenommen werden. Bei größeren Datenbank ist daher mit einer mehrstündigen Unterbrechung des Betriebs zu rechnen.

#### Webfrontend

* CSV Importer: Unterstützung von Mehrfach-Feldern für EAS-Spalten
* Tag & Workflows werden neu geladen, wenn das Speichern fehlschlägt
* Bugfix: Anzeigen von Collections aus der Detail-Anzeige in manchen Fällen
* Bugfix: Esc wenn Tooltip is aktiv über einem aktiven Layer
* Bugfix: Suche nach mehreren Worten hat die Reihenfolge der Wörter vertauscht

#### Server

* E-Mail-Templates & darin verwendbare Variablen korrigiert und erweitert
* georgische Sprache für Daten hinzugefügt (ka-GE)
* Tag-Namen im XML-Export
* verbesserte Fehlerbehandlung, z.B. beim Löschen von Tags
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

* [Objektstore](https://github.com/programmfabrik/easydb-objectstore) zum Verwalten von Datenmodel auf einen zentralen Server
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

* Anbindung von [cloudsight.com](http://cloudsight.com).
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


# Support

Mängel beheben wir je nach Mängelklasse im folgenden Zeitrahmen (sofern vom Kunden gebucht und nicht anders vereinbart):

|Mängelklasse|Reaktionszeit|Wiederherstellungszeit|
|-|-|-|
|Betriebsverhindernder Mangel|2 Stunden|24 Stunden = 3 Werktage|
|Betriebsbehindernder Mangel|2 Stunden|40 Stunden = 5 Werktage = 1 Woche|
|Leichter Mangel|2 Stunden|80 Stunden = 10 Werktage = 2 Wochen|

Für diese Aufstellung zählen nur Stunden innerhalb unserer Servicezeiten: werktags 9 Uhr bis 17 Uhr.

Mängel können je nach Situation auch in einer lokalen Umgehungslösungen behoben werden statt in einer neuen Version bzw. bis zu einer neuen Version.
