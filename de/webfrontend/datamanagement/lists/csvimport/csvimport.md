# CSV-Importer

easydb erlaubt den Import von Datensätzen und Benutzern über CSV (*UTF-8* oder *UTF-16*). Erreichbar ist der CSV-Importer im Menü unter *Listen* unten in der Sidebar über das <i class="fa fa-cog"></i>-Symbol.

![CSV-Importer](csv_importer.png)

## Funktionsumfang

* Importieren von einfachen Objekttypen
* Importieren von hierarchischen Objekttypen
* Importieren von verlinkten Datensätze (einfache & hierarchische), die gleichermaßen vollständig und verlinkt angelegt werden
* Importieren einer Ebene von Mehrfach-Feldern (z.B. Schlagwörter an Medien) (weiter verschachtelte Ebenen können nicht berücksichtigt werden)
* Aktualisierungen von Datensätzen im CSV-Importer vornehmen
* Anlegen von neunen Datensätzen im CSV-Importer vornehmen

### Unterstützte Feldtypen

- Einzeiliger Text
- Mehrzeiliger Text
- Einfacher Text (String)
- Datum
- Datum + Zeit
- Verlinkte Datensätze (auch hierarchisch)
- Zahl (ganzzahlig)
- Kommazahl (2 Stellen)
- Ja/Nein-Feld (Boolesch)
- Dateien (Siehe [Dateien importieren](../importfiles/importfiles.html))
- Alle Custom-Datentypen

Falls Sie Unterstützung für andere Typen benötigen, senden Sie bitte Ihre Anfrage an unseren Support.

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

Für die Ziel-Spalten sind folgende Format zu beachten:

### Einfache Felder (Text, Boolean, Ganz- und Kommazahlen)

Hier verwenden Sie den Namen der Spalte, wie im Datenmodell angegeben. Dem Namen kann optional der Namen des Objekttyps vorangestellt werden. Für eine Spalte **titel** im Objekttyp **medien** wäre das entweder **titel** oder **medien.titel**.
Für Ja/Nein-Felder (Boolean) verwenden Sie "1" für Ja und "0" für Nein.
Ganzzahlen müssen ohne Nachkommastellen eingetragen werden. Kommazahlen dürfen zwei Nachkommastellen haben, die jedoch mit einem "." angehängt werden müssen.
Beispiel mit:
- Titel: Einzeiliger Text
- Beschreibung: Mehrzeiliger Text
- Bauprojekt: Boolean
- Dauer: Ganzzahl
- Kosten: Kommazahl

|Titel|Beschreibung|Bauprojekt|Dauer|Kosten|
|---|---|---|---|---|
|Hausbau|Keine Beschreibung.|1|2|2.5|
|Wohnungsausbau|"Eine Mehrzeilige<br>Beschreibung<br>wird in Anführungszeichen<br>gestellt."|1|4|17.85|
|Fuchsbau|Keine Beschreibung.|0|1|0|


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

Hierarchie-Ebenen werden mit "#&lt;Ebene&gt;" durchnummeriert. Beachten Sie, dass die Numeriung mit 0 beginnt. Für zusätzliche Informationen wie z. B. *Bermerkungen* kann eine Spalte am Ende optional hinzugefügt werden.

### Verlinkte Objekttypen

Um verlinkte Datensätze im CSV anzugeben, verwenden Sie den Namen der Spalte (optional mit dem Objekttyp) und darauffolgend den Namen der Spalte im verlinkten Objekttyp. Statt den Namen der Ziel-Spalte im Objekttyp anzugeben, können Sie auch die Objekt-ID des verlinkten Datensätzes direkt angeben.

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

Sie können optional Begriffe in Anführungszeichen schreiben. Wenn der Begriff ein &lt; oder &gt; enthält, müssen Sie Anführungszeichen verwenden. Wenn Trenner innerhalb eines Begriffs vorkommen, werden diese durch die Anführungszeichen so übernommen. Wenn ein Begriff mit Anfürhungszeichen übernommen werdwen soll, muss dieser inklusive der Anführungszeichen in Anführungszeichen (also doppelte Anführungszeichen) gesetzt werden.

### Mehrfachfelder

Mehrfachfelder werden im Spalten-Namen mit dem vollen Pfad zum Feld referenziert. Beachten Sie, dass Sie nur die erste Ebene der Mehrfach-Felder mit dem CSV-Importer importieren können. Wenden Sie sich an den Support, wenn Sie tiefere Verschachtelungen importieren wollen.

|titel|personen[].person#name|personen[].person#vorname|schlagworte[].schlagwort#name|
|---|---|---|---|
|Bild mit 4 Personen|Lee Lewis<br>Perkins<br>Presley<br>Cash|Jerry<br>Carl<br>Elvis<br>Johnny|Schlagwort 1<br>Schlagwort 2<br>Schlagwort 3|
|Bild mit 2 Personen|Allen<br>Jackson|Woody<br>Michael|Schlagwort 1<br>Schlagwort 2<br>Schlagwort 3|

