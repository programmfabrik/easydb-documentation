---
menu:
  main:
    name: "5.71 (August 2020)"
    identifier: "5.71"
    parent: "releases579"
    weight: -571
---

>Dieses Release benötigt **keinen Re-Index**.

# Version 5.71.3

*Veröffentlicht am 14.08.2020*

## Webfrontend

*Behoben*

* Verschiedene Problembehebungen für die neue **Tabellenansicht** insbesondere im Zusammenhang mit Hierarchien und Reverse Objekten.
* Bei bestimmen Rechtemanagement-Einstellungen wurde die **Detail-Ansicht** für einige Nutzer nicht geladen. 

# Version 5.71.2

*Veröffentlicht am 11.08.2020*

## Webfrontend

*Behoben*

* Die neue **Tabellenansicht** hat in Mehrfachfeldern zuviele Felder angezeit.
* **Editor**: Anzeige von Fehlern im Formular wurde grafisch repariert.

# Version 5.71.1

*Veröffentlicht am 06.08.2020*

## Webfrontend

*Behoben*

* Freigabe von Mappen bei ungewöhnlichen **email**-Nutzern behoben.

## Server

*Behoben*

* Fehler beim Datenbank-Upgrade auf relativ alten Datenbanken behoben.

# Version 5.71.0

*Veröffentlicht am 05.08.2020*

## Webfrontend

*Neu*

* **Suche**: In der Suche wurde die Tabellen-Ansicht vollständig überarbeitet und neu gestaltet.

*Verbessert*

* Auf- und Zuklappen des **Schnellzugriffs** erfolgt jetzt über einen Button.

*Behoben*

* Fehlerbehebung im **User-CSV-Importer** in Zusammenhang mit Loginnamen und Groß- und Kleinschreibung.
* **Single-Sign-On**: Anzeige von mehr Informationen bei Login-Fehlern repariert.
* Die Anzeige gespeicherten Suchen war für einige Nutzer fehlerhaft.
* Korrekte Auswahl des Objektes wenn innerhalb von ausgewählten Objekten der Editor aufgerufen wird.

* Nutzer ohne Zugriff auf die Suche bekommen keine gespeicherten Suchen mehr angezeigt.

## Server

*Neu*

* Beim Einloggen von Nutzern über SSO (Single-Sign-On) oder LDAP werden die Nutzerinfos (Email, Name, Gruppen) aktualisiert. Zuvor wurden diese Informationen nur beim ersten Login übertragen.

*Verbessert*

* SSO: Wenn es beim Einloggen Fehler gab werden diese nun besser auf der SSO-Fehlerseite dargestellt.
* **Beschleunigung von Logins bei Connector-Partnern** durch Parallelisierung der Requests.
* Vorbereitungen für den neuen Asset-Janitor.

*Behoben*

* Datenmodellaktualisierungen führen seltener zu Dead-Locks in der Datenbank.
* Metadatenmapping für Daten wurde für einige Fälle korrigiert.
* Verbesserte Neu-Indizierung bei Aktualisierungen in Bidirektionalen Top-Level-Objekten.
* **Email**: Die im Workflow hintergelegte konfigurierbare Nachricht wird jetzt auch in die Email geschrieben.
* Fehlerbehebungen im Hotfolder.
* Verbesserte Behandlung von UTF-8 im Gazetteer-Plugin.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome        sha256:c797ded5694f320a2804eec746211ebb754c0506cd789063adcb4158a21e8a34
docker.easydb.de/pf/eas           sha256:2dc74cfe0e98999ef33016ff260a8817cc054e103a9d0215230b0de0a7a97568
docker.easydb.de/pf/elasticsearch sha256:bc1158ab95899270c04aa5e2e12fcfb6d386ac0db8ce90ce7cd68c0213ff25a3
docker.easydb.de/pf/fylr          sha256:f7edb6660514be738abf4b0c92cb3c605cce057be6b47475717b7de8b229643f
docker.easydb.de/pf/postgresql-11 sha256:28652aa27b33f768ca4faad084c65cea8fceddb274b99f93a1e583317c66241f
docker.easydb.de/pf/postgresql    sha256:4fa479c79d9d84553aa0c02a3c69ead4d1dbaed7567c01a662cf1717c101f4b2
docker.easydb.de/pf/server-base   sha256:4ae1067598b93196de7dacf422f8276027094fca8009251d5eae00ac44853220
docker.easydb.de/pf/webfrontend   sha256:0a29e6575a92b208ff6824109d51de93dc8de7f1f6eadfc061dee481404d6289
```

