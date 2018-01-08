
# Login Screen

## Registration mask

After the easydb is called up in the web browser, the login page appears.

![Registration page](login.png)

## Input

| Login | Statement | Details |
|----|--|--|
| Login | Enter your username here. ||
| Password | Enter your password here. ||
|Forgotten your password? | If you have forgotten your password, a new dialog will open here. ||
|| Dialog: Forgotten your password?| Enter your username or your registered e-mail address. Via 'Send access', a link with a nine-digit access code will be sent to the registered e-mail address. Follow the link in the e-mail and assign your new password |
|| Dialog: Confirmation | After you have sent an e-mail to your e-mail address, a dialog box opens with the confirmation of the transmission of the access code. If you do not receive an email, try again to exclude typing errors or contact the administrator |
|Search without login | If configured, users can search anonymously and without registration in shared data sets. ||
| Always directly Load the login page | Activate this checkbox if you want to always get the login dialog when you call the easydb. ||
| Stay logged in (for 1 week) | Activate this checkbox if you want to stay logged in every week for easydb. ||
| Language | If this setting is activated, a selection menu appears in the upper right corner, in which a language selection can be made. The language setting refers to the language of the system |

## Text and information for users

Texts with information for users can be displayed in the login screen (as shown in the screenshot above). Above the fields for username and password is space for a welcome text. If required there is space for another information text on the left aside the login. The texts can be defined in the [Basic configuration](.../.../administration/base-config/base-config.html#login) by an easydb administrator.

## Access for anonymous users (guests)

Records in easydb can be designated as freely searchable - i. e. a search without log in. When calling the easydb-URL, the user gets direct access to shared records (the extent of use depends on the rights settings) without having to log in. The administrator must allow the option for anonymous access in the basic configuration and distinguish the rights for the "anonymous users" group.

With the easydb-URL and "/login" appended at the end (http: //your.easydburl.de/login/), the login page opens directly with the option to search without log in (if configured).

Another option is to grant guest access to shared records, then providing access via a link including an ID. The link can be set on your own website. The guest user will be redirected to easydb and logged in with the appropriate rights. For this kind of access the URL needs to include login and password (the user "guest" with the password "guest" is transferred as follows: http: //your.easydburl.de?login=guest&password=guest\).