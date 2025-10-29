---
menu:
  main:
    name: "5.148 (September 2025)"
    identifier: "5.148"
    parent: "releases"
    weight: -648
---

> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.148.0

*Veröffentlicht am 24.09.2025*


# Server

## Verbessert

* **Docker Container:**
  * verbesserte Vergabe von UIDs/GIDs


# Webfrontend

## Behoben

* **Suche:**
  * **Auswahl:**
    * Fehler behoben, der den Ladevorgang blockierte, wenn eine große Anzahl an Objekten (`>700`) mit der Option *Alle auswählen* oder dem Shortcut ausgewählt wurden
  * **Eingabe:**
    * Fehler im Verhalten des `Strg+A`-Shortcuts in Eingabefeldern behoben, wenn die Suche geöffnet ist
* **Editor:**
  * Aufforderung zum Neuladen bei eingehendem Update-Ereignis korrigiert, um mehrfache aufeinanderfolgende Aufforderungen zu vermeiden
  * Fehler behoben, bei dem mehrere "Neuer Datensatz"-Dialoge durch aufeinanderfolgende `Alt+N`-Shortcuts ausgelöst wurden
  * Fehler beim Speichern mit dem Shortcut `Strg+S` behoben
  * **Masken-Manager:**
    * Fehler behoben, der beim Wiederherstellen einer vorausgewählten Maske über den Maskenspeicher auftrat;
    * die Objektdaten wurden nicht korrekt geladen, wodurch unvollständige Daten im Editor angezeigt wurden
  * **Rechtemanagement:**
    * Fehler behoben, bei dem mehrere "Keine Rechte"-Popups für verknüpfte Objekte mit eingeschränkten Rechten angezeigt wurden
* **Tabellenansicht:**
  * Fehler behoben, der falsche ausgeschlossene Felder übermittelte
* **Mappen:**
  * Sortierleistung verbessert für ein schnelleres und reibungsloseres Nutzererlebnis
* **Tags:**
  * Fehler behoben, der beim Zugriff auf Top-Level-Daten in der Detaildarstellung von Tag-Feldern auftrat


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.148.0            sha256:fdfe11685fe6fc45580d7d0950023a09e2f8783ea4a1afd662fd38580991a9a4
docker.easydb.de/pf/elasticsearch:5.148.0  sha256:f9daa78c17e9a19a8b69f4ada666dc969118490fdae6beb335ffab197a9535f4
docker.easydb.de/pf/fylr:5.148.0           sha256:dfcf2ed7ef0f050e16982ee8dc57dc8177ebd4de2e63c3a5a494394958a993c8
docker.easydb.de/pf/postgresql-14:5.148.0  sha256:507104d84da06ae8d64d2964516bdaf10a3991d1800f4b703cc4dbece8b3fd41
docker.easydb.de/pf/server-base:5.148.0    sha256:7b6d0053b207d17c22b9c09d620d0b1c23aaeb45531f57808d3c89e19200730b
docker.easydb.de/pf/webfrontend:5.148.0    sha256:7d7e5be598bacb7eee83814b72c7e3c5f5ad67212747a3f1c9269780653052f1
```
