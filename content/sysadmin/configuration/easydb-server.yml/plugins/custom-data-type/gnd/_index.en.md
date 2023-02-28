---
title: "GND"
menu:
  main:
    name: "GND"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/gnd"
    weight: -943
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-gnd
---

# GND

## Enable easydb-custom-data-type-gnd

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.custom-data-type-gnd
```