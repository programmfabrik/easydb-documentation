---
menu:
  main:
    name: "5.67"
    identifier: "5.67"
    parent: "releases"
    weight: -567
---

# Version 5.67.0

*Veröffentlicht am 14.05.2020*

### Webfrontend

*Neu*

* Suche: Ein Suchfilter für **vector3d** wurde ergänzt.

*Verbessert*

* **JSON-Importer**: Verbesserte Fehlerausgabe bei defekten Payloads.
* **Detail**: Die aktuelle Version des Objektes wird in der Fußleiste angezeigt.

* **Maskenmanagement**: Grafisch Verbesserte Anzeige der Beispieldaten.

*Behoben*

* **Login**: In Fällen wo neben dem Login besonders viel Text eingeblendet wurde, wird die Größe des Dialogs jetzt korrekt angepasst.
* **Export**: Anzeige des XSLT-Dateinamen als Fallback wenn kein separater Name vergeben wurde.

### Server

*Neu*

* **Dateiformate**: Unterstützung von **3GPP** Audio/Video.

*Verbessert*

* In **Events** werden sensible Daten wie z.B. FTP-Passwörter nicht mehr gespeichert.

*Behoben*

* **Commit**: Fehler im Zusammenhang mit Email versenden wurden korrigiert.
* **Rechtemanagement**: Bei ACLs mit Tagfilter die für Objekttypen ohne Tags angewendet wurde kam es zu einem Datenbankfehler.