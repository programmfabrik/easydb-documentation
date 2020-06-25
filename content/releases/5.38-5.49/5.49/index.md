---
menu:
  main:
    name: "5.49"
    identifier: "5.49"
    parent: "releases549"
    weight: -549
---

> * Das neue Systemrecht **Zugriff nur auf Mappen (Recherche ohne Suchfunktion)** wurde in **Version 5.48.0.** hinzugefügt. Wir werden das alte Systemrecht **Suchfunktion deaktivieren (nur Zugriff auf Mappen)** in der **Version 5.50.0** (geplante Veröffentlichung am 02.05.2019) **entfernen**. Stellen Sie sicher, Ihr Rechtemanagement bis dahin auf das neue Recht umzustellen.

# Version 5.49.1

*Veröffentlicht am 25.04.2019*

### Webfrontend

*Neu*

* Mit zwei [Konfigurationsvariablen](/en/sysadmin/configuration/easydb-server.yml/webfrontend/) **index_html_head_include** und **index_html_body_include** ist es möglich, die **index.html** der One-Page-App zu beeinflussen, um so eigene Inhalte für eine Suchmaschinen-Indexierung zu konfigurieren.  

### Server

*Behoben*

* Der Dateiname für die Endung **webdvd.zip** wurde bei einigen Downloads nicht korrekt wiederhergestellt.
* Rechtemanagement: Nutzer mit Systemrecht **system.root**, dürfen ohne weitere Rechteprüfungen ACL speichern. Damit können Inkonsistenten bei Collectionrechten behoben korrigiert werden. 

# Version 5.49.0

*Veröffentlicht am 10.04.2019*

### Webfrontend

*Neu*

- Neue Maskeneinstellung für **publish**. Wenn aktiviert, werden Veröffentlichungen die über **/api/publish** erfolgt sind, im Detail und im Teilen-Dialog angezeigt.
- Eine Suche nach Veröffentlichungen wurde in die Expertensuche integriert.
- Im Debug-Menü (STRG-ALT-D) gibt es jetzt eine Möglichkeit zum Senden einer **Test-Email**, um das Setup für das Mailsystem zu testen.

*Verbessert*

* Die Anzeige von Objekten mit mehreren Dateien springt jetzt automatisch auf die erste Datei für die eine Vorschau existiert.
* Bei Collection-Eigenschaften wird die Karteikarte **Allgemein** nun an erster Stelle ausgegeben.
* Die Objekt-ID wird jetzt auch in der Textansicht ausgegeben, wenn in der Maske aktiviert.
* Kleinere grafische Verbesserungen und Reparaturen.

*Behoben*

* Die Suche im Pool-Dropdown wurde repariert.
* Das **Adhoc-Erzeugen** von einem neuen Eintrag in einer Nebenliste wurde repariert.
* Der Feldfilter für **Owner** filtert jetzt auch in Reverse Nested Objekten korrekt.
* Wenn bei aktiviertem Editormodus in der Sidebar ein Objekt gewählt wird, für das der Nutzer nur Leserechte hat, wird jetzt automatisch in den Detailmodus geschaltet.
* Einige Bugs in Zusammenhang mit aktiviertem **Connector** wurden behoben.
* **Connector-Verbindungen** werden jetzt **ohne Cookie** durchgeführt, so dass mehr Browser den Zugriff erlauben sollten.
* Die Suche nach dem **Originaldateinamen** sucht jetzt im kompletten Namen, inkl. Extension.

### Server

*Neu*

* Neue Maskeneinstellung für **publish**. Wenn aktiviert, werden Veröffentlichungen die über **/api/publish** erfolgt sind, im Detail angezeigt.

- Testmailversand über **/api/v1/settings/sendmail** an beliebige registrierte Mailadresse.

*Verbessert*

- Suchergebnisse nach mehrsprachigen Feldern werden alphabetisch sortiert, auch wenn das Feld nicht für alle Sprachen ausgefüllt ist.

- Prozess zum Anfordern eines neuen Passworts wurde verbessert und mit detallierteren Fehlermeldungen ausgestattet.
- **Metadatenmapping**: mehr EXIF-Tags für Bildbreite, Bildhöhe und Digitalisierungsdatum werden für das Mapping unterstützt.

*Behoben*

- Das **owner**-Recht wird jetzt immer korrekt ausgewertet. An einigen Stellen im Rechtemanagement wurde das **owner**-Recht nicht korrekt interpretiert, was bei Objekten zu fehlenden Rechten führen konnte.