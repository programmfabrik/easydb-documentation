---
title: "Link"
menu:
  main:
    name: "Link"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/link"
    weight: -948
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-link
---

# Link

## Enable easydb-custom-data-type-link

in `easydb-server.yml`:

```yaml
plugins:
  enable+:
    - base.custom-data-type-link
```