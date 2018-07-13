# Basis-Konfiguration

In der Basis-Konfiguration werden globale Einstellungen für easydb vorgenommen. Über die Reiter und das <code class="button">...</code>-Menü können die Einstellungsbereiche aufgerufen werden.

![](basis_config_de.jpg)

Das Kapitel enthält Erläuterungen und zu den Themen:

* [Allgemein](general/general.html)
* [Hochladen](upload/upload.html)
* [Anmelden](login/login.html)
* [Erweiterte Funktionen](extended/extended.html)
* [Export und OAI/PMH](export/export.html)
* [Cloud-Dienstleister](cloud/cloud.html)
* [CMS](cms/cms.html)
* [Editor](editor/editor.html)
* [Remote Plugins](plugins/plugins.html)
* [Server-Config](server-config/server-config.html)

## Hochladen/Herunterladen der Basis-Konfiguration 

In der Basis-Konfiguration besteht unten links über den <i class="fa fa-cog"></i>-Button die Möglichkeit die bestehenden Einstellungen der Basis-Konfiguartion herunterzuladen und eine Basis-Konfigurationsdatei hochzuladen (z.B. als Fallback). 

![](basis_config_schema_de.jpg)

Der Download und Upload der Konfiguration erfolgt über eine JSON-Datei. In der Basis-Konfiguration enthaltene Medien-Dateien (z.B. Logos) werden beim Download oder Upload nicht berücksichtigt.

### Konfigurationsdatei für für andere easydb Instanzen erzeugen

Beim Download der Datei sind standardmäßig die IDs der Dateien enthalten. Halten Sie beim Download gleichzeigt `ALT` geklickt, um eine von den IDs bereinigte Version der Konfigurationsdatei zu erhalten. Die IDs werden benötigt, wenn Sie die Datei als Backup für ein Produktivsystem speichern. Beim Übertragen der Konfigurationseinstellung in eine andere andere easydb ist eine bereinigte Version erforderlich, da die dazugehörigen Dateien dort nicht enthalten sind.
