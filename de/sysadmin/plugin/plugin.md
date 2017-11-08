# Installation eines Plugins

Die easydb bringt eine Reihe von Plugins bereits mit, die so genannten Base-Plugins.

Davon abgesehen können Sie Plugins von z.B. https://github.com/programmfabrik laden oder selbst entwickeln. Die Installation eines solchen Plugins beschreiben wir weiter unten bei [Extension-Plugin](#extension-plugin).

## Liste der aktiven Plugins

Welche Plugins derzeit aktiv sind sehen Sie im Web-Frontend der easydb, ganz links über den "i"(nfo) Knopf und dann mit dessen Unterpunkt "Über".

---

# Base-Plugin

Base-Plugins sind bereits bei der easydb-Installation mit installiert worden und müssen daher nur noch aktiviert werden.

Ergänzen Sie, soweit die Zeilen fehlen, in die Konfigurationsdatei `config/easydb5-master.yml`, deren [Speicherort](/sysadmin/installation/installation.html#datenablage-bestimmen) bei der Installation festgelegt wurde:

    easydb-server:
      plugins:
        enabled+:
          - base.custom-data-type-link
          - base.custom-data-type-gnd

... für z.B. die beiden Plugins custom-data-type-link und custom-data-type-gnd.

Danach sollten Sie noch die easydb neu starten.

---

# Extension-Plugin

Am Beispiel easydb-custom-data-type-geonames:

Ergänzen Sie, soweit die Zeilen fehlen, in die Konfigurationsdatei `config/easydb5-master.yml`, deren [Speicherort](/sysadmin/installation/installation.html#datenablage-bestimmen) bei der Installation festgelegt wurde:

    easydb-server:
      extension:
        plugins:
          - name: easydb-custom-data-type-geonames
            file: plugin/easydb-custom-data-type-gnd/CustomDataTypeGeonames.config.yml
      plugins:
        enabled+:
          - extension.easydb-custom-data-type-geonames

Befehle zur Installation: (Auszuführen in der [Datenablage](/sysadmin/installation/installation.html#datenablage-bestimmen), also dem Verzeichnis dessen Ort bei der Installation festgelegt wurde)

    mkdir config/plugin
    cd config/plugin
    git clone https://github.com/programmfabrik/easydb-custom-data-type-geonames easydb-custom-data-type-geonames
    cd easydb-custom-data-type-geonames
    git submodule init
    git submodule update
    make

Als letztes sollten Sie noch die easydb neu starten.

## Bei Problemen

Bitte beachten Sie dass Probleme mit Extension-Plugins vom Entwickler des Plugins zu beantworten sind. Richten Sie Ihre Fragen daher bitte an den sogenannten Issue-Tracker des Plugins. Für das Beispiel easydb-custom-data-type-geonames wäre das: https://github.com/programmfabrik/easydb-custom-data-type-geonames/issues

---

# Solution-Plugin

Falls wir ein Plugin für Sie entwickeln, dann liefern wir dieses evtl. als Solution-Plugin aus.

In diesem Fall erstellen wir auch Dokumentation, die auf das Plugin zugeschnitten ist. Den Link zu dieser Dokumentation bekommen Sie dann von uns.



