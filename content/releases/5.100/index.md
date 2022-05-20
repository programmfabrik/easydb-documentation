---
menu:
  main:
    name: "5.100 (Mai 2022)"
    identifier: "5.100"
    parent: "releases"
    weight: -600
---

> Diese Version **benötigt keinen neuen Index-Aufbau**

> Für diese Version wurde **python 3** eingeführt, und ersetzt **python 2.7** vollständig. Alle Plugins mit einer Python-Version unter **python 3.x** werden nicht mehr funktionieren

# Version 5.100.0

*Veröffentlicht am 18.05.2022*


## Webfrontend

### Neu

* Ein neuer Kontakt wurde zu den Workflows hinzugefügt: **Poolkontakt** (siehe unten)

### Verbessert

* **Suche**: Viele Verbesserungen und Bugfixes im **Filter**
* **Ereignisse**: Die Art und Weise, wie die Benutzertypen für die Ereignisse ermittelt werden, wurde geändert (interne Änderung)
* **Rechteverwaltung**: Verbesserungen der Benutzerfreundlichkeit im Feldselektor für Rechte
* **Export**: Allgemeine Fehlerbehebungen und Verbesserungen

### Behoben

* **Editor**: Bugfix beim Schließen des Editors, manchmal wurde mehr als einmal die Meldung "ungespeicherte Änderungen" angezeigt
* **Kleinere Bugfixes in**:
  * Asset-Detailansicht
  * Mappenansicht
  * Zählung der Objekte in Listen (manchmal war die Zahl negativ)
  * Detailansicht, in der die Maske nicht in der Fußzeile angezeigt wurde
  * Button "Aktualisieren" bei Mappen

## Server

### Neu

* **Plugin-Implementierung**:
  * interne Python-Implementierung wurde von **python 2.7** auf **python 3.x** aktualisiert
  * alle Plugins, die eine Python-Implementierung haben, wurden ebenfalls aktualisiert
* **Workflows**: es ist nun möglich, Benutzerkonten, die als Poolkontakt verwendet werden, als E-Mail-Empfänger in Workflows zu definieren
* **Benutzerverwaltung**: das Recht zum Bearbeiten oder Löschen von SSO-Benutzern kann nun auch anderen Benutzern/Gruppen gewährt werden
* **Rechteverwaltung**:
  * Benutzer können jetzt ihre eigenen Lese-/Schreibrechte für Objekte entfernen
  * Dies ermöglicht das Verstecken von Objekten für sich selbst, anstatt Objekte tatsächlich zu löschen.

### Verbessert

* **Janitor**: Leistungsverbesserung bei Anweisungen zum Sammeln unbenutzter Wasserzeichenversionen von Assets

### Behoben

* **Gruppeneditor**: versucht nicht mehr, Pools für Objekte zu aktualisieren, für die die Poolverwaltung nicht aktiviert ist

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:02a6f3bf6d5b7932e98b46e60d878f07e0670730d10c9f804d07f266c3d2038a
docker.easydb.de/pf/eas                  sha256:f271316bc335e9cd8c3bc919bdba623f5493cbca9a31c5f094ce362b91bff498
docker.easydb.de/pf/elasticsearch        sha256:93cf92e964b6c25fe6acff8d0eb38a53935d0ec159c36038606ed9b6c4957bb3
docker.easydb.de/pf/fylr                 sha256:e59c504f7fad36c5da09fa558351293e710148f7fc10ed3f19fa1a8c566dcbeb
docker.easydb.de/pf/postgresql-11        sha256:a0800dfaf78ea5cef8df083677b7a842e9d6f629ed5aa2e060ec6b973d4648f4
docker.easydb.de/pf/server-base          sha256:53bb27ddcc5e3685d2bd9907b84ce5ee132a629264c975f5963424e895db1862
docker.easydb.de/pf/server-base-py3      sha256:ee5cc91b4f691fa4c6664cb96f13e80c802d44c213866e9e134ec6db9f74bb65
docker.easydb.de/pf/webfrontend          sha256:4df060fc228538ecdb90c62788d4b682cab0061055f79dda7b94d226e674a27d
```
