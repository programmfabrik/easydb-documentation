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

### Webfrontend

*Neu & Verbessert*

* **Mitteilungen**: Der Mitteilungstyp `Download` erlaubt nun ein Hinzufügen eines Formulars in dem eine maximale Anzahl von ausgewählten Checkboxen angegeben werden kann.

* **Maskenmanagement**: Verbesserte Unterstützung für die Sortierung von Mehrfachfeldern.
* **CSV-Importer**: Bessere Organisation der Optionen für verlinkte Objekte und andere kleinere Verbesserungen und Fehlerbehebungen.
* **Maskenmanagement**: Im Datenmodell können Demo-Daten nun heruntergeladen, statt nur angezeigt werden.
* **Basis-Konfiguration**: Bei größeren Eingabeformularen wird nun ein `+`-Button benutzt um weitere Einträge hinzuzufügen. 
* **Connector**: Sicherheitsverbesserungen bei der Passwortverwaltung.

*Behoben*

* Die **Hochladen-Einstellungen** für Mappen  haben in einigen Fällen Felder aus Reverse-Nested angezeigt, ohne diese zu unterstützen. Die Anzeige des Pools in diesem Dialog wurde ebenfalls korrigiert.
* **Multi-Instanz-Support** beim Schließen der Sidebar verbessert.
* **Filtertree**: Sprachabhängige Ausgabe von Daten v. Chr. wurde korrigiert.
* **Neue Objekte**: Die Anzeige der Pools konnte in einigen Fällen durcheinander kommen.

### Server

*Neu & Verbessert*

* **/api/group**: Gruppen haben einen IPv4-Filter für Subnetze. Damit lassen sich Gruppenzuordnungen auf bestimmte IP-Adressbereiche filtern. 

* **/api/xmlmapping**: Feldnamen werden auf Gültigkeit überprüft.

*Behoben*

* Probleme beim **reindex/purge** für Multi-Instanz Elastics-Installationen wurden beseitigt. 
* **/api/search**: Sortierung für flache Hierarchien wurde behoben.
* **/api/db**: `_path` in alten Versionen wird jetzt korrekt ausgegeben.
* **/api/export**: `easydb_flat` Format wurde für einige Fälle mit Reverse-Nested repariert.

* 

# Prüfsummen

* Hier die Prüfsummen unserer Docker-Images (neueste Version)

```ini
docker.easydb.de/pf/chrome               sha256:5b01af4f17676ee4295fa3cc279d15f7b6e4a43f9faad41dace54fe1b36861fd
docker.easydb.de/pf/eas                  sha256:b2fabc3363625c814493745e35a4f0c5c2de5b93eb5c262743f2227ebc6f6b6e
docker.easydb.de/pf/elasticsearch        sha256:1475d92455542b0102cf0ddc6110b17cc452cc986556857dbcf0ab79e888224f
docker.easydb.de/pf/fylr                 sha256:2fd1ab38a06a2f365984653da1546f56d6cf988602b640266cea91a4129c86b1
docker.easydb.de/pf/postgresql-11        sha256:86172297d81a82a0b303137ed5857783c6419b14358587cef05eb794da627154
docker.easydb.de/pf/postgresql           sha256:3374be1a129f4e751fce7b1ddcd561cd209a197faf9faabba5d0454d16946420
docker.easydb.de/pf/server-base          sha256:17b8ba143ef6781417c34506522a617b1d83c0e1391960ad65bb34d5667dcc2c
docker.easydb.de/pf/webfrontend          sha256:b1a0d1ffebd574cebd515803d83a59d8af7a17be4c47a16651401a38e454a70a
```

