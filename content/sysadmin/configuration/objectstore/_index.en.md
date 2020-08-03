---
title: "Objectstore"
menu:
  main:
    name: "Objectstore"
    identifier: "sysadmin/configuration/objectstore"
    parent: "sysadmin/configuration"
    weight: 62
---
# Objectstore

To configure the objectstore for your easydb, add the following lines to your easydb-server.yml. You can obtain the <objectstore-ID> from programmfabrik GmbH.

```yml
default_client:
  datamodel:
    uid: <objectstore-ID>
    server: https://schema.easydb.de/objectstore
    instance: prod
```