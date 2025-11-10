---
menu:
  main:
    name: "5.149 (Oktober 2025)"
    identifier: "5.149"
    parent: "releases"
    weight: -649
---

> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.149.1

*Veröffentlicht am 10.11.2025*

# Webfrontend

## Behoben

* **Vollbild**: Anzeigefehler behoben

# Version 5.149.0

*Veröffentlicht am 29.10.2025*

# Webfrontend

## Behoben

* **Sortierung**: Bug behoben, der bei geschlossenen Panels die Sortierung nicht korrekt angewendet hat.
* **Expertensuche**: verschiedene Bugs beim Filter "has value" behoben
* **Default-Tags**: Bug behoben, bei dem versteckte Default-Tags nicht korrekt angewendet wurden.
* **Geteilte Mappen**: Probleme beim Blättern durch die Mappen behoben, wenn der Benutzer mehr als 100 geteilte Mappen hat.
* **Tags & Workflows**: Workflows-Panel ließ sich nicht öffnen, wenn die gespeicherten Daten Fehler enthielten. Eine Korrektur war so nicht möglich.
* **Mappen-Präsentation**: Präsentation ließ sich nicht öffnen, wenn Assets nicht mehr verfügbar waren.
* **Nested-Tabellen**: Problem mit leerer Zeile behoben, wenn erste Spalte ein Asset beinhaltet.
* **Export-Transport**: Öffnen des Transport-Editors schlug fehl, wenn der Transport ungültige Daten enthielt.
* **Gruppen-Editor**: Reihenfolge von Buttons und Check-Boxen behoben.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.149.0            sha256:dd77214b2d62b084faadfe28490aa984de48b7758fa7028368e867b232b1ad0a
docker.easydb.de/pf/elasticsearch:5.149.0  sha256:f2004f759cfd7f3218d6f15d9b972de3d9cccad3a2efa98bdb3f16bd084f7ac2
docker.easydb.de/pf/fylr:5.149.0           sha256:30a320ea3f95b5fa2300a93d701b327343598c0e074e76ce523967ec66ddda55
docker.easydb.de/pf/postgresql-14:5.149.0  sha256:1d2874de390056e7ff7e8401d4e9a3ac2c1a8b0fe75fc161c1effac8aa11fe38
docker.easydb.de/pf/server-base:5.149.1    sha256:911b8444e23cb3e0d8f0b09c48b51b68be1aa64300c6eadd4e0aeba8caad83de
docker.easydb.de/pf/webfrontend:5.149.1    sha256:e786aa4427ff0374454ac4e0cc62e7873689b2b458e02bdac8fd932669f13556
```
