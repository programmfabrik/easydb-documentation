---
title: "Location"
menu:
  main:
    name: "Location"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/location"
    weight: -941
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-location
---

# Location

## Enable easydb-custom-data-type-location

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.custom-data-type-location
```