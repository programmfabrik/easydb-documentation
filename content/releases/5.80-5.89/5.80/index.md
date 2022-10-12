---
menu:
  main:
    name: "5.80 (Ende Februar 2021)"
    identifier: "5.80"
    parent: "releases589"
    weight: -580
---

> Für dieses Release ist **kein Re-Index** nötig.

# Version 5.80.2

*Veröffentlicht am 04.03.2021*

## Server

### Neu

- **Server Environment:** der Server kann als nicht-**root**-User gestartet werden

### Behoben

- **Pool API:** der Zugriff auf `api/v1/pool` ist nicht mehr auf User mit **root**-Rechten beschränkt

# Version 5.80.1

*Veröffentlicht am 01.03.2021*

## Webfrontend

### Verbessert

- **Tabellenansicht:** für hierarchische Objekte werden nicht mehr alle Kinder automatisch aufgeklappt, wenn ein Objekt ausgewählt wird

### Behoben

- **Editor:** Masken mit Felder, die abhängig von Tagfiltern angzeigt werden, werden korrekt neu geladen, wenn Tags geändert werden
- **Expertensuche:** Tags, die nicht für die Suche aktiviert sind, werden ausgeblendet

## Server

### Neu

- **Server Environment:** die effektive UID/GID des Servers kann angegeben werden

### Verbessert

- **Custom Data Type Gazetteer:** Alte Einträge vom custom datatype Gazetteer, die das obsolete und invalide `_fulltext` Format beinhalten, können mithilfe des [Custom Datatype Updater](/en/technical/plugins/customdatatype/customdatatype_updater/#custom-data-type-updater) aktualisiert und behoben werden

### Behoben

- **Datenschutz:** Klartext-Passwörter wurden aus der Anzeige der Serverkonfiguration im Serverstatus entfernt, zudem wurde die Ausgabe der Serverkonfiguration im Log komplett deaktiviert

# Version 5.80.0

*Veröffentlicht am 24.02.2021*

## Webfrontend

### Neu

* **Benutzermanagement:** Die Lister der Benutzer kann jetzt je Spalte sortiert werden.
* **Editor:** Verlinkte Reverse Objekte können manuell sortiert werden.
* **Suche:** Sortieren nach reverse verlinkten Objekten.
* **Export:** Ein neuer `all_languages`Parameter erlaubt das Exportieren aller Datenbanksprachen jetzt auch für `XML`.

### Verbessert

* **Maskenmanagement:** Die Feldbreite kann jetzt auch für die Textansicht eingestellt werden.

* **Typo3-Plugin:** Beim Export werden jetzt alle konfigurierten Sprachen übernommen, nicht nur die eingestellten Sprachen des Nutzers.

* Grafische Verbesserungen in den meisten Ansichten.
* **Ereignismanager:** Sortierung wurde verbessert.
* **Detail/Editor:** Mehrfachfeldern werden jetzt Serverseitig sortiert.
* **CSV-Importer:** Das Löschen von Tags ist jetzt möglich.

### Behoben

* **Präsentation:** Der Umschalter zum Anzeigen von Standard-Info wurde repariert.

* **Detail:** Im Zoomer hat der `100%`-Button manchmal nicht korrekt funktioniert.
* **Editor:** Kopieren und sofortiges Schließen des Editors wurde repariert.
* **Experten-Suche:** Die Suche mit Bereichsangaben wurde repariert.

## Server

### Neu

* **/api/db:** Unterstützung von manuellem sortieren von reverse verlinkten Objekten.
* **/api/export:** Ein neuer `all_languages`Parameter erlaubt das Exportieren aller Datenbanksprachen für alle Formate.

### Verbessert

* **/api/.../list:** Diese Endpoints sind jetzt nur noch für Nutzer mit `system.root`-Recht erreichbar. Zuvor wurden Objekte je nach Sichtbarkeit gefiltert bevor das Ergebnis zurückgegeben wurde. Damit haben`offset` und `limit` nicht wie erwartet funktioniert.
* Performance-Verbesserung beim Laden von Mappen und Rechten (z.B. auch beim Speichern eines Pools)

### Behoben

* **/api/export:** URLs im CSV-Export wurden repariert.
* **/api/user/list:** Ausgabe von `_automatic_auth`wurde repariert.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:15e82b1a80281b83372c92b0ace52f343bc9eb8457497a76843f3ec8650af8d9
docker.easydb.de/pf/eas                  sha256:fceaf1329c063c6bc6ae8d37e2c2df5076d9aa0d8e2e0f0bf3e51469afd59f7a
docker.easydb.de/pf/elasticsearch        sha256:34843553d665c05e684a5a8c65372c61f232bb3ff5de0767da769b6bb72f99e5
docker.easydb.de/pf/fylr                 sha256:7c1b6949957fa32c9dd90f0710b92b109dd2b298c03aa6d7f5f665eb68594602
docker.easydb.de/pf/postgresql-11        sha256:8c9ac649827eec7cdb080cd2ffb5fcc865066093e95c196f0e529e91a3b07ce5
docker.easydb.de/pf/server-base          sha256:c4a1caddffc7dd2b72789cf5d692c673af34a59eb0ddcd3580d1428925e8257a
docker.easydb.de/pf/webfrontend          sha256:42236f2fe0303e88bf3bb75f1438dc3b364dd93356b5ac63f6f0f5bf76871071
```

Programmfabrik GmbH

