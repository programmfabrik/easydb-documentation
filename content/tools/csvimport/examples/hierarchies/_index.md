---
title: "CSV-Importer Beispiele Hierarchische Listen"
menu:
  main:
    name: "Hierarchien"
    identifier: "tools/csvimport/examples/hierarchies"
    parent: "tools/csvimport/examples"
---
# Import von hierarchischen Listen

Hierarchische Listen enthalten Einträge, die über- und untergeordnete Einträge haben können. Diese Listen können aus nur einem Feld, oder aber auch aus mehreren Feldern bestehen. Die CSV-Datei muss eine Spaltenüberschrift enthalten. Diese kann frei vergeben werden. Es wird empfohlen, sprechende Namen zu vergeben, da diese Bezeichnungen später beim Mapping verwendet werden. Entsprechen die Spaltenüberschriften in der CSV-Datei den internen Feldbezeichnungen in easydb, erfolgt das Feld-Mapping automatisch.

> Bitte beachten Sie auch die [allgemeinen Hinweise](../../general).

## Beispiel-Datei "Orte"

| id   | ebene1                 | ebene2      | ebene3     |
| ---- | ---------------------- | ----------- | ---------- |
| 1    | Deutschland            |             |            |
| 2    |                        | Berlin      |            |
| 3    |                        | Brandenburg |            |
| 4    |                        |             | Potsdam    |
| 5    | Vereinigtes Königreich |             |            |
| 6    |                        | Schottland  |            |
| 7    |                        |             | Glasgow    |
| 8    |                        | England     |            |
| 9    |                        |             | London     |
| 10   |                        |             | Brighton   |
| 11   |                        |             | Manchester |



Alternativ können die Daten auch wie folgt strukturiert sein. Wichtig ist aber, dass jede Ebene in einer eigenen Zeile in der CSV-Datei vorkommt (die Zeilen 1, 3, 5, 6, 8 dürfen nicht entfallen):

| id   | ebene1                 | ebene2      | ebene3     |
| ---- | ---------------------- | ----------- | ---------- |
| 1    | Deutschland            |             |            |
| 2    | Deutschland            | Berlin      |            |
| 3    | Deutschland            | Brandenburg |            |
| 4    | Deutschland            | Brandenburg | Potsdam    |
| 5    | Vereinigtes Königreich |             |            |
| 6    | Vereinigtes Königreich | Schottland  |            |
| 7    | Vereinigtes Königreich | Schottland  | Glasgow    |
| 8    | Vereinigtes Königreich | England     |            |
| 9    | Vereinigtes Königreich | England     | London     |
| 10   | Vereinigtes Königreich | England     | Brighton   |
| 11   | Vereinigtes Königreich | England     | Manchester |



Außerdem besteht die Möglichkeit, die Hierarchien mittels Verweis auf den jeweils übergeordneten Eintrag zu importieren. Wichtig ist aber, dass jede Ebene in einer eigenen Zeile in der CSV-Datei vorkommt (die Zeilen 1, 3, 5, 6, 8 dürfen nicht entfallen):

| id   | parent                 | name                   |
| ---- | ---------------------- | ---------------------- |
| 1    |                        | Deutschland            |
| 2    | Deutschland            | Berlin                 |
| 3    | Deutschland            | Brandenburg            |
| 4    | Brandenburg            | Potsdam                |
| 5    |                        | Vereinigtes Königreich |
| 6    | Vereinigtes Königreich | Schottland             |
| 7    | Schottland             | Glasgow                |
| 8    | Vereinigtes Königreich | England                |
| 9    | England                | London                 |
| 10   | England                | Brighton               |
| 11   | England                | Manchester             |

Beim Mapping muss hier für die Spalte "parent" das Feld "id_parent" und für die Spalte "name" das entsprechende easydb-Feld ausgewählt werden. Enthält ihre Datei übergeordnete Einträge die noch nicht in der easydb vorhanden sind, müssen Sie den Import zweimal durchführen. Im ersten Schritt werden alle Einträge angelegt und beim zweiten Import werden die Verknüpfungen zwischen über- und den neuen untergeordneten Einträgen hergestellt. Voraussetzung ist, dass bei den Import-Einstellungen das "Feld zum Update" ausgewählt wurde über das der Abgleich erfolgen soll (in unserem Beispiel z.B. "id").



## Beispiel "Kategorien"

| id   | ebene1   | ebene2     | bemerkung                                                    |
| ---- | -------- | ---------- | ------------------------------------------------------------ |
| 1    | Personen |            | In diese Kategorie fallen z.B. Mitarbeiterfotos oder Fotos von Veranstaltungen. |
| 2    | Gebäude  |            |                                                              |
| 3    |          | Gebäude #1 | Dieses Gebäude war der ehemalige Sitz des Fachbereich XYZ. Aktuell befindet sich dort der Fachbereich ABC. |
| 4    |          | Gebäude #2 | Das Gebäude wurde 1986 erbaut.                               |



## Vorgehen

- öffnen Sie zunächst den CSV-Importer
- laden Sie Ihre CSV-Datei hoch
- wählen Sie bei CSV-Feldnamen "1. Zeile" aus
- wählen Sie den Ziel-Objekttyp sowie die dazugehörige Maske aus
- wechseln Sie in den Reiter "Import-Mapping" und wählen dort für jede Spalte die hierarchische Daten enthält das gleiche Zielfeld aus und tragen die Ebenen-Nummer ein (Achtung: die erste Ebene muss mit 0 beginnen)
- wählen Sie auch für alle weiteren Spalten im CSV die entsprechenden Ziel-Felder aus (wie z.B. für "Geburtsort" oder "Bemerkungen")
- wechseln Sie zurück zum Reiter "Import-Einstellungen" und wählen noch das "Feld zum Update" aus, wenn bereits Einträge in der Liste vorhanden sind, die ggfs. aktualisiert werden sollen
- klicken Sie anschließend auf "Vorbereiten" und sie erhalten eine Übersicht wie viele Zeilen importiert oder aktualisiert werden
- anschließend kann der Import / die Aktualisierung gestartet werden



