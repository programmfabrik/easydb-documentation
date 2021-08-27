---
title: "Basemigration"
menu:
  main:
    name: "Basemigration"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/basemigration"
    weight: -943
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
easydb-server.yml:
  - plugins.enable.base.basemigration
---

# Basemigration Plugin


## Enable easydb-basemigration-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enable+:
    - base.basemigration
```