---
menu:
  main:
    name: "5.145 (Ende Juni 2025)"
    identifier: "5.145"
    parent: "releases"
    weight: -645
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

# Version 5.145.0

*Veröffentlicht am 25.06.2025*


# Server

## Verbessert

* **Dateidownload**: das interne Verhalten des Exports wurde angepasst, so dass der Download einer spezifischen Datei-Version möglich ist

## Behoben

* `api/v1/db` mit `all_versions=true`:
  * Falsche Reihenfolge von Einträgen in Mehrfachfeldern (nested tables) behoben
  * In älteren Versionen von Datensätzen war diese Reihenfolge nicht definiert und nicht stabil
  * Die Einträge werden jetzt immer in der richtigen Reihenfolge der jeweiligen alten Version des Datensatzes ausgegeben

# Webfrontend

## Behoben

* **Detailansicht**: Fehler behoben, bei dem nicht die korrekte Maske verwendet wurde, und Daten in einer falschen Maske angezeigt wurden
* **Speichern von Einstellungen**:
  * Bug behoben, der die `savePrefs` Methode deaktivierte, wenn die Einstellungen einer Nutzer-Session nicht geladen werden konnten
  * Dies hatte Auswirkugnen korrekte Verhalten des Formulars zur Registrierung von Nutzern
* **Filteransicht**: Fehler behoben, der auftrat wenn der Filter ohne Aggregationen ausgeführt wurde


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.145.0            sha256:fa31b022f424f3ac9733f1fbd3a4f4526addd4580b7333190b1f3c2c7a0bbd4d
docker.easydb.de/pf/elasticsearch:5.145.0  sha256:833dbbdf2056989c4ebb78e4f64762802dc85b5400705bc32d6d5c301b6f41fd
docker.easydb.de/pf/fylr:5.145.0           sha256:b6389af0155a070870340206353d21a65314086f845ff02571daa21a4439534a
docker.easydb.de/pf/postgresql-14:5.145.0  sha256:1251dc9510977ec5b80d70d306ec7287c70e63f9af0677551ff2e012b46010da
docker.easydb.de/pf/server-base:5.145.0    sha256:4e62ebaf08563f85c3b5ff3c5c68a33a2eafb7cf0bfae7e4120f610594f8fd78
docker.easydb.de/pf/webfrontend:5.145.0    sha256:0dddfe53ff09aaed380ad9b51253cea5643114aca715d4771f8bb2626683ca07
```
