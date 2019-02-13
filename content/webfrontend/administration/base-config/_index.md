---
title: "63 - Basis-Konfiguration"
menu:
  main:
    name: "Basis-Konfiguration"
    identifier: "webfrontend/administration/base-config"
    parent: "webfrontend/administration"
---
# Basis-Konfiguration

In der Basis-Konfiguration werden globale Einstellungen für easydb vorgenommen. Über die Reiter können die Einstellungsbereiche aufgerufen werden.

![](basis_config_de_new.png)

Das Kapitel enthält Erläuterungen und zu den Themen:

* [Allgemein](general)
* [Anmelden](login)
* [Cloud-Dienstleister](cloud)
* [CMS](cms)
* [Editor](editor)
* [Erweiterte Funktionen](extended)
* [Events loggen](event_logging)
* [Export und OAI/PMH](export)
* [Hochladen](upload)
* [Remote Plugins](plugins)
* [Server-Config](server-config)

## Hochladen/Herunterladen der Basis-Konfiguration

In der Basis-Konfiguration besteht unten links über den <i class="fa fa-cog"></i>-Button die Möglichkeit die bestehenden Einstellungen der Basis-Konfiguartion herunterzuladen und eine Basis-Konfigurationsdatei hochzuladen (z.B. als Fallback).

![](basis_config_schema_de.jpg)

Der Download und Upload der Konfiguration erfolgt über eine JSON-Datei. In der Basis-Konfiguration enthaltene Medien-Dateien (z.B. Logos) werden beim Download oder Upload nicht berücksichtigt.

### Konfigurationsdatei für andere easydb Instanzen erzeugen

Beim Download der Datei sind standardmäßig die IDs hinterlegter Dateien enthalten. Halten Sie beim Download gleichzeitig `ALT` geklickt, um eine von den IDs bereinigte Version der Konfigurationsdatei zu erhalten. Die IDs werden benötigt, wenn Sie die Datei als Backup für ein Produktivsystem speichern. Beim Übertragen der Konfigurationseinstellungen in eine andere easydb ist eine bereinigte Version erforderlich, da Verweise auf Dateien wie Logos und XSLT Sheets in einem anderen System möglicherweise nicht zur Verfügung stehen.
