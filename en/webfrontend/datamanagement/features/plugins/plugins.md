# Plugins

## <a name="wordpress"> </a> Wordpress

With this easydb plugin you can transfer media files to Wordpress CMS. In Wordpress they appear in the Media Gallery and can be used as usual. Media files can be sent from easydb and updates can be synchronized. There is no support for deleting media. An installation guide for activating the Wordpress plugin in easydb can be found under[Plugin Installation](/sysadmin/configuration/plugin/plugin.html).

After the installation, a [Wordpress transport](../../features/export/export.html#transport) can be created via the [Exporter](../../features/export/export.html#transport). Only image files are sent. Therefore, for changes to the record in easydb, the following applies to Wordpress:

|Change in easydb | example | change in Wordpress |
| - | - | - |
| Delete a record || Image file is retained in WordPress. |
| File change | crop the image | Image file is created during transport in Wordpress. |
| Change metadata to the record | Change the title and use it as a new filename for export. | During transport, the existing file is retained in WordPress. The name of the file is updated
| Change to the user | by changing the name | image file remains unaffected in Wordpress. |


## <a name="TYPO3"> </a> TYPO3

An easydb plugin for TYPO3 can be used to send records from easydb to TYPO3. They appear in the file list and can then be used as usual. The plugin for setup in easydb can be found on [GitHub](https://github.com/programfabrik/typo3-easydb-plugin). In the Typo3 Extensions, the easydb plugin for TYPO3 is available and can be installed in the CMS.

![TYPO3 plugin for easydb](typo3_easydb_plugin.png)

After the installation, a button appears above the filelist, with which easydb opens in a new window. Here the data records to be sent to TYPO3 are selected. The "Transfer to TYPO3" option is available via the toolbar and the context menu.

Modified or deleted records in easydb are not synchronized with TYPO3. Changes to the record must be manually transferred in TYPO3.

## <a name="falconio"> </a> Falcon.io

Records can be exported from easydb to Falcon.io. In Falcon.io they appear in the content pool and can be used from there as usual.
After the installation, a Falcon.io transport can be sent from the easydb asset browser or from the list view. Whe the Falcon.io plugin is active, simply right click a record, or multiple records, and select 'Send to Falcon.io'.

