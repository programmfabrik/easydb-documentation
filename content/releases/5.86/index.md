---
menu:
  main:
    name: "5.86 (Anfang Juli 2021)"
    identifier: "5.86"
    parent: "releases"
    weight: -586
---

> Für dieses Release ist ein **Re-Index nötig**, bitte planen Sie entsprechende Zeit für das Einspielen des Updates ein. 

# Version 5.86.2

*Veröffentlicht am 21.07.2021*

## Webapp

### Verbessert

* **Detail**: Die Darstellung der URL in der Teilen-Anzeige wurde verbreitert.

### Behoben

* **Mappen**: Die Auswahl (mit ALT) von Objekttypen die nicht in der Hautsuche angezeigt werden wurde für die Konfiguration des Hochladens ausgestellt, da Objekte in solchen Objekttypen nicht in Mappen gesammelt werden können.
* **Plugin custom-mask-splitter-detail-linked**: Das für die Anzeige verdendete Datenmodell war fälschlicherweise das Entwicklungsmodell aber nicht das Aktuelle.
* **Suche**: Die Auswahl eines Unterpools im Filter konnte in einigen Datenbanken nicht durchgeführt werden.
* **Suche**: Das Auswahl-Menü Resourcen konnte den Spezialfall von nur einem Objekttyp ohne Pool nicht korrekt anzeigen.

## Server

### Behoben

* Mappen: Fehler beim Verschieben von Mappen zwischen verschiedenen Benutzern behoben.

# Version 5.86.1

*Veröffentlicht am 13.07.2021*

## Webapp

### Behoben

* **Suche**: Ein Rekursionsproblem im Filtertree wurde behoben
* **Datenmodell**: Ein Fehler führte beim Kopieren von Objekttypen mit einem Reverse-verlinktem Objekttyp zu einer illegalen Duplizierung des Reverse-Maske. Dieser Fehler hatte kein sichtbaren Auswirkungen.

## Server

### Behoben

* **Index**: Indizierung von Datumsbereichen für den Filtertree wurde behoben.

# Version 5.86.0

*Veröffentlicht am 07.07.2021*

## Webapp

### Neu

* **Detail**: In der Anzeige gibt es jetzt Vor- und Zurückbuttons.
* **Datenmodell**: Unterstützung eines Kontextmenüs beim Erstellen.
* **Pool- / Gruppenmanager**: Anzeige von Änderungs- und Erstelldatum.
* **Detail**: Im Teilen-Menü wird jetzt ein Button zum Aufruf der Links angezeigt.
* Beta: Unterstützung von **gemeinsamen Filtern** (nur im Debug-Modus).

### Verbessert

* Umstellungen beim Tastatur-Fokus für **verbesserte Barrierefreiheit**.
* **Editor**: Die Vorschauleiste kann jetzt in der Breite manuell verstellt werden.
* **CSV-Importer**: Unterstützung zum Leeren von Feldern.
* **Layoutverbesserungen** bei den Systemrechten, im Druckdialog und in der Basiskonfiguration (Letzteres nur easydb 6).

### Behoben

* **CSV-Importer**: Importe von Zeitstempeln mit Zeitzone führen nicht mehr zu einem Fehler.
* **Schnellzugriff**: Beim Filtern von einigen Mapentypen konnte es zu Javascript-Fehlern kommen.

## Server

### Neu

* `pool`und `group`Objekte haben neu einen `created_timestamp`und`last_updated_timestamp`.

* **Datumsbereichsfelder** können über `:middle`die Mitte der Daten aggregieren und suchen.
* **Build-Info** für Plugins wird generiert.
* Support für **Postgres** Version **12** und **13**.

### Verbessert

* **Beschleunigung** beim Laden von **Mappen**.
* Warnung beim **Löschen von Metadaten-Mappings** welche in Verwendung sind.
* Filter für **Datumsbereiche** arbeiten jetzt mit der Mitte des Bereichs.

### Behoben

* **XML-Export**: Ausgabe von EAS-URL auch in verlinkten Objekten.
* **CSV-Export**: Ausgabe von `_standard` wurde bei manueller Feldauswahl nicht korrekt durchgeführt.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version): 

```ini
docker.easydb.de/pf/chrome               sha256:dec745a2f97ff54e3fb34289c0ac5abc368bc8dcbb95ec93fe6124d35c9574c5
docker.easydb.de/pf/eas                  sha256:18f3f17f11d865a1ad953d36541747dde4fb1363a0e8e2174f5a23989c3dd768
docker.easydb.de/pf/elasticsearch        sha256:01564b2dbaf9cb2d7d1666fd2d954ffc61cf0bde2ea6a598330a31c5ab0e56a4
docker.easydb.de/pf/fylr                 sha256:386ee9ef4249ebda216bc4818d09fc84cd3f94ce062ceb2c0c64941b5cb58612
docker.easydb.de/pf/postgresql-11        sha256:4454c79b53e696726507f934be08705ef16916641548d922186838b83f993309
docker.easydb.de/pf/server-base          sha256:1cb11fbc288e89513be11ff635028556a7ba9c7ca72b9e5eb38e3c74c881a0f4
docker.easydb.de/pf/webfrontend          sha256:005dc15b9428f22e6db4b321632cde4ed35934b020825a8ec49d52694f19ad35
```

