---
title: "easydb5-master.yml"
layout: config
menu:
  main:
    name: "easydb5-master.yml"
    identifier: "sysadmin/konfiguration/easydb5-master.yml"
    parent: "sysadmin/konfiguration"
    weight: 10
---

# easydb5-master.yml

The **easydb5-master.yml** combines different configurations into one file. This file is read at startup time of the docker images of easydb and split into pieces.

Example content: (only the first paragraph is mandatory)

```yaml
# easydb-server: the core of easydb5
easydb-server:
  docker-hostname: easydb-server
  pgsql:
    database: easydb
  server:
    external_url: http://hostname.as.seen.in.browser.example.com
  extension:
    external-user-schema: true

# Easydb Asset Sserver (EAS) configuration. For most installations nothing has to be configured.
eas:
  docker-hostname: easydb-eas       # also used by other containers to find EAS
  canonical-name: easydb-eas		# used for self-referencial URLs in EAS's Apache
  log-level: info                   # critical, error, warning, info, debug
  pgsql:                            # database configuration
    host: easydb-pgsql
    port: 5432
    username: ****
    password: ****
    database: eas
  num-workers: 1                    # can be set, but there are constraints with
                                    # EAS_NUM_SOFFICE (must be greater than EAS_NUM_WORKERS)
  trusted-net: 172.0.0.0/8          # network with full access to EAS API, usually only
                                    # internal Docker network. Use with care.

# Configuration used by multiple containers
common:
  email:
    server: mail                    # mail relay host name
    from-address: root@localhost    # envelope sender address
    hostname: localhost             # sender host name
```
