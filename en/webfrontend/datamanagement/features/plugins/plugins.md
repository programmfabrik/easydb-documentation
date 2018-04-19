# Plugins

easydb verfügt über offene Schnittstellen und kann durch Plugins um Feature erweitert werden. Einige Plugins für easydb sind Open Source und stehen über [GitHub](https://github.com/programmfabrik) frei zur Verfügung.

## Wordpress {#wordpress}

With this easydb plugin you can transfer media files to Wordpress CMS. In Wordpress they appear in the Media Gallery and can be used as usual. Media files can be sent from easydb and updates can be synchronized. There is no support for deleting media. An installation guide for activating the Wordpress plugin in easydb can be found here [Plugin Installation](../../../../sysadmin/plugin/plugin.html#wordpressplugin).

After the installation, a [Wordpress transport](../../features/export/export.html#transport) can be created via the [Exporter](../../features/export/export.html#transport). Only image files are sent. The following applies to Wordpress for changes to records in easydb:

|Change in easydb | example | change in Wordpress |
| - | - | - |
| Delete a record || Image file is retained in WordPress. |
| File change | crop the image | Image file is created during transport in Wordpress. |
| Change metadata to the record | Change the title and use it as a new filename for export. | During transport, the existing file is retained in WordPress. The name of the file is updated
| Change to the user | by changing the name | image file remains unaffected in Wordpress. |


## TYPO3 {#typo3}

An easydb plugin for TYPO3 (starting with Version 7) and can be used to send records from easydb to TYPO3. They appear in the file list and can then be used as usual. The plugin for setup in easydb can be found on [GitHub](https://github.com/programmfabrik/typo3-easydb-plugin). In the Typo3 Extensions, the easydb plugin for TYPO3 is available and can be installed in the CMS.

![TYPO3 plugin for easydb](typo3_easydb_plugin.png)

After the installation, a button appears above the filelist, with which easydb opens in a new window. Here the data records to be sent to TYPO3 are selected. The "Transfer to TYPO3" option is available via the toolbar and the context menu.

Modified or deleted records in easydb are not synchronized with TYPO3. Changes to the record must be manually transferred in TYPO3.

## Falcon.io {#falconio}

With the plugin for Falcon.io it possible to export records from easydb and use them in Falcon.io. First the plugin needs to be installed and acivated by a system adminitrator, see [Plugin Installation](../../../../sysadmin/konfiguration/plugin/plugin.html#falconio). After installing the plugin, one or more Falcon. io instances can be created in the easydb [Basic Configuration](../../../administration/base-config/base-config.html#falconio). 

Records can be exported from easydb to Falcon.io after successful installation. In Falcon.io they appear in the content pool and can be used as usual.
A Falcon.io-transport can be sent from the easydb asset browser or from the list view. If the Falcon.io plugin is active, right-click on one or more records and select "Send to Falcon. io".



