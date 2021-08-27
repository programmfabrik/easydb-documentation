---
title: "nomisma"
menu:
  main:
    name: "nomisma"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/nomisma"
    weight: -942
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-nomisma
---

# nomisma

## Enable easydb-custom-data-type-nomisma

in `easydb-server.yml`:

```yaml
plugins:
  enable+:
    - base.custom-data-type-nomisma
```
