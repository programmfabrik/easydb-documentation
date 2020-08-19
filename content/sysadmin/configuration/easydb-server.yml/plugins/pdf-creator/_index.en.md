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
    --net easy5net \
    docker.easydb.de/pf/chrome
```

Check that your container network is `easy5net`. Use the same for chrome as for the other containers.

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

1. Surf to your easydb web URL

2. Login with an account with administrative privileges

3. Select in the menu: Base Config - Extended Functions - Fylr URL 

4. Set Fylr URL to your easydb URL plus `/fylr/pdf`.

    Example: https://easydb.example.com/fylr/pdf

