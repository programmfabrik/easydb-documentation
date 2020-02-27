---
title: "2 - FAQ"
menu:
  main:
    name: "FAQ"
    identifier: "faq"
    weight: -900
---
# FAQ

## Frequently Asked Questions

> Note: Always use a current browser for easydb. In case of problems or error messages, first check whether you use your browser in the latest version. If necessary, perform an update.

### My account has been blocked because I have entered the wrong password too often. What do I do now?

The blocking is only temporary, wait a day or contact your administrator.

### I do not have a download button for some records?

Access to records is controlled by the management of the records. Access rights are set and managed by your administrator.

### The save button remains inactive?

Please check whether you have completed the required fields.

### When uploading, I get an error message about unauthorized formats?

A message appears like this:

> "The upload of the file apple_getamac_calmingteas_20080818_480x272.mov has been rejected. The file type mov from the class video is not allowed."

It is a restriction that was set up in the system. If necessary, contact your system administrator.

### How can I register for easydb?

Registration for easydb is made according to the regulations of the operator. Unless otherwise specified, the easydb administrator creates new users in the easydb. There is the possibility to provide self-registration in easydb. You can find instructions for this here.

### How can I completely empty my (test) system?

You can reset your (test) system to its original state by selecting "[Delete database](../webfrontend/administration/server-status)" in the server status area at the bottom right of the gearwheel icon. Please note, however, that **all data will be deleted**, you will then find an empty system and the action **cannot be undone**. If the function is deactivated, [api.settings.purgedata](../sysadmin/configuration/easydb-server.yml) must first be configured by a system administrator.

### How can I drop and recreate the elasticsearch index?

You can drop the elasticsearch index by selecting "[Reindex](../webfrontend/administration/server-status)" in the server status area at the bottom right of the gearwheel icon. This will restart the server and drop the elasticsearch directly after the server start. The index will then be rebuilt, please note that this **may take a long time**. If the function is deactivated, [api.settings.reindex](../sysadmin/configuration/easydb-server.yml) must first be configured by a system administrator.

### You get an error when importing CSV files?

If you receive errors when importing CSV files, proceed as follows to narrow down the problem:

- set the package size on the "File" tab to `"1 line"`.
- start the import again

In the right area "Table View" you can now see in the column `"easydb|status"` which record has caused a problem. The columns `"easydb|status_text"` and `"easydb|warning_text"` contain further information if necessary.

If you are unable to identify the problem, please click on "Save CSV" in the lower left corner and send this file with the error message to our support team.
