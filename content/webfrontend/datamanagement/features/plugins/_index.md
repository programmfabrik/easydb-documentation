---
title: "Plugins"
menu:
  main:
    name: "Plugins"
    identifier: "webfrontend/datamanagement/features/plugins"
    parent: "webfrontend/datamanagement/features"
---
# Plugins

Der Funktionsumfang der easydb kann über sog. Plugins erweitert werden. So lassen sich zum Beispiel externe Vokabulare einbinden, Inventarnummern generieren oder Content Management Systeme anbinden.

Plugins können nicht nur von Programmfabrik GmbH entwickelt werden, sondern mit entsprechendem Know-How auch in-house oder durch externe Partner. Weitere Informationen zur Entwicklung von Plugins können in der [technischen Dokumentation](/en/technical/plugins/) gefunden werden.

Viele Plugins die entweder durch Progrmmfabrik GmbH oder durch externe Partner entwickelt wurden, stehen als Open Source Plugins auf dem offiziellen [Github-Account der Programmfabrik](https://github.com/programmfabrik) zur Verfügung.

Darüber hinaus gibt es folgende kostenpflichtige Plugins:

- [Anbindung an die Content Management Systeme Wordpress, Typo3 & Drupal](cms)
- [Automatische Verschlagwortung mit externen KI-Diensten](autokeyworder)
- [PDF-Creator](../../../rightsmanagement/objecttypes/#pdf-creator)

Es wird unterschieden zwischen Frontend- und Server-Plugins:

|                         | Frontend | Server                                                    |
| ----------------------- | -------- | --------------------------------------------------------- |
| **Programmiersprachen** | <ul><li>CoffeeScript (konvertiert zu JavaScript)</li><li>CSS</li></ul> | <ul><li>Python 3</li><li>SQL</li></ul> |
| **Beispiele**           | <ul><li>[Einbindung externer Vokabulare](/en/technical/plugins/customdatatype/), wie z.B. GND, Getty Normdaten, Gazetteer</li><li>Zugriff auf Daten anderer easydb-Instanzen im [Connector-Verbund](/en/sysadmin/configuration/easydb-server.yml/plugins/connector/)</li><li>OpenStreetMap-Karte</li><li>Darstellung von Objektdaten als [Barcode](/en/technical/plugins/webfrontend/barcode/)</li><li>Erzeugen von [PDF-Dateien](/en/sysadmin/configuration/easydb-server.yml/plugins/pdf-creator/) mit Objektdaten</li></ul> | <ul><li>Automatische Generierung von Inventarnummern</li><li>[OAI](/en/sysadmin/configuration/easydb-server.yml/plugins/oai/) Schnittstelle zum Export von Objekten</li><li>Import von Dateien aus WebDAV-Ordnern per [Hotfolder](/en/sysadmin/configuration/easydb-server.yml/plugins/hotfolder/)</li><li>Formatierung von Exporten in beliebige andere Formate</li><li>[Herunterladen](/en/sysadmin/configuration/easydb-server.yml/plugins/presentation-pptx/) von Mappen-Präsentation im PowerPoint Format</li></ul> |
