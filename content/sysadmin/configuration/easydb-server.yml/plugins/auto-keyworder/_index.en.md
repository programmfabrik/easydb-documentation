---
title: "Auto Keyworder"
menu:
  main:
    name: "Auto Keyworder"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/auto-keyworder"
    weight: -942
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
easydb-server.yml:
  - plugins.enable.base.auto-keyworder
---

# Auto Keyworder Plugin

This page describes the server configuration in `easydb-server.yml` for the [Auto Keyworder Plugin](/en/webfrontend/datamanagement/features/keyword_plugin/).

## Enabling the plugin

To use the plugin, it must be enabled in `easydb-server.yml`:

```
plugins:
  enabled+:
    - base.auto-keyworder
```

## Basic Settings

The following configuration must be added to `easydb-server.yml`:

* `baseconfig_poll_interval_sec`
    - Delay in seconds before the main loop loads the base config and updates the plugin configurations
    - If a worker loop is running at the moment, the delay is applied after the worker loops are done
    - If `start_now` is set to `True` in the Base Configuration or by the API call, this flag will also be checked with this delay (see below)
    - Defaults to `10`

* `poll_start_hour`
    - Specify a hour between `0` and `23`
    - The next time where the objects are searched and updated is the next possible time when this full hour is reached
    - Defaults to `0`

* `poll_every_days`
    - The next update time would be starting at the next day
    - This value can be increased to wait several days before starting the update process again
    - A value of `0` means the worker loop runs every day
    - Minimum: `0`
    - Defaults to `0`

* `search_chunk_size`
    - (Maximum) number of objects that are searched in one batch
    - Minimum: `1`
    - Maximum: `1000`
    - Defaults to `100`

* `webhook_hmac`
    - HMAC secret to authenticate API calls. If this value is not set, the plugin API can not be used
    - This value must also be used for webhooks to start the update process (see below)

## Logging levels

The plugin has different log levels, the top level debugger is `pf.plugin.base.auto_keyworder`.

For detailled logging, the log level for the following loggers can be set to `debug`:

- `pf.plugin.base.auto_keyworder`
- `pf.plugin.base.auto_keyworder.cloudsight.config` (very verbose)
- `pf.plugin.base.auto_keyworder.cloudsight.worker`
- `pf.plugin.base.auto_keyworder.api`
- `pf.plugin.base.auto_keyworder.eas`
- `pf.plugin.base.auto_keyworder.easydb_api` (very verbose)
- `pf.plugin.base.auto_keyworder.search` (very verbose)

The loggers `cloudsight.config`, `search` and `easydb_api` are very verbose and print the parsed base configurations, search requests and responses, and the object data that are sent to the easydb api as JSON objects to the console. Only activate these loggers if necessary.

## Example Configuration in `easydb-server.yml`

```
auto_keyworder:
  baseconfig_poll_interval_sec: 30
  poll_start_hour: 0
  poll_every_days: 3
  search_chunk_size: 500
  webhook_hmac: '894wf76w93487t3f9'
```