Mehrfach-Felder werden zeilenweise erzeugt. Für das erste Beispiel "Bild mit 4 Personen" entstehen demnach aus den Personen-Mehrfach-Feldern 4 Zeilen mit den Einträgen *Jerry Lee Lewis*, *Carl Perkins*, *Evlis Presley* und *Johnny Cash*. Um also Datensätzen mit mehereren Einträgen in einem Mehrfachfeld anzulegen, müssen diese innerhalb der Trenner durch Zeilenumbrüche getrennt werden. In einem Texeditor ohne weitere Formatierung ergibt sich folgende Struktur für den ersten Datensatz in der Tabelle:

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

Es gibt die Möglichkeit Dateien über URL mit dem CSV Importer zu importieren. Die Konfigurationsoptionen sind in Kapitel [Dateien importieren](../importfiles/importfiles.html) zu finden.

### Gruppen (nur Benutzer-Import)

Mit dem Spalten-Namen "_groups#find" können Sie Gruppen zu Benutzern hinzufügen. Die Gruppen werden kommasepariert angegeben. Es wird zunächst die ID gesucht, dann der interne Name, dann der Displayname (in allen Sprachen), um die Gruppe zu finden und zuzuordnen.

>HINWEIS: Es können nur easydb-Gruppen verknüpft werden, keine Custom-Groups und keine System-Gruppen.

## Vorbereitung

Die CSV-Datei wird hochgeladen und es werden folgende Einstellung vorgenommen:

|Einstellung|Beschreibung|
|---|---|
|CSV-Feldnamen|Zeile, in der die Spalten-Namen stehen.|
|Ziel-Feldnamen|Zeile, in der die Ziel-Feld-Namen stehen.|
|Objekttyp|Objekttyp, der importiert werden soll.|
|Pool|Angabe des Pools. Der Pool wird nur beim Einfügen von Datensätzen gesetzt.|
|Maske|Maske, die für den Import verwendet werden soll.|
|Feld zum Update|Angabe eines Feldes, welches zum Suchen der Datensätze dient, wenn Sie ein Update machen möchten. Hier wählen Sie auch das Datei-Feld aus, wenn Sie Dateinamen in Ihrem CSV angegeben haben.|
|---|Bei mehrsprachigen Feldern hat man dann die Möglichkeit den Abgleich über eine bestimmte Sprache zu machen (z.B. name#de-DE oder name#en-US). Um die Auswahl zu aktivieren, legen Sie im Reiter Mapping fest, für welche Felder, welche Sprachen zur Verfügung stehen sollen.|
|Mehrfachfelder anfügen|Mit dieser Option werden angegebene Mehrfach-Felder hinzugefügt und nicht wie gewöhnlicherweise bei einem Update ersetzt.|
|Verlinkte Datensätze anlegen|Legen Sie fest, ob verlinkte Datensätze vor dem eigentlich Import angelegt werden sollen oder nicht. Ein Einfügen oder Aktualisieren von Datensätzen mit neuen verlinkten Datensätzen ist bei ausgeschalteter Option nicht möglich.|
|Kommentar|Kommentar zum Speichern der Datensätze.|
|Paket-Größe|Größe der Verarbeitungs-Pakete die nach und nach zum Server geschickt werden.|

### Aktionen

|Button|Beschreibung|
|---|---|
|Neu Einlesen|Liest das CSV neu ein und verwirft alle bereits geladenen Informationen.|
|CSV speichern|Beim Vorbereiten und nach dem Speichern entstehen Mehr-Informationen, die in das CSV zurückgeschrieben werden. Mit **CSV speichern** können Sie sich diese Informationen auf Ihren Desktop holen. Zum Beispiel werden die Datensatz-IDs in das CSV zurückgeschrieben, wenn Datensätze neu erzeugt wurden.|
|Vorbereiten...|Bereitet den CSV-Import vor. Dazu gehören das Suchen von bereits bestehenden Datensätzen und verlinkten Datensätzen. Nach der Vorbereitung können Sie in der Tabellen-Ansicht überprüfen, welche Zeilen auf welche Art und Weise vereinnahmt werden.|
|Einfügen|Startet den CSV-Import und fügt neue Datensätze ein. Zuvor werden alle unbekannten verlinkten Datensätze neu angelegt.|
|Aktualisieren|Startet den CSV-Import und aktualisiert bestehende Datensätze. Zuvor werden alle unbekannten verlinkten Datensätze neu angelegt. Beachten Sie, dass leere Spalten auch zum Server geschickt werden.|
|Einfügen + Aktualisieren|Führt beide Schritte direkt hintereinander durch.|
