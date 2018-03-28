# Basis-Konfiguration

## Allgemein


|Einstellung | | Erläuterung |
|------|--|--------|
|Name der easydb| | Der Name der easydb wird als Verzeichnis-Name und ZIP-Prefix Exporte verwendet. Auch ist es der Name der easydb, wie er in Logs und Administrator-E-Mails erscheint. |
|Anzeigename | | Name der easydb wie er im Web-Browser angezeigt wird (als Dokument-Titel). Dieses Feld ist mehrsprachig. |
|Sprachen | Frontend | Die Frontend-Sprachen sind die Sprachen, die für End-Anwender zur Auswahl zur Verfügung stehen. <br>_Die aufgelisteten Sprachen sind Server-seitig fest eingestellt und können nicht verändert werden._|
|         | Datenbank | Die Datenbank-Sprachen sind die Sprachen die für End-Anwender für die Datenmodellierung und -Eingabe sowie die Suche zur Verfügung stehen. <br>_Die aufgelisteten Sprachen sind Server-seitig fest eingestellt und können nicht verändert werden._ |
|Administrator-Emails| |Administrator-E-Mails können angegeben werden. easydb schickt solche Emails, bei folgenden Events: server_start, server_shutdown, ...|
|Erlaubte Herkunftsadresse| |URLs von denen ein Fremd-Browser-Zugriff erlaubt werden soll. Die URLs müssen vollständig mit Protokoll angegeben werden. Zum Beispiel "​​http :// myown.easydb.api.example. com" |
|Benutzer-Aktivität loggen |Suchanfragen loggen |Protokolliert die Suchanfragen der Benutzer. |
| |Login / Logout loggen |Protokolliert Login- und Logout-Events eines Benutzers. |
| |Detail-Anzeige loggen |Protokolliert die Aufrufe einer Detail-Ansicht. |
| |Loggen, wenn ein Nutzer ein Asset hochlädt |Protokolliert das Hochladen eines Assets durch einen Benutzer. |
| |Loggen, wenn ein Nutzer einen Export herunterlädt |Protokolliert das Herunterladen eines Exports durch einen Benutzer. |
| |Loggen, wenn ein Nutzer ein Asset aus einem Export herunterlädt |Protokolliert das Herunterladen eines Assets aus einem Export durch einen Benutzer. |
|Autovervollständigung|Wann||
||Umfang||
|System-Adressen|Absender||
||Envelope-Absender||
|API-Calls loggen|||
||aktiv|hier wird festgelegt ob und welche Logs in easydb gemacht werden|
||folgende Calls loggen|über die Checkboxen können die Calls, die geloggt werden sollen, definiert werden|

## Hochladen

Unter diesem Reiter werden globale Limits für Uploads (Hochladen von Assets in easydb) definiert.

|Einstellung | | Erläuterung |
|----|--|---|
|Upload-Limit | | Das Globale-Upload Limit in Bytes. Wenn ein Upload größer ist, wird er in jedem Fall abgelehnt, auch wenn per Rechtemanagement andere Werte eingestellt sind. |
|_Datei-Klasse_ | Limit | Pro Datei-Klasse kann ein eigenes Limit definiert werden. Wenn es größer ist als das globale Upload-Limit, wird es ignoriert. |
|				| Typ | Es werden nur die Formate für einen Upload akzeptiert, die hier aktiviert sind. Für die Datei-Klasse _Sonstige_ werden immer alle Formate erlaubt, die nicht in einer der anderen Datei-Klasse aufgelistet sind. |


## Anmelden {#login}

Unter diesem Reiter können Einstellungen für den Login vorgenommen werden.

