---
menu:
  main:
    name: "5.51"
    identifier: "5.51"
    parent: "releases"
    weight: -551
---
# Version 5.51.2

*Veröffentlicht am 30.05.2019*

* Keine Änderungen im Kern, es gab nur eine Änderung für eine kundenspezifisches System.

# Version 5.51.1

*Veröffentlicht am 23.05.2019*

### Webfrontend

*Neu*

* Mappen-Deep-Links können mit dem URL Zusatz `anonymous` für anonyme Logins benutzt werden.

*Behoben*

* In Poolsuchen ist das Auswählen von übergeordneten strukturierenden Pools wieder möglich. 
* Problem in der Objectstore-Synchronisation behoben.

### Server

*Behoben*

* Ermittlung der Maskenreihenfolge korrigiert. Führte u.U. zu fehlenden Ergebnissen in der Suche.
* Session-Gruppen-Zuordnung korrigiert. Führte u.a. zu Fehler bei SSO-Authentifizierung.

# Version 5.51.0

*Veröffentlicht am 22.05.2019*

### Webfrontend

*Neu*

* Metadaten-Mapping: Es können **eigene Metadaten-Felder** zu Profilen hinzugefügt werden.
* Metadaten-Mapping: Zwei **neue Profile ohne vorkonfigurierte Metadaten** zum eigenen Befüllen.
* Editor: In allen Editoren gibt es die neue Möglichkeit zwischen den aktuell selektieren (oder gefundenen) **Vor- und Zurückzublättern**.
* Datenmodell: Zwei neue Maskenoptionen erlauben das **Verbergen der Maske** im Editor und Detail.

*Verbessert*

* Anzeige der Zoomstufe wurde grafisch verbessert.
* Im Infomenü einer Veröffentlichung gibt es jetzt einen Button **Link kopieren**.

*Behoben*

* **Detail**: In einigen Fällen blieb die Info-Button der vorherigen Datei sichtbar.
* Bei leeren neu aufgesetzen easydbs startete die Suche nicht.

### Server

*Neu*

* Neuer Endpunkt **/api/xmlmapping/tags**: Listet verfügbare Tags für Metadaten schreiben und lesen auf.
* **/api/mask**: Zwei neue Optionen: `hide_in_editor`, `hide_in_detail`. 
* Das **Gazetteer-Plugin** nutzt nun den automatischen Update-Mechanismus zum regelmäßigen Aktualiseren vorhandener Einträge.
* Abgelaufene Sessions werden vom Janitor aus dem System gelöscht.
* Volltextsuche für Zahlen.
* Neuer Endpunkt: **/api/settings/updatecustomdata**.
* Um beim Löschen eines Datensatz in verlinkten Objekte die Verlinkung zu diesem Datensatz zu lösen, gab es einen Fehler wenn der Nutzer über das Löschrecht (**DELETE**) am verlinkten Datensatz verfügte.

*Verbessert*

* Das **Webhook-Plugin** nutzt jetzt die zentrale Node.js Infrastruktur des Server. Der Webhook des Example-Plugins wurde erweitert.
* Performance Verbesserungen für **/api/session**.
* **MAIL_SENT** Events werden vom Janitor regelmäßig entsorgt.

*Behoben*

* **Zeitgesteuerte Exporte** funktionieren nun auch, wenn die damit verbundene Session abgemeldet wird.
* Neuindizierung von Objekten, die auf Kinder des editierten Objekts verlinken wurde repariert.
* Bei Transaktionsabruch konnten in einigen Fällen keine Tags gesetzt werden.



