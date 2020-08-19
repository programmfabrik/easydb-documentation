---
title: "Pdf Creator"
menu:
  main:
    name: "Pdf Creator"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/pdf-creator"
    weight: -941
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# Barcode Plugin
The [pdf creator](/en/technical/plugins/reference/webfrontend/pdf-creator) is a webfrontend plugin.

## Installation

Make sure you did at least once pull the container images:

```bash
docker pull docker.easydb.de/pf/fylr
docker pull docker.easydb.de/pf/chrome
```

Create the chrome container:

```bash
docker run -d -ti \
    --name chrome \
    --restart=always \
    --shm-size=1g \
    --net easydb_default \
    docker.easydb.de/pf/chrome
```

## Activiation
To enable the plugin:

In e.g. `/srv/easydb/config/easydb-server.yml`: (assuming `/srv/easydb` is your [base directory](/en/sysadmin/installation/#mount))

```yaml
plugins:
  enabled+:
    - base.pdf-creator
```

The easydb-server has to be restarted to make the change effective.

## Configuration in the Frontend

Surf to your easydb web URL and there select in the menu: Base Config - Extended Functions - Fylr URL 

Set Fylr URL to your easydb URL plus `/fylr/pdf`.

Example: https://easydb.example.com/fylr/pdf

