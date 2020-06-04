---
menu:
  main:
    name: "5.66"
    identifier: "5.66"
    parent: "releases"
    weight: -566
---

> Für dieses Release ist ein Re-Index nötig, bitte planen Sie entsprechende Zeit für das Einspielen des Updates ein. 

> **5.66.0** - **5.66.2** haben Probleme mit Connector-Verbindungen über SSL (besonders bei Certificates vom DFN), bitte aktualisieren Sie auf **5.66.3**.

# Version 5.66.3

*Veröffentlicht am 06.05.2020*

### Webfrontend

*Behoben*

* **Connector**: Bei Verbindungen über SSO oder Neu-Authentifizierungen (erst anonym, dann mit Login), wurden die verfügbaren Verbindungen nicht aktualisiert.

### Server

*Verbessert*

* **Connector**: Eine neue Option in der Basis-Konfiguration erlaubt das Deaktivieren der Zertifkatsprüfungen für Verbindungen. 

*Behoben*

* **Connector**: CA-Zertifikate für DFN und Let's Encrypt für Connector-Verbindungen aufgenommen.
* **Connector**: Das Verbinden mit easydbs die Passwörter mit Sonderzeichen verwenden wurde behoben. 
* **Mailer**: Verbesserte Fehlerbehandlung.

# Version 5.66.2

*Veröffentlicht am 28.04.2020*

### Webfrontend

*Behoben*

* Editor: In einigen Fällen mit Mehrfachfeldern wurde der **Editor** nicht angezeigt. Das Problem zeigte sich auch im **CSV-Importer**.

# Version 5.66.1

*Veröffentlicht am 24.04.2020*

### Webfrontend

*Neu*

* **Gruppenmanager**: Eingabemöglichkeit für den neuen **IPv4 Filter**.

*Behoben*

* Bei aktiviertem Connector-Plugin gab es einen Fehler beim **Nutzer abmelden**.

### Server

*Behoben*

* **Startprobleme** bei aktiviertem **Connector-Plugin** wurden repariert.
* **Startprobleme** in einigen Datenbanken beim **Easydb-Asset-Server** Datenbank Upgrade.

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

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:5b01af4f17676ee4295fa3cc279d15f7b6e4a43f9faad41dace54fe1b36861fd
docker.easydb.de/pf/eas                  sha256:5a35553dcddae1614821a38e8f207b6065b9082ee1499a65fa3b03fed3f2c57f
docker.easydb.de/pf/elasticsearch        sha256:1475d92455542b0102cf0ddc6110b17cc452cc986556857dbcf0ab79e888224f
docker.easydb.de/pf/fylr                 sha256:2fd1ab38a06a2f365984653da1546f56d6cf988602b640266cea91a4129c86b1
docker.easydb.de/pf/postgresql-11        sha256:86172297d81a82a0b303137ed5857783c6419b14358587cef05eb794da627154
docker.easydb.de/pf/postgresql           sha256:3374be1a129f4e751fce7b1ddcd561cd209a197faf9faabba5d0454d16946420
docker.easydb.de/pf/server-base          sha256:0675bd429e0c670a678b86695cc9298f0f8f1b702f0449e356178438172059ff
docker.easydb.de/pf/webfrontend          sha256:1f62ff7b834c23d2f29379bfaf2a2126e5c466c267b742c45cf37f255210f980
```

