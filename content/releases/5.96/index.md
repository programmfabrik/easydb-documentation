---
menu:
  main:
    name: "5.96 (Februar 2022)"
    identifier: "5.96"
    parent: "releases"
    weight: -596
---

> Diese Version **benötigt keinen neuen Index-Aufbau**

# Version 5.96.1

*Veröffentlicht am 25.02.2022*

## Webfrontend

### Behoben

* **Export-Manager**: unzulässige Aggregation vermieden
* **Login**: Fehler bei erlaubter anonymer Suche behoben

# Version 5.96.0

*Veröffentlicht am 23.02.2022*

## Webfrontend

### Verbessert
* **Filter**: Tooltips mit langen Feldnamen
* **Filter**: Filter und Suche verwenden bei Datumsbereichen die selben Felder, Ergebnisgrößen sind jetzt identisch
* **Suchergebnis**: Verhalten von Fokus und Selektion optimiert

### Behoben
* **Objekttyp-Einstellungen**: Javascript-Fehler behoben
* **Upload**: Verlinkung von Assets in verschachtelten Mehrfachfeldern behoben
* **Listen**: Fehler bei unzulässigem Limit behonen
* **Expertensuche**: fehlerhafte Anzeige der Suche für Boolean-Werte korrigiert
* **JSON-Importer**: Fehler beim Lookup korrigiert
* **Session**: Sprachauswahl beim ersten Start behoben
* **Filter**: fehlendes Jahr 2020 für Datumsfelder hinzugefügt
* **Editor**: Speichern-Button weiter aktiv, wenn Speichervorgang fehlschlägt

## Server

### Neu
* Subfeld `.from_to` für Datumsbereiche in Suche und Aggregation hinzugefügt
* Sammlung zu löschender Assets wieder standardmäßig aktiviert (finales Löschen noch nicht)

### Behoben
* Überprüfung bei Vergabe von Systemrechten korrigiert, Rechte-Parameter mit Werten können auch von Nicht-Root-Nutzern weitergegeben werden
* Aggregation von Datumsfeldern korrigiert

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:92a28b8e623b2ccea6a5432187bb456840dd4daa53b5157dc935840063a48f2d
docker.easydb.de/pf/eas                  sha256:57347ba2a6424f833134f6a9e4f45629cf0e84a68c93ed6a7ae819f04bb3344e
docker.easydb.de/pf/elasticsearch        sha256:ab52585539b6da9746161316c9fbd01eb14b6b5fa5fa9a47d367df63d09763b0
docker.easydb.de/pf/fylr                 sha256:29d8bef5582ec5e2252af7e6537046e152eb1f672e7b1c7c93bb66216f038952
docker.easydb.de/pf/postgresql-11        sha256:2199d9e062db47ba58b3dcf11d65f605cfc47f278c9853e392f076e76a392f2a
docker.easydb.de/pf/server-base          sha256:453cf50e1e287a67ee65c01377cf7ab65135b8e4fd8be321733687460e4a4ef6
docker.easydb.de/pf/webfrontend          sha256:3ac74bf18ab5fde753261cb2e990f8c2f9d0c5439cf26af907dbd7027a9f3a52
```
