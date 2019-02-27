---
menu:
  main:
    name: "5.47"
    identifier: "5.47"
    parent: "releases"
    weight: -547

---

> - Die Versionen ab **5.47.0** erfordert eine Neuindizierung, planen Sie entsprechende Zeit für das Update ein.
> - Performance-Optimierungen bei der Auswahl, Detail und Editor. Hier wurde der **Bearbeiten**-Button in das Drei-Punkte-Menü verschoben.
> - Der Aufruf von **fylr** wurde geändert. Bitte schauen Sie **fylr —help** für mehr Informationen.

# Version 5.47.0

*Veröffentlicht am 27.02.2019*

### Webfrontend

*Neu*

* Suche: Sortieren nach Originaldateiname wurde ergänzt.
* Serien & Versionserkennung auch in Mappen & Hotfolder.
* Schnellanzeige: Die Anzeige im Detail für Objekte ist jetzt über das Kontextmenü möglich.
* Plugins: Ein **AssetDetailPlugin** kann jetzt automatisch starten.
* Connector: Unterstützung von Sortierungen.

*Verbessert*

* Performanceverbesserungen bei der Auswahl, Anzeige im Detail und Laden im Editor für Objekte. Wir mussten dafür den **Bearbeiten**-Button im Detail entfernen. Dieser verbirgt sich jetzt im Drei-Punkte-Menü. Es werden jetzt erst beim Klick auf dieses Menü und auch erst beim Klick auf das Kontextmenü die nötigen Rechtechecks durchgeführt.
* Zoomer: Anzeige der aktuellen Zoomstufe in Prozent.
* Drucken: Mehr Einstellmöglichkeiten im Druckmenü. 
* Mappen werden jetzt im Baum aufgeklappt wenn sie anzeigt werden.
* Verbesserter Tastatursupport für Menüs und andere Auswahlen.
* Performance beim Aufbau von Präsentationen wurde verbessert.

*Behoben*

* Poolmanager: Das Entfernen des Kontaktes wurde repariert.
* Vollbildanzeige: Das Springen zur richtigen Vorschau wurde repariert.
* Suche nach Vorschaustatus wurde für einige Kombinationen repariert.
* Suche: Die Eingabe von Leerzeichen nach Anführungszeichen führt nicht mehr zu einem Fehler.
* Detail/Editor: Die Auswahl der Maske zum Anzeigen von verlinkten Objekten war in einigen Fällen, inbesondere bei neu angelegten Objekten nicht korrekt.
* Bei der Auswahl von Objekten wird das Detail jetzt  wieder nur noch dann aktualisiert, wenn aktuell nur ein Objekt in der Auswahl ist.
* Connector: Verschiedene Suchen wurde repariert.

### Fylr

*Neu*

* GZIP Unterstützung for **/objectstore**.
* **fylr apitest** ist jetzt ein jetzt ein [**eigenständiges Tool**](https://github.com/programmfabrik/fylr-apitest/settings) unter Open-Source-Lizenz.
* TLS/SSL Unterstützung. 

Verbessert

* **/zip** arbeitet jetzt schneller (parallel) beim überprüfen ob alle URLs erreichbar sind.

*Behoben*

* Ein Cache-Header Problem in Zusammenhang mit ETag wurde behoben.



