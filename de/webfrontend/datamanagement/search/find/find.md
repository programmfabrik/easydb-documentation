# Suche

![Hauptsuche](mainsearch.png)

Die Hauptsuche erreichen Sie über den Menüpunkt Recherche. Dies ist standardmäßig auch die Ansicht nach dem Benutzer-Login.

## Automatische Vervollständigung

Wenn Sie anfangen Ihre Sucheingabe in das Suchfeld einzugeben, werden Vorschläge basierend auf dem eingegebenen Wort oder Worten generiert. easydb sucht dabei nach passenden Wörtern und auch nach passenden verlinkten Datensätzen.

![Automatische Vervollständigung](autocomplet.png)

Sie können ein gefundenes *Token* oder einen verlinkten Datensatz auswählen (Cursor-hoch/runter + Return oder Maus). Der ausgewählte Eintrag erzeugt dann einen Suchbegriff im Suchfeld. Es können mehrere Suchbegriffe hinzugefügt und mit Befehlen (Suchoperatoren) kombiniert werden.

## Und/Oder-Verknüpfungen

Um eine Kombination von Suchbegriffen zu erzeugen, können mithilfe der Booleschen Logik folgende Einträge über Tastenkombinationen eingegeben werden:

|Taste|Such-Operator|Erläuterung|
|--|--|--|
|<code class="button">-</code>|<code class="token">NOT</code>|Der nachfolgende Suchbegriff wird mit "Nicht" gesucht.|
|<code class="button">+</code>|<code class="token">AND</code>|Der nachfolgende Suchbegriff wird mit "Und" verbunden.|
|<code class="button">,</code>|<code class="token">OR</code>|Der nachfolgende Suchbegriff wird mit "Oder" verbunden.|
|<code class="button">(</code>|<code class="token">(</code>|Klammer für logische Zusammenhänge.|
|<code class="button">)</code>|<code class="token">)</code>|Klammer für logische Zusammenhänge.|


>Benutzen Sie die Tastatur, um mit Cursor links und Cursor rechts die Suchbegriffe zu durchlaufen. Benutzen Sie <code class="button">Backspace</code> oder <code class="button">Delete</code>, um einen Suchbegriff zu löschen. Suchbegriffe können nicht geändert werden, Sie können sie nur löschen und wieder neu eingeben.

## <a name="pool"></a>Objekttypen/Pools

Die Suche läuft standardmäßig über alle Pools und Objekttypen in denen sich Datensätze befinden, die Sie mindestens Lesen dürfen. Klicken Sie auf <code class="button">Objekttypen/Pools</code>, um diesen Such-Filter anzupassen.

![Objekttypen/Pools](objekttypen+pools.png)

Benutzen Sie die Checkboxen um einzelne Objekttypen oder Pools zu wählen oder abzuwählen. Halten Sie <code class="button">Alt</code> gedrückt um alle Checkboxen einer Ebene auf einmal umzuschalten.

Klicken Sie auf das <i class="fa fa-info"></i>, um Informationen zu dem Objekttyp oder Pool zu erhalten. Es werden hier Ansprechpartner und ggfs. eine Beschreibung angezeigt.

## <a name="expert"></a>Expertensuche

Um komplexere Filter für die Suche zu definieren klicken Sie auf <i class="fa fa-sliders"></i> rechts im Suchfeld. Durch die Eingabe von Begriffen in die Suchfelder können Sie die Suche für ein oder mehrere Felder definieren. Die Einträge werden als Suchbegriffe in das Suchfeld übernommen.

![Expertensuche](expertensuche.png)

Sie können auf andere Objekttypen zugreifen, wenn Sie das Pulldown <code class="button">Alle Objekttypen</code> benutzen. Dann wird der Suchbegriff auf einen Objekttyp beschränkt. Wenn Sie mehrere Objekttypen einzeln durchsuchen wollen, müssen Sie mehrere Experten-Suchen aufrufen und jeweils einzelne Suchbegriffe in das Suchfeld übernehmen.

Die Checkbox in der rechten Spalte sucht *Datensätze ohne Eintrag*, d.h. wenn Sie beispielweise bei einem Feld mit Namen *Beschreibung* diese Checkbox anwählen, und dann auch <code class="button">In die Suche übernehmen</code> klicken, filtern Sie alle Datensätze bei denen das Feld *Beschreibung* leer ist.

In *Alle Objekttypen* zeigt die Nebensuche im oberen Teil unter *Verknüpfte Objekttypen* gemeinsame verlinkte Objekttypen und ggfs. den Typ *Datei* der gemeinsam durchsucht werden kann.

In *Gemeinsame Felder* sind die Felder angezeigt, die begrifflich in allen Objekttypen vorkommen. Beachten Sie, dass hier der übersetzte Name zum Vergleich herangezogen wird, nicht der Datenbank-Feldname.

Innerhalb einzelner Objekttypen wird dann in *Gemeinsame Felder* angezeigt, wenn das Feld in mehr als einer Maske vorkommt.

