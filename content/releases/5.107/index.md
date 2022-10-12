---
menu:
  main:
    name: "5.107 (Oktober 2022)"
    identifier: "5.107"
    parent: "releases"
    weight: -607
---

> Dieses Update erfordert einen Re-Index, planen Sie entsprechende Downtime / Updatezeit ein

# Version 5.107.0

*Veröffentlicht am 12.10.2022*


# Webfrontend

## Neu

* **CSV Import**: Unterstützung für revers verlinkte Objekte

## Behoben

* **Nutzermanager**: der root User kann nicht mehr deaktiviert werden
* **PDF Creator**: leere Felder werden nicht mehr gespeichert, um den benötigten Speicherplatz im Server stark zu verringern
* **Connector**: Problem beim Zugriff auf entfernte Instanz mit anonymer Anmeldung behoben
* **Schlüsselwortverlinkung per Drag and Drop im Schnellzugriff**: Der Zähler für verlinkte Schlüsselworte wird automatisch aktualisiert
* Design Bug im Sprachauswahlmenü behoben


# Server

## Neu

* **Objekt-Standard**:
  * Die Linktiefe von verlinkten Objekten, die im Standard inkludiert werden, kann limitiert werden
  * Um die Limitierung zu aktivieren, setzen Sie die Server Variable `debug/limited_standard_depth` auf `true` (der Defaultwert ist `false`, aktuell gibt es kein verändertes Verhalten im Vergleich zu älteren Versionen)

## Verbessert

* **Anmeldung**: Nutzer vom Typ `anonymous`, `ldap` und `sso` können die Anmeldung mit Nutzernamen und Passwort nicht mehr nutzen
* **Assetversionen**: Displayname der Version `full` wurde geändert zu "Original (formatted)"



# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:4f3ec61075c605b674340179f4a2630be6ab903aa3f1ca6b7b54f00a15ee2f1c
docker.easydb.de/pf/eas                  sha256:b8a405baf379d185c93f32763cd8eee67246fd34f02847003f37aad8c60358e9
docker.easydb.de/pf/elasticsearch        sha256:60d4a819ab5311f6fa6d8d7c0a9e4a89eff7dad1d2e016d8a286370893bf51e6
docker.easydb.de/pf/fylr                 sha256:df80ddc7ea48cebeff89bd88b51c6da531bd1b0d5676f87c79b269cc9f586b9a
docker.easydb.de/pf/postgresql-11        sha256:95a52158929dd466bc6d2fd86c22c2ed17c2486005387bb79b80697a0650c170
docker.easydb.de/pf/postgresql-14        sha256:35aa4a484a832850e0d17e6ce6efcc3dc37e5d601102ac54db6edf77dd17c896
docker.easydb.de/pf/server-base          sha256:d62a82ed973537df46a735f155f186215f4d58bd00aa55ec6bacf2d93237d446
docker.easydb.de/pf/webfrontend          sha256:4609b8d8d52122d1a7be1c213640388bbafa78bd2b3eb72a7a83fcb1935015fe
```
