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

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:9005241c1191177c9ccddadba843ddd09d1ebee337acd1ff4c68217521397b0a
docker.easydb.de/pf/eas                  sha256:7a565f01c23ba5f511efc973566495d62ea4cffec7919280ddf0cbec270d0b13
docker.easydb.de/pf/elasticsearch        sha256:5da9c774cc717d085f8dfef1ee5f6602a1633131414ca362a66ca6d905a3ae5f
docker.easydb.de/pf/fylr                 sha256:1855e036f799e342bae51a95c272a78a396cdf005bc48363b85ccfcf950c9e43
docker.easydb.de/pf/postgresql-11        sha256:f88386976c7dbe798c82f62a60aecafa74cf11a6cbbe31688b5b234d81d3758b
docker.easydb.de/pf/postgresql           sha256:d7a2a39907a6d4d26299e960b5f5d968a789384edd5fcd668961d65954d9e8fc
docker.easydb.de/pf/server-base          sha256:42f9ca0517cf59a3d16a5c5493830eeedb1c1d8b74e20b9263a85106ec2f045b
docker.easydb.de/pf/webfrontend          sha256:399c93364c0721321387bf9ccf9800f95c84c8c315b17f35e2c8b3aa15fc4ead
```



