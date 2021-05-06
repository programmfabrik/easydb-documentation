---
menu:
  main:
    name: "5.76 (November 2020)"
    identifier: "5.76"
    parent: "releases579"
    weight: -576
---

> This release brings the announced mandatory **application of Postgres 11**. More information can be found in the section **[PostgreSQL 11](../5.73#postgres-11)**.
>
> No re-index required.

# Version 5.76.2

*Published on 26.11.2020*

## Webfrontend

*Fixed*

- **Data model**: Memory problem when switching in the mask editor fixed.
- **Search**: Fixed display of linked objects in table view
- **Search**: Incorrect print preview was fixed.
- **Search**: Indicator for image series was fixed.
- **Search**: Cases where the lasso selected invisible objects have been fixed.
- **Search**: Visibility logic corrections for Standard Info.

# Version 5.76.1

*Published on 23.11.2020*

## Webfrontend

*Fixed*

- **Search**: Fixed display of standard info in standard and text view The option is now activated for all users and must be deactivated if necessary.
- **Detail**: Display of the menu for reverse linked objects has been restored.
- **CSV importer**: Saving at certain Tag constellations was fixed.

# Version 5.76.0

*Released on 18.11.2010*

## Web frontend

*New*

* **Detail**: In debug mode, objects can be loaded as JSON directly by clicking (next to string fields).

*Enhanced*

* **Design** of search, detail and editor was unified in the output from the standard info.
* **Group manager**: output of the group type in the form.
* **Basic configuration**: the output of the Server-Config was removed.
* **Admin area**: All areas now have individual headings for the respective parts of the display.
* **Filter**: Fields which are right managed are not shown anymore (tag filters are ignored) .
* **Plugin Editor-Tagfilter-Defaults**: Filling read-only fields is now supported.

*Removed*

* **Autocompletion** no longer shows duplicates for linked objects
* **Data model**: Preview in the editor of the current model was fixed.
* **Pool selection**: For some users the sorting of subpools did not work correctly.
* Detail: Plugins can no longer cover the Info Bar.
* **Detail**: Display of versions with GPS coordinates in extended information was fixed.
* **Detail/Editor/Text**: Hidden tags are no longer displayed if the mask does not allow it.
* **Plugin Connector**: Multiple download, pool filter, interaction with plugin auto keyworder, display of versions has been fixed for affected cases.

## Server

*Enhanced*

* **Postgres 11** is required, otherwise easydb will not start.
* Data model error messages were improved.

*Removed*

* **Collections**: Deleting hierarchical objects was not possible in certain constellations.

# Checksums
Here are the checksums of our docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:f24a68195f7215c5fba3ab3d0dca910ead74cc6659a5b2b3cdf8fe912d8d10e2
docker.easydb.de/pf/eas                  sha256:1143ce8cfbdff9ae602df7163150b34833637ae41600ebef5e164adc000e9202
docker.easydb.de/pf/elasticsearch        sha256:daf032af6c43c8b7a63797525478ad31d04a7e57924324089fd990c1b1de98d9
docker.easydb.de/pf/fylr                 sha256:e6a341d8c92f23027241e26f71ed811f65fd8176a133da0c92010405f9e8e13f
docker.easydb.de/pf/postgresql-11        sha256:188046e6935796f66037a9a9f6788ba7962160664dc5bcdcfdca4d7fe9ca04e7
docker.easydb.de/pf/postgresql           sha256:909a680aea9d5475570e089ca8e8cc8ebdc0c4e9c76c28789d1936795ed77715
docker.easydb.de/pf/server-base          sha256:6bb1cf810ddac352995534b63703a225645c369a73014ad90eabc2fc65fab955
docker.easydb.de/pf/webfrontend          sha256:94e008bed7695b27f17f9ab57565653eed808bd0c63681d96099b0ee327188a2
```

*Translated with www.DeepL.com/Translator*

