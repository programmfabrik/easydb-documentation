---
menu:
  main:
    name: "5.111 (January 2023)"
    identifier: "5.111"
    parent: "releases5110"
    weight: -611
---


> This version **does not require** a new index build


# Version 5.111.1

*Released on 01.02.2023*

# Webfrontend

## Fixed

* **metadata mapping**: custom input fields are l10n-aware now

# Version 5.111.0

*Released on 18.01.2023*

# Webfrontend

## New

* Added a new button for show the parents of a record in the main search for hierarchycal and polyhierarchical objects
* **Mask settings**:
  * Added new tool tips to mask IO settings
  * The path of hierarchy linked objects is shown in text mode, this can be controlled in the mask custom settings of the linked objects fields
  * It is possible to select a record to preview mask settings in mask configuration window

## Improved

* **PDF Creator**:
  * Added new buttons for move up and down nodes in the pdf-creator node-list
  * Added more depths for the fields node in pdf-creator, now you can select fields up to 3 levels of depth
  * Fixed an error in pdf-creator where the preview was not rendered after modifying a field node
* **Search**: Enhanced how the main search is rendered to lower the calls for render and improve performance
* The calendar button is disabled when a B.C. date is inserted in the date field
* Changed the color of links in pool tooltips so they have more contrast

## Fixed

* Fixed an error in the filter for linked object on objecctypes when old datamodel fields was used for create a filter
* Fixed several errors in the Tag Management tool in main search
* Fixed replacements for download messages
* Fixed a problem with single-value fields marked as List in metadata-mapping configuration
* Fixed the behaviour of the close button in fullscreen detail mode
* Fixed an error with suggestion and connector fields
* Fixed the preview placeholder of `processing` records in the main search
  * Also the size info of the image won't be shown in the assetbrowser when the image is still being processed


# Server

## New

* **Plugins**: Translations in Finnish and Swedish in different plugins

## Fixed

* **Datamodel**: Fixed possible errors when activating multilinguage fields
* **XML Metadata Mapping**: Fixed bug when importing/exporting data to lists




# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.111.0         sha256:ef7e8117c83253351f51a408ef0707a306db5779a5f3bfeca7fd63b6abb4aac7
docker.easydb.de/pf/eas:5.111.0            sha256:2f9396e47c51545f3ba0b05b3addf9ff866b1c218cd2d7e255c1dc3ecefcca0f
docker.easydb.de/pf/elasticsearch:5.111.0  sha256:59959716bbe807afe86fb0c58d46599c87d77aaa130b0a489b064b1156cfdab8
docker.easydb.de/pf/fylr:5.111.0           sha256:2b471ace6ae7df7f79e76c32f841aa9eaba090da70ae187124905b0e3ddaf2da
docker.easydb.de/pf/postgresql-11:5.111.0  sha256:ae69be481c062daf7dfb37578ff006b0ba8ef9a3c56dfdff4984711ce3c59b16
docker.easydb.de/pf/postgresql-14:5.111.0  sha256:ca05b4ee6affd68d680fbbed9c7a28368eb26ec5b637d814cd52a17d9c9885c6
docker.easydb.de/pf/server-base:5.111.1    sha256:9d48e0a76a159d5a99342f1f01ffd5beec480a0fadbb0a613b161cf1aeb3ed71
docker.easydb.de/pf/webfrontend:5.111.1    sha256:b99f347d4c20951bb1250b72cb8ada8952b31fccb32e26ee12aad542cf9abcc2
```

