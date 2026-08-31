---
menu:
  main:
    name: "5.155 (Ende Juli 2026)"
    identifier: "5.155"
    parent: "releases"
    weight: -655
---

> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.155.1

*Veröffentlicht am 31.08.2026*

# Server

## Behoben

* Fehler behoben, der die XSLT-Transformation einzelner Objekte verhindert hat.
* Bei Speichermangel konnte es vorkommen, dass der easydb-Server andere Prozesse des verwendeten Nutzers (`www-data`, PID 33) mit beendet hat.

# Version 5.155.0

*Veröffentlicht am 29.07.2026*


# Webfrontend

## Verbessert

* **Editor**: Verschieben eines Datensatzes in einen anderen Pool entfernt (nach einer Warnung) die Tags, die im neuen Pool nicht erlaubt sind.
* **Metadaten-Mapping**: ungültige Tags werden markiert und blockieren das Speichern, statt einfach entfernt zu werden.
* **Suche**: merklich schnellere Darstellung großer Ergebnisseiten.
* **Detail**: Beschleunigung bei der Darstellung von reverse-verlinkten Objekten
* **Editor**: verbesserte Darstellung von Pflichtfeldern bei verlinkten, verschachtelten und Asset-Feldern.
* **Asset-Browser**: Wenn die bevorzugte Asset-Variante geändert wurde, wird auch die Standard-Ansicht direkt aktualisiert.


## Behoben

* **Editor**: Übersetzung von Tab-Titeln und Vorschau-Spalten bei Templates
* **Suche**: Vorschläge, die zu keinem Ziel führen, werden nicht mehr angezeigt
* **Suche**: Hinzufügen zu Collection auch möglich, wenn man noch keine Collections angelegt hat
* **Suche**: Rechtsklick auf Datensatz lädt die Seitenleiste nicht mehr neu
* **Expertensuche**: funktioniert wieder, wenn kein Objekttyp ausgewählt ist
* **verlinkte Objekte**: ein Wert, den der Nutzer nicht sehen darf, wird beim Speichern behalten
* **Detail**: Schließen und Öffnen des Wurzeleintrags öffnet nicht mehr die gesamte Hierarchie
* **Übergeordneter Eintrag**: Link funktioniert wieder, auch wenn der Eintrag im Short-Format dargestellt wird
* **Suchergebnis**: Platzhalter und Abstände für Datensätze ohne Asset korrigiert
* **Text-Felder**: überlanger Text läuft nicht mehr aus dem Feld
* **Datenmodell**: Namens für neue Masken korrigiert, die nicht die Standardmaske sind
* **Tags**: Speichern von Tags und -gruppen ohne Namen nicht mehr möglich
* **Collections**: Firefox versucht nicht mehr, den Collection-Filter mit dem Nutzernamen zu befüllen

# Server

## Verbessert

* `debug/max_core_size` (Default 0) wirkt jetzt auch im Vordergrund-Modus (z.B. im Docker-Container), vorher war dort die Systemvorgabe aktiv. Dies verhindert, dass unerwünschte Core-Dateien im Container angelegt werden.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.155.0            sha256:09a2e335e68282c8d24d8d48282bd36ca2b969cc5f6c3e0bef0f2c115e56f58c
docker.easydb.de/pf/elasticsearch:5.155.0  sha256:8bbeee2e9f415f92bcab25ebc573ac3dea1dce6ad31e22925d91c93aa54e8507
docker.easydb.de/pf/fylr:5.155.0           sha256:be376566ba232aec17b8d66f100c1344b012ffcc03e0f19f1018bd3355f1a283
docker.easydb.de/pf/postgresql-14:5.155.0  sha256:5f4e214824d4136785d388dda438bd53c15ed03badd693ef66401542eb9b0af1
docker.easydb.de/pf/server-base:5.155.1    sha256:49ec91ce724ad4fa21d9f3fef4dbf5c340d922d4649aa75c738972bc83255c75
docker.easydb.de/pf/webfrontend:5.155.1    sha256:ccbc6a99acbd29c87f71051fa1cd5681ff9e5a47d9506492631dd0c06e7c1184
```
