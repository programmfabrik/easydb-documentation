# General

## Name of easydb

| Settings | Explanation |
|------|--------|
|Name of the easydb| The name of the easydb is used as the directory name and ZIP prefix for exports. This name also appears in logs and administrator emails. |
| Display name | Name of the easydb as it is displayed in the web browser (as document title). This field is multilingual.|

## Languages

| Settings | Explanation |
|------|--------|
| Database | The database languages ​​are the languages, which are ​​available to users for data modeling and input as well as search. <br><br>NOTE: The system right "Modify data model > Commit changes" is required for changing the database languages. To activate the changed database languages, you must rewrite the index. This is achieved by saving the data model again and commiting the changes.<br><br>_The listed languages ​​are defined on the server and can not be changed._|
| Frontend |The frontend languages ​​are the languages, which are ​​available for users. <br><br>_The listed languages ​​are defined on the server and can not be changed._ |

## Administrator-E-Mails

| Settings | Explanation |
|------|--------|
|Administrator emails|The Administrator email adress can be specified to send easydb emails. This address is used for events like server_start, server_shutdown, ...|

## Permitted origin address

| Settings | Explanation |
|------|--------|
|Permitted origins| Permitted URL origins from which browser access is allowed. The URLs must be complete containing the application protocoll. For example "http://myown.easydb.api.example.com" |

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


## E-mail addresses of the system

| Settings | Explanation |
|------|--------|
|Display name for sender|Name of sender, which is displayed instead of the e-mail address for sender emails.|
|Sender|E-mail sender for system e-mails. This is the address that can be seen in the recipient e-mail program. Unless this address is changed by other headers, replies ("reply-to-emails") are sent to this address. |
|Envelope sender|This sender address is normally invisible and is used to verify the sender when sending e-mails. Errors emails that may have occurred while using easydb are sent to this email address ("bounce emails").|

## Log API calls 

| Settings | Explanation |
|------|--------|
| enabled |Options to choose for logs in easydb:  none, only write operations, all  |
| log the following calls | Specification of calls, which are supposed to be logged.|

> NOTE: More detailed information on the logs can be found in the [technical documentation](https://docs.easydb.de/en/technical/api/api.html) beneathe the chapter API. 


