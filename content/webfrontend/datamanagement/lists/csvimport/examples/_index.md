---
title: "91 - CSV-Import Beispiele"
menu:
  main:
    name: "Beispiele"
    identifier: "webfrontend/datamanagement/lists/csvimport/examples"
    parent: "webfrontend/datamanagement/lists/csvimport"
---
# Beispiele - In Bearbeitung

An dieser Stelle finden Sie für jeden in easydb verfügbaren Datentyp ein Beispiel für die Aufbereitung der Daten im CSV-Format. Für weitere Informationen schauen Sie in unsere [allgemeinen Hinweise](../general). EIne Best-Practice-Anleitung findet Sie in unseren Tutorials. Eine CSV-Datei mit allen Beispielen können Sie sich hier herunterladen.

### Einzeiliger & Mehrzeiliger Text, Einfacher Text (String)

Es empfiehlt sich die Texte in doppelte Anführungszeichen zu setzen. Sollte ein Text ein Komma, Semikolon, einen Backslash oder einen Umbruch enthalten, müssen doppelte Anführungszeichen verwendet werden.

| id   | titel (einzeiliger Text) | beschreibung (mehrzeiliger Text)                             | signatur (String) |
| ---- | ------------------------ | ------------------------------------------------------------ | ----------------- |
| 1    | Berlin bei Nacht         | Das Bild zeigt den beleuchteten Alexanderplatz bei Nacht.    | Signatur_2019_001 |
| 2    | Berliner Dom             | "Der Berliner Dom in der Mittagssonne.<br> <br>Viele Menschen liegen auf der Wiese vorm Berliner Dom." | SIgnatur_2018_002 |
| 3    | Berlin von oben          |                                                              | Signatur_2017_003 |

Im Mapping müssen jeweils nur die entsprechenden Ziel-Felder ausgewählt werden. Es gibt keine weiteren Optionen.



### Einzeiliger & Mehrzeiliger Text (mehrsprachig)

Bei mehrsprachigen Feldern werden die Inhalte für die verschiedenen Sprachen intern in getrennten Feldern gespeichert. Daher müssen die Sprachen auch in der CSV-Datei in unterschiedliche Spalten geschrieben werden.

| id   | titel_de                                        | titel_en                                 | titel_es          |
| ---- | ----------------------------------------------- | ---------------------------------------- | ----------------- |
| 1    | Deutscher Titel                                 | English title                            | Título en español |
| 2    | Hier ist nur ein deutscher Titel vorhanden      |                                          |                   |
| 3    | Diesen Titel haben wir auf Deutsch und Englisch | We have this title in German and English |                   |

Im Mapping muss für beide Spalten zunächst das gleiche Ziel-Feld ausgewählt werden. Anschließend kann die dazugehörige Sprache ausgewählt werden.



### Datum, Datum + Zeit

Beim Import von Datumsangaben wird sowohl das deutsche als auch das amerikanische Format unterstützt. 

| id   | aufnahmedatum (Datum) | aufnahmezeitpunkt (Datum + Zeit) |
| ---- | --------------------- | -------------------------------- |
| 1    | 2019-12-06            | 2019-12-09 13:39:00              |
| 2    | 24.12.2019            |                                  |
| 3    | 2018-11               | 2019-12-09                       |
| 4    | 2017                  |                                  |

Im Mapping müssen jeweils nur die entsprechenden Ziel-Felder ausgewählt werden. Es gibt keine weiteren Optionen.



### Datum (Bereich)

Das Datumsbereichsfeld zeichnet sich dadurch aus, dass die Werte intern in zwei Feldern gespeichert werden. Es gibt ein Feld "von" und "bis". Daher müssen das Start- und Enddatum auch in der CSV-Datei in zwei Spalten geschrieben werden.

| id   | datum_von  | datum_bis  |
| ---- | ---------- | ---------- |
| 1    | 2019-10-01 | 2019-10-08 |
| 2    | 2016-01    | 2018-12    |
| 3    | 2009       | 2019-12-31 |

Im Mapping muss für beide Spalten zunächst das gleiche Ziel-Feld ausgewählt werden. Anschließend kann ausgewählt werden, ob die Daten in "von" oder "bis" geschrieben werden sollen.



### Zahl (ganzzahlig), Kommazahl (2 Stellen)



| id   | anzahl (Zahl) | wert (Kommazahl) |
| ---- | ------------- | ---------------- |
| 1    | 1             | 1.40             |
| 2    | 2             | 5,80             |
| 3    | 3             | 35               |

Im Mapping müssen jeweils nur die entsprechenden Ziel-Felder ausgewählt werden. Es gibt keine weiteren Optionen.



### Ja/Nein-Feld (Boolesch)

Felder des Typs "Ja/Nein-Feld (Boolesch)" werden im easydb-Frontend als Checkbox dargestellt. Die beiden Zustände "aktiviert" und "deaktiviert" können beim Import durch "true" bzw. "1" und "false" bzw. "0" gesetzt werden. Leere Felder im CSV entsprechen "false".

| id   | original_vorhanden |
| ---- | ------------------ |
| 1    | true               |
| 2    | false              |
| 3    |                    |

Im Mapping ist lediglich das entsprechende Ziel-Feld auszuwählen. Es gibt keine weiteren Optionen. 



### Einfache Verlinkung mit flacher Liste

Ist in easydb bei einem Feld eine flache Liste hinterlegt, können diese Verknüpfungen auch über CSV-Importiert werden. Hierzu muss der zu verlinkende Eintrag noch nicht in der Liste vorhanden sein. 

| id   | kategorie       |
| ---- | --------------- |
| 1    | Personen        |
| 2    | Gebäude         |
| 3    | Veranstaltungen |

Im Mapping wählen Sie zunächst das entsprechende Ziel-Feld aus. Im Anschluss wählen Sie das Feld aus dem verlinkten Objekttyp aus. Die easydb prüft über dieses Feld, ob das Schlagwort bereits in der Liste vorhanden ist. Wenn ja, wird der vorhandene Eintrag verknüpft. Falls nicht, wird ein neues Schlagwort in der Liste angelegt und verknüpft (sofern beim CSV-Import auf dem Reiter "Datei" die Checkbox "Verlinkte Objekte anlegen" aktiviert ist).



### Einfache Verlinkung mit hierarchischer Liste

Ist in easydb bei einem Feld eine hierarchische Liste hinterlegt, können diese Verknüpfungen auch über CSV-Importiert werden. Hierzu muss der zu verlinkende Eintrag noch nicht in der Liste vorhanden sein. 

| id   | aufnahmeort                                   |
| ---- | --------------------------------------------- |
| 1    | Deutschland > Berlin                          |
| 2    | Irland > Dublin                               |
| 3    | Vereinigtes Königreich > Schottland > Glasgow |

Im Mapping wählen Sie zunächst das entsprechende Ziel-Feld aus. Im Anschluss wählen Sie das Feld aus dem verlinkten Objekttyp aus. Die easydb prüft über dieses Feld, ob der Ort bereits in der Liste vorhanden ist. Wenn ja, wird der vorhandene Eintrag verknüpft. Falls nicht, wird ein neuer Ort in der Liste angelegt und verknüpft (sofern beim CSV-Import auf dem Reiter "Datei" die Checkbox "Verlinkte Objekte anlegen" aktiviert ist). Beim Import von hierarchischen Listen kann noch der verwendete Trenner gewählt werden (">" oder "/").



### Wiederholbares Freitext-Feld

Handelt es sich bei dem Zielfeld um ein sog. Mehrfach-Feld (d.h. pro Datensatz können davon mehrere Angaben gemacht werden), müssen alle Einträge in eine CSV-Zelle geschrieben und mit Umbruch getrennt werden. Verwenden Sie doppelte Anführungszeichen, um Texte die einen Umbruch enthalten, zu importieren.

