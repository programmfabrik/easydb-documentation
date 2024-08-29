---
menu:
  main:
    name: "5.136 (August 2024)"
    identifier: "5.136"
    parent: "releases"
    weight: -636
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.136.0

*Veröffentlicht am 29.08.2024*

# Webfrontend

## Neu

- **Masken**: Feld zum Setzen von Platzhalter für Custom-Felder
* **Masken**: Option zum Verstecken des ersten leeren Eintrags in verschachtelten Tabellen

## Verbessert

* **Datenmodell**: Fehlermeldung beim Versuch, einen anderweitig benutzten Objekttyp zu löschen, verbessert
* **Default-Values-Plugin**: Unterstützng für Bool-Felder in `editor-tagfilter-defaults-plugin`
* **Editor-Templates**: Check des Namens auf doppelte Vergabe
* **Objectstore**: Unterstützung für Pull-Only-Instanzen
* **Zeitplaner**: Erkennung von ungültigen Kombinationen von Angaben
* **Filter-Panel**: verbessertes Verhalten von hierarchischen Filtern, wenn der OR-Operator verwendet wird
* **Ereignisse**: verbesserter Dateiname beim Export als Liste

## Behoben

* **Volltext-Vorschläge in Expertensuche**: Wildcards werden jetzt korrekt hinzugefügt
* **Detail**: inkorrekte Darstellung von Hierarchien behoben
* **Filter**: Problem bei Darstellung von Tags ohne Namen behoben

# Server

## Verbessert

* `/api/db?all_versions`: Hierarchietiefe als `_level` für jede Version hinzugefügt
* Erweiterungen im Auto-Keyworder-Plugin

## Behoben

* Fix für spezielle Metadaten-Typen, die Fehler bei der Vereinnahmung hervorriefen

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.136.0            sha256:841f65883c90252a73ab1a101c88f76b9842ffb6275be7460cb52b32b5be3b81
docker.easydb.de/pf/elasticsearch:5.136.0  sha256:1480fbb397bd5258dbed1c4275003696b8b862542bcd754449ae941e602dae04
docker.easydb.de/pf/fylr:5.136.0           sha256:78fbe5dfda52339fe92609e3c1a033be3fa6bcac7944ace3ad5a3eb24dbf1c89
docker.easydb.de/pf/postgresql-14:5.136.0  sha256:f50d2d5759520962f49c49f68eb14c1541691de955f169ab22dba64fd9cf8325
docker.easydb.de/pf/server-base:5.136.0    sha256:c4a7fe799f934a6d7b4e096703dc1e8b708e8f9cce59bd45ed02d153b246d577
docker.easydb.de/pf/webfrontend:5.136.0    sha256:a2a3a209d7c892f5f24352198d36a162b5722eec8439fd8d11553ff785f3f21a
```
