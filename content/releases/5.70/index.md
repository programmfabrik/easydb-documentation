---
menu:
  main:
    name: "5.70 (Juli 2020)"
    identifier: "5.70"
    parent: "releases"
    weight: -570
---

> Dieses Release bringt **umfangreiche Änderungen** im Design der **Suche, Detail und Editor**. Sollten Sie ein **eigenes CSS** benutzen, empfehlen wir eine Testinstallation und ensprechende Anpassung vorab durchzuführen.
>
> Dieses Release benötigt **keinen Re-Index**.

# Version 5.70.2

*Veröffentlicht am 23.07.2020*

## Webfrontend

*Behoben*

* Behoben, dass sich die Detailanzeige bei Datensätzen ohne Standard nicht öffnete.

# Version 5.70.1

*Veröffentlicht am 20.07.2020*

## Webfrontend

*Behoben*

* Anzeige der **Objekt-ID** im **Gruppeneditor** war überflüssig, da diese nicht neu geschrieben werden kann.
* **Typo3**: Wenn keine Typo3-Mapping in der Basiskonfiguration hinterlegt war, kam es zu einem Fehler bei der Datenübertragung.

# Version 5.70.0

*Veröffentlicht am 15.07.2020*

## Webfrontend

*Neu*

* Anzeige von aller reverse verlinkten Objekte aus dem Detail in der Suche über einen Menüpunkt.

*Verbessert*

* Unterstützung von **Chromium** basierten Browsern.
* Neues Design für Schnellzugriff. Der Schnellzugriff wurde in Bereiche **Mappen** und **Suchen** unterteilt für eine bessere Übersicht.
* **Beschleunigung der Anzeige** des Schnellzugriff bei vielen freigegebenen Mappen.
* Verbesserung des **Split-Modus** zum gleichzeitigen Anzeigen einer Mappe und der Suche.
* Generelle übersichtliche Anzeige von Standardinformationen (Objekttyp, Pool, System-Object-ID, Standard-Info, Tags) im **Detail, Editor und der Textansicht**.
* Beschleunigung des Ladens des Frontends bei wiederkehrenden Benutzern.
* Anzeige einer generischen **Fußzeile** im Detail und Editor mit Systeminformationen.

*Behoben*

* **Experten-Suche**: Die Suche nach Bereichen von Währungszahlen mit Kommastellen wurde repariert.
* Anzeige von mehrsprachigen Feldern wurde für einige Fälle repariert.
* Laden der Voreinstellungen für neue anonymen Benutzer wurde für einige Fälle repariert.
* Die Eingabe von Datenmodell-Checks für Bereiche von Nummern wurde repariert.

## Server

*Neu*

* **/api/user**: `include_password` ist ein neuer URL-Parameter zur Ausgabe von gespeicherten Passwörtern.
* Unterstützung von Objekte-**Aktualisierungen** per **Hotfolder** per Einstellungen in der Mappe.

*Verbessert*

* Verbesserte Performance im Gruppen-Editor beim Ändern vom Pool.

*Behoben*

* Reindexing bei bidirektionalen Links verbessert.
* Beim Löschen von Objekten die in Mappen liegen, konnte es zu Unique-Constraint-Fehlern kommen die das Löschen verhindert haben.

# Prüfsummen

Hier die Prüfsummen unserer Docker-Images (neueste Version):

```ini
docker.easydb.de/pf/chrome               sha256:62ac9147529a03491b3edc35898b076fad86be181c96be9b2b701962688623f5
docker.easydb.de/pf/eas                  sha256:ba2f1a42f281934a56f88cb8790f4d40e0787a2a5856ad9d495e6aad7fa46af6
docker.easydb.de/pf/elasticsearch        sha256:d6737a517f2cbc2c4441eb37173901ded1042250b17eef426e5758c709bf307f
docker.easydb.de/pf/fylr                 sha256:714c66d7570a96a015dce120ad1de4769dc4f8eb7bc74dbb9f41a6b55f2fb5c7
docker.easydb.de/pf/postgresql-11        sha256:a491f8fbb5e1df8e1acd804455a6cf3c459afdd2b63aad47595945ec2c55fe81
docker.easydb.de/pf/postgresql           sha256:6a3453a8b7066ded00a8255a4ab02b587b7a534c9effcbab8ee4d721533d8eae
docker.easydb.de/pf/server-base          sha256:2b2ae03b4e4c29417d1d672a1f4000a73c153bd0a372840eda79cda662df722b
docker.easydb.de/pf/webfrontend          sha256:2e6aab97a873c8e8f65b9452c210d5c32f63e3c27f09f4fe41048cae09008be4
```

