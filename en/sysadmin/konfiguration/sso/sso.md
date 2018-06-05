# Single Sign-On

The easydb allows the use of various single-sign-on systems, provided the protection is provided via the Apache HTTP server. Mainly supported:

* [Kerberos](#kerberos)
* [Shibboleth](#shibboleth)

However, other systems can be connected if they are based on the protection of resources in the web server and can pass the information of the authenticated user to the easydb via HTTP headers.

## Secure HTTP servers

A special URL must be protected for operation, namely `/api/v1/session/sso/authenticate`. When using docker containers, a port is already exported, on which the easydb can be reached without encryption and without single sign-on. In the following example, this is port 80, but this can also be changed when the easydb webfrontend container is started.

This step now configures an Apache HTTP server that adds HTTPS and Single Sign-On. However, the general configuration parts as well as the SSL configuration are reduced to a minimum, so that the overview is preserved. There are already numerous documentation, e.g. In the [Apache HTTP Server documentation](https://httpd.apache.org/docs/2.4/ssl/ssl_howto.html).

### Kerberos {#kerberos}

The module [`mod_auth_kerb`](http://modauthkerb.sourceforge.net/install.html) must be active for Kerberos.

~~~~
<VirtualHost *:443>
	RewriteEngine on
	RewriteRule .* - [E=X_REMOTE_USER:%{LA-F:REMOTE_USER}]
	RequestHeader set X-Remote-User "%{X_REMOTE_USER}e"

	ProxyPass / http://127.0.0.1:80/
	ProxyPassReverse / http://127.0.0.1:80/

	<Location /api/v1/session/sso/authenticate>
		AuthType Kerberos
		AuthName "Kerberos login"
		KrbServiceName HTTP/kerberos.easydb.example.com
		KrbAuthRealms EXAMPLE.COM
		Krb5Keytab /etc/apache2/krb5.keytab
		KrbMethodNegotiate off
		KrbVerifyKDC off
		KrbMethodK5Passwd on
		Require valid-user
	</Location>

	ErrorDocument 401 /web/sso_authentication_required.html

	SSLEngine on
	SSLCertificateFile /etc/ssl/private/self/cert.pem
	SSLCertificateKeyFile /etc/ssl/private/self/key.pem
</VirtualHost>
~~~~

### Shibboleth {#shibboleth}

The module [`mod_shib2`](https://wiki.shibboleth.net/confluence/display/SHIB2) is used for Shibboleth.

This module is only active for URLs, e.g. Apache are protected with `AuthType shibboleth`.

Mod_shib2 then searches among e.g. Debian 8 in `/ etc/shibboleth/shibboleth2.xml` after the values valid for your network for MetadataProvider, SessionInitiator, CredentialResolver, entityID. Changes to this file can be read with a restart of the service `shibd`.

Here is an example configuration with Apache 2.4:

~~~~
<VirtualHost *:443>
	RewriteEngine on
	RewriteRule .* - [E=X_REMOTE_USER:%{LA-F:REMOTE_USER}]
	RequestHeader set X-Remote-User "%{X_REMOTE_USER}e"

	ProxyPass /Shibboleth.sso !
	ProxyPass /shibboleth !
	ProxyPass /shibboleth-sp !
	Alias /shibboleth-sp /usr/share/shibboleth

	ProxyPass/http://127.0.0.1:80/
	ProxyPassReverse/http://127.0.0.1:80/

	<Location /api/v1/session/sso/authenticate>
		AuthType shibboleth
		ShibRequireSession on
		ShibRequestSetting requireSession 1
		ShibUseHeaders on
		Require valid-user
	</Location>

	ErrorDocument 401 /web/sso_authentication_required.html

	SSLEngine on
	SSLCertificateFile /etc/ssl/private/self/cert.pem
	SSLCertificateKeyFile /etc/ssl/private/self/key.pem
</VirtualHost>
~~~~

Under Debian 8, you enable the necessary modules. With:

~~~~
a2enmod shib2
a2enmod socache_shmcb
a2enmod headers
a2enmod ssl
a2enmod rewrite
a2enmod proxy_http
a2enmod proxy
apache2ctl configtest && apache2ctl restart
~~~~


## easydb configuration

In principle, the easydb configuration is the same for Kerberos and Shibboleth. But in Kerberos only the username is passed on to the application via HTTP headers. That is why there are also options for LDAP-queries, to get group memberships.

Easydb configuration is done in the central file `easydb5-master.yml`, located during [install](/sysadmin/installation/installation.html).

We divide the configuration into paragraphs about frontend and backend on this page, to not discuss all at once. But both parts are relevant.

### backend configuration

The `sso` plugin must be activated to have the following configuration effect.

The values of the HTTP headers can be used directly, or additional variables can be defined and edited (section `mapping`). The login name (`login`), the display name (` displayname`) and the primary e-mail address (`email`) can be set for the user (section` user`). The value can be composed of different variables. Groups are also determined from the variables, which can be divided according to a separator (section `groups`). There may be multiple sources for groups; groups are a list. The groups identified by the SSO system can be mapped to [easydb groups](../../../webfrontend/rightsmanagement/groups/groups.html) in the Web front-end.

~~~~
easydb-server:
  plugins:
    enabled+:
      - base.sso
  sso:
    environment:
      mapping:
        m_login:
          attr: REMOTE_USER
          regex_match: '@.*$'
          regex_replace: ''
      user:
        login: "%(m_login)s"
        displayname: "%(givenName)s %(sn)s"
        email: "%(eppn)s"
      groups:
        - attr: unscoped_affiliation
          divider: ';'
~~~~


### List of backend settings

This is the list of all SSO configuration settings (except those for the fronted which are shown [below](#list-of-frontend-settings)). They all reside below **easydb-server &#8614; sso**:

| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `environment`                              |               |         | Most SSO systems (such as Shibboleth) allow access to authenticated user properties using environment variables. With the following options, these variables can be used through the `sso` plugin.| |
| &#8614; `mapping`                          |               |         | with `mapping` variables can be extracted from the environment and rewritten | |
| &#8614; &#8614; `\<var\>`                  |               |         | definable variable name, which may only consist of letters and underscores | |
| &#8614; &#8614; &#8614; `attr`             | String        | Yes      | Environment variable with value of the variable to be set | |
| &#8614; &#8614; &#8614; `regex_match`      | String        | No    | Regular expression for finding parts of the attribute value. An example would be `"@.$"`to find all characters from the "@" to the end (so-called "scope"). | |
| &#8614; &#8614; &#8614; `regex_replace`    | String        | No    | Value to replace the part found by `regex_match`. The "Scope" from the example above could be replaced by an empty string (`""`) or also by a fixed value (`": shibboleth"`) | |
| &#8614; `user`                             |               |         | defines the properties of the user. Format strings can be used to define the final values for the properties from environment variables and variables defined via `mapping`. In addition to variable values, you can also use fixed texts. An example of the value of `displayname` would be `"SSO user % (givenName)s % (sn)"`: the first name (`givenName`) and last name (`sn`) are preceded by the fixed text "SSO user". | |
| &#8614; &#8614; `login`                    | Format-String | No    | Format for `login` of the SSO user | "%(eppn)s" |
| &#8614; &#8614; `displayname`              | Format-String | No    | Format for `displayname` of the SSO user | "%(displayName)s" |
| &#8614; &#8614; `email`                    | Format-String | No    | Format für primäre E-Mail des SSO-Nutzers | |
| &#8614; `groups`                           | List         |         | | |
| &#8614; &#8614; `attr`                     | String        | Yes      | Environment variable or variable set in `mapping` with GroupList | |
| &#8614; &#8614; `divider`                  | String        | No    | Separator for group list | ";" |
| `ldap`                                     |               |         | LDAP | |
| &#8614; `machine_bind`                     |               |         | Configuration for server access to the LDAP server (SSO plug-ins may need these variables) | |
| &#8614; &#8614; `url`                      | String        | No    | LDAP-Server-URL | |
| &#8614; &#8614; `who`                      | String        | No    | login (i.e. only AUTH_SIMPLE supported: User) | |
| &#8614; &#8614; `cred`                     | String        | No    | credential (i.e. only AUTH_SIMPLE supported: Password) | |

### LDAP connection

User and group information can be obtained from an LDAP server. The connection to a Microsoft Active Directory is also possible.

An example configuration would be:

~~~~
easydb-server:
  sso:
    ldap:
      machine_bind:
        url: 'ldap://ldap.example.com'
        who: 'bind-user@example.com'
        cred: 'PASSWORD'
~~~~


## Frontend configuration

There are several variables available for configuring the web front end, which are set in the `easydb5-master.yml`.

The location of `easydb5-master.yml` is chosen during the [install](/sysadmin/installation/installation.html).

> Only add those lines which are missing in your configuration.

Example 1:

~~~~
easydb-server:
  sso:
    auth_method:
      client:
        login:
          visible: true
          show_errors: true
          window_open: ""
~~~~

In example 1 the login dialog appears. In the login dialog, clicking "Use logon service" displays a window with the login dialog of your Single Sign-On System. We recommend to start with these settings.

Example 2:

~~~~
easydb-server:
  sso:
    auth_method:
      client:
        login:
          visible: true
          show_errors: true
          window_open: ""
          visually_preferred: true
~~~~

Example 2 replaces the easydb login dialog with the one of your Single Sign-On System. We recommend to use this configuration once the login has been successfully set up and tested.

Example 3:

~~~~
easydb-server:
  sso:
    auth_method:
      client:
        autostart:
		  timeout: 5000
          visible: false
          show_errors: false
          anonymous_fallback: false
        login:
          visible: true
          window_open: "height=600, width=400"
          show_errors: true
        logout:
          url: https://www.testshib.org/Shibboleth.sso/Logout
          window_open: "width=640,height=400"
~~~~

In example 3, an automatic login is explicitly configured, so the Kerberos ticket or Shibboleth token is tried first. If this does not succeed within 5 seconds, the login dialog will appear with the "Use logon service" link. Clicking on this link opens an iframe by default, but in the example a separate browser window in the size 600 x 400 pixels is opened instead. Also there is a window opened after logout.


### List of frontend settings

They are all configured below  **easydb-server &#8614; sso &#8614; auth_method &#8614; client** :

| Variable | Type | Obligation | Explanation | Default Value |
| ------------------------------------------------- | --------------- | --------- | ----------- | -------------- |
| login | | | Settings for calling the SSO login from the login dialog. Without this block, the SSO login is not visible in the login dialog ||
| &#8614; timeout | Integer | No | Number of milliseconds before the single-sign-on iframe is automatically terminated if not previously authenticated. The value 0 turns off the timeout. The timeout is only considered if `visible = false` | 5000 |
| &#8614; window_open | String | No | If set, the SSO system is opened when the login page is opened in a separate browser window. The browser window is started with the specified window.open parameters. The parameter is the *strWindowFeatures* as described in [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open). *StrWindowName* is always `\ _blank`. If set to **self**, the URL is opened inside the main window. | - |
| &#8614; visible | Boolean | No | If set, the Iframe call is displayed visibly in a modal dialog. | True |
| &#8614; show_errors | Boolean | No | If set, iframe errors are visible. | True |
| &#8614; visually_preferred | Boolean |  No | If set, the login dialog has a design with the SSO login in the foreground. | False |
| logout                                      |               |         | Configure what happens after Logout. | |
| &#8614; url                             | String       | No    | URL which is called as soon as the user logs out. By default this is done in a new browser window. | |
| &#8614; window_open                              | String       | No    | Parameters for the window.open call. Configures the new browser window. This is *strWindowFeatures* as described in [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open). If this is set to **self**, then no new window is opened but the current one is used instead. | |
| autostart | | | Settings for automatically starting the SSO logon. Without the block, Autostart is inactive | |
| &#8614; timeout | Integer | No | Number of milliseconds before the single-sign-on iframe is automatically terminated if not previously authenticated. The value 0 turns off the timeout. The timeout is only considered if **visible = false** | 5000 |
| &#8614; visible | Boolean | No | If set, the Iframe call is displayed visibly in a modal dialog. | True |
| &#8614; show_errors | Boolean | No | If set, iframe errors are visible. | True |
| &#8614; anonymous_fallback | Boolean | No | If set, attempts are made to log the user anonymously. | False |


> From the login, you can force CTRL-mouse click: `visible = true`,` show_errors = true` and `timeout = 0`. The settings for window_open are ignored with ALT mouse click.
