---
menu:
  main:
    name: "5.120 (Anfang August 2023)"
    identifier: "5.120"
    parent: "releases"
    weight: -620
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.120.0

*Veröffentlicht am 02.08.2023*


# Webfrontend

## Neu

* **Editor**: Es ist jetzt möglich, den Vollbild-Editor eines Datensatzes direkt aus der Suche heraus mit der Tastenkombination `alt + Doppelklick` oder `cmd + Doppelklick` zu öffnen

## Verbessert

* Zum Start der Anwendung wurden Verbesserungen vorgenommen, um die Ladegeschwindigkeit zu verringern
* Beim Zugriff auf die Anwendung über einen Deep Link zum Pool wird die Willkommensnachricht nicht angezeigt
* Verbessertes Verhalten beim Löschen von Objekten im Listenfeld
* **Mappenfreigabe**: Die Benutzer- und Gruppenauswahl im Share-Panel wurde verbessert. Wenn Benutzern eine E-Mail-Adresse zugewiesen ist, wird diese in der Auswahl angezeigt, um die Benutzerauswahl zu erleichtern
* **Ereignis-Manager**:
  * Das Detailpanel wurde verbessert
  * Es wurde eine Schaltfläche zum Zurücksetzen der Suchfilter hinzugefügt
* Der EAS-Selektor in den ACL-Konfigurationsfeldern wurde verbessert und korrigiert

## Behoben

* Ein Fehler wurde behoben, bei dem die mehrsprachige Spalte im Gruppeneditor nicht mit einem leeren Wert bearbeitet werden konnte
* **Ereignis-Manager**: Es wurde ein Fehler beim Versuch, alle Ereignisse aus der Liste zu löschen, behoben
* Fehler behoben, der das Herunterladen der ursprünglichen Assets in EAS-Feldern aus der Basiskonfiguration nicht ermöglichte
* Fehler behoben, der auftrat, wenn ein Metadaten-Mapping verwendet wurde, um neue Elemente zu einem verschachtelten Objekt hinzuzufügen, das bereits Elemente enthielt

# Server

## Neu

* **Plugins**: die Konfigurationsdatei `manifest.yml` kann jetzt im `build` Ordner angegeben werden

## Verbessert

* **`/api/v1/db`** mit aktiviertem `all_versions` Parameter:
  * alle verknüpften Objekte in History-Versionen haben eine `_system_object_id`
  * Überspringen von verschachtelten Einträgen
* **Metadaten-Mapping**:
  * Listenmodus für `XMP-iptcCore:Scene` Tag wurde aktiviert
  * `api/xmlmapping/mapping/<name>`: Mapping `id` als wird als Integer zurückgegeben

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.120.0         sha256:713e13856c004ab026c8e7258dfd6a299b67ed1b57650b88488f5c47c64af6d5
docker.easydb.de/pf/eas:5.120.0            sha256:c02b34ea47f8f1fa43b042ad760f3f85667aafb10d03369f8b02de0df071423a
docker.easydb.de/pf/elasticsearch:5.120.0  sha256:73b11a4096079138a39fe92e1967c5f6b6e00c982e20cb54da34bc7727b6586c
docker.easydb.de/pf/fylr:5.120.0           sha256:babab810fab1a09d712cd97497b587f974073f3889ad263a90c37c815c767c60
docker.easydb.de/pf/postgresql-14:5.120.0  sha256:7bc2f9c717adfa1a25e8efb08936b245c6bbb70bca3105b3ea023447a62e7487
docker.easydb.de/pf/server-base:5.120.0    sha256:223c3f758a437043a93e70e7342b06fb06e7274bae4c46e31bf3c90f38a7dcb0
docker.easydb.de/pf/webfrontend:5.120.0    sha256:ff62fe50677be30fef2041f5b25d62f2039c9596294def4971ba5537636ba8d0
```
