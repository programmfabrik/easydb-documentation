---
title: "HTML Editor"
menu:
  main:
    name: "HTML Editor"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/html-editor"
    weight: -948
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-html-editor
---

# HTML Editor
The custom data type [HTML Editor](/en/technical/plugins/reference/webfrontend/html-editor) is a webfrontend plugin.

## Installation
To enable the plugin:

In e.g. `/srv/easydb/config/easydb-server.yml`: (assuming `/srv/easydb` is your [base directory](/en/sysadmin/installation/#mount))

```yaml
plugins:
  enabled+:
    - base.custom-data-type-html-editor
```

The easydb-server has to be restarted to make the change effective.