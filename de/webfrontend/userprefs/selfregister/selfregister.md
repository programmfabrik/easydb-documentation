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
