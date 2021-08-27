---
title: "Geonames"
menu:
  main:
    name: "Geonames"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/geonames"
    weight: -945
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-geonames
---

# Geonames

## Enable easydb-custom-data-type-geonames

in `easydb-server.yml`:

```yaml
plugins:
  enable+:
    - base.custom-data-type-geonames
```