---
title: "CSV-Import Beispiele je Datentyp"
menu:
  main:
    name: "Alle Datentypen"
    identifier: "tools/csvimport/examples/datatypes"
    parent: "tools/csvimport/examples"
---
# Beispiele je Datentyp

An dieser Stelle finden Sie für jeden in easydb verfügbaren Datentyp ein Beispiel für die Aufbereitung der Daten im CSV-Format. Für weitere Informationen schauen Sie in unsere [allgemeinen Hinweise](./general) bzw. in die Erklärung der CSV-Importer-Optionen. Eine Best-Practice-Anleitung findet Sie in unseren Tutorials. Eine CSV-Datei mit allen Beispielen können Sie sich hier herunterladen.

<br>

## Pools

Sollten Sie Datensätze nur in einen Pool importieren wollen, so müssen Sie den Pool nicht in der CSV-Datei eintragen, sondern wählen ihn lediglich in den Import-Einstellungen. Haben Sie allerdings Datensätze die in unterschiedlichen Pools abgelegt werden sollen oder wollen Sie bei bereits im System vorhandenen Datensätzen den Pool ändern, so müssen Sie den Pool in der CSV-Datei ergänzen. Sie können die ID, den Kurznamen oder die Referenz des Pools in der CSV-Datei verwenden. Ist für einen Datensatz in der CSV-Datei kein Pool angegeben, wird der Pool aus den Import-Einstellungen verwendet.

| id   | Titel                | Pool   |
| ---- | -------------------- | ------ |
| 1    | Berlin bei Nacht     | Pool A |
| 2    | Berliner Fernsehturm |        |
| 3    | Berliner Dom         | Pool B |

Im Import-Mapping wählen Sie für die Spalte in der der Pool steht "_pool" sowie das Feld "ID", "Kurzname" oder "Referenz" aus.

<br>

## Tags

Auch Tags können über den CSV-Importer importiert werden. Sie können die ID oder den Tagnamen in der CSV-Datei verwenden. Wollen Sie mehrere Tags importieren, können Sie ein Komma (","), ein Semikolon (";"), eine Pipe ("|") oder einen Zeilenumbruch ("\n") verwenden.

| id   | Titel                | Tags            |
| ---- | -------------------- | --------------- |
| 1    | Berlin bei Nacht     | Tag A           |
| 2    | Berliner Fernsehturm |                 |
| 3    | Berliner Dom         | Tag B<br/>Tag C |

Im Import-Mapping wählen Sie für die Spalte in der die Tags stehen "_tags" sowie das Feld "ID" oder "Anzeigename", sowie den verwendeten Trenner aus.

<br>

## Einzeiliger & Mehrzeiliger Text, Einfacher Text (String)

Es empfiehlt sich die Texte in doppelte Anführungszeichen zu setzen. Sollte ein Text ein Komma, Semikolon, einen Backslash, Tabulator oder einen Umbruch enthalten, müssen doppelte Anführungszeichen verwendet werden, damit diese nicht als Spaltentrenner interpretiert werden.

| id   | titel (einzeiliger Text) | beschreibung (mehrzeiliger Text)                             | signatur (String) |
| ---- | ------------------------ | ------------------------------------------------------------ | ----------------- |
| 1    | Berlin bei Nacht         | Das Bild zeigt den beleuchteten Alexanderplatz bei Nacht.    | Signatur_2019_001 |
| 2    | Berliner Dom             | "Der Berliner Dom in der Mittagssonne.<br> <br>Viele Menschen liegen auf der Wiese vorm Berliner Dom." | SIgnatur_2018_002 |
| 3    | Berlin von oben          |                                                              | Signatur_2017_003 |

Im Mapping müssen jeweils nur die entsprechenden Ziel-Felder ausgewählt werden. Es gibt keine weiteren Optionen.

<br>

## Einzeiliger & Mehrzeiliger Text (mehrsprachig)

Bei mehrsprachigen Feldern werden die Inhalte für die verschiedenen Sprachen intern in getrennten Feldern gespeichert. Daher müssen die Sprachen auch in der CSV-Datei in unterschiedliche Spalten geschrieben werden.

