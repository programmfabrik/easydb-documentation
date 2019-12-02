---
title: "86 - Zeiträume"
menu:
  main:
    name: "Zeiträume"
    identifier: "webfrontend/datamanagement/features/daterange"
    parent: "webfrontend/datamanagement/features"
---
# Zeiträume

Das easydb-Datumsfeld interpretiert die Eingabe des Datums und speichert das Ergebnis, zusätzlich zu Ihrer Eingabe, als **Zeitraum** in der Datenbank.

Auf diese Weise können Sie einen Datensatz unter einem konkreten Datum, aber auch unter einer festen oder ungefähren Zeitspanne einordnen und finden.

Aktiviert werden kann diese Funktion im Datenmodell durch die [Option "Support für Text Ein- und Ausgabe"](../../../administration/datamodel/mask/) in der Maske wo sich das Datumsfeld befindet. Der Benutzer kann anschließend im Editor wählen, ob er die Texteingabe (ein Feld) oder die Datumseingabe (zwei Felder für "von" und "bis") nutzen möchte.



### Unterstützte Syntax:

| Syntax     | Bedeutung                                                    | Synonyme                 |
| :--------- | :----------------------------------------------------------- | :----------------------- |
| TT.MM.JJJJ | Exakter Tag                                                  | T.M.JJJJ                 |
| JJJJ-MM-TT | Exakter Tag                                                  | JJJJ-M-T                 |
| JJJJ-MM    | Zeitraum: Monat vom 1. bis letzten Tag.                      | JJJJ-M                   |
| MM-JJJJ    | Zeitraum: Monat vom 1. bis letzten Tag.                      | M-JJJJ                   |
| JJJJ       | Zeitraum: Jahr vom 1. bis letzten Tag.                       |                          |
| vor JJJJ   | Zeitraum: Zeitspanne an Jahren vor bis zum angegegebene Jahr. Die Zeitspanne hängt von der Jahreszahl ab, siehe dazu untenstehende Tabelle. | vor, before, bis, Ende1  |
| nach JJJJ  | Zeitraum: Zeitspanne an Jahren vom angegebenen Jahr bis zu einem nachfolgenden Jahr. Die Zeitspanne hängt von der Jahreszahl ab, siehe dazu untenstehende Tabelle. | nach, ab, after, Anfang1 |
| um JJJJ    | Zeitraum: Spanne in Jahren von vor dem angegeben Jahr und danach. Die Spanne hängt von der Jahreszahl ab, siehe dazu untenstehende Tabelle. | um, gegen, about, ca.    |
| JJJJ bc    | Interpretiert das Jahr als vor Christus (Before Christ).     | BC, AD, ANTE, BCE        |
| nn Jhd.    | Zeitraum: das gesamte Jahrhundert nn vom ersten bis zum letzten Tag. | Jh, Jh. Jhd.             |
| nn Jt.     | Zeitraum: das gesamte Jahrtausend nn vom ersten bis zum letzten Tag. | Jt, Jt.                  |



### Zeitspannen:

| Jahreszahl teilbar durch | Spanne ± |
| :----------------------- | :------- |
| 1000                     | 500      |
| 100                      | 50       |
| 50                       | 15       |
| 10                       | 5        |
| 1                        | 2        |



### Anmerkungen:

- **Anfang** und **Ende** funktionieren nur für Jahrtausende und Jahrhunderte
- Groß- und Kleinschreibung wird bei den Schlüsselwörtern ignoriert
- Für Daten und Zeiträume bis zum Jahr 1000 werden nur reine Jahreszahlen und keine exakten Tage/Monate akzeptiert
- Angaben vor Christus werden "umgekehrt" notiert – "nach 2000 bc" entspricht also "2000 – 1500 bc", wogegen "nach 1000" synonym wäre zu "1000 – 1500"



### Beispiele:

| Eingabe                   | Datum von    | Datum bis    |
| ------------------------- | ------------ | ------------ |
| 2 Jt.                     | 1001         | 2000         |
| 3 Jt. v. Chr.             | 3000 v. Chr. | 2001 v. Chr. |
| 10 Jhd.                   | 901          | 1000         |
| 10 Jhd. v. Chr.           | 1000 v. Chr. | 901 v. Chr.  |
| Anfang 2. Jh.             | 101          | 116          |
| Anfang 2. Jh. v. Chr.     | 200 v. Chr.  | 185 v. Chr.  |
| Ende 3. Jh.               | 285          | 300          |
| Ende 3. Jh. v. Chr.       | 215 v. Chr.  | 200 v. Chr.  |
| nach 2000 v. Chr.         | 2001 v. Chr. | 1501 v. Chr. |
| nach 2000                 | 2000         | 2500         |
| um 2000                   | 1500         | 2500         |
| um 2000 v. Chr.           | 2501 v. Chr. | 1501 v. Chr. |
| vor 2000                  | 1500         | 2000         |
| vor 2000 v. Chr.          | 2501 v. Chr. | 2001 v. Chr. |
| 06.01.1989 bis 16.08.1991 | 06.01.1989   | 16.08.1991   |

