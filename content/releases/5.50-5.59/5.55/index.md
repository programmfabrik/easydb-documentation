---
menu:
  main:
    name: "5.55"
    identifier: "5.55"
    parent: "releases559"
    weight: -555
---

> Dieses Release erfordert einen kompletten **Re-Index**. Planen Sie eine Downtime für das Update ein, da in der Zeit der Neuindizierung das System nicht komplett zu nutzen ist.

> Das CSV-Format von exportierten Ereignissen wurde geändert.

# Version 5.55.0

*Veröffentlicht am 14.08.2019*

### Webfrontend

*Neu*

* Per Maskeneinstellung kann **eine Nebenliste** (verlinkter Objekttyp) als **einfaches Pulldown** angezeigt werden. Das ist sinnvoll für Wertelisten, die nur eine kleine und abgeschlossene Menge von Objekten enthalten.
* Im **Suchergebnis** kann jetzt über das Kontextmenü ein **Objekt aus einer Mappe** entfernt werden, in der es sich befindet.
* Der Nutzermanager zeigt jetzt für LDAP und SSO Nutzer die beim letzten Login des Nutzers **automatisch zugewiesenen Gruppen** an.
* **Experimenteller Markdownsupport** in der Detailansicht. Das Rendern mit Markdown kann im Maskeneditor aktiviert werden, wenn der Debug-Modus aktiv ist.
* Das **Webhook-Plugin** unterstützt jetzt die automatische Überprüfung von **HMAC-Secrets** aus der Basis-Konfiguration.
* In der **Ereignisanzeige** können beim **CSV-Download** einige Optionen ausgewählt werden.

*Verbessert*

* Das **Hijri-Gregorian-Plugin** kann jetzt auch in Mehrfachfeldern und Datumsbereichsfeldern verwendet werden.
* **Grafische Detailverbesserungen** im CSS.
* **Benutzermanagement**: Nutzer vom Typ `collection` werden nicht mehr angezeigt.

*Behoben*

* **Metadatenmapping**: Der Export von verlinkten Objekten mit nur Standard-Info und von Feldern mit fixem Text wurde repariert. Existierende Mappings müssen neu gespeichert werden.
* Die Anzeige *undefined* in der **Tabellenansicht** wurde repariert.
* **Suche** nach **Datum in Mehrfachfeldern** wurde repariert.
* Die Suchanfrage einer **Platzhalter-Suche in Verbindung mit Anführungszeichen** wurde korrigiert.
* Der **Hinweis für Felder im Detail** wird jetzt auch angezeigt, wenn das Feld nur gelesen werden kann.
* Die **Vollbildanzeige aus dem Detail** wurde für Fälle repariert in denen das Detail aus der Tabellenansicht geöffnet wurde.
* **Filter bei aktiviertem Connector** wurden repariert, so dass jetzt nicht mehr zuviel Treffer angezeigt werden.

### Server

*Neu*

* Die Datenbanksprache `nl-NL` wird neu unterstützt.

*Verbessert*

- **Metadatenmapping** bevorzugt jetzt dc-DateCreated, die Vereinnahmung doppelter Werte wird jetzt auch vermieden.
- Der **CSV-Export** benutzt kompaktes JSON.
- Beim **Export** werden nur noch die konfigurierten Sprachen aus der Basis-Konfiguration oder die des Nutzers benutzt, nicht mehr alle Sprachen. 
- Für neue Systeme werden jetzt nur noch die Sprachen `de-DE` und `en-US` standardmäßig aktiviert. 
- Das Format `standard` in **/api/search** (type: `object`) beinhaltet jetzt auch `_collections`.

*Behoben*

* Gruppen von **Nutzern die automatisch per LDAP und SSO** zugewiesen werden, verbleiben jetzt permanent am Nutzer. Beim nächsten Login werden diese Gruppen aktualisiert. Damit wird sichergestellt, dass Mappenfreigaben die durch LDAP / SSO Nutzer erfolgt sind funktionieren.
* Der **CSV-Export** von Ereignissen (**/api/event)** wurde korrigiert und verbessert. Die erzeugten Spalten von `event.info` werden bei `csv_explode` mit einem vorangestellten`info.` bennant. Die Spalte`event.info` wird jetzt korrekt exportiert, wenn `csv_explode=false`gesetzt ist.

* Metadatenmapping exportiert jetzt auch **DateTime und Date** korrekt.
* Das Löschen von Mappen löscht nun auch deren **untergeordnete Mappen** aus dem Index.