|Einstellung | | Erläuterung |
|-----|--|---|
|Cookie-Absicherung für Session aktivieren| ||
|Anonym über Internet erlaubt| |Bei Aufruf der Haupt-easydb-URL (http://<easydb-server>/) wir mit dieser Einstellung festgelegt, dass ein unbekannter Benutzer als anonymer Benutzer am System angemeldet wird. Jeder anonyme Benutzer ist automatisch in der Gruppe `Anonymer Benutzer` und kann darüber mit Rechten ausgestattet werden. easydb hinterlegt beim Benutzer einen Browser-Cookie mit dem er beim nächsten Mal wiedererkannt wird und intern derselben Benutzer-ID zugeordnet wird. Für den Benutzer können dadurch Benutzer-Einstellung usw. gespeichert werden. Ob ein Benutzer aus dem Internet kommt oder nicht, wird über _Intranet-Konfiguration_ festgelegt.|
|Anonym über Intranet erlaubt| |Wie *Anonym über Internet erlaubt* nur dass sich diese Einstellung auf Benutzer bezieht, die als Intranet-Benutzer erkannt wurden.|
|Intranet-Konfiguration| |Hier werden IP-Adressen (172.16.0.2) und Netze (zb. 192.168.0.0/16) hinterlegt, die als _Intranet_ gelten. Beim Aufruf des Servers wird die IP-Adresse des Aufrufes festgestellt und eine entsprechende Einordnung vorgenommen.|
|Prozess für vergessene Passwörter initiieren| |Wenn aktiv, wird dem Benutzer auf der Anmeldeseite eine Möglichkeit angeboten, über seine hinterlegte E-Mail-Adresse ein neues Passwort zu setzen. Diese Einstellung gilt systemweit für alle Benutzer und nicht deaktiviert entzogen werden.|
|Hintergrundbild| |Für die Login-Seite kann ein Hintergrund-Bild hochgeladen werden. Ein Standard-Bild wird in der .ini-Variable `[default-pics]background` festgelegt. Achten Sie darauf, dass das Bild groß ist, so dass für große Bildschirme keine Artefakte sichtbar werden.|
|Information neben dem Login| |Hier kann ein Hinweis für den Benutzer hinterlegt werden. Der Text wird im Anmeldedialog neben dem Login angezeigt. Hier ist nur Text (Markdown) erlaubt, kein HTML.|
|Begrüßungstext| |Der Begrüßungstext kann für die Login-Seite mehrsprachig hinterlegt werden. Hier ist nur Text (Markdown) erlaubt, kein HTML.|
|Passwort-Überprüfung|Policy|Legen sie mit +/- Regeln zur Überprüfung von Passwörtern fest. Über ein Regulären-Ausdruck wird das Passwort geprüft. Mit _Minimum_ und _Maximum_ legen sie fest wie oft der Reguläre Ausdruck mindestens gefunden werden muss und maximal gefunden werden darf.|
| |Hinweis|Der mehrsprachige Text erklärt dem Benutzer, was er bei seinem Passwort beachten muss.|
|Wiederholte Passwörter erlauben| |easydb speichert alle vom Benutzer benutzen Passwörter (verschlüsselt). Für wiederverwendete Passwörter kann festgelegt werden, wie alte ein Passwort sein darf.|
| | _Immer_ | Ein Passwort darf niemals wiederverwendet werden. |
| | _Monat_ | Ein Passwort darf im selben Monat nicht wiederverwendet werden. |
| | _Niemals_ | Der Server schaltet die Überprüfung nach wiederholten Passwörtern ab. |
|Anmeldedienste: SSO|Text für Anmeldelink |Eigenen Anmeldetext für den Link zum Authentifizierungsdienst hinterlegen. Beleibt das Feld leer wird standardmäßig "Anmeldedienst verwenden" angezeigt. |


## Erweiterte Funktionen {#design}

|Einstellung||Erläuterung|
|--|--|--|
|Logo & Kopfzeile|||
||Logo | Das Logo kann hochgeladen werden. Es wird in der Original-Auflösung und im Original-Format oben rechts angezeigt. Mit Mausrad + Move kann das Logo justiert werden. Über die .ini-Variable `[default-pics]logo` kann ein Pfad zu einem Standard-Bild festgelegt werden. |
||Hintergrundfarbe| Hintergrundfarbe für das Logo wählen. |
|Dokumentation|Link-Button|Aktiviert im Frontend den Link-Button zur easydb Dokumentation. Der Button erscheint oben rechts in der Zeile neben den Benutzereinstellungen.|
||URL|Bleibt diese Feld leer, führt der Link standardmäßig zur allgemeinen easydb-Dokumentation. Es kann ein eigener Link zu einer individuellen Dokumentation hinterlegt werden.|
|CSS-Dateien||Eigenes Design für easydb erstellen.|
|Karten-Einstellungen|[Karten im Detail](/webfrontend/datamanagement/search/detail/detail.html#geotag) anzeigen|Anzeige des Thumbnails in einer Karte, wenn die Datei Geokoordinaten enthält.|

Bei geladenem CSS-Plugin (Standard) erscheinen hier Eingabefelder zum modifizieren des geladenenen CSS. Das CSS-Plugin erkennt, wenn dsich die angegebenen URLs ändern und stellt ein neues CSS für die Applikation bereit. Benutzen Sie auch das Tool [CSS-Developer], um mehr Übersicht über die geladenenen SCSS-Dateien zu bekommen.

Das CSS der easydb ist in [SCSS](http://sass-lang.com/) erstellt.

### CSS-Dateien

|Einstellung| Erläuterung |
|------|--------|
|Header| Hier können URLs zu SCSS-Dateien angegeben werden, die vor dem Header-SCSS der easydb geladen werden. |
|Body| Hier können URLs zu SCSS-Dateien angegeben werden, die nach dem Body-SCSS der easydb geladen werden. |
|Footer| Hier können URLs zu SCSS-Dateien angegeben werden, die nach dem Footer-SCSS der easydb geladen werden. |




