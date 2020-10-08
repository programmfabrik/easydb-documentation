---
menu:
  main:
    name: "5.74 (Oktober 2020)"
    identifier: "5.74"
    parent: "releases"
    weight: -574
---

> Dieses Release benötigt **keinen Re-Index**.

# Version 5.74.1

*Veröffentlicht am 08.10.2020*

## Webfrontend

*Behoben*

* Anzeige von Vorschaubildern während des Uploads wurde repariert.

# Version 5.74.0

*Veröffentlicht am 07.10.2020*

## Webfrontend

*Verbessert*

* Suche: In der Tabellenansicht werden Mehrfachfelder eines Elternelements ausgeblendet, sobald die Kinder geöffnet werden.
* Suche: Mehr Anzeigegrößen in den Suchen.

*Behoben*

* Unterstützung von versteckten Tags wurde repariert. Versteckte Tags wurden beim Speichern im Editor fälschlicherweise gelöscht.
* Mappen: Bei bestimmten Rechteeinstellungen konnte es vorkommen dass nicht alle Mappen eines Nutzers korrekt angezegit wurden.
* Präsentationen: Die Anzeige von Connector-Objekten wurde für einige Fälle repariert.

## Server

*Neu*

- Serverseitiges Sortieren von Mehrfachfeldern.

*Verbessert*

* /api/schema: Beim Speichern vom Schema werden die Unterstützung für Typenumwandlung verbessert.

*Behoben*

* Fehlerbehandlung für SSO-Logins bei doppelten Logins wurde verbessert.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:d5f7a58adaac58a12222938ef95187f0bbdac4700131b1c3bfae21cf3ee6421e
docker.easydb.de/pf/eas                  sha256:e9c9ac0ad4a7edd7a0404bace2cdf4da84491cb841b6dfb17ddb9eb7af68e99c
docker.easydb.de/pf/elasticsearch        sha256:dcdffe49347544254e438029bcd5e784287842dfb4324c0ec4f2d96784bc2e7c
docker.easydb.de/pf/fylr                 sha256:8ff9ecc5244a497d7b5ebd59f34fa8592a949a4c5d3463dbe20c9148b178cfb8
docker.easydb.de/pf/postgresql-11        sha256:3e4f3df062810da94ec2feb7d54fa6c8aa271c600b57330086fe9c4c0623f0ff
docker.easydb.de/pf/postgresql           sha256:ba51aac137b64a3f5b79f29af94b98114994a34757d0f16885027f78b60c778c
docker.easydb.de/pf/server-base          sha256:c1798798ebf3ae8f8115bc5dc6789019bef64f9524fc87bde53a8cd04a76c56e
docker.easydb.de/pf/webfrontend          sha256:51de622e0f6282cc9e656b8489615a954f189451dc533bce720ed9ef31b39a40
```

