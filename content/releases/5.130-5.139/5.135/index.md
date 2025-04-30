---
menu:
  main:
    name: "5.135 (Juli 2024)"
    identifier: "5.135"
    parent: "releases5130"
    weight: -635
---

> Diese Version benötigt **keinen neuen** Index-Aufbau

> Der `pf/chrome` Container wird ab sofort nicht mehr benötigt und ist nicht mehr Teil der Releases. Die Aufgaben werden jetzt vom `pf/fylr` Container übernommen.
>
> Das alte `pf/chrome` Container Image kann entfernt werden.


# Version 5.135.0

*Veröffentlicht am 24.07.2024*


# Webfrontend

## Verbessert

* **Suche**:
  * Die Option "nicht gesetzt" für das Parent-Feld in hierarchischen Objekten in der Expertensuche wurde entfernt. Um nach Objekten ohne Elternteil zu suchen, kann die Schaltfläche "Optionen" verwendet werden
  * Die Funktionalität der Listensuche sowie die Darstellung der hierarchischen Listenergebnisse in der Hauptsuche wurde deutlich verbessert
* Verbesserte Oberfläche des Sortierfeldes
* Verbessertes Layout des Bereichs "Mehr..." in den Suchfiltern
* Die Basetype-Manager wurden so verbessert, dass die aktive Registerkarte beim Speichern eines Elements erhalten bleibt
  * Dies bedeutet, dass nach dem Speichern eines Elements, z.B. eines Pools, die aktive Registerkarte auf dem Bildschirm sichtbar bleibt
* **Zoomer**:
  * Der Zoomer wurde verbessert, um übermäßige Serveraufrufe beim Zoomen zu vermeiden
  * Diese zusätzlichen Aufrufe führten zum Blockieren des Servers und verlangsamten den Zoomer

## Behoben

* **CSV-Importer**: Es wurde ein Fehler behoben, wenn versucht wurde, Zahlenfelder als Identifier-Felder zu verwenden, um verknüpfte Objekte zu erstellen
* Ein Problem beim Sortieren nach der Änderungshistorie wurde behoben
* Es wurde ein Problem behoben, das beim Senden von leeren Werten in der Basiskonfiguration anstelle von Standardwerten auftrat
* Fehler bei der Verwendung großer Datumswerte v.Chr. in Datumsbereichsfeldern behoben
* Korrigierte Überprüfungen in Feldern vom Typ Datumsbereich
* Fehler in der Rechtevorgabenverwaltung behoben
* Behebung eines Problems beim Kopieren von Objekttypen, die als bidirektional konfigurierte Felder enthalten
* Behebung eines Fehlers, bei dem der Mappen-Manager nach dem Hinzufügen einer neuen Mappe zu lange brauchte, um zu reagieren


# Server

## Behoben

* **PDF Creator**: fehlgeschlagene PDF-Datei-Erzeugung wurde behoben, indem ein anderer Docker-Container diese Aufgabe übernimmt
* URL Weiterleitungen nach `/api/objects`: Probleme mit Dateinamen durch Nutzung von percent-encoding behoben


# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/eas:5.135.0            sha256:7c497989191305d99c0da3dd2ef1bcf1a491c7e21c488a2a8c7985604b99dea1
docker.easydb.de/pf/elasticsearch:5.135.0  sha256:1d6640f903d68b06660b873186330f533171e59f67725c8dc5cd127c528317d9
docker.easydb.de/pf/fylr:5.135.0           sha256:2f5ada17c5d66875717dd218b7330f94450f15df5c87c54a74eb082058165012
docker.easydb.de/pf/postgresql-14:5.135.0  sha256:f8166da72c3cbcc17f972363c670ac7da80511639d0aaf0dc7857c6cfe006566
docker.easydb.de/pf/server-base:5.135.0    sha256:62e245851f52149f412e9bdcb144cd2d599c8aca503b00c3c2628f9800ebb9e2
docker.easydb.de/pf/webfrontend:5.135.0    sha256:110231137b690b25a944e8a65d156a7a45ba9240d1425b81a4dd2324b9fcc11c
```
