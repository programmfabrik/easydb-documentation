---
title: "Plugins"
menu:
  main:
    name: "Plugins"
    identifier: "webfrontend/datamanagement/features/plugins"
    parent: "webfrontend/datamanagement/features"
---
# Plugins

The functional range of easydb can be extended via so-called plugins. For example, external vocabularies can be integrated, inventory numbers can be generated or content management systems can be connected.

Plugins can be developed not only by Programmfabrik GmbH, but with appropriate know-how also in-house or by external partners. More information about the development of plugins can be found in the [technical documentation](/en/technical/plugins/).

Many plugins developed either by Progrmmfabrik GmbH or by external partners are available as open source plugins on the official [Github account of the program factory](https://github.com/programmfabrik).

In addition, there are the following paid plugins:

- [Connection to the content management systems Wordpress, Typo3 & Drupal](cms)
- [Automatic keywording with Cloudsight](autokeyworder)
- [PDF-Creator](../../../rightsmanagement/objecttypes/#pdf-creator)

A distinction is made between frontend and server plugins:

|                           | Frontend | Server                                                    |
| ------------------------- | -------- | --------------------------------------------------------- |
| **Programming languages** | <ul><li>CoffeeScript (converted to JavaScript)</li><li>CSS</li></ul> | <ul><li>Python 3</li><li>SQL</li></ul> |
| **Examples**              | <ul><li>[Integration of external vocabularies](/en/technical/plugins/customdatatype/), for example GND, Getty Normdaten, Gazetteer</li><li>Access to data of other easydb instances using the [Connector](/en/sysadmin/configuration/easydb-server.yml/plugins/connector/)</li><li>OpenStreetMap</li><li>Displaying of object data as [Barcode](/en/technical/plugins/webfrontend/barcode/)</li><li>Creation of [PDF files](/en/sysadmin/configuration/easydb-server.yml/plugins/pdf-creator/) with object data</li></ul> | <ul><li>Automatic generation of inventory numbers</li><li>[OAI](/en/sysadmin/configuration/easydb-server.yml/plugins/oai/) Interface for exporting objects</li><li>Import files from WebDAV folders via [Hotfolder](/en/sysadmin/configuration/easydb-server.yml/plugins/hotfolder/)</li><li>Formatting exports into any other formats</li><li>[Download](/en/sysadmin/configuration/easydb-server.yml/plugins/presentation-pptx/) of collection presentations in PowerPoint format</li></ul> |
