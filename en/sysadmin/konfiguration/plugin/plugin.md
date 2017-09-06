# Plugin configuration

The easydb5 already contains several plugins, these are marked "base" in the configuration.

These plugins only need to be activated, in the central configuration file `easydb5-master.yml` whose location has been set during the [Installation](/sysadmin/installation/installation.md#anpassungen).

In this example, the custom-data-type-link plug-in is configured as active:

~~~~
  plugins:
    enabled+:
      - base.custom-data-type-link

~~~~


After a reboot, the plugin can be found in the list "Plugins" on the page "Version Information".

The click path there is: `i` button (far left in the bar) ->` About`.