---
menu:
  main:
    name: "5.60"
    identifier: "5.60"
    parent: "releases569"
    weight: -560
---

> Das Release bringt Performance-Verbesserungen für den Aufbau des Collection-Managers für Installationen mit vielen Nutzern.

# Version 5.60.0

*Veröffentlicht am 27.11.2019*

### Webfrontend

*Neu*

* Für **AssetDetailPlugin** gibt es eine neue Funktion `getSiblingsFromData`um auf andere Asset-Versionen zuzugreifen.

*Verbessert*

* **Veröffentlichungen** haben jetzt erweiterte Konfigurationsmöglichkeiten für die Anzeige im Detail.
* **Datenmodell:** Im Maskenmanager werden einzelne Optionen jetzt kontextabhängig ein- und ausgeblendet
* **Datenmodell:** Verbesserungen beim Schemaserver.

*Behoben*

* **CSV-Importer:** Ein Fehler beim Finden von verlinkten Objekten bei Listen mit mehr als 100 Einträgen wurde behoben.
* **Collection-Manager:** Split-Mode funktioniert jetzt wieder korrekt.
* **Suche nach Tags** über alle Objekttypen wurde korrigiert.
* **Neue Objekte:** Das Speichern der Pool- und Maskenauswahl für den Nutzer wurde repariert.
* Der **Aufruf des Webfrontend** war in einigen Browser/Betriebssystem Kombinationen für Cross-Server-Benutzung nicht möglich. Aktuell umgehen wir das Problem in dem **Webfrontend-Sessions ohne Cookies** betrieben werden.

### Server

*Verbessert*

* **Performanceverbesserungen** im Rechrtemanagement, inbesondere der Aufbau der Collections sollte jetzt schneller gehen.

*Behoben*

* **/api/user:** POST gibt `database_languages` und `search_languages`korrekt zurück, dadruch kann man als Nutzer seine Sprachen korrekt ändern ohne sich danach neu einloggen zu müssen.

* **/api/objecttype**: Support für `:eas_data` in `custom_data`.
* Das **massenhafte Versenden** von Emails in einigen Fällen wurde korrigiert. 
* **/api/db**: Ausgabe von `_changelog`für archivierte Nutzer wurde repariert.
* **CustomDataTypeUpdater**: Fixes für Fälle in denen ein Objekttyp mehrfach umbenannt wurde.