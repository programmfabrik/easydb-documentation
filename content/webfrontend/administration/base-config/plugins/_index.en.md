---
title: "159 - Remote Plugins"
menu:
  main:
    name: "Remote Plugins"
    identifier: "webfrontend/administration/base-config/plugins"
    parent: "webfrontend/administration/base-config"
---
# Remote Plugins

This function is added to the basic configuration via a plugin. This feature allows you to add your own plugin files for the frontend to easydb, if the plugin do not require a server component.

* The plugin is available via [Github](https://github.com/programmfabrik/easydb-remote-plugin).
* The plugin is configured in the yml on the server, see [Plugin Installation](/en/sysadmin/installation/plugin/).

After successful installation the plugin appears in the selection of the basic configuration.

> The Remote Plugin is shipped with the standard easydb installation and does not need to be installed and configured separately.

![](remote_plugin.jpg)!

* You can enter a URL for a JS file and a CSS file in each of the input fields.
* It is possible to add several tuples.
