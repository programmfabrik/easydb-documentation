---
title: "Display of References"
menu:
  main:
    name: "Display of References"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-mask-splitter-detail-linked"
    weight: -941
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# Custom mask splitter - Detail Linked (Display of References)
The [Custom mask splitter - Detail Linked](/en/webfrontend/administration/datamodel/mask/mask-splitter/#display-of-references) plugin is a webfrontend plugin.

## Installation
To enable the plugin:

In e.g. `/srv/easydb/config/easydb-server.yml`: (assuming `/srv/easydb` is your [base directory](/en/sysadmin/installation/#mount))

```yaml
plugins:
  enabled+:
    - base.custom-mask-splitter-detail-linked
```

The easydb-server has to be restarted to make the change effective.