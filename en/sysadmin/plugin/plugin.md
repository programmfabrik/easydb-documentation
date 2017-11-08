# Install a plugin

The easydb provides a number of plugins already, the so-called base plugins.

Apart from this, you can use plugins found on Https://github.com/programfabrik or develop it yourself. We describe the installation of such a plugin in the [Extension-Plugin](#extension-plugin).

## List of active plugins

Which plugins are currently active can be seen in the web front end of the easydb, on the far left via the "i"(nfo) button and then with its subpoint "About".

---

# Base plugin

Base plugins have already been installed with the easydb installation and must therefore only be activated.

Compare the following lines to the configuration file `config/easydb5-master.yml` whose [location](./sysadmin/installation/installation.html#mount) was defined during the installation. Add the missing lines.

    easydb-server:
      plugins:
        enabled+:
          - base.custom-data-type-link
          - base.custom-data-type-gnd

... for e.g. The two plugins custom-data-type-link and custom-data-type-gnd.

After that, you should restart the easydb.

---

# Extension plugin

The example easydb-custom-data-type-geonames:

Compare the following lines to the configuration file `config/easydb5-master.yml` whose [location](./sysadmin/installation/installation.html#mount) was defined during the installation. Add the missing lines.

    easydb-server:
      extension:
        plugins:
          - name: easydb-custom-data-type-geonames
            file: plugin/easydb-custom-data-type-gnd/CustomDataTypeGeonames.config.yml
      plugins:
        enabled+:
          - extension.easydb-custom-data-type-geonames

Commands for installation: (to be executed in the [data store](./sysadmin/installation_data_determine/installation_data_determine.html) directory, whose location was defined during the installation)

    mkdir config/plugin
    cd config/plugin
    git clone https://github.com/programmfabrik/easydb-custom-data-type-geonames easydb-custom-data-type-geonames
    cd easydb-custom-data-type-geonames
    git submodule init
    git submodule update
    make

Lastly, you should restart the easydb.

## In case of problems

Please note that problems with extension plugins are to be answered by the developer of the plugin. Therefore, please direct your questions to the so-called issue tracker of the plug-in. For example, easydb-custom-data-type-geonames would be: https://github.com/programmfabrik/easydb-custom-data-type-geonames/issues

---

# Solution plugin

If we are developing a plug-in for you, we can deliver it as a solution plug-in.

In this case, we also create documentation that is tailored to the plugin. You will get the link to this documentation from us.
