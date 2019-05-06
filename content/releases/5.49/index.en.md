---
menu:
  main:
    name: "5.49"
    identifier: "5.49"
    parent: "releases"
    weight: -549
---

> * A new system right **Access only for collections (research without search function)** has been added in **Version 5.48.0**. We will **remove** the old system right **Search not allowed (collection-only users)** in **Version 5.50.0** (planned publication on 02.05.2019). Make sure to change your rights management to the new right by then.

# Version 5.49.1

*Published on 25.04.2019*

### Web frontend

*New*

- With two [configuration variables](https://docs.easydb.de/en/sysadmin/konfiguration/easydb-server.yml/webfrontend/) **index_html_head_include** and **index_html_body_include** it is possible to influence the index.html of the one-page app to configure your own content for search engine indexing.  

### Server

*Fixed*

- The file name for the extension **webdvd.zip** was not restored correctly for some downloads.
- Rights management: Users with system rights **system.root** may save ACL without further rights checks. This allows inconsistencies in collection rights to be corrected. 

# Version 5.49.0

*Published on 10.04.2019*

### Web frontend

*New*

- New mask setting for **publish**. If enabled, publications made via /api/publish will be displayed in detail and in the Share dialog.
- A search for publications has been integrated into the expert search.
- In the debug menu (CTRL-ALT-D) there is now a possibility to send a **test email** to test the setup for the mail system.

*Improved*

- The display of objects with multiple files now automatically jumps to the first file for which a preview exists.
- The **General** tab is now displayed first in Collection Properties.
- The object ID is now also displayed in the text view if activated in the mask.
- Minor graphical improvements and repairs.

*Fixed*

- The search in the pool dropdown was repaired.
- The **ad hoc creation** of a new entry in a sublist was repaired.
- The field filter for **Owner** now also filters reverse nested objects correctly.
- If an object for which the user has read-only rights is selected in the sidebar when the editor mode is activated, the system now automatically switches to detail mode.
- Some bugs in connection with activated **Connector** have been fixed.
- **Connector connections** are now performed **without cookies**, so more browsers should allow access.
- The search for the **original file name** now searches in the complete name, including extension.

### Server

*New*

- New mask setting for **publish**. If activated, publications made via **/api/publish** will be displayed in detail.

- Test mail dispatch via **/api/v1/settings/sendmail** to any registered mail address.

*Improved*

- Search results by multilingual fields are **sorted alphabetically**, even if the field is not filled for all languages.

- The process for requesting a new password has been improved and provided with more detailed error messages.
- **Metadata mapping**: more EXIF tags for image width, image height and digitization date are supported for mapping.

Fixed

- The **owner** right is now always evaluated correctly. In some places in rights management, the **owner** right was not interpreted correctly, which could lead to missing rights for objects.

*Translated with www.DeepL.com/Translator*

