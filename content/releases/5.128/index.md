---
menu:
  main:
    name: "5.128 (Februar 2024)"
    identifier: "5.128"
    parent: "releases"
    weight: -628
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.128.0

*Veröffentlicht am 07.02.2024*

# Webfrontend

## Neu

* Die Schnellzugriffsansicht zeigt jetzt standardmäßig den Asset-Browser an

## Verbessert

* Der PDF-Creator wurde verbessert, indem die Möglichkeit hinzugefügt wurde, eine Maske im Editor auszuwählen, so dass User eine Vorschau darauf erhalten, wie die PDF-Vorlage mit einer bestimmten Maske aussehen wird
* Die Schaltfläche "Verlauf anzeigen" im Druckmanager wurde verbessert
* Die Anzahl der in der Detailansicht angezeigten Objekte wurde erhöht und die Funktionalität der Schaltfläche "Weitere Objekte laden" wurde korrigiert
* Die Funktionalität der Hauptsuche wurde verbessert:
  * Wenn ein Objekt in der Detailansicht über die unteren Navigationsschaltflächen geändert wird, wird die Auswahl in der Hauptsuche korrekt aktualisiert, um das neu ausgewählte Objekt anzuzeigen
* Die Funktionalität des Hauptmenüs wurde verbessert
  * Die Anwendung merkt sich jetzt ihre Konfiguration (unabhängig davon, ob User sie geöffnet oder geschlossen haben)
* Das Verhalten des Asset-Browsers beim Laden neuer Assets in die Anwendung wurde deutlich verbessert:
  * Der Asset-Browser zeigt nun nach und nach die verarbeiteten Versionen an
  * Das heißt, wenn beispielsweise ein Video hochgeladen wird, zeigt der Asset-Browser zunächst die Vorschau an, sobald sie verfügbar ist, und zeigt dann die bearbeiteten Versionen des Videos an (360p, 720p usw.)
* Die Verwendung des EAS-Pollers in der Anwendung wurde verbessert, so dass er nicht mehr ausgeführt wird, wenn er nicht benötigt wird

## Behoben

* Ein Fehler in der Sucheingabe, der doppelte Anführungszeichen in Suchbegriffen verursachte, wurde behoben
* Der Vollbild-Editor zeigt nun den Asset-Browser korrekt an, wenn er geöffnet wird
* Das Feld "System Object ID" in der Expertensuche und im Sortiermenü wurde korrigiert
* Ein Fehler, der verhinderte, dass das neu geladene Objekt in der Hauptsuche angezeigt wurde, wurde behoben
* Die Reihenfolge der Optionen in der Qualitätsauswahl des Videoplayers wurde korrigiert
* Korrekturen an der Funktionalität des Vollbildeditors

# Server

## Behoben

* Datenmodell: Probleme bei der Umbenennung von Feldern mit langen Namen behoben

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.128.0         sha256:a0912128b9537b1cc74716007eb74e819d6fa72720882301b39050b66d25bc84
docker.easydb.de/pf/eas:5.128.0            sha256:c33543d6afa5e5f71ed9f26b50a1285df4302bdb909848fd88be92435104bdc3
docker.easydb.de/pf/elasticsearch:5.128.0  sha256:a50b7a670d2c85b1bc2cbda0a58c1bca2d081b25ca58ec34e8cfca699679de93
docker.easydb.de/pf/fylr:5.128.0           sha256:16b6a996996c546ad7d123e513ee5069c72d2a48ca76ce2dc6ecef2835217376
docker.easydb.de/pf/postgresql-14:5.128.0  sha256:c4fb4892e216034df67ef53118faa2c73df60604ff07e80cf513b1d44bb66bdd
docker.easydb.de/pf/server-base:5.128.0    sha256:18f1867000b337843d2bec2bf8589661e1009aa2bdaa32ca48888566f4c05f3f
docker.easydb.de/pf/webfrontend:5.128.0    sha256:b786e45138d15056c1aef71f282ed903b84aee4de737a570d319a1b3487a3490
```
