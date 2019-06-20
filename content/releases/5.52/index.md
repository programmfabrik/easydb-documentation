---
menu:
  main:
    name: "5.52"
    identifier: "5.52"
    parent: "releases"
    weight: -552
---

# Version 5.52.2

*Veröffentlicht am 20.06.2019*

### Webfrontend

*Behoben*

* Anzeigeprobleme in einigen Connector Szenarien behoben.
* Speichern von Reverse-Nested bei neuen Objekten mit Pools behoben.

### Server

*Behoben*

* Lokalisierung von Workflow-Nachrichten wurde repariert.
* Webhook Callbacks die aus dem Gruppeneditor heraus generiert werden, senden jetzt auch die `_version`des Objektes zum Webhook.

# Version 5.52.1

*Veröffentlicht am 17.06.2019*

### Webfrontend

*Verbessert*

* Autovervollständigung startet jetzt erst nachdem 500 Millisekunden kein neues Zeichen eingegeben wurde. Die vorherigen 200 Millisekunden waren zu kurz.

### Server

*Neu*

* **/api/suggest** unterstützt einen neuen Parameter **fields_suggest**, damit lässt sich die Suche für **fields** in der Antwort unterdrücken. Das führt zu kürzeren Antwortzeiten.

# Version 5.52.0

*Veröffentlicht am 12.06.2019*

### Webfrontend

*Neu*

* Neue Objekte: Einstellung zum dauerhaften Überspringen des Duplikatechecks.
* **Mappen**: Neue Kontextmenüoption zum Anzeigen von fremden Objekten aus Connector-Datenbanken.

*Verbessert*

* Mappen: Beim Teilen mit der Gruppe **Alle Nutzer** oder **Anonyme Nutzer** wird ein Link erzeugt der explizit mit **anonym** authentifziert. Damit wird das Test solcher Links vereinfacht und bekannte Nutzer nicht mit ihrem Cookie angemeldet sondern als neuer Nutzer.
* **Verbesserte Darstellung** beim Auswahlmenü für Nutzer und Gruppen.
* Datenmodell: **Eingebahilfe** für Feld- und Objekttypbezeichner.
* **Neue Fortschrittsanzeige** beim Hochladen von Dateien im Editor.
* Grafische Detailverbesserungen.

*Behoben*

* Das **Speichern** und die Aktualisierung von Pools in untergeordneten Reverse-verschachtelten Objekten hat in einigen Fällen nicht korrekt funktioniert.
* **Drucken von Mappen** mit Connector-Objekten wurde korrigiert: Connector-Objekte können nur über die Suche gedruckt werden, nicht direkt aus der Mappe.

### Server

*Verbessert*

* Speicherbedarf des Janitor wurde reduziert.
* Schnellerer CSV-Export für Events.

*Behoben*

* **OAI/PMH**: Blättern durch die Sets wurde korrigiert und war bei vielen Objekttypen / Pool - Kobinationen fehlerhaft.
* Standard für Mehrfachfelder wurde in einigen Fällen nicht korrekt sortiert.
* Fehler in der Suche korrigiert der bei bestimmten Sprachkombinationen auftreten konnte.
* Neu-Indizierung von abhängigen Objekten wurde verbessert.
* Rechtecheck bei Reverse verlinkten Assets korrigiert.