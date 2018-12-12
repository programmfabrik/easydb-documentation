---
menu:
  main:
    name: "5.44"
    identifier: "5.44"
    parent: "releases"
    weight: -544
---

> Zur Umsetzung der erweiterten Konfigurationsmöglichkeiten (siehe unten) sind Anpassungen in der Konfiguration notwendig. Die aufgezeigten Beispiele beziehen sich alle auf die schon vorhandene `easydb5-master.yml`:
>
> **E-Mail-Konfiguration**. Sofern der Block `common.email` verwendet wird, muss dieser dupliziert als `easydb-server.smtp` und `eas.smtp` abgelegt werden. Der alte Block `common` kann nach dem Update entfernt werden. Siehe auch [E-Mail-Konfiguration](/en/sysadmin/konfiguration/recipes/email).
>
> alt:
>
> ````yaml
> common:
>   email:
>     server: 172.18.0.1
>     hostname: easy.example.com
>     from-address: noreply@example.com
> ````
>
> neu:
>
> ````yaml
> easydb-server:
>   smtp:
>     server: 172.18.0.1
>     hostname: easy.example.com
>     from-address: noreply@example.com
> eas:
>   smtp:
>     server: 172.18.0.1
>     hostname: easy.example.com
>     from-address: noreply@example.com
> ````
>
> **Host-Konfiguration**. Diese Änderung sollte nur in Ausnahmefällen notwendig sein, wenn die Installation vom Standard abweicht und z.B. auf mehrere Maschinen verteilt ist oder mehrere Instanzen auf einer Maschine laufen. In dem Fall, dass `docker-hostname` in `easydb5-master.yml` vorkommt, sollte die Konfiguration erweitert werden. Dabei wird `easydb-server.docker-hostname` zu `easydb-server.hostnames.server`, `eas.docker-hostname` zu `easydb-server.hostnames.eas` sowie `fylr.docker-hostname` zu `easydb-server.hostnames.fylr`. Die bisherigen Konfigurationsvariablen sollten erhalten bleiben.
>
> alt:
>
> ````yaml
> eas:
>   docker-hostname: custom-eas
> easydb-server:
>   docker-hostname: custom-server
> fylr:
>   docker-hostname: custom-fylr
> ````
> neu:
>
> ````yaml
> eas:
>   docker-hostname: custom-eas
> easydb-server:
>   docker-hostname: custom-server
>   hostnames:
>     eas: custom-eas
>     server: custom-server
>     fylr: custom-fylr
> fylr:
>   docker-hostname: custom-fylr
> ````

# Version 5.44

*Veröffentlicht am 12.12.2018*

### Webfrontend

*Neu*

* **Tags** können jetzt in der **Filteranzeige** angezeigt werden.
* Sucheingaben können mit Leertaste oder Return im Nachhinein verändert werden.
* Sucheingaben in doppelten Anführungszeichen führen keine Platzhaltersuche mehr durch, die Platzhaltersuche kann ohne Anführungszeichen benutzt werden. Neu ist dabei, dass neben ***** (mehrere Zeichen) auch **?** (einzelnes Zeichen) funktioniert.
* **System-Object-ID** kann im Suchergebnis angezeigt werden (Anzeigeeinstellung, das ist die ID in der Detail-Anzeige mit dem **#**)
* Die **Reihenfolge** von System-Object-ID, Standard + Tags Spalten in der Tabellenansicht können vom Benutzer festgelegt werden.
* Unterstützung von **Editor-Plugins** zur Überprüfung von Eingaben.
* Unterstützung von **Script-Runner-Plugins**. Ein erstes Plugin erlaubt das Herunterladen als CSV von beliebig gefilterten Asset-Metadaten aus dem Suchergebnis.
* Feldfilter für Objekttypen funktionieren jetzt auch für die Systemfelder **Owner** und **Parent**.
* Im Editor können **zusätzliche Informationen** angezeigt, wenn das Formular nicht gespeichert werden kann.

*Verbessert*

* JSON-Importer: Logausgabe wurde verbessert
* Verbesserte Tastatureingabe für Auswahlen und Menüs.
* Bei selbst definierter dunkler Hintergrundfarbe wird der Text im Titel der easydb weiß dargestellt.

*Behoben*

* Sucheingaben mit doppelten Anführungszeichen innerhalb von doppelten Anführungszeichen werden korrekt verarbeitet.

* PDF-Anzeige wurde für Fälle repariert in denen der Server keine Einzelseitenvorschauen generieren konnte.
* Die Mehrsprachen-Anzeige wird nach Ändern der Spracheinstellungen korrekt aktualisiert.
* Filteranzeige von Mehrfachfeldern vom Maskentyp **nested** repariert.

### Server, Plugins und Container

*Neu*

* Konfigurierbares Synonym-Mapping für Volltext-Suche.
* Speichern von Systemfeldern in Spaltenfiltern ermöglicht.
* gemeinsame Docker-Container-Konfigurationsdatei `easydb5-master.yml` kann durch einzelne Konfigurationsdateien ersetzt oder erweitert werden.
* **Webhook-Plugin**

*Verbessert*

* Schriftzeichen **asiatischer Schriften** (CJK, Hiragana, Katakana, Hangul) werden in der Volltext-Suche als eigenständige Token behandelt.
* Pool-Filter für Suchen mit `system.root`-Nutzern optimiert.

*Behoben*

* Fehler bei Suche nach Unicode-Zeichen der Ebene 1 aufwärts behoben.

