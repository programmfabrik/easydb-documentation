---
menu:
  main:
    name: "5.68"
    identifier: "5.68"
    parent: "releases"
    weight: -568
---

> Dieses Release benötigt keinen Re-Index.

# Version 5.68.1

*Veröffentlicht am 09.06.2020*

### Webfrontend

*Neu*

* **CSV-Importer**: Mapping von Tags und Pools wird unterstützt.

# Version 5.68.0

*Veröffentlicht am 03.06.2020*

### Webfrontend

*Verbessert*

* **JSON-Importer**: Verbesserungen in der Bedienung und der Anzeige.

*Behoben*

* **Neue Objekte**: Tags aus der Vorlage wurden nicht bei der Masken-Auswahl für die einzelne Objekte berücksichtigt, was zu falschen fehlenden Rechte Warnungen führen konnte.

### Server

*Neu*

* Vorbereitung für neue Webfrontend-Sprachen: **Polnisch, Russisch, Tschechisch**.

*Verbessert*

* XML-Export: `_standard.1.eas`wird zusammen in `_standard`exportiert.
* **Geschwindigkeitsverbesserung** beim Speichern von Pools wenn viele Maskenrechte überprüft werden müssen.

*Behoben*

* **Export**: In einigen Fällen konnte es passieren dass zeitlich gesteuerte Exporte nicht mehr ausgeführt wurden, weil die zugrundeliegende Session abgelaufen war.
* **Suche**: Die Suche nach offenen Datumsbereichen wurde repariert.
* **CSV-Importer**: Fehlerbehebung im Zusammenhang mit verlinkten Objekten für die Pool-Management aktiv ist.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:a86f879e38d32f16d86a4e04a0d62bc5410da43eed617ebefbc30e8c320c9ffe
docker.easydb.de/pf/eas                  sha256:13a29e8675a041c008692aefbf9d3e669e3a495f925ce06542fcdd8beb51c8e1
docker.easydb.de/pf/elasticsearch        sha256:d188c3c26a3abcebb4c40ab197220991bdfc052d3bc0599ddfddcf66c9fe61f4
docker.easydb.de/pf/fylr                 sha256:2a0eb8bda0c0ca08d1f9b21dd1e8ebda4e0c630672cb7201c9f53cb0a82db6d4
docker.easydb.de/pf/postgresql-11        sha256:3cdc08443ea30f7265d1fdc135712f040ba245092e8feeebc5d93fbbf54b952a
docker.easydb.de/pf/postgresql           sha256:4f172a604c30e0395f40012c83cc05e7e6ef6f572a982cae3d59b0a35a643854
docker.easydb.de/pf/server-base          sha256:a41ea4691d727f892b40ba17f4bd2c8361a9be2dc96d725ec74150c11dc8dada
docker.easydb.de/pf/webfrontend          sha256:6f73ec1db4ac2947b165ff4eb86efc8c016184c940cbaacef110716f5f3b359c
```

