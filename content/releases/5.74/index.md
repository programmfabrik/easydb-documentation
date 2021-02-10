---
menu:
  main:
    name: "5.74 (Oktober 2020)"
    identifier: "5.74"
    parent: "releases"
    weight: -574
---

> Dieses Release benötigt **keinen Re-Index**.
>
> Ab Version **5.76** (erscheint geplant am **18.11.2020**) startet die **easydb** nur noch mit der neueren **PostgreSQL-Version 11**. Dieser Schnitt ist notwendig, um neue Funktionen von PostgreSQL nutzen zu können, ohne alte Installationen zu gefährden. Außerdem bekommt die alte PostgreSQL-Version keine Sicherheits-Updates mehr. Mehr Informationen im Abschnitt **[PostgreSQL 11](../5.73#postgres-11)**.
>
> Es steht ein neues Plugin zum **automatischen Verschlagworten** von Bildern zur Verfügung. Mehr Information im Abschnitt **[Auto-Keyworder](#auto-keyworder)**.

# Version 5.74.2

*Veröffentlicht am 16.10.2020*

## Webfrontend

*Verbessert*

* **Suche**: Die neue Tabellenansicht ist jetzt auch in Nebensuchen verfügbar.

*Behoben*

* **Mappen**: Gespeicherte Suchen wurden für Nutzer nicht geöffnet, die keine eigenen Mappen haben.
* **Drucken**: Die erzeugten PDF hatten in vielen Fällen zerstörtes Design.
* **Datamodel**: Speichern von lokalisierten Feldern beim ersten Anlegen von Mappen wurde repariert.

## Server

*Behoben*

* **Mappen**: Das Entfernen von Connector-Objekten wurde repariert.

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

## Auto-Keyworder

Das neue kostenpfplichtige Plugin [**Auto-Keyworder**](../../../en/webfrontend/datamanagement/features/keyword_plugin/) erlaubt eine Anbindung von Keyword Dienstleistern (aktuell nur [**cloudsight.ai**](https://couldsight.ai) zum automatischen Verschlagworten (Beschreibung, Keywords) von Bildern.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:d5f7a58adaac58a12222938ef95187f0bbdac4700131b1c3bfae21cf3ee6421e
docker.easydb.de/pf/eas                  sha256:e9c9ac0ad4a7edd7a0404bace2cdf4da84491cb841b6dfb17ddb9eb7af68e99c
docker.easydb.de/pf/elasticsearch        sha256:dcdffe49347544254e438029bcd5e784287842dfb4324c0ec4f2d96784bc2e7c
docker.easydb.de/pf/fylr                 sha256:8ff9ecc5244a497d7b5ebd59f34fa8592a949a4c5d3463dbe20c9148b178cfb8
docker.easydb.de/pf/postgresql-11        sha256:3e4f3df062810da94ec2feb7d54fa6c8aa271c600b57330086fe9c4c0623f0ff
docker.easydb.de/pf/postgresql           sha256:ba51aac137b64a3f5b79f29af94b98114994a34757d0f16885027f78b60c778c
docker.easydb.de/pf/server-base          sha256:06f89c57f7bee84a33b3312973bac58a246c5bb9e3029a87cf07c2ca0510650e
docker.easydb.de/pf/webfrontend          sha256:33cd085b7d5edf4281aa1ca3a83db6a445fe3d30848d77bc01141921e0ee865c
```

