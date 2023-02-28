---
title: "export-transport-ftp"
menu:
  main:
    name: "export-transport-ftp"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/export-transport-ftp"
    weight: -946
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
easydb-server.yml:
  - plugins.enable.base.export-transport-ftp
---

# Export transport ftp Plugin

## Enable easydb-export-transport-ftp-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.export-transport-ftp
```