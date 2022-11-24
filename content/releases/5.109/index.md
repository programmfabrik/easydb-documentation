---
menu:
  main:
    name: "5.109 (November 2022)"
    identifier: "5.109"
    parent: "releases"
    weight: -609
---


> Diese Version benötigt **keinen neuen** Index-Aufbau

> Mit diesem Release wurde die Funktion des endgültigen Löschens von Dateien auf dem easydb-Server von in der Software gelöschten Inhalten (Siehe [Release 5.97](/de/releases/5.90-5.99/5.97)) standardmäßig für alle easydbs (bereits im Betrieb genommene und neu installierte easydb) aktiviert.


# Version 5.109.0

*Veröffentlicht am 23.11.2022*


# Webfrontend

## Neu

* **Nutzer Manager**: Neue Expertensuche wurde hinzugefügt, Nutzer können jetzt nach Namen, Telefonnummer etc gesucht werden
* **Lokalisierung**: Spezielles Datums- und Zeitformat für die dänische Sprache hinzugefügt
* **Mappen**: Für das Teilen mit anonymen Nutzern wurde eine Spracheauswahl hinzugefügt

## Verbessert

* **Dateibrowser**: Der Dateibrowser verhält sich jetzt im Editor genau wie in der Detailansicht: wenn der Objekttyp kein Dateifeld hat, wird kein Dateibrowser angezeigt
* **Datemodelleditor**: Checks für die internen Namen von Objekttypen und Felder hinzugefügt, um zu verhindern, dass falsche Daten zum Server gesendet werden
* **Minisuche**: Suche nach verlinkten Objekten verbessert. Die Suche nutzt jetzt den Modus `fulltext`, um mehr passende Suchtreffer zu finden

## Behoben

* **Connector**: Bug behoben, der die Suchergebnisse bei mehreren verbunden Connector-Instanzen falsch dargestellt hat
* **Mappen**: Fehler beim Verschieben der Slides im Präsentationseditor behoben
* **Export**: Falsche Darstellung von exportierten Dateien im Exporter bei einer großen Anzahl von Datensätzen behoben
* **Detailansicht**: Fehler behoben, bei dem die Änderunghistorie falsch dargestellt wurde, wenn die Auswahl der Versionen von Datensätzen zu schnell geändert wurde
* **Minisuche**: Fehler in der Autovervollständigung behoben
* Fehler behoben, bei dem die Upload-Information im Editor nicht korrekt angezeigt wurden
* Doppelte Darstellung des Gruppeneditor-Eintrags im Kontextmenü von Suchergebnissen behoben
* Fehler behoben, bei dem Tooltips das Schließen von modelen Dialogen verhindern konnten


# Server

## Neu

* **Automatisches Löschen von Assets**:
  * Nachdem Assets in der easydb gelöscht wurden, werden sie endgültig vom easydb-Server gelöscht
  * Dieses Feature ist nun **standardmäßig aktiviert**
  * Die technische Variable `server/janitor/enable_asset_cleanup` ist nun **standardmäßig aktiviert**

## Verbessert

* **XML Mapping**: Nicht suchbare Felder können für XML Export Mapping ausgewählt und genutzt werden

## Behoben

* **Asset Versionen**: Konfiguration der Bitrate von hochauflösenden Videos behoben


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:c0f17ed1f925787b8eae7971c9a98ebea02c2a41e8d7df0a5fb520cd40c89a3c
docker.easydb.de/pf/eas                  sha256:f010d3d88650c1723f49383843f1a990d4e08aee18b66e914a31a56d806c0a64
docker.easydb.de/pf/elasticsearch        sha256:1fbb7466b69ec9bebff2e0340c4ca59d72d9c3b8faad99b72659c0aa45d3c58f
docker.easydb.de/pf/fylr                 sha256:50e3d9840a5707f003865b65c61d0f6f5890b12cdc1afd8530abe65d3ecf59ed
docker.easydb.de/pf/postgresql-11        sha256:69717d744cd8f2b666a0d9882259b2ca0ea96241b8764d9f2c05357d84489ea0
docker.easydb.de/pf/postgresql-14        sha256:d447e0b2e6abbbf45845192b983fff930d57dbb838159823a5ddf4f85b35a16b
docker.easydb.de/pf/server-base          sha256:9524a6ef51290ac362cdb71d43e366bff3586a12f93c90fd4a2710817723646d
docker.easydb.de/pf/webfrontend          sha256:8f9e2e1b6ac25711bc742fe5af9193e2bcac995ae765b4e504a6cd43c9810db2
```
