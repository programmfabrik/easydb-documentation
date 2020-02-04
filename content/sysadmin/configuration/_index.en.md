---
title: "All Configuration"
layout: allconfig
serverconfigs:
  - config1
  - config2
  - config3
easconfigs:
  - easconfig1
  - easconfig2
  - easconfig3
tags:
  - tag1
  - tag2
  - tag3
categories:
  - cat1
  - cat2
  - cat3
menu:
  main:
    name: "Configuration"
    identifier: "sysadmin/configuration"
    parent: "sysadmin"
    weight: 6
---
# Configuration

The typical configuration of the easydb takes place outside of the containers, in YAML files.

## Load order

The YAML files are loaded in the following order:

- `/srv/easydb/config/`[easydb5-master.yml](easydb5-master.yml/) Assumption from now on: the folder `/srv/easydb/config` was chosen during [installation](/en/sysadmin/installation).
- `/srv/easydb/config/`[easydb-server.yml](easydb-server.yml/) and `/srv/easydb/config/easydb-server.d/*.yml` for the containers easydb-server and easydb-webfrontend
- `/srv/easydb/config/`[eas.yml](eas/) for the container easydb-eas
- `/srv/easydb/config/easydb_asset_server.conf` (discouraged, soon obsolete, not YAML) for the container easydb-eas
- `/srv/easydb/config/`[fylr.yml](fylr.yml/) for the container easydb-fylr
- `/srv/easydb/config/`[elasticsearch.yml](elastic/elasticsearch.yml/) for the container easydb-elasticsearch
- `/srv/easydb/config/pgsql.yml` for the container easydb-pgsql

Inside the containers:

- Files inside of containers should only be relevant for you as a customer in exceptional cases.
- Files inside of containers are overwritten by recreation of containers, for example, during updates. This is opposed to files which are mapped/mounted into containers ("volumes").
- For example in the docker container easydb-server, the file `easydb-server.yml`, if available, is first loaded from the current directory of the executable.
- Then other files are loaded that are specified as arguments in the command line (with `--configfile`) in the order in which they are specified.

A YAML file can also include other configuration files:

- The variable **include_before** is a list of files that are loaded before the file in which it is defined
- The variable **include_after** is a list of files that are loaded after the file in which it is defined
- Such files are defined either with an absolute path or relative to the YAML file in which they were specified. Paths will be interpreted inside the container, where for example `/srv/easydb/config`(outside) is typically mapped to `/config`(inside).

## Auxiliary configuration

The Easydb server is primarily configured by YAML files, but there are other configuration mechanisms for certain areas:

- [E-Mail-Configuration](/en/sysadmin/konfiguration/recipes/email)
- [Plugin Configuration](/en/sysadmin/konfiguration/easydb-server.yml/plugin)
- [HTTPS](/en/sysadmin/konfiguration/recipes/https)
- [LDAP](/en/sysadmin/konfiguration/easydb-server.yml/ldap)
- [Data Model-Server](/en/webfrontend/administration/datamodel/#objectstore)
- [Single Sign-On](/en/sysadmin/konfiguration/recipes/sso)
- [File size for download and preview](/en/sysadmin/konfiguration/easydb-server.yml/produce)


[not ready]: # "- [EAS-Configuration](sysadmin/konfiguration/eas.yml)  "

[not ready2]: # "- [L10n-Configuration](sysadmin/konfiguration/l10n)  "

[not ready3]: # "- [Runtime-Configuration](sysadmin/konfiguration/baseconfig)  "

