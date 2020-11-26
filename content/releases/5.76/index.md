---
menu:
  main:
    name: "5.76 (November 2020)"
    identifier: "5.76"
    parent: "releases"
    weight: -576
---

> Dieses Release bringt die angekündigte zwingende **Anwendung von Postgres 11**. Mehr Informationen im Abschnitt **[PostgreSQL 11](../5.73#postgres-11)**.
>
> Es wird kein Re-Index benötigt.

# Version 5.76.2

*Veröffentlicht am 26.11.2020*

## Webfrontend

*Behoben*

* **Datenmodell**: Speicherproblem beim Umschalten im Masken-Editor behoben.
* **Suche**: Anzeige von verlinkten Objekten in der Tabellenansicht wurde repariert.
* **Suche**: Fehlerhafte Druckansicht wurde korrigiert.
* **Suche**: Indikator für Bildserien wurde repariert.
* **Suche**: Fälle in denen das Lasso unsichtbare Objekte selektiert hat wurde repariert.
* **Suche**: Korrekturen bei der Sichtbarkeitslogik für Standard Info.

# Version 5.76.1

*Veröffentlicht am 23.11.2020*

## Webfrontend

*Behoben*

* **Suche**: Anzeige der Standard-Info in Standard- und Text-Ansicht wurde repariert. Die Option ist jetzt bei allen Nutzern aktiviert und muss ggfs. de-aktiviert werden.
* **Detail**: Anzeige des Menüs bei reverse verlinkten Objekten wurde wiederhergestellt.
* **CSV-Importer**: Speichern bei bestimmten Tag-Konstellationen wurde repariert.

# Version 5.76.0

*Veröffentlicht am 18.11.2020*

## Webfrontend

*Neu*

* **Detail**: Im Debug-Modus können Objekte als JSON direkt per Klick geladen werden (neben String-Feldern).

*Verbessert*

* Design der Suche, Detail und Editor wurde bei der Ausgabe von der Standard-Info vereinheitlicht.
* **Gruppenmanager**: Ausgabe des Typs der Gruppe im Formular.
* **Basis-Konfiguration**: Die Ausgabe der Server-Config wurde entfernt.
* Adminbereich: Alle Bereiche haben jetzt einzelne Überschriften für die jeweiligen Teile der Anzeige.
* **Filter**: Felder die rechtegemanagt sind werden nicht mehr angezeigt (Tagfilter werden ignoriert) .
* **Plugin Editor-Tagfilter-Defaults**: Das Befüllen von Nur-Lesen-Felder wird jetzt unterstützt.

*Behoben*

* **Autovervollständigung** zeigt für verlinkte Objekte keine Duplikate mehr an.
* Datenmodell: Vorschau im Editor des aktuellen Modells wurde repariert.
* **Poolauswahl**: Für einige Nutzer hat die Sortierung von Unterpools nicht korrekt funktioniert.
* Detail: Plugins können die Info-Bar nicht mehr überdecken.
* **Detail**: Anzeige von Versionen mit GPS-Koordinaten in erweiterten Information wurde behoben.
* **Detail/Editor/Text**: Versteckte Tags werden jetzt nicht mehr angezeigt, wenn es die Maske nicht erlaubt.
* **Plugin Connector**: Mehrfachdownload, Pool-Filter, Zusammenspiel mit Plugin Auto-Keyworder, Anzeige von Versionen wurde für betroffene Fälle repariert.

## Server

*Verbessert*

* **Postgres 11** ist erfoderlich, sonst startet easydb nicht mehr.
* Datenmodell-Fehlermeldungen wurden verbessert.

*Behoben*

* Mappen: Das Löschen von hierarchischen Objekten war in bestimmten Konstellationen nicht möglich.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:f24a68195f7215c5fba3ab3d0dca910ead74cc6659a5b2b3cdf8fe912d8d10e2
docker.easydb.de/pf/eas                  sha256:1143ce8cfbdff9ae602df7163150b34833637ae41600ebef5e164adc000e9202
docker.easydb.de/pf/elasticsearch        sha256:daf032af6c43c8b7a63797525478ad31d04a7e57924324089fd990c1b1de98d9
docker.easydb.de/pf/fylr                 sha256:e6a341d8c92f23027241e26f71ed811f65fd8176a133da0c92010405f9e8e13f
docker.easydb.de/pf/postgresql-11        sha256:188046e6935796f66037a9a9f6788ba7962160664dc5bcdcfdca4d7fe9ca04e7
docker.easydb.de/pf/postgresql           sha256:909a680aea9d5475570e089ca8e8cc8ebdc0c4e9c76c28789d1936795ed77715
docker.easydb.de/pf/server-base          sha256:18dd210b7816e6da94f39ff20480c87161d83530ec26f42608f5cff09d640a65
docker.easydb.de/pf/webfrontend          sha256:eacebeb05921632d76a5eca999a920f329bc413bf7287983c6805866cd40c95c
```
