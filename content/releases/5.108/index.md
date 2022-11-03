---
menu:
  main:
    name: "5.108 (Anfang November 2022)"
    identifier: "5.108"
    parent: "releases"
    weight: -608
---

> Mit diesem Update werden die Versionen von Video-Assets neu berechnet und wegen der Konfigurationsänderung auch Objekte neu indiziert. Dies geschieht im Hintergrund, kann die Applikation aber unter Umständen ausbremsen.

# Version 5.108.1

*Veröffentlicht am 03.11.2022*

# Webfrontend

## Behoben

* Download-Problem behoben

# Version 5.108.0

*Veröffentlicht am 02.11.2022*

# Webfrontend

## Neu

* **Mitteilungen**: Pool-Filter für Hinweise vor dem Download

## Verbessert

* **PDF-Creator**: Fortschrittsanzeige bei Erstellung des PDFs

## Behoben

* **Metadaten-Mapping**: Fehler bei Verwendung des Filters behoben
* **Metadaten-Mapping**: Mapping fester Werte als Ziel des Import-Mappings ausgeblendet
* **Metadaten-Mapping**: doppelte Tag-Info ausgeblendet
* **Suchergebnisse drucken**: feste Limitierung entfernt, maximale Anzahl der druckbaren Datensätze wird aus Konfiguration gelesen
* **Nutzer-Bild**: Platzhalter-Icon, falls kein Bild vorhanden ist
* **Detail**: Asset-Browser auch für unangemeldete Nutzer standardmäßig aktiviert
* **CSV-Import**: Problem bei leerem Pool-Feld behoben
* **Vollbild-Ansicht**: Funktion des Detail-Buttons korrigiert

# Server

## Neu

* Option `tokens_dont_split_query` für `/api/suggest`

## Verbessert

* **Video-Assets**: vorberechnete Video-Versionen erhalten durch Verwendung höherer Bit-Raten eine bessere Qualität

## Behoben

* **XML-Mapping**: nicht suchbare Felder können im Export-Mapping verwendet werden

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:58463979ca8515e6cb156d8b96dbaec67930edcbe8143ab69345dafe8f03d4cd
docker.easydb.de/pf/eas                  sha256:df5946ca633ffe4ecd890de077b1814009f32fa41d5f62637dad20495009cfec
docker.easydb.de/pf/elasticsearch        sha256:69bd37e20ee4a588e95c037071d6cf99e6cb3eec5f42d96a047b28116a18aab9
docker.easydb.de/pf/fylr                 sha256:744b61cdeab8b9d2158089ef4da234bf076a10e523b654318fb233d7258bda68
docker.easydb.de/pf/postgresql-11        sha256:1aeb133fff1848b498c5e6887629bac088fec0aef318fbee2d278a0d90af2830
docker.easydb.de/pf/postgresql-14        sha256:174855604dc22ef42c2baed8f18872392d5c599d95ad3b6709dbed5e28fbbf8e
docker.easydb.de/pf/server-base          sha256:06932d49cd4547c64732bbc255e3f0ea7410d6c6f6fa9f22d0e55f5a3d80dbae
docker.easydb.de/pf/webfrontend          sha256:9614e04f9097795ae3783217cbb9e5681f62389ced3a19263b5a114a794b32b2
```
