---
menu:
  main:
    name: "5.48"
    identifier: "5.48"
    parent: "releases549"
    weight: -548
---

> * Das neue Systemrecht **Zugriff nur auf Mappen (Recherche ohne Suchfunktion)** wurde hinzugefügt. Wir werden das alte Systemrecht **Suchfunktion deaktivieren (nur Zugriff auf Mappen)** in der **Version 5.50.0** (geplante Veröffentlichung am 02.05.2019) **entfernen**. Stellen Sie sicher, Ihr Rechtemanagement bis dahin auf das neue Recht umzustellen.

# Version 5.48.2

*Veröffentlicht am 01.04.2019*

### Webfrontend

*Verbessert*

* **Export**: Das Umschalten zwischen Export-Plugins startet jetzt automatische eine neue Suche. Damit wird sichergestellt, dass, wenn Objekte für eine Plugin gefiltert werden, diese sofort ersichtlich wird.

*Behoben*

* **Editor**: Beim Verändern von Datensätzen die unter derselben ID auch über eine Connector-Instanz erreichbar sind, wurde die Suche im Listenmodus unter Umständen nicht mit den lokalen Daten sondern mit den Daten der entfernten easydb aktualisiert.
* **Datenmodell**: Die Checkbox **Editierbar in Verlinkung** ist auf dem Topplevel wieder sichtbar.

# Version 5.48.1

*Veröffentlicht am 27.03.2019*

### Webfrontend

*Neu*

* **JSON-Importer**: Es gibt jetzt einen expliziten **Vorbereiten**-Button, um die Payloads zu laden. Das separiert die Verifizierung der Payloads vom eigentlich Hochladen.
* **Änderungshistorie**: Für die Änderungshistorie reicht jetzt das **Leserecht** am dem Objekt benötigt.

*Verbessert*

* **Performance** beim Rendern der **Detail-Anzeige** mit vielen Reitern wurde verbessert. Inbesondere funktioniert der Wechsel zwischen den Reitern jetzt schneller als vorher.
* Bei einer **Auswahl** in der Suche, Nebensuchen und in Mappen werden jetzt immer alle zur Verfügung stehenden **Werkzeuge** geladen, d.h. Editor, Gruppen-Editor und andere stehen jetzt sowohl in allen Kontextmenüs als auch in den 3-Punkte-Menüs zur Verfügung.
* **ScriptExecuter**: Die Suche der Objekte wird jetzt komplett durchgeführt bevor das Script für die Objekte gestartet wird. Dadurch ist sichergestellt, dass sich die Anzahl der Objekte während eines Laufs nicht ändert, durch beispielsweise durch ein Script aktualisierte Tags oder sonstige Metadaten die das Suchergebnis beeinflussen würden.
* **ScriptExecuter**: Bei der Verwendung in **hierarchischen Listen** wird jetzt eine Suche wie für den Export durchgeführt. Dadurch werden auch alle untergeordneten Objekte mit in den Lauf einbezogen.
* Kleiner grafische Verbesserungen in unterschiedlichen Dialogen.

*Behoben*

* Die **Anzeige einer Mitteilung** die keine Bestätung erfordert wurde repariert. Wenn zuvor der Typ der Mitteilung eine Bestätigung erlaubt hat, wurde diese Bestätigung auch in den geänderten Typ übernommen.

### Server

*Neu*

- **/api/db** und **/api/search**: Im Format full wird _changelog jetzt auch für Nutzer rausgegeben, die nur über das **READ**-Recht am Objekt und das Systemrecht **frontend_features[changelog]** verfügen.

*Behoben*

- **Serverstatus**: Bei einigen Installationen konnte der Serverstatus nicht ermittelt werden und ist mit einem Fehler abgebrochen.

# Version 5.48.0

*Veröffentlicht am 20.03.2019*

### Webfrontend

*Neu*

