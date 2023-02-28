---
title: "easydb4migration"
menu:
  main:
    name: "easydb4migration"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/easydb4migration"
    weight: -939
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
easydb-server.yml:
  - plugins.enable.base.easydb4migration
---

# Easydb4migration Plugin

## Enable easydb-easydb4migration-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.easydb4migration
```