---
title: "OAI"
menu:
  main:
    name: "OAI"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/oai"
    weight: -942
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
easydb-server.yml:
  - plugins.enable.base.oai
---

# Oai Plugin

## Enable easydb-oai-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.oai
```

The plugin uses the external url of the server:

```yaml
server:
  external_url: "http://example.com"
```
