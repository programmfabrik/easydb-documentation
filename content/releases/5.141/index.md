---
menu:
  main:
    name: "5.141 (Februar 2025)"
    identifier: "5.141"
    parent: "releases"
    weight: -641
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.141.0

*Veröffentlicht am 26.02.2025*


# Webfrontend

## Neu

* **Tool: Mappe zur Suche hinzufügen**:
  * Es wurde ein neues Tool hinzugefügt, mit dem die Mappensuche an das Ende der Sucheingabe angehängt werden kann, anstatt die gesamte Sucheingabe zu überschreiben
  * Dies ermöglicht es, Mappenabfragen mit anderen Abfrageelementen zu kombinieren

## Verbessert

* **Vorschläge zur Autovervollständigung der Suche**: Die Geschwindigkeit der Autovervollständigung bei der Sucheingabe wurde erhöht
* **Hauptsuche und Deep Links**:
    * Verbesserte Ausführungsreihenfolge, wenn ein Deep Link in der URL in der Hauptsuche vorhanden ist
    * Die Deep-Link-Suche wird jetzt innerhalb der Hauptsuche ausgeführt, was Ressourcen spart und die Ladedauer des Frontends verringert
* **Tool zum Zurücksetzen der Suche**: Die Schaltfläche "Zurücksetzen" setzt jetzt auch den Suchtyp-Auswahlmanager zurück und aktiviert alle Optionen im Ressourcen-Panel
* **CSV-Importer**:
  * Es wurde ein Warnhinweis für Zahlen hinzugefügt, die im CSV-Importer von Dezimalformaten in Ganzzahlen umgewandelt werden
  * Diese Warnung wird bei der Vorbereitung des Imports in die entsprechende Spalte `warning_text` aufgenommen

## Behoben

* **Mappeneigenschaften**: Es wurde ein Problem behoben, das die korrekte Anzeige der Eigenschaften einer Mappe verhinderte, wenn die Instanz einen Objekttyp ohne sichtbare Masken hatte
* **Nur-Lesen-Modus**: Die Anzeige der Nur-Lese-Meldung im Nur-Lese-Modus wurde korrigiert
* **Detail-Seitenleiste**: Es wurde ein Fehler behoben, bei dem die Detail-Seitenleiste ohne `global_object_id` geöffnet wurde, nachdem der Server das Frontend informiert hatte, dass der Benutzer keine Berechtigung hat, ein Objekt zu erstellen
* **Token-Suche**: Ein Fehler wurde behoben, bei dem exakte Token-Vorschläge nicht anklickbar waren
* **Sucheingabe**:
  * Es wurde ein Fehler behoben, bei dem die Sucheingabe nach einem leeren Aufruf unbrauchbar wurde
  * Das Platzhalter-Token wurde nach einem leeren Aufruf nicht wieder eingefügt, was eine Eingabe durch den Benutzer verhinderte
* **Autovervollständigung in der Sucheingabe**:
  * Die Bereinigung von Einträgen, wenn das Autovervollständigungs-Popup angezeigt wird, wurde korrigiert
  * Zuvor wurden die Ergebnisse früherer Suchen einige Millisekunden lang angezeigt, wodurch die Benutzeroberfläche beim Laden neuer Ergebnisse weniger flüssig war
* **Metadaten-Mapping**:
  * Es wurde ein Fehler behoben, der dazu führte, dass "Deep Link URL" in easydb hinzugefügt wurde, obwohl dies nur in fylr unterstützt wird
  * Fehler behoben, bei dem der Kopierbutton für Metadatenfelder für alle Felder aktiviert war (dieser Button sollte nur für benutzerdefinierte Metadatenfelder aktiviert sein)
* **Page Viewer**: Es wurde ein Fehler in der Seitenansicht behoben
* **Editor-Templates**: Fehler beim Zusammenführen von Editorvorlagen in einem Datensatz mit verknüpften Objekten, die durch Metadaten-Zuordnung erstellt wurden, behoben
* **Standard-Tags im neuen Editor**: Standard-Tags werden jetzt korrekt in `dbinfo` gesetzt, wenn ein neues Objekt erstellt wird.


# Server

## Verbessert

* `api/v1/db/*?all_versions=1`: in älteren Versionen werden Asset-IDs, die inzwischen gelöscht wurden, nicht mehr ausgegeben

## Behoben

* **Bidirektionale Verlinkungen**:
  * Probleme bei automatischen Updates von bidirektionalen Verlinkungen behoben
  * Automatische Cache-Invalidierung und Dirty Queueing nach Änderungen in bidirektionalen Links verbessert


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.141.0            sha256:22d2742af819a4498f9d2658ca62b6737d2ed6fd504e65c5504b8a46cd6b0484
docker.easydb.de/pf/elasticsearch:5.141.0  sha256:697c8aea400507f242d9137935414591e288d93b42eb2c4144a32347958bf3e9
docker.easydb.de/pf/fylr:5.141.0           sha256:21d450138f3745d41cbda05ab256c4af6bdf50deeaaaa273ad11fec018e3d377
docker.easydb.de/pf/postgresql-14:5.141.0  sha256:24df38ec98ac77d0d38cd4ab87e57f0255b276215e5f867e9eaefde1919e0b40
docker.easydb.de/pf/server-base:5.141.0    sha256:4dbe5876b158024958c4c6285d5e3deca3d52fa20a1ef4a97683adfa5d834b5a
docker.easydb.de/pf/webfrontend:5.141.0    sha256:4375ebaa7603accdb2c138c64b99d7abb4278e77191c6c8c30b5890dae828bc7
```
