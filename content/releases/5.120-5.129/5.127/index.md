---
menu:
  main:
    name: "5.127 (Januar 2024)"
    identifier: "5.127"
    parent: "releases5120"
    weight: -627
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.127.0

*Veröffentlicht am 17.01.2024*


# Webfrontend

## Neu

* **Detail**: Masken-Option, um Werkzeuge bei reverse-verlinkten Objekten auszublenden

## Verbessert

* **Vollbild-Editor**: Kopierwerkzeuge hinzugefügt
* **Vollbild-Modus**: Beschleunigung bei vielen Elementen
* **gefilterte Listen**: Eingabe-Felder blockieren nicht mehr, während Anfragen laufen
* **Suche**: Option "Hierarchie anzeigen" entfernt, stattdessen kann mit Alt+Klick bzw. Cmd+Klick der Hierarchiebaum eines Eintrags rekursiv geöffnet werden
* **Allgemein**: CSS-Verbesserungen an verschiedenen Stellen

## Behoben

* Darstellungsfehler bei verschachtelten Elementen in kompakter Ansicht korrigiert
* Korrektur bei Freitext-Eingabe in Datumsbereichsfeldern
* doppelte Suchen im Zusammenhang mit Filter-Manager unterbunden

# Server

## Behoben

* Syntax der erzeugten `Last-Modified`- bzw. `Date`-HTTP-Header korrigiert
* Berechnungsfehler beim Bestimmen des nächsten Laufs im Custom-Datatype-Updater behoben
* Fehlerbehebung im EAS verbessert

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.127.0         sha256:0c9f00b83ea7c09fb0cd91df1f1d84a899a2ec8c59e2dd014bbd22e4816af27f
docker.easydb.de/pf/eas:5.127.0            sha256:1b0b6a95f6cb192b9cb6657d99cfe60e33278df7570d2ca804b9390b19c7a4c7
docker.easydb.de/pf/elasticsearch:5.127.0  sha256:05c72e35b2ef4bcec55f59d18c847916451a4fb0e0bda74373e5a9a5aedbe69e
docker.easydb.de/pf/fylr:5.127.0           sha256:23e760eba4070431c11fd3d6ec99ec12d22697337571adac2460329f9e3dbbc4
docker.easydb.de/pf/postgresql-14:5.127.0  sha256:63f0f404e14ed47f827c1df335cfe1e396d762b5ff89e24cb98409efb2d88fcc
docker.easydb.de/pf/server-base:5.127.0    sha256:fbe4901421a67e9158f05d7c02e8bc6e11baad739bd784e2f368eeaaa08ddcab
docker.easydb.de/pf/webfrontend:5.127.0    sha256:33d45280c36f4658d690e6f18cecd9d8ee8aaa8736cdeb6129ee066139fd8350
```
