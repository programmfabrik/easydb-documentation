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

# easydb-master.yml

The **easydb-master.yml** combines different configurations into one file. This file is read at startup time of the docker images of easydb and split into pieces.


# Variables

## extension 

| Variable | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `plugins` | string | yes | | |
| `external-user-schema` | bool | true: Schema is located at `/var`-directory (will be mapped in the docker container, see [installation documentation](/en/sysadmin/installation)) | yes |