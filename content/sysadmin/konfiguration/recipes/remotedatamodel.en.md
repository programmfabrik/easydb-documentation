---
title: "Connection to a data model server"
menu:
  main:
    name: "Remote data model"
    identifier: "sysadmin/konfiguration/recipes/datamodelserver"
    parent: "sysadmin/konfiguration/recipes"
    weight: 1
---
# Connection to a remote data model server

You can define that the data model is not only stored locally but also on a remote data model server.

This is typically done when someone else is also doing changes on your data model, e.g. on a separate test instance of easydb.

The data model server in this scenario tries to make sure that the data model is not changed on both instances at once but only on one instance at a time. ("locking")

## Configuration

To the configuration file easydb5-master.yml, which you created during [Installation](../../../installation), add the lines:

```yaml
easydb-server:
  default_client:
    datamodel:
      uid: 12345678-90ab-cdef-1234-567890abcdef
      server: https://schema.easydb.de/objectstore
      instance: prod
```

Only add lines that you do not already have. (e.g. do not add a second "easydb-server:" line, you probably already have it)

> Take care to use consistent indentation. We recommend to use two spaces per indentation-level and no tabulators.

Make sure to use the "datamodel uid" that the data model server is using for *your* datamodel. If in doubt, ask the provider of the data model server.

The data model server https://schema.easydb.de/objectstore is provided by Programmfabrik GmbH. Contact: support@programmfabrik.de.
