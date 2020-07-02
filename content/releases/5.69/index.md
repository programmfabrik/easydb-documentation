---
menu:
  main:
    name: "5.69 (Juni 2020)"
    identifier: "5.69"
    parent: "releases"
    weight: -569
---

> Dieses Release benötigt keinen Re-Index.

# Version 5.69.3

*Veröffentlicht am 02.07.2020*

### Webfrontend

*Verbessert*

* **Chromium** wird jetzt als Browser erkannt und als unterstützt akzeptiert.

*Behoben*

* Darstellung von Filtereingabefeld im Nutzermanager wurde korrigiert.
* Darstellung einiger Texte wurde korrigiert (Zeilenumrüche fehlten seit 5.69.0).

### Server

*Behoben*

* **E-Mail Versand** wurde repariert.
* Erkennung geänderter Gruppen (deren Rechte geprüft werden) beim Speichern von Nutzern korrigiert.

# Version 5.69.2

*Veröffentlicht am 30.06.2020*

### Webfrontend

*Behoben*

* Anzeige von Daten im Editor für Masken die nur im Detail verfügbar sind wurde korrigiert.

### Server

*Neu*

* Neue Frontendsprachen *PL*,*RU*,*CZ* as Dummy angelegt.

*Behoben*

* **Custom-Data-Type-Updater**: Das Verarbeiten großer Payloads führt nicht mehr zu Verarbeitungsfehlern.
*  Verbesserungen im Zusammenspiel mit **podman**.

# Version 5.69.1

*Veröffentlicht am 25.06.2020*

### Webfrontend

*Behoben*

* **CSV-Importer**: Fix für Import von verlinkten Objekten und Pools.

### Server

*Behoben*

* SQL-Fehler bei hierarchischen Objekten behoben.
* Pool-Auswahl für verlinkte Objekte im CSV-Importer korrigiert.

# Version 5.69.0

*Veröffentlicht am 24.06.2020*

### Webfrontend

*Neu*

* **Maskenverwaltung**: Unterstützung von `|`-Trenner im Standard.

*Verbessert*

* Verbesserter Browser-Check beim Start.

*Behoben*

* Die Anzeige von **Metadaten-Feldern** in tief verschachtelten Datenmodellen wurde repariert.
* Die Anzeige verfügbarer Tags beim **Pool-Wechsel** im Neu-Editor wurde korrigiert.
* Der Editor konnte nach Anzeige von historischen Objekte-Informationen unter Umständen nicht mehr benutzt werden.
* **CSV-Importer**: Verbesserte Fehlerbehandlung in Zusammenhang mit hierarischen Importen.
* Detailanzeige von offenen Datumsbereichen wurde korrigiert.

### Server

*Neu*

* Für das Rendern von `_standard`gibt es eine neue Option **pipe**. Damit werden Begriffe durch `| ` miteinander verbunden.

*Verbessert*

* Unterstützung von `lookup:_id` in Reverse-Objekten.
* **/api/user**: Performance-Verbesserung beim Laden von vielen Nutzern.
* Besseres Fehlerhandling im Custom-Data-Type-Updater.
* Sortierung Bidirektionaler Links wird jetzt gespeichert, zuvor war die Reihenfolge der Verlinkungen nicht vorhersagbar.

*Behoben*

* Bei größeren Indizes konnte es in der **OAI/PMH**-Schnittstelle zu Elasticsearch Fehlern kommen (**uuid**-Suche).
* **/api/export**: Fehlerbereinigung beim Export mit festen Asset-IDs.
* SSO: Verbesserte Fehlerbehandlung für sichtbare Anzeige von Anmeldefehlern.
* **/api/pool**: Das Löschen von Pools konnte in bestimmten Fällen nicht durchgeführt werden.
* Aktualisierungen im Index nach Gruppeneditor mit Reverse-Objekten behoebn.



# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:62ac9147529a03491b3edc35898b076fad86be181c96be9b2b701962688623f5
docker.easydb.de/pf/eas                  sha256:1eb9b08f107be72fc601753715441f4200c64653f42a8c7dabb6b9dbbd7edd5f
docker.easydb.de/pf/elasticsearch        sha256:023e67865e375cdfc475a34cc44b69cf0b2fc12a574c43e4fc7ecc0e9f8ecca3
docker.easydb.de/pf/fylr                 sha256:786ea3419e7c1395b0b720b94afdc8a6f85a697a91e9ce159e0fac44df856db7
docker.easydb.de/pf/postgresql-11        sha256:df579b5bae260a3755c3edc48fd2b94df8df9944acef46328c04195027939037
docker.easydb.de/pf/postgresql           sha256:17c8ac88d8d37e805083fa3311b93520d0488e0115b1faa33cf78ce56b63dc74
docker.easydb.de/pf/server-base          sha256:49739ab8f123febb25f6aec9c115b551b7b4801b162ffb23ea7071755d50331a
docker.easydb.de/pf/webfrontend          sha256:2d1a78f4f685d27f8c28fa043725eee994dc1c2654cf0d5fe430678ac0dc227f
```

