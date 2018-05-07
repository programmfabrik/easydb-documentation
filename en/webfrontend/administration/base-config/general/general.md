# General



|Permitted origin address || URLs from which third-party browser access is to be allowed. The URLs must be complete with log. For example "http://myown.easydb.api.example.com" |
|User Activity Logging |Search Logs|  Records user search requests. |
| | Login / Logout |  Records a user's login and logout events. |
| | Detail View Logs | Records the views of a detail view. |
| | Asset upload Logs | Records the upload of an asset by a user. |
| | Export download Logs  | Records the download of an export by a user. |
| | Asset download from an export Logs | Records the download of an asset from an export by a user. |
| Autocomplete | When ||
|| extent ||
| System addresses | sender ||
|| envelope sender ||
| API-Call Logs |||
|| active | here it is determined if and which logs are made in easydb |
|| log the following calls | the checkboxes can be used to define the calls that are to be logged|

> NOTE: More detailed information on the individual logs can be found in the [technical documentation](https://docs.easydb.de/en/technical/api/api.html) beneathe the chapter API. 

## Name of easydb

| Settings | Explanation |
|------|--------|
|Name of the easydb| The name of the easydb is used as the directory name and ZIP prefix for exports. This name also appears in logs and administrator emails. |
| Display name | | Name of the easydb as it is displayed in the web browser (as document title). This field is multilingual.|

## Languages

| Settings | Explanation |
|------|--------|
| Database | The database languages ​​are the languages, which are ​​available to users for data modeling and input as well as search. <br>_The listed languages ​​are defined on the server and can not be changed._|
| Frontend |The frontend languages ​​are the languages, which are ​​available for users. <br><br>_The listed languages ​​are defined on the server and can not be changed._ |

## Administrator-E-Mails

| Settings | Explanation |
|------|--------|
|Administrator emails|The Administrator email adress is used for emails |

## Zugriff von Fremdbrowsern

| Settings | Explanation |
|------|--------|
|Erlaubte Herkunftsadresse|URLs von denen ein Fremd-Browser-Zugriff erlaubt werden soll. Die URLs müssen vollständig mit Protokoll angegeben werden. Zum Beispiel "​​http :// myown.easydb.api.example. com" |

## Benutzer-Aktivität loggen

| Settings | Explanation |
|------|--------|
|Webfrontend-Probleme loggen. |Protokolliert die Fehler, die bei der Verwendung der Benutzeroberfläche auftreten. |
|Loggen, wenn ein Benutzer eine Datei aus einem Export herunterlädt. |Protokolliert das Herunterladen eines Assets aus einem Export durch einen Benutzer. |
|Loggen, wenn ein Benutzer eine Datei hochlädt. |Protokolliert das Hochladen eines Assets durch einen Benutzer. |
|Suchanfragen loggen. |Protokolliert die Suchanfragen der Benutzer. |
|Loggen, wenn ein Benutzer einen Export herunterlädt. |Protokolliert das Herunterladen eines Exports durch einen Benutzer. |
|Detailansicht loggen. |Protokolliert die Aufrufe einer Detailansicht. |
|Login / Logout loggen. |Protokolliert Login- und Logout-Events eines Benutzers. |

## Autovervollständigung

| Settings | Explanation |
|------|--------|
|Umfang|**Wörter & verlinkte Datensätze**: Vorschläge für alle Eingabefelder und alle anderen über Listen verwalteten Objekttypen <br>**Wörter**: Vorschläge für alle Eingabefelder <br>**Verlinkte Datensätze**: Vorschläge für alle anderen über Listen verwalteten Objekttypen|
|Wann|**nie**: keine Vorschläge anzeigen <br> **immer**: Vorschläge mit Eingabe des ersten Zeichens anzeigen <br> **ab 2 Zeichen**: Vorschläge ab Eingabe des zweitens Zeichens anzeigen <br> **ab 3 Zeichen**: Vorschläge ab Eingabe des dritten Zeichens anzeigen|

## System-Adressen

| Settings | Explanation |
|------|--------|
|Anzeigename für Absender|Name der in E-Mail für die Absenderadresse angezeigt wird.|
|Absender|E-Mail-Absender für System-E-Mails. Dies ist die Adresse, die im Empfänger-E-Mail-Programm zu sehen ist. Sofern diese Adresse nicht durch andere Header geändert wird, gehen Rückantworten ("Reply-To-E-Mails") an diese Adresse. |
|Envelope-Absender|Diese Absender-Adresse ist normalerweise unsichtbar und wird zur Verifizierung des Absenders beim E-Mail-Versand verwendet. An diese Adresse werden auch mögliche Fehler, die beim Versand einer E-Mail entstanden sind, zugestellt ("Bounce-E-Mails").|

## API-Calls loggen

| Settings | Explanation |
|------|--------|
|aktiv|Hier wird festgelegt ob und welche Logs in easydb gemacht werden. Optionen: keine, nur Scheiboperationen, alle|
|folgende Calls loggen|Durch Aktivieren der Checkboxen werden die Calls definiert, die geloggt werden sollen.|

> HINWEIS: Nähere Informationen zu den einzelnen Logs sind in der [Technischen Dokumentation](https://docs.easydb.de/en/technical/api/api.html) unterhalb des Kapitels API zu finden.

