---
menu:
  main:
    name: "5.78 (Januar 2021)"
    identifier: "5.78"
    parent: "releases579"
    weight: -578
---

> Für dieses Release ist ein **Re-Index nötig**, bitte planen Sie entsprechende Zeit für das Einspielen des Updates ein. 

# Version 5.78.0

*Veröffentlicht am 13.01.2021*

## Webfrontend

*Neu*

* CSV-Importer: Das Ersetzen von Tags mittels CSV-Importer wird unterstützt.

*Verbessert*

* Suche: Deep-Links in die Suche wurden etwas verkürzt.
* Design: Verbesserte Ausgabe der Standard-Info der Objekte.
* HTML-Editor: Verbesserungen und Fehlebehebungen.

*Behoben*

* Druck: Fehler beim Erzeugen des PDF wurde behoben.
* Mappen: Auswahl von allen Mappenelementen wurde repariert.

## Server

*Neu*

* Dauerhaftes Speichern von konfigurierbaren **Nutzerinformationen** im Eventlog.

*Verbessert*

* **Dateinamen-Templates** können jetzt Datumsfelder enthalten.
* Verbesserte Fehlermeldung beim Speichern von **zirkulären Referenzen** im Gruppeneditor.

*Behoben*

* Möglicher überflüssiger Transaktionsverbrauch im **Suggest-Index** vermieden.
* Indexierung von **Volltextfeldern** in einigen Fällen behoben.
* Das Speichern von mehreren **bidirektionalen** Beziehungen auf oberster Ebene wird jetzt unterbunden.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:3b0d0e3b97be2fc7129f29f56434608f6fcb3a213b2f7cfe042eccd6adbe6d0b
docker.easydb.de/pf/eas                  sha256:4765219fe3ac76a3bc05e27b28bbfab864e7db4bd2daaacd4c097397ea077bd7
docker.easydb.de/pf/elasticsearch        sha256:2c61c8d9096a741cadaa496861ae13bdc4ce808995710a2849c29e25160350c3
docker.easydb.de/pf/fylr                 sha256:efd5728211e52119f63f2d24e41abaa62692a310aa59857c801b1ad3e8db7a58
docker.easydb.de/pf/postgresql-11        sha256:98756185f6e1995f6cf64f46d1190968f771311967187dd5bf5c433157517290
docker.easydb.de/pf/server-base          sha256:967411bcc87aae646295a1c8b9dbe7152182232af8598676ef80c1addaf60ed0
docker.easydb.de/pf/webfrontend          sha256:ef2cc9c6a468200268cf569c5f010fe560a1b9efb9dee4cd39ea5425d5bacf95
```

