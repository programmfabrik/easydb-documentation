---
title: "Barcode"
menu:
  main:
    name: "Barcode"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/barcode"
    weight: -940
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# Barcode Plugin
The [barcode](/en/technical/plugins/reference/webfrontend/barcode) is a webfrontend plugin.

## Instalation
To enable the plugin:

In e.g. `/srv/easydb/config/easydb-server.yml`: (assuming `/srv/easydb` is your [base directory](/en/sysadmin/installation/#mount))

```yaml
plugins:
  enabled+:
    - base.barcode-display
    - base.barcode-display-pdf
```

*Note:* **base.barcode-display-pdf** is only necessary when the [PDF creator](../pdf-creator) is enabled.

The easydb-server has to be restarted to make the change effective.