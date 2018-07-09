# Plugin configuration

The easydb 5 already contains several plugins, which are marked with "base" in the configuration.

Many of these plugins are enabled by default.

Changes can be made in the central configuration file `easydb5-master.yml`. Its location has been set during the [installation](/sysadmin/installation/installation.html#mount).

In this example, the custom-data-type-link plug-in is configured as active:

~~~~
  plugins:
    enabled+:
      - base.custom-data-type-link
~~~~

In the same way it is also possible to deactivate a plugin that is activated by default:

~~~~
easydb-server:
  plugins:
    enabled-:
      - base.custom-data-type-link
~~~~


After a reboot, the plugin can be found in the list "Plugins" on the page "Version Information".

You get there via the `i` button (far left in the bar) and then ->` About`.


# Extension Plugins

Before using Extension Plugins they need to be installed and activated.

Find more information in the chapter [Plugin-Installation](/sysadmin/plugin/plugin.html).
