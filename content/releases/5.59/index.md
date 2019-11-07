---
menu:
  main:
    name: "5.59"
    identifier: "5.59"
    parent: "releases"
    weight: -559
---

# Version 5.59.0

*Veröffentlicht am 06.11.2019*

### Webfrontend

*Neu*

* **Zeitpläne** können jetzt mit Zeitzone gespeichert werden. Ältere Versionen der easydb nehmen hier immer **UTC**, so dass Zeipläne die um Mitternacht beginnen sollten im Sommer tatsächlich um 02:00 starteten.
* Unterstützung von **tiefenhierarischen Objekt-Export** für XML (maximale Tiefe einstellbar in der Basis-Konfiguration).

*Verbessert*

* **Kopieren von Rechten** ist stabiler beim Kopieren von Maskenrechten.

*Behoben*

* Fix für Markierung bei der **Autovervollständigung**.
* Verbesserung von **Cookiebehandlung** beim Speichern von Nutzereinstellungen für die Detailansicht.

### Server

*Neu*

* **XML-Export** unterstützt `merge_max_depth`zum tiefenhierarhischen Rendern von Objekten.
* Zeitzonenunterstützung für Zeitpläne.
* Beim **Speichern von Mappen** werden jetzt immer die Rechte geprüft auch wenn der Nutzer das `system.root`Recht hat.

*Verbessert*

* Das Löschen von **verlinkten Objekten** kann durch den Benutzer aktiviert oder übersprungen werden.
* Mehr EXIF Tags im **Metadaten-Mapping** verfügbar (**ExifIFD**).
* **XML-Export** wurde beschleunigt, insbesondere für die **OAI/PMH**-Schnittstelle.
* **XML-Export** enthält mehr Systemfelder.
* Mehr **Email-Adressen** werden beim Speichern akzeptiert.

*Behoben*

* **CSV-Export von Ereignissen**: Korrekter Export von abgeschnittenen Feldern mit mehrbytigen UTF-8-Werten.
* **CSV-Export von Ereignissen**: Export funktioniert jetzt auch mit Nutzern die archiviert sind.
* **Sortierung von Mehrfachfeldern** wurde repariert.

