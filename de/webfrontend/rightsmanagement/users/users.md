# Benutzer

Es gibt verschiedene Methoden Benutzer in easydb anzulegen. Diese werden nachfolgend unter *Benutzertypen* im Einzelnen erläutert. Benutzer können vom easydb Administrator oder von Benutzern, die das Systemrecht zur Verwaltung von Benutzern haben, angelegt, verändert und gelöscht werden. Zum Anlegen eines neuen Benutzers besteht die Möglichkeit, einen bestehenden Benutzer (ausgenommen der Benutzertyp *system*) zu kopieren, um diesen dann zu modifizieren.

![Benutzer-Management](/de/webfrontend/rightsmanagement/users/rights_user_copy.jpg)

## Allgemein


|Einstellung|Erklärung|
|--|--|
|Typ|Die unterschiedlichen Methoden in easydb Benutzer anzulegen, entsprechen verschiedenen Typen. Siehe hierfür nachfolgende Tabelle **Benutzertypen**.|
|Login|Das Login für Benutzer muss easydb-weit eindeutig sein. Es ist allerdings optional. Benutzer können so konfiguriert werden, dass sie ihr Login zum Anmelden verwenden können. Benutzer können sich aber auch mit einer E-Mail-Adresse anmelden, weshalb Login optional ist.|
|Vorname|Der Vorname des Benutzers.|
|Name|Der Nachname des Benutzers.|
|Anzeigename|Der Anzeigename ist der Name, den andere Benutzer sehen, wenn sie Information über diesen Benutzer angezeigt bekommen. Ohne Anzeigename setzt easydb aus Vorname und Name bzw Login einen Anzeigenamen automatisch zusammen.|
|Firma|Feld zum Hinterlegen einer Firma. Wird momentan nur in der Benutzerverwaltung angezeigt.|
|Abteilung|Feld zum Hinterlegen einer Abteilung. Wird momentan nur in der Benutzerverwaltung angezeigt.|
|Telefon|Telefonnummer. Wird momentan nur in der Benutzerverwaltung angezeigt.|
|Bild|Für einen Benutzer kann ein Bild hinterlegt werden. Dieses Bild wird bei Bedarf anderen Benutzern angezeigt. Wenn kein Bild hochgeladen wurde, wird ein Default-Bild angezeigt, welches in der Config der easydb festgelegt werden kann. Ein hochgeladenens Bild kann mit Mausrad vergrößert oder verkleinert und mit Drag & Drop positioniert werden.|
|Bemerkungen|Internes Bemerkungsfeld.|


### Benutzertypen

Die Unterscheidung von Benutzertypen bezieht sich auf die Methode, mit der ein Benutzer in easydb angelegt wurde.

|Typ|Erklärung|
|---|---|
|system|Der System-Benutzer in der easydb. Derzeit ist das nur **root** (siehe [Systemrechte](/webfrontend/rightsmanagement/rightsmanagement.html)). Dieser Benutzer wird bei Einrichtung von easydb automatisch angelegt und kann auch nicht gelöscht werden.|
|easydb|Der normale easydb Benutzer. Dieser Benutzer wird in der easydb vom Administrator eingerichtet und verwaltet.|
|email|Dieser Benutzer wird immer dann angelegt, wenn beim Freigeben oder Export verschicken eine E-Mail als Freigabe-Ziel benutzt wird. Durch das zentrale Verwalten der E-Mail als einfacher Benutzer ist eine spätere Umwandlung in einen vollen easydb Benutzer möglich.|
|anonymous|Für jedes anonyme Login in der easydb (Aufruf ohne Login), wird ein anonymer Benutzer eingerichtet. Dieser Benutzer wird über einen Cookie wiedererkannt und kann unter seinem anonymen Benutzer-Account auch Einstellungen speichern. Anonyme Benutzer werden von easydb verwaltet und sind im Frontend nicht sichtbar.|
|collection|Beim Freigeben von Mappen (intern auch Collections) können anonyme Links eingerichtet werden, über die dann direkt auf eine Mappe zugegriffen werden kann. Diese Benutzer werden von easydb automatisch angelegt und verwaltet. Sie sind über das Frontend nicht erreichbar.|

> HINWEIS: In der Regel werden nur die Typen *easydb*, *system* und *email* sichtbar angezeigt, die Auflistung der Typen beinhaltet auch noch die intern verwalteten Typen *anonymous* und *collection*.


## E-Mails

easydb erlaubt das Hinterlegen beliebig vieler E-Mail-Adressen pro Benutzer. E-Mail-Adressen können verschiedene Funktionen erfüllen. So kann eine E-Mail-Adresse vom Benutzer zum Anmelden benutzt werden oder es können E-Mails als Folge von Transaktionen (Workflow-Management) verschickt werden.

Die *Bevorzugte E-Mail* ist die E-Mail, die dem Benutzer als seine E-Mail-Adresse kommuniziert wird und die er, soweit konfiguriert, auch selber ändern kann.

### E-Mails

|Einstellung|Erläuterung|
|--|--|
|E-Mail|Ist die E-Mail-Adresse. Die E-Mail ist systemweit einmalig.|
|Angefordert|Zeitpunkt, an dem easydb eine E-Mail rausgeschickt hat, um vom Benutzer eine Bestätigung der E-Mail anzufordern.|
|Bestätigt|Zeitpunkt, an dem der Benutzer seine E-Mail-Adresse bestätigt hat.|
|Bestätigung anfordern|Kann gesetzt werden, um den Benutzer (erneut) zur Bestätigung dieser E-Mail-Adresse aufzufordern.|
|Für Login benutzen|Wenn gesetzt, kann der Benutzer diese E-Mail-Adresse zum Login benutzen. Der Benutzer hat insgesamt immer nur ein aktuelles Passwort, egal was er zum Login benutzt.|
|Für E-Mail benutzen|Wenn gesetzt, wird diese E-Mail für Workflow-E-Mails benutzt. Im *Zeitplan* kann eingestellt werden, wie oft ein Benutzer E-Mails erhält.|
|E-Mail senden|Wenn gesetzt, werden Änderungen am Benutzer-Datensatz per E-Mail an den Benutzer kommuniziert. Wenn der Benutzer selber seine Daten in den Benutzereinstellungen (User-Self-Management) ändert, wird immer eine E-Mail geschickt, diese Checkbox bezieht sich nur auf Änderungen, die im Administrationsbereich durchgeführt werden.<br>*Hinweis: Beim aktivieren dieser Option wird vom System eine Willkommens-E-Mail verschickt.*|
|... mit Passwort|Wenn gesetzt, wird in den Systm-E-Mails das Passwort des Benutzers im Klartext mitgeschickt. Das passiert aber nur dann, wenn die Speichern-Aktion das Passwort geändert oder gesetzt hat.|
|Bevorzugte E-Mail|Dem Benutzer wird nur eine E-Mail-Adresse angezeigt. Wenn gesetzt wird dem Benutzer diese E-Mail-Adresse als seine E-Mail-Adresse angezeigt. Die bevorzugte E-Mail ist die E-Mail, die andere Benutzer von diesem Benutzer angezeigt bekommen. Wenn keine bevorzugte E-Mail konfiguriert ist, wird für diesen Benutzer keine E-Mail angezeigt.|
|Wird bevorzugte E-Mail|Wenn ein Benutzer per Benutzereinstellungen seine E-Mail-Adresse ändert und im Anschluss bestätigt, wird die E-Mail auf *bevorzugt* gesetzt. Der Administrator kann diese Checkbox auch manuell setzen und manuell eine Bestätigung anfordern. Nach Bestätigung durch den Benutzer wird diese E-Mail-Adresse die bevorzugte des Benutzers.|


### <a name="schedule"></a>Zeitplan

Der Zeitplan wird verwendet, um dem Benutzer zusammengefasste Workflow-E-Mails zuzustellen. Häufig ist es nicht gewünscht, dass mit jedem E-Mail auslösendem Workflow-Ereignis sofort eine E-Mail geschickt wird. Durch den Zeitplan werden die E-Mails zusammengefasst und zum angegeben Zeitpunkt versendet. Wenn kein Zeitplan konfiguriert ist, werden Workflow-E-Mails sofort bei jedem Ereignis rausgeschickt.

Per Checkboxen wird ein Filter definiert. Wenn dieser Filter passt, wird eine E-Mail geschickt. Z. B. kann man konfigurieren, dass E-Mails immer am 1. des Montags um 10 Uhr rausgeschickt werden: *Tag im Monat*:1 *Stunde*: 10.

|Einstellung|Erläuterung|
|--|--|
|Tag im Monat|Die Tage im Monat, die für den Filter benutzt werden.|
|Wochentag|Die Wochentage, die für den Filter benutzt werden.|
|Stunde|Die Stunden, die für den Filter benutzt werden.|


## Passwortverwaltung

|Einstellung|Erläuterung|
|--|--|
|Login gesperrt|Checkbox um das Login eines Benutzers zu sperren. Der Benutzer wird über die Sperrung per E-Mail informiert.|
|Benutzer muss beim nächsten Anmelden Passwort setzen bzw. ändern|Um sich erfolgreich anzumelden, muss der Benutzer bei diesem Anmeldeversuch ein Passwort vergeben.|
|Passwort setzen|Wenn gesetzt, wird das Benutzer-Passwort vom Administrator gesetzt oder gelöscht.|
|Automatisch generiertes Passwort|Wenn gesetzt, wird an den Benutzer ein automatisch generiertes Passwort vergeben. Das macht nur Sinn in der Verbindung der Optionen *E-Mail senden* + *...mit Passwort*, sonst kann niemand das Passwort sehen. Passwörter werden in der easydb verschlüsselt gespeichert und können nicht einfach entschlüsselt werden.|
|Passwort|Zum Setzen des Passworts durch den Administrator kann hier ein Passwort eingegeben werden. Wenn es leer bleibt, wird das Passwort gelöscht und der Benutzer kann sich in Folge nicht mehr anmelden.|

## Gruppen

Per Checkbox legen Sie hier fest, in welchen Gruppen sich der Benutzer befindet. Beachten Sie, dass ein Benutzer manuell nur in Nicht-Systemgruppen eingeordnet werden kann. Die Einordnung in [Systemgruppen](/webfrontend/rightsmanagement/groups/groups.html) erfolgt automatisch.

## Systemrechte

Eine Auflistung der Systemrechte finden Sie unter [Rechtemanagement](/webfrontend/rightsmanagement/rightsmanagement.html). Beachten Sie, dass kontextabhängig ggfs. weitere, hier nicht aufgelistete Systemrechte zur Verfügung stehen können.

## Berechtigungen

Eine Auflistung aller Rechte finden Sie unter [Rechtemanagement](/webfrontend/rightsmanagement/rightsmanagement.html). Beachten Sie, dass kontextabhängig ggfs. nicht alle aufgelistete Rechte zur Verfügung stehen.
