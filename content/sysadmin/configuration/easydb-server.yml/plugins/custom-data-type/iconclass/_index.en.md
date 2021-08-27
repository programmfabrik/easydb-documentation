---
title: "iconclass"
menu:
  main:
    name: "iconclass"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/iconclass"
    weight: -942
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-iconclass
---

# iconclass

## Enable easydb-custom-data-type-iconclass

in `easydb-server.yml`:

```yaml
plugins:
  enable+:
    - base.custom-data-type-iconclass
```