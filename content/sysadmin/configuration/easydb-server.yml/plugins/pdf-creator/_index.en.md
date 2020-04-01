---
title: "Pdf Creator"
menu:
  main:
    name: "Pdf Creator"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/pdf-creator"
    weight: -941
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# Barcode Plugin
The [pdf creator](/en/technical/plugins/reference/webfrontend/pdf-creator) is a webfrontend plugin.

## Instalation
To enable the plugin:

In e.g. `/srv/easydb/config/easydb-server.yml`: (assuming `/srv/easydb` is your [base directory](/en/sysadmin/installation/#mount))

```yaml
plugins:
  enabled+:
    - base.pdf-creator
```

The easydb-server has to be restarted to make the change effective.