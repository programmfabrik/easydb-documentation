---
title: "Typo 3"
menu:
  main:
    name: "Typo 3"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/typo3"
    weight: -934
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# Typo-3 Plugin

## Enable easydb-typo3-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enable+:
    - base.typo3
```
