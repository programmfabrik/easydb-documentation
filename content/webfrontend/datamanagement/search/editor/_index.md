---
title: "97 - Editor"
menu:
  main:
    name: "Editor"
    identifier: "webfrontend/datamanagement/search/editor"
    parent: "webfrontend/datamanagement/search"
---
# Eingabe


Die Eingabe, das Verändern, Neu-Anlegen etc. von Datensätzen wird in easydb im sogenannten **Editor** vorgenommen. Je nachdem von wo der Editor aufgerufen wird, wird er in verschiedenen Größen angezeigt. Funktional unterscheiden sich die verschiedenen Größen nur wenig.

|Editor|Aufruf|Datei-Vorschau|Historie|
|---|---|---|---|
|Neu-Editor|Durch Klick auf [Neue Datensätze](/de/webfrontend/datamanagement/new_objects) im Hauptmenü oder durch Drag & Drop lokaler Dateien in die Rechercheansicht|X|-|
|Sidebar|Durch Klick auf einen Datensatz aus dem Suchergebnis oder aus der Mappen-Vorschau.|X|-|
|Vollbild|Bei der Benutzung des Kontext-Menüs aus dem Suchergebnis heraus und bei *Listen* im Administrations-Bereich.|X|X|
|Gruppeneditor|Kontext-Menü nach Selektion von mehreren Datensätzen im Suchergebnis.|-|-|
|Popover|Kleiner Editor, erreichbar aus Experten-Suche und aus den anderen Editoren, wenn verlinkte Datensätze gesucht werden.|-|-|

Die Datei-Vorschau im Editor kann über <i class="fa fa-picture-o" aria-hidden="true"></i> aktiviert und deaktiviert werden. Sie präsentiert alle Dateien eines Datensatzes (soweit in der Maske angegeben) in einem Vorschau-Browser. Sie stellt z.B. [Zoomer](../../features/datatypes) und [Office-Viewer](../../features/datatypes) zur Verfügung.

> HINWEIS: Je nach Datentyp gibt es unterschiedliche Ausprägungen von Eingabefeldern. Mehr Informationen dazu finden Sie [hier](../../features/datatypes).

## Funktionen im Editor {#editor}

|Button|Erklärung|Verfügbarkeit|
|---|---|---|
|<code class="button">Bearbeiten</code>|Kann aktiviert und deaktiviert werden, um in die [Detailansicht](../editor) zu wechseln.|- Sidebar-Editor (Button) <br>- Kontextmenü in der Recherche|
|<code class="button">Speichern</code>|Speichert den Datensatz oder aktualisiert den Datensatz nach Änderungen. Im Vollbildmodus schließt der Editor nach dem Speichern.                                                           HINWEIS: Eine gleichzeitige Bearbeitung desselben Datensatzes durch mehrere Nutzer ist nicht möglich! Sollte ein Nutzer Änderungen an einem Datensatz speichern, an dem ein weiterer Nutzer arbeitet, erhält dieser eine Nachricht, dass der Datensatz gespeichert wurde. Der Editor wird neu geladen und Eingaben des zweiten Nutzers gehen verloren.|- Sidebar-Editor (Button) <br>- Vollbildeditor (Button)|
|<code class="button">Übernehmen</code>|Speichert die Änderungen am Datensatz, ohne den Editor zu schließen.|- Vollbildeditor (Button)|
|Pflichtfeld|Pflichtfelder müssen ausgefüllt sein, damit der Datensatz gespeichert werden kann. Besteht ein Pflichtfeld aus mehreren Feldern für Mehrsprachigkeit, reicht es aus, wenn eine Sprache (=Feld) ausgefüllt wird.|- Sidebar-Editor <br>- Vollbildeditor|
|Kommentar (Checkbox)|Wenn die Kommentarfunktion für die Maske aktiviert wurde, erscheint beim Speichern über dem Speichern-Button eine Kommentar-Checkbox. Bei Klick auf den Speichern-Button erscheint ein Dialog für den Kommentar, der dann in der Historie angezeigt wird. Je nachdem ob der Kommentar optional oder obligatorisch ist, kann die Checkbox aktiviert oder deaktiviert werden oder ist ausgegraut.|- Sidebar-Editor <br>- Vollbildeditor|
|<code class="button">Kopieren</code>|Erzeugt eine Kopie des aktuellen Datensatzes im Editiermodus. Bevor der Datensatz in der Datenbank angelegt wird, muss die Kopie mit Speichern bestätigt werden.|- Sidebar-Editor (Toolbar) <br>- Vollbildeditor (Button)<br> - Kontextmenü in der Recherche|
|<code class="button">Löschen</code>|Löscht den aktuellen Datensatz. Gelöschte Datensätze können in easydb nicht wieder aufgefunden werden. Alte Versionen des gelöschten Datensatzes können aber noch über direkten Zugriff auf die Datenbank nachvollzogen werden. Aktuell ist es noch nicht möglich, diese aus der Datenbank wiederherzustellen. |- Sidebar-Editor (Toolbar) <br>- Vollbildeditor (Button)<br> - Kontextmenü in der Recherche|
|<code class="button"> < </code> & <code class="button"> > </code>|Erscheint unterhalb der Vorschau bei Datensätzen, für die mehrere Dateien gespeichert werden können. Hierdurch können die angehängten Dateien durchblättert werden.  |- Sidebar-Editor <br>- Vollbildeditor|
|<code class="button">Dateivorschau</code>|Schaltet die Datei-Vorschau an oder aus.|- Sidebar-Editor (Button) <br>- Vollbildeditor (Button)|
|<code class="button">Änderungshistorie</code>|Blendet die Änderungshistorie ein oder aus (siehe unten).|- Sidebar-Editor (Toolbar) <br>- Vollbildeditor (Button)|
|<code class="button">Maske</code>|Schaltet die Maske um, ggfs. müssen Sie vorher speichern, um Ihre Daten nicht zu verlieren.|- Sidebar-Editor (Button) <br>- Vollbildeditor (Button)|
|<i class="fa fa-thumb-tack"> </i>|Verwenden und Erstellen von Vorlagen. Wenn Sie Vorlagen gespeichert haben, steht über dieses Menü die Liste verfügbarer Vorlagen bereit. <br > *Als Vorlage speichern...*: Es wird eine Vorlage auf Basis dieses Datensatzes erstellt. Es öffnet ein Dialog, in dem ein Name für die Vorlage vergeben wird. <br > *Anpassen*: Name bestehender Vorlagen anpassen oder Vorlagen löschen |- Sidebar-Editor (Toolbar) <br>- Vollbildeditor (Button)|
|Letzte Änderung | Ein Hinweis am unteren Rand der Felder zeigt an, wann der Datensatz das letzte Mal geändert wurde. |- Sidebar-Editor|

