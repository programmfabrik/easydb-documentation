---
title: "editor-tagfilter-defaults"
menu:
  main:
    name: "editor-tagfilter-defaults"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/tagfilter"
    weight: -940
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
easydb-server.yml:
  - plugins.enable.base.editor-tagfilter-defaults
---

# Editor tagfilter Plugin

## Enable easydb-editor-tagfilter-defaults-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enable+:
    - base.editor-tagfilter-defaults
```
