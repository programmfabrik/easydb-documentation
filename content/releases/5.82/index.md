---
menu:
  main:
    name: "5.82 (April 2021)"
    identifier: "5.82"
    parent: "releases"
    weight: -582
---

> Für dieses Release ist ein **Re-Index nötig**, bitte planen Sie entsprechende Zeit für das Einspielen des Updates ein. 

# Version 5.82.0

*Veröffentlicht am 14.04.2021*

## Webfrontend

### Neu

* **Editor**: Mit der neue Funktion "Filter für verknüpfte Objekte" können Suchen von verlinkten Objekten automatisch gefiltert werden.
* **Nutzermanager**: Anzeige und Suche von archivierten Nutzern.
* **Datenmodell**: Unterstützung der serverseitigen Sortierung von Mehrfachfeldern.
* **Maskenmanagement**: Panels können jetzt automatisch aufgeklappt werden, wenn sie nicht leer sind.

### Verbessert

* **Export**: Das Feld `_uuid` wurde in der Feldauswahl ergänzt.
* Workflow: Nach dem Speichern bleibt der Workflow-Reiter aktiv.

### Behoben

* Mappen ohne Namen führen nicht mehr zu einem Fehler.
* CSV-Importer: Speichern von Mapping mit Tags wurde repariert.
* CSV-Importer: Nicht-suchbare Felder werden ignoriert.
* **Export**: Nicht-suchbare Felder werden ignoriert.
* Editor: Eingaben in Datumsbereichsfeldern bei leerem Von oder Bis wurden repariert.
* Maskenmanagement: Vorschau wurde für große Datenmodell repariert.
* Änderungshistorie: Tags werden jetzt nicht mehr doppelt angezeigt.

## Server

### Neu

* **Exporter**: Im CSV-Format werden `_uuid`,`_tags`nud `_last_modified_date` exportiert.

### Verbessert

* **Mappen**: Generelle Beschleunigung von Rechte-Checks für geteilte Mappen. Das wirkt sich auch auf die Geschwindigkeit beim Speichern von Pools aus.

### Behoben

* **Export**: Der Laden von verlinkten Objekten im XML Export wurde verbessert und teilweise repariert.
* **Hotfolder**: Verschiedene Fehlerbehebungen für komplexe Objektstrukturen.
* **User**: Einige Fälle für die Pseudonymisierung wurden repariert.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:e3599220fca5194ee6b1e4792a10009982b4528f4484162d9b6a8da42b2bae10
docker.easydb.de/pf/eas                  sha256:6da52cee973c66ff69e61ced2f8b1cef36dcd4cd89fd7a091143a32b95d0e022
docker.easydb.de/pf/elasticsearch        sha256:efacf01d4b972fbfd87923598b48a761dab2d01d95282b6d987cf8932d10974e
docker.easydb.de/pf/fylr                 sha256:8a8d3be7d46ee32cbcea12b0fad14be82ebec8845b8d4e68c2288947a89e9d4b
docker.easydb.de/pf/postgresql-11        sha256:16374ce88db01d7b83f785423a04616f5175a6b52ff190cc19d8e5972f11a611
docker.easydb.de/pf/server-base          sha256:a17434bc4ca0584a01e775554831cb650fbc66f81cc032c632bbc00f5731badd
docker.easydb.de/pf/webfrontend          sha256:179a5190f4d1ab3a99e4a673188196aa2a7953c8094971613a70a882ec9ed9b5
```

