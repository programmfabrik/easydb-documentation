---
menu:
  main:
    name: "5.44"
    identifier: "5.44"
    parent: "releases550"
    weight: -544
---

> * **Version 5.44.1** requires a re-index, schedule the system downtime for the update.

> * Probably all installations require minor [configuration adjustments](#configuration-changes). This was necessary to enable new features. 

# Version 5.44.1

*Published on 13.12.2018*

* Index is recreated to make the search improvements active.
* Possible error when deleting events in frontend fixed.

# Version 5.44.0

*Published on 12.12.2018*

### Web frontend

*New*

* **Tags** can now be displayed in the **filter display**.
* Search entries can be changed afterwards with space bar or return.
* Search entries in double quotation marks no longer perform a wildcard search, the wildcard search can be used without quotation marks. A new feature is that **?** (single character) works in addition to **\*** (multiple characters).
* **System-Object-ID** can be displayed in the search result (display setting, this is the ID in the detail display with the **#**)
* The **order** of System Object ID, Standard + Tags columns in Table View can be set by the user.
* Support for **Editor plugins** to verify input.
* Support for **Script Runner Plugins**. A first plugin allows downloading as CSV arbitrarily filtered asset metadata from the search result.
* Field filters for object types now also work for the system fields **Owner** and **Parent**.
* In the editor, **additional information** can be displayed if the form cannot be saved.

*Improved*

* JSON-Importer: log output has been improved
* Improved keyboard input for selections and menus.
* The text in the title of the easydb is displayed in white if you have defined a dark background color.

*Resolved*

* Search entries with double quotation marks within double quotation marks are processed correctly.
* PDF display repaired for cases where server could not generate single page previews.
* Multi-language display updated correctly after changing language settings.
* Fixed filter display of multiple fields of mask type **nested**.

### Server, plugins and containers

*New*

* Configurable synonym mapping for full-text search.
* Saving of system fields in column filters enabled.
* common Docker container configuration file `easydb5-master.yml` can be replaced or extended by single configuration files.
* **Webhook plugin**

*Improved*

* Characters **of Asian scripts** (CJK, Hiragana, Katakana, Hangul) are treated as independent tokens in the full text search.
* Pool filter optimized for searches with `system.root` users.

*Resolved*

* Fixed a bug when searching for Unicode characters of level 1 and up.


# Configuration changes

The examples shown all refer to the already existing `easydb5-master.yml`.

## Email configuration

If the block `common.email` is used, it must be duplicated as `easydb-server.smtp` and `eas.smtp`, but without creating e.g. a second easydb-server line. The old block `common` can be removed after the update. See also [E-Mail configuration](/en/sysadmin/konfiguration/recipes/email).

### old

````yaml
common:
  email:
    server: 172.18.0.1
    hostname: easy.example.com
    from-address: noreply@example.com
````

### new

````yaml
easydb-server:
  smtp:
    server: 172.18.0.1
    hostname: easy.example.com
    from-address: noreply@example.com
eas:
  smtp:
    server: 172.18.0.1
    hostname: easy.example.com
    from-address: noreply@example.com
````
## Host configuration

This change should only be necessary in exceptional cases if the installation deviates from the standard and, for example, is distributed over several machines or several instances run on one machine. In case `docker-hostname` occurs in `easydb5-master.yml` the configuration should be extended. This will turn `easydb-server.docker-hostname` into `easydb-server.hostnames.server`, `eas.docker-hostname` into `easydb-server.hostnames.eas`, and `fylr.docker-hostname` into `easydb-server.hostnames.fylr`. The previous configuration variables should be kept.

### old

````yml
eas:
  docker-hostname: custom-eas
easydb-server:
   docker-hostname: custom-server
fylr:
   docker-hostname: custom-fylr
````
### new

````yaml
eas:
  docker-hostname: custom-eas
easydb-server:
  docker-hostname: custom-server
  hostnames:
    eas: custom-eas
    server: custom server
    fylr: custom-fylr
fylr:
  docker-hostname: custom-fylr
````

*Translated with [www.DeepL.com/Translator](https://www.DeepL.com/Translator)*





