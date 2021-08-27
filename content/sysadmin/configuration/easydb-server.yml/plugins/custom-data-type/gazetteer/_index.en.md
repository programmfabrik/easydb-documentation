---
title: "Gazetteer"
menu:
  main:
    name: "Gazetteer"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type/gazetteer"
    weight: -949
    parent: "sysadmin/configuration/easydb-server.yml/plugins/custom-data-type"
easydb-server.yml:
  - plugins.enable.base.custom-data-type-gazetteer
---

# Gazetteer

## Enable easydb-custom-data-type-gazetteer

in `easydb-server.yml`:

```yaml
plugins:
  enable+:
    - base.custom-data-type-gazetteer
```


## Server YAML Variables to configure the Gazetteer Plugin

The server part of this plugin uses NodeJS to run the `update.js` script to get data from the gazetteer repository [gazetteer.dainst.org](https://gazetteer.dainst.org). This data is used to [insert hierarchic objects](https://github.com/programmfabrik/easydb-custom-data-type-gazetteer/#automatic-updating-and-inserting-of-objects-with-gazetteer-fields) into the gazetteer tree in easydb5.

The plugin uses the general NodeJS settings of the server:

```yaml
nodejs:
  node_modules: "../../node-runner/node_modules"
  node_runner_binary: "/usr/bin/env node"
  node_runner_app: "../../node-runner/app.js"
```

| Variable | Type | Required | Description | Default |
|---|---|---|---|---|
| `nodejs` | List | No | Parent element which contains the configuration for easydb's NodeJS installation | |
| &#8680;`node_modules` | `string` | No | Path to the `node_modules` folder | `../../node-runner/node_modules` (relative to `easydb-server` executable)|
| &#8680;`node_runner_binary` | `string` | No | Path to the NodeJS installation on the system | `/usr/bin/env node` |
| &#8680;`node_runner_app` | `string` | No | Path to the `noderunner` main app | `../../node-runner/app.js` (relative to `easydb-server` executable)|
