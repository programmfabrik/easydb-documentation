# Allgemein


|Einstellung | | Erläuterung |
|------|--|--------|
|Name der easydb| | Der Name der easydb wird als Verzeichnis-Name und ZIP-Prefix Exporte verwendet. Auch ist es der Name der easydb, wie er in Logs und Administrator-E-Mails erscheint. |
|Anzeigename | | Name der easydb wie er im Web-Browser angezeigt wird (als Dokument-Titel). Dieses Feld ist mehrsprachig. |
|Sprachen | Datenbank | Die Datenbank-Sprachen sind die Sprachen die für End-Anwender für die Datenmodellierung und -Eingabe sowie die Suche zur Verfügung stehen. <br><br>_Die Liste verfügbarer Sprachen ist Server-seitig fest eingestellt und kann nicht verändert werden._ |
|  | Oberfläche | Die Frontend-Sprachen sind die Sprachen, die für End-Anwender zur Verfügung stehen. <br><br>_Die Liste verfügbarer Sprachen ist Server-seitig fest eingestellt und kann nicht verändert werden._|
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

