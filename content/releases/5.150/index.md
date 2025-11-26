---
menu:
  main:
    name: "5.150 (November 2025)"
    identifier: "5.150"
    parent: "releases"
    weight: -650
---

> Diese Version benötigt **keinen neuen** Index-Aufbau


# Version 5.150.0

*Veröffentlicht am 26.11.2025*


# Webfrontend

## Behoben

* **Geteilte Mappen:**
  * Ein Fehler wurde behoben, der auftrat, wenn versucht wurde, ein Objekt von einer Mappe in eine andere zu übertragen, während der Schnellzugriff-Suchfilter verwendet wurde
  * Ein Fehler wurde behoben durch den die Paginierung in freigegebenen Mappen nach Verwendung des Schnellzugriff-Suchfilters nicht mehr funktionierte
* **Unbekannte Custom Mask Splitters:**
  * Das Verhalten des Frontends wurde verbessert, wenn ein Mask-Splitter nicht korrekt initialisiert werden kann, was in der Regel passiert, wenn das Plugin deaktiviert ist oder abstürzt
  * Bisher wurde im Frontend eine Fehlermeldung angezeigt und die Objektdetails wurden nicht angezeigt
  * Jetzt werden die Objektdetails angezeigt und ein Platzhalter ersetzt den fehlerhaften Mask-Splitter
* **Tabellenansicht:**
  * Ein Problem wurde behoben, das zu zufälligen Fehlern in der Tabellenansicht führte, wenn Objektaktualisierungs-Ereignisse empfangen wurden


# Server

## Behoben

* **API**:
  * Checks wurden in `api/v1/db` mit `?all_versions` hinzugefügt
  * Zuvor konnten in seltenen Ausnahmefällen interne Serverfehler auftreten


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.150.0            sha256:9e02793739b8cefc199d72e023bf066413db7a7fd662ad0120298b52d4c0b528
docker.easydb.de/pf/elasticsearch:5.150.0  sha256:d05abf7bd45390c1cd707ec9008c912a47bb944a92c8ddbf3ff2cc40509f5028
docker.easydb.de/pf/fylr:5.150.0           sha256:9516b9c4a51fac32f968e34b18d1adc53846c2ff070a946a536729c7f3757f64
docker.easydb.de/pf/postgresql-14:5.150.0  sha256:62db7a5ed433a817426c49931168a0018954402fb3d3c450a59d921bc7f13416
docker.easydb.de/pf/server-base:5.150.0    sha256:4938a03a78d703c007c24a13f18204c3495d75858ecc6ca888916dc96d9da177
docker.easydb.de/pf/webfrontend:5.150.0    sha256:9a45d916bf9b71d66ca256a06474f6bd8c833dc8da9f03a2f5ce68e72711235a
```
