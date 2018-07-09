# Plugin configuration

The easydb 5 already contains several plugins, which are marked with "base" in the configuration.

These plugins only need to be activated via the central configuration file `easydb5-master.yml`. Its location has been set during the [installation](/sysadmin/installation/installation.html#mount).

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

Die easydb 5 bringt bereits mehrere Plugins mit, diese werden in der Konfiguration mit "base" gekennzeichnet.

Viele dieser Plugins sind standardmäßig aktiviert.

Änderungen können in der zentralen Konfigurationsdatei `easydb5-master.yml` vorgenommen werden, deren Speicherort bei der [Installation](/sysadmin/installation/installation.html#anpassungen) festgelegt wurde.

In diesem Beispiel wird das Plugin "custom-data-type-link" als aktiv konfiguriert:

~~~~
easydb-server:
  plugins:
    enabled+:
      - base.custom-data-type-link
~~~~

Ebenso ist es möglich, ein standardmäßig aktiviertes Plugin wieder zu deaktivieren:

~~~~
easydb-server:
  plugins:
    enabled-:
      - base.custom-data-type-link
~~~~

Nach einem Neustart findet sich das Plugin in der Liste "Plugins" auf der Seite "Versionsinformation".

Der Klickweg dorthin ist: `i`-Knopf (ganz links in der Leiste) -> `Über`.

# Extension Plugins

Extensions-Plugins müssen installiert werden und aktiviert werden.

Dies ist beschrieben unter [Plugin-Installation](/sysadmin/plugin/plugin.html).
