---
menu:
  main:
    name: "5.90 (Ende September 2021)"
    identifier: "5.90"
    parent: "releases599"
    weight: -590
---

> Dieses Release **beinhaltet ein neues Elastic-Docker-Image** (Version **7.15.0**). Wir hatten in den letzten Releases eine Version von Elastic ausgeliefert die einige unangenehme Performance-Eigenschaften hatte, so waren die Aggregationen (Filter) teilweise sehr langsam. Diese Problem sollten mit der **7.15.0** nun gelöst sein. Wir wissen nicht genau seit wann die Elastic diesen Performance-Einbruch hatte, sicher wissen wir das **7.10.0** noch ok war.

> Diese Version **benötigt keinen neuen Index-Aufbau**, das neue Elastic-Image arbeitet mit den vorhandenen Index-Dateien.

> In dieser Version werden vorbereitend **ungenutzte Dateien im System** markiert. Das erfolgt durch das Setzen einer negativen EAS-ID. In der Folge sind diese Assets nicht mehr für den Server verfügbar und würden bei einem Zugriff einen Fehler melden. Es werden aktuell noch keine Dateien tatsächlich gelöscht, das kommt in einer der nächsten Versionen.

# Version 5.90.2

*Veröffentlicht am 14.10.2021*

## Webfrontend

### Verbessert

- **Performance**:
  - Nutzung von Caching für `api/v1/l10n/user/CURRENT` Requests

### Behoben

- **Editor**: Speichern von Objekten wird verhindert, solange der Request zum Speichern nicht komplett ist und die Objektdaten im Editor geladen wurden. Dadurch wird ein inkonsistenter Stand zwischen dem Editor und der aktuellsten Objektversion im Server verhindert.

## Server

### Verbessert

- **Performance**:
  - Requests zu `api/v1/l10n/user/CURRENT` werden gecached
  - Geschwindigkeit des Eventpollings erhöht

# Version 5.90.1

*Veröffentlicht am 11.10.2021*

## Webfrontend

### Verbessert

- **Performance**:
  - eine verkleinerte Version des Webfrontend-Javascript wird verwendet, um die Ladezeit zu verkürzen
  - verbesserte Nutzung von Caches für `api/v1/objecttype`

### Behoben

- **Editor für neue Objekte**: Probleme mit fehlender Pool-Auswahl für verknüpfte Objekte behoben
- Bugfix bei der Facettierung von Tags
- Bugfix für mögliche Probleme beim Neuladen beim Löschen von verknüpften Objekten

## Server

### Verbessert

- **Performance**:
  - verbesserte Nutzung von Caches:
    - Requests für das *CURRENT* Schema und Maskset werden zwischengespeichert, um die Zeit für wiederholte Anfragen drastisch zu reduzieren
    - Cache Headers für Requests zur base db werden verwendet
  - Antworten für das *CURRENT* Schema und Maskset werden komprimiert

# Version 5.90.0

*Veröffentlicht am 29.09.2021*

## Webfrontend

### Verbessert

* **Nebensuchen**: Bei gefilterten hierarchischen Nebensuchen ist es jetzt nicht mehr möglich übergeordnete Objekte auszuwählen die nicht vom Filter erfasst werden, wohl aber zur Darstellung der Hierarchie benötigt werden. Solche Objekte sind ausgegraut markiert.

### Behoben

* **CSV-Importer**: Ein Update-Problem im Zusammenhang mit Hierarchien wurde repariert.
* **CSV-Importer**: Ein Problem mit Objekttypen ohne verfügbare Tags wurde behoben.
* **Editor**: Der Speichern-Button war in seltenen Fällen aktiviert, ohne dass ein Speichern erlaubt war.

## Server

### Neu

* Unterstützung von Apples `HEIC` Datei-Format (**High Efficiency Image File Format**).
* **/api/objects**: Versionszugriff nach Datum wurde implementiert.

### Verbessert

* **Easydb-Asset-Server**: Der Python-basierte Server zum Management der Dateien läuft jetzt mit Python 3 und nicht mehr mit Python 2.7.

### Behoben

* **/api/db**: Der Zugriff auf gelöschte Objekte wird jetzt blockiert.
* **/api/schema**: Anlegen eines Datei-Feldes mit einem Namen der zuvor schon einmal existiert hat wurde repariert.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:b5fe29ee03c23bea847c4333ad8d675ed333d51834ce8ee5855072e213a4a5c8
docker.easydb.de/pf/eas                  sha256:ca4eae963eae7986706ce66dac3bb5c2de6fd05672086dcb2810b6378ada8cd3
docker.easydb.de/pf/elasticsearch        sha256:81314bcaa640d8a366733a242c6902aaee32b4aaadfa2be86999a6ddc266c5e3
docker.easydb.de/pf/fylr                 sha256:cad5248dab0ddaddb7d93aa0f53a580507963636922b14d42ef259c73cfcad4e
docker.easydb.de/pf/postgresql-11        sha256:7d4565382d4ac1beb9d1ef7a9b97800605a9f8bfef34210e66531bb7c9f68045
docker.easydb.de/pf/server-base          sha256:e6eab654b35a4296c775f1a3eb11ccf4e9a4720994841881389185b1e8c0ee71
docker.easydb.de/pf/webfrontend          sha256:cb263dce2325534d1b848ac9914346967d22d4672ecf1305ed621e5b68ea0fe0
```
