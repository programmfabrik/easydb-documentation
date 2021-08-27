---
title: "Wordpress"
menu:
  main:
    name: "Wordpress"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/wordpress"
    weight: -935
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# Wordpress Plugin

## Enable easydb-wordpress-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enable+:
    - base.wordpress
```

The plugin uses the external url of the server:

```yaml
server:
  external_url: "http://example.com"
```
