---
menu:
  main:
    name: "5.132 (Mai 2024)"
    identifier: "5.132"
    parent: "releases5130"
    weight: -632
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.132.0

*Veröffentlicht am 08.05.2024*


# Webfrontend

## Neu

* **Änderungshistorie im Editor**:
  * Es wurde die Möglichkeit hinzugefügt, die Änderungshistorie eines Objekts im Seitenleisten-Editor anzuzeigen
  * Zuvor war dies nur möglich, wenn man sich im Detail des Objekts befand

## Verbessert

* **Request Data**:
  * Das Senden von JSON in Requests des Frontends wurde optimiert
  * Dies führt zu einer Reduzierung der Anfragegröße in bestimmten Szenarien, wie z.B. bei großen Datenmodelle
* **JSON-Importer**: Verbesserte Anzeige der vom JSON-Importer verursachten API-Fehlermeldungen
* **Zoom**:
  * Das Zoomer-Tool zum Vergrößern des Asset-Browsers wurde verbessert
  * Diese Verbesserungen umfassen eine bessere Visualisierung von Bildern mit Transparenz und Optimierungen bei der Verwendung sehr großer Bilder als Quelle
* **Passwortfeld**: Es wurden Verbesserungen an den Passwortfeldern vorgenommen, die die Schaltfläche „Passwort anzeigen/verbergen“ betreffen
* **Hochladen der Basiskonfiguration**: Verbesserte Kompatibilität von exportierten Basiskonfigurationen zwischen *easydb5* und *fylr*

## Behoben

* **Vollbildansicht**: Es wurden mehrere Korrekturen an der Vollbild-Detailansicht vorgenommen, insbesondere bei der Arbeit mit Objekten, die keine Assets enthalten
* **Detailansicht**:
  * Die Detail-Seitenleiste versucht nun nicht mehr, Objekte zu laden, die noch nicht fertig indiziert wurden
  * Jetzt kann die Detailansicht auf die Indizierung warten
* **Tabellenansicht**: Es wurde ein Fehler behoben, bei dem Zeilen, die nicht in der Tabellenansicht geöffnet werden sollten, nach der Durchführung einer Suche geöffnet wurden
* **Mappen**: Es wurde ein Problem behoben, bei dem der Mappen-Manager unter bestimmten Umständen automatisch aktualisiert wurde, wodurch der Arbeitsablauf des Benutzers unterbrochen wurde
* **CSV-Importer**: Es wurde ein Fehler beim Importieren von Texten mit Zeilenumbrüchen behoben, die fälschlicherweise als mehrere Werte in einem verschachtelten Feld erkannt wurden
* **Basetype-Sortierung**:
  * Die Sprachauswahl für die Sortierung von Basetypes wurde korrigiert
  * Jetzt wird die für das Frontend eingestellte Sprache verwendet
* **Anmeldung**: Fehler behoben, bei dem eine Fehlermeldung angezeigt wurde, wenn ein Cookie mit einer sehr alten Sitzung vorhanden war
* **Datensortierung**: Die Sprache, die für die Sortierung der Daten in der Anwendung verwendet wird, wurde korrigiert
* **Logo-Anpassung**: Es wurde ein Fehler behoben, bei dem das Feld zur Konfiguration des Logos in der Basiskonfiguration nicht korrekt angezeigt wurde
* **Datums-Spalten**:
  * Datumsspalten in Datensätzen verwenden nun korrekt die eingestellte Sprache als Datenbanksprache
  * Zuvor wurde die Sprache des Frontends verwendet, um die Datumsangaben in diesen Feldern zu formatieren

# Server

## Neu

* **Server-Prozesse**: Maximale Request-Größe kann jetzt in der Serverkonfiguration als Wert `max_request_size_mb` definiert werden

## Verbessert

* Geändertes Datumsformat für `en-US`: Format geändert von `MM/DD/YYYY` zu `YYYY-MM-DD`

## Behoben

* **Metadaten-Import**: Import-Profile: defekte Video-Attribute wurden entfernt
* **Schema Upgrade**:
  * umbenannte Pool-Linkfelder in Mappen aktualisiert
  * Entfernen des verknüpften Pool-Linkfeldes aus den Mappeneinstellungen, wenn das Feld entfernt wurde


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.132.0         sha256:1537535c5ede2af6e1f561bdd79b1823a7aab99b22fd0504156409f9efacb143
docker.easydb.de/pf/eas:5.132.0            sha256:34578c980a2849d34a5ac20470a449c5e689f2c634e07eec6f3f53f397d4b64f
docker.easydb.de/pf/elasticsearch:5.132.0  sha256:400b32419d215f35bba940106d50c62af7798b389185a867fbf6d5c38a5763ba
docker.easydb.de/pf/fylr:5.132.0           sha256:29b905bbad6a49c7995d9297d29a99e092d509d23fa622b67d60ea24458f112f
docker.easydb.de/pf/postgresql-14:5.132.0  sha256:78359080406dd9db32d787ec595c1017127f26f1cee1298ae1836893450106a0
docker.easydb.de/pf/server-base:5.132.0    sha256:c7551a3010b19ea711c11b404ec49e33157c614337f2ffd8b322644d960b69e1
docker.easydb.de/pf/webfrontend:5.132.0    sha256:22abcb50a43143859d72bbb8639b94d806121deeda0426fd8582d8b82ce03e1d
```
