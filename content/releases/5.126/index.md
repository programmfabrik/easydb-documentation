---
menu:
  main:
    name: "5.126 (Dezember 2023)"
    identifier: "5.126"
    parent: "releases"
    weight: -626
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

> Ein neues Feature im Easydb Asset Server wird einmalig einen Abgleich der Versionen verursachen, der einmalig mehr Last erzeugen kann

# Version 5.126.0

*Veröffentlicht am 13.12.2023*


# Webfrontend

## Neu

* **Editor**: Das Verhalten von Mehrfachfeldern, die als "Nur anhängen" konfiguriert sind, wurde verbessert:
  * die Zeilen, die bereits in der Tabelle existieren, werden als schreibgeschützte Felder angezeigt
  * nur das Hinzufügen neuer Felder wird erlaubt

## Verbessert

* **Design**: Es wurden zahlreiche Korrekturen und Anpassungen im CSS vorgenommen

## Behoben

**Editor für Metadaten-Mapping**: Es wurde ein Problem behoben, bei dem einige Tags nicht korrekt angezeigt wurden
* Ein Fehler in den Berechtigungseinstellungen für geteilte Mappen (Collections) wurde behoben
* Es wurde ein Problem behoben, bei dem Server-Parameter manchmal fälschlicherweise in URLs für freigegebene Objekte enthalten waren


# Server

## Neu

**Easydb Asset Server**: neue Funktion, die den Zugriff auf Dateien innerhalb von Archiven ermöglicht
  * Es ist nun möglich, auf Dateien innerhalb von Archiven zuzugreifen, indem die `versions.directory.url` mit dem Dateinamen verkettet wird
  *Dies löst neue Versionsberechnungen aus, die vorübergehend zu einer höheren Belastung des Easydb Asset Servers führen können*

## Verbessert

* **Standard**: Nur die erste Datei im `eas`-Teil des Standards wird gerendert, um den Datenverkehr zu reduzieren und die Leistung zu verbessern

## Behoben

* Fehler in der Selbstregistrierung für neue Benutzer behoben


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.126.0         sha256:ab51d95640f8e0f608ed26015a30f19e5e25534d1224a972b8b381def9b99fdd
docker.easydb.de/pf/eas:5.126.0            sha256:1d572a161595ec5267fbe35a913cf4b229ec638084fbab17f1075d4bdc0289ab
docker.easydb.de/pf/elasticsearch:5.126.0  sha256:3092714720e3e3eca85106941aefc305152edc13e044383ecc6f99faf7b82664
docker.easydb.de/pf/fylr:5.126.0           sha256:db47b3a6ad0bef5e8d881006812a56974a133badcb041b5defd782e2b5c4ba0b
docker.easydb.de/pf/postgresql-14:5.126.0  sha256:c1d3b7882cdb4ea9a3293ae0d6bea21417e20ffc2e133f6274afeba72409e0c8
docker.easydb.de/pf/server-base:5.126.0    sha256:d4412665a021f9c51d58d12c50b70164190f6dc69a69e9cda2ecd8297a764aff
docker.easydb.de/pf/webfrontend:5.126.0    sha256:b69aba45095acf6941bd548ec33e1ce1d479eccd6e9da2edbf9484b5ce4c6f7f
```
