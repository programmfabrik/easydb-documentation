# General

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
|Administrator emails|The Administrator email adress can be specified to send easydb emails. This address is used for events like server_start, server_shutdown, ...|

## Permitted origin address

| Settings | Explanation |
|------|--------|
|Permitted origins|| Permitted URL origins from which browser access is allowed. The URLs must be complete containing the application protocoll. For example "http://myown.easydb.api.example.com" |

## Benutzer-Aktivität loggen

| Settings | Explanation |
|------|--------|
|Log detail view|Records the calls for detail views.|
|Log export file downloads|Records the download of a file from an export by a user.|
|Log file uploads|Records the upload of an asset by a user.|
|Log search requests|Records user search request.|
|Log export downloads|Records the download of an export by a user.|
|Log login/logout|Records a user's login and logout events.|
|Log webfrontend problems.|Records frontend problems while using easydb.|

## Autocompletion

| Settings | Explanation |
|------|--------|
|When|**never**: no suggestions are made <br> **always**: Suggestions are made starting with the first entered character <br> **starting from 2 characters**: Suggestions are made starting with the second character <br> **starting from 3 characters**: Suggestions are made starting with the third character|
|Scope|**Words and linked records**: Suggestions for all fields and all sencondary object types <br>**Words**: Suggestions for all fields <br>**Linked records**: Suggestions for all secondary object types|


## System-Adressen

| Settings | Explanation |
|------|--------|
|Anzeigename für Absender|Name der in E-Mail für die Absenderadresse angezeigt wird.|
|Absender|E-Mail-Absender für System-E-Mails. Dies ist die Adresse, die im Empfänger-E-Mail-Programm zu sehen ist. Sofern diese Adresse nicht durch andere Header geändert wird, gehen Rückantworten ("Reply-To-E-Mails") an diese Adresse. |
|Envelope-Absender|Diese Absender-Adresse ist normalerweise unsichtbar und wird zur Verifizierung des Absenders beim E-Mail-Versand verwendet. An diese Adresse werden auch mögliche Fehler, die beim Versand einer E-Mail entstanden sind, zugestellt ("Bounce-E-Mails").|

## Log API calls 

| Settings | Explanation |
|------|--------|
| enabled |Options to choose for logs in easydb:  none, only write operations, all  |
| log the following calls | Specification of calls, which are supposed to be logged.|

> NOTE: More detailed information on the logs can be found in the [technical documentation](https://docs.easydb.de/en/technical/api/api.html) beneathe the chapter API. 


