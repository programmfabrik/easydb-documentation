---
title: "Objectstore"
menu:
  main:
    name: "Objectstore"
    identifier: "sysadmin/configuration/objectstore"
    parent: "sysadmin/configuration"
    weight: 1
---
# Objectstore

To configure the Objectstore for your easydb, put the following lines in your easydb-server.yml. The **objectstore-ID** you receive from programmfabrik GmbH.

```yml
default_client:
  datamodel:
    uid: <objectstore-ID>
    server: https://schema.easydb.de/objectstore
    instance: prod
```