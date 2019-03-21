---
menu:
  main:
    name: "5.48"
    identifier: "5.48"
    parent: "releases"
    weight: -548
---

> Das neue Systemrecht **Zugriff nur auf Mappen (Recherche ohne Suchfunktion)** wurde hinzugefügt. Wir werden das alte Systemrecht **Suchfunktion deaktivieren (nur Zugriff auf Mappen)** in der **Version 5.50.0** (geplanete Veröffentlichung am 02.05.2019) **entfernen**. Stellen Sie sicher, Ihr Rechtemanagement bis dahin auf das neue Recht umzustellen.

# Version 5.48.0

*Veröffentlicht am 20.03.2019*

### Webfrontend

*Neu*

* Neues Systemrecht **Zugriff nur auf Mappen (Recherche ohne Suchfunktion)** wurde hinzugefügt.
* Der Status des **Schnellzugriff** wird jetzt je automatisch Nutzer gespeichert. Der Status wird auch in den Gruppenprofilen für neue Nutzer hinterlegt.
* Feldrechte können jetzt dem **Owner (Verantwortlicher)**  eines Objektes gegeben werden. Beachten Sie, dass hierfür die Maskenoption **Owner** zumindest sichtbar eingestellt sein muss.
* Im **Debug-Modus** des Webfrontend werden alle Rechte jetzt mit ihrem Api-Namen ausgegeben.
* Editor: Im **Hochladen-Dialog** werden ab **100 Dateien** eine Navigation eingeblendet. Maximal 1000 Dateien können in einem Vorgang hochgeladen werden.

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

