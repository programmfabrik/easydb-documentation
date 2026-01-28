---
menu:
  main:
    name: "5.152 (Ende Januar 2026)"
    identifier: "5.152"
    parent: "releases"
    weight: -652
---

> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.152.0

*Veröffentlicht am 28.01.2026*


# Webfrontend


## Verbessert

* **Maskeneditor**:
  * Das Verhalten des Maskeneditors wurde verbessert, wenn unbekannte Mask-Splitter in einer Maske vorhanden sind
  * Das betrifft insbesondere Mask-Splitter, die in nicht geladenen Plugins implementiert sind
  * Sie können nun korrekt gelöscht werden und führen nicht mehr dazu, dass die Maske beschädigt wird

* **Varianteneditor**:
  * Beim Erstellen einer neuen Datei-Variante im Varianten-Editor wurde ein neues Kontrollkästchen hinzugefügt
  * Damit kann die neue Variante automatisch als Standardvariante festgelegt werden

* **Sucheingabe**:
  * Die Verarbeitung verschiedener Suchtypen im Suchfeld wurde verbessert

* **Export-Manager**:
  * Der Export-Manager wurde um neue beschreibende Texte ergänzt


## Behoben


* **Sidebar**:
  * Es wurde ein Problem behoben, bei dem unter bestimmten Umständen die Detail-Seitenleiste leer geöffnet wurde, wenn ein zuvor geladenes Objekt erneut geöffnet wurde

* **Feldsichtbarkeit**:
  * Es wurde ein Fehler behoben, bei dem die Einstellungen für die Feldsichtbarkeit in der Detailansicht ignoriert wurden

* **Verlinkte Objekte**:
  * Es wurde ein Fehler behoben, bei dem bei der Verwendung verlinkter Objekte in der Expertensuche fälschlicherweise eine Meldung über fehlende Berechtigungen angezeigt wurde

* **CSV-Importer**:
  * Ein Problem beim Importieren leerer Werte in Spalten mit dem Typ *Datumsbereich* wurde behoben
  * Diese importierten Werte werden nun korrekt ausgewertet und löschen den aktuellen Wert, wenn eine Objektaktualisierung durchgeführt wird

* **Datenmodell**:
  * *Datumsbereich* Spalten: Die Anzeige von Feldern vom Typ *Datumsbereich* mit Textdarstellung in der Tabellenansicht wurde korrigiert
  * Darüber hinaus wurde die automatische Erkennung von Bereichen aus Text verbessert, sodass nun auch Monate mit kleinen Buchstaben am Anfang berücksichtigt werden


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.152.0            sha256:a295b058504b8880e22ffb958152320f549db2b17a6f3b372585f8aa070cde35
docker.easydb.de/pf/elasticsearch:5.152.0  sha256:e1e1ba2935e4f9777c267fcf1bd73c1d37b6a526e3550d62100310fa4f2cecf5
docker.easydb.de/pf/fylr:5.152.0           sha256:9dede0c6895cdb44f72c4b40bf714cf583db6a60327351b2470523ad225afda5
docker.easydb.de/pf/postgresql-14:5.152.0  sha256:3f32e39a8ac803fbf31e31ab1f994f5b38ac9add7bdd1163426f6bf314d44ad3
docker.easydb.de/pf/server-base:5.152.0    sha256:7db7e7c5510d54152e49a6a88a1f9ebee559522537b56a7b7bfd889af542582c
docker.easydb.de/pf/webfrontend:5.152.0    sha256:b570cf993db83da04d8b05f4ce70020ab1444780fd953cffbc30fb709c63acea
```