>HINWEIS: Die Sortierung in der Expertensuche ist alphabetisch, da sie sich auf mehrere Masken beziehen kann. Aus diesem Grund ist es nicht möglich die Reihenfolge der Felder wie in einer Maske anzuzeigen.


## Sortierung

Das Suchergebnis kann nach einem Kriterium oder nach zwei Such-Kriterien sortiert werden.

Je nach gewählter Objekttypen/Pool-Auswahl stehen hier verschiedene Felder zur Verfügung. Felder werden nach ihrem lokalisierten Namen zusammengefasst.

![Sortierung](sortierung.png)

Bei einigen Feldern kann neben der Sortierrichtung noch das Sortierattribut ausgewählt werden, so z.B. bei Dateien wo nach *Dateigröße*, *Datei-Klasse* und *Format* sortiert werden kann.

Für einige Datentypen wird bei einer Sortierung auch eine Gruppierung aktiv, die Zwischen-Überschriften im Such-Ergebnis einblendet.

Attribute für ausgewählte Feldtypen:

|Datentyp|Attribut|Erläuterung|
|--|--|--|
|Datei|Dateigröße|Sortiert nach der Dateigröße in Bytes.|
| |Art, Format|Sortiert zuerst nach Datei-Klasse und darin nach dem Format.|
| |Format|Sortiert nur nach dem Format.|
|Changelog|Angelegt|Sortiert nach dem Zeitpunkt wann ein Datensatz angelegt wurde.|
| |Geändert|Sortiert nach dem Zeitpunkt wann ein Datensatz zuletzt geändert wurde.|
|Datums-Bereich|Datum von|Sortiert nach dem *von*-Datum.|
| |Datum bis|Sortiert nach dem *bis*-Datum.|


## Anzeige

Die Anzeige im Suchergebnis schalten Sie mit den Auswahlbuttons über den Treffern ![Pulldown](anzeige_pulldown.png) zwischen Standard (Galerie), Textansicht und Tabelle um. Klicken Sie auf <i class="fa fa-angle-down"></i>, um die Anzeigeoptionen für die jeweilige Anzeigeauswahl zu verfeinern.

### Anzeigeoptionen

#### Anzeigeoption *Standard*

|Einstellung|Auswahl|Erläuterung|
|--|--|--|
|Größe|Klein|Kleinste Vorschaugröße|
| |Mittel|Mittlere Vorschaugröße|
| |Groß|Größte Vorschaugröße|
|Format|Füllen|Ausfüllende Vorschau entsprechend des Seitenverhältnisses des Thumbnails |
| |Thumbnail| Vorschau mit vollständigen Thumbnail unter Berücksichtigung des Seitenverhältnisses |
| |Ohne Rand|Ausfüllende Vorschau ohne Berücksichtigung des Seitenverhältnis des Thumbnails (Ausschnitt) |
|Stil|Überlagert|Anzeige zusätzlicher Informationen das Thumbnail überblendent|
| |Unterlegt|Anzeige zusätzlicher Informationen unterhalb des Thumbnails|
| |Seitlich|Anzeige zusätzlicher Informationen neben dem Thumbail|
|Kurz-Info| Checkbox |Einblendung einer Dateiinformation|
|Objekttyp| Checkbox|Einblendung des Objekttypen als Information|
|Pools| Checkbox|Einblendung des Pools als Information|
|Tags|Checkbox |Einblendung der Tags als Information|
|Treffer je Seite|Dropdown|Auswahl der Menge an Treffern, die pro Seite angezeigt werden sollen.|

#### Anzeigeoption *Text*

|Einstellung|Auswahl|Erläuterung|
|--|--|--|
|Treffer je Seite|Dropdown|Auswahl der Menge an Treffern, die pro Seite angezeigt werden.|

#### Anzeigeoption *Tabelle*

|Einstellung|Auswahl|Erläuterung|
|--|--|--|
|Anzeige in erster Spalte|Nicht anzeigen|Ohne Anzeige der Kurzinfo für Datensätze|
||Standard|Vorschau der Kurzinfo für Datensätze|
||Tags|Vorschau der Tags für Datensätze|
|Treffer je Seite|Dropdown|Auswahl der Menge an Treffern, die pro Seite angezeigt werden sollen.|

> HINWEIS: Die Anzeigeoptionen werden beim Benutzer gespeichert und stehen beim nächsten Mal so als Vorauswahl wieder zur Verfügung.

### Navigation

Für jede Seite gibt es einen eigenen Button, den Sie direkt klicken können, um zu der Seite zu gelangen. Die Beschriftung der Buttons entspricht den Nummern der Treffer im Suchergebnis.

Um eine Seite vor- oder zurückzublättern, benutzen Sie die Buttons <i class = "fa fa-chevron-left"> </i> und <i class = "fa fa-chevron-right"> </i>. Wenn Sie die Maus auf diesen Pfeilen gedrückt halten, scrollt die Anzeige der Seiten.

