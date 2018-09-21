---
title: "easydb-master.yml"
layout: config
menu:
  main:
    name: "easydb-master.yml"
    identifier: "sysadmin/konfiguration/easydb-master.yml"
    parent: "sysadmin/konfiguration"
    weight: 10
---

# easydb5-master.yml

The **easydb5-master.yml** combines different configurations into one file. This file is read at startup time of the docker images of easydb and split into pieces.


# Variables

## extension 

| Variable | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `plugins` | string | yes | | |
| `external-user-schema` | bool | true: Schema is located at `/var`-directory (will be mapped in the docker container, see [installation documentation](/en/sysadmin/installation)) | yes |

```yaml
# EAS configuration. For most installations nothing has to be configured.
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
