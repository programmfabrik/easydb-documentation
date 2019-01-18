---
title: "66 - Connector"
menu:
  main:
    name: "Connector"
    identifier: "webfrontend/administration/base-config/connector"
    parent: "webfrontend/administration/base-config"
---
# Connector {#connectorplugin}

Der Connector ermöglicht es Ihnen andere easydb's in Ihre Suche zu integrieren, sodass Ihre Nutzer ohne Anmeldung beim Connector-Partner in deren freigegebenen Beständen recherchieren können.   

Ein Tutorial zur Einrichtung von Connectoren finden Sie [hier](../../../../tutorials/connector).

> Sollten Sie diesen Menüpunkt nicht sehen, so müssen Sie das Connector-Plugin installieren.



| Bereich                                | Einstellung                      | Erläuterung                                                  |
| -------------------------------------- | -------------------------------- | ------------------------------------------------------------ |
| Connector                              | Connector für Benutzer aktiviert | Aktivierung / Deaktivierung der Connector-Funktion für alle Nutzer die auf die Recherche zugreifen können. |
|                                        | easydb-Instanzen für Connector   | Liste an hinterlegten Connector-Partnern                     |
|                                        | Aktiviert                        | Aktivierung / Deaktivierung des Connector-Partners           |
|                                        | Name                             | Name des Connector-Partners. Wird für den Benutzer im Auswahl-Menü aktivierter Connector-Partner angezeigt. |
|                                        | URL                              | URL des Connector-Partners                                   |
|                                        | Login                            | Login des Connector-Partners                                 |
|                                        | Passwort                         | Passwort des Connector-Partners                              |
| FYLR-Konfiguration                     |                                  |                                                              |
|                                        | URL                              | Tragen Sie hier http://ihre-easydb-url/fylr/zip ein, damit ein massenhafter Download von Dateien des Connector-Verbunds als ZIP durchgeführt kann. |
| Daten für migrierte easydb 4 Instanzen |                                  | Die nachfolgenden Einstellungen sind nur bei Kunden notwendig, die von easydb 4 auf easydb 5 umgestiegen sind. |
|                                        | easydb-ID der 4                  | Angabe der easydb-ID der easydb 4 (zu finden im ezadmin).    |
|                                        | Tabellen-ID in easydb 4          | Angabe der ID der Haupttabelle in easydb 4 (häufig "1").     |
|                                        | Tabellenname in easydb 4         | Angabe des Haupttabellenamens in easydb 4 (häufig "bilder" oder "Bilder"). |
|                                        | Objekttyp in easydb 5            | Angabe des internen Namens des Hauptobjekttyps in easydb 5 (häufig "bilder" oder "objekte"). |
|                                        | Referenzspalte in easydb 5       | Angabe der Spalte mit den migrierten easydb 4 IDs (häufig "easydb4_reference"). |