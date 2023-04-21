---
menu:
  main:
    name: "5.115 (Mitte April 2023)"
    identifier: "5.115"
    parent: "releases"
    weight: -615
---


> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.115.0

*Veröffentlicht am 19.04.2023*


# Webfrontend

Das Webfrontend nutzt nun NodeJS mindestens in Version 16

## Verbessert

* **Suche**:
  * Verbesserte Filter für Datumsfelder
* **Objekte mit fehlendem Standard**:
  * Verbessertes Such-Popover bei fehlendem eas-Standard
  * Verbesserte Vorschau von Objekten ohne Standard
* Wenn keine konfigurierte Sprache verfügbar ist, wird eine Fallback-Sprache verwendet


## Behoben

* Fehler in der Vollbildansicht von Mappen behoben
* Fehler im Drag & Drop-Verhalten von Dateien/Assets im Editor behoben
* Fehler im Weblink Custom Datatype (Plugin) für Links mit den Parametern `#` und `?` behoben
* Probleme im Gruppeneditor mit mehr als 100 Objekten behoben
* Fehler mit Feldrechten behoben
* Fehler in der Expertensuche behoben
* Probleme mit Mask Splittern und Mehrfachfeldern ohne sichtbare Kinder behoben

# Server

## Neu

* **XML Export**:
  * Die Top Level Felder `_id`, `_system_object_id`, `_version` sind jetzt optional

## Verbessert

* Bei Workflows, die Berechtigungen widerrufen: verbessertes Handling von Bestätigungscodes und Policies in der API


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.115.0         sha256:0dec1b427f6d420c3793e8f0d6a2952d9e82f026f20d9cf7332aa40933363630
docker.easydb.de/pf/eas:5.115.0            sha256:6ecfd1750ec0319a64c197a4849329bdb3809a9a54d6ec287074fa4b9bd67d65
docker.easydb.de/pf/elasticsearch:5.115.0  sha256:576e7ae7f45f2eabd18a88a24cb5b49314c4289c4e23bacc53eb7f8f5058306c
docker.easydb.de/pf/fylr:5.115.0           sha256:88e88dbc881b5f7145c981b8daccb640feb6c2bada70597121306867048f72e0
docker.easydb.de/pf/postgresql-11:5.115.0  sha256:86d2ea1d89d245a77017bce8f3c454dc3cd36bb80a5e0f00e4231d3d8f61725c
docker.easydb.de/pf/postgresql-14:5.115.0  sha256:726f3ca5e83fcb75f98c97c90d1102d5b1795c3c60320427c03e217804f1af47
docker.easydb.de/pf/server-base:5.115.0    sha256:470040311fe0ffce2a82260884baf8cc2d9553578fb139eba4ec2ce8d3b2ca78
docker.easydb.de/pf/webfrontend:5.115.0    sha256:62f5f24dd405bc41e8869e4abcaa81fa46c691a1186fea05637447e9b25dbad5
```
