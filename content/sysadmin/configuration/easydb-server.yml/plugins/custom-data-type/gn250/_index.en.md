---
title: "gn250"
menu:
  main:
    name: "gn250"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/gn250"
    weight: -945
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-gn250
---

# gn250

## Enable easydb-custom-data-type-gn250

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.custom-data-type-gn250
```