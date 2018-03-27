# Mandantenfähigkeit auf Basis des Rechtemanagements

Über das Rechtemanagement in easydb können administrative Zuständigkeiten für Fachbereiche oder Abteilungen, die auf Poolebene abgebildet werden, getrennt werden. Für die jeweiligen Pools wird dementsprechend je ein Admin eingerichtet. In dem nachfolgenden Konfigurationsbeispiel werden unterschiedliche Fachbereiche (Pools) mit eigenen Administratoren und Benutzergruppen eingerichtet. 

Hierfür werden 3 Benutzergruppen je Fachbereich benötigt, z. B.:
•	Fachbereich-Admins
•	Fachbereich-Schreiben
•	Fachbereich-Lesen

Die Benutzergruppe Fachbereich-Admins benötigt folgende Systemrechte:
•	Benutzer verwalten
•	Pools verwalten

![](/assets/admins_system.png)

Die Fachbereich-Admins benötigen darüber hinaus Rechte an den Gruppen Fachbereich-Schreiben und Fachbereich-Lesen. Hierfür muss an diesen beiden Gruppen jeweils im Reiter *Berechtigungen* eine neue Zeile hinzugefügt und die Fachbereich-Admins ausgewählt werden.

Folgende Checkboxen müssen da gesetzt werden:

![](/assets/admin_berechtigung.png)

Sollen die Fachbereich-Admins über die Berechtigung verfügen weitere Pools unter Ihrem Fachbereich-Pool anlegen zu dürfen, muss im Pool-Editor am entsprechenden Pool die Berechtigung erlaubt werden.