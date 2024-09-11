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

This page describes the server configuration in `easydb-server.yml` for the [Auto Keyworder Plugin](/en/webfrontend/datamanagement/features/plugins/autokeyworder/).

## Enabling the plugin

To use the plugin, it must be enabled in `easydb-server.yml`:

```
plugins:
  enabled+:
    - base.auto-keyworder
```

## Basic Settings

The following configuration can be added to `easydb-server.yml` under the top level key `auto_keyworder`. This is only necessary if you want to override the default values.

The `webhook_hmac` is optional and only necessary if you want to use the additional [Plugin API](/en/webfrontend/datamanagement/features/plugins/autokeyworder/#plugin-api) features.

| Variable | Type | Min | Max | Default | Description |
|---|---|---|---|---|---|
| `baseconfig_poll_interval_sec` | Integer | `1` | | `10` | <ul><li>Delay in seconds before the main loop loads the base config and updates the plugin configurations</li><li>If a worker loop is running at the moment, the delay is applied after the worker loops are done</li><li>If `start_now` is set to `True` in the Base Configuration or by the API call, this flag will also be checked with this delay (see below)</li></ul> |
| `poll_start_hour` | Integer | `0` | `23` | `0` | <ul><li>Specify a hour between `0` and `23`</li><li>The next time where the objects are searched and updated is the next possible time when this full hour is reached</li></ul> |
| `poll_every_days` | Integer | `0` | | `0` | <ul><li>The next update time would be starting at the next day</li><li>This value can be increased to wait several days before starting the update process again</li><li>A value of `0` means the worker loop runs every day</li></ul> |
| `search_chunk_size` | Integer | `1` | `1000` | `50` | (Maximum) number of objects that are searched in one batch |
| `webhook_hmac` | String (optional) | | | | <ul><li>HMAC secret to authenticate API calls. If this value is not set, the plugin API can not be used</li><li>This value must also be used for webhooks to start the update process</li></ul> |

## Logging levels

The plugin has different log levels, the top level debugger is `pf.plugin.base.auto_keyworder`.

For detailled logging, the log level for the following logger can be set to `debug`:

- `pf.plugin.base.auto_keyworder`

The debug level is very verbose and prints the parsed base configurations, and other often repeated information to the console. Only activate this log level if necessary.

## Example Configuration in `easydb-server.yml`

```yaml
auto_keyworder:
  baseconfig_poll_interval_sec: 30
  poll_start_hour: 0
  poll_every_days: 3
  search_chunk_size: 500
  webhook_hmac: '894wf76w93487t3f9'

logging:
  pf.plugin.base.auto_keyworder: debug
```
