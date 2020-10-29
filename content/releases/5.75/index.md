---
menu:
  main:
    name: "5.75 (Late Oktober 2020)"
    identifier: "5.75"
    parent: "releases"
    weight: -575
---

> Für dieses Release ist ein **Re-Index nötig**, bitte planen Sie entsprechende Zeit für das Einspielen des Updates ein. 
>
> Es wird ab diesem Release **keine Benutzer-Historie** mehr geschrieben, die existierende Historie (nur über die Datenbank erreichbar) wird mit diesem Release gelöscht.
>
> Ab Version **5.76** (erscheint geplant am **18.11.2020**) startet die **easydb** nur noch mit der neueren **PostgreSQL-Version 11**. Dieser Schnitt ist notwendig, um neue Funktionen von PostgreSQL nutzen zu können, ohne alte Installationen zu gefährden. Außerdem bekommt die alte PostgreSQL-Version keine Sicherheits-Updates mehr. Mehr Informationen im Abschnitt **[PostgreSQL 11](../5.73#postgres-11)**.

# Version 5.75.0

*Veröffentlicht am 28.10.2020*

## Webfrontend

*Neu*

* **Detail**: Für Reverse verschachtelte Objekte könner per Masken-Option **Tags** angezeigt werden.
* **Suche**: Anzeige von Optionen bei Gruppierung nach verlinkten Objekten.
* **PDF**: Einbindung des Browser-internen PDF-Viewers zusätzlich zu dem internen Viewer der easydb.
* **Expertensuche**: Die Suche nach Datumsbereichen hat jetzt die Möglichkeit zwischen dem unteren und oberen Datum in der Suche zu unterscheiden.

*Verbessert*

* Eine neue Anzeige von **#Neu** und **#Kopie** unterscheidet im Editor ob ein Datensatz kopiert oder neu angelegt wird.
* **Suche**: Bei der Anzeige der Anzahl der Treffer wird jetzt bei Eindeutigkeit der Name des Objekttyps mit angegeben.

*Behoben*

* **Typo3-Plugin**: Anpassung für Typo3 easydb Plugin [Version 1.4.0](https://docs.typo3.org/p/easydb/typo3-integration/1.4/en-us/AdministratorManual/). Mit dieser Version kommt es nicht mehr zu der Fehlermeldung *Request URI Too Long*.
* Fehler in der **Tabellenansicht** bei der Anzeige von tief verschachtelten Hierarchien korrigiert.
* Fehler bei der Anzeige von **Pools in Reverse** verlinkten Objekten im Editor korrigiert.
* **Connector**: Anzeige von Vorschauen für einige Fälle korrigiert.
* **Filter**: Die Filterung von Datumsbereichen wurde für einige Fälle repariert.
* **Expertensuche**: Bei Felder ungleichen Typs aber mit denselben lokalisierten Feldnamen konnte es zu Javascript-Fehlern kommen.

# Server

*Neu*

* **/api/xmlmapping**: Events `MAPPING_INSERT`, `MAPPING_UPDATE` und `MAPPING_DELETE`werden geschrieben.
* **/api/db**, **/api/search**: Ausgabe von `_tags`innerhalb von Reverse-verlinkten Objekten.

*Verbessert*

* **/api/db**: Für Datumsfelder werden Jahre mit vorangestelltem `+`akzeptiert.
* **/api/search**: Datumsfelder akzeptieren jetzt auch Timestamps mit Millisekunden.

*Beboben*

* Probleme mit **/api/suggest** nach dem Elasticsearch Update auf 7.x wurden behoben.
* **/api/collection**: Beim Verschieben von Collections wird der Besitzer der übergeordneten Collection übernommen.
* **Aktualisierungen vom Index** beim Entfernen von verlinken Objekten wurden verbessert.
* **/api/search**: Aggregation von Datum ohne Zeit wurde repariert.
* Das Systemrecht `system.user.default_needs_confirmation` wird jetzt beachtet.
* **Welcome**-Mail wird jetzt auch verschickt, wenn **Confirm**-Mail deaktiviert ist.
* **/api/export**: Versionsauswahl beim Export wurde korrigiert.
* **/api/search**: Suche nach Nichtexistenz von verlinkten Objekten wurde für komplexe Indices repariert.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome
sha256:f24a68195f7215c5fba3ab3d0dca910ead74cc6659a5b2b3cdf8fe912d8d10e2
docker.easydb.de/pf/eas
sha256:94266f584b75b6755a615ecb0141626c00265d7419747e883b7ab80878d715dc
docker.easydb.de/pf/elasticsearch
sha256:67891a41d3f83d0210607826957fc3f0469ab276b113fd49fd9911a28da451ab
docker.easydb.de/pf/fylr
sha256:e25c897842ca3c3f4ea4699729655bd5b8aa2f5314d87b27c9e1c8520ffcf4b0
docker.easydb.de/pf/postgresql-11
sha256:f9018e12f629da8466e69bdf9ea01b17b1a73413b297ddf600bff7c5f8ad6b7e
docker.easydb.de/pf/postgresql
sha256:61bd66bd6734f316af5ae139946b83d085ebe1a310450805d5456201692f5fed
docker.easydb.de/pf/server-base
sha256:0bba89bb97267b65f5585deec30a3ebd07cb4e8111dfbbf28ed8b03901a3ca41
docker.easydb.de/pf/webfrontend
sha256:d2d64f67dba57293deb95f830f3128ca9faba40c488c12cf745adcbc9881e60c
```