* Neues Systemrecht **Zugriff nur auf Mappen (Recherche ohne Suchfunktion)** wurde hinzugefügt.
* Der Status des **Schnellzugriff** wird jetzt automatisch je Nutzer gespeichert. Der Status wird auch in den Gruppenprofilen für neue Nutzer hinterlegt.
* Feldrechte können jetzt dem **Owner (Verantwortlicher)**  eines Objektes gegeben werden. Beachten Sie, dass hierfür die Maskenoption **Owner** zumindest sichtbar eingestellt sein muss.
* Im **Debug-Modus** des Webfrontend werden alle Rechte jetzt mit ihrem Api-Namen ausgegeben.
* Editor: Im **Hochladen-Dialog** werden ab **100 Dateien** eine Navigation eingeblendet. Maximal 1000 Dateien können in einem Vorgang hochgeladen werden.
* In der Basis-Konfiguration kann das **Loggen und Speichern von personenbezogenen Daten** für Export-, Such- und Detailansicht-Events eingestellt werden.
* Das **Server-Status-Plugin** hat jetzt die Möglichkeit den Server neuzustarten und einen Reindex zu forcieren.
* **Neue Plugin-Schnittstelle** um im **Poolmanager** eigene Reiter einzubinden, die dann Custom Data speichern können.

*Verbessert*

* Die **Pool/Objekttyp-Auswahl** und die **Sortierauswahl** haben jetzt keinen **Anwenden**-Button mehr. Die Auswahl wird automatisch aktiv wenn außerhalb der Auswahl geklickt wird. Damit verhält sich dieser Dialog analog zu den anderen kleineren Dialogen in der Suche.

* Detail: Die **Anzeige von Hierarchien** wurde verbessert. Es werden jetzt (wieder) die Geschwister (auch aller Väter) angezeigt.
* Neue Coffeescript-UI-Version mit verbessertem **Tooltipverhalten** und neuen Regeln für Formularabstände in der Anzeige.

* **JSON-Importer**: Neue Möglichkeite alle Payloads auf einmal zu markieren.
* Verbesserungen bei der **Druckausgabe** für einige Browser.
* Editor: Beim **Ändern eines Pool** in Objekten mit Reverse-Nested-Objekten die auch in Pools sind, wird der Pool auch für die Nested-Objekte aktualisiert.
*  **Änderungshistorie**: Die Nutzernamen der Änderungen werden nur noch angezeigt, wenn der Nutzer Schreibrecht für das Objekt hat, sonst wird nur der Zeitpunkt der Änderung angezeigt.
* Poolmanager: Unterstützung von mehr als **1000 Pools**.
* **Metadaten-Mapping**: Feldnamen werden jetzt mit kompletten Pfad angezeigt.

*Behoben*

* Die **index.html** Seite der easydb enthält jetzt keinen DUMMY Text mehr, der von **Google indiziert** wurde.
* In einigen Fällen hat sich der **+**-Button in der **Mappenübersicht** deaktiviert und niemals wieder aktiviert.

### Server

*Neu*

* **config**: Das **Loggen und Speichern von personenbezogenen Daten** für Export-, Such- und Detailansicht-Events kann eingestellt werden.
* **config**: In der Basis-Konfiguration können Zahlwerte bis maximal `2^64 − 1` (UINT64) angegeben werden.
* **pool**: Speichern von **custom_data** möglichCustom Data speichern
* **config**: Upload-Limits für Dateien pro Klasse
* **settings/reindex** erlaubt eine **komplette Neu-Indizierung**

*Verbessert*

* **EAS Supervisor** wird bei endgültig fehlgeschlagenen Assets und Asset-Versionen nicht weiter versuchen, den Status vom EAS abzurufen.

* **Performance beim Löschen** von Collections und Objekten in Collections wurde verbessert.

* **Performance bei Neu-Indizierung** von Objekten verbessert.

* Upload-Limit für alle Dateien: maximal 25 GB.

*Behoben*

* Nach dem Löschen von Tags werden Objekte, die diese Tags gesetzt hatten, neu indiziert.

* Nach der **Anmeldung per SSO** wird der Zustand der Session aktualisiert und alle Gruppen neu geladen.

* Fehler beim Löschen von Objekten, die sich selbst verlinken (Selbst-Referenz), wurde behoben.

* Das Vererben von **persistenten Pool-Rechten** wurde repariert.
