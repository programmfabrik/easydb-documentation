---
title: "Fields Migrator - ScriptExecuter Plugins"
menu:
  main:
    name: "Fields migrator"
    identifier: "webfrontend/datamanagement/search/find/scriptexecuter/fields_migrator"
    parent: "webfrontend/datamanagement/search/find/scriptexecuter"
---
# Feld-Migrator

Der Feld-Migrator ist ein Plugin vom ScriptExecuter. Er kann benutzt werden, um innerhalb eines Objekttyps Daten von einem Feld in ein anderes zu migrieren.

![](scriptexecuter_fields_migrator_en.png)

|Feld| Erklärung |
|---|---|
|Objekttyp | Es muss ein Objekttyp ausgewählt werden. Befinden sich in der Suche Objekte eines anderen Objekttyps werden diese ignoriert. |
|Feld von | Die Daten werden von diesem Feld übernommen. Sie werden dort nicht entfernt. Es ist nicht möglich, ein Feld innerhalb eines Mehrfachfeldes zu wählen. |
|Feld bis | Das ist das Ziel-Feld für die Daten. Es ist möglich, ein Feld innerhalb eines Mehrfachfeldes zu wählen (nur erste Ebene).|
|Caster | Die Caster werden weiter unten erklärt. |
|Caster-Optionen | Abhängig vom gewähten Caster (Beispiel siehe unten). |

### Caster (Typänderungen)

Um Daten von einem Feld in ein anderes zu migrieren, ist es wichtig, zu wissen, wie jedes Feld seine Daten behandelt.
Der Caster ist für die Umwandlung von einem Typen in einen anderen verantwortlich.
Wenn beide Felder den gleichen Typ haben, besitzen sie einen Caster, der die Daten ohne Umwandlung transferiert. (Es gibt Ausnahmen -> siehe Tabelle)
Custom Data Types: Caster sind Plugins. Es ist also möglich, personalisierte Caster hinzuzufügen, um Daten von/bis Custom-Data-Types zu transferieren.

#### Verfügbare Caster

| Von / Bis                       | Einzeiliger Text | Einzeiliger Text (mehrsprachig) | Mehrzeiliger Text | Mehrzeiliger Text (mehrsprachig) | Einfacher Text (String) | Datum | Datum (Bereich) | Datum + Zeit | Zahl/Kommazahl | Datei | Ja/Nein-Feld (Boolesch) | Verlinkte Objekttypen  |
|---------------------------------|------------------|---------------------------------|-------------------|----------------------------------|-------------------------|-------|-----------------|--------------|----------------|-------|-------------------------|----------------------- |
| Einzeiliger Text                |JA                |                                 |                   |                                  |                         |JA     |JA               |              |                |       |                         |                        |
| Einzeiliger Text (mehrsprachig) |                  |JA                               |                   |                                  |                         |       |                 |              |                |       |                         |                        |
| Mehrzeiliger Text               |                  |                                 |JA                 |                                  |                         |       |                 |              |                |       |                         |                        |
| Mehrzeiliger Text (mehrsprachig)|                  |                                 |                   |JA                                |                         |       |                 |              |                |       |                         |                        |
| Einfacher Text (String)         |                  |                                 |                   |                                  |JA                       |       |                 |              |                |       |                         |                        |
| Datum                           |JA                |                                 |                   |                                  |                         |JA     |JA               |              |                |       |                         |                        |
| Datum (Bereich)                 |JA                |                                 |                   |                                  |                         |JA     |JA               |              |                |       |                         |                        |
| Datum + Zeit                    |                  |                                 |                   |                                  |                         |       |                 |JA            |                |       |                         |                        |
| Zahl/Kommazahl                  |                  |                                 |                   |                                  |                         |       |                 |              |JA              |       |                         |                        |
| Datum                           |                  |                                 |                   |                                  |                         |       |                 |              |                |       |                         |                        |
| Ja/Nein-Feld (Boolesch)         |                  |                                 |                   |                                  |                         |       |                 |              |                |       |JA                       |                        |
| Verlinkte Objekttypen           |                  |                                 |                   |                                  |                         |       |                 |              |                |       |                         |JA (gleicher Objekt-Typ)|

### Caster Beispiel

In diesem Beispiel ist das Feld 'von' vom Typ 'Datum' und das Feld 'bis' ist vom Typ 'Datum (Bereich)'.
Der Caster gibt zusätzliche Informationen an, sodass das Datum entweder zu 'Datum von', 'Datum bis' oder 'beide' transferiert wird.

![](scriptexecuter_fields_migrator_example_en.png)
