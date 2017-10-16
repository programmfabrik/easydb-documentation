# Registration page

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

## Access for anonymous users

Records in easydb can be released for free searches - i. e. for a search without log in. When calling the easydb-URL, the user gets direct access to shared records (the extent of use depends on the rights settings) without having to log in. The administrator must allow the option for anonymous access in the basic configuration and set up rights for the "anonymous users" group.

Via the easydb-URL and "/login" at the end (http://<your-easydb-url>/login\), the login page opens directly with the option to search without log in (if configured).

Another option to grant guest access to shared records, is the access via a link including an ID. The link can be set for example on your own website. The guest will be redirected directly to easydb and logged in with the appropriate rights. For this option the URL needs to include login and password (the user "guest" with the password "guest" is transferred as follows: http://<your-easydb-url>?login=gast&password=gast\).