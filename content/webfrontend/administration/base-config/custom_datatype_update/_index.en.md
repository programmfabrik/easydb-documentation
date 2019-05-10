---
title: "Custom Datatype Update"
menu:
  main:
    name: "Custom Datatype Update"
    identifier: "webfrontend/administration/base-config/custom-datatype-update"
    parent: "webfrontend/administration/base-config"
---

# Update settings for Custom Data Types

For Custom Data Types that support automatic updates, you can choose the intervals for the update cycles.

All objects that have a field with this Custom Data, will be updated and reindexed. Please note that this might take a long time.

| Setting | Explenation | Range | Default |
| --- | --- | --- | --- |
| Enable automatic updates | Enable or disable the custom data type updater for all custom types | `true` / `false` | `false` |
| Update hour | Update all Custom Data Types at this full hour per day | `0..23` | `0` (0 am) |
| Break between updates in days | After an update of custom data types, wait this many days before the next run | `> 0` | `1` (run every day) |

Custom Data Type Plugins with base configuration settings can add these settings here.