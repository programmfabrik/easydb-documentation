---
menu:
  main:
    name: "5.45"
    identifier: "5.45"
    parent: "releases550"
    weight: -545
---

> - **Version 5.45.0** requires a Re-Index, schedule a corresponding downtime of the system during the update. **This version internally changes the indexing of the assets, which means that initially all assets have to be re-inquired from Easydb-Asset-Server.** This means that the downtime for this update is longer than for previous releases.
> - The database size has increased since this version as more information about assets is buffered in the easydb database by the EAS. This increases the backup dumps of the Postgresql database.
> - Due to a very unfortunate combination of cache problems and new templates an error **"Not all required elements were found for Template"** could occur. This error appears in the browser cache due to outdated templates of easdb. We tried to mitigate the problem in **5.45.1.** by giving the user a **"Reload"** option. This did not fix the problem completely, because the error reappeared with the next login. In **5.45.2.** we go one step further and try to update the outdated templates automatically. If the error still persists, the cache of the affected browsers must be deleted manually. After that easydb should start and work as usual.
>

# Version 5.45.4

*Published on 30.01.2019*

### Server

*Fixed*

- Fixed a bug in the update of the EAS versions in the database. Many unnecessary indexing jobs were planned.

### Fylr

*Fixed*

- Endpoint /zip Improved connection management for timeouts and DNS errors.

# Version 5.45.3

*Published on 25.01.2019*

### Web frontend

Improved

- The localization of connector settings and connector messages has been revised.

*Fixed*

- More robust processing of missing technical_metadata in the detail view with activated map view.
- An error in the zoomer led to an error message if you clicked on a new object with activated zoom without preview image.

### Server

*Fixed*

- Incorrect transaction handling could lead to a dead lock in the database for larger batch processes.

# Version 5.45.2

*Published on 22.01.2019*

### Web frontend

*New*

- **Internet Explorer 11** support ends with this release. easydb displays a warning message to inform users of this browser.

*Improved*

- Error handling for obsolete templates in the browser cache of users has been further improved.

*Fixed*

- Fix for the image zoomer, which showed a javascript error with incomplete metadata (see **Server**).

### Server

*Fixed*

- In instances where **/eas/rput** was used to transfer files to, metadata was not completely updated, so the zoomer for images did not work and displayed a Javascript error. This fix fixes the problem in the server and automatically re-indexes the missing metadata.

# Version 5.45.1

*Published on 18.01.2019*

### Web frontend

*New*

- For **panels**, an automatic expansion in the text view can be defined in the mask editor. 

*Improved*

- For errors that occur due to missing templates in the start page, the error output was changed so that users can reload the page, which then loads the missing templates from the server.
- An unfavorable constant reloading of **maintenance messages** was improved, so that less requests have to be sent to the server. 

*Fixed*

- The detail view of connector objects with logging "View detail" switched on led to an error.
- If a **maintenance message** was set up in connection with an activated connector, an error could occur.

### Server

*Fixed*

- The cache headers for the start page were previously kept too aggressively in the cache and were not updated when changes were made. This led in 5.45.0. with some users in connection with Chrome to a Javascript error which could no longer be clicked away.

# Version 5.45.0

*Published on 17.01.2019*

### Web frontend

*New*

- The expert search now allows to **search for the status for the preview calculation** in the file properties. This allows you to find files whose preview could not be created.
- The expert search now allows **searching by asset ID**.
- **Select whole page** was added to the search.
- For objects with multiple files in the default view, the previews can also be browsed in the search result.
- New Custom-Mask-Splitter  [Plugin](https://github.com/programmfabrik/easydb-hijri-gregorian-converter) to convert **Hijri** to **Gregorian** calendar dates (Beta).
- Separators **Horizontal divider** and **block** are now allowed within tabs and panels.
- Two new message types **Maintenance Announcement** and **Maintenance** in the administration area allow setting up messages for users. The messages are presented as a dialog and can then be viewed again in the upper right area by clicking on a warning triangle. 

*Improved*

- Separators in the mask editor have improved colors.
- The change history in the detail view is only displayed for objects if the user has at least one write permission (**WRITE**) on the object. Previously, one read permission (**READ**) was sufficient.
- The dialog for creating new objects now saves the settings.
- Searches are always limited to 256 characters. The restriction is the maximum length of a search term.
- Improved interaction in video player when switching to full screen.
- In the basic configuration, the vertical tabs are now sorted alphabetically.
- Improved expert search for terms in a string field. The search term is now completely searched, not just the beginning of the search term.
- The **View Details** event (DETAIIL_VIEW) now stores more IDs and the pool of the viewed object.

*Fixed*

- The Save button in the Mask Editor did not become active when changing settings in **Custom Data Type** options.
- For objects with multiple files, the selection of the file in detail was wrong in some cases.
- Download in **Connector** when selecting Connector objects without files was repaired.
- Display of the current data model with Connector active was repaired.
- When uploading files with metadata mapping enabled, the metadata is correctly assigned to the files in reverse nested relations.
- The upload of multiple files to a workbook using **drag & drop** has been fixed.
- Fixed the display of change history for objects with already deleted linked objects.

### Server

*New*

- **/api/settings** now also returns the easydb version.
- **/api/search** objects can be searched for asset properties.
- **/api/search** length limitation for search values to 256 characters.
- **/api/db** Rejected workflows can set tags, send emails and trigger webhooks.
- New system group for users logged in via LDAP.

*Improved*

- Plugins to be activated are checked at startup, the server does not start in case of incorrect configuration.
- High-resolution video version will only be charged if the original size is sufficient.
- Content-Type can be set in the deeplink via XSLT attribute.
- More requirements for users to be saved (login or e-mail must be set).
- Improvements in the Suggest-Index.
- Error handling when deleting pools improved.
- No events for empty scheduled exports.
- Enhancements in metadata mapping.

*Fixed*

- Error when deleting events removed.
- Corrected use of ico file as favicon.

### EAS

- Raw format **.raf** supported
- Geogebra zip files get .ggb extension
- Fixes for .wmf

### Fylr

*New*

- A new [Link-Shortener](https://fylr.io/docs/fylr/server/link-shortener/) allows the creation of shortened easydb URLs.

*Translated with www.DeepL.com/Translator*