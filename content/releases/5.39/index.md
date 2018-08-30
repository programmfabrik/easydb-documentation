---
menu:
  main:
    name: "5.39"
    identifier: "5.39"
    parent: "releases"
    weight: -539
---

# Version 5.39.0

*Veröffentlicht am 30.08.2018*

> Die Release Notes sind noch nicht vollständig!

#### Bitte Beachten:

1. Dieses Release hat einen Re-Index zur Folge, entsprechende Update-Zeit sollte eingeplant werden.
2. Bitte überprüfen Sie Ihre Metadaten-Mappings und passen sie diese ggf. an um Fehlverhalten vorzubeugen. In vereinzelten Fällen muss das Mapping neu angelegt werden, um alle Werte korrekt zu übernehmen.

### Server

* Neue Implementierung für **/api/suggest**: Bisher wurden Aggregationen verwendet, um Vorschläge für die Suche zu finden. Dieses Verfahren war für große Indexe zu langsam und brauchte zuviel Speicher. Im neuen Verfahren wird zu festen Zeiten parallel ein Suggest-Index aufgebaut in dem dann Wortvorschläge gesucht werden. Standardmäßig wird ein solcher Index alle 2 Stunden im Hintergrund aufgebaut. 

### Webfrontend

*Neu*

- Custom Data Type: Neue Methode **isPluginSupported** die angibt, ob ein Plugin im Detail-View für diesen Type geladen werden soll oder nicht.
- Neue Maskenoption: **Maske in Detail-Ansicht ausblenden**.
- Neue Maskenoption: Anzeige von **Tags** von verlinkten Objekten.
- Custom Data Type: Wenn ein Custom Data Type nicht geladen wurde, wird in der Detail-Ansicht ein JSON-Browser ausgegeben, um die gespeicherten Daten anzuzeigen.
- Textfelder: Wenn ein Textfeld valides JSON enthält, wird ein JSON-Browser ausgegeben, um die Daten anzuzeigen.
- Neues Systemrecht **script_runner**. Damit lässt sich der ScriptRunner für Nutzer explizit erlauben, bisher war das nur sichtbar für Nutzer mit dem **root** Systemrecht.
- Connector: Unterstützung für Download über Connector (Beta).
- Connector: Verbesserte Konfiguration für Connector (Beta).
- Developer-Menu: Unterstützung einer *Remote-URL* zum laden von Plugins von einem fremden Server.
- Datumspicker: Anzeige von Wochennummern und -tagen.

*Verbessert*

* Große Mappenbäume (>100 Mappen) werden jetzt in Gruppen à 50 angezeigt um die Ladezeiten zu verbessern und mehr Übersicht herzustellen.
* JSONImporter: *eas_type* und *eas_replace_url* können im Manifest.json festgelegt werden.
* Anzeige des Suchergebnisses bei fehlenden Vorschauen wurde beschleunigt.
* Datamodel: Anzeige der aktuellen *HEAD* Version nach Speichern im Tooltip.
* Metadaten-Mappings: Neue Profile mit verbesserten Mappings.

*Behoben*

* Maskenvorschau im Maskeneditor für Email-Felder repariert.
* Tagfiltervorschau in vielen Eingabemasken repariert.
* Performance-Probleme beim Start von Datenbanken mit vielen Datumsfelder im Filter behoben.

