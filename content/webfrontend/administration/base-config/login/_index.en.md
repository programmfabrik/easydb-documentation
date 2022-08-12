---
title: "158 - Login"
menu:
  main:
    name: "Login"
    identifier: "webfrontend/administration/base-config/login"
    parent: "webfrontend/administration/base-config"
---
# Log In {#login}

You can make settings for the login under this tab.

| Settings | | Explanation |
| ------ | ---- | -------- |
|Use cookies for session protection ||Cookies can be activated for the session token. This makes it difficult to copy links to sessions, since the HTTP request for the token also requires the cookie. [*Go to entry in the technical documentation*](https://docs.easydb.de/en/technical/api/session)|
| Anonymous over Internet allowed || When calling the main easydb URL (http://<easydb-server>/), this setting specifies that an unknown user is logged into the system as an anonymous user. Each anonymous user is automatically in the group `Anonymous user` and can be given rights. Easydb stores a browser cookie with the user, which he will be recognized the next time and assigned internally to the same user ID. This allows the user to save user settings, etc. Whether or not a user comes from the Internet is defined by _Intranet configuration_ |
| Anonymous over Intranet allowed || How *allows Anonymous over Internet* only that this setting applies to users who have been recognized as intranet users|
| Intranet configuration | | Here, IP addresses (172.16.0.2) and networks (eg 192.168.0.0/16) are stored, which are valid as _Intranet_. When the server is called, the IP address of the call is determined and a corresponding classification is made |
| User can initiate a forgotten password process. || If active, the user is offered to log on to the login page via his registered email address a forgotten password. This setting is valid for all users. It can not be restricted (ugs) |
| Wallpaper | | For the login page, a background image can be uploaded. A default image is set in the .ini variable `[default-pics] background`. Make sure the image is large so that no artifacts are visible for large screens |
| Information next to the login | | An information for the user can be stored here. The text is displayed in the login dialog next to the login. Only text (markdown) is allowed, no HTML. |
| Welcome text | | The welcome text can be stored in multiple languages ​​for the login page. Here is only text (markdown) allowed, no HTML |
| Password Verification | Policy | Set +/- rules to verify user passwords. The password is checked using a regular expression. With _Minimum_ and _Maximum_ they determine how often the regular expression must be found at least and can be found at most. One or more regular expressions can be defined. The check is only done for new passwords. It is not done for existing passwords. |
| | Note | The multilingual text tells the user what he has to do with his password |
| Repeat passwords | | Easydb saves all passwords (encrypted) used by the user. For reused passwords, you can specify how old a password may be |
| | _Always_ | A password must never be reused. |
| | _Month_ | A password can not be reused in the same month. |
| | _Never_ | The server turns off the check for repeated passwords. |
|Label for the button to switch to the easydb login screen | | Text to be displayed on the button to switch from the SSO login screen to the easydb login screen. Input fields for login and password are displayed there. Used only if easydb starts with SSO login page by default (Server-YML: visually_preferred: true) |
|Label for the button to switch to the SSO service | | Text to be displayed on the button that redirects the user to the SSO service. |
|Label for the button to switch to the SSO login screen | | Text to be displayed on the button to switch from the easydb login screen to the SSO login screen. No more input fields for login and password will be displayed there. Used only if easydb starts with SSO login screen by default and you switched to easydb login screen manually (Server-YML: visually_preferred: true) |
