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

The plugin must be additionally activated in the frontend:
EN: https://docs.easydb.de/en/webfrontend/administration/base-config/cms/#typo3
DE: https://docs.easydb.de/de/webfrontend/administration/base-config/cms/#typo3
