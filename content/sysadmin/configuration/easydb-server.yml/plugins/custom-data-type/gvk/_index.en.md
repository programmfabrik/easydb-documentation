---
title: "Gvk"
menu:
  main:
    name: "Gvk"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/gvk"
    weight: -946
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-gvk
---

# Gvk

## Enable easydb-custom-data-type-gvk

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.custom-data-type-gvk
```