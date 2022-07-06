---
menu:
  main:
    name: "5.102 (Ende Juni 2022)"
    identifier: "5.102"
    parent: "releases"
    weight: -602
---

> Diese Version **benötigt keinen neuen Index-Aufbau**

# Version 5.102.1

*Veröffentlicht am 06.07.2022*

# Webfrontend
## Behoben

* von externem Plugin verwendete interne Funktion korrigiert
* Vorlage im Editor für Zeitraum-Felder korrigiert

# Server
## Behoben

* Fehler beim Schema-Upgrade behoben
* Metadaten-Mapping beim Export korrigiert

# Version 5.102.0

*Veröffentlicht am 29.06.2022*


# Webfrontend

## Neu

* Die Deeplink URL für Objekte wurde geändert. Jetzt wird die `UUID` anstelle der `ID` des Objekts verwendet. Alte URLs, die die `ID` verwenden, funktionieren weiterhin
* **Metadaten Mapping**: Unterstützung für Custom Data Typen
* Neue Option im Objekttyp-Manager, um dynamisch neue Menü-Buttons für Listen von Objekttypen hinzuzufügen. Diese zeigen direkt Listen der jeweiligen Objekttypen an

## Verbessert

* Im Datenmodell werden die internen Namen und Masken neben den lokalisierten Namen in der Listenansicht angezeigt
* Die Ansichtseinstellungen für Mappen werden gespeichert
* Im Datenmodell-Editor wird jetzt bei der Option "Bereich" bei einem Pflichtfeld ein Info-Tag für das Feld angezeigt
* Es wurde ein neues internes Attribut in Datumsbereichsspalten hinzugefügt, wenn die textuelle Darstellung aktiviert ist. Es wird verwendet, um die vom Benutzer eingegebene Textdarstellung beizubehalten, anstatt sie durch die automatische Textdarstellung zu ersetzen
* Datumsbereichsfelder mit aktivierter Textdarstellung erlauben ein offenes Von/Bis-Datum bei Verwendung der Wörter "nach" und "vor"
* Start der Filterung, wenn mindestens ein Zeichen im Filter enthalten ist
* Die Filter-Checkbox für Zahlenfelder im Maskeneditor wurde entfernt
* Speichern der ausgewählten "Filter" beim Speichern einer Suche
* Erlaubt das Hinzufügen neuer Tags zu einem Objekt, was dazu führen würde, dass der Benutzer nach dem Speichern seine Berechtigungen verliert

## Behoben

* Ein Fehler wurde behoben, bei dem in manchen Situationen die Prüfung auf Asset-Duplikate einen leeren Datensatz erzeugte
* Im Ereignismanager ist die Schaltfläche "Anzeigen" nicht sichtbar, wenn es sich um ein Ereignis für einen gelöschten Datensatz handelt
* Der Asset-Browser zeigt die Wasserzeichenversion von Bildern an, wenn das Bild zu klein ist. Die Wasserzeichenvorschau wird nur noch angezeigt, wenn keine andere Version verfügbar ist
* Der Dateinamensvorschlag (für "Datei"-Felder) in der Expertensuche wurde korrigiert und ein neuer interner Parameter in der API hinzugefügt
**Such-Token**: Die Anzeige des vorgeschlagenen Tokens bei mehreren Tokens in der Expertensuche wurde korrigiert
* Problem bei der Verwendung der Funktion "Dive" von hierarchischen Objekten in den Suchergebnissen bei Verwendung des Connector-Plugins behoben
* Problem im Gruppeneditor behoben, das auftrat, wenn ein mehrsprachiges Textfeld verschachtelt war

# Server

## Neu

* **Datenmodell**: der Feldtyp `daterange` (Datumsbereich) hat ein neues mehrsprachiges Textfeld, um freien Text mit den Datumswerten zu speichern

## Verbessert

* **Suche**: Sub-Felder für Datumsbereichsfelder (`.from`, `.to`) können zum Suchen und Sortieren verwendet werden
* **Event Polling**: `API_PROGRESS`-Ereignisse haben ein begrenztes Info-Objekt, wenn Ereignisse abgefragt werden. Kein anderer Ereignistyp hat ein Info-Objekt für die Abfrage
* **/api/v1/db**: weitere Verbesserungen für `all_versions=true` (Bulk-API in Vorbereitung für Migrationszwecke)

## Behoben

* **Datenmodell**: Umbenennung von mehrsprachigen Textfeldern korrigiert
* **CSV-Export**: Export von URLs von Asset-Versionen korrigiert und umstrukturiert (ausgewählte Versions-URLs aus dem Export-Dialog werden berücksichtigt)
* Benutzerbild im Benutzerdialog wurde manchmal entfernt, dies wird jetzt vermieden

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:ba4c705b074e7752c90edb6397cf405ca34030e9f58dc95750dd7d3b94e4a488
docker.easydb.de/pf/eas                  sha256:27a523e91a9321d10896019c4f002ebdd9b88b9e448ac7a1b42dd14379687291
docker.easydb.de/pf/elasticsearch        sha256:2e3fa619198a63ae432fd4cb25d295e7e017563186c5c5a42c3f0fdba2ef20f8
docker.easydb.de/pf/fylr                 sha256:a501864a51611ca067fcaaccbcec0395aa3853ac5442fb2d14c0bbfbb5284b74
docker.easydb.de/pf/postgresql-11        sha256:da6ab72d9726b921e55121ed9329c1a236b5922db531e73a23bb042c36c45251
docker.easydb.de/pf/postgresql-14        sha256:53d1e9cff20dc6d942fbb9f9abb0410cf6a09d522f4aa7258b0659195cb6108e
docker.easydb.de/pf/server-base          sha256:d338ebabe00ee81cd62363bda4164d2ba1e6960b4d6c100c5647a468d1f31a13
docker.easydb.de/pf/webfrontend          sha256:4e40150a6f17092b8be6365d51bb8fc3844e36766ed6c76826891e52e74c7a2f
```
