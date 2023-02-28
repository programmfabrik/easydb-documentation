---
title: "Remote"
menu:
  main:
    name: "Remote"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/remote"
    weight: -945
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
easydb-server.yml:
  - plugins.enable.base.remote-plugin
---

# Remote Plugin

## Enable easydb-remote-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.remote-plugin
```