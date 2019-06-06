---
title: "Connector"
menu:
  main:
    name: "Connector"
    identifier: "sysadmin/konfiguration/recipes/connector"
    parent: "sysadmin/konfiguration/recipes"
    weight: 3
---

# Connector

The easydb connector is a webfrontend plugin which allows to connect remote easydbs to the local one.

The plugin needs to be **installed** and **enabled** on the local and the remote easydb server.

This is how the plugin is enabled in e.g. `/srv/easydb/config/easydb-server.yml`: (assuming `/srv/easydb` is your [base directory](../../../installation/#mount))

```yaml
plugins:
  enabled+:
    - base.connector
```

The easydb-server has to be restarted to make the change effective.

The following configuration is done additionally in the webfrontend.

## Base Config

The tab base config uses the following config options.

> Its important to configure the URLs on both sides of the connection, the remote needs to have all connecting connectors listed in **Allowed Origins** on the **General** tab of the base config, the local easydb needs to list all remotes in the **Connector** tab in **General Options**.

### General Options

| Option           | Description                                                  |
| ---------------- | ------------------------------------------------------------ |
| Active for users | If enabled, the connector configuration is accessible for users with the system right **root** or **connector**. |

### Instances

Each remote **easydb** needs to be configured as individual instance. The connection is done using a single account on the remote easydb for all users of the local **easydb**. However, each login, logout, and download event are logged on the remote easydb with the *login*, *displayname*, and *email* of the local connecting user. 

The privacy implications of this, need to be communicated to the user by the administrator of the local easydb.

> If the remote **easydb** has pending messages or tasks for the remote user, the local user is unable to connect until all pending messages and tasks are read and done. In such cases, the local users will get see an error message in their connector configuration dialog.

| Option   | Description                                                  |
| -------- | ------------------------------------------------------------ |
| Active   | If enabled, this instance                                    |
| Name     | The local name of the remote **easydb**. By setting a name, you overwrite the actual name of the remote **easydb**. This option is mandatory. |
| Url      | The *URL* of the remote **easydb**.                          |
| Login    | The login for the user of the remote **easydb**.             |
| Password | The *password* for the user of the remote **easydb**.        |
|          |                                                              |

### FYLR. configuration

FYLR. is needed to support download of multiple files from remote **easydbs** using the ZIP file format. Without this option setup, the local user can only download one file at once.

| Option | Description                       |
| ------ | --------------------------------- |
| Url    | The *URL* of Fylr, ending in /zip |

FYLR. does allow zipping the following URLs:

- EASYDB_EXTERNAL_URL/fylr/
- */eas/partitions/

If you have not already installed the FLYR. component:
```
docker pull docker.easydb.de/pf/fylr
```

To start FLYR., please refer to the `docker run` command on the [installation](../../../installation/#start)) page.

### Migrated easydb 4 instances

This part of the setup is necessary only if you are using a migrated easydb 4, and remote users stored objects of the local easydb in their collections and presentation.

These settings are needed so that the remote objects can be found on the remote easydb 5 and updated with their new easydb 5 ID in the remote easydb. This update to easydb 5 IDs is a task the remote user has to start manually from the collection's context menu or from inside the collection detail view. The webfrontend will inform the remote users if such objects exist inside the user's collection or presentation.

> You can contact our support to learn the required settings for your easydb. The information can be found in the /ezadmin tool of the easydb 4.   Or in the eadb_attrs table of the backup sqlite file of the easydb for.

| Option                    | Description                                                  |
| ------------------------- | ------------------------------------------------------------ |
| easydb ID of the 4        | This is the unique ID of the easydb 4.or ask the administrator of the remote easydb. |
| Table ID in the 4         | This is the ID of the main table in easydb 4. It is generally **01**. |
| Table name in the 4       | This is the name of the main table in easydb 4, such as **Bilder**, or **assets**. |
| Objecttype in the 5       | Name of the objecttype of the mapped easydb 4 table in easydb 5. |
| Reference column in the 5 | The migration of easydb 4 uses a reference column in the 5 to store the old easydb 4 id. This is generally **easydb4_reference**. |

#### Notation for migration scripts

The global_object_id for migrated easydb objects looks as follows: ```<easydb-id><table-id><object-id>@easydb4```. The ```<object-id>``` is padded with ```0``` to fill seven digits, ```<table-id>``` and  ```<easydb-id>``` are two digits.

In Javascript this look like this:

```javascript
easydb_id * Math.pow(10, 9) + table_id * Math.pow(10, 7) + object_id + "@easydb4"
```









