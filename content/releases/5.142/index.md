---
menu:
  main:
    name: "5.142 (März 2025)"
    identifier: "5.142"
    parent: "releases"
    weight: -642
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.142.0

*Veröffentlicht am 26.03.2025*

# Webfrontend

## Verbessert

* **Suchergebnis**: verbessertes Rendering zur Minimierung von Flackern bei großen Listen
* **Download-Manager**: verbesserte Behandlung von Assets beim Download

## Behoben

* **Suchvorschläge**: inkorrekte Ergebnisse durch fehlerhafte Teilung der Eingaben behoben
* **Suchvorschläge**: leere Vorschläge bei einigen Custom-Typen behoben
* **Editor**: Anzeige von Validierungsfehlern bei Custom-Feldern behoben
* **Objekttypen**: doppelte Anzeige des Menüeintrags unterbunden
* **Benachrichtigungen**: Behandlung der Min-/Max-Felder korrigiert
* **Expertensuche**: Fehler beim Öffnen der Expertensuche mit ausgeblendeten Feldern behoben
* **Änderungshistorie**: Laden der neuesten Version beim Vergleich korrigiert
* **Download-Manager**: Fehler beim Download von Assets ohne Feldinformationen behoben
* **Download-Manager**: Fehler im Titel des Popup-Menüs beim Download behoben


# Server

## Verbessert

* **/api/db**: `base_fields_only`-Optimierung wird ausgesetzt, wenn sich Plugins in den Speicher-Prozess gehängt haben. Das ermöglicht mehr Manipulationen in den Plugins.

## Behoben

* **/api/pool**: korrekter Status für Wasserzeichen-Assets


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.142.0            sha256:5b856bedc5f4a6c0a64345aa18ebd809fc6e06ad993b1b30fb6fbd892983cca9
docker.easydb.de/pf/elasticsearch:5.142.0  sha256:8a982e18886fdf68e10ba871563950e6849f28ed28012ace989bced0f63af7ed
docker.easydb.de/pf/fylr:5.142.0           sha256:8228eee009eb91da6687e153ff887280f27ac35f17ae62f28c3e92ad59b0caae
docker.easydb.de/pf/postgresql-14:5.142.0  sha256:832330ca0d818b07c4d904b84b53c3067c90f62a8fee8d7ff63e7c0e66da76fa
docker.easydb.de/pf/server-base:5.142.0    sha256:ce0e6d3940c24206194dd3982925f74c163c1751780d4df8055bff8ad90ece37
docker.easydb.de/pf/webfrontend:5.142.0    sha256:5feb815392a43807cb4ed1876388f5c83662d98a6fc3380ed98530370aeeefe2
```
