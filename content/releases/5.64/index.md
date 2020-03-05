---
menu:
  main:
    name: "5.64"
    identifier: "5.64"
    parent: "releases"
    weight: -564
---

> Diese Version bringt eine Änderung des Verhaltens bei **Workflows** mit (siehe unten).
>
> Es gibt keinen Re-Index so dass ein Update nur einen Server-Neustart erfordert.

# Version 5.64

*Veröffentlicht am 04.03.2020*

### Webfrontend

*Neu*

* Checkbox zum Ein- und Ausschalten von allen **Resourcen** direkt in der Suche.
* **Editor**: Eine Nutzereinstellung erlaubt das einzelne Ein- und Ausschalten von Sprachen in mehrsprachigen Eingabefeldern.
* **Massenhaftes Löschen** benötigt das neue Systemrecht `editor_bulk_delete`.
* **Maskenoption**: Mehrfachfelder können bei der Anzeige nach Pool sortiert werden.
* **Maskenoption**: Mehrfachfelder mit Booleans können die Sortierung von Vorschaubildern im Asset-Browser beinflussen.
* Maskenoption: Ausbleden von Masken im Druckmenü ist mit dieser Option möglich.
* **Aktualisierungen per Upload** in Collections (aktuell nur im *Debug*-Modus sichtbar, *Beta*)

* **Workflows**: Ein Kopieren von Zeilen ist jetzt möglich.
* **CSV-Importer**: Der Import von hierarchischen Objekten wurde erweitert, so dass jetzt das Elternelement gesetzt werden kann.

*Behoben*

* Die Integration mit **cloudsight.ai** wurde repariert. 
* Erstellen von neuen **verlinkten Objekten** direkt im Editor wurde für besondere Maskenrechts-Einstellungen repariert.

### Server

*Neu*

* Custom-Data-Type-Updater bekommt jetzt die komplette System-Konfigaration in der `start_update`Aktion übermittelt.
* **/api/mask**: Neue Option `hide_in_print_dialog`. 
* **Export**: Der Transport **FTP** untertstützt nun ein Ablegen als **ZIP-Datei** auf dem FTP-Server.
* **/api/user**: Unterstützung von `custom_data`.
* Neues **Systemrecht**: ` frontend_features.editor_bulk_delete`.

*Verbessert*

* Beschleunigung vom **Löschen** von Datensätzen mit vielen Dateien.
* **Workflows**: Für Tagfilter werden bei Objekten eines Objekttyps der keine Tags aktiviert hat, eine leere Tag-Liste angenommen. Zuvor wurden die Tagfilter für den entpsrechenden Workflow ignoriert.
* **XML-Export**: `_path`bei verlinkten Objekten wird jetzt exportiert. Zudem werden `_standard.2.text`und `_standard.3.text`jetzt auch exportiert.
* **/api/db**, **/api/search**: Format `standard`beinhaltet jetzt den Pool bei verlinkten Objekten.

*Behoben*

* **Janitor**: Konfiguration wurde unter Umständen nicht korrekt geladen, was dazu führte dass der Janitor zu oft gestartet wurde und das System unnötig belastet hat.
* **LDAP**: Bei Anmeldungen konnte es zu Problemen kommen wenn der Benutzer zuvor als easydb-Benutzer angemeldet war und gelöscht wurde.

* Die **Sortierung** nach den Blatteinträgen bei hierarchischen verlinkten Objekten wurde für die meisten Fälle repariert.