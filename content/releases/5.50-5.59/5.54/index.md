---
menu:
  main:
    name: "5.54"
    identifier: "5.54"
    parent: "releases559"
    weight: -554
---

# Version 5.54.2

*Veröffentlicht am 01.08.2019*

### Webfrontend

*Behoben*

* Detail: **Lange Texte in mehrsprachigen Feldern** wurden nicht korrekt umbrochen.
* Editor: Beim mehrfachen Benutzen von **+ Neue Objekte** konnte es zu einem Fehler kommen.
* Mappen: Das Icon für Mappen mit **PIN-Code** gab es nur in der deutschen Sprachversion.

### Server

*Behoben*

* Ein Rechtemanagement-Fehler bei **geteilten Mappen** wurde behoben.

# Version 5.54.1

*Kundenspezifisches Release ohne Auswirkungen auf den allgemeinen Code.*

# Version 5.54.0

*Veröffentlicht am 24.07.2019*

### Webfrontend

*Neu*

* Beta: **PIN-Code Support** für Mappen. Jede Rechteliste einer Mappe kann mit einem PIN-Code abgesichert werden. Wenn ein Nutzer auf einer Mappe mit PIN zugreifen möchte, muss er die PIN zuvor eingeben.
* Suchergebnis: In der Textansicht können jetzt **Pools** und **Tags** optional eingeblendet werden.
* In **Präsentationen** können nun bei der Ausgabe von Standard Titel, Untertitel und Beschreibung ausgegeben werden.
* **JSON/CSV-Importer**: Für den Import mit Dateien kann ein **Metadaten-Mapping** ausgewählt werden.
* **Datenmodell**: Eine neue Spalte im Maskeneditor erlaubt das Anlegen von Nutzerhinweisen für die Detailausgabe.

*Verbessert*

* Editor/Detail: Die **Anzeigelogik von Masken** wurde verbessert. Nun werden auch erlaubte Masken aus der jeweiligen Liste im Editor entfernt, wenn sie nicht im Editor angezeigt werden sollen.
* **Strukturmappen** haben ein Icon zur besseren Lesbarkeit bekommen.
* Der **Datumsfilter** hat neue Gruppierungen für zukünftige Daten bekommen.
* Anzeigeverbesserungen für die **Texteingabe in Datumsbereichsfeldern**.
* Die Liste der Metadaten-Mappings wird gefiltert, wenn die Objekttypen bekannt sind. 

*Behoben*

* Expertensuche: Die Suche nach **Änderungshistorie mit einem Datumsfilter** wurde repariert.

<h3>Server</h3>
*Neu*

- Beta: **PIN-Code Support** für Mappen (siehe oben).
- Möglichkeit eigene Felder für das **Metadaten-Mapping-Profil** zu verwenden.

*Verbessert*

- Die Text-Formatierung im **Präsentationsplugin** wurde verbessert.
- Suche nach *ohne Inhalt* berücksichtigt bei **mehrsprachigen Feldern** jetzt nur Datensätze in denen alle der aktivierten Sprachen nicht ausgefüllt sind.
- **Optimierung** für Pool-Änderungen im Gruppeneditor.
- **Stabile Maskenreihenfolge,** wenn aus Datenmodell geladen.
- Verbesserte Sicherheit bei **Remote Objects** in Collections.
- **Export von Veröffentlichungen** in XML. und CSV-Exporten.

*Behoben*

- Die **Sortierung nach Datumsbereichsfeldern** wurde behoben.
- Fehler beim Löschen und Neuanlegen der selben Tabelle in einem Durchlauf behoben.
- Fixes für **Indizierung** beim Ändern von Base-Objekten.
- Fehler beim **Export in mehrsprachige XMP-Felder** behoben.