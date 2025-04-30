---
menu:
  main:
    name: "5.143 (Ende April 2025)"
    identifier: "5.143"
    parent: "releases"
    weight: -643
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.143.0

*Veröffentlicht am 30.04.2025*


# Webfrontend

## Neu

* **CSV Importer**:
  * Unterstützung für mehrfach verschachtelte Werte in „Datumsbereich“-Feldern hinzugefügt
  * Benutzer können nun mehrere verschachtelte Werte in dieselbe "Von"-Zelle einfügen

## Verbessert

* **Suche**:
  * Verbesserte Abfrage, um ungültige Suchanfragen zu verhindern, Abfrageeingabe wird nun vor der automatischen Ausführung validiert
  * Verbessertes Parsen der Abfrageeingabe, um `OR` und `AND` Operatoren korrekt anzuwenden
* **Boolesches Feld**:
  * Die Ansicht von booleschen Feldern im Editor wurde aktualisiert und zeigt nun immer "Ja" an, was die Übersichtlichkeit verbessert

## Behoben

* **Feldwerte anzeigen**:
  * Ein Problem im Plugin wurde behoben, das das Laden von Owner-Feldern verhinderte, wenn Gruppen anstelle von Benutzern verwendet wurden
* **Workflow Validierung**:
  * Stiller Fehler in der Methode `getSaveData` in `TagTransition` behoben
  * Außerdem wurde ein Problem behoben, bei dem mehrere Warnsymbole in ungültigen Workflows erschienen
* **Nur-Lesen-Modus**:
  * Deaktiviert Drag-and-Drop in Hotfoldern und verhindert das Hinzufügen neuer Objekte zu Sammlungen im schreibgeschützten Modus
* **Hauptanwendung**:
  * Fehler beim Drag-and-Drop einer Datei in der Hauptanwendung behoben
* **Query Element Field Editor**:
  * Rendering-Probleme mit Feldern, die eine Suchinstanz erfordern, behoben
* **Änderungshistorie: Diff-Ansicht**:
  * Fehler behoben, der durch den Zugriff auf `null`-Werte während der Diff-Berechnung verursacht wurde
* **CSV Importer**:
  * Unbehandelter Fehler beim Importieren von verknüpften Objekten über CSV behoben


# Server

## Neu


* **Api**:
  * `/api/v1/user?include_last_seen=true`: neues `_last_seen_at` Timestamp-Feld im `user`-Objekt, wenn der User sich mindestens einmal eingeloggt hat

## Verbessert

* **Suche**:
  * Wechsel des Sub-Felds für `fulltext` + `phrase` Suchen in `string` Feldern

## Behoben


* **Api**:
  * `/api/v1/db/.../list?all_versions=true`:
    * Doppelte Einträge aus Mehrfachfeldern entfernt
    * Ebenfalls wurden Probleme mit der Sortierung von Einträge in Mehrfachfeldern behoben
* Datenbank-Statement für den supervisor, das invalide Zeilen zurückgab, wurde gefixt


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.143.0            sha256:e9ccacabbf14d2af78b8d6ce189e203597b74a4bd0cb04e8165e63c726b12386
docker.easydb.de/pf/elasticsearch:5.143.0  sha256:06d73caccf650d2de383970d17e7d17e8bee9dd8898d513e1e8cad0d7029dc84
docker.easydb.de/pf/fylr:5.143.0           sha256:d1aadee8563d7fe1db654427c3c04c83fedc30502bf847528a1ac09ef993edb0
docker.easydb.de/pf/postgresql-14:5.143.0  sha256:865abb0cdf238713a5c29b06ff508b9a247ff2147765c4f7ecc9b0e2a88b56b4
docker.easydb.de/pf/server-base:5.143.0    sha256:958ad3f2aebd879986c335b37ec41cc642061a7979eddea84c8d40516a62e902
docker.easydb.de/pf/webfrontend:5.143.0    sha256:476d01e9f1ba33207dcff9eb562c469d83cb3b379d62f187f421e311cb551403
```
