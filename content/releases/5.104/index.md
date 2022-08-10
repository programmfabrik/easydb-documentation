---
menu:
  main:
    name: "5.104 (August 2022)"
    identifier: "5.104"
    parent: "releases"
    weight: -604
---

> Dieses Update erfordert einen Re-Index, planen Sie entsprechende Downtime / Updatezeit ein

# Version 5.104.0

*Veröffentlicht am 10.08.2022*

# Webfrontend

## Neu

* optionale Unterstützung für Deeplinks mit System ID


## Verbessert

* **Nutzer-/Gruppenmanager:**
  * Suche nutzt jetzt immer den `wildcard` Modus, dadurch wird die Suche insgesamt nutzerfreundlicher
  * Problem behoben das verhindert hatte, dass die gesamte Liste angezeigt wird, wenn der Text im Suchfeld gelöscht wurde
* **Export:**
  * existierende Export-Templates werden nicht automatisch geladen
  * Default-Wert für `batch size` für CSV Export wird gesetzt
* **Expertensuche:** Suche nach Dateinamen mit Wildcards verbessert
* **PDF Creator:** Gespeicherte Datenmenge im `custom_data` wurde deutlich reduziert
* Neue Tooltips für dynamische Menüeinträge für Objekttypen

## Behoben

* **Datumsbereichfelder:** automatische Generierung der textlichen Darstellung deaktiviert, wenn  `from` und `to` gesetzt sind
* Link zu `/login` gefixt
* **Asset Browser:** Corner Case behoben, bei dem Bilder nicht angezeigt wurden, wenn keine `standard` Version existiert
* Lokalisierung für Text mit URL-enkodiertem Inhalt behoben
* **Präsentation Download:** Probleme behoben, die auftreten wenn das Folienlauyout geändert wurde und die Präsentation heruntergeladen wurde, ohne vorher zu speichern

# Server

## Neu

* **Transitions/Workflows** neue Kommentarfeld, um den Workflow zu beschreiben
* **Detail URL:** in der Basiskonfiguration kann zwischen dem alten Format mit der System ID und dem neuen Format, das die UUID nutzt, umgeschaltet werden
* **Expertensuche:** die Dateinamensuche wurde verändert, so dass jetzt rechtstrunkierte Suchen mit Wildcards möglich sind

## Verbessert

* **Extension Plugins**:
  * für Plugins mit API Callbacks gibt es einen eigenen URL-Pfad `plugin/extension/`, anstatt nur `plugin/base/` wie bisher
  * Siehe auch [API Callbacks](/en/technical/plugins/#api-callbacks)
* **Rechtemanagement:** Nutzern/Gruppen kann das Recht gegeben werden, Nutzer aus `sso`, `ldap` Gruppen zu sehen.

## Behoben

* **Datei Upload:** die externe URL des EAS `eas.external_url` wird für Asset-URLs genutzt
* **Änderungshistorie:** inzwischen gelöschte Pools werden nicht versucht zu laden

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:2c0222ed258b40a21739b877e4684796bee62cca99a09bf74e668f40a1450327
docker.easydb.de/pf/eas                  sha256:e3350e816f03bb10f27f741d7124d287b0d943fd9e5e6b2f22d533ae28fcf621
docker.easydb.de/pf/elasticsearch        sha256:fc72ee8ec1ac3a27827a9b39b2cc921c0e659e0fc2d8e8126ad4d151c45b4624
docker.easydb.de/pf/fylr                 sha256:4a4feaf64f65a343be1e0de140b4470d53ebb7e7c723749fea79b53f17a32e63
docker.easydb.de/pf/postgresql-11        sha256:f2134eb9225dd2f7277f5c3d1d18b6bf76f7510828eb9eb9f5f194ee81625099
docker.easydb.de/pf/postgresql-14        sha256:459318519972b451bcefc425d04c9718e37bffd2c27130999744d4f696ee26d4
docker.easydb.de/pf/server-base          sha256:f5161d65d8fdb38b3c9439a83bb10e4377e292aa491c558ba17ff5f2f3de5be8
docker.easydb.de/pf/webfrontend          sha256:f4c5da770996b74b4ccaa329b94bfe4643d46fd6aef1a77bf42770b0000f2aad
```
