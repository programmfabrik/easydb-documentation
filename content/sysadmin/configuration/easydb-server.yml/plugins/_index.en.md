---
title: "Plugins"
menu:
  main:
    name: "Plugins"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins"
    weight: -998
    parent: "sysadmin/configuration/easydb-server.yml"
---

# Plugins

The easydb provides a number of plugins already, the so-called base plugins.

Apart from this, you may develop plugins yourself or install plugins installed by others. We describe the installation of such a plugin in the [Extension-Plugin](#extension-plugin).

Plugins found on https://github.com/programmfabrik support both ways. You may activate them as a base-plugins or install them as an extension-plugins. The latter is much more complicated.

## List of active plugins

Which plugins are currently active can be seen in the web front end of the easydb, on the far left via the "i"(nfo) button and then with its subpoint "About".

---

## Base plugin

### Available base plugins

| Pluginname | Source code | Description |
|:-----------|-------------|---|
| [ easydb-auto-keyworder-plugin](auto-keyworder) | | Automatically fill objects with information from external AI services for image recognition | |
| [ easydb-presentation-pptx-plugin](presentation-pptx) | | Allows to create powerpoint presentations in easydb5 |
| [ easydb-server-plugin](server) | | Allows you to see server statistics  in easydb5 frontend |
| [ easydb-eventmanager-plugin](eventmanager) | | Allows you to see all events in easydb5 frontend |
| [ easydb-hotfolder-plugin](hotfolder) | | Allows you to configure the hotfolder |
| [ easydb-export-transport-ftp-plugin](export-transport-ftp) | | Allows you to export your files via ftp |
| [ easydb-remote-plugin](remote) | | Allows you to connect your frontend to another easydb5 |
| [ easydb-connector-plugin](connector) | | Allows you to connect your easydb5 to other instances |
| [ easydb-basemigration-plugin](basemigration) | | |
| [ easydb-oai-plugin](oai) | | |
| [ easydb-detail-map-plugin](detail-map) | | |
| [ easydb-editor-tagfilter-defaults-plugin](tagfilter) | | |
| [ easydb-easydb4migration-plugin](easydb4migration) | | |
| [ easydb-sso-plugin](sso/) | | Allow the easydb to communicate with [Kerberos](sso/kerberos) or [Shibboleth](sso/shibboleth) |
| [ easydb-ldap-plugin](ldap/) | | Allow the easydb to communicate with the [LDAP](ldap/) |
| [ easydb-webhook-plugin](webhook) | | |
| [ easydb-wordpress-plugin](wordpress) | | |
| [ easydb-typo3-plugin](typo3) | | |
| [ easydb-drupal-plugin](drupal) | | |
| [ easydb-falconio-plugin](falconio) | |
| [ easydb-barcode-plugin](barcode) | | |
| [ easydb-hijri-gregorian-converter-plugin](hijri-gregorian-converter) | [https://github.com/programmfabrik/easydb-hijri-gregorian-converter-plugin](https://github.com/programmfabrik/easydb-hijri-gregorian-converter-plugin) |
| [ easydb-custom-data-type-dante-plugin](custom-data-type/dante) | [https://github.com/programmfabrik/easydb-custom-data-type-dante](https://github.com/programmfabrik/easydb-custom-data-type-dante) | References to entities of the DANTE-Vokabulary-Server (https://dante.gbv.de) |
| [ easydb-custom-data-type-gazetteer](custom-data-type/gazetteer) | [https://github.com/programmfabrik/easydb-custom-data-type-gazetteer](https://github.com/programmfabrik/easydb-custom-data-type-gazetteer) |  |
| [ easydb-custom-data-type-geonames](custom-data-type/geonames) | [https://github.com/programmfabrik/easydb-custom-data-type-geonames](https://github.com/programmfabrik/easydb-custom-data-type-geonames) | References to entities of the GeoNames geographical database |
| [ easydb-custom-data-type-georef](custom-data-type/georef) | [https://github.com/programmfabrik/easydb-custom-data-type-georef](https://github.com/programmfabrik/easydb-custom-data-type-georef) | References to geoJSON-Objects |
| [ easydb-custom-data-type-getty](custom-data-type/getty) | [https://github.com/programmfabrik/easydb-custom-data-type-getty](https://github.com/programmfabrik/easydb-custom-data-type-getty) | References to entities of the Getty Vocabularys. |
| [ easydb-custom-data-type-gn250](custom-data-type/gn250) | [https://github.com/programmfabrik/easydb-custom-data-type-gn250](https://github.com/programmfabrik/easydb-custom-data-type-gn250) | References to entities of the gn250-Set of Bundesamt für Kartographie |
| [ easydb-custom-data-type-gnd](custom-data-type/gnd) | [https://github.com/programmfabrik/easydb-custom-data-type-gnd](https://github.com/programmfabrik/easydb-custom-data-type-gnd) | References to entities of the Integrated Authority File (GND) |
| [ easydb-custom-data-type-gvk](custom-data-type/gvk) | [https://github.com/programmfabrik/easydb-custom-data-type-gvk](https://github.com/programmfabrik/easydb-custom-data-type-gvk) | References to entities of the Gemeinsamer Verbundkatalog (GVK) |
| [ easydb-custom-data-type-goobi](custom-data-type/goobi) | [https://github.com/programmfabrik/easydb-custom-data-type-goobi](https://github.com/programmfabrik/easydb-custom-data-type-goobi) | |
| [ easydb-custom-data-type-iconclass](custom-data-type/iconclass) | [https://github.com/programmfabrik/easydb-custom-data-type-iconclass](https://github.com/programmfabrik/easydb-custom-data-type-iconclass) | |
| [easydb-custom-data-type-html-editor](custom-data-type/html-editor) | [https://github.com/programmfabrik/easydb-custom-data-type-html-editor](https://github.com/programmfabrik/easydb-custom-data-type-html-editor) |  |
| [ easydb-custom-data-type-link](custom-data-type/link) | [https://github.com/programmfabrik/easydb-custom-data-type-link](https://github.com/programmfabrik/easydb-custom-data-type-link) | Allows you to configure fields as web-link |
| [ easydb-custom-data-type-location](custom-data-type/location) | [https://github.com/programmfabrik/easydb-custom-data-type-location](https://github.com/programmfabrik/easydb-custom-data-type-location) | Allows you to configure gps data in easydb5 |
| [ easydb-custom-data-type-nomisma](custom-data-type/nomisma) | [https://github.com/programmfabrik/easydb-custom-data-type-nomisma](https://github.com/programmfabrik/easydb-custom-data-type-nomisma) | |
| [ easydb-custom-data-type-tnadiscovery](custom-data-type/tnadiscovery) | [https://github.com/programmfabrik/easydb-custom-data-type-tnadiscovery](https://github.com/programmfabrik/easydb-custom-data-type-tnadiscovery) | References to entities of the Nationalarchives-Discovery-System |

Base plugins have already been installed with the easydb installation and must therefore only be activated.

Compare the following lines to the configuration file `config/easydb-server.yml` below the [data store](/en/sysadmin/installationi#mount) (defined during the installation). Add the missing lines.

```yaml
plugins:
  enabled+:
    - base.detail-map
    - base.eventmanager
```

... for e.g. The two plugins `easydb-detail-map-plugin` and `easydb-eventmanager-plugin`.

After that, you should restart the easydb.

To explicitly deactivate a plugin, use the suffix `-` for the list of enabled plugins:

```yaml
plugins:
  enabled+:
    - base.detail-map
  enabled-:
    - base.eventmanager
```

The `easydb-eventmanager-plugin` will be disabled although it was enabled by default.

---

## Extension plugin

### Available extension plugins

| Pluginname | Plugin website | Description |
|:-----------|----------------|-------------|
| example-plugin | [example-plugin](https://github.com/programmfabrik/easydb-plugin-examples/tree/a85c57c4d80113656c9a62259e37c698600e98f0) | Just for testing purposes |


Extension plugins are typically made by developers outside of Programmfabrik.

Thus the installation procedure can be different than shown here. In that case please contact the plugin developer for more information.

For the plugin shown here (example-plugin) and others on github.com there is a so called issue tracker for each plugin: https://github.com/programmfabrik/easydb-plugin-examples/issues

Installation example:

Commands to be executed in the data store directory ([defined during installation](/en/sysadmin/installationi#mount)):

```bash
mkdir config/plugin
cd config/plugin
git clone https://github.com/programmfabrik/easydb-custom-data-type-geonames easydb-custom-data-type-geonames
cd easydb-custom-data-type-geonames
git submodule init
git submodule update
make
```

If "make" asks for the programm "coffee" then please install the newest version which starts with "1." e.g. version 1.12.7 during the time of writing this. On a Debian 10 server, these commands have been tested to achieve that:

```bash
apt-get install npm
npm install -g coffee-script@1
cd /usr/bin
ln -s nodejs node  # this may not be needed
```

After that you should return to the directory where you executed "make" and execute it again.

Now the plugin is ready but the easydb does not yet know of the plugin. To change that, compare the following lines to the configuration file `config/easydb-server.yml` below the [data store](/en/sysadmin/installationi#mount). Add the missing lines:

```yaml
extension:
  plugins:
    - name: easydb-plugin-example
      file: plugin/example-plugin/example-plugin.config.yml
plugins:
  enabled+:
    - extension.easydb-plugin-example
```

In detail, look for the name of the yml-file in the git clone directory.

Also look for the name of the plugin in that yml-file. Place the names in the configuration. For clarification, here another example with capital letters as emphasis to show where to replace strings:

```yaml
extension:
  plugins:
    - name: NAME_FROM_YML_FILE
      file: plugin/CLONE_DIRECTORY/NAME_OF_THE_YML_FILE
plugins:
  enabled+:
    - extension.NAME_FROM_YML_FILE
```

Lastly, you should restart the easydb to load the new plugin:

```bash
docker restart easydb-server easydb-webfrontend
```

---

## Solution plugin

If we are developing a plug-in for you, we can deliver it as a solution plug-in.

In this case, we also create documentation for the plugin. You will get the documentation from us.

---

## CMS Plugins

### Wordpress Plugin {#wordpressplugin}

[Wordpress Plugin](/en/webfrontend/datamanagement/features/plugins) to easily transport media files to Wordpress CMS.

Currently, this plugin supports the creation of new media as well as the updating of related metadata. When a new record is created in easydb, a new record is also created in Wordpress. There is no support for deleting media.

#### Prerequisites

* Support for Wordpress 4.7 and higher
* For the use in the frontend, the JSON rest API must be activated (is default) and authentication must be set up.

#### Setup (Wordpress)

* easydb supports **JSON Basic Authentication** and **WP REST API - OAuth 1.0a Server**.
  * Install plugin(s) for authentication
  * Enable plugin(s) for authentication
  * Setup a user for oauth plugin, <br> Callback URL: **http:// *easydb-server* /api/v1/plugin/base/easydb-wordpress-plugin/oauth1**<br> *(Log into WP > Main Menu > User > Application > enter a name and callback URL here. Save and keep the generated client key and client secret ready for the setup in the basic configuration.)*

#### Install Plugin in easydb

* Make sure the plugin is correctly installed (paths are relative to the .yml)

Add the following lines to your easydb-server.yml:

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

### Falcon.io Plugin {#falconio}

Plugin to easily transport media files to Falcon.io CMS. Currently this supports sending selected media to Falcon.io. Updating is not supported, new files are created in Falcon.io instead.

#### Setup (Falcon.io)

* Must have a registered Falcon.io account
* Register minimum one **Channel** so the Content Pool becomes an accessible feature
* Generate an API_Key for easydb under Settings->Integration & APIs

#### Install Plugin in easydb

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