Der Gruppeneditor ist nur im Vollbildmodus verfügbar und verfügt neben den Funktionen des einfachen Editors noch über einige weitere Funktionen. Siehe dazu den Abschnitt [Gruppeneditor](#groupedit).

> HINWEIS: Vorlagen können nur pro Benutzer und je Objekttyp und/oder Maske gespeichert werden. Wenn eine Vorlage mehreren Benutzern zur Verfügung stehen soll, müssen Vorlagen auf Poolebene definiert werden. Hierdurch haben Benutzer Zugriff auf allgemeine Vorlagen und können diese in ihre eigene Vorlagenliste übernehmen.

## Änderungshistorie {#history}

![Änderungshistorie im Vollbild-Editor](historie.png)

In der Änderungshistorie lassen sich frühere Versionen des Datensatzes einblenden. Angezeigt wird, welcher Nutzer den Datensatz geändert hat, der Änderungszeitpunkt und der Kommentar, sofern einer angelegt wurde.


# Bearbeiten im Gruppeneditor {#groupedit}

Im Gruppeneditor können Sie für einen Objekttyp gleichzeitig bis zu 1000 Datensätze aktualisieren. Dafür können Sie einzelne oder mehrere Felder auswählen. Die Aktualisierung je Datensatz beschränkt sich dann auf die angegebenen Felder. Andere Felder bleiben von der Aktion unberührt.

Für die Bearbeitung im Gruppeneditor müssen Sie eine Auswahl von mehr als einem Datensatz treffen. Der Gruppeneditor steht dann über das Kontextmenü zur Verfügung. Enthält die Auswahl unterschiedliche Objekttypen, kann der Gruppeneditor im Kontextmenü über eine Auswahlliste je Objekttyp gestartet werden.

![Gruppeneditor](group_editor_de.jpg)

Der Gruppeneditor ist nur im Vollbildmodus verfügbar. Die Eingabe der Felder folgt denselben Regeln, wie die Eingabe bei einzelnen Datensätzen. Neben den allgemeinen Funktionen des Editors bietet der Gruppeneditor noch einige spezielle Funktionen:

|Funktion|Erklärung|
|---|---|
|Vorlage|Ist das erste Element links in der Anzeige der Auswahl. Über die Vorlage können alle Datensätze, die unterhalb der Vorlage gelistet sind, bearbeitet werden.|
|Ckeckbox|Vor jedem Eingabefeld ist eine Checkbox, die aktiviert werden muss, damit die Änderungen für alle Datensätze beim Speichern übernommen werden. Je Feld stehen unterschiedliche Auswahloptionen für das Hinzufügen, Ersetzen oder Entfernen von Eingaben zur Verfügung. |
|<code class="button"> < </code> & <code class="button"> > </code>|Die Paginierung erscheint, wenn mehr als 50 Datensätze für die Gruppenbearbeitung ausgewählt wurden.|
|<i class="fa fa-minus"> </i>| Entfernt den markierten Datensatz aus dem Gruppeneditor. Es kann jeweils nur ein Datensatz aus dem Gruppeneditor entfernt werden. Das Markieren mehrerer Datensätze wird in diesem Modus nicht unterstützt.|
|<i class="fa fa-clipboard"> </i>|Übernimmt die Einträge des markierten Datensatzes in die Vorlage.|
|<i class="fa fa-thumb-tack"> </i>|Speichert die Vorlage. Gespeicherte Vorlagen stehen dann bei neuen Arbeitsvorgängen im Gruppeneditor an dieser Stelle über das Auswahlmenü zur Verfügung. Vorlagen können nur pro Benutzer und Maske gespeichert werden. Beachten Sie auch den Hinweis unter [Funktionen im Editor](/de/webfrontend/datamanagement/search/editor)  |
|Paket-Größe|Standardmäßig werden die im Gruppeneditor befindlichen Datensätze in 1.000er-Pakete verarbeitet. Bei sehr komplexen Datenmodellen kann es in Ausnahmefällen zu einer Zeitüberschreitung kommen. In diesem Fall kann die Paket-Größe z.B. auf 100 Datensätze verringert werden, sodass die easydb kleinere Pakete nacheinander verarbeiten kann. |
|Kommentar|Bietet die Möglichkeit, beim Speichern einen Kommentar einzugeben. Dieser wird in der Änderungshistorie der Datensätze angezeigt. |



## Rechte-Listen

|Einstellung|Erklärung|
|---|---|
|Berechtigungen hinzufügen|Fügt die neu eingegebenen Rechte-Zeilen je Datensatz hinzu.|
|Berechtigungen ersetzt|Ersetzt die angegebenen Rechte-Zeilen je Datensatz. Dabei wird nur der Benutzer bzw. die Gruppe verglichen. *If the who attribute is empty, its rights will be appended to all existing ACL entries*|
|Berechtigungen entfernen|Entfernt die angegebenen Rechte-Zeilen je Datensatz. Dabei wird nur der Benutzer bzw. die Gruppe verglichen. *If the who attribute is empty, its rights will be appended to all existing ACL entries*|
|Alle Berechtigungen entfernen|Entfernt alle Rechte-Zeilen an jedem Datensatz.|

## Tags

|Einstellung|Erklärung|
|---|---|
|Tag(s) hinzufügen|Tags, die noch nicht gesetzt sind, werden je Datensatz gesetzt.|
|Tag(s) ersetzen|Die angegebenen Tags ersetzen die bestehenden Tags je Datensatz.|
|Tag(s) entfernen|Die angegebenen Tags entfernen.|
|Alle Tags entfernen|Alle Tags in jedem Datensatz werden entfernt.|

## Mehrfach-Felder

|Einstellung|Erklärung|
|---|---|
|Am Ende hinzufügen|Fügt die Mehrfach-Felder-Zeilen ans Ende bei jedem Datensatz hinzu.|
|Am Anfang hinzufügen|Fügt die Mehrfach-Felder-Zeilen am Anfang bei jedem Datensatz hinzu.|
|Alle ersetzen|Fügt die Mehrfach-Felder-Zeilen jedem Datensatz hinzu, löscht vorher alle bestehenden.|
|Entfernen, wenn gesetzt|Entfernt Mehrfach-Felder am Datensatz, wenn die gesetzten Felder identisch sind.|
|Alle entfernen|Entfernt alle Mehrfach-Felder am Datensatz.|

## Boolesche Variablen (Ja/Nein-Felder)

Boolesche Variablen mit Ja/Nein werden über eine Checkbox bedient. Über Masken lässt sich definieren, wie Einträge dieses Feldtyps in der Detailansicht angezeigt werden. Siehe hierzu die Einstellung in [Optionen](../../../administration/datamodel/mask) für Ja/Nein-Felder.








