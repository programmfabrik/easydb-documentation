---
menu:
  main:
    name: "5.53"
    identifier: "5.53"
    parent: "releases"
    weight: -553
---

> * Dieses Release erfordert einen kompletten **Re-Index**. Planen Sie eine Downtime für das Update ein, da in der Zeit der Neuindizierung das System nicht komplett zu nutzen ist.

# Version 5.53.1

*Veröffentlicht am 09.07.2019*

### Webfrontend

*Behoben*

* Einfache CustomMaskSplitter funktionieren wieder in Mehrfachfeldern.
* Exporte die einen gelöschten Objekttyp beinhalten, können verändert werden ohne das ein Fehler erscheint. 

### Server

*Verbessert*

* Beschleunigtes und in einigen Fällen repariertes Speichern im Editor durch Optimierung von ACL-Überprüfung in verbundenen Collections.

*Behoben*

* Rechteüberprüfung in **/api/message** wurde für einen Fall korrigiert.

# Version 5.53.0

*Veröffentlicht am 03.07.2019*

### Webfrontend

*Neu*

* Das **Datumsbereichsfeld** unterstützt nun die aus easydb 4 bekannte textuelle Ein- und  Ausgabe von Daten. Damit kann z.B. "1. Jhd." angegeben werden.

* **Suche**: Für Datumsfelder gibt es jetzt Zusammenstellungen im Filter für **heute**, **morgen**, **diese & nächste Woche**, **nächsten Monat**. 
* **Listen**: Hierarchische Listen können jetzt per Einstellung ohne Hierarchie angezeigt werden.
* [EditorPlugin](https://docs.easydb.de/en/technical/plugins/reference/webfrontend/editor-plugin/) untertsützt jetzt einen **onSave**-Callback.
* Die **Anzeige der Nutzerhinweise** im Editor werden mittels Markdown gerendert, d.h. es lassen sich hier jetzt Formatierungen verwenden.
* **Editor**: Es kann jetzt eine beliebige Anzahl neuer leerer Datensätze hinzugefügt werden. 

*Verbessert*

* Das Ändern von Wasserzeichen im **Pool** ist jetzt auch möglich, wenn der Nutzer nur über das `BAG_WRITE`-Recht verfügt.
* **Ereignisse**: Die Anzeige beim Start führt jetzt keine automatische Suche nach Ereignissen mehr durch. In Datenbanken mit sehr vielen Events dauert eine ungefilterte Suche zu lange und es kam u.U. zu Timeouts.
* Kleinere grafische Verbesserungen.

*Behoben*

* Unterstützung von Host-Only-Domains in EAS-URLs. 

### Server

*Neu*

- Neues Plugin [easydb-editor-field-visibility](https://github.com/programmfabrik/easydb-editor-field-visibility).

*Verbessert*

* Optimierte Liste von Events die über die Poll-Schnittstelle rausgegeben werden, dadurch wird die Serverlast reduziert. Weggefallen sind `EPORT_ASSET`, `JANITOR_USER_PURGE`, `JANITOR_SESSION_PURGE`
* **/api/db/list** liefert an Stelle eines Fehlers ein leeres Ergebnis, wenn keine Objekte gefunden wurden.
* Verbesserungen im Passwort-Vergessen-Anforderungsprozess.
* Re-Index für Aktualisierungen die aus Plugins stammen verbessert.
* Basetypes werden jetzt durch Servercode und ohne Datenbanktrigger neu-indiziert.
* Speichern wurde durch neue Indices auf Historie-Tabellen beschleunigt.

*Behoben*

* Zuordnung **Intranet** für anonyme Nutzer wurde repariert.
* **/api/pool** speichert jetzt auch ohne `BAG_ACL` Recht.
* **Historie gelöschter Tabellen** wird jetzt auch gelöscht, wenn ein Objekttyp gelöscht wird.
* Sprachabhängie Poolnamen im Aggregationen wurden korrigiert.
* Serverstatus wurde für leere Datenbanken (keine Assets) repariert.