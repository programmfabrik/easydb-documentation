# Single Sign-On

The easydb allows the use of various single-sign-on systems, provided the protection is provided via the Apache HTTP server. Mainly supported:

* [Kerberos](#kerberos)
* [Shibboleth](#shibboleth)

However, other systems can be connected if they are based on the protection of resources in the web server and can pass the information of the authenticated user to the easydb via HTTP headers.

## Secure HTTP servers

A special URL must be protected for operation, namely `/api/v1/session/sso/authenticate`. When using docker containers, a port is already exported, on which the easydb can be reached without encryption and without single sign-on. In the following example, this is port 80, but this can also be changed when the easydb webfrontend container is started.

This step now configures an Apache HTTP server that adds HTTPS and Single Sign-On. However, the general configuration parts as well as the SSL configuration are reduced to a minimum, so that the overview is preserved. There are already numerous documentation, e.g. In the [Apache HTTP Server documentation](https://httpd.apache.org/docs/2.4/ssl/ssl_howto.html).

### <a name="kerberos"> </a> Kerberos

The module [`mod_auth_kerb`](http://modauthkerb.sourceforge.net/) must be active for Kerberos.

~~~~
<VirtualHost *:443>
	RewriteEngine on
	RewriteRule .* -[E=X_REMOTE_USER:%{LA-F:REMOTE_USER}]
	RequestHeader set X-Remote-User "%{X_REMOTE_USER}e"

	ProxyPass/http://127.0.0.1:80/
	ProxyPassReverse/http://127.0.0.1:80/

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

### <a name="shibboleth"></a>Shibboleth

The module [`mod_shib2`](https://wiki.shibboleth.net/confluence/display/SHIB2/NativeSPApacheConfig) is used for Shibboleth.

This module is only active for URLs, e.g. Apache are protected with `AuthType shibboleth`.

Mod_shib2 then searches among e.g. Debian 8 in `/ etc/shibboleth/shibboleth2.xml` after the values valid for your network for MetadataProvider, SessionInitiator, CredentialResolver, entityID. Changes to this file can be read with a restart of the service `shibd`.

Here is an example configuration with Apache 2.4:

~~~~
<VirtualHost *:443>
	RewriteEngine on
	RewriteRule .* -[E=X_REMOTE_USER:%{LA-F:REMOTE_USER}]
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

In principle, the easydb configuration is similar for Kerberos and Shibboleth, but in Kerberos, only the username is passed on to the application via HTTP headers. If more information is required for the authorization, a plug-in is currently required that is specifically implemented by the customer and, e.g. An LDAP server asks for information about the user.

This configuration comes in the central file `easydb-server.yml`, whose location you set in [install](/docs/sysadmin/installation).

For the complete list of options, see [YAML files](/docs/sysadmin/config/yaml).

### common configuration

The `sso` plugin must be activated to have the following configuration effect.

The values ​​of the HTTP headers can be used directly, or their own variables can be defined and edited (section `mapping`). The login name (`login`), the display name (` displayname`) and the primary e-mail address (`email`) can be set for the user (section` user`). The value can be composed of different variables. Groups are also determined from the variables, which can be divided according to a separator (section `groups`). There may be multiple sources for groups; groups are a list. The groups identified by the SSO system can be mapped to [easydb groups](/docs/webfrontend/rightsmanagement/groups) in the Web front-end.

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

### Customer-specific plugin with LDAP connection

With a plug-in, user and group information can be obtained from an LDAP server. The connection to a Microsoft Active Directory is also possible.

An example for configuring the plugin would be:

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

There are several variables available for configuring the web front end, which are set in the .yml.

Example 1:

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
~~~~

> In example 1, an automatic login is tried, if the entry of the identifier is not necessary (for example, a Kerberos ticket is used). If this does not happen within 5 seconds, the login dialog will appear with the "Use logon service" link. Clicking on this link opens by default iframe, but in the example instead a separate browser window in the size 600 x 400 pixels, with the URL configured in Shibboleth.

Example 2:

~~~~
easydb-server:
  sso:
    auth_method:
      client:
        login:
          visible: true
          show_errors: true
~~~~

> In example 2 no automatic login is tried, the login dialog appears. In the login dialog, clicking "Use logon service" displays an iframe with the URL configured in Shibboleth.


The variables are all configured in path **sso &#8614; auth_method &#8614; client** .


| Variable | Type | Obligation | Explanation | Default Value |
| ------------------------------------------------- | --------------- | --------- | ----------- | -------------- |
| Login | | | Settings for calling the SSO login from the login dialog. Without this block, the SSO login is not visible in the login dialog ||
| &#8614; timeout | Integer | No | Number of milliseconds before the single-sign-on iframe is automatically terminated if not previously authenticated. The value 0 turns off the timeout. The timeout is only considered if `visible = false` | 5000 |
| &#8614; window_open | String | No | If set, the SSO system is opened when the login page is opened in a separate browser window. The browser window is started with the specified window.open parameters. The parameter is the *strWindowFeatures* as described in [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open). *StrWindowName* is always `\ _blank`. | - |
| &#8614; visible | Boolean | No | If set, the Iframe call is displayed visibly in a modal dialog. | True |
| &#8614; show_errors | Boolean | No | If set, iframe errors are visible. | True |
| &#8614; visually_preferred | Boolean |  No | If set, the login dialog has a design with the SSO login in the foreground. | False |
| Autostart | | | Settings for automatically starting the SSO logon. Without the block, Autostart is inactive | |
| &#8614; timeout | Integer | No | Number of milliseconds before the single-sign-on iframe is automatically terminated if not previously authenticated. The value 0 turns off the timeout. The timeout is only considered if **visible = false** | 5000 |
| &#8614; visible | Boolean | No | If set, the Iframe call is displayed visibly in a modal dialog. | True |
| &#8614; show_errors | Boolean | No | If set, iframe errors are visible. | True |
| &#8614; anonymous_fallback | Boolean | No | If set, attempts are made to log the user anonymously. | False |


> From the login, you can force CTRL-mouse click: `visible = true`,` show_errors = true` and `timeout = 0`. The settings for window_open are ignored with ALT mouse click.
