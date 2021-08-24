---
menu:
  main:
    name: "5.88 (August 2021)"
    identifier: "5.88"
    parent: "releases"
    weight: -588
---

> Für dieses Release ist **kein Re-Index** nötig. 

> Die **Plugin-Namen** und Konfiguration-Dateien haben sich geändert. Für von Programmfabrik ausgelieferte Plugins heisst die Konfigurationsdatei jetzt immer `manifest.yml`. Mehr Informationen findet sich [hier](https://docs.easydb.de/en/technical/plugins/#plugin-definition)
>
> In der **Elastic Version 7.14.0**, welche in **easydb 5.88.0** verwendet wurde, hat es einen Bug, welcher die Indexierung von neuen Objekten blockiert. Technische Details finden Sie hier bei [Elastic](https://discuss.elastic.co/t/cannot-copy-field-to-fields-copy-to-currently-only-works-for-value-type-fields-not-objects/280429). Wir haben das entsprechende Docker-Image am 20.08.2021 wieder auf Elastic 7.13.2 zurückgerollt. Die Checksum wurde angepasst.

# Version 5.88.2

*Veröffentlicht am 24.08.2021*

## Webfrontend

### Behoben

* **Suche**: Ein Fehler im Filter führte dazu dass ab Level 2 keine Einträge angezeigt wurden.
* Detail: Die Vollbild-Detailanzeige zeigt Bilder nun wieder in höchster Auflösung an. 

# Version 5.88.1

*Veröffentlicht am 19.08.2021*

## Webfrontend

### Behoben

- **Mitteilungen**: Angezeigte Deeplink URL wurde repariert.
- **Usermanagement**: Auswahl der *Typ* wurde für installierte LDAP- und SSO-Plugins repariert.

# Version 5.88.0

*Veröffentlicht am 18.08.2021*

## Webfrontend

### Neu

* **Maskenmanagement**: Eine neue Option erlaubt es nur den ersten Eintrag von Mehrfachfeldern in die Standard-Info zu rendern.
* **Usermanagement**: Verschiedene Sortiermöglichkeiten für die Nutzerliste wurden hinzugefügt.

### Verbessert

* Beim Anlegen eines neuen **Email-Benutzers** in der Nutzersuche (z.B. Mappen) kann man jetzt immer einen neuen Nutzer anlegen, auch wenn eine ähnliche Email im System bereits existiert.
* **Metadaten**: Der`Fester Wert`-Dialog kann abgebrochen werden.
* **Editor**: Ändern des Pools hat in einigen Fällen den Speicher-Button nicht aktiviert.
* **Systemnachrichten** bei nicht erreichbaren Servern wurde verbessert.
* **CSV-Importer**: Das Hochladen von Hierarchien wurde verbessert und erlaubt nun ein referenzieren von Eltern-Datensätzen aus dem CSV, also Datensätzen die noch nicht in der Datenbank sind.
* **Mappen**: Das Verschieben einer Mappe in die höchste Ebene ist jetzt möglich.

### Behoben

* **Asset-Browser**: Die Anzeige konnte in einigen Fällen nicht gewechselt werden und es kam zu einem Javascript-Fehler.
* **Editor**: Das Datumsbereichs-Feld hat unter Umständen das Bis-Datum nicht automatisch ausgefüllt.
* **PDF-Creator**: Anzeigefehler bei Textfeldern behoben.
* **Vollbildansicht**: Die Anzeige von leeren Objekten (ohne Bild) zeigt jetzt einen Platzhalter-Text.
* **Detail/Editor**: Anzeige von Tags bei verlinkten Objekten im Text-Modus wurde behoben.
* **Suche**: Bei verändertem Entwicklungs-Datenmodell konnte es im Filter zu Javascript-Fehlern kommen.
* **Suche**: In der Tabellenansicht sind teilweise Zeilen verschwunden nachdem die Datensätze bearbeitet wurden.

## Server

### Neu

- Support von `.obj`Dateien als `vector3d`.
- **Standard-Info** in Mehrfachfeldern kann jetzt nur das erste Feld berücksichtigen.

### Verbessert

* Änderungen bei den Plugin-Namen und Pfaden.
* Verbesserungen im internen HTTP-Aufruf des Easydb-Asset-Server.

- **Standard-Info** für Datumsbereiche zeigt nur noch ein Datum, wenn von und bis diesselben Daten sind.

### Behoben

* **/api/schema**: Beim Laden von neuen Datenmodellen werden Masken mit reverse Verlinkten Objekttypen korrekt gepflegt. Zuvor konnte es zu Inkonsistenten im Datenmodell kommen, was aber keine weitere Auswirkungen hat.

- **/api/db_info**: Anfragen mit `pool_id`für Objekttypen ohne Pool-Support verusachen keinen Fehler mehr.
- Fehlerbehebungen im **Speichermanagement**.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version): 

```ini
docker.easydb.de/pf/chrome               sha256:ce4ccb312e12cdcb8daa9151e80081738b2612b1c109ecdcb39519e3f367c6ec
docker.easydb.de/pf/eas                  sha256:ca98bb2b8ad5b7f185e730446752153dfc5fac0b8bae5e06326aa41b66b794b4
docker.easydb.de/pf/elasticsearch        sha256:2a9ca9620e35567d8ea6c666055e4377ca556d16b0a619f2198d9cc9fe9bc526
docker.easydb.de/pf/fylr                 sha256:c468d4f73670d4fb2b40b62290c3a680ba83ed611b5991102c940c15013d7272
docker.easydb.de/pf/postgresql-11        sha256:0edc0e28c643c886790c5b5d84ab224e4950edaad3b4d27dda04fa875c0f6ce1
docker.easydb.de/pf/server-base          sha256:43067ee9e6c48417838c5e7c88cbff934f860fc9d7fc64bb8d3748a85f19358f
docker.easydb.de/pf/webfrontend          sha256:fe0b2f058d4161956351825e487bf38d38b4f0fb5ad56f7123b30095f0d952e8
```

