---
menu:
  main:
    name: "5.118 (Juni 2023)"
    identifier: "5.118"
    parent: "releases"
    weight: -618
---


> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.118.0

*Veröffentlicht am 22.06.2023*


# Webfrontend

## Verbessert

* **Detail**: Erkennung von Weblinks verbessert
* **Asset-Anzeige**: AAC-Dateien können direkt im Browser abgespielt werden
* **Detail**: Buttons für Suche nach verschachtelten Objekten verbessert
* **PDF-Creator**: Textfelder erlauben jetzt auch Zeilenumbrüche
* **HTML-Editor-Custom-Typ**: Template-Unterstützung

## Behoben

* **Editor**: Kopieren von Datensätzen korrigiert
* **Benutzer-Suche**: Anzeige des Filter-Icons für "archivierte Benutzer" korrigiert
* **Hauptmenü**: Konfiguration von Objekten als Buttons korrigiert
* **Schnellansicht**: komplett versteckt, wenn Nutzer keinerlei Rechte hat, dort Inhalte zu sehen
* **Allgemein**: Fehler bei unerwarteten Sprach-Tags behoben
* **Benutzerverwaltung**: Fehlerhaftes Ausfüllen von Feldern durch den Browser unterbunden
* **Metadaten-Mapping-Konfiguration**: Duplizierung von Feldern beim Editieren verhindert

# Server

## Behoben

* fehlende System-Object-IDs werden beim Upgrade ergänzt

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome:5.118.0         sha256:9d30fa74fe6a6a1ad9d0f36e84e4489093d04a37b341c4fe8f98f96969ba054a
docker.easydb.de/pf/eas:5.118.0            sha256:ffef84b28e04fb77f9935fa9d0cada573a250954021aa5acaeda58270aee82d0
docker.easydb.de/pf/elasticsearch:5.118.0  sha256:78f15e8aa21be1be55145969d37613849ce3d6aa5724efa08ce2a5f9b6c02b35
docker.easydb.de/pf/fylr:5.118.0           sha256:f731980cbdb55ef4f24e3902753dd8ad7735b53b921943fb8c1f6b3eb8e4dc5b
docker.easydb.de/pf/postgresql-14:5.118.0  sha256:41aefdf99d296cfa189215fa3ff1fc60e1073091d8bfba0fa156a54ce42d14df
docker.easydb.de/pf/server-base:5.118.0    sha256:c9b4010e0eb9d7547f492aa51f1d5d16f7c8bf1e7a8df3ceb53ee548184080dd
docker.easydb.de/pf/webfrontend:5.118.0    sha256:38406c5d4e631754cda84c4fb710b09d4b67f50ca9f4c09f05a55ceb08e846ef
```
