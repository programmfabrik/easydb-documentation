---
title: remote data model
layout: config
menu:
  main:
    name: "remote data model"
    identifier: "sysadmin/configuration/easydb-server.yml/config_webfrontend/remotedatamodel"
    parent: "sysadmin/configuration/easydb-server.yml/config_webfrontend"
    weight: -999
---

# Connection to a remote data model server

You can define that the data model is not only stored locally but also on a remote data model server.

This is typically done when someone else is also doing changes on your data model, e.g. on a separate test instance of easydb.

The data model server in this scenario tries to make sure that the data model is not changed on both instances at once but only on one instance at a time. ("locking")

## Configuration

To the configuration file easydb-master.yml, which you created during [Installation](../../../../installation), add the lines:

```yaml
default_client:
  datamodel:
    uid: 12345678-90ab-cdef-1234-567890abcdef
    server: https://schema.easydb.de/objectstore
    instance: prod
```

Only add lines that you do not already have. (e.g. do not add a second "default_client:" line)

> Take care to use consistent indentation. We recommend to use two spaces per indentation-level and no tabulators (not supported by yaml).

Make sure to use the "datamodel uid" that the data model server is using for *your* datamodel. If in doubt, ask the provider of the data model server.

The data model server https://schema.easydb.de/objectstore is provided by Programmfabrik GmbH. Contact: `support@programmfabrik.de`.
