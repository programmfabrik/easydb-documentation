---
menu:
  main:
    name: "5.130 (März 2024)"
    identifier: "5.130"
    parent: "releases5130"
    weight: -630
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.130.0

*Veröffentlicht am 20.03.2024*


# Webfrontend

## Neu

* **Zur Mappe hinzufügen**: Das Tool "Zur Mappe hinzufügen" wurde an mehr Stellen in der App hinzugefügt, z.B. im Detailbereich und in der Vollbildansicht
* **Auswahl für die Ansicht im Hierarchiemodus**:
  * In der Hauptsuche und in der Listensuche wurde ein Selektor hinzugefügt, mit dem Sie auswählen können, wie hierarchische Objekte angezeigt werden
  * Dieser neue Selektor ersetzt die Schaltfläche "Nur oberste Ebene" in der vorherigen Version und ersetzt auch die alten Optionen für "flache Hierarchie"
* **Connector Plugin**:
  * Das Connector Plugin wurde aktualisiert, um Verbindungen zwischen *easydb5*- und *fylr*-Instanzen zu unterstützen
  * Unterstützung für das Connector-Plugin wurde in *fylr* hinzugefügt


## Verbessert

* **Ereignisse**:
  * Es wurden Design-Korrekturen am Event-Manager vorgenommen
  * Für Ereignisse, die sich auf Assets beziehen, wurde eine Schaltfläche zur Anzeige des referenzierten Assets hinzugefügt
**CSS**: Es wurden zahlreiche Verbesserungen im CSS der Anwendung vorgenommen
* **Filteransicht**: Die Datumsfilter zeigen jetzt nur noch 10 Elemente an, ähnlich wie andere Filter


## Behoben

* **Editor**: Es wurde ein Fehler behoben, bei dem das Editor-Popover beim Laden einen JavaScript-Fehler auslöste, so dass es nicht verwendet werden konnte
* **Gruppeneditor**: Es wurde ein JavaScript-Fehler behoben, der auftrat, wenn versucht wurde, den Gruppeneditor mit einem Benutzer zu laden, der nicht über bestimmte Berechtigungen verfügte
* **Suche**:
  * Ergebnisansichten: Es wurde ein JavaScript-Fehler behoben, der auftrat, wenn die Suchansichten in der Hauptsuche zu schnell geändert wurden, während die Suche ausgeführt wurde
  * Such-Filter: Fehler bei der Sortierung von Suchfiltern nach Namen behoben
* **Tabellenansicht**:
  * Es wurden Korrekturen bei der Durchführung von Suchen in der Tabellenansicht vorgenommen
  * Korrektur der Meldung "Leere Suche" bei Suchen in der Tabellenansicht
* **Hochladen von Mappen**: Die Fehlermeldung wurde korrigiert, wenn versucht wurde, Dateien per Drag & Drop in Mappen hochzuladen, und der Benutzer keine Berechtigung dazu hatte
* **Datenmodell SVG-Download**: Die Schaltfläche zum Herunterladen von SVGs eines Schemas wurde korrigiert. In einigen Fällen wurde das falsche Schema verwendet.
* **Audioplayer**: Es wurde ein Fehler behoben, der dazu führte, dass der Audioplayer im Asset-Browser nicht korrekt angezeigt wurde, wenn das Asset von einem verknüpften Objekt stammte
* **Schaltfläche "Nur oberste Ebene"**: Die in der vorherigen Version hinzugefügte Schaltfläche, die nur Datensätze der obersten Ebene anzeigt, wurde durch einen Selektor ersetzt


# Server

## Neu

* Neues Timestamp Feld `_id_parent_deleted_at` wurde für hierarchische Objekte in `/api/v1/db` mit `all_versions=1` hinzugefügt

## Behoben

* **Metadaten Import Mapping**: Korrektur des falschen Tags für die Video-Bildrate
* Asset-Verknüpfungen zu Pool-Wasserzeichen werden jetzt aktualisiert. Dies behebt Probleme beim Versuch, Pools zu löschen, die Assets verwenden/verwendet haben


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.130.0         sha256:3a118631706619b1de46fc84d1f598cf49d3622260ab779f6fd44326ed6ffb7a
docker.easydb.de/pf/eas:5.130.0            sha256:a7e640665b211602d20e2e9f0b1f70c8b8e52ce2ecc2c6f708e71f25f8acf36d
docker.easydb.de/pf/elasticsearch:5.130.0  sha256:df6333c4b9ccc9f59ade4e4ca8597466e8397993d385f49b607722c44ee7f34c
docker.easydb.de/pf/fylr:5.130.0           sha256:e5854f18a4a889a4167bc5e27acc0f98f692085a9e1b325c331f196c08bd5d5e
docker.easydb.de/pf/postgresql-14:5.130.0  sha256:1196d0427d7ecb87e1948a47a5ab7ff8135638fa0b1c524061536ed1d241229a
docker.easydb.de/pf/server-base:5.130.0    sha256:8a43c66c22d3a4b7b59b66c09d2fa07243d361399cb33fc569711a701ddaa596
docker.easydb.de/pf/webfrontend:5.130.0    sha256:63a36686172075e13b7416e2d9694cb68bbd8bbd0794cc5223221caffecc14ea
```