| id   | titel_de                                        | titel_en                                 | titel_es          |
| ---- | ----------------------------------------------- | ---------------------------------------- | ----------------- |
| 1    | Deutscher Titel                                 | English title                            | Título en español |
| 2    | Hier ist nur ein deutscher Titel vorhanden      |                                          |                   |
| 3    | Diesen Titel haben wir auf Deutsch und Englisch | We have this title in German and English |                   |

Im Mapping muss für beide Spalten zunächst das gleiche Ziel-Feld ausgewählt werden. Anschließend kann die dazugehörige Sprache ausgewählt werden. Wird eine Sprache im Pulldown nicht angezeigt, so muss diese zunächst vom Administrator in der [Basiskonfiguration](../../../../administration/base-config/general) aktiviert werden.

<br>

## Datum, Datum + Zeit

Beim Import von Datumsangaben wird sowohl das deutsche als auch das amerikanische Format unterstützt.

| id   | aufnahmedatum (Datum) | aufnahmezeitpunkt (Datum + Zeit) |
| ---- | --------------------- | -------------------------------- |
| 1    | 2019-12-06            | 2019-12-09 13:39:00              |
| 2    | 24.12.2019            |                                  |
| 3    | 2018-11               | 2019-12-09                       |
| 4    | 2017                  |                                  |

Im Mapping müssen jeweils nur die entsprechenden Ziel-Felder ausgewählt werden. Es gibt keine weiteren Optionen.

<br>

## Datum (Bereich)

Das Datumsbereichsfeld zeichnet sich dadurch aus, dass die Werte intern in zwei Feldern gespeichert werden. Es gibt ein Feld "von" und "bis". Daher müssen das Start- und Enddatum auch in der CSV-Datei in zwei Spalten geschrieben werden. Auch hier werden wieder das deutsche als auch das amerikanische Format akzeptiert.

| id   | datum_von  | datum_bis  |
| ---- | ---------- | ---------- |
| 1    | 2019-10-01 | 2019-10-08 |
| 2    | 2016-01    | 2018-12    |
| 3    | 2009       | 2019-12-31 |

Im Mapping muss für beide Spalten zunächst das gleiche Ziel-Feld ausgewählt werden. Anschließend kann ausgewählt werden, ob die Daten in "von" oder "bis" geschrieben werden sollen.

<br>

## Zahl (ganzzahlig), Kommazahl (2 Stellen)

Beim Import von Kommazahlen wird sowohl der Punkt als auch das Komma unterstützt. Tausender-Trenner (Punkt oder Komma) dürfen aktuell nicht verwendet werden.

| id   | anzahl (Zahl) | wert (Kommazahl) |
| ---- | ------------- | ---------------- |
| 1    | 1             | 1.40             |
| 2    | 2             | 5,80             |
| 3    | 3             | 35               |

Im Mapping müssen jeweils nur die entsprechenden Ziel-Felder ausgewählt werden. Es gibt keine weiteren Optionen.

<br>

## Ja/Nein-Feld (Boolesch)

Felder des Typs "Ja/Nein-Feld (Boolesch)" werden im easydb-Frontend als Checkbox dargestellt. Die beiden Zustände "aktiviert" und "deaktiviert" können beim Import durch "true" bzw. "1" und "false" bzw. "0" gesetzt werden. Leere Felder im CSV entsprechen "false".

| id   | original_vorhanden |
| ---- | ------------------ |
| 1    | true               |
| 2    | false              |
| 3    |                    |

Im Mapping ist lediglich das entsprechende Ziel-Feld auszuwählen. Es gibt keine weiteren Optionen.

<br>

## Einfache Verlinkung mit flacher Liste

Ist in easydb bei einem Feld eine flache Liste hinterlegt, können diese Verknüpfungen auch über CSV-Importiert werden. Der zu verlinkende Eintrag kann, muss aber nicht in der hinterlegten Liste vorhanden sein.

| id   | kategorie       |
| ---- | --------------- |
| 1    | Personen        |
| 2    | Gebäude         |
| 3    | Veranstaltungen |

