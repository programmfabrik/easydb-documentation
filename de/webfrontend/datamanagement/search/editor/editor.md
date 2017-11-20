# Eingabe


Die Eingabe, das Verändern, Neu-Anlegen etc. von Datensätzen wird in easydb im sogenannten **Editor** vorgenommen. Je nachdem von wo der Editor aufgerufen wird, wird er in verschiedenen Größen angezeigt. Funktional unterscheiden sich die verschiedenen Größen nur wenig.

|Editor|Aufruf|Datei-Vorschau|Historie|
|--|--|--|--|
|Sidebar|Durch Klick auf einen Datensatz aus dem Suchergebnis oder aus der Mappen-Vorschau.|X|-|
|Vollbild|Bei der Benutzung des Kontext-Menüs aus dem Suchergebnis heraus und bei *Listen* im Administrations-Bereich.|X|X|
|Gruppeneditor|Kontext-Menü nach Selektion von mehreren Datensätzen im Suchergebnis.|-|-|
|Popover|Kleiner Editor erreichbar aus Experten-Suche und aus den anderen Editoren, wenn verlinkte Datensätze gesucht werden.|-|-|

Die Datei-Vorschau im Editor kann über <i class="fa fa-picture-o" aria-hidden="true"></i> aktiviert und deaktiviert werden. Sie präsentiert alle Dateien eines Datensatzes (soweit in der Maske angegeben) in einem Vorschau-Browser. Sie stellt z.B. [Zoomer](../../features/datatypes/datatypes.html#tools) und [Office-Viewer](../../features/datatypes/datatypes.html#tools) zur Verfügung.

> HINWEIS: Je nach Datentyp gibt es unterschiedliche Ausprägungen von Eingabefeldern. Mehr Informationen dazu finden sie [hier](../../features/datatypes/datatypes.html).

## Funktionen im Editor

|Button|Erklärung|
|--|--|
|<code class="button">Speichern</code>|Speichert den Datensatz oder die Datensätze (Neu) oder aktualisiert die Datensätze (Gruppeneditor).|
|Pflichtfeld|Pflichtfelder müssen ausgefüllt sein, um speichern zu können. Besteht ein Pflichtfeld aus mehreren Feldern für Mehrsprachigkeit, reicht es aus, wenn eine Sprache (=Feld) ausgefüllt wird.|
|Kommentar (Checkbox)|Wenn gesetzt, wird vor dem Speichern ein Kommentar abgefragt, der dann in der Historie angezeigt wird. Wenn in der Maske vorgesehen, kann der Kommentar verpflichtend sein und Sie können die Checkbox nicht abwählen.|
|<code class="button">Kopieren</code>|Öffnet eine ungespeicherte Kopie des aktuellen Datensatzes zur Bearbeitung als neuen Datensatz.|
|<code class="button">Löschen</code>|Löscht den aktuellen Datensatz. Beachten Sie, dass in der aktuellen easydb Version gelöschte Datensätze nicht wieder auffindbar sind. easydb speichert aber alle alten Versionen des gelöschten Datensatzes.|
|<code class="button"> < </code> & <code class="button"> > </code>|Blättern Sie zum vorherigen oder nächsten Treffer. Bei Neu-Eingabe springen Sie damit in der linken Leiste einen Datensatz vor oder zurück.|
|<code class="button">Dateivorschau</code>|Schaltet die Datei-Vorschau an oder aus.|
|<code class="button">Änderungshistorie</code>|Blendet die Änderungshistorie ein oder aus (siehe unten).|
|<code class="button">Maske</code>|Schaltet die Maske um, ggfs. müssen Sie vorher speichern, um Ihre Daten nicht zu verlieren.|


## <a name="history"></a>Änderungshistorie

![Änderungshistorie im Vollbild-Editor](historie.png)

In der Änderungshistorie lassen sich frühere Versionen des Datensatzes einblenden. Angezeigt wird wer wann den Datensatz geändert hat und der Kommentar, sofern einer angelegt wurde.


# Bearbeiten im Gruppeneditor

Im Gruppeneditor können Sie für einen Objekttyp gleichzeitig bis zu 1000 Datensätze aktualisieren. Dafür können Sie einzelne oder mehrere Felder auswählen. Die Aktualisierung je Datensatz beschränkt sich dann auf die angegebenen Felder, andere Felder bleiben von der Aktion unberührt.

![Gruppeneditor](editor gruppen.png)

Sie sehen auf der linken Seite das erste Element in der Liste, die *Vorlage*. Eingaben für Aktualisierungen werden in dieser Vorlage vorgenommen. Die einzelnen Datensätze unterhalb der Vorlage zeigen die Datensätze in der Detail-Ansicht mit aktuellen Daten ohne Berücksichtigung der Aktualisierung.

Markierte Datensätze können mit <i class="fa fa-minus"></i> aus der Liste entfernt werden.

Jedes Feld verfügt links über eine Checkbox. Diese muss aktiviert sein, um dieses Feld im Datensatz zu aktualisieren.

Wenn Sie <code class="button">Speichern</code> klicken, wird der Aktualisierungs-Prozess gestartet.

Die Eingabe der Felder folgt denselben Regeln, wie die Eingabe bei einzelnen Datensätzen. Für einige Datentypen gibt es im Gruppeneditor noch Spezial-Funktionen:

## Rechte-Listen

|Einstellung|Erklärung|
|--|--|
|Berechtigungen hinzufügen|Fügt die neu eingegebenen Rechte-Zeilen je Datensatz hinzu.|
|Berechtigungen ersetzt|Ersetzt die angegebenen Rechte-Zeilen je Datensatz. Dabei wird nur der Benutzer bzw. die Gruppe verglichen. *If the who attribute is empty, its rights will be appended to all existing ACL entries*|
|Berechtigungen entfernen|Entfernt die angegebenen Rechte-Zeilen je Datensatz. Dabei wird nur der Benutzer bzw. die Gruppe verglichen. *If the who attribute is empty, its rights will be appended to all existing ACL entries*|
|Alle Berechtigungen entfernen|Entfernt alle Rechte-Zeilen an jedem Datensatz.|

## Tags

|Einstellung|Erklärung|
|--|--|
|Tag(s) hinzufügen|Tags die noch nicht gesetzt sind, werden je Datensatz gesetzt.|
|Tag(s) ersetzen|Die angegebenen Tags ersetzen die bestehenden Tags je Datensatz.|
|Tag(s) entfernen|Die angegebenen Tags entfernen.|
|Alle Tags entfernen|Alle Tags in jedem Datensatz werden entfernt.|

## Mehrfach-Felder

|Einstellung|Erklärung|
|--|--|
|Am Ende hinzufügen|Fügt die Mehrfach-Felder-Zeilen ans Ende bei jedem Datensatz hinzu.|
|Am Anfang hinzufügen|Fügt die Mehrfach-Felder-Zeilen am Anfang bei jedem Datensatz hinzu.|
|Alle ersetzen|Fügt die Mehrfach-Felder-Zeilen jedem Datensatz hinzu, löscht vorher alle bestehenden.|
|Entfernen, wenn gesetzt|Entfernt Mehrfach-Felder am Datensatz, wenn die gesetzten Felder identisch sind.|
|Alle entfernen|Entfernt alle Mehrfach-Felder am Datensatz.|

## Ja/Nein-Felder (Boolesch)

Boolesche Variablen mit Ja/Nein werden über eine Checkbox bedient. Über Masken lässt sich definieren, wie Einträge dieses Feldtyps in der Detailansicht angezeigt werden. Siehe hierzu die Einstellung in [Optionen](../../webfrontend/administration/datamodel/mask/mask.md#definition) für Ja/Nein-Felder.








