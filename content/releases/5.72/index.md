---
menu:
  main:
    name: "5.72 (September 2020)"
    identifier: "5.72"
    parent: "releases"
    weight: -572
---

>Dieses Release benötigt **keinen Re-Index**.

# Version 5.72.0

*Veröffentlicht am 27.08.2020*

## Webfrontend

*Neu*

* Laden vom mehrer Versionen beim **Download** wird unterstützt.
* Standard-Design aus dem Maskeneditor entfernt.
* Mappen: Die **Auswahl des Pools** beim Erzeugen von neuen Objekten nach dem Hochladen wird unterstützt.

*Verbessert*

* Laden von Bildern erfolgt jetzt erst dann wenn es nötig ist (Lazy Loading).
* Tabellenansicht zeigt jetzt auf Wunsch die **Hierarchie** an.

*Behoben*

* Verbesserung im Menü zum Laden eines Bildes in der Vorschau.
* Anzeige von lokalisierten Namen im **CSV-User-Importer** wurde repariert.
* Fehlerbehebungen für die neue **Tabellenansicht**.
* **Mappen**: In einigen Rechtemanagement-Einstellungen konnte es zu einem fehlerhaften Verhalten des `+`-Buttons kommen.
* **Detail**: In einigen Rechtemanagement-Einstellungen konnte es zu einem Fehler beim Laden des Details kommen.

## Server

*Neu*

* **/api/mask**: `standard_design` Parameter wurde aus der API entfernt. Dieser Parameter wurde vom easydb Webfrontend nicht benutzt.
* **/api/collection**: Neuer Parameter `linked_pool_id`. Der Parameter setzt den Pool für verlinkte Objekte die beim Erstellen innerhalb der Mappe  benutzt wird.

*Behoben*

* Fehler im **Gruppeneditor** im Zusammenhang mit Tags & Pool behoben.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:268fc098104f2ae58f234df2abda856f7c2fe2ae9f0ac36e689ca3a3ada16d0a
docker.easydb.de/pf/eas                  sha256:c918d1320423f6adcd9f2ae438537966e225c643a6f6521c81cd5bd4daa45c33
docker.easydb.de/pf/elasticsearch        sha256:96136e2cf3440534f8ffc111888b08bae64c02fc5558ec114f0064b9b19e1372
docker.easydb.de/pf/fylr                 sha256:6b435119b593be668dc91e6479af390e8d02f8ba7ef99faeeb553e86af9c71c9
docker.easydb.de/pf/postgresql-11        sha256:fe6fd87ace569e9f30f3e1b4c6eb89744fb2691fa651e89c0b6bdcd804bba43a
docker.easydb.de/pf/postgresql           sha256:6be6074fec5abb39400dbbbf12bdcac48beb92e3b1292027f91eebfdfe40209c
docker.easydb.de/pf/server-base          sha256:ec9eb2cab24ef6014f8adcca1aae39f9582b3539724311cb933071011a8d5790
docker.easydb.de/pf/webfrontend          sha256:885485270ebd444bcdbabe790d113e22845e752bfb6c983c8d7beb2164a1ef38
```

