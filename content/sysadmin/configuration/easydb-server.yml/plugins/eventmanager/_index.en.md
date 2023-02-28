---
title: "Eventmanager"
menu:
  main:
    name: "Eventmanager"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/eventmanager"
    weight: -948
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
easydb-server.yml:
  - plugins.enable.base.eventmanager
---

# Eventmanager Plugin

## Enable easydb-eventmanager-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.eventmanager
```