---
title: "eas.yml"
layout: config
menu:
  main:
    name: "eas.yml"
    identifier: "sysadmin/konfiguration/eas.yml"
    parent: "sysadmin/konfiguration"
    weight: 60
---

# eas.yml

**work in progress**

| variable | type | default | description |
|----------|------|---------|-------------|
|`canonical-name`          | `string` | `easydb-eas` | external name of EAS |
|`docker-hostname`         | `string` | `easydb-eas` | name of docker container |
|`log-level`               | one of `debug`, `info`, `warn`, `error` | `info` | log level |
|`pgsql`                   |          |              | connection settings for PostgreSQL |
|&#8193;`host`             | `string` | `easydb-pgsql` | |
|&#8193;`port`             | `integer` | `5432` | |
|&#8193;`username`         | `string` | `***` | |
|&#8193;`password`         | `string` | `***` | |
|&#8193;`database`         | `string` | `eas` | |
|`smtp`                    |          |       | mail server settings |
|&#8193;`server`           | `string` | `mail` | |
|&#8193;`from-address`     | `string` | `root@localhost` | |
|&#8193;`hostname`         | `string` | `localhost` | |
|`imagemagick`             |          | | ImageMagick settings |
|&#8193;`policy`           |          | | IM policies |
|&#8193;&#8193;`resource`  |          | | IM resource policies |
|&#8193;&#8193;&#8193;`memory` | `string` | `1024MiB` | |
|&#8193;&#8193;&#8193;`map`    | `string` | `2048MiB` | |
|&#8193;&#8193;&#8193;`width`  | `string` | `64KP` | |
|&#8193;&#8193;&#8193;`height` | `string` | `64KP` | |
|&#8193;&#8193;&#8193;`area`   | `string` | `512MB` | |
|&#8193;&#8193;&#8193;`disk`   | `string` | `4GiB` | |
