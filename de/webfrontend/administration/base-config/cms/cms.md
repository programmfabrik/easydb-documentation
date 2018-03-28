# CMS

Für die Anbindung von CMS-Systemen können [Plugins](/webfrontend/datamanagement/features/plugins/plugins.html) genutzt werden. Hier werden die Einstellungen für die Anbindung von CMS-Systemen vorgenommen.

## Wordpress {#wordpress}

![Konfiguration: Wordpress in easydb](bc_wp.jpg)

|Eingabefeld|Erläuterung|
|--|--|
|Instanzname|Hier können eine oder mehrere Instanzen angelegt werden. Pro Instanz muss ein Name vergeben werden. |
|URL| URL der Wordpress-Instanz, in die Medien transportiert werden sollen.|
|Methoden für die Authentifizierung|Option 1: <br> Authentifizierungstyp HTTP: <br> Loginname und Passwort des Wordpress-Adminis.|
||Option 2: <br> Authentifizierungstyp OAuth 1.0a: <br >Kopieren Sie den Client Key und das Client Secret vom (vorbereiteten) Applikationsbenutzer aus Wordpress <br > Klicken Sie "Generate Key" um sich mit Wordpress zu verbinden, sich zu authentifizieren und ein Token bzw. Token Secret zu erhalten.|

> HINWEIS: Vorausgesetzt sind min. Wordpress 4.7, eine aktive JSON-Rest-API (ist default) und eine eingerichtete Authentifizierung. Für die Verwendung im Frontend muss für den Benutzer oder die Gruppe das [Systemrecht](/webfrontend/rightsmanagement/rightsmanagement.html#aclsystem) "Wordpress Export erlauben" für Wordpress aktiviert werden.

Eine Anleitung zur Installation des Plugins ist [hier](/sysadmin/plugin/plugin.html#wordpressplugin).

## Falcon.io {#falconio}

![Konfiguration: Falcon.io](falconio.jpg)

|CMS|Eingabefeld|Erläuterung|
|--|--|--|
| Falcon.io | Instanzname | Hier können eine oder mehrere Instanzen angelegt werden. Pro Instanz muss ein Name vergeben werden. |
|| API_Key | Die genereierten unique API Key um deine RESTful API zu nutzen. |
|| Aktiv | Über die Checkbox kann die API zu der jeweiligen Instanz aktiviert und deaktiviert werden. |


## TYPO3 {#typo3}

![Konfiguration: TYPO3-Plugin für easydb](bc_cms_typo3.jpg)

Nach erfolgreicher [Pluginkonfiguration](../../../sysadmin/konfiguration/plugin/plugin.html) in einer [YAML-Datei](../../../sysadmin/konfiguration/yaml/yaml.html) durch einen System-Administrator, können hier Einstellungen für das TYPO3-Plugin vorgenommen werden.

|CMS|Eingabefeld|Erläuterung|
|--|--|--|
|TYPO3 (ab Version 7)|Schnittstelle aktivieren|Aktiviert das [Plugin](../../datamanagement/features/plugins/plugins.html). |
||Dateien über den Browser versenden| Über das Plugin in TYPO3 wird easydb für den Export von Dateien erreicht. Ist der Export vom easydb-Server zum Typo3-Server nicht direkt möglich, kann die Option zum Export über den Browser aktiviert werden.|
||Maximale Datei-Größe| Limit für Dateien wenn diese über den Browser verschickt werden sollen. |
||Metadaten-Profil|Einstellung für Metadaten-Mapping beim Export von easydb zu TYPO3.<br><br>**- Standard -**: Ohne Profil wird Standard A auf *title* gemappt und Standard B auf *description*.<br><br> **Eigenes Mapping**: Individuelle Mappings können unter [Metadaten-Mapping](../profiles/profiles.html) angelegt werden. Diese stehen dann über das Pulldown zur Auswahl. |
