---
title: "hijri-gregorian-converter"
menu:
  main:
    name: "hijri-gregorian-converter"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/hijri-gregorian-converter"
    weight: -930
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# hijri-gregorian-converter

## Enable easydb-hijri-gregorian-converter-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.hijri-gregorian-converter
```