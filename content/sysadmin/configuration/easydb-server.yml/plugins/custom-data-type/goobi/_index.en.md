---
title: "goobi"
menu:
  main:
    name: "goobi"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/goobi"
    weight: -943
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-goobi
---

# goobi

## Enable easydb-custom-data-type-goobi

in `easydb-server.yml`:

```yaml
plugins:
  enable+:
    - base.custom-data-type-goobi
```