---
title: "90 - CSV-Import"
menu:
  main:
    name: "CSV-Import"
    identifier: "webfrontend/datamanagement/lists/csvimport"
    parent: "webfrontend/datamanagement/lists"
---
# CSV-Importer - In Bearbeitung



## Funktionsumfang

* Importieren von einfachen Objekttypen
* Importieren von hierarchischen Objekttypen
* Importieren von verlinkten Datensätze (einfache & hierarchische), die gleichermaßen vollständig und verlinkt angelegt werden
* Importieren einer Ebene von Mehrfach-Feldern (z.B. Schlagwörter an Medien) (weiter verschachtelte Ebenen können nicht berücksichtigt werden)
* Aktualisierungen von Datensätzen im CSV-Importer vornehmen
* Anlegen von neuen Datensätzen im CSV-Importer vornehmen



## CSV-Datei

Sie erstellen ausserhalb der easydb eine Datei im CSV-Format. Diese Datei muss im *UTF-8*-Encoding oder *UTF-16*-Encoding vorliegen, sonst werden unter Umständen Sonderzeichen nicht korrekt importiert.

Bei der Verwendung von Microsoft Excel wählen Sie beispielsweise "Unicode-Text" zum Speichern.

Der easydb CSV-Importer hat eine automatische Erkennung für folgende Trennzeichen:

- **,** *(Komma)*
- **;** *(Semikolon)*
- **&lt;TAB&gt;**

und für die folgenden Anführungszeichen:

- **"** *(Doppelte Anführungszeichen)*
- **'** *(Einfache Anführungszeichen)*

Die Datei muss in der ersten Zeile einen Bezeichner für die Spalte enthalten. Diese Spalte wird im Rahmen des Mappings im easydb-CSV-Importer als Quell-Feld angezeigt.

In einer zweiten Spalte können Sie schon das Ziel-Feld in der easydb eingeben. Der CSV-Importer zeigt die Ziel-Spalte dann bereits im Mapping an.




### Hierarchische Textfelder

Beim Import von Haupt-Objekttypen müssen die Hierarchie-Ebenen in eigenen Spalten angegeben werden.

|ort#0|ort#1|ort#2|Bemerkung|
|---|---|---|---|
|Deutschland||||
| *Kann leer bleiben* |Brandenburg|||
|||Potsdam|*optional*|
|Italien|Trentino-Alto Adige|Bolzano||
|Italien|Lacio|Rom||

Sie können in einzelnen Zeilen den Eintrag vom Vater weglassen (siehe: *Kann leer bleiben*), wenn er in der Zeile davor steht. Der Eintrag wird an die darunterliegenden Zeilen automatisch vergeben, bis zu der Zeile, in der ein neuer Eintrag beginnt (*Hier im Beispiel bis Italien*).

Hierarchie-Ebenen werden mit "#&lt;Ebene&gt;" durchnummeriert. Beachten Sie, dass die Nummeriung mit 0 beginnt. Für zusätzliche Informationen wie z. B. *Bemerkungen* kann eine Spalte am Ende optional hinzugefügt werden.

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

#### Dateien importieren

Es gibt die Möglichkeit, Dateien über URL mit dem CSV Importer zu importieren. Die Konfigurationsoptionen sind in Kapitel [Dateien importieren](../importfiles) zu finden.

### Gruppen (nur Benutzer-Import)

Mit dem Spalten-Namen "_groups#find" können Sie Gruppen zu Benutzern hinzufügen. Die Gruppen werden kommasepariert angegeben. Es wird zunächst die ID gesucht, dann der interne Name, dann der Displayname (in allen Sprachen), um die Gruppe zu finden und zuzuordnen.

>HINWEIS: Es können nur easydb-Gruppen verknüpft werden, keine Custom-Groups und keine System-Gruppen.