Im Mapping wählen Sie zunächst das entsprechende Ziel-Feld aus. Im Anschluss wählen Sie das Feld aus dem verlinkten Objekttyp aus. Die easydb prüft über dieses Feld, ob der Eintrag bereits in der Liste vorhanden ist. Wenn ja, wird der vorhandene Eintrag verknüpft. Falls nicht, wird ein neuer Eintrag in der Liste angelegt und verknüpft (sofern beim CSV-Import auf dem Reiter "Datei" die Checkbox "Verlinkte Objekte anlegen" aktiviert ist).

<br>

## Einfache Verlinkung mit hierarchischer Liste

Ist in easydb bei einem Feld eine hierarchische Liste hinterlegt, können diese Verknüpfungen auch über CSV-Importiert werden. Der zu verlinkende Eintrag kann, muss aber nicht in der hinterlegten Liste vorhanden sein.

| id   | aufnahmeort                                   |
| ---- | --------------------------------------------- |
| 1    | Deutschland > Berlin                          |
| 2    | Irland > Dublin                               |
| 3    | Vereinigtes Königreich > Schottland > Glasgow |

Im Mapping wählen Sie zunächst das entsprechende Ziel-Feld aus. Im Anschluss wählen Sie das Feld aus dem verlinkten Objekttyp aus. Die easydb prüft über dieses Feld, ob der Eintrag bereits in der Liste vorhanden ist. Wenn ja, wird der vorhandene Eintrag verknüpft. Falls nicht, wird ein neuer Eintrag in der Liste angelegt und verknüpft (sofern beim CSV-Import auf dem Reiter "Datei" die Checkbox "Verlinkte Objekte anlegen" aktiviert ist). Beim Import von hierarchischen Listen kann noch der verwendete Trenner gewählt werden (">" oder "/").

<br>

## Wiederholbares Freitext-Feld

Handelt es sich bei dem Zielfeld um ein sog. Mehrfach-Feld (d.h. pro Datensatz können davon mehrere Angaben gemacht werden), müssen in der CSV-Datei alle Einträge in eine Zelle geschrieben und mit Umbruch getrennt werden. Verwenden Sie doppelte Anführungszeichen, um Texte die einen Umbruch enthalten, zu importieren.

| id   | wiederholbares_freitextfeld                                  |
| ---- | ------------------------------------------------------------ |
| 1    | Erster Text<br>Zweiter Text<br>Dritter Text                  |
| 2    | "Text der einen Umbruch<br/>enthält."<br/>"Text ohne Umbruch, aber mit Komma." |

Im Mapping ist lediglich das entsprechende Ziel-Feld auszuwählen. Es gibt keine weiteren Optionen.

> Alternativ kann jeder Eintrag des wiederholbaren Feldes auch in eine eigene Spalte geschrieben werden. Beim Import ist allerdings zu beachten, dass dieser mehrstufig erfolgen muss, da man beim Mapping das Ziel-Feld immer nur einmal auswählen darf. Im ersten Durchlauf mappt und importiert man also die erste Spalte. Im zweiten Durchlauf nur die zweite, etc. Wichtig ist, dass in diesem Fall unter "Import-Einstellungen" die Option "Mehrfachfelder anfügen" aktiviert wird, damit die Einträge im Mehrfachfeld ergänzt und nicht jedes mal überschrieben werden.

<br>

## Wiederholbare Verlinkung

Handelt es sich bei dem Zielfeld um ein sog. Mehrfach-Feld in dem auf einen anderen Objekttyp verwiesen wird, müssen alle zu verlinkenden Einträge in der CSV-Datei in eine Zelle geschrieben und mit Umbruch getrennt werden. Verwenden Sie doppelte Anführungszeichen, um Einträge die einen Umbruch oder Trennzeichen enthalten, zu importieren.

| id   | schlagwörter                                  |
| ---- | --------------------------------------------- |
| 1    | Sonne<br>Mond<br>Sterne                       |
| 2    | "Stadt, Land, Fluss Spiel"<br/>"Kinderspiele" |

Dies funktioniert auch, wenn der verlinkte Objekttyp hierarchisch ist:

| id   | frühere_standorte                                            |
| ---- | ------------------------------------------------------------ |
| 1    | Deutschland > Berlin<br>Irland > Dublin<br>Vereinigtes Königreich > Schottland > Glasgow |

Im Mapping wählen Sie zunächst das entsprechende Ziel-Feld aus. Im Anschluss wählen Sie das Feld aus dem verlinkten Objekttyp aus. Die easydb prüft über dieses Feld, ob der Eintrag bereits in der Liste vorhanden ist. Wenn ja, wird der vorhandene Eintrag verknüpft. Falls nicht, wird ein neuer Eintrag in der Liste angelegt und verknüpft (sofern beim CSV-Import auf dem Reiter "Datei" die Checkbox "Verlinkte Objekte anlegen" aktiviert ist). Beim Import von hierarchischen Listen kann noch der verwendete Trenner gewählt werden (">" oder "/").

> Alternativ kann jeder Eintrag des wiederholbaren Feldes auch in eine eigene Spalte geschrieben werden. Beim Import ist allerdings zu beachten, dass dieser mehrstufig erfolgen muss, da man beim Mapping das Ziel-Feld immer nur einmal auswählen darf. Im ersten Durchlauf mappt und importiert man also die erste Spalte. Im zweiten Durchlauf nur die zweite, etc. Wichtig ist, dass in diesem Fall unter "Import-Einstellungen" die Option "Mehrfachfelder anfügen" aktiviert wird, damit die Einträge im Mehrfachfeld ergänzt und nicht jedes mal überschrieben werden.

<br>

## Wiederholfeld mit mehreren Feldern

Handelt es sich bei dem Ziel-Feld um ein sog. Mehrfach-Feld, welches mehr als nur ein Feld beinhaltet, so müssen diese Felder auf einzelne Spalten aufgeteilt werden. Soll mehr als nur ein Eintrag mit einem Datensatz verknüpft werden, müssen diese wieder in einer Zelle eingetragen und durch Umbruch getrennt werden.

| id   | weitere_ids                  | id_typ                          |
| ---- | ---------------------------- | ------------------------------- |
| 1    | IDA123<br>ID1XYZ<br>IDA1B2C3 | Altsystem XY<br>  <br>Portal XY |

> Alternativ kann jeder Eintrag des wiederholbaren Feldes auch in eine eigene Spalte geschrieben werden. In unserem Beispiel wären es für die drei Einträge also insg. 6 Spalten ("weitere_id1", "weitere_id1_typ", "weitere_id2", "weitere_id2_typ", "weitere_id3", "weitere_id3_typ"). Beim Import ist allerdings zu beachten, dass dieser mehrstufig erfolgen muss, da man beim Mapping das Ziel-Feld immer nur einmal auswählen darf. Im ersten Durchlauf mappt und importiert man also die erste Spalte. Im zweiten Durchlauf nur die zweite, etc. Wichtig ist, dass in diesem Fall unter "Import-Einstellungen" die Option "Mehrfachfelder anfügen" aktiviert wird, damit die Einträge im Mehrfachfeld ergänzt und nicht jedes mal überschrieben werden.

<br>

## Dateien

Der Import von Dateien wird bei den Beispielen erläutert.

<br>

## Plugins

Um Inhalte in Custom Data Fields zu importieren, legen Sie am Besten zunächst manuell einen Datensatz in easydb an und exportieren diesen als [CSV](../../../features/export). Dort können Sie sich die Struktur des Inhalt anschauen. Dieser variiert je nach Plugin. Teilweise werden für den Import nicht alle Informationen benötigt, sondern können durch den Custom-Data-Updater nachträglich automatisiert ergänzt werden. Weitere Informationen finden Sie bei den jeweiligen [Plugins](https://github.com/programmfabrik).

Für den GND-Custom-Data-Type sind folgende Angaben ausreichend:

```text
{
  "conceptURI": "http://d-nb.info/gnd/118868284",
  "conceptName": "Jobs, Steve  (1955 - 2011)"
}
```



Für den GVK-Custom-Data-Type sind folgende Angaben ausreichend:

```text
{
  "conceptURI": "http://uri.gbv.de/document/gvk:ppn:1039947670",
  "conceptName": "K. Lynch, „Steve Jobs“. Harvard Common Press, Minneapolis, 2018."
}
```



Im Mapping ist lediglich das entsprechende Ziel-Feld auszuwählen. Es gibt keine weiteren Optionen.
