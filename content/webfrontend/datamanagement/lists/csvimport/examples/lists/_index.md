---
title: "CSV-Importer Beispiele Flache Listen"
menu:
  main:
    name: "Listen"
    identifier: "webfrontend/datamanagement/lists/csvimport/examples/lists"
    parent: "webfrontend/datamanagement/lists/csvimport/examples"
---
# Import von flachen Listen - In Bearbeitung

Flache Listen enthalten Einträge, die alle gleichrangig sind. Diese Listen können aus nur einem Feld, oder aber auch aus mehreren Feldern bestehen. Die CSV-Datei muss eine Spaltenüberschrift enthalten. Diese kann frei vergeben werden. Es wird empfohlen, sprechende Namen zu vergeben, da diese Bezeichnungen später beim Mapping verwendet werden. Entsprechen die Spaltenüberschriften in der CSV-Datei den internen Feldbezeichnungen in easydb, erfolgt das Feld-Mapping automatisch.

> Bitte beachten Sie auch die [allgemeinen Hinweise](../../general).

## Beispiel-Datei "Schlagwörter"

| schlagwörter |
| ------------ |
| Sonne        |
| Mond         |
| Sterne       |



## Beispiel-Datei "Personen"

| vorname | nachname   | geburtsort                                       | bemerkung                 |
| ------- | ---------- | ------------------------------------------------ | ------------------------- |
| Steve   | Jobs       | Vereinigte Staaten > Kalifornien > San Francisco | Mitgründer von Apple Inc. |
| Bill    | Gates      | Vereinigte Staaten > Washington > Seattle        | Gründer von Microsoft     |
| Mark    | Zuckerberg | Vereinigte Staaten > New York > White Plains     | Gründer von Facebook Inc. |

> In unserem Beispiel handelt es sich bei dem Geburtsort um eine Verknüpfung mit einer hierarchischen Liste. Siehe auch [Datentypen - Einfache Verlinkung mit hierarchischer Liste](../../datatypes).



## Vorgehen

- öffnen Sie zunächst den CSV-Importer
- laden Sie die Datei hoch
- wählen Sie bei CSV-Feldnamen "1. Zeile" aus
- wählen Sie den Ziel-Objekttyp sowie die dazugehörige Maske aus
- wechseln Sie in den Reiter "Mapping" und wählen dort die entsprechenden Zielfelder aus
- wechseln Sie zurück zum Reiter "Datei" und wählen noch das "Feld zum Update" aus, wenn bereits Einträge in der Liste vorhanden sind, die ggfs. aktualisiert werden sollen
- klicken Sie anschließend auf "Vorbereiten" und sie erhalten eine Übersicht wie viele Zeilen importiert oder aktualisiert werden
- anschließend kann der Import / die Aktualisierung gestartet werden



## Screenshots

