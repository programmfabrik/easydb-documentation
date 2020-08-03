---
title: "Display field values"
menu:
  main:
    name: "Display field values"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/display-field-values"
    weight: -940
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# Display field values plugin
The [Display field values](/en/webfrontend/administration/datamodel/mask/mask-splitter) plugin is a webfrontend plugin.

## Installation
To enable the plugin:

In e.g. `/srv/easydb/config/easydb-server.yml`: (assuming `/srv/easydb` is your [base directory](/en/sysadmin/installation/#mount))

```yaml
plugins:
  enabled+:
    - base.display-field-values
```

The easydb-server has to be restarted to make the change effective.