![Navigation im Suchergebnis](navigation.png)

## Suchfilter

Klicken Sie auf <code class="button">Filter</code>, um den *Suchfilter* zu aktivieren oder zu deaktivieren. Der *Suchfilter* gruppiert gefundene Datensätze nach verlinkten Objekttypen, Datei-Eigenschaften, Objekttypen und Pools.

![Suchfilter mit Filter-Suche](filtertree.png)

Je Block werden die Filter mit der Anzahl der dazu gehörigen Datensätze angezeigt.

Die ausgewählten Check-Boxen zeigen aktive Filter. Wenn mehr als 10 Filter je Block gefunden werden, gibt es die Möglichkeit auf <code class="button">Mehr</code> zu klicken und in dem jeweiligen Block separat nach gefilterten Begriffen zu suchen.

Das Suchfeld ist sehr einfach. Hier kann nur nach einem Begriff automatisch links- und rechtstrunkiert gefiltert werden.

Der Filter für Zeiträume bezieht sich auf alle Zeit- und Datumsfelder. Gemeint ist hiermit das Aufnahme- oder Entstehungsdatum. Nachfolgende Filteroptionen stehen dafür zur Verfügung:

* heute
* gestern
* diese Woche (*die Woche ab Montag bis Sonntag*)
* letzte Woche (*die vorherige Woche von Montag bis Sonntag*)
* dieser Monat
* letzter Monat
* dieses Jahr
* letztes Jahr

## Auswählen

Benutzen Sie die Maus, um mit einem Netz-Werkzeug Datensätze zu Ihrer aktuellen Auswahl hinzuzufügen. Wenn Sie <code class="button">ALT</code> benutzen, dann wird das Netz verwendet, um die ausgewählten Datensätze aus Ihrer Auswahl zu entfernen.


## <a name="search-context-menu"></a>Kontextmenü

An den Datensätzen im Suchergebnis können Sie ein Kontextmenü benutzen.

![Kontextmenü](kontextmenu.png)

|Auswahl|Erläuterung|
|--|--|
|Exportieren...|[Exportieren](export/export.md) des Datensatzes oder des gesamten Suchergebnisses.|
|In Sidebar bearbeiten...|Ruft den [Sidebar-Editor](editor/editor.md) in der Sidebar rechts auf.|
|In Vollbild bearbeiten...|Ruft den [Vollbild-Editor](editor/editor.md) auf.|
|Als Vorlage übernehmen|Ruft den [Vollbild-Editor](editor/editor.md) mit einer Kopie des aktuellen Datensatzes als Vorlage für neue Datensätze auf.|
|In Sidebar zeigen|Zeigt die Detail-Ansicht des Datensatzes in der Sidebar.|
|In Vollbild zeigen|Zeigt die Vollbild-Ansicht des Datensatzes.|
|Auswahl aufheben|Hebt die aktuelle Auswahl auf.|
|Auswahl exportieren...|[Exportieren](export/export.md) der ausgewählten Datensätze.|
|*Objekttyp* bearbeiten|Ruft den [Gruppeneditor](editor/editor.md#group) mit den Datensätzen auf. Beachten Sie, dass eine Bearbeitung nur pro Objekttyp erfolgen kann, deshalb wird die Auswahl in die einzelnen Objekttypen der Auswahl aufgeteilt.|
|Alle auswählen|Wählt alle Datensätze des Suchergebnisses aus (maximal 1000).|
|Auswahl filtern|Fügt dem Such-Schlitz einen Filter mit der aktuellen Auswahl hinzu. Dadurch können Sie in der Auswahl suchen.|

## Text-Suche

Die Suche verfügt über verschiedene Möglichkeiten zur Suche von Text. Dabei wird zwischen **Exakt** und **Volltext** und jeweils zwischen normaler, **Wildcard-** und **Phrasen**-Suche unterschieden.

> Die Suche macht in der Autovervollständigung Vorschläge, als würde man die exakten Begriffe mit einem angehängten * suchen.

#### Beispielobjekte
|           | Text field                         | String Field      |
|-----------|------------------------------------|-------------------| 
| objekte 1 | Alle Häuser haben eine weiße Wand. | ZHGÖ123-321       |
| objekte 2 | Benutzer-Handbuch & "LEITFADEN"    | Z HGÖ*123 _ &/    |
| objekte 3 | Benutzer-Handbuch & (LEITFADEN)    | Benutzer_Handbuch |
| objekte 4 | Benutzer_Handbuch & "Leitfaden"    | Benutzer-Handbuch |


### Datentyp **Text**

!INCLUDE "search_text.md"

Sonderzeichen die gesucht werden können: **&**, **%**, **§**, **$**, **€**.

Zahlen werden wie suchbare Zeichen behandelt.

### Datentyp **String**

!INCLUDE "search_string.md"

### Wildcard search

!INCLUDE "search_wildcard.md"
