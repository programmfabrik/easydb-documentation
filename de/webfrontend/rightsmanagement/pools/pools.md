# Pools

easydb speichert Datensätze, für deren Objekttyp *Pool-Management* aktiviert ist, in Pools ab. Pools können genutzt werden, um Datensätze:

* inhaltlich zu strukturieren
* organisatorisch zu strukturieren
* für Abläufe zu unterteieln

Pools werden in einer Hierarchie verwaltet. An oberster Stelle der Hierarchie steht der Root-Pool. Weitere Pools können gleichgeordnet und/oder hierarchisch angelegt werden. Alle Einstellungen, die in einem übergeordneten Pool gemacht werden, strahlen auf alle untergeordneten Pools aus. Diese Einstellung kann bei den untergeordneten Pools überschrieben werden.

> HINWEIS: Namensänderungen von Pools und Wasserzeichen-Einrichtung können aufwendige Neuberechnungen auf Server-Seite nach sich ziehen.

## Allgemein

Pools können vom easydb Administrator und Benutzern, die das Systemrecht zur Verwaltung von Pools haben, angelegt, verändert und gelöscht werden. Zum Anlegen eines neuen Pools, besteht die Möglichkeit einen bestehenden Pool zu kopieren, um diesen dann zu modifizieren.

![Pool-Management](rights_poolmanagement_de.jpg)

|Einstellung|Erläuterung|
|--|--|
|ID|Wird automatisch bei der Erstellung des Pools vergeben.|
|Verantwortlicher|Standardmäßig ist das der Ersteller des Pools. Als Pool-Administratoren können andere Benutzer eingetragen werden. Die Rechtekonfiguration für Pool-Administratoren lesen Sie bitte im Kapitel [Mandantenfähigkeit](../../../tutorials/mandanten/mandanten.html).   |
|Name|Name des Pools, mehrsprachig. Eine Namensänderung zieht eine komplette Neu-Indizierung aller betroffenen Datensätze mit sich, was unter Umständen einige Zeit in Anspruch nimmt.|
|Ansprechpartner|Ansprechpartner für den Pool. Wird Benutzern in der Pool-Übersicht über <i class="fa fa-info-circle"> </i> angezeigt.|
|Beschreibung|Beschreibung des Pools. Mehrsprachig. Wird dem Benutzer in der Pool-Übersicht über <i class="fa fa-info-circle"> </i> angezeigt.|
|Referenz|Wird bei für Exporte über OAI/PMH und Deeplinks verwendet. Muss *unique* sein.|
|Kurzname|Wird bei für Exporte über OAI/PMH und Deeplinks verwendet. Muss *unique* sein.|
|Export-Profil für Dublin-Core|Wird als Standard-Mapping für Dublin-Core Exporte gesetezt. Der Benutzer kann sich beim Export noch einmal für ein anderes Mapping entscheiden.|
|Export-Profil für Bilder|Standard-Mapping für den Export von Bildern. Der Benutzer kann sich beim Export noch einmal für ein anderes Mapping entscheiden, allerdings gibt es diese Möglichkeit beim einfachen Download nicht. Dort wird das hier eingestellte Mapping verwendet.|
|Import-Profil für Bilder|Standard-Mapping für den Improt von Bildern. Der Benutzer kann sich beim Improt noch für ein anderes Mapping entscheiden.|


## Wasserzeichen

Für Bilder kann easydb Pool-abhängig ein Wasserzeichen in die Bilder einrechnen. In diesem Reiter legen Sie fest, welches Bild als Wasserzeichen verwendet wird.

|Einstellung|Erläuterung|
|--|--|
|Wasserzeichen|Das Bild|
|Dissolve|Transparenz des Bildes|
|Position|Position des Wasserzeichens als Himmelsrichtung|
|Größe|Größe des Wasserzeichens|
|Kacheln|Wasserzeichen wird als Kachelbild angezeigt.|

> HINWEIS: Das für einen Pool festgelegte Wasserzeichen wird nicht automatisch an untergeordnete Pools vergeben. Die Einstellungen müssen je Pool (gleichgeordnete) und Poolebene (untergeordnete) vorgenommen werden.

## Masken

Für jeden Objekttyp, für den Pool-Management aktiviert ist, kann hier die Reihenfolge der Masken festgelegt werden, die für den Benutzer zur Anzeige von Datensätzen verwendet werden. Die an erster Stelle stehende Maske wird dann als Standardmaske ausgegeben.

![*Einstellungen für Masken*](masken.png)

|Einstellung|Erläuterung|
|--|--|
|Vom Objekttyp|Übernimmt die Einstellungen vom Objekttyp. Nur im Root-Pool verfügbar.|
|Vom übergeordneten Pool|Übernimmt die Einstellungen vom übergeordneten Pool. Nicht im Root-Pool verfügbar.|
|&lt;Maske&gt;|Bringen Sie die Masken per Drag Handle in die gewünschte Reihenfolge. *Hinweis: Wenn Sie die Maske unter die Doppellinie ziehen, wird diese nicht indiziert. Der Benutzer kann Datensätze dann nicht mit dieser Maske sehen.


## Tags

Siehe Kapitel [Objekttypen](../objecttypes/objecttypes.html#tags).

## Workflows

Siehe Kapitel [Objekttypen](../objecttypes/objecttypes.html#workflows).

## Berechtigungen

Hier stellen Sie ein, welche Rechte Benutzer und Gruppen für Datensätzen erhalten, die in diesem Pool oder in einem der untergeordneten Pools befinden.

|Einstellung|Erläuterung|
|--|--|
|Eigene Rechteliste|Wenn diese Checkbox gesetzt wird, werden Rechte aus den übergeordneten Pools nicht übernommen, es sei denn sie wurden dort als *Persistent* markiert. Diese Funktion ist für den Root-Pool nicht verfügbar.|

Alle weiteren Erklärungen zu den Rechtelisten und eine Übersicht über die Rechte finden Sie [hier](../...html#Rechte).
