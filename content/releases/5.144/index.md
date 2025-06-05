---
menu:
  main:
    name: "5.144 (Anfang Juni 2025)"
    identifier: "5.144"
    parent: "releases"
    weight: -644
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.144.0

*Veröffentlicht am 04.06.2025*


# Webfrontend

## Verbessert
* **Datumsfelder**: es werden Platzhalter im Format der Instanzkonfiguration angezeigt.
* **Detail-Ansicht**: Organisation der Werkzeug-Buttons verbessert.
* **Event-Manager**: Darstellung von Objektreferenzen in Ereignissen verbessert.
* **Text-Ansicht**: Darstellungsoptionen für Text-Ansicht der Suche hinzugefügt.
* **Editor**: Verhalten von Tags in Template-Objekten für den Popover-Editor verbessert.
* **Hierarchie-Darstellung**: Darstellung von Objekten verbessert, die der Benutzer nicht sehen darf.

## Behoben
* **ACL-Manager**: Fälle behoben, in denen `undefined` als Gruppen-Name angezeigt wurde.
* **Masken-Editor**: Problem bei der Darstellung der `condensed_output`-Option behoben.
* **Read-Only-Modus**: Fehler beim Versuch, den Editor aus der Listenansicht zu öffnen, behoben.
* **Expertensuche**: Darstellungsfehler bei der Auswahl von verlinkten Objekten behoben.
* **Datumsbereiche**: Probleme bei Verwendung der textuellen Repräsentation behoben.
* **Filter**: Fehler einiger Plugins bei Verwendung der AND/OR-Modi behoben.
* **Metadaten-Mapping**: Erstellung verlinkter Objekte verbessert.
* **PDF-Ansicht**: Fehler im Asset-Browser behoben.
* **Nachricht vor Downloads**: Fehler behoben, die den Download verhindern konnten.
* **Vollbild-Detailansicht**: Fehler behoben, der die Aktivierung der Zoom-Ansicht mittels Mausrad verhindern konnte.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.144.0            sha256:00a801ba9b0f849e49af33991de947b394c19703f4ee993355679e66062825b3
docker.easydb.de/pf/elasticsearch:5.144.0  sha256:ed71b5fdb392b2d920e0305aee8b4e17f68ceb360960abb250fcb166131e03aa
docker.easydb.de/pf/fylr:5.144.0           sha256:71f7fff54cc94a259b826f684909ba94a272bce542e1ba2d25a04106ed5b83c9
docker.easydb.de/pf/postgresql-14:5.144.0  sha256:3be5f7992b463ac4aa6f2a06ea91d9337163e509ee7c60ddb900c070e85992f8
docker.easydb.de/pf/server-base:5.144.0    sha256:e6bb39b78bb166aa0ea77d7cbbdb039507b65e4a899156079188b73007cf8832
docker.easydb.de/pf/webfrontend:5.144.0    sha256:79841286dde3a97c2129f4a29b4948c0fc57bccc2f97f872c89bd3b3a45aa7a7
```
