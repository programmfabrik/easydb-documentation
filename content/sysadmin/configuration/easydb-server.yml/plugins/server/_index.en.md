---
title: "Server"
menu:
  main:
    name: "Server"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/server"
    weight: -949
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
easydb-server.yml:
  - plugins.enable.base.server
---

# Server Plugin

## Enable easydb-server-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.server
```