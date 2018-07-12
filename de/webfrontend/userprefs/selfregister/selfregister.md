#Selbstregistrierung

## Als Benutzer registrieren

Wenn die Funktion eingerichtet ist, können Benutzer selbst eine Registrierung für easydb vornehmen. Wird easydb im Browser geöffnet, erscheint auf der Startseite oben rechts der Button für die Registrierung.

![Registrierung](register.png)

## Als Admin Selbstregistrierung einrichten

Um einen öffentlichen Zugang mit Selbstregistrierung einzurichten, müssen vom easydb Administrator nachfolgende Einstellungen vorgenommen werden.

###1) Einstellungen in der Basis-Konfiguration vornehmen
*PFAD: Basis-Konfiguration > Reiter: Anmelden*

* "Anonym über Internet erlauben" aktivieren
* alle Felder im Bereich "Selbstregistrierung" ausfüllen

![Basis-Konfiguration: Anmelden](register_baseconfig.png)

###2) Systemrechte für Benutzergruppe anpassen
*PFAD: Rechtemanagement > Gruppen/Rollen > Anonyme Benutzer > Reiter: Systemrechte*

* "Recherche" aktivieren
* "Benutzer-Registrierung anlegen" aktivieren
	* alle für die Selbstregistrierung erforderlichen Felder auswählen
	* Typ "easydb Selbstregistrierung" wählen

![Systemrechte für Anonyme Benutzer](group_systemrights.png)

###3) Inhalte für die Gruppen/Rollen "Anonyme Benutzer" freigeben
*PFAD: Tags & Workflows > Reiter: Tags*

* im Bereich "Tags & Workflows" die Tag-Gruppe "Freigabe" anlegen
* den Tag "extern" anlegen

![Freigabe anlegen](tags_register.png)

*PFAD: Rechtemanagement > Pools > Pool(ebene) wählen > Reiter: Berechtigungen*

* im Bereich "Pools" Rechte hinzufügen für die Gruppe "Anonyme Benutzer" (min. Objekte ansehen, Erlaubte Masken und Pool ansehen aktivieren; je nach Bedarf auch Ansehen/Download-Rechte vergeben)
* als Tagfilter den Tag "extern" auswählen

![Berechtigung für Pool](pool_permission.png)

###4) Eine Nachricht (optional mit Bestätigungscheckbox) einbinden

Optional kann eine Nachricht für den Benutzer in das Registrierungsformular eingebunden werden. Die wird über [Mitteilungen](../../administration/messages/messages.html) im Hauptmenü gemacht. Wählen Sie dafür die Option 'Ständiger Hinweis im Selbstregistrierungsformular'.  Dies können zum Beispiel allgemeine Informationen oder Nutzungsbedingungen sein. Es erscheint unten im Formular ein Linktext, über den die Nachricht in einem Pop-Up-Fenster abgerufen wird. Optional ist es möglich eine Checkbox zu aktivieren, durch die der Text gelesen werden muss, bevor der Registrierungsvorgang abgeschlossen wird.
