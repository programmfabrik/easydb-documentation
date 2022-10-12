---
menu:
  main:
    name: "5.94 (Januar 2022)"
    identifier: "5.94"
    parent: "releases599"
    weight: -594
---

> Diese Version bringt **beschleunigte Ladezeit** der Applikation. In einigen Tests lädt **easydb** nun bis zu **5x schneller** als zuvor. Diese Beschleunigung konnte erreicht werden durch massive Parallelisierung beim initialem Laden der benötigten Resourcen.
>
> **5.94.1**. bringt die aktuelles Elasticsearch-Version [7.16.3](https://www.elastic.co/guide/en/elasticsearch/reference/current/release-notes-7.16.3.html), welche das **log4j**-Sicherheitsproblem löst.

# Version 5.94.3

*Veröffentlicht am 27.01.2022*

## Webfrontend

### Behoben

* **CSV-Importer**: fehlerhafte Suche korrigiert
* **CSV-Importer**: leere Daten bei Datumsbereichen können importiert werden
* **Feld-Rechte**: fehlende Verarbeitung der Rechte korrigiert
* **mask-splitter-detail-linked-Plugin**: Fehler bei fehlendem Zugriff auf `HEAD`-Schema korrigiert

## Server

### Behoben

* Antwort auf `/api/v1/mask/CURRENT/_all_fields` korrigiert

# Version 5.94.2

*Veröffentlicht am 18.01.2022*

## Webfrontend

### Behoben

* **Detail**: Render-Bug bei bestimmten verschachtelten Daten behoben.

# Version 5.94.1

*Veröffentlicht am 14.01.2022*

## Webfrontend

### Behoben

* **Objekttyp-Manager**: Fehler beim Speichern wurde behoben.
* **Collection**: Link für einen anonymen Nutzer wurde behoben.
* **Detail**: Beim Öffnen des Asset-Versions-Dialog wurde ein JS-Fehler behoben.
* **PDF-Druck**: Die Anzeige von Bilder wurde nochmals repariert.

## Server

### Behoben

* **Elasticsearch-Docker-Image** ist jetzt die Version  [7.16.3](https://www.elastic.co/guide/en/elasticsearch/reference/current/release-notes-7.16.3.html) mit einem Fix für das **log4j**-Sicherheitsproblem.

# Version 5.94.0

*Veröffentlicht am 12.01.2022*

## Webfrontend

### Neu

* **Vollbild**: Anzeige der Detailinformation ist in neuem Design und rechts neben der Vollbilddarstellung.
* **Editor**: Beim Kopieren kann nun ausgewählt werden ob Reverse Nested Objekte mitkopiert werden oder nicht.

### Verbessert

* **Optimierung** der Ladezeit der Applikation.
* **Filtertree**: Ausgabe von doppelten Bezeichnungen bei Mehrfachfeldern wurde unterdrückt.
* **Suche**: Anzeige hierarchischer Objekte mit langen Namen wurde verbessert

### Behoben

* **Detail**: Info > Version hatte teilweise Probleme komplexere Versionshierarchien anzuzeigen.
* **PDF-Druck**: Es konnte passieren, dass einige Bilder im PDF nicht angezeigt wurden.
* **Accessibility-Attribute** für einige Inputs wurden korrigiert.

## Server

### Neu

* **Easydb-Asset-Server**: SVG-Support in `vector2d`.
* **Group Edit Mode**: Aktualisierung des Pool in Reverse Nested Objekten.
* **Transitions**: Email vom Pool-Ansprechpartner kann für **Transition-Emails** genutzt werden.

### Verbessert

* **Performance**-Verbesserungen bei **Session-Requests**.
* **Performance**-Verbesserungen bei der Suche von Type `message`.
* Optimierungen beim Elastic-Mapping mit vielen konfigurierten Sprachen und Custom-Data-Types.

### Behoben

* Ein **Indizierungsproblem** beim Import hierarchischer Objekte wurde behoben.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:159c4b4bc369dffa9751cbcc040a244bf5b2c6cc7856366afe5ba7a0c48b8b28
docker.easydb.de/pf/eas                  sha256:03bedfbf2b538ca64e4252fe90bafd98ef46ed3d48122eff94b81775b8793010
docker.easydb.de/pf/elasticsearch        sha256:4dcd768f26abab24ea894642619541b7993885521925130599b408991fbc1444
docker.easydb.de/pf/fylr                 sha256:2b10cafd9de76f064cc8b90afa9c5103fafd5baafd69912c6cb245ed172f632b
docker.easydb.de/pf/postgresql-11        sha256:8aa9ff8cbc673b2b1f234b9fe058a3bf1544ea8074cebef45d35dba8081f8afa
docker.easydb.de/pf/server-base          sha256:0ac826fb01798031a8d9b2e5c5b0c15f7f65c236a557fb3cf295e169baa943cd
docker.easydb.de/pf/webfrontend          sha256:90dc4ef33e4412e84425ff3ec65e90cba29e6f263918e60a632fcfc2c0e3eb03
```
