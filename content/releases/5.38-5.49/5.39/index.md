---
menu:
  main:
    name: "5.39"
    identifier: "5.39"
    parent: "releases549"
    weight: -539
---

# Version 5.39.2

*Veröffentlicht am 11.09.2018*

### Server

*Behoben*

* **/api/suggest** sendet beim Index-Bau kleinere Pakete an die Elasticsearch und vermeidet damit einen bisher unsichtbaren Fehler der bei komplexeren Datenmodellen dazu führen konnte, dass der Index nicht verfügbar ist und somit keine Vorschläge zur Verfügung standen.

### Webfrontend

*Behoben*

* Der **Pool-Manager** ignoriert Objekttypen denen kein Pool mehr zugeordnet ist korrekt und erlaubt das Speichern der Einstellungen.

*Neu*

* Das Custom Data Type Plugin **gazetteer**(Beta) ist jetzt standardmässig verfügbar. Mehr Informationen unter [iDAI.gazetteer](https://gazetteer.dainst.org/app/#!/home).

# Version 5.39.1

*Veröffentlicht am 05.09.2018*

### Server

*Behoben*

* **/api/suggest** korrigiert einige Fehler Zusamenhang mit **fields**-Parameter
* **/api/search** sucht jetzt korrekt für Nutzer, die keine eigene Suchsprache eingestellt haben
* Compiler Fix für ältere GCC Versionen

*Verbessert*

* **/api/eas/rput** gibt einen Fehlercode zurück, wenn die entfernte Datei nicht gefunden wird

### Webfrontend

*Behoben*

* Anzeige von Vorschlägen in der Expertensuche für einige Fälle korrigiert
* Anzeige von Vorschlägen wurde grafisch korrigiert und verbessert
* Suche nach **#SystemObjectId** wird wieder korrekt unterstützt
* Anzeige von hochgeladenen Datei-Vorschauen aktualisiert sich wieder sobald die Vorschau verfügbar ist

# Version 5.39.0

*Veröffentlicht am 30.08.2018*

#### Bitte Beachten:

1. Dieses Release hat einen Re-Index zur Folge, entsprechende Update-Zeit sollte eingeplant werden.
2. Bitte überprüfen Sie Ihre Metadaten-Mappings und passen sie diese ggf. an um Fehlverhalten vorzubeugen. In vereinzelten Fällen muss das Mapping neu angelegt werden, um alle Werte korrekt zu übernehmen.

### Server

* Neue Implementierung für **/api/suggest**: Bisher wurden Aggregationen verwendet, um Vorschläge für die Suche zu finden. Dieses Verfahren war für große Indexe zu langsam und brauchte zuviel Speicher. Im neuen Verfahren wird zu festen Zeiten parallel ein Suggest-Index aufgebaut in dem dann Wortvorschläge gesucht werden. Standardmäßig wird ein solcher Index alle 2 Stunden im Hintergrund aufgebaut
* **/api/search** repariert, um nach selbst-verlinkten Objekten zu suchen
* CSV-Export für Custom-Data-Types repariert
* **/api/mask**: Neue Maskeneinstellung **used_for_linked_object_display**
* CSV-Export von vielen Ereignissen repariert
* Fehler beim Speichern von Objektrechten behoben
* Fehler bei Sonderzeichen in Facet-Terms behoben

### Webfrontend

*Neu*

- Custom Data Type: Neue Methode **isPluginSupported** die angibt, ob ein Plugin im Detail-View für diesen Type geladen werden soll oder nicht
- Neue Maskenoption: **Maske in Detail-Ansicht ausblenden**
- Neue Maskenoption: Anzeige von **Tags** von verlinkten Objekten
- Custom Data Type: Wenn ein Custom Data Type nicht geladen wurde, wird in der Detail-Ansicht ein JSON-Browser ausgegeben, um die gespeicherten Daten anzuzeigen
- Textfelder: Wenn ein Textfeld valides JSON enthält, wird ein JSON-Browser ausgegeben, um die Daten anzuzeigen
- Neues Systemrecht **script_runner**. Damit lässt sich der ScriptRunner für Nutzer explizit erlauben, bisher war das nur sichtbar für Nutzer mit dem **root** Systemrecht
- Connector: Unterstützung für Download über Connector (Beta)
- Connector: Verbesserte Konfiguration für Connector (Beta)
- Developer-Menu: Unterstützung einer *Remote-URL* zum laden von Plugins von einem fremden Server
- Datumspicker: Anzeige von Wochennummern und -tagen

*Verbessert*

* Große Mappenbäume (>100 Mappen) werden jetzt in Gruppen à 50 angezeigt um die Ladezeiten zu verbessern und mehr Übersicht herzustellen
* JSONImporter: *eas_type* und *eas_replace_url* können im Manifest.json festgelegt werden
* Anzeige des Suchergebnisses bei fehlenden Vorschauen wurde beschleunigt
* Datamodel: Anzeige der aktuellen *HEAD* Version nach Speichern im Tooltip
* Metadaten-Mappings: Neue Profile mit verbesserten Mappings

*Behoben*

* Maskenvorschau im Maskeneditor für Email-Felder repariert
* Tagfiltervorschau in vielen Eingabemasken repariert
* Performance-Probleme beim Start von Datenbanken mit vielen Datumsfelder im Filter behoben

