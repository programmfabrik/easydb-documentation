---
menu:
  main:
    name: "5.53"
    identifier: "5.53"
    parent: "releases"
    weight: -553
---

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

* Das Ändern von Wasserzeichen im **Pool** ist jetzt auch möglich, wenn der Nutzer nur über das **BAG_WRITE**-Recht verfügt.
* **Ereignisse**: Die Anzeige beim Start führt jetzt keine automatische Suche nach Ereignissen mehr durch. In Datenbanken mit sehr vielen Events dauert eine ungefilterte Suche zu lange und es kam u.U. zu Timeouts.
* Kleinere grafische Verbesserungen.

*Behoben*

* Unterstützung von Host-Only-Domains in EAS-URLs. 

