---
menu:
  main:
    name: "5.154 (Ende Mai 2026)"
    identifier: "5.154"
    parent: "releases"
    weight: -654
---

> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.154.0

*Veröffentlicht am 27.05.2026*


# Webfrontend

## Verbessert

* **Editor**:
  * Inkompatible Tags bei Pool-Wechsel: beim Wechsel des Pools werden inkompatible Tags entfernt; der Nutzer wird vor dem Speichern gewarnt
* **Sicheres Token-Handling bei Uploads**:
  * Das Access Token wird bei EAS-Uploads nicht mehr als URL-Parameter in PUT/POST-Requests übertragen
  * es wird nun im Request-Header übergeben
* **Browser-Kontextmenü auf Text und Eingabefeldern**:
  * Die Überschreibung des Kontextmenüs per Rechtsklick ist deaktiviert, wenn der Zielbereich markierter Text oder ein Eingabefeld ist
  * das native Browser-Menü (Kopieren/Einfügen etc.) funktioniert beim Umgang mit Text wie erwartet
* **Gruppen-Manager**:
  * Standard-Einstellungen-Panel: das Panel, das die von einem Nutzer kopierten Standardeinstellungen anzeigt, listet keine Objekttypen mehr auf, die in der Hauptsuche nicht mehr verfügbar sind
* **Drag & Drop von Assets**:
  * Drag & Drop von Assets zur Datensatzerstellung wird nicht mehr ausgelöst, wenn das Asset auf einer Detailansicht oder dem Editor abgelegt wird
  * vermeidet falsch-positive Auslösungen (z. B. beim Verfehlen eines EAS-Feldes beim Drop)
* **Tokenizer**:
  * Bereiche mit Leerzeichen: der Tokenizer in der Expertensuche (für String-Felder) erlaubt nun Bereiche mit Leerzeichen, z. B. `A 1 - A 5`

## Behoben

* **Connector-Plugin**:
  * Verfügbarkeitsprüfung von Remote-Instanzen: Fehler bei der Connector-Verfügbarkeitsprüfung für die neue Version des Connector-Plugins behoben
* **Druck-Manager**:
  * Harmlose Warnungen aus Print-Assertions behoben
  * Verhindert, dass das Frontend in Print-Szenarien auf manchen Browsern (z. B. Firefox) Tooltips zu rendern versucht
  * `cUI.dom.empty`-Fehler wird nun als Log-Warnung ausgegeben statt als Fehler geworfen
* **Cross Instance Request Header**:
  * Unsicherer Header in Cross-Instanz-Requests (z. B. Connector) behoben
  * Harmlose Konsolen-Warnungen in Connector-Szenarien beseitigt
* **Hierarchie "Nicht gefunden" Label**:
  * Das "Nicht gefunden"-Label in der Suche bei Hierarchie-Modus "auto" korrigiert
  * es wurde fälschlicherweise die Top-Level-Variante verwendet
* **CSV-Importer**:
  * Race Condition beim Aufbau des CSV-Importer-Konfigurator-Panels behoben
  * Das Panel konnte rendern, bevor die korrekten DBInfo-Daten verfügbar waren, und einen Fehler werfen
* **Mappen-Einstellungen**:
  * Initiale Datenprüfung in den Mappen-Einstellungen korrigiert
  * Der Speichern-Button bleibt deaktiviert, solange keine Änderungen vorgenommen wurden
* **DBInfo-Masken**:
  * Null-Prüfung in der Funktion "verfügbare Masken abrufen" behoben
  * Die Funktion konnte aufgerufen werden, bevor echte DBInfo-Daten verfügbar waren, und einen Fehler werfen
* **Rechte-Presets**:
  * Fehler behoben, bei dem die Preset-Liste beim Navigieren im Preset-Manager nicht korrekt gespeichert wurde
  * Gelöschte Einträge blieben dadurch weiterhin sichtbar
* **Facets/gespeicherte Suche**:
  * Kritischer Frontend-Fehler beim Generieren einer Suche aus gespeicherten Suchdaten behoben
  * Bei gespeicherter Suche mit Filter konnte auf Zielsystemen ohne Filter-Manager (z. B. Popover-Suche) ein Fehler auftreten
* **Tabellenansicht**:
  * Fehler behoben, bei dem nach einem `OBJECT_INDEX`-Event falsche Zeilen in der Tabellenansicht selektiert wurden


# Server

## Verbessert

* **Sicheres Token-Handling bei Uploads**:
  * `/api/v1/eas/put`: bei `OPTIONS` Requests wird kein Token erwartet


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.154.0            sha256:637647f8097a9b3eecce850f804dc646f4a645cf12ad710c581d2baba7511a6e
docker.easydb.de/pf/elasticsearch:5.154.0  sha256:049e98512933bb582bdb54c6c014aa6dbd144d19b18fb2bf7b07479ee21c1397
docker.easydb.de/pf/fylr:5.154.0           sha256:78ff91b129b383f334757e3a191b3334bfb531a79e03d3e3ffbb7c208d1f4aa7
docker.easydb.de/pf/postgresql-14:5.154.0  sha256:d5816a18d74ba7f3336077c5363bda988e827e2b4e00372bc422a02e415b3b1b
docker.easydb.de/pf/server-base:5.154.0    sha256:928e9dab82fa464219c2d186290006839f58b0ef58938c790fee164d7c5c0f56
docker.easydb.de/pf/webfrontend:5.154.0    sha256:bc16b904441dac0f8782b25c70555e9ae803b397ff5a4d20ba238bbfd6e088b0
```
