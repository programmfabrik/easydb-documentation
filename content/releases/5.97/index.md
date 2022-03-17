---
menu:
  main:
    name: "5.97 (März 2022)"
    identifier: "5.97"
    parent: "releases"
    weight: -597
---

> Diese Version **benötigt keinen neuen Index-Aufbau**

> Nach Löschung von Dateien in easydb werden diese mit zeitlichem Versatz endgültig vom Speichermedium des easydb-Servers gelöscht. Dieses endgültige Löschen wurde nun verbessert. Gelöscht werden alle Dateien, die in easydb gelöscht sind und somit weder in einer aktuellen noch in einer publizierten Version eines easydb-Objekts verknüpft sind.
>
> Nach Einspielen des Updates ist diese Verbesserung als Standardeinstellung deaktiviert. Sie muss manuell durch den Wartungsadministrator aktiviert werden. Diese technische Variable `server/janitor/enable_asset_cleanup` ist in der easydb-5-Dokumentation beschrieben: https://docs.easydb.de/en/sysadmin/configuration/easydb-server.yml/available-variables/.
>
> Im easydb-Frontend im Hauptmenü > Administration > Server-Status im Reiter "Datenübersicht" im Block "Dateien" ist zu finden, wie viele Dateien nach der Aktivierung gelöscht werden und wie viel Speicherplatz diese Originale belegen.
>
> Bitte stellen Sie sicher, VORHER ein vollständiges und wieder einspielbares BACKUP erstellt zu haben!
>
> Bei Kunden mit Wartungsvertrag erstellen wir dieses Backup und aktivieren anschließend das verbesserte Löschen.

# Version 5.97.0

*Veröffentlicht am 16.03.2022*

## Webfrontend

### Neu
* **Export/Download/Upload**: neue Rechte für Metadaten-Mapping

### Verbessert
* **Tabellenansicht**: unterschiedliche Bildgrößen auswählbar
* **Connector**: Instanz wird im Filter am Pool-Namen angezeigt
* **Allgemein**: Accessibility-Verbesserungen

### Behoben
* **Detail-Mask-Splitter-Plugin**: Fix für nicht suchbare Felder
* **Expertensuche**: Objekttyp-Filter korrigiert
* **CSV-Importer**: JS-Fehler behoben
* **CSV-Importer**: nur suchbare Felder tauchen im Mapping-Tab auf
* **Rechte**: ungültige Überschrift entfernt
* **Export-Liste**: Navigation wird beim Löschen von Exporten aktualisiert
* **Suche**: "Heute bearbeitet" kann auch ohne "Gespeicherte Suchen" erlaubt werden
* **Objekte erstellen**: Pool für neue verlinkte Objekte aus Metadaten-Mapping kann ausgewählt werden
* **Editor**: Fehler beim Anwenden von Vorlagen korrigiert
* **Start**: L10n wird früher geladen, um fehlende Übersetzungen zu vermeiden

## Server

### Verbessert
* **Rechte**: Entziehen eigener Rechte beim Speichern optional möglich
* **Rechte**: vergebene Text-Parameter implizieren "kleinere" Werte
* **Rechte**: neue Werte für `metadata_export`, neuer Parameter `metadata_upload`
* **CORS**: Wildcards bei "Erlaubten Herkunftsadressen" möglich
* **Asset-Cleanup**: Funktionalität komplettiert, standardmäßig aber deaktiviert
* **/api/v1/objecttype**: leicht beschleunigt

### Behoben
* **ZIP-Export**: kein Padding der ZIP-Dateien, verursachte Warrnungen
* **EAS**: problematische `docx`-Dateien blockiert
* **EAS**: interner Fehler bei Office-Prozess-Neustart behoben
* **EAS**: Autorotation für `heic` behoben

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:a1bacefda757e7d44a00bd89b30c041fffc9973b553014152ee3ef69a50e33d1
docker.easydb.de/pf/eas                  sha256:c25d07a55d0f81795b195afe4e2d7ebe21d6dbe23fc6cb41128d9d6f5ce75c5e
docker.easydb.de/pf/elasticsearch        sha256:2b1942a329ebbd104cb5427307d150f67b60ebde84918dfe5a6b03f2a0f997af
docker.easydb.de/pf/fylr                 sha256:22b0b504e4f66b6d0542efeb89bea9512c94cd479d4ef7287a398038c148084c
docker.easydb.de/pf/postgresql-11        sha256:85d4ceba8eef8c125ee4b276cb3f97bd03cb7d9e714fac3cde7b2f66199ccacd
docker.easydb.de/pf/server-base          sha256:ae128f9a0fd145c84b10985e83423f6c3a44674658f48d85ba818ecaeb6e0279
docker.easydb.de/pf/webfrontend          sha256:50fd8c5859549ae98d53a4ecd4a62e3ea06332ffeb62766ec5c12bfac577a63c
```
