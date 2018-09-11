---
title: "Plugins"
menu:
  main:
    name: "Plugins"
    identifier: "sysadmin/installation/plugin"
    parent: "sysadmin/installation"
    weight: 2
---
# Install a plugin

The easydb provides a number of plugins already, the so-called base plugins.

Apart from this, you may develop plugins yourself or install plugins installed by others. We describe the installation of such a plugin in the [Extension-Plugin](#extension-plugin).

Plugins found on https://github.com/programmfabrik support both ways. You may activate them as a base-plugins or install them as an extension-plugins. The latter is much more complicated. 

## List of active plugins

Which plugins are currently active can be seen in the web front end of the easydb, on the far left via the "i"(nfo) button and then with its subpoint "About".

---

# Base plugin

## Available base plugins

| Pluginname | Description |
|:-----------|-------------|
| [css](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/css) | Allows to modify easydb's css files. |
| [presentation-pptx](/en/sysadmin/konfiguration/easydb-server.yml/plugin/presentation-pptx) | Allows to create powerpoint presentations in easydb5 |
| [server](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/server) |  |
| [eventmanager](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/eventmanager) | Allows you to see all events in easydb5 frontend |
| [basemigration](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/basemigration) |  |
| [hotfolder](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/hotfolder) | Allows you to configure the [hotfolder](/en/sysadmin/konfiguration/hotfolder) |
| [export-transport-ftp](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/export-transport-ftp) | Allows you to export your files via ftp |
| [oai](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/oai) |  |
| [detail-map](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/detail-map) |  |
| [editor-tagfilter-defaults](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/editor-tagfilter-defaults) |  |
| [remote-plugin](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/remote-plugin) | Allows you to connect your frontend to another easydb5 |
| [easydb4migration](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/easydb4migration) |  |
| [connector](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/connector) | Allows you to connect your easydb5 to other instances |
| [a-frame](/en/sysadmin/konfiguration/easydb-server.yml/plugin/base/a-frame) |  |

Base plugins have already been installed with the easydb installation and must therefore only be activated.

Compare the following lines to the configuration file `config/easydb5-master.yml` whose [location](/en/sysadmin/installation) was defined during the installation. Add the missing lines.

```yaml
easydb-server:
  plugins:
    enabled+:
      - base.detail-map
      - base.eventmanager
```

... for e.g. The two plugins `detail-map` and `eventmanager`.

After that, you should restart the easydb.

---

# Extension plugin

## Available extension plugins

| Pluginname | Plugin website | Description |
|:-----------|----------------|-------------|
| [custom-data-type-dante](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/dante) | [dante](https://github.com/programmfabrik/easydb-custom-data-type-dante) | References to entities of the DANTE-Vokabulary-Server (https://dante.gbv.de) |
| [custom-data-type-gazetter](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/gazetter) |  | Work in progress |
| [custom-data-type-link](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/link) | [link](https://github.com/programmfabrik/easydb-custom-data-type-link) | Allows you to configure fields as web-link |
| [custom-data-type-getty](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/getty) | [getty](https://github.com/programmfabrik/easydb-custom-data-type-getty) | References to entities of the Getty Vocabularys. |
| [custom-data-type-gvk](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/gvk) | [gvk](https://github.com/programmfabrik/easydb-custom-data-type-gvk) | References to entities of the Gemeinsamer Verbundkatalog (GVK) |
| [custom-data-type-geonames](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/geonames) | [geonames](https://github.com/programmfabrik/easydb-custom-data-type-geonames) | References to entities of the GeoNames geographical database |
| [custom-data-type-gn250](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/gn250) | [gn250](https://github.com/programmfabrik/easydb-custom-data-type-gn250) | References to entities of the gn250-Set of Bundesamt für Kartographie |
| [custom-data-type-georef](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/georef) | [georef](https://github.com/programmfabrik/easydb-custom-data-type-georef) | References to geoJSON-Objects |
| [custom-data-type-gnd](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/gnd) | [gnd](https://github.com/programmfabrik/easydb-custom-data-type-gnd) | References to entities of the Integrated Authority File (GND) |
| [custom-data-type-tnadiscovery](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/tnadiscovery) | [tnadiscovery](https://github.com/programmfabrik/easydb-custom-data-type-tnadiscovery) | References to entities of the Nationalarchives-Discovery-System |
| [custom-data-type-location](/en/sysadmin/konfiguration/easydb-server.yml/plugin/custom-data-type/location) | | Allows you to configure gps data in easydb5 |

Extension plugins are typically made by developers outside the Programmfabrik. 

Thus the installation procedure can be different than shown here. In that case please contact the plugin developer for more information.

For the plugin shown here (easydb-custom-data-type-geonames) and others on github.com there is a so called issue tracker for each plugin: https://github.com/programmfabrik/easydb-custom-data-type-geonames/issues

Installation example:

Compare the following lines to the configuration file `config/easydb5-master.yml` whose [location](/en/sysadmin/installation) was defined during the installation. Add the missing lines.

```yaml
easydb-server:
  extension:
    plugins:
      - name: easydb-custom-data-type-geonames
        file: plugin/easydb-custom-data-type-geonames/CustomDataTypeGeonames.config.yml
    plugins:
      enabled+:
        - extension.easydb-custom-data-type-geonames
```

Commands for installation: (to be executed in the [data store](/en/sysadmin/installation) directory, whose location was defined during the installation)

```bash
mkdir config/plugin
cd config/plugin
git clone https://github.com/programmfabrik/easydb-custom-data-type-geonames easydb-custom-data-type-geonames
cd easydb-custom-data-type-geonames
git submodule init
git submodule update
make
```

If "make" asks for the prgramm "coffee" than please install the version 1.10. One way on a debian server is to install it like this:

```bash
apt-get install npm
npm install -g coffee-script@1.10
cd /usr/bin
ln -s nodejs node
```

After that you should return to the directory where you executed "make" and execute it again.

Lastly, you should restart the easydb to load the new plugin.


---

# Solution plugin

If we are developing a plug-in for you, we can deliver it as a solution plug-in.

In this case, we also create documentation that is tailored to the plugin. You will get the link to this documentation from us.

---

# CMS Plugins

## Wordpress Plugin {#wordpressplugin}

[Wordpress Plugin](/en/webfrontend/datamanagement/features/plugins) to easily transport media files to Wordpress CMS. 

Currently, this plugin supports the creation of new media as well as the updating of related metadata. When a new record is created in easydb, a new record is also created in Wordpress. There is no support for deleting media.

### Prerequisites

* Support for Wordpress 4.7 and higher
* For the use in the frontend, the JSON rest API must be activated (is default) and authentication must be set up.

### Setup (Wordpress)

* easydb supports **JSON Basic Authentication** and **WP REST API - OAuth 1.0a Server**.
  * Install plugin(s) for authentication
  * Enable plugin(s) for authentication
  * Setup a user for oauth plugin, <br> Callback URL: **http:// *easydb-server* /api/v1/plugin/base/easydb-wordpress-plugin/oauth1**<br> *(Log into WP > Main Menu > User > Application > enter a name and callback URL here. Save and keep the generated client key and client secret ready for the setup in the basic configuration.)*


## Install Plugin in easydb 

* Make sure the plugin is correctly installed (paths are relative to the .yml)

Add the following lines to your server.yml:

```yaml
base:
  plugins+:
    - name: wordpress
      file: easydb-wordpress-plugin/wordpress.yml

plugins:
  enabled+:
    - base.sso
    - base.simple-example
    - base.wordpress
```

Now go to [Basic Configuration](/en/webfrontend/administration/base-config/cms) to finish the WP configuration for easydb.

## Falcon.io Plugin {#falconio}

Plugin to easily transport media files to Falcon.io CMS. Currently this supports sending selected media to Falcon.io. Updating is not supported, new files are created in Falcon.io instead.

## Setup (Falcon.io)

* Must have a registered Falcon.io account 
* Register minimum one **Channel** so the Content Pool becomes an accessible feature
* Generate an API_Key for easydb under Settings->Integration & APIs

## Install Plugin in easydb

* Make sure the plugin is correctly installed (paths are relative to the .yml);

Add the following lines to your server.yml:

```yaml
base:
  plugins+:
    - name: falconio
      file: easydb-falconio-plugin/falconio.yml

plugins:
  enabled+:
    - base.falconio
```

