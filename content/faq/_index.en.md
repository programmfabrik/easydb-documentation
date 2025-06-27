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

It is a restriction that was set up in [Base config](/en/webfrontend/administration/base-config/) - [Upload](/de/webfrontend/administration/base-config/upload/). If necessary, please contact your administrator.

### The calculation of a preview version failed. What can I do?

This can be caused by many problems. For example, it could be a broken original file or a lack of disk space. First find and resolve the cause. Therefore, please contact your system administrator and, if in doubt, contact support@programmfabrik.de and provide a sample file to examine. 2. To make sure that you have fixed the cause, upload a file into your easydb and check that preview versions are now made. 3. Calculate the missing versions that have failed while the problem persisted: [Sysadmin Manual](/en/sysadmin/eas/faq/#restart-all-failed-jobs)

### How can I register for easydb?

Registration for easydb is made according to the regulations of the operator. Unless otherwise specified, the easydb administrator creates new users in the easydb. There is the possibility to provide self-registration in easydb. You can find instructions for this [here](./../../content/tutorials/rechte_nutzer/).

### How can I completely empty my (test) system?

You can reset your (test) system to its original state by selecting "[Delete database](../webfrontend/administration/server-status)" in the server status area at the bottom right of the gearwheel icon. Please note, however, that **all data will be deleted**, you will then find an empty system and the action **cannot be undone**. If the function is deactivated, [api.settings.purgedata](../sysadmin/configuration/easydb-server.yml) must first be configured by a system administrator.

### How can I drop and recreate the elasticsearch index?

You can drop the elasticsearch index by selecting "[Reindex](../webfrontend/administration/server-status/#controls)" after the gearwheel icon in the bottom right area of the server status. This will restart the server and drop the elasticsearch directly after the server start. The index will then be rebuilt, please note that this **may take a long time**. If the function is deactivated, [api.settings.reindex](/en/sysadmin/configuration/easydb-server.yml/available-variables/) must first be configured to be [true](../sysadmin/configuration/easydb-server.yml) by a system administrator.

Instead of allowing this, the system administrator may trigger the re-index once by just the following sql command in the database of the easydb (not the database of the EAS).

To get the name of the database, look for `db-name` in the response of your easydb at https://myeasydb.example.com/api/v1/settings (replace myeasydb.example.com).

Connect to the database: (replace my-db-name)

```bash
docker exec -ti easydb-pgsql psql -U postgres my-db-name
```

The SQL command:

```sql
SELECT easydb_reindex();
```

### You get an error when importing CSV files?

If you receive errors when importing CSV files, proceed as follows to narrow down the problem:

- set the package size on the "File" tab to `"1 line"`.
- start the import again

In the right area "Table View" you can now see in the column `"easydb|status"` which record has caused a problem. The columns `"easydb|status_text"` and `"easydb|warning_text"` contain further information if necessary.

If you are unable to identify the problem, please click on "Save CSV" in the lower left corner and send this file with the error message to our support team.



### I want to change my domain. What do I have to do?

To change the primary domain of easydb we recommend to replace the old domain in all files below /srv/easydb/config and then restart easydb.

Find all mentions:

```
grep -IRis 'old\.' /srv/easydb/config --color
```

Restart after changing (only the relevant containers here):

```
docker restart easydb-eas easydb-server easydb-webfrontend easydb-fylr
```

Also, of course, in /etc/apache2/sites-enabled/easydb-ssl.conf.
