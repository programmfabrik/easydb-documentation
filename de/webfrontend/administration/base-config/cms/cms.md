# CMS

Für die Anbindung von CMS-Systemen können [Plugins](/webfrontend/datamanagement/features/plugins/plugins.html) genutzt werden. Hier werden die Einstellungen für die Anbindung von CMS-Systemen vorgenommen.

## Wordpress {#wordpress}

Wenn die [Installation des Plugins](/sysadmin/plugin/plugin.html#wordpressplugin) abgeschlossen ist, finden Sie im Reiter <code class="tab">CMS</code> den Konfigurationsblock für Wordpress.

1. Geben Sie den Instanznamen und die URL an und wählen Sie eine Authentifizierungsmethode (siehe Details in der Tabelle unter dem Screenshot).
2. Speichern Sie die Basis-Konfiguration nach erfolgreicher Authentifizierung.

> HINWEIS: Vorausgesetzt sind min. Wordpress 4.7, eine aktive JSON-Rest-API (ist default) und eine eingerichtete Authentifizierung. 

![Konfiguration: Wordpress in easydb](bc_wp.jpg)

|Eingabefeld|Erläuterung|
|--|--|
|Instanzname|Hier können eine oder mehrere Wordpress Instanzen angelegt werden. Pro WP-Instanz muss ein Name vergeben werden. |
|URL| URL der Wordpress-Instanz, in die Medien transportiert werden sollen. Beachten Sie dabei die korrekte Schreibweise http**s**://www.meine-webseite.de|
|Methoden für die Authentifizierung|Option 1: <br> Authentifizierungstyp HTTP: <br> Loginname und Passwort des Wordpress-Admins.|
||Option 2: <br> Authentifizierungstyp OAuth 1.0a: <br >Kopieren Sie den Client Key und das Client Secret vom [vorbereiteten Applikationsbenutzer](https://docs.easydb.de/de/sysadmin/plugin/plugin.html?h=benutzer%20f%C3%BCr%20das%20oauth-plugin%20in%20wp%20einrichten.) aus Wordpress. <br > Klicken Sie "Generate Key" um sich mit Wordpress zu verbinden. Es öffnet ein Pop-up, in dem Sie sich authentifizieren müssen. Damit erhalten Sie ein Token und Token Secret, dass Sie von hier in das entsprechende Feld kopieren können.|

Wenn Sie die Basis-Konfiguration erfolgreich gespeichert haben, müssen noch **Zugriffsrechte für Benutzer** eingerichtet werden. Für die Verwendung im Frontend benötigen berechtigte Benutzer oder Gruppen das [Systemrecht](/webfrontend/rightsmanagement/rightsmanagement.html#aclsystem) **"Wordpress Export erlauben"**.

## Falcon.io {#falconio}

![Konfiguration: Falcon.io](falconio.jpg)

|CMS|Eingabefeld|Erläuterung|
|--|--|--|
| Falcon.io | Instanzname | Hier können eine oder mehrere Instanzen angelegt werden. Pro Instanz muss ein Name vergeben werden. |
|| API_Key | Die genereierten unique API Key um deine RESTful API zu nutzen. |
|| Aktiv | Über die Checkbox kann die API zu der jeweiligen Instanz aktiviert und deaktiviert werden. |


## TYPO3 {#typo3}

![Konfiguration: TYPO3-Plugin für easydb](bc_cms_typo3.jpg)

Nach erfolgreicher [Pluginkonfiguration](../../../../sysadmin/konfiguration/plugin/plugin.html) in einer [YAML-Datei](../../../../sysadmin/konfiguration/yaml/yaml.html) durch einen System-Administrator, können hier Einstellungen für das TYPO3-Plugin vorgenommen werden.

|CMS|Eingabefeld|Erläuterung|
|--|--|--|
|TYPO3 (ab Version 7)|Schnittstelle aktivieren|Aktiviert das [Plugin](../../../datamanagement/features/plugins/plugins.html). |
||Dateien über den Browser versenden| Über das Plugin in TYPO3 wird easydb für den Export von Dateien erreicht. Ist der Export vom easydb-Server zum Typo3-Server nicht direkt möglich, kann die Option zum Export über den Browser aktiviert werden.|
||Maximale Datei-Größe| Limit für Dateien wenn diese über den Browser verschickt werden sollen. |
||Metadaten-Profil|Einstellung für Metadaten-Mapping beim Export von easydb zu TYPO3.<br><br>**- Standard -**: Ohne Profil wird Standard A auf *title* gemappt und Standard B auf *description*.<br><br> **Eigenes Mapping**: Individuelle Mappings können unter [Metadaten-Mapping](../../profiles/profiles.html) angelegt werden. Diese stehen dann über das Pulldown zur Auswahl. |

## Drupal {#drupal}

Das [Drupal](https://www.drupal.org/) CMS wird ab der Version 8 von easydb unterstützt. Dateien können aus Drupal in easydb recherchiert werden und dann als Kopie nach Drupal übernommen werden. Dabei können verschiedene Dateigrößen zur Übernahme ausgewählt werden.

Die [Pluginkonfiguration](../../../../sysadmin/konfiguration/plugin/plugin.html) erfolgt in einer [YAML-Datei](../../../../sysadmin/konfiguration/yaml/yaml.html) durch einen System-Administrator.

Nach erfolgreicher Installation können hier über die Basis-Konfiguration folgende Einstellungen vorgenommen werden.

|CMS|Eingabefeld|Erläuterung|
|--|--|--|
|Drupal|Schnittstelle aktivieren|Aktiviert das [Plugin](../../../datamanagement/features/plugins/plugins.html). |
||Dateien über den Browser versenden| Über das Plugin in Drupal wird easydb für den Export von Dateien erreicht. Ist der Export vom easydb-Server zum Drupal-Server nicht direkt möglich, kann die Option zum Export über den Browser aktiviert werden.|
||Maximale Datei-Größe| Limit für Dateien, wenn diese über den Browser verschickt werden sollen. |