---
menu:
  main:
    name: "5.139 (Dezember 2024)"
    identifier: "5.139"
    parent: "releases5130"
    weight: -639
---

> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.139.1

*Veröffentlicht am 10.01.2025*

# Webfrontend

## Behoben

* **Detail-Map-Plugin**: JS-Fehler behoben, der das Öffnen der Detail-Ansicht verhinderte

# Version 5.139.0

*Veröffentlicht am 11.12.2024*


# Webfrontend

## Neu

* **Datums-Spalten**: Es wurde eine neue Maskenoption "Umwandlung in v. Chr. / n. Chr. vermeiden" für Datumsspalten hinzugefügt
  * Damit wird die automatische Konvertierung von Datumsangaben in das "v. Chr."-Format deaktiviert, was eine größere Flexibilität bei der Handhabung von Datumsangaben ermöglicht

## Verbessert

* **Standardansicht**:
  * Verbesserte HTML-Elemente unterstützen das HTML-Attribut `"title"` und ermöglichen Tooltips, die vollständige Werte anzeigen
* **Verknüpfte Objekte**:
  * Verknüpfte Objektfelder im Editor werden jetzt automatisch aktualisiert, wenn ein anderes Feld, das auf dasselbe Objekt verweist, seine Daten aktualisiert
  * Dies stellt sicher, dass alle verknüpften Felder aktuell bleiben
* **Mappen-Manager**:
  * Ereignis-Listener für sichtbare Sammlungen wurden wieder aktiviert
  * Dies ermöglicht eine automatische Aktualisierung des Frontends, wenn eine Sammlung in einer anderen Sitzung bearbeitet wird
* **Benutzer-/Gruppenauswahl**:
  * Die Anzahl der angeforderten Objekte bei der Anzeige von Gruppen und Benutzern wurde erhöht
  * Dies dient dazu, Einschränkungen in größeren Umgebungen zu beheben
* **Maskeneditor** & **Konfigurationspanel**:
  * Es wird sichergestellt, dass die Standardeinstellungen für Custom Datatypes ohne Konfiguration in der `manifest.yml` des Plugins sichtbar bleiben
  * Die Schaltfläche "Einstellungen" ist immer zugänglich, so dass Benutzer ohne explizite Konfiguration auf die Standardeinstellungen zugreifen können

## Behoben

* Die Download-Methode wurde korrigiert, um den angegebenen Dateinamen korrekt anzuwenden
  * Zuvor ignorierte die Hilfe die definierte Download-Namens-Eigenschaft und gab das Verhalten des Browsers vor
  * Jetzt wird die Datei mit dem vom Benutzer angegebenen Namen heruntergeladen
* **Revers verlinkte Tabellen**:
  * Es wurden Probleme beim Aktualisieren von revers verlinkten Feldern behoben, die gleichzeitig in einem anderen Editor geöffnet und bearbeitet werden
  * Änderungen werden jetzt korrekt übertragen, um die Datenkonsistenz zu gewährleisten
* **Scheduler**: Es wurde ein Fehler behoben, der die Anzeige von `weekdays` ("Wochentag") and `days_of_the_week` ("Tag innerhalb der Woche") verhinderte
* **Benutzer-Manager**: Es wurde ein Problem behoben, bei dem das Deaktivieren aller sichtbaren Spalten dazu führte, dass die Benutzerliste nicht gerendert wurde und die Suchfunktionalität unterbrochen wurde
* **Dezimalfelder**: Die Hinweise zur Bereichsvalidierung für Dezimalfelder wurden korrigiert, um eine genaue Anleitung zu bieten
* **Benutzervorlagen**: Es wurde ein Problem behoben, das die korrekte Persistenz von Änderungen in Editor-Benutzervorlagen verhinderte


# Server

## Neu

* Neuer optionaler URL Parameter für `/api/event/list`:
  * `skip_count` (boolean): wenn gesetzt wird `"total"` (Anzahl aller Events) in der Ausgabe nicht ausgegeben
  * Das kann die Performance besonders bei vielen Events verbessern

## Verbessert

* **Easydb Asset Server** (EAS):
  * Der `rput` Endpunkt prüft beim Laden der Dateien den HTTP-Statuscode
  * Dieser wird im (Fehler-)status der Datei wiedergegeben
* Geschwindigkeit der `/api/db?all_versions` API wurde verbessert


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.139.0            sha256:444f97c0f781f1ad96a1df2e929a34aa993d143898a9deba08e0548760d68678
docker.easydb.de/pf/elasticsearch:5.139.0  sha256:225b72c92d11646811353ba4961b44ea81b948715ee799cd58d89cd582ccf613
docker.easydb.de/pf/fylr:5.139.1           sha256:63a841187de0022be6e642b62695d61ba9b0894b2885e337e807ef7420d49f9e
docker.easydb.de/pf/postgresql-14:5.139.0  sha256:47cfa219dc0935685ed5626ee70c5ed95fffe31e31ebed729fc71fd9000759c0
docker.easydb.de/pf/server-base:5.139.1    sha256:b652df495f4703121e0c51b1931ea51a6a32fdac7fdbf6412428dce1e63bf72e
docker.easydb.de/pf/webfrontend:5.139.1    sha256:6618d7a291c9d280f0a171a8278c56fc62f6e109e0341e1277e2fae6facc9dda
```
