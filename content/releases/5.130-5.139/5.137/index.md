---
menu:
  main:
    name: "5.137 (Anfang Oktober 2024)"
    identifier: "5.137"
    parent: "releases5130"
    weight: -637
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.137.1

*Veröffentlicht am 10.10.2024*

# Webfrontend

## Behoben

* **Gruppeneditor**: unnötige Fehlermeldung nach erfolgreichem Lauf unterdrückt
* **Login**: Nutzer wird nicht bei jedem Login gespeichert
* **Tabellenansicht**: Javascript-Fehler behoben

# Version 5.137.0

*Veröffentlicht am 02.10.2024*

# Webfrontend

## Neu

- **Neuer Dialog zum Hochladen überspringen:** Fügt eine neue Option im Dialog für neue Objekte hinzu, um das Konfigurationsfenster zu überspringen, wenn der Dialog für neue Objekte das nächste Mal geöffnet wird

## Verbessert

- **Hierarchie Tooltip:** Den Hierarchie-Handles wurde ein Tooltip hinzugefügt, der darauf hinweist, dass es möglich ist, die gesamte Hierarchie mit einem Shortcut zu erweitern
- **Lokalisierung des Kalenders:** Verbesserungen am Kalender hinsichtlich der Lokalisierung vorgenommen
- **Serveraufrufe für PDFs mit Bildern:** Unnötige Serveraufrufe beim Drucken von PDFs mit Bildern wurden reduziert
- **Leaflet-Bundle:** Die Leaflet-Bibliothek wurde direkt in das Frontend-Bundle aufgenommen, um eine zusätzliche Anfrage des Frontends zu vermeiden, um die Bibliothek zu erhalten
- **Deep Link:** Wenn ein Deep Link zu einem Datensatz geöffnet wird, wird dieser nun immer in der Hauptsuche angezeigt
- **Tags:** Verbesserte Tooltips für Tags in der gesamten Anwendung, wodurch diese Funktionalität in der gesamten Anwendung konsistenter ist
- **Migrationen:** Verhindert einen schwerwiegenden Frontend-Fehler, wenn der Server nicht `frontend_locale` und `database_locale` in den Session-Daten enthält
  - Dies kann passieren, wenn Instanzen geöffnet werden, die aus der easydb5 migriert wurden
  - Behebt auch Probleme mit benutzerdefinierten Metadatenfeldern in Mappings, die von anderen Instanzen migriert wurden
- **Verzeichnis-Upload:** Schließt `.DS_Store`-Dateien beim Hochladen von Verzeichnissen im neuen Objektmodal aus
- **CSS:** Allgemeine Anpassungen und Verbesserungen wurden am CSS der Anwendung vorgenommen

## Behoben

- **Versteckte Tags:** Das Verhalten von Tags, die gleichzeitig als versteckt und als Standard konfiguriert sind, wurde korrigiert
  - Jetzt werden diese Tags automatisch hinzugefügt, auch wenn sie versteckt sind
  - Zuvor wurden diese Tags ignoriert
- **Filter-Panel:** Mehrere Probleme im Filter-Panel im Zusammenhang mit der Verwendung des neuen `AND/OR`-Systems wurden behoben
- **Gespeicherte Suchen:** Es wurde ein Fehler behoben, wenn versucht wurde, Tag-Facetten aus gespeicherten Suchen wiederzuverwenden
- **Datums-Experten-Suchfelder:** Platzhalter für Datumsfelder in den Experten-Suchoptionen des Changelogs hinzugefügt
  - Zuvor waren diese Platzhalter nicht lokalisiert.
- **Datumsfilter:** Die Option zur Verwendung des Operators `AND` in Datumsfeldern, die sich nicht in einer verschachtelten Tabelle befinden, wurde entfernt
- **Datumsfelder:** Ein Problem wurde behoben, das auftrat, wenn versucht wurde, eine nicht unterstützte Sprache in Datumsfeldern auszuwählen
- **Aktualisierung von Mappen:** Es wurde ein Problem behoben, bei dem offene Mappen nicht korrekt aktualisiert wurden, wenn ein Objekt hinzugefügt oder entfernt wurde
- **Ereignisabfrage im Entwicklerbereich:** Der Selektor für die Auswahl des Abfragetyps im Entwicklermenü wurde korrigiert
- **Benutzermanager:** Das Verhalten des Benutzermanagers, wenn keine Berechtigung zum Lesen eines Objekts verfügbar ist, nachdem es gespeichert wurde, wurde korrigiert.
  - Jetzt aktualisiert der Manager die Liste der Benutzer und löscht die Detailansicht
- **Verknüpfte Objekte:** Ein Problem wurde behoben, bei dem ein Datensatz nicht gespeichert werden konnte, wenn ein nicht sichtbares verknüpftes Objekt als erforderlich markiert war
- **Filter-Panel:** Es wurde ein Fehler behoben, bei dem die Schaltfläche "Mehr anzeigen" in hierarchischen Filtern nicht korrekt angezeigt wurde
- **`AND/OR`-Schalter:** Der `AND/OR`-Schalter wird jetzt nicht mehr angezeigt, wenn diese Modi nicht tatsächlich verwendet werden
  - Dadurch wird verhindert, dass der Schalter in Filtern angezeigt wird, in denen er nicht sinnvoll ist.
- **Mehrfachfeldstrukturen:** Ein Fehler wurde behoben, bei dem komplexe geschachtelte Mehrfachfelder ohne Feldnamen dargestellt wurden

# Server

## Verbessert

- **AI Auto Keyworder:** nicht mehr benötigte Einstellungen für die Verbindung zu Cloudsight wurden entfernt
  - Dieses Feature ist als Teil des [Auto Keyworder Plugins](/de/webfrontend/administration/base-config/auto_keyworder/) verfügbar


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.137.0            sha256:a55e9a53ce0b9f64a997936c5f1419125825a036cd15bf0140e8b1080870c529
docker.easydb.de/pf/elasticsearch:5.137.0  sha256:72822a7cdfa41ecbe044e6fce90f2b2400db62f71fd9233e0d5845b0c7601823
docker.easydb.de/pf/fylr:5.137.0           sha256:cde9a84dca0dd2ee1ff3a2a3e22cb423c60344562b2ed6a1487c490ae0c892ad
docker.easydb.de/pf/postgresql-14:5.137.0  sha256:cb42e48f794a18309ba94e9bd24839b0b0d888d8e28865d0c3e80b8aef87844c
docker.easydb.de/pf/server-base:5.137.1    sha256:58a09eac5f78731aaacf7e6c31461eca1db2def72299c50bad1824fa37abb19d
docker.easydb.de/pf/webfrontend:5.137.1    sha256:4ab8a05b9b3ac1227cd49a7347cd4dc5a2d536dd3968b99212ee0a9affcedc01
```
