---
menu:
  main:
    name: "5.73 (Mitte September 2020)"
    identifier: "5.73"
    parent: "releases"
    weight: -573
---

> Es gibt einen großen Versionssprung im Elasticsearch-Container (**5.x auf 7.x**). Aus diesem Grund ist eine **Neuerstellung des Index** erforderlich. Das Upgrade erfordert im Normalfall keine zusätzlichen Schritte, im Einzelfall kann es aber zu Problemen kommen. Mehr Information findet sich im Abschnitt **[Elasticsearch 7](#elasticsearch-7)**.
>
> Ab Version **5.76** (erscheint geplant am **18.11.2020**) startet die **easydb** nur noch mit der neueren **PostgreSQL-Version 11**. Dieser Schnitt ist notwendig, um neue Funktionen von PostgreSQL nutzen zu können, ohne alte Installationen zu gefährden. Außerdem bekommt die alte PostgreSQL-Version keine Sicherheits-Updates mehr. Mehr Informationen im Abschnitt **[PostgreSQL 11](#postgres-11)**.

# Version 5.73.1

*Veröffentlicht am 24.09.2020*

## Webfrontend

*Verbessert*

* Ein konfiguriertes **Browser-Favicon** wird jetzt schon beim Login geladen und nicht erst danach.

## Server

*Behoben*

* **/api/search**: Die Suche nach Datum (nur Jahr + Jahr und Monat) wurde repariert.

# Version 5.73.0

*Veröffentlicht am 16.09.2020*

## Webfrontend

*Neu*

* Suche: Unterstützung einer **dritten Sortierebene**.
* Suche: Sortierung für **String-Felder** mit dem Typ *numerisch* ist jetzt möglich.

*Verbessert*

* Detail: Die **Auswahl der Spracheinstellungen** direkt am Textfeld ist nicht mehr möglich.
* Export: Die eigene Feldauswahl funktioniert jetzt genauer beim Ein- und Ausblenden von Feldern.

*Behoben*

* **Detailansicht**: Aktualisierungsprobleme für die Vorschauanzeige wurden repariert.
* Tabellenansicht: Verschiedene kleinere Reparaturen für die Anzeige bestimmter komplexerer Datenmodelle.
* **Metadaten-Mapping**: Kleinere Unstimmigkeiten zwischen Server und Webfrontend wurden beseitigt.
* Drucken: Ein Fehler im Druckmanager im Zusammenhang mit  verschiedenen Masken wurde behoben.
* Editor: Die Nebensucht konnte nach Verwendung der Autovervollständigung nur einmalig geöffnet werden.
* Workflows: Die Auswahlmöglichkeit von Systemgruppen bei Email-Aktionen wurde entfernt. 
* Mappen: Die automatische Erkennung von Serien und Versionen wurde für einige Fälle repariert.
* Mappen: Die **Unterstützung von Deep-Links** für angemeldete und anonyme Nutzer wurde repariert. 
* Mappen: Ein Problem im Zusammenhang mit Hochladen von Objekten, bei denen die Datei in einem verlinkten Objekt mit Pool-Management angelegt wird, wurde repariert.
* Das Nutzer-Login wird bei manuellem Login nur noch einmal geloggt und nicht zweimal.
* Filter: Die **Facettierung von Datumsbereichen** wurde verbessert, es wird jetzt diesselbe Anzahl gefiltert wie in der Aggregation angezeigt (beide System benutzten das `from`-Feld des Bereichs).

## Server

*Neu*

* /api/session/authenticate: Neuer Parameter `log_event`. Damit kann eine Authentifizierung ohne Logging durchgeführt werden.
* /api/search: **sort** unterstützt jetzt _numeric_ für Felder vom Typ **string**.
* /api/search: Für **daterange** Felder wird für Aggregationen und Suchen der Appendix `.from` und `.to` unterstützt.
* Shibboleth: Mapping von mehr Benutzerinformationen bei Anmeldungen.

*Verbessert*

* Unterstützung von **Elasticsearch 7** (von 5)

*Neu*

* Sortierung von Standard-Bildern wurde für einige Fälle in Zusammenhang mit verlinkten Objekten repariert.

* Speicherleck im Hotfolder behoben.

### Elasticsearch 7

Das Update bringt die Elasticsearch 7 mit, im Normalfall sollte es keine Probleme geben, außer wenn:

* eigene **Konfiguration** für Elasticsearch verwendet wird (Block `config` in [elasticsearch.yml](/en/sysadmin/configuration/elastic/elasticsearch.yml/)). In diesem Fall wird der `easydb-elasticsearch`-Container nicht erfolgreich starten.

* ein **Index-Template** für Elasticsearch verwendet wird (`elasticsearch.default_template` in [easydb-server.yml](/en/sysadmin/configuration/easydb-server.yml/available-variables/)). Hier könnten Fehler beim Erstellen des Indexes durch den easydb-Server auftreten.

* insbesondere falls Sie noch folgende Konfiguration verwenden, sollten Sie diesen Block entfernen und mindestens den server-container neu starten:

````yaml
  "store" : {
    "throttle" : {
      "type" : "merge",
      "max_bytes_per_sec" : "50mb"
    }
  },
````

Typischerweise findet sich dies in der Datei `/srv/easydb/config/elastic_index_template.json`.

Falls das Entfernen der zitierten Konfiguration nicht ausreicht ist ein Blick ins Log des Elasticsearch-Containers notwendig (`docker logs easydb-elasticsearch`), die Fehler dort sollten Hinweise geben, wie mit den dort verwendeten Optionen zu verfahren ist. Im Zweifelsfall ist die [Elasticsearch-Dokumentation](https://www.elastic.co/guide/en/elasticsearch/reference/7.x/settings.html) zu konsultieren .

### Postgres 11

PostgreSQL Version 11 steht für alle Kunden seit Anfang 2020 bereit und kann mit [dieser Anleitung](https://docs.easydb.de/en/sysadmin/installation/postgres-upgrade/) installiert werden. Leider ist der Prozess nicht automatisch sondern erfordert einen Linux-Administrator.

Ab **5.76** (erscheint geplant **18.11.2020**) macht der Server einen Check zur PostgreSQL-Version und startet nicht mehr, falls diese kleiner als 11 ist.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:d5f7a58adaac58a12222938ef95187f0bbdac4700131b1c3bfae21cf3ee6421e
docker.easydb.de/pf/eas                  sha256:f8e2775ad3dd8edd307ae3727813f464a9fd7d448a1c3136c09de7d6fb388284
docker.easydb.de/pf/elasticsearch        sha256:6306674fb15197ddb371cbc63827891cf4be36b33338b92026b6f3b79f9ddc03
docker.easydb.de/pf/fylr                 sha256:9eefa5355209c9fdf288f8be42887a3096a24f8ce9ff03f14a8edc9bd355ccfa
docker.easydb.de/pf/postgresql-11        sha256:47a1737d6895da0b5fe2e2d41318283a6597489e1b0fa58e299bdef533958e28
docker.easydb.de/pf/postgresql           sha256:9a2e45b364c8e9b2f68f4f5a3d945c7ac1eef00fbe1b046f108dc6cebd2ac5f8
docker.easydb.de/pf/server-base          sha256:85bc26c8f0529ca7bfa28e1b35c4570fefe807dc55150fa9c8d6e5a48e8f65e1
docker.easydb.de/pf/webfrontend          sha256:d48c782dd4a857e0abd404b8374603a623ecbaa4548632d8cfb2a867de3ad155
```
