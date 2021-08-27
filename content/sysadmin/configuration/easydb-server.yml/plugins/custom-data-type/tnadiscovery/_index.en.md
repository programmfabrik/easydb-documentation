---
title: "tnadiscovery"
menu:
  main:
    name: "tnadiscovery"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/tnadiscovery"
    weight: -942
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-tnadiscovery
---

# tnadiscovery

## Enable easydb-custom-data-type-tnadiscovery

in `easydb-server.yml`:

```yaml
plugins:
  enable+:
    - base.custom-data-type-tnadiscovery
```