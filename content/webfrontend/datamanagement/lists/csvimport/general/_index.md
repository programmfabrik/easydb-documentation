---
title: "93 - Allgemeine Hinweise"
menu:
  main:
    name: "Allgemeine Hinweise"
    identifier: "webfrontend/datamanagement/lists/csvimport/general"
    parent: "webfrontend/datamanagement/lists/csvimport"
---
# Allgemeine Hinweise - In Bearbeitung

- die CSV-Datei muss UTF-8 oder UTF-16 kodiert sein (andernfalls werden Umlaute und Sonderzeichen nicht korrekt importiert)
- als Spaltentrennzeichen können Komma, Semilokon oder Tabulator verwendet werden (die Erkennung erfolgt durch easydb automatisch)
- Texte die Kommas, Semikolons, Tabulatoren oder Umbrüche enthalten, müssen von doppelten oder einfachen Anführungszeichen umschlossen werden (die Erkennung erfolgt durch easydb automatisch)
- die Spaltenüberschriften in der CSV-Datei können frei gewählt werden (das Mapping der Quell- und Ziel-Felder muss dann manuell erfolgen, siehe [Optionen](../options))
- wenn Sie die internen easydb-Feldnamen als Spaltenüberschrift in der CSV-Datei verwenden, erfolgt das Mapping automatisch (z.B. BEISPIELE ERGÄNZEN)
- verwenden Sie wenn möglich immer einen eindeutigen Idendifier, denn nur über diesen können später vorhandene Datensätze aktualisiert werden
- beim Import von Anführungszeichen ist folgendes zu beachten:

| Zu importierender Text                                       | Schreibweise in der CSV-Datei                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| "Einfacher Text, der in Anführungszeichen eingeschlossen ist, die importiert werden sollen." | """Einfacher Text, der in Anführungszeichen eingeschlossen ist, die importiert werden sollen.""" |
| Einfacher Text, der "Anführungszeichen" enthält.             | "Einfacher Text, der ""Anführungszeichen"" enthält."         |
| "Einfacher Text in Anführungszeichen, der aber auch Anführungszeichen" enthält." | """Einfacher Text in Anführungszeichen, der aber auch ""Anführungszeichen"" enthält.""" |
| "Dies ist ein Zitat." sagte Person Z.                        | """Dies ist ein Zitat."" sagte Person Z."                    |
| Person Z sagte "Dieses Zitat."                               | "Person Z sagte ""Dieses Zitat."""                           |

