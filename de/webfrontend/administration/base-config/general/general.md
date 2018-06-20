# Allgemein

## Name der easydb

|Einstellung | Erläuterung |
|------|--------|
|Name der easydb| Der Name der easydb wird als Verzeichnis-Name und ZIP-Prefix für Exporte verwendet. Auch ist es der Name der easydb, der in Logs und Administrator-E-Mails erscheint. |
|Anzeigename | Name der easydb, wie er im Web-Browser angezeigt wird (als Dokumenten-Titel). Dieses Feld ist mehrsprachig. |

## Sprachen

|Einstellung | Erläuterung |
|------|--------|
| Datenbank* | Die Datenbank-Sprachen sind die Sprachen, die für Endanwender für die Datenmodellierung und -eingabe sowie die Suche zur Verfügung stehen. <br><br> _Die Liste verfügbarer Sprachen ist Server-seitig fest eingestellt und kann nicht verändert werden._ |
| Oberfläche | Die Oberflächen-Sprachen sind die Sprachen, die für End-Anwender in den Benutzer-Einstellungen zur Verfügung stehen. <br><br>_Die Liste verfügbarer Sprachen ist Server-seitig fest eingestellt und kann nicht verändert werden._|

> *HINWEIS: Um die Datenbanksprachen ändern zu können, ist das Systemrecht "Datenmodell bearbeiten > Änderungen aktivieren" erforderlich. Für die Aktivierung der geänderten Datenbanksprachen ist das Neuschreiben des Index erforderlich. Dies wird erreicht, indem das Datenmodell neu gespeichert wird und die Änderungen aktiviert werden.

## Zugriff von Fremdbrowsern

|Einstellung | Erläuterung |
|------|--------|
|Erlaubte Herkunftsadresse|URLs von denen ein Fremd-Browser-Zugriff erlaubt werden soll. Die URLs müssen vollständig mit Protokoll angegeben werden. Zum Beispiel "​​http :// myown.easydb.api.example. com" |

## Benutzer-Aktivität loggen

|Einstellung | Erläuterung |
|------|--------|
|Webfrontend-Probleme loggen. |Protokolliert die Fehler, die bei der Verwendung der Benutzeroberfläche auftreten. |
|Loggen, wenn ein Benutzer eine Datei aus einem Export herunterlädt. |Protokolliert das Herunterladen eines Assets aus einem Export durch einen Benutzer. |
|Loggen, wenn ein Benutzer eine Datei hochlädt. |Protokolliert das Hochladen eines Assets durch einen Benutzer. |
|Suchanfragen loggen. |Protokolliert die Suchanfragen der Benutzer. |
|Loggen, wenn ein Benutzer einen Export herunterlädt. |Protokolliert das Herunterladen eines Exports durch einen Benutzer. |
|Detailansicht loggen. |Protokolliert die Aufrufe einer Detailansicht. |
|Login / Logout loggen. |Protokolliert Login- und Logout-Events eines Benutzers. |

## Autovervollständigung

|Einstellung | Erläuterung |
|------|--------|
|Umfang|**Wörter & verlinkte Datensätze**: Vorschläge für alle Eingabefelder und alle anderen über Listen verwalteten Objekttypen <br>**Wörter**: Vorschläge für alle Eingabefelder <br>**Verlinkte Datensätze**: Vorschläge für alle anderen über Listen verwalteten Objekttypen|
|Wann|**nie**: keine Vorschläge anzeigen <br> **immer**: Vorschläge mit Eingabe des ersten Zeichens anzeigen <br> **ab 2 Zeichen**: Vorschläge ab Eingabe des zweitens Zeichens anzeigen <br> **ab 3 Zeichen**: Vorschläge ab Eingabe des dritten Zeichens anzeigen|

## E-Mail-Adressen des System

|Einstellung |Erläuterung |
|------|--------|
|Anzeigename für Absender|Name der in E-Mail für die Absenderadresse angezeigt wird.|
|Absender|E-Mail-Absender für System-E-Mails. Dies ist die Adresse, die im Empfänger-E-Mail-Programm zu sehen ist. Sofern diese Adresse nicht durch andere Header geändert wird, gehen Rückantworten ("Reply-To-E-Mails") an diese Adresse. |
|Envelope-Absender|Diese Absender-Adresse ist normalerweise unsichtbar und wird zur Verifizierung des Absenders beim E-Mail-Versand verwendet. An diese Adresse werden auch mögliche Fehler, die beim Versand einer E-Mail entstanden sind, zugestellt ("Bounce-E-Mails").|

## API-Calls loggen

|Einstellung | Erläuterung |
|------|--------|
|aktiv|Hier wird festgelegt ob und welche Logs in easydb gemacht werden. Optionen: keine, nur Scheiboperationen, alle|
|folgende Calls loggen|Durch Aktivieren der Checkboxen werden die Calls definiert, die geloggt werden sollen.|

> HINWEIS: Nähere Informationen zu den einzelnen Logs sind in der [Technischen Dokumentation](https://docs.easydb.de/en/technical/api/api.html) unterhalb des Kapitels API zu finden.