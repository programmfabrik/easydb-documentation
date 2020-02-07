---
title: "CSV-Importer"
menu:
  main:
    name: "CSV-Importer"
    identifier: "tools/csvimport"
    parent: "tools"
---
# CSV-Importer - In Bearbeitung

Über den CSV-Importer können massenhaft Daten in easydb importiert und aktualisiert werden. Hierbei kann es sich um einfache Listen, hierarchische Thesauri oder um Bild- und Objektinformationen handeln. 

Die Daten können Sie beispielsweise in Microsoft Excel, Apple Numbers oder Notepad++ erstellen. Sollten Sie mit Excel oder Numbers arbeiten, müssen Sie die Daten vor dem Import als .csv mit der Kodierung in UTF-8 bzw. UTF-16 abspeichern. Der Upload von Dateien des Typs .xls, .xlsx oder .numbers wird **nicht** unterstützt.



Bitte beachten Sie auch die [allgemeinen Hinweise](./general). Unter [Datentypen](./datatypes) können Sie nachlesen, wie die Daten in der CSV-Datei aufbereitet werden müssen. Eine Step-by-Step-Anleitung finden Sie bei den [Beispielen](./examples) und alle Optionen des CSV-Importers sind [hier](./options) beschrieben.



## CSV-Datei

### Verlinkte Objekttypen

Um verlinkte Datensätze im CSV anzugeben, verwenden Sie den Namen der Spalte (optional mit dem Objekttyp) und darauffolgend den Namen der Spalte im verlinkten Objekttyp. Statt den Namen der Ziel-Spalte im Objekttyp anzugeben, können Sie auch die Objekt-ID des verlinkten Datensatzes direkt angeben.

|schlagwort#name|kuenstler#name|kuenstler#vorname|
|---|---|---|
|Mona Lisa|da Vinci|Leonardo|
|Skrik|Munch|Edvard|

Wenn der verlinkte Objekttyp hierarchisch ist, können Sie nur eine Spalte des verlinkten Objekttyps angeben (z.B. "ort#name" nicht aber "ort#name_alternativ"). Die verlinkten hierarchischen Datensätze werden dann direkt erzeugt.

|titel|ort#name|
|---|---|
|Brandenburger Tor|Deutschland > Brandenburg > Potsdam|
|Colloseum|Italien > Lacio > Rom|
|Marktplatz|Italien > "Trentino-Alto Adige" > Bolzano|

Sie können optional Begriffe in Anführungszeichen schreiben. Wenn der Begriff ein &lt; oder &gt; enthält, müssen Sie Anführungszeichen verwenden. Wenn Trenner innerhalb eines Begriffs vorkommen, werden diese durch die Anführungszeichen so übernommen. Wenn ein Begriff mit Anführungszeichen übernommen werden soll, muss dieser inklusive der Anführungszeichen in Anführungszeichen (also doppelte Anführungszeichen) gesetzt werden.

### Mehrfachfelder

Mehrfachfelder werden im Spalten-Namen mit dem vollen Pfad zum Feld referenziert. Beachten Sie, dass Sie nur die erste Ebene der Mehrfach-Felder mit dem CSV-Importer importieren können. Wenden Sie sich an den Support, wenn Sie tiefere Verschachtelungen importieren wollen.

|titel|personen[].person#name|personen[].person#vorname|schlagworte[].schlagwort#name|
|---|---|---|---|
|Bild mit 4 Personen|Lee Lewis<br>Perkins<br>Presley<br>Cash|Jerry<br>Carl<br>Elvis<br>Johnny|Schlagwort 1<br>Schlagwort 2<br>Schlagwort 3|
|Bild mit 2 Personen|Allen<br>Jackson|Woody<br>Michael|Schlagwort 1<br>Schlagwort 2<br>Schlagwort 3|

Mehrfach-Felder werden zeilenweise erzeugt. Für das erste Beispiel "Bild mit 4 Personen" entstehen demnach aus den Personen-Mehrfach-Feldern 4 Zeilen mit den Einträgen *Jerry Lee Lewis*, *Carl Perkins*, *Elvis Presley* und *Johnny Cash*. Um also Datensätzen mit mehreren Einträgen in einem Mehrfachfeld anzulegen, müssen diese innerhalb der Trenner durch Zeilenumbrüche getrennt werden. In einem Texteditor ohne weitere Formatierung ergibt sich folgende Struktur für den ersten Datensatz in der Tabelle:

```csv
"titel";"personen[].person#name";"personen[].person#vorname";"schlagworte[].schlagwort#name"
"Bild mit 4 Personen";
"Lee Lewis
Perkins
Presley
Cash";"Jerry
Carl
Elvis
Johnny";"Schlagwort 1
Schlagwort 2
Schlagwort 3"
```

### Dateien

Sie können mit dem CSV-Importer bereits vereinnahmte Dateien (z.B. durch den Hotfolder), um Metadaten anreichern, wenn die Dateien mit einem eindeutigen Dateinamen hochgeladen wurden, den Sie im CSV verwenden. Dazu geben Sie den Spalten-Namen des Datei-Feldes an.

>HINWEIS: Ebenfalls kann über ein separates "Filesystem2CSV" Python-Skript (Siehe www.github.com/programmfabrik) eine hierarchische Ordnerstruktur, in der die zu importierenden Daten liegen, in einer CSV-Datei gespeichert werden. Über diesen Weg können Ordnernamen in easydb zum Beispiel als (hierarchische) Kategorien oder Schlagwörter eingelesen werden.