| id   | wiederholbares_freitextfeld                                  |
| ---- | ------------------------------------------------------------ |
| 1    | Erster Text<br>Zweiter Text<br>Dritter Text                  |
| 2    | "Text der einen Umbruch<br/>enthält."<br/>"Text ohne Umbruch, aber mit Komma." |

Im Mapping ist lediglich das entsprechende Ziel-Feld auszuwählen. Es gibt keine weiteren Optionen. 



### Wiederholbare Verlinkung

Handelt es sich bei dem Zielfeld um ein sog. Mehrfach-Feld in dem auf einen anderen Objekttyp verwiesen wird, müssen alle zu verlinkenden Einträge in eine CSV-Zelle geschrieben und mit Umbruch getrennt werden. Verwenden Sie doppelte Anführungszeichen, um Einträge die einen Umbruch oder Trennzeichen enthalten, zu importieren.

| id   | schlagwörter                                  |
| ---- | --------------------------------------------- |
| 1    | Sonne<br>Mond<br>Sterne                       |
| 2    | "Stadt, Land, Fluss Spiel"<br/>"Kinderspiele" |

Dies funktioniert auch, wenn der verlinkte Objekttyp hierarchisch ist:

| id   | frühere_standorte                                            |
| ---- | ------------------------------------------------------------ |
| 1    | Deutschland > Berlin<br>Irland > Dublin<br>Vereinigtes Königreich > Schottland > Glasgow |

Im Mapping wählen Sie zunächst das entsprechende Ziel-Feld aus. Im Anschluss wählen Sie das Feld aus dem verlinkten Objekttyp aus. Die easydb prüft über dieses Feld, ob der Eintrag bereits in der Liste vorhanden ist. Wenn ja, wird der vorhandene Eintrag verknüpft. Falls nicht, wird ein neuer Eintrag in der Liste angelegt und verknüpft (sofern beim CSV-Import auf dem Reiter "Datei" die Checkbox "Verlinkte Objekte anlegen" aktiviert ist). Beim Import von hierarchischen Listen kann noch der verwendete Trenner gewählt werden (">" oder "/").



### Wiederholfeld mit mehreren Feldern

Handelt es sich bei dem Ziel-Feld um ein sog. Mehrfach-Feld, welches mehr als nur ein Feld beinhaltet, so müssen diese Felder auf einzelne Spalten aufgeteilt werden. Soll mehr als nur ein Eintrag mit einem Datensatz verknüpft werden, müssen diese wieder in einer Zelle durch Umbruch getrennt werden.

| id   | weitere_ids            | id_typ                          |
| ---- | ---------------------- | ------------------------------- |
| 1    | A123<br>1XYZ<br>A1B2C3 | Altsystem XY<br>  <br>Portal XY |





### Plugins

Um Inhalte in Custom Data Fields zu importieren, legen Sie am Besten zunächst manuell einen Datensatz in easydb an und exportieren diesen als CSV. Dort können Sie sich die Struktur des Inhalt anschauen. Dieser variiert je nach Plugin. Teilweise werden für den Import nicht alle Informationen benötigt, sondern diese können durch den Custom-Data-Updater nachträglich automatisiert ergänzt werden. Weitere Informationen finden Sie bei den jeweiligen [Plugins](https://github.com/programmfabrik).

Für den GND-Custom-Data-Type sind folgende Angaben ausreichend:

| id   | personen_gnd                                                 |
| ---- | ------------------------------------------------------------ |
| 1    | "{<br>     "conceptURI": "http://d-nb.info/gnd/118559206" <br>}" |



Für den GVK-Custom-Data-Type sind folgende Angaben ausreichend:

| id   | literatur_gvk |
| ---- | ------------- |
| 1    |               |