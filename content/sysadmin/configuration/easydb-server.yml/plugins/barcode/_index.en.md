---
title: "Barcode"
menu:
  main:
    name: "Barcode"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/barcode"
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# Barcode Plugin

The easydb barcode plugin is a webfrontend plugin. To enable it:

In e.g. `/srv/easydb/config/easydb-server.yml`: (assuming `/srv/easydb` is your [base directory](../../../installation/#mount))

```yaml
plugins:
  enabled+:
    - base.barcode-display
    - base.barcode-display-pdf
    - base.pdf-creator
```

The easydb-server has to be restarted to make the change effective.


