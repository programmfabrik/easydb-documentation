---
menu:
  main:
    name: "5.79 (Februar 2021)"
    identifier: "5.79"
    parent: "releases579"
    weight: -579
---

> Für dieses Release ist **kein Re-Index** nötig. 

# Version 5.79.1
*Veröffentlicht am 10.02.2021*

## Webfrontend

### Verbessert

* **Suche**: Suchtyp kann bei kommagetrennter Eingabe getrennt für die einzelnen Terme bestimmt werden.

### Behoben

* **Export**: "Dateien"-Tab immer sichtbar, wenn Dateien exportiert werden können.
* **Datenmodell-Editor**: unnötige Typauswahl bei Nested-Tabellen entfernt.

## Server

### Behoben

* Sessions archivierter Nutzer werden gelöscht. Das verhindert auch Fehler bei Abfrage dieser Sessions.
* Fehler beim Speichern des Ereignisses nach dem Senden einer E-Mail behoben.
* Collections von SSO- und LDAP-Nutzern werden beim Löschen auch entfernt (wie bei easydb-Nutzern).

# Version 5.79.0

*Veröffentlicht am 03.02.2021*

## Webfrontend

### Neu

* **Gruppenmanagement**: Konfiguration der Nutzer-Pseudonymisierung ergänzt.

### Verbessert

* **Maskenmanagement**: Option zur Anzeige von verlinkten Objekten wurde vereinfacht.
* **Usermanagement**: Anzeige der Email für Nutzer ohne Login in der Tabelle.
* **Suche**: Beschleunigte Anzeige von verlinkten Objekten im Suchschlitz.
* **202-Prozess**: Unterstützung von vertikal angeordneten Formularen (wird aktuell nur FYLR benutzt).
* **Rechtemanagement**: Kontextbezogene Anzeige von Objekttypen-Listen in Pool, Collections, Systemrechten und Workflows. 

### Behoben

* **Mappen**: Löschen von nicht mehr erreichbaren Connector-Objekten ist nun möglich.
* **Mappen**: Verbesserte alphabetische Sortierung der Darstellung. 
* **Datenmodell**: Das Speichern von multiplen Bidi-Paaren auf Top-Level-Ebene wird nun unterbunden.
* **Suche**: Ein Doppelklick auf ein ausgewähltes Objekt bei geschlossener Sidebar konnte u.U. das falsche Objekt im Detail öffnen.
* **Grafische Korrekturen**: Editor, Suchanzeige verlinkter Objekte mit Bild, weiße Tags auf weißen Grund.
* Ladefehler bei Datenbanken mit fehlendem Logo behoben.
* **Tags**: Sichtbarkeit in Detail und Editor je nach Einstellungen wurde repariert.
* **Suche**: Fehlerbehebung bei der Anzeige von hierarchischen Objekten.
* **Detail**: Anzeige von Deep-Links im Teilen-Menü im Versionen-Dialog wurde behoben.
* **Usermanager**: Unterstütztung von CSV Runter- und anschließendem Hochladen wurde repariert.

## Server

### *Neu*

* **Usermanagement**: Archivierte und anonyme Nutzer können zeitgesteuert gelöscht werden.
* **/api/user**: Neuer Parameter `delete_policy`. 
* **Ereignisse**: Für das Automatisches Löschen von temporären Ereignissen ist jetzt eine Lebensdauer konfigurierbar. 
* **Mappen**: Die PIN-Code-Eingabe wird für Nutzer vom Typ *email* und *collection* jetzt für jede neue Session erzwungen.

### Verbessert

* **Usermanagement**: Die Konfiguration für die Pseudonymisierung ist jetzt bei den Gruppen, nicht mehr in der Basis-Konfiguration.
* **Poolmanagement**: Beschleunigung beim Speichern mit Tags und vielen Mappen.

### Behoben

* **Indexer**: Archivierte Nutzer werden nicht mehr indiziert (was zu einem Fehler im Log führte).

## Plugins

### GVK-Plugin

* Der zu Grunde liegende Dienst wurde von der alten GVK-Schnittstelle auf die neue k10plus-Schnittstelle geswitched. Das heißt, dass jetzt wieder der neuste Stand der Datenbank genutzt wird. Sonst ändert sich nichts, das drückt sich aber in den Labels aus und es gibt wieder den jeweils aktuellsten Stand und somit auch wieder die aktuellsten Bücher...

### Hotfolder

* Geschwindigkeitsverbesserung durch Batching.

### Auto-Keyworder

* Speicherleck bei Verbindungen wurde repariert.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:15e82b1a80281b83372c92b0ace52f343bc9eb8457497a76843f3ec8650af8d9
docker.easydb.de/pf/eas                  sha256:5fea450226eeccf8b3208795c5905dc45f1f4e0d78bcb8b553be2cc2d8002fe2
docker.easydb.de/pf/elasticsearch        sha256:34843553d665c05e684a5a8c65372c61f232bb3ff5de0767da769b6bb72f99e5
docker.easydb.de/pf/fylr                 sha256:7c1b6949957fa32c9dd90f0710b92b109dd2b298c03aa6d7f5f665eb68594602
docker.easydb.de/pf/postgresql-11        sha256:8c9ac649827eec7cdb080cd2ffb5fcc865066093e95c196f0e529e91a3b07ce5
docker.easydb.de/pf/server-base          sha256:9d92575b7bfdb5687a5cb7dacaf0ee1ca4ecab6de8739acd26cf4ff0d5b59f17
docker.easydb.de/pf/webfrontend          sha256:664ad1d569fc2c81fb8362cae9366bfbbd3335362b7108dec0fabf96d902719e
```

