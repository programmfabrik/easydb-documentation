---
title: "Drupal"
menu:
  main:
    name: "Drupal"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/drupal"
    weight: -932
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# Drupal Plugin

## Enable easydb-drupal-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.drupal
```