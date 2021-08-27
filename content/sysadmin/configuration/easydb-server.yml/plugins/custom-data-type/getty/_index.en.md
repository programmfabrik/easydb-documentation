---
title: "Getty"
menu:
  main:
    name: "Getty"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/getty"
    weight: -947
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-getty
---

# Getty

## Enable easydb-custom-data-type-getty

in `easydb-server.yml`:

```yaml
plugins:
  enable+:
    - base.custom-data-type-getty
```