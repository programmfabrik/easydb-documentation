---
title: "Georef"
menu:
  main:
    name: "Georef"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/georef"
    weight: -944
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-georef
---

# Georef

## Enable easydb-custom-data-type-georef

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.custom-data-type-georef
```