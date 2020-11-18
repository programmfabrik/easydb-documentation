---
menu:
  mainWEG:
    name: "5.76 (November 2020)"
    identifier: "5.76"
    parent: "releases"
    weight: -576
---

> Dieses Release bringt die angekündigte zwingende **Anwendung von Postgres 11**.
>
> Es wird kein Re-Index benötigt.

# Version 5.76.0

*Veröffentlicht am 18.11.2020*

## Webfrontend

*Neu*

* Detail: Im Debug-Modus können Objekte als JSON direkt per Klick geladen werden (neben String-Feldern)

*Verbessert*

* Design der Suche, Detail und Editor wurde bei der Ausgabe von der Standard Info vereinheitlicht.
* Gruppenmanager: Ausgabe des Typs der Gruppe im Formular.
* Basis-Konfiguration: Die Ausgabe der Server-Config wurde entfernt.
* Adminbereich: Alle Bereiche haben jetzt einzelne Überschriften für die jeweiligen Teile der Anzeige.
* Filter: Felder die rechtegemanagt sind werden nicht mehr angezeigt (Tagfilter werden ignoriert) .
* Plugin Editor-Tagfilter-Defaults: Das Befüllen von Nur-Lesen-Felder wird jetzt unterstützt.
* Plugin Auto-Keyworder: Small fix when having the connector activated.
* Plugin Connector: Fixes when downloading multiple files and in the aggregations of pools.
* Plugin Connector: Implemented wrapping of EAS API.

*Behoben*

* Autovervollständigung zeigt für verlinkte Objekte keine Duplikate mehr an.
* Datenmodell: Vorschau im Editor des aktuellen Modells wurde repariert.
* Poolauswahl: Für einige Nutzer hat die Sortierung von Unterpools nicht korrekt funktioniert.
* Detail: Plugins können die Info-Bar nicht mehr überdecken.
* Detail: Anzeige von Versionen mit GPS-Koordinaten in erweiterten Information wurde behoben.
* Detail/Editor/Text: Versteckte Tags werden jetzt nicht mehr angezeigt, wenn es die Maske nicht erlaubt.

## Server

*Verbessert*

* Postgres 11 ist erfoderlich, sonst startet easydb nicht mehr.
* Datenmodell-Fehlermeldungen wurden verbessert.

*Behoben*

* Mappen: Das Löschen von hierarchischen Objekten war in bestimnmten Konstellationen nicht möglich und wurde von der Datenbank untersagt.

