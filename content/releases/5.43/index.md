---
menu:
  main:
    name: "5.43"
    identifier: "5.43"
    parent: "releases"
    weight: -543
---

> * Das **CSS-Developer-Plugin** wurde entfernt und damit entfällt serverseitiges Erzeugen des CSS. Es werden für Farbumstellungen jetzt CSS-Variablen verwendet, die nur in den aktuellen Browsern funktionieren. Die Möglichkeit externes CSS zu laden, besteht weiterhin mit dem [Remote-Plugin](https://github.com/programmfabrik/easydb-remote-plugin), welches standardmäßig in der easydb aktiviert ist. Farbeinstellungen müssen neu eingestellt und gespeichert werden.
> * **CustomMaskSplitter**: Diese neue Plugin-API erlaubt das Erstellen von Plugins, die im Datenmodell-Manager in den Masken eine Unterteilung der Formulare vornehmen. Beispiele für vorhandene Splitter sind: Reiter, Panels, horizontale Teiler und Blöcke
> * Beta: Die neue **/api/publish** wird in diesem Release freigeschaltet.
> * Beta: Workflow-Webhooks, die in der Basis-Konfiguration eingestellt werden können.

# Version 5.43.4

*Veröffentlicht am 05.12.2018*

### Server

*Behoben*

* `_id:lookup`für verlinkte Objekte im Gruppenmodus wurde repariert.

# Version 5.43.3

*Veröffentlicht am 29.11.2018*

### Webfrontend

*Behoben*

* Das Anmelden mit Login-Namen oder Passwörtern mit Sonderzeichen (z.B. ä, ö, Ü) wurde repariert.

# Version 5.43.2

*Veröffentlicht am 28.11.2018*

### Webfrontend

*Behoben*

* Das Laden aller Plugins wird jetzt wieder im UTF-8 Zeichensatz gemacht. Dadurch sollten Sonderzeichen wieder korrekt dargestellt werden.
* JavaScript-Error im Export-Menü bei der Auswahl von alternativen Masken behoben.
* Anzeige für einen Nutzer mit **system.root** zeigt jetzt auf jeden Fall auch die Suche, auch wenn im System allgemein **Nur Mappen anzeigen** konfiguriert ist.

# Version 5.43.1

*Veröffentlicht am 21.11.2018*

### Webfrontend

*Behoben*

* Datenmodell: Neue Maskentrenner konnten nicht hinzugefügt werden.
* Connector: Download von lokalen und entfernten Dateien wurde repariert.
* Custom-Data-Type-Link: Die Überprüfung der URL wurde repariert.
* 

# Version 5.43.0

*Veröffentlicht am 21.11.2018*

### Webfrontend

*Neu*

* Gruppeneditor: Der Nutzer hat die Möglichkeit eine Stapelgröße zu bestimmen, dadurch können für aufwendige Aktualisierungen Server-Timeouts vermieden werden.
* Favicon: Es kann in der Basis-Konfiguration ein Favicon hochgeladen werden.
* Suche: Die Tabellenanzeige erlaubt ein seitenweises Durchblättern von massenhaften Mehrfachfeldern je Objekt.
* Benutzerverwaltung: Eine E-Mail-Bestätigungsanforderung die ein Einloggen verhindert weil der Nutzer die Email nicht bestätigt hat, kann vom Administrator zurückgezogen werden.
* Automatische Vervollständigung: Die Wortvorschläge berücksichtigen jetzt die aktuell aktivierten Pools des Nutzers.

*Verbessert*

* CSV-Importer: Warnung beim Import von fehlerhafen JSON für Custom-Data-Types
* CSV-Importer: Verbesserte Darstellung von Dateifeldeinstellungen
* JSON-Importer: Verbesserungem in der Protokoll-Datei
* Editor: Verbesserungen in der Vorschau von hochgeladenen Dateien die noch nicht fertig berechnet sind
* Nutzer/Gruppen-Suche: Die Gruppierung nach Typ wurde aufgehoben, es wird nur noch nach Gruppe und Nutzer sortiert.
* Connector: Verbesserungen beim Gruppieren des Suchergebnisses nach Pool.
* CSS-Developer-Plugin wurde entfernt, Plugins müssen ihr CSS jetzt selber laden.
* Wenn beim Start der Applikation länger als 15 Sekunden gewartet werden muss wird der Nutzer informiert, dass der Server gerade zu beschäftigt ist, um Anfragen zu beantworten (z.B. weil ein Update mit nachfolgender Neuindizierung läuft).
* Expertensuche: Die Aufbereitung und der alphabetischen Listen wurde übersichtlicher gestaltet und fasst keine Felder mehr zusammen.
* Detail: Grafische Markierung von Dateifeldern für die mehrere Versionen hinterlegt sind.
* Der Maskentrenner **Horizontaler Teiler** wird jetzt immer ausgegeben, auch wenn bis zum nächsten Teiler keine Felder ausgefüllt sind. Benutzen 

*Behoben*

* Download: Bei aktiviertem Connector war kein Download möglich.
* Expertensuche: Die Suche nach unbekannten Dateien ohne Endung wurde repariert.
* Datenmodell: In Modellen mit mehrfachen Reverse-Nested-Objekttypen wurde in der Anzeige ein gemeinsamer lokalisierte Bezeichnung verwendet.
* Mappen: Ein Ladefehler wurde korrigiert der zu falschen Breiten der Vorschauanzeige führen konnte.
* Export: Die Maskenauswahl beim Export von einzelnen Objekten wurde repariert.

### Server & Plugins

*Neu*

* `publish`-API (Beta)
* Webhook-Aktion in Workflows (Beta)

*Verbessert*

* Array-Unterstützung für `_lookup:id`
* Verbesserte Fehlermeldungen
* `_path.standard` durchsuchbar
* Pool-Filter für `suggest`-API
* Basisobjekt-Listen auf maximal 1000 Ergebnisse beschränkt
* Event-Filter-Möglichkeiten erweitert
* Server-Plugin erweitert, mehr Diagnoseinformationen und Konfiguration hinzugefügt

*Behoben*

* Suche: `_sort` korrigiert
* Suggest-Index-Erstellung bei Verwendung des speziellen Objekttypnamens "user" korrigiert
* Rechtemanagement für verschachtelte Pools korrigiert
* Umwandlung von L10n- und Text-Feldern korrigiert (beide Richtungen)
* Entfernen von Einträgen mit dem Gruppeneditor bei bestimmten Inhalten korrigiert
* Transaktion wird abgebrochen, wenn Server mit HTTP 202 antwortet
* möglicher Fehler beim Speichern der Masken wird erkannt und abgewiesen
* Einbetten verlinkter Objekte beim XML-Export mit dem Format "flach" deaktiviert, da nicht implementiert
* Fehler beim Ändern der primären E-Mail behoben
* Fehlende Neuindizierung beim Ändern verlinkter Objekte behoben
* Suggest-Vorschläge enthalten keine Formatierung mehr
