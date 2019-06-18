---
![screenshot upload](C:\Users\jens\Pictures\screenshot upload.PNG)title: "101 - Mappen"
menu:
  main:
    name: "Mappen"
    identifier: "webfrontend/datamanagement/search/quickaccess/collection"
    parent: "webfrontend/datamanagement/search/quickaccess"
---
# Mappen

## Mappen erstellen und löschen

Authentifizierte Benutzer können in der Schnellanzeige über den <code class="button">+</code> -Button neue Mappen erzeugen. Mit <code class="button">-</code> kann eine im Schnellzugriff markierte Mappe wieder entfernt werden.
Markierte Datensätze können aus der Trefferanzeige per Drag & Drop in die Mappe gezogen werden. Es ist möglich, aus der Trefferanzeige heraus eine Mappe direkt zu erstellen. Hierfür muss eine Auswahl von Treffern markiert und mit der rechten Maustaste das Kontextmenü aufgerufen werden.

## Mappen im Detail

![Mappen](finder_kontext.png)

Unter den dynamischen "Such-Mappen" befinden sich Ihre eigenen Mappen und von anderen Benutzern freigegebene Mappen. Bei Klick auf <i class = "fa fa-chevron-right"> </i> *Meine Mappen* oder <i class = "fa fa-chevron-right"> </i> *Freigegebene Mappen*, werden alle Mappen angezeigt oder verborgen. Halten Sie dabei noch gleichzeitig die Strg-Taste, werden auch alle hierarchisch untergeordneten Mappen in dem Baum geöffnet. Durch Klick auf eine Mappe wird der Inhalt der Mappe rechts im Detail angezeigt. Durch Doppelklick auf einen Datensatz wird rechts daneben die Detailansicht geöffnet. In der Anzeige über dem Mappeninhalt befindet sich der Split-Button <i class="fa fa-columns"></i>, mit dem die [Suche](../../find) neben der Mappe geöffnet wird.

> HINWEISE:

> Mit Drag & Drop kann die Reihenfolge der Datensätze in der Mappe verändert werden.

> Wenn die Anzahl der Mappen einen Wert größer als 100 übersteigt, werden die Mappen in Gruppen unterteilt.

### Funktionen im Kontextmenü {#functions}

Mit Rechtsklick auf eine Mappe öffnet das Kontextmenü mit Funktionen für die Mappe. Markieren Sie Datensätze in der Mappe und öffnen von hier aus mit der rechten Maustaste das Kontextmenü, werden zusätzlich Funktionen für die Datensätze angezeigt. Über die Toolbar oberhalb der Detailansicht für die Mappe sind die Funktionen ebenfalls aufrufbar.

![Mappen](finder_mappe_suche.png)

Für Mappen stehen folgende Funktionen über das Kontextmenü bereit:

