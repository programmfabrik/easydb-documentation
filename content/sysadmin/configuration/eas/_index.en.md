---
title: "eas.yml"
layout: config
menu:
  main:
    name: "eas.yml"
    identifier: "sysadmin/configuration/eas.yml"
    parent: "sysadmin/configuration"
    weight: 60
---

# eas.yml

`eas.yml` is the typical main configuration file for the container easydb-eas (which is hosting the [easydb asset server](/en/sysadmin/eas/)). But it is not the only one. For more information on this, see [configuration](/en/sysadmin/configuration/).

`eas.yml` is read from the subdirectory `config` of the [base directory](/en/sysadmin/installation/#mount) which was chosen during installation. The path outside the container would be `/srv/easydb/config/eas.yml`, assuming your base directory is `/srv/easydb`.

> In yml-files created by Programmfabrik we use an indentation of 2 spaces per &#8680;.

| variable <div style="width:200px"></div> | type | default | description |
|----------|------|---------|-------------|
|`canonical-name`          | `string` | `easydb-eas` | external name of EAS |
|`docker-hostname`         | `string` | `easydb-eas` | name of docker container |
|`log-level`               | one of `debug`, `info`, `warn`, `error` | `info` | log level |
|`pgsql`                   |          |              | connection settings for PostgreSQL |
|&#8680;`host`             | `string` | `easydb-pgsql` | |
|&#8680;`port`             | `integer` | `5432` | |
|&#8680;`username`         | `string` | `***` | |
|&#8680;`password`         | `string` | `***` | |
|&#8680;`database`         | `string` | `eas` | |
|`smtp`                    |          |       | mail server settings |
|&#8680;`server`           | `string` | `mail` | |
|&#8680;`from-address`     | `string` | `root@localhost` | |
|&#8680;`hostname`         | `string` | `localhost` | |
|`imagemagick`             |          | | ImageMagick settings |
|&#8680;`policy`           |          | | IM policies |
|&#8680;&#8680;`resource`  |          | | IM resource policies |
|&#8680;&#8680;&#8680;`memory` | `string` | `1024MiB` | |
|&#8680;&#8680;&#8680;`map`    | `string` | `2048MiB` | |
|&#8680;&#8680;&#8680;`width`  | `string` | `64KP` | |
|&#8680;&#8680;&#8680;`height` | `string` | `64KP` | |
|&#8680;&#8680;&#8680;`area`   | `string` | `512MB` | |
|&#8680;&#8680;&#8680;`disk`   | `string` | `4GiB` | |
|`apache-mmap`             | `string` | `"on"` | Alternative: `"off"`. Whether to use Apache's `EnableMMap`, see [here](/en/sysadmin/eas/faq#corrupted-asset-read-access). |
|`num-workers`             | `integer` | `1` | Maximum simultaneous processes of time-intensive work. Also see [here](/en/sysadmin/eas/conf/#number-of-workers). Should not be bigger than the number of CPU cores. |
|`num-soffice`             | `integer` | `2` | Maximum simultaneous processes of office documents. Must always be bigger than `num-workers`. |
|`num-services`             | `integer` | `5` | See [here](/en/sysadmin/eas/conf/#eas-num-services). |
|`trusted-net`             | string | | Networks with full access to EAS API, for example: `10.12.12.0/24`. Requests originating from these networks can manipulate the asset server without further restrictions, so use with care. Only the `easydb-server` is required to have this full access. In addition to the value set, the default Docker network (`172.0.0.0/8`) and localhost (`127.0.0.1`) already have this access, so usually no extra configuration is required. It is possible to set multiple networks separated by space, e.g. `10.12.0.0/16 10.13.0.0/16`. You should check `https://<external-address>/eas/config` to ensure the restrictions are in place. When configured correctly, HTTP 403 ("Access forbidden") is returned. |


## example

```yaml
canonical-name: https://official.example.com
log-level: debug
pgsql:
  host: pgsql
  port: 15432
  username: docker
  password: d8s2H3.mgy/ap6
  database: eas
num-workers: 4
num-soffice: 5
trusted-net: 10.123.123.0/24

smtp:
  server: relay.example.com
  hostname: easydb-server.example.com
  from-address: noreply@example.com
```

In many cases you do not need this file at all.

The typical `eas.yml` only contains `num-workers` and `num-soffice`.
