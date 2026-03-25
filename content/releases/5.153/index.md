---
menu:
  main:
    name: "5.153 (Ende März 2026)"
    identifier: "5.153"
    parent: "releases"
    weight: -653
---

> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.153.0

*Veröffentlicht am 25.03.2026*


# Webfrontend

## Verbessert

* **Vollbild-Detailansicht**: Der Vollbild-Browser wird entsprechend aktualisiert, wenn in der Vollbild-Detailansicht die Option zum Ansehen verlinkter Objekte aktiviert ist.
* **Dateinamen-Suche**: Es ist jetzt möglich, mehrere Suchbegriffe komma-separiert im Dateinamensfeld anzugeben,

## Behoben

* **Sucheliste**: Bug behoben, bei dem Hierarchien nicht korrekt dargestellt wurden, wenn auf einzelne Pools gefiltert wurde.
* **Verlinkte Objekte**: Validierung verbessert, ob ein verlinktes Objekt korrupt oder nicht existent ist.
* **CSV-Importer**: Import lokalisierter Strings in verschachtelten Strukturen korrigiert.
* **Maske merken**: Bugs in der Initialisierung beim Öffnen von Editor oder Detail behoben.
* **Metadaten-Mapping-Editor**: Drag & Drop von Feldern korrigiert.
* **Tooltips**: Verhalten in vertikalen Menüs behoben, jetzt korrekt ausgerichtet.
* **Export-Manager**: Bug bei der Sortierung behoben.
* **Metadaten-Mapping**: Bug bei Verwendung von Custom-Datentypen behoben.
* **Verlinkte Objekte**: Bug behoben, bei dem neu erstellte verlinkte Objekte als "nicht gefunden" angezeigt wurden. Außerdem ein Problem behoben, bei dem die Standard-Information vom Server ungenutzt blieb und bei Nachladeversuch eine Rechte-Warnung angezeigt wurde.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.153.0            sha256:6fa0ce2b13ae30e00a1a24894b14e91d0d53d8cb90f3f9287ec50f188125b51a
docker.easydb.de/pf/elasticsearch:5.153.0  sha256:be0527b75cdaae3b2ae4a1c341fa9437a52598ae12729116b6d23766962d8b81
docker.easydb.de/pf/fylr:5.153.0           sha256:23e36d632cb5101f43766d830f9e0a4e7047ae9112f5ec90c1411b055c838485
docker.easydb.de/pf/postgresql-14:5.153.0  sha256:8d7710d5687f2cb81b0f040f9a66138522c8593b76e4a230ab5e18975fa20ccd
docker.easydb.de/pf/server-base:5.153.0    sha256:9c7491b2e1cbd39cda1c53533a2db30dc28c8752babbda0988111b131f31e2d3
docker.easydb.de/pf/webfrontend:5.153.0    sha256:21f56d720ccfe55ae306f52c058edf150036e315278eb49df519937d8f901657
```