|Funktion|Kontextmenü|Erklärung|
|---|---|---|
|**Für Mappe**|||
|![](screenshot upload.PNG)|Alle auswählen|Markiert alle Datensätze, die sich in der Mappe befinden.|
|<i class="fa fa-search"></i>|In der Suche anzeigen|Erzeugt ein Suchelement in der Suche und zeigt die lokalen Inhalte der Mappe als Treffer an. Die Suche kann dann um noch weitere Suchelemente erweitert werden.|
|<i class="fa fa-search"></i>|In der Suche anzeigen (inkl. Connector)|Erzeugt ein Suchelement in der Suche und zeigt alle Inhalte der Mappe als Treffer an (inkl. Datensätze verbundener easydb's). Die Suche kann dann um noch weitere Suchelemente erweitert werden.|
|<i class="fa fa-arrows-alt"></i>|Im Vollbild anzeigen|Zeigt die Inhalte der Mappe in easydb Vollbild an.|
|<i class="fa fa-expand"></i>||Steht im Vollbildmodus zur Verfügung. Öffnet die Ansicht als Browser-Vollbild.|
|<i class="fa fa-download"></i>|Herunterladen...|Lädt die Dateien der Mappe herunter. Es öffnet sich ein Auswahldialog, in dem Einstellungen für den Download vorgenommen werden können. |
||Hochladen...|Lädt Dateien von Ihrem Computer in die Mappe hoch |
|<i class="fa fa-sign-out"></i>|Exportieren...|Öffnet das [Export-Menü](../../../features/export) zum Exportieren der Mappe.|
|<i class="fa fa-print"></i>|Drucken...|Öffnet den Drucken-Dialog für alle in der Mappe enthaltenen Datensätze. Für den Druck können die Detailansicht oder die Text-Ansicht und eine hohe oder niedrige Auflösung gewählt werden.  |
|<i class="fa fa-share"></i>|Freigabe...|Öffnet das [Freigaben-Menü](#sharecollection) für die Mappe. Darüber können Sie die Mappe anderen easydb-Benutzern zur Verfügung stellen, die Mappe per E-Mail freigeben oder einen anonymen Link zu der Mappe erzeugen.|
|<i class="fa fa-newspaper-o"></i>|Präsentation|Alle Dateien aus der Mappe werden geladen.|
|<i class="fa fa-files-o"></i>|Mappe kopieren|Mappe wird kopiert. Enthaltene Präsentation wird mitkopiert. Freigabe- und Upload-Einstellungen werden nicht kopiert.|
|<i class="fa fa-plus"></i>|Neue Mappe unterhalb...| Erzeugt eine neue, leere Mappe unterhalb dieser Mappe.|
|<i class="fa fa-cogs"></i>|Einstellungen|Öffnet das [Menü](#collectionsettings) im Reiter *Allgemein* für Einstellungen zur Mappe.|
|<i class="fa fa-pencil-square-o"></i>|Umbenennen|Name der Mappe ändern.|
|<i class="fa fa-minus"></i>|Mappe löschen...|Löscht ein Mappe. Die Datensätze in der Mappe werden dabei nicht gelöscht, sondern verbleiben suchbar in der easydb.|
|**Für Auswahl**||Diese Optionen erscheinen, wenn Datensätze in der Mappe ausgewählt sind.|
|<i class="fa fa-arrows-alt"></i>|Auswahl im Vollbild anzeigen |Zeigt die markierten Datensätze im Vollbild Modus an.|
|<i class="fa fa fa-folder-open-o"></i>|Auswahl in Mappe | Neue Mappe mit den ausgewählten Datensätzen erzeugen.|
|<i class="fa fa fa-minus-circle"></i>|(x) Datensätze entfernen |Entfernt die markierten Datensätze aus der Mappe. Die Datensätze sind weiterhin in easydb verfügbar.|
|<i class="fa fa-download"></i>| Herunterladen...|Lädt die ausgewählten Dateien der Mappe herunter. Es öffnet ein Auswahldialog, in dem Einstellungen für den Download vorgenommen werden können.  |
|<i class="fa fa-sign-out"></i>|Export...|Öffnet das [Export-Menü](../../../features/export) zum Exportieren der markierten Datensätze in der Mappe.|
|<i class="fa fa-print"></i>| Drucken...|Öffnet den Drucken-Dialog für alle in der Mappe markierten Datensätze. Für den Druck kann die Detailansicht oder die Text-Ansicht und eine hohe oder niedrige Auflösung gewählt werden. |
|<i class="fa fa-pencil"></i>| Gruppeneditor |Öffnet den Gruppeneditor zum Bearbeiten der markierten Datensätze |
|<i class="fa fa-trash-o"></i>| Datensätze löschen... |Löscht alle markierten Datensätze aus easydb. Die Datensätze stehen danach nicht mehr in easydb zur Verfügung.  |

## Freigaben {#sharecollection}

Eine Mappe kann anderen Benutzern freigegeben werden. Dazu gehören:

* Benutzer mit einem easydb Login
* Eine ganze easydb Gruppe
* Benutzer, die kein eigenes easydb Login haben, können per E-Mail eingeladen werden
* Links für den anonyme Zugriff von Extern

![Mappe freigeben](share_collection_de.jpg)

|Funktion| |Erklärung|
|---|---|---|
|<i class="fa fa-plus"></i>|Benutzer/Gruppe/E-Mail|Erstellt eine neue Freigabe für diese Mappe. Suchen Sie den Benutzer, die Gruppe oder die E-Mail, für die Sie die Mappe freigeben möchten. Wenn Sie eine E-Mail eingeben, die noch nicht in der easydb hinterlegt ist, haben Sie die Möglichkeit für diese E-Mail einen neuen Benutzer anzulegen. Dazu müssen Sie noch die Sprache für diesen Benutzer festlegen. |
|||Eine Freigabe für die Systemgruppe *Anonyme Benutzer* ermöglicht einen unauthentifizierten Zugriff auf die freigegebenen Inhalte. Dieser Benutzer muss im Rechtemanagement konfiguriert sein. Beim Aufruf von easydb werden die Inhalte dann angezeigt, ohne dass sich der Benutzer dafür anmelden muss. Der Link kann zur Weitergabe genutzt werden. Die Inhalte sind auch ohne den Link erreichbar. |
| |Link erzeugen für externen Zugriff|Für diese Art der Freigabe wird ein Pseudobenutzer mit einer kryptischen ID angelegt und ein Link generiert. Die freigegeben Datensätze sind **nur** über diesen Link erreichbar. Der unauthentifizierte Zugriff auf diese Mappe ermöglich dem Benutzer, auf die freigegeben Daten zuzugreifen, ohne sich anmelden zu müssen oder eine E-Mail preiszugeben. Der Link muss manuell z.B. per E-Mail an den Adressaten weitergeben werden. Klicken Sie auf <i class="fa fa-share"> </i>, um den Link anzuzeigen und für die Weitergabe zu kopieren.|
|<i class="fa fa-minus"> </i>||Entfernt die Freigabe. Sie müssen vorher die entsprechende Zeile markieren.|
|Vordefinierte Berechtigung||In diesem Pulldown wählen Sie aus, welches Recht für diese Freigabe erteilt wird. Beachten Sie, dass diese Rechte vom Administrator der easydb [vorkonfiguriert](../../../../rightsmanagement/presets) werden. Es wird der Name der Berechtigung angezeigt, nicht jedoch die Einstellungen im Einzelnen. Für jede Berechtigung kann der Administrator einen erklärenden Text hinterlegen, der als *Tooltip* erscheint, wenn Sie mit dem Mauszeiger länger auf der jeweiligen Berechtigung verweilen.|
|Ende||Terminierung der Freigabe. Geben Sie das Datum ein, an dem die Freigabe enden soll. Das Datum kann auch mit einer Uhrzeit angegeben werden. Die Eingabe erfolgt ohne Trennzeichen im Format dd.mm.yyyy & hh:mm (00:00-23:59), z.B. *12.12.2012 12:12*. |
|E-Mail||Wenn gesetzt, wird der Benutzer oder die Gruppe per E-Mail über die Freigabe informiert. Sie können im Experten-Menü eine persönliche Nachricht ergänzen. Beachten Sie, dass diese E-Mail verschickt wird, nachdem Sie gespeichert haben. Beim nächsten Aufruf des *Sharing-Popover* erscheint die Checkbox wieder leer. So haben Sie die Möglichkeit, erneut eine E-Mail zu verschicken.|
|<i class="fa fa-share"> </i>||Generierter Link. Für Freigaben des Typs "Link erzeugen für externen Zugriff" sind die geteilten Datensätze nur über diesen Link erreichbar. Für andere Typen von Freigaben kann der Link optional verwendet werden. Die Freigabeeinstellungen müssen immer erst gespeichert werden, bevor der Link kopiert wird. |
|<i class="fa fa-bars"> </i>||Zugang zum Experten-Popover (siehe nächster Abschnitt) für individuelle Berechtigungsvergabe.|

> HINWEIS: Freigaben wirken sich auch auf alle untergeordneten Mappen aus, wenn für diese nicht *Berechtigungen übergeordneter Mappen ignorieren* aktiviert ist. Die Freigabeeinstellungen müssen gespeichert werden, bevor der Link zur Freigabe kopiert wird.

### Experten-Popover für Freigaben

Freigaben können im Experten-Popover mit zusätzlichen Funktionen ausgestattet werden. Klicken Sie dazu bei der Freigabe auf <i class="fa fa-bars"></i>, um das Experten-Popover zu öffnen.

![Mappen Experten-Popover](collections share expert.png)

|Einstellung|Erklärung|
|---|---|
|Aktiv|Wenn gesetzt, ist die Freigabe aktiv. Nutzen Sie diese Checkbox, um eine Freigabe vorübergehend zu de-aktivieren. Benutzer werden über diesen Vorgang nicht informiert.|
|Benutzer/Gruppe/E-Mail/Anonym|Hier wird angezeigt, für wen die Freigabe gilt. Bei anonymen Freigaben erscheint ein Hash-Key der keine weitere Bedeutung hat und der Absicherung des Zugriffs dient.|
|Beginn|Zeitpunkt wann eine Freigabe aktiv wird. Wenn nicht gesetzt, ist die Freigabe sofort nach dem Speichern aktiv.|
|Ende|Zeitpunkt bis wann eine Freigabe aktiv bleibt. Wenn nicht gesetzt, bleibt die Freigabe immer aktiv.|
|Persistent|Mappen können mit der Checkbox *Rechte-Zeilen übergeordneter Mappen ignorieren* eigene Freigaben deklarieren. Wenn Sie *Persistent* gesetzt haben, kann diese Freigabe in untergeordneten Mappen auch durch diese Einstellung nicht mehr de-aktiviert werden.|
|Link zum Weitergeben|Für anonyme Freigaben erscheint hier ein Link, der weitergegeben werden kann. Klicken Sie auf <code class="button">Goto</code>, um den Link in einem neuen Browser-Fenster auszuprobieren.|
|Recht|Wählen Sie hier das Recht aus (siehe bei [Freigaben](#sharecollection)).|

> HINWEIS: Wenn Sie über das System-Recht *root* oder *allow_custom_enabled_in_preset_enabled_acl* verfügen, werden die [Rechte](../../../../rightsmanagement) im Einzelnen angezeigt.

## Einstellungen {#collectionsettings}

Der Dialog für Einstellung zur Mappe ist derselbe wie bei Sharing, nur das der Reiter *Allgemein* aktiv ist.

### Allgemein

Auf diesem Reiter sind allgemeine Einstellungen für die Mappe verfügbar.

|Einstellung|Erklärung|
|---|---|
|Anzeigename|Anzeigename der Mappe. Mehrsprachig.|
|Beschreibung|Beschreibung der Mappe. Mehrsprachig. Wird dem Benutzer beim Betrachten der Mappe im Mappen-View angezeigt.|
|Link zu dieser Mappe|Der Deep-Link zu dieser Mappe. Benutzen Sie den Link, wenn Sie für sich selber ein Bookmark auf diese Mappe setzen wollen oder jemandem einen Link weitergeben wollen, der ebenfalls Zugriff auf diese Mappe hat.|


### Hochladen (Hotfolder)

Mappen können genutzt werden, um direkt Dateien in die easydb zu laden. Dazu können Sie eine Mappe entsprechend konfigurieren (Hotfolder). Die Einstellungen hier wirken sich auf alle untergeordneten Mappen aus. Sie können in den untergeordneten Mappen verändert, aber nicht mehr abgeschaltet werden.

> HINWEIS: Dateien können von Ihrem Computer einer Mappe hinzugefügt werden, indem sie per Drag & Drop entweder auf das Mappensymbol in der Spalte Schnellzugriff oder direkt in die geöffnete Mappe gezogen werden.  Alternativ können Dateien mit dem Upload-Button oder über das Kontextmenü hochgeladen werden. Die Dateien werden bei diesem Vorgang in die easydb kopiert, d.h. die Datei auf Ihrem Computer bleibt erhalten.

Da die easydb mit einem flexiblen Datenmodell arbeitet, müssen Sie konfigurieren in welchem Objekttyp, Pool und in welchem Feld die hochgeladenen Dateien landen sollen. Dabei kann ein Import-Mapping konfiguriert werden. Um einen Workflow zu starten, können Sie den Datensätzen ausserdem voreingestellte Tags zuordnen.

> HINWEIS: Für jede hochgeladene Datei wird genau ein Datensatz erzeugt. Mappen, die für den Upload konfiguriert sind, erscheinen mit einem Upload-Symbol <i class="fa fa-upload"></i>.

| Einstellung | Erklärung |
|---|---|
| Objekttyp          | Der Objekttyp, für den der Datensatz erzeugt wird. |
| Pool               | Der Pool, mit dem der Datensatz verknüpft wird. |
| Maske              | Wählen Sie die Maske aus, um ein Feld festzulegen, mit welchem die Datei verknüpft wird. |
| Feld               | Wählen Sie das Feld aus, mit dem die Datei verknüpft wird. Hierbei wird auch der Import von [Serienbildern und Versionen](../../../new_objects) unterstützt. |
| Versionen erkennen | Wählen Sie aus, ob der Hotfolder gleiche Dateinamen mit verschiedenen Endungen als Versionen der selben Datei betrachten soll. |
| Serien erkennen    | Wählen Sie aus, ob der Hotfolder Serien anhand von Dateinamen erkennen soll. Dies funktioniert nur, wenn in `Feld` ein Dateifeld innerhalb eines Mehrfachfelds oder innerhalb eines revers verlinkten Objekts ausgewählt ist. |
| Mapping            | Das Mapping, welches für den Import verwendet wird. |
| Tags               | Legen Sie die *Tags* fest, die für den neu erzeugten Datensatz gesetzt werden. |
