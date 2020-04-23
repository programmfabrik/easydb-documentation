---
menu:
  main:
    name: "5.66"
    identifier: "5.66"
    parent: "releases"
    weight: -566
---

> Für dieses Release ist ein Re-Index nötig, bitte planen Sie entsprechende Zeit für das Einspielen des Updates ein. 

# Version 5.66.0

*Veröffentlicht am 22.04.2020*

### Server

*Neu & Verbessert*

* /api/group: Gruppen haben einen IPv4 Filter für Subnetze. Damit lassen sich Gruppenzuordnungen auf bestimmte IP Adressbereiche filtern. 

* /api/xmlmapping: Feldnamen werden auf Gültigkeit überprüft.

*Behoben*

* Probleme beim reindex/purge für Multi-Instanz Elastics-Installationen wurden beseitigt. 
* /api/search: Sortierung für flache Hierarchien wurde behoben.
* /api/db: `_path`in alten Versionen wird jetzt korrekt ausgegeben.
* /api/export: `easydb_flat`Format wurde für einige Fälle mit Reverse-Nested repariert.

### Webfrontend

*Neu & Verbessert*

* Mitteilungen: Der Mitteilungstyp `Download`erlaubt nun ein hinzufügen eines Formulars in dem eine maximale Anzahl von ausgewählten Checkboxen angegeben werden kann.

* Maskenmanagement: Verbesserte Unterstützung für Sortierung von Mehrfachfeldern.
* CSV-Importer: Bessere Organisation der Optionen für verlinkte Objekte und andere kleinere Verbesserungen und Fehlerbehebungen.
* Maskenmanagement: Bei der Anzeige von Demo-Daten können größere Objekte nun geladen werden, anstatt angezeigt.
* Basis-Konfiguration: Bei größeren Eingabeformularen wird nun ein `+`-Button benutzt um weitere Einträge hinzuzufügen. 
* Connector: Sicherheitsverbesserungen bei der Passwortverwaltung.

*Behoben*

* Die **Hochladen**-Einstellungen für Mappen  haben in einigen Fällen Felder aus Reverse-Nested angezeigt, ohne diese zu unterstützen. Die Anzeige des Pools in diesem Dialog wurde ebenfalls korrigiert.
* Multi-Instanz-Support für easydb 6 beim Schließen der Sidebar verbessert.
* Filtertree: Sprachabhängige Ausgabe von Daten v. Chr. wurde korrigiert.
* Neue Objekte: Die Anzeige der Pools konnte in einigen Fällen durcheinander kommen.