---
menu:
  main:
    name: "5.117 (Ende Mai 2023)"
    identifier: "5.117"
    parent: "releases5110"
    weight: -617
---


> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.117.0

*Veröffentlicht am 31.05.2023*


# Webfrontend

## Neu

* **Editor**:
  * **Adhoc template**: neue Funktion, die das Kopieren eines Objekts als Vorlage ermöglicht. In der Vorlagenauswahl erscheint eine temporäre Vorlage, die die Daten des zuletzt als Vorlage kopierten Objekts enthält
* ein Parent-Feld wurde zum Header in der Detailansicht von Hierarchieobjekten hinzugefügt, wenn die Hierarchie so konfiguriert ist, dass sie in der Maske angezeigt wird

## Verbessert

* **Mappen-Präsentation**: Die Option "Standardinfo anzeigen" ist jetzt als Standardoption für Folien in Präsentationen voreingestellt
* **Masken**: Der Maskeneditor für Objekttypen wurde verbessert, wenn die Option "Nested Index" für verschachtelte Felder ausgewählt wird. Jetzt kopieren die anderen Masken des Objekts dieses Attribut, wodurch sichergestellt wird, dass alle Masken denselben Wert für "Nested Index" für ein bestimmtes Feld haben. Zuvor war der Server dafür verantwortlich
* **Suche**: Das Untermenü der gespeicherten Mappen-Suchen wurde verbessert. Optionen, die in diesem Untermenü nicht erscheinen sollten, wurden entfernt
* **Pool Manager**:
  * Die Reihenfolge der Poolfelder im allgemeinen Formular wurde verbessert
  * die Texte der Navigationstools in der Poolmanagerliste wurden verbessert
* **Transitionen / Workflows**: "Löschen" und "Kopieren" Buttons verbessert
* Der Standardwert der Update-Policy für Upload in Mappen wurde auf "neue bevorzugte Asset-Version erstellen" geändert
* die Admin-Mitteilungen vor Downloads wurden verbessert, jetzt enthalten alle Asset-Download-Optionen diese Meldungen
* der Gruppen-Tag-Editor wurde verbessert, er benötigt nun weniger Requests, um die Tags zu ändern

## Behoben

* **Objekttyp-Manager**:
  * Problem mit dem Dateinamen für den Export von Assets für Objekttypen wurde behoben.
  * Die Schaltflächen des Hauptmenüs für Objekttypen wurden so verbessert, dass sie auch für Benutzer angezeigt werden, die nur Leserechte für diese Objekttypen haben
* **Teilen von Versionen von Assets**: Schaltflächen zum Freigeben werden nur noch für Benutzer mit entsprechenden Rechten angezeigt
* Fehlerbehebungen in der Expertensuche des "Filter für verknüpfte Objekte"-Panels
* Fehler in der Funktion "Filter für verknüpfte Objekte" wurden behoben
* Fehler beim Versuch, den Gruppeneditor mehrfach zu öffnen, behoben
* ein Problem mit dem Standardpool für die Option "Pool für verknüpfte Objekte" in den Einstellungen für das Hochladen von Sammlungen wurde behoben
* Fehler in der Detailansicht wurde behoben, wenn die einzige verfügbare Version eines Assets eine mit Wasserzeichen versehene Version war
* Problem mit "Reverse Linked Nested" wurde behoben, wenn es einen Verweis auf ein Objekt gibt, bei dem das konfigurierte Feld, das in der Reverse Nested Tabelle angezeigt werden soll, geleert wurde

# Server

## Verbessert

* Verweise auf archivierte Benutzer werden durch den Fallback-Systembenutzer `deleted_user` ersetzt

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.117.0         sha256:51aa8f6572748f163d90100970cb835c9149edb0815e98763bd889a83d54ab23
docker.easydb.de/pf/eas:5.117.0            sha256:bd466ce347605349b2cd9055a1644cad6b167448cf5bfee436593ed15a4c16af
docker.easydb.de/pf/elasticsearch:5.117.0  sha256:ff10cf15bf50d9f7cd3b40073e398af07d2bb52f836eb03850cef49c595e5ec9
docker.easydb.de/pf/fylr:5.117.0           sha256:265f6630b4ac897e1f68dd42e7fcc6b66e1e1398e681cf51efe58ec746b25d8b
docker.easydb.de/pf/postgresql-14:5.117.0  sha256:6a9cca4fb7b73d47434963bafb75700df5b1e0ad6744732e6ef8d23650371b2c
docker.easydb.de/pf/server-base:5.117.0    sha256:3239013b4a05bdf0c5b21d01d7f79050e821cc8a63de3b6fb28d704c539b2029
docker.easydb.de/pf/webfrontend:5.117.0    sha256:33f6a9539a55b3e68834df1470f5bbe6da108f57b54b64a62f7e26041c8ba3ed
```
