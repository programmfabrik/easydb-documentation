---
title: "CSV-Importer Beispiele Hierarchische Listen"
menu:
  main:
    name: "Hierarchien"
    identifier: "webfrontend/datamanagement/lists/csvimport/examples/hierarchies"
    parent: "webfrontend/datamanagement/lists/csvimport/examples"
---
# Import von hierarchischen Listen - In Bearbeitung

Hierarchische Listen enthalten Einträge, die über- und untergeordnete Einträge haben können. Diese Listen können aus nur einem Feld, oder aber auch aus mehreren Feldern bestehen. Die CSV-Datei muss eine Spaltenüberschrift enthalten. Diese kann frei vergeben werden. Es wird empfohlen, sprechende Namen zu vergeben, da diese Bezeichnungen später beim Mapping verwendet werden. Entsprechen die Spaltenüberschriften in der CSV-Datei den internen Feldbezeichnungen in easydb, erfolgt das Feld-Mapping automatisch.

> Bitte beachten Sie auch die [allgemeinen Hinweise](../../general).

## Beispiel-Datei "Orte"

| ebene1                 | ebene2      | ebene3     |
| ---------------------- | ----------- | ---------- |
| Deutschland            |             |            |
|                        | Berlin      |            |
|                        | Brandenburg |            |
|                        |             | Potsdam    |
| Vereinigtes Königreich |             |            |
|                        | Schottland  |            |
|                        |             | Glasgow    |
|                        | England     |            |
|                        |             | London     |
|                        |             | Brighton   |
|                        |             | Manchester |



## Beispiel "Kategorien"

| ebene1   | ebene2     | bemerkung                                                    |
| -------- | ---------- | ------------------------------------------------------------ |
| Personen |            | In diese Kategorie fallen z.B. Mitarbeiterfotos oder Fotos von Veranstaltungen. |
| Gebäude  |            |                                                              |
|          | Gebäude #1 | Dieses Gebäude war der ehemalige Sitz des Fachbereich XYZ. Aktuell befindet sich dort der Fachbereich ABC. |
|          | Gebäude #2 | Das Gebäude wurde 1986 erbaut.                               |



## Vorgehen

- öffnen Sie zunächst den CSV-Importer
- laden Sie die Datei hoch
- wählen Sie bei CSV-Feldnamen "1. Zeile" aus
- wählen Sie den Ziel-Objekttyp sowie die dazugehörige Maske aus
- wechseln Sie in den Reiter "Mapping" und wählen dort für jede Spalte die hierarchische Daten enthält das gleiche Zielfeld aus und tragen die Ebenen-Nummer ein (Achtung: die erste Ebene muss mit 0 beginnen)
- wählen Sie auch für alle weiteren Spalten im CSV die entsprechenden Ziel-Felder aus (wie z.B. für "Geburtsort" oder "Bemerkungen")
- wechseln Sie zurück zum Reiter "Datei" und wählen noch das "Feld zum Update" aus, wenn bereits Einträge in der Liste vorhanden sind, die ggfs. aktualisiert werden sollen
- klicken Sie anschließend auf "Vorbereiten" und sie erhalten eine Übersicht wie viele Zeilen importiert oder aktualisiert werden
- anschließend kann der Import / die Aktualisierung gestartet werden



## Screenshots





