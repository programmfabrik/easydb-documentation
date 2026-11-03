---
menu:
  main:
    name: "5.156 (Ende September 2026)"
    identifier: "5.156"
    parent: "releases"
    weight: -656
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.156.1

Veröffentlicht am 03.11.2026

> Security-Release ohne inhaltliche Änderungen. Es wurden Software-Updates für [CVE-2026-111497](https://nvd.nist.gov/vuln/detail/cve-2026-111497) eingespielt.
* Node.js auf v22.23.4 aktualisiert.
* `libbrotli1` jetzt auf Version 1.0.9-2+deb12u1. Diese enthält die Patches für CVE-2026-111497, siehe https://security-tracker.debian.org/tracker/CVE-2026-111497.

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
docker.easydb.de/pf/eas:5.156.1            sha256:4a4ca17e87c89da19c1da42be948b9cb3d944ad9823f9dc001bc3f40304d6637
docker.easydb.de/pf/elasticsearch:5.156.1  sha256:57e6e839745ba493eae879acac808541983a7d3de2cbe3ed5abc5d0ef7ccccec
docker.easydb.de/pf/fylr:5.156.1           sha256:85f7213dd3927bb1fec53bacb634080c7d35a8be84ce9be7f26510cb80527d4b
docker.easydb.de/pf/postgresql-14:5.156.1  sha256:97194dc46fb8ee7e489812e6cb29add694dc308ba9b8cba1da6eb0ea35dd3e2d
docker.easydb.de/pf/server-base:5.156.1    sha256:633413c6ccbfc2e5dfd790470630ac6683db19f749de57ec20c493019264565a
docker.easydb.de/pf/webfrontend:5.156.1    sha256:5b46a7e4d81df9ebf391a54c50c4aec08d66930e2861e2d34296509f92c8cc38
```
