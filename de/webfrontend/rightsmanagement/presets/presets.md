# Voreinstellungen für Freigaben

Der easydb Administrator kann mithilfe der **Voreinstellungen für Freigaben** Profile für Berechtigungen vordefinieren. Benutzern stehen diese vordefinierten Berechtigungen für die Freigabe von *Datensätzen* und *Mappen* zur Verfügung.

> HINWEIS: Benutzer, die nicht über das System-Recht *allow_custom_enabled_in_preset_enabled_acl* oder *root* verfügen, können Zugriffrechte für *Mappen* und *Datensätzen* nur aus diesen vordefinierten Berechtigungen wählen und anderen Benutzern erteilen. Es ist deshalb wichtig, dass für diese Benutzer Voreinstellungen angelegt sind.

Voreinstellungen beinhalten zum einen *Berechtigungen* und ggfs. auch *Tagfilter*. Welche Berechtigungen und Tags zur Verfügung stehen, richtet sich nach dem Kontext (*Mappen* oder *Datensatz*) und nach der idividuellen Konfiguration Ihrer easydb.

[Übersicht möglicher Rechteeinstellungen in easydb](../...md#rechte)

## Voreinstellungen für Freigaben einrichten (easydb-Admin)

![Voreinstellungen](voreinstellungen allgemein.png)

Wählen Sie im Menü unter Rechtemanagement *Voreinstellugen* aus. Dann wählen Sie den Kontext (*Mappen* oder *Datensatz*), für den ein Profil mit vordefinierten Berechtigungen erstellt werden soll.

Bereits angelegte Voreinstellungen, werden daneben in einer *Liste* angezeigt. Nutzen Sie <code class="button">+</code> und <code class="button">-</code>, um neue Voreinstellungen hinzuzufügen oder bestehende zu löschen. Sie können die Reihenfolge der Voreinstellungen in der Liste per Drag & Drop verändern. Die neue Reihenfolge wird sofort gespeichert, und steht Benutzer entsprechend sortiert zur Verfügung.

## Editor

Im *Editor* (wie im Screenshot oberhalb) erscheint die neu hinzugefügte oder ausgewählte bestehende Voreinstellung zur Bearbeitung.

### Allgemein

|Feld|Erklärung|
|--|--|
|ID|Wird mit dem Speichern von easydb automatisch vergeben.|
|Name|Der Name der Voreinstellung wie sie dem Benutzer im Pulldown erscheint. Mehrsprachig.|
|Beschreibung|Eine Beschreibung was die Voreinstellung macht. Der Benutzer sieht diese Beschreibung als Tooltip.|

> HINWEIS: Beachten Sie, dass für das <code class="button">Speichern</code> einer neuen Voreinstellung mindestens der Name und eine Berechtigung unter dem Reiter *Berechtigungen* vergeben sein muss.


### Rechte

Im Reiter *Berechtigungen* finden Sie die, für die Voreinstellung konfigurierten, Rechte. Die Liste der Rechte finden Sie [hier](../...md#rechte).

![Berechtigungen](voreinstellungen rechte.png)

### Tagfilter

Im Reiter *Tagfilter* finden Sie die, für die Voreinstellung konfigurierten, Tagfilter. Eine Erklärung zu den Tagfilter finden Sie [hier](../...md#tagfilter).

> HINWEIS: Beachten Sie, dass Sie hier Zugriff auf alle Tags haben, aber ggfs. durch Konfiguration im [Objekttyp](../objecttypes/objecttypes.md) oder [Pool](../pools/pools.md) weniger Tags zur Verfügung stehen, um den Tagfilter tatsächlich anzuwenden.

![Tagfilter](voreinstellungen tagfilter.png)

