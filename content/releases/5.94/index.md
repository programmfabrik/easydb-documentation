---
menu:
  main:
    name: "5.94 (Januar 2022)"
    identifier: "5.94"
    parent: "releases"
    weight: -594
---

> Diese Version bringt **beschleunigte Ladezeit** der Applikation. In einigen Tests lädt **easydb** nun bis zu **5x schneller** als zuvor. Diese Beschleunigung konnte erreicht werden durch massive Parallelisierung beim initialem Laden der benötigten Resourcen. 

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

* **Easdb-Asset-Server**: SVG-Support in `vector2d`.
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
docker.easydb.de/pf/elasticsearch        sha256:b772d2f4078f78272c74819ba15aedb70b50b5f627293eb814d318d54aed453a
docker.easydb.de/pf/fylr                 sha256:2b10cafd9de76f064cc8b90afa9c5103fafd5baafd69912c6cb245ed172f632b
docker.easydb.de/pf/postgresql-11        sha256:8aa9ff8cbc673b2b1f234b9fe058a3bf1544ea8074cebef45d35dba8081f8afa
docker.easydb.de/pf/server-base          sha256:f569419e282a3d1d0cfbe781ee6a04cfde77b86e078ad62ea04704193937e6d6
docker.easydb.de/pf/webfrontend          sha256:a191cf6bcef98905840cccebe88fe571f08768c5f437e820e46da9c26d77b714
```
