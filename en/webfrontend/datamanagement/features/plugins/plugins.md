# Plugins

easydb provides an open API and can be extended by features using plugins. It is possible to use existing plugins or add your own plugins to easydb.

Some plugins for easydb are open source and are freely available via the Programmfabrik [GitHub](https://github.com/programmfabrik) repository.

Chargeable Plugins are delivered by Programmfabrik. Some of the available plugins for CMS integration consist of 2 components.

|CMS|	Plugin for easydb	| Plugin for CMS|
|---|---|---|
|Wordpress|	Yes, chargeable |none|
|TYPO3|Yes, chargeable	|Yes, open source via github|
|Drupal|Yes, chargeable	|Yes, open source via github|
|Falcon.io|	Yes, chargeable |none|


## Wordpress {#wordpress}

With this easydb plugin you can transfer media files to Wordpress CMS. In Wordpress they appear in the Media Gallery and can be used as usual. Media files can be sent from easydb and updates can be synchronized. There is no support for deleting media. 

The installation to activate the Wordpress plugin in easydb takes 3 steps:

1. [Install Wordpress Plugin](../../../../sysadmin/plugin/plugin.html#wordpressplugin)

2. Configure Access to Wordpress in [Basic Configuration](../../../../administration/base-config/base-config.html#wordpress).

3. Assign the [system rights](/webfrontend/rightsmanagement/rightsmanagement.html#aclsystem) to authorized users or groups.

After successful installation and configuration, users can use [Exporter](../../features/export/export.html) to create a [Wordpress transport](../../features/export/export.html#transport). Only image files are sent. The following applies to Wordpress for changes to records in easydb:

|Change in easydb | example | change in Wordpress |
| - | - | - |
| Delete a record || Image file is retained in WordPress. |
| File change | crop the image | Image file is created during transport in Wordpress. |
| Change metadata to the record | Change the title and use it as a new filename for export. | During transport, the existing file is retained in WordPress. The name of the file is updated
| Change to the user | by changing the name | image file remains unaffected in Wordpress. |


## Wordpress {#wordpress}

Mit diesem easydb Plugin können Mediendateien ins Wordpress CMS transferiert werden. In Wordpress erscheinen sie in der Mediengalerie und können von dort wie gewohnt verwendet werden. Mediendateien können aus easydb gesendet und Aktualisierungen synchronisiert werden. Eine Unterstützung für das Löschen von Medien existiert nicht. 

Die Installation zur Aktivierung des Wordpress-Plugins in easydb erfolgt in 3 Schritten:

1. Das Wordpress [Plugin installieren](../../../../sysadmin/plugin/plugin.html#wordpressplugin)

2. Zugriff auf Wordpress in der [Basis-Konfiguration](../../../../administration/base-config/base-config.html#wordpress) einrichten.

3. Berechtigten Benutzern oder Gruppen das [Systemrechte](/webfrontend/rightsmanagement/rightsmanagement.html#aclsystem) für die Nutzung des Plugins zuweisen.

Nach erfolgreicher Installation und Konfiguration können Benutzer über den [Exporter](../../features/export/export.html) einen [Wordpress-Transport](../../features/export/export.html#transport) anlegen. Gesendet werden nur Bilddateien. Bei Änderungen am Datensatz in easydb gilt Folgendes für Wordpress:

|Änderung in easydb|Beispiel|Veränderung in Wordpress|
|--|--|--|
|Löschen eines Datensatzes||Bilddatei bleibt in Wordpress erhalten.|
|Datei verändern|durch Zuschneiden|Bilddatei wird beim Transport in Wordpress neu angelegt. |
|Metadaten am Datensatz ändern| Titel ändern und durch Ersetzung als neuen Dateinamen für Export verwenden. | Beim Transport bleibt die existierende Datei in Wordpress erhalten. Der Name der Datei wird aktualisiert.|
|Änderung am Benutzer|durch Änderung des Namen|Bilddatei bleibt in Wordpress davon unberührt.|





## TYPO3 {#typo3}

An easydb plugin for TYPO3 (starting with Version 7) and can be used to send records from easydb to TYPO3. They appear in the file list and can then be used as usual. The plugin for setup in easydb can be found on [GitHub](https://github.com/programmfabrik/typo3-easydb-plugin). In the Typo3 Extensions, the easydb plugin for TYPO3 is available and can be installed in the CMS.

![TYPO3 plugin for easydb](typo3_easydb_plugin.png)

After the installation, a button appears above the filelist, with which easydb opens in a new window. Here the data records to be sent to TYPO3 are selected. The "Transfer to TYPO3" option is available via the toolbar and the context menu.

Modified or deleted records in easydb are not synchronized with TYPO3. Changes to the record must be manually transferred in TYPO3.

## Falcon.io {#falconio}

With the plugin for Falcon.io it possible to export records from easydb and use them in Falcon.io. First the plugin needs to be installed and acivated by a system adminitrator, see [Plugin Installation](../../../../sysadmin/konfiguration/plugin/plugin.html#falconio). After installing the plugin, one or more Falcon. io instances can be created in the easydb [Basic Configuration](../../../administration/base-config/base-config.html#falconio). 

Records can be exported from easydb to Falcon.io after successful installation. In Falcon.io they appear in the content pool and can be used as usual.
A Falcon.io-transport can be sent from the easydb asset browser or from the list view. If the Falcon.io plugin is active, right-click on one or more records and select "Send to Falcon. io".



