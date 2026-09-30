---
menu:
  main:
    name: "5.156 (Ende September 2026)"
    identifier: "5.156"
    parent: "releases"
    weight: -656
---

> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.156.0

Veröffentlicht am 30.09.2026

# Webfrontend

## Verbessert

* **Maskeneditor**:
	* Mehrere Felder mit Shift/Strg auswählen und gemeinsam verschieben
	* Warnung, wenn ein NOT-NULL-Feld mit der Maske nicht befüllt werden kann; sie verschwindet, sobald das Feld wieder befüllbar ist
* **Datenmodell-CSV**: Export und Upload behalten Reverse-Edit- und bidirektionale Verknüpfungs-Einstellungen. Der Upload wird nur auf einer Instanz ohne Datenmodell angeboten
* **Detail**: Aus der Detail-Seitenleiste geöffnetes Vollbild zeigt die Detailansicht sofort; das Editor-Seitenleistenmenü erhält „Editor im Vollbild öffnen"
* **Renditions & Varianten**: Der Reiter ist sofort nutzbar; Link-Prüfungen laufen im Hintergrund, je Klasse und Version statt je Datei
* **Asset-Browser**:
	* Die im Asset-Info gewählte Variante bleibt beim Ändern der Fenstergröße ausgewählt
	* Einträge technischer Metadaten-Listen im Asset-Info erhalten ihre korrekten Bezeichnungen
* **Mappen**:
	* Ein falscher PIN und ein abgelaufener Share zeigen jetzt unterschiedliche Meldungen
	* Beim Filtern öffnet eine Collection zunächst nur mit den passenden Kindern; ein Klick darauf zeigt nun alle
* **Markdown**: Darstellung auf den neuesten Renderer aktualisiert. Admin-Nachrichten behalten ihre volle Formatierung, Links öffnen weiterhin in neuem Tab. Code-Editor und Drittabhängigkeiten aktualisiert
* **Barrierefreiheit**: Ein nicht-interaktiver Fokus-Helfer wird vor Screenreadern verborgen

## Behoben

* **Manager**:
	* Beim Speichern von Pool, Objekttyp oder Nutzer gehen keine `custom_data` mehr verloren, die von Plugins, der API oder Migrationen geschrieben wurden
	* Kein Fehler-Popup mehr, wenn ein Löschen, Speichern oder Laden nach Verlassen der Seite abschließt
* **CSV-Import**: Ein per System-Objekt-ID referenziertes, nicht existierendes verlinktes Objekt markiert die Zeile mit klarer Meldung als ungültig, statt den ganzen Block scheitern zu lassen
* **Mappen**: Die Liste der Mappen wird bei jedem Öffnen des Menüs geladen, sodass zwischenzeitlich angelegte Mappen erscheinen und der Leer-Platzhalter nicht wiederholt wird
* **Datenmodell**:
	* „Commit" und „Zurücksetzen" bleiben deaktiviert, wenn es nichts zu committen gibt; „Zurücksetzen" bleibt verfügbar, solange ein Knoten ohne Änderungen ausgewählt ist
	* Das Leeren des Anzeigenamens eines verschachtelten Feldes wird gespeichert
* **Collection-Upload**: Die Upload-Einstellungen zeigen die Datei-Spalte als nicht gesetzt an, statt still die erste zu wählen; ein Upload ohne Datei-Spalte lässt sich nicht speichern
* **Geteilte Mappen**: Zeigen nur dann einen Aufklapp-Pfeil, wenn sie für den Nutzer lesbare Kinder haben. Die gilt auch auf paginierten Seiten, bei nachgeladenen Kindern und nach Neuladen
* **Dateiauswahl**:
	* Jedes Kopier-Ereignis wird an seinem eigenen Datensatz gespeichert (bisher alle am ersten). Die Datei-URL wird nicht mehr im Ereignis abgelegt
	* Der Ladefortschritt zählt Datensätze statt jeder exportierten Datei
* **Entwickler-Menü**: „OK" wirft beim Neuladen des Themes keinen Browser-Fehler mehr
* **Gruppeneditor**: Der verschachtelte Löschen-Button zeigte einen rohen Lokalisierungs-Key
* **Dialoge**: Sitzungsablauf, Benutzereinstellungen, Speichern von Präferenzen und Sprachwechsel hängen nicht mehr, wenn der Nutzer nicht gelesen oder neu geladen werden kann
* **Ergebnisansicht**: Das Umschalten der Ergebnisansicht während einer laufenden Suche führt nicht mehr zum Absturz und lässt den Suchen-Button nicht mehr endlos drehen
* **Präsentationen**: Beim Verlassen einer Präsentation, in der nichts geändert wurde, wird nicht mehr fälschlicherweise vor ungespeicherten Änderungen gewarnt
* **Gespeicherte Suchen**: Kein Absturz mehr, wenn die eigene Collection nicht in den Panels ist
* **Verlinkte Objekte**: Ein Klick auf die Datei eines verlinkten Objekts in einer Reverse- oder verschachtelten Zeile öffnet die Schnellansicht; Layout-Korrekturen für als Text dargestellte verlinkte Objekte
* **Auswahlmenü**: Keine Ausnahme mehr, wenn das Bearbeiten-Flyout öffnet
* **Feldsichtbarkeit (Tags)**: Filter-Panel und Expertensuche verbergen Felder nicht mehr wegen des Tag-Anteils einer Sichtbarkeitsregel
* **Hierarchie-Pfad**: Ein Klick, während eine Suche läuft oder fehlgeschlagen ist, führt nicht mehr zum Absturz
* **Zeitplan-Editor**: „+" bleibt deaktiviert, bis die Zeitpläne geladen sind; frühes Schließen des Dialogs wirft keinen Fehler mehr
* **Nachrichten**: „Aktiv von/bis"-Daten werden validiert, aber nur wenn der Nutzer sie ändert
* **Datumsformate**: Eigene Datumsformate der Frontend-Sprache greifen wieder; unbekannte Datenbank-Locales führen nicht mehr zum Fehler, sobald ein Datumsfeld angezeigt wurde
* **Dateivarianten**: In Builds mit aktivierten Asserts wieder erreichbar
* **Connector**: Die Konsole füllt sich nicht mehr mit „Refused to get unsafe header" bei Cross-Origin-Antworten
* **Konsolenhinweise**: „ResizeObserver loop"-Browserhinweise werden nicht mehr als Frontend-Fehler gemeldet


# Server

## Behoben

* **Plugin Callbacks**:
  * die korrekte externe EAS URL (falls gesetzt) wird an Plugins übergeben
  * Das behebt Probleme mit falschen exportierten EAS URLs, z.B. im OAI/PMH Endpunkt

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.156.0            sha256:0ed419620bbbf72de7c1ed86a48a7be6e34ea5138a7badfd81423ec124a9b500
docker.easydb.de/pf/elasticsearch:5.156.0  sha256:edeeec8b19a2043be8d1af9a54b562376b8f4ef117ea1f8ced76fe29ed472c9e
docker.easydb.de/pf/fylr:5.156.0           sha256:4d5b9ca6329c7e673592109bf1faf4b9593aafc1d018e74324757483ef440962
docker.easydb.de/pf/postgresql-14:5.156.0  sha256:81fad6654102622a079f56ad704cdc5250722c25594107fc8fdb5b3c69fb07e5
docker.easydb.de/pf/server-base:5.156.0    sha256:5df140da5a514a19f106dff6d8b5a2073b7f9db8dfe22f1dbfe12c36e9e3bfa7
docker.easydb.de/pf/webfrontend:5.156.0    sha256:d686d28e0c712e2cebefeceb04a9fef29651ea42429221f8ac14975d7f1159b2
```
