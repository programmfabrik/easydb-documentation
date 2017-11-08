# Plugins

## <a name="wordpress"> </a> Wordpress

Records can be exported from easydb to Wordpress. In Wordpress they appear in the media gallery and can be used from there as usual. Instructions for installing and using the Wordpress plugin can be found on [GitHub](https://github.com/programfabrik/easydb-wordpress-plugin).

After the installation, a [Wordpress transport](../../features/export/export.html#transport) can be created via the [Exporter](../../features/export/export.html). Only image files are sent. Therefore, for changes to the record in easydb, the following applies to Wordpress:

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

Records can be exported from easydb to Falcon.io. In Falcon.io they appear in the content pool and can be used from there as usual. Instructions for installing and using the Falcon.io plugin can be found on [GitHub](https://github.com/programfabrik/easydb-falconio-plugin).

After the installation, a [Falcon.io transport](../../features/export/export.html#transport) can be created via the [Exporter](../../features/export/export.html). Only image files are sent. Therefore, for changes to the record in easydb, the following applies to Falcon.io.

