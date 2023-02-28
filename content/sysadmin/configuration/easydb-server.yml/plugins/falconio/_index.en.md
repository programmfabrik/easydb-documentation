---
title: "Falconio"
menu:
  main:
    name: "Falconio"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/falconio"
    weight: -931
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# Falconio Plugin

## Enable easydb-falconio-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.falconio
```