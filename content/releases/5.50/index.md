---
menu:
  main:
    name: "5.50"
    identifier: "5.50"
    parent: "releases"
    weight: -550
---

> * Das alte Systemrecht **Suchfunktion deaktivieren (nur Zugriff auf Mappen)** wurde durch das neue System **Zugriff nur auf Mappen (Recherche ohne Suchfunktion)** ersetzt. Stellen Sie sicher, Ihr Rechtemanagement **vor Update** auf das neue Recht umzustellen.
> * Dieses Release erfordert einen kompletten **Re-Index**. Planen Sie eine Downtime für das Update ein, da in der Zeit der Neuindizierung das System nicht komplett zu nutzen ist.

# Version 5.50.0

*Veröffentlicht am 04.05.2019*

### Webfrontend

*Neu*

* **Datenmodell**: **Horizontaler Zeiler und Block** sowie alle CustomMaskSplitter die dafür eingerichtet sind, können **in Mehrfachfeldern** benutzt werden.
* Im **Kontextmenü** gibt es eine neue Option zum Kopieren in die Zwischenablage.
* Die Listenansicht erlaubt jetzt optional **1000 Treffer** pro Seite.

*Verbessert*

* Rechtemanagement: Für Objekttypen ohne Assets, wurde die **Anzeige im Rechtemanagement verschlankt**, so dass die Rechte für Assets nicht mehr angezeigt werden.
* In der **Druck-Textansicht** wurde die System-Objekt-ID hinzugefügt.
* Die **Experten-Suche** zeigt nur noch Tags an der aktuellen Suche zur Verfügung stehen.
* Editor: Für das **Kopieren von Datensätzen** wird die aktuell ausgewählte Maske verwendet.
* Detail: Die Funktion **Kopieren** steht jetzt auch im **3-Punkte-Menü** zur Verfügung.
* Die Anzeige von **ausgewählten Mehrfachfelder** in der Suche wurde verbessert.
* **Präsentationen**: Verbesserung der Ausgabe bei Datensätzen ohne Vorschauen.

*Behoben*

* **Connector**: Das Blättern in Suchergebnissen wurde repariert.
* Objekttypmanager: Der **Speichern-Button** wurde bei ausschließlichen Änderungen an Tags nicht aktiviert.
* Anzeige vom **Owner-Field** in Abhängigkeit von Feldrechten und Tags wurde repariert.
* In einer leeren Poolsuche wurde mit **Esc** ein Javascript-Fehler produziert.
* **Anzeige von gedrehten Bildern** in kleinen Vorschauen wurde repariert.
* In **Nebeneditoren** springt die Anzeige nicht mehr nach oben, wenn in einem gescrollten Bereich getippt wird.

### Server

*Neu*

* **CustomDataTypeUpdater**: Ein neuer Server Prozess erlaubt das automatische periodische Aktualisieren von CustomDataTypes. Als Beispiel liefern wir ein Updater im [custom-data-type-gazetteer](https://github.com/programmfabrik/easydb-custom-data-type-gazetteer/). (Beta). 
* **Datenmodell**: Boolsche Felder sind nicht mehr für die Generierung von **Standard** unterstützt.
* **CSV-Export**: Ausgabe der Asset-ID und Ausgabe von hierarchien auch für Top-Level-Datensätze (nicht nur für verlinkte Objekte).

*Verbessert*

* **Performance**: Das Rechtemanagement für einige Aufrufe ist für komplexe Konfigurationen schneller. Die Verbesserungen sind hauptsächlich für **/api/db_info**, aber auch **/api/search** (mit generate_rights, verwendet in der Detailansicht) ist schneller.
* **Performance**: Das Laden von Einstellungen wurde beschleunigt, dadurch in ein Aufruf von **/api/session** schneller.
* Im **Webhook-Python-Plugin** wird jetzt **node.js** des Systems benutzt.

*Behoben*

* Die Verwendung von Passwörtern über **LDAP** mit **Sonderzeichen** wird korrekt unterstützt.
* Das Generieren des **Standard in Mehrfachfeldern** berücksichtigt die Reihenfolge der Felder korrekt.
* Beim Neuanlegen von Objekten konnte es in einigen Fällen zu Race-Konditionen kommen die einen Javascript-Fehler im Frontend erzeugt haben. Grund war, dass der **/api/eas**-Endpunkt nicht immer die Original-Dateinamen zurückgegeben hat. Das wurde korrigiert.
* Die **Suche mit Wildcards** für verbundene Wörter wurde repariert. Das Suchen von "worta wortb*" funktioniert jetzt korrekt.