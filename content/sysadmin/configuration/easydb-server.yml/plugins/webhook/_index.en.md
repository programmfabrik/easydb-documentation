---
title: "Webhook"
menu:
  main:
    name: "Webhook"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/webhook"
    weight: -936
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# Webhook Plugin

## Enable easydb-webhook-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enable+:
    - base.webhook
```
