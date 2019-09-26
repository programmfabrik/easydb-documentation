---
menu:
  main:
    name: "5.47"
    identifier: "5.47"
    parent: "releases550"
    weight: -547
---

> - Die Versionen ab **5.47.0** erfordert eine Neuindizierung, planen Sie entsprechende Zeit für das Update ein.
> - Performance-Optimierungen bei der Auswahl, Detail und Editor. Hier wurde der **Bearbeiten**-Button in das Drei-Punkte-Menü verschoben.
> - Der Aufruf von **fylr** wurde geändert. Bitte schauen Sie **fylr —help** für mehr Informationen.

# Version 5.47.3

*Veröffentlicht am 06.03.2019*

### Webfrontend

*Verbessert*

* **Präsentationen**: Es ist jetzt möglich Folien von einer Seite auf eine andere zu verschieben (Kontextmenü). Neue Folien werden vor der aktuell ausgewählten Folie eingefügt.

*Behoben*

* Editor: Das **Kopieren von Objekten** wurde repariert. Dies ist durch die Performance-Verbesserungen in 5.47.0 kaputt gegangen.
* Suche: Die Experten-Suche nach **fehlgeschlagenen Versionen** (Vorschauen) hat nicht in allen Fällen korrekt funktioniert.
* Datenmodell: Das Löschen von Zeilen im Nur-Lesen-Modus wurde unterbunden (Speichern war aber nicht möglich).
* Exporter: In einigen komplexen Suchen konnte das Exportmenü nicht geöffnet werden.

### Server

*Behoben*

* Das Anmelden per **Single-Sign-On** (zum Beispiel mit Shibboleth) hat den Nutzer nicht aus der Gruppe der anonymen Nutzer genommen, wenn der Nutzer zuvor durch eine automatische oder manuelle anonyme Anmeldung in dieser Gruppe war.

# Version 5.47.2

*Veröffentlicht am 04.03.2019*

### Webfrontend

*Verbessert*

* **Alle selektieren** wird jetzt bei Suchergebnissen mit mehr als **1000** Treffern deaktiviert.
* Drucken unter Chrome wurde für einige Fälle verbessert.

*Behoben*

* **Kopieren** aus dem Editor wurde repariert.
* **Zurücksetzen** in modalen Suchen wurde repariert.
* Export mit mehr als **1000** Treffern wurde repariert.
* Umschalten von Masken im Export wurde verbessert, so dass jetzt nicht mehr doppelt geladen werden muss.
* Die Suche nach Dateitypen in der Expertensuche wurde wiederhergestellt.

# Version 5.47.1

*Veröffentlicht am 28.02.2019*

### Webfrontend

*Behoben*

* Aufruf des Gruppeneditors im Kontextmenü war nach den Performanceverbesserungen in einigen Fällen kaputt gegangen.

# Version 5.47.0

*Veröffentlicht am 27.02.2019*

### Webfrontend

*Neu*

* Suche: Sortieren nach Originaldateiname wurde ergänzt.
* Serien & Versionserkennung auch in Mappen & Hotfolder.
* Schnellanzeige: Die Anzeige im Detail für Objekte ist jetzt über das Kontextmenü möglich.
* Plugins: Ein **AssetDetailPlugin** kann jetzt automatisch starten.
* Connector: Unterstützung von Sortierungen.
* Neue Option bei Option, verlinkte Datensätze beim Deeplink einzubetten.
* Neue Basis-Konfiguration um personenbezogene Daten in einigen Events nicht zu speichern.

*Verbessert*

* Performanceverbesserungen bei der Auswahl, Anzeige im Detail und Laden im Editor für Objekte. Wir mussten dafür den **Bearbeiten**-Button im Detail entfernen. Dieser verbirgt sich jetzt im Drei-Punkte-Menü. Es werden jetzt erst beim Klick auf dieses Menü und auch erst beim Klick auf das Kontextmenü die nötigen Rechtechecks durchgeführt.
* Zoomer: Anzeige der aktuellen Zoomstufe in Prozent.
* Drucken: Mehr Einstellmöglichkeiten im Druckmenü. 
* Mappen werden jetzt im Baum aufgeklappt wenn sie anzeigt werden.
* Verbesserter Tastatursupport für Menüs und andere Auswahlen.
* Performance beim Aufbau von Präsentationen wurde verbessert.

*Behoben*

* Poolmanager: Das Entfernen des Kontaktes wurde repariert.
* Vollbildanzeige: Das Springen zur richtigen Vorschau wurde repariert.
* Suche nach Vorschaustatus wurde für einige Kombinationen repariert.
* Suche: Die Eingabe von Leerzeichen nach Anführungszeichen führt nicht mehr zu einem Fehler.
* Detail/Editor: Die Auswahl der Maske zum Anzeigen von verlinkten Objekten war in einigen Fällen, inbesondere bei neu angelegten Objekten nicht korrekt.
* Bei der Auswahl von Objekten wird das Detail jetzt  wieder nur noch dann aktualisiert, wenn aktuell nur ein Objekt in der Auswahl ist.
* Connector: Verschiedene Suchen wurde repariert.

### Server

*Neu*

* Neue Basis-Konfiguration um personenbezogene Daten in einigen Events nicht zu speichern.
* Neue Option bei Option, verlinkte Datensätze beim Deeplink einzubetten.
* `_created`-Metadatenfeld in Objekten.

*Verbessert*

* Ausgabe von `_system_object_id` für reverse-verknüpfte Objekte im XML-Export
* Nicht konfigurierte Sprachen werden nicht mehr im Export ausgegeben.
* Blacklist für Tabellennamen im Datenmodell, um Index-Problemen vorzubeugen.
* Serienbildunterstützung im Hotfolder analog zum Webfrontend.
* Überprüfung von Custom-Typ-Daten beim Speichern entsprechend Mapping.

*Behoben*

* Speichern im Gruppenmodus benutzt jetzt die Datenbanklogik um UNIQUE zu checken.

* Systemrecht `system.datamodel` mit Stufe `commit` erlaubt auch Stufe `development`.
* Bestätigungsprozess beim Löschen verlinkter Objekte korrigiert.
* Download-Dateinamen wurde in einigen Fällen korrigiert.
* Das Feld `position` in Basiskonfigurationsbeschreibung wird erzwungen. Das hat
  Auswirkungen auf Plugins, die die Konfiguration erweitern.
* ID & Standard-Info für verlinkte Assets immer im XML-Export.

### Fylr

*Neu*

* GZIP Unterstützung for **/objectstore**.
* **fylr apitest** ist jetzt ein [**eigenständiges Tool**](https://github.com/programmfabrik/fylr-apitest/) unter Open-Source-Lizenz.
* TLS/SSL Unterstützung. 

Verbessert

* **/zip** arbeitet jetzt schneller (parallel) beim überprüfen ob alle URLs erreichbar sind.

*Behoben*

* Ein Cache-Header Problem in Zusammenhang mit ETag wurde behoben.



