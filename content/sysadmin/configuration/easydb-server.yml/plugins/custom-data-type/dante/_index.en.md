---
title: "Dante"
menu:
  main:
    name: "Dante"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/dante"
    weight: -950
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-dante
---

# Dante

## Enable easydb-custom-data-type-dante

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.custom-data-type-dante
```