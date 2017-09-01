# Single Sign-On

Die easydb erlaubt die Verwendung verschiedener Single-Sign-On-System, sofern die Absicherung über den Apache HTTP Server erfolgt. Hauptsächlich unterstützt werden:

* [Kerberos](#kerberos)
* [Shibboleth](#shibboleth)

Es können jedoch weitere Systeme angebunden werden, sofern sie auf der Absicherung von Ressourcen im Webserver beruhen und die Informationen des authentifizierten Nutzers über HTTP-Header an die easydb weitergeben können.

## Absicherung der HTTP-Servers

Zum Betrieb muss eine spezielle URL geschützt werden, nämlich `/api/v1/session/sso/authenticate`. Beim Betrieb über Docker-Container wird bereits ein Port exportiert, auf dem die easydb bereits unverschlüsselt und ohne Single Sign-On zu erreichen ist. Im folgenden Beispiel ist das der Port 80, das kann allerdings beim Start des easydb-webfrontend-Containers auch geändert werden.

In diesem Schritt wird nun ein Apache HTTP Server konfiguriert, der HTTPS und Single Sign-On hinzufügt. Die generellen Konfigurationsteile sowie die SSL-Konfiguration sind aber auf ein Minimum reduziert, damit die Übersicht erhalten bleibt. Hierzu gibt es bereits zahlreiche Dokumentation, z.B. in der [Apache-HTTP-Server-Dokumentation](https://httpd.apache.org/docs/2.4/ssl/ssl_howto.html).

### <a name="kerberos"></a>Kerberos

Für Kerberos muss das Modul [`mod_auth_kerb`](http://modauthkerb.sourceforge.net/) aktiv sein.

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

### <a name="shibboleth"></a>Shibboleth

Für Shibboleth wird das Modul [`mod_shib2`](https://wiki.shibboleth.net/confluence/display/SHIB2/NativeSPApacheConfig) verwendet.

Dieses Modul ist nur für URLs aktiv, die in z.B. Apache geschützt sind mit `AuthType shibboleth`.

mod_shib2 sucht dann unter z.B. Debian 8 in `/etc/shibboleth/shibboleth2.xml` nach den in Ihrem Netzwerk gültigen Werten für MetadataProvider, SessionInitiator, CredentialResolver, entityID. Änderungen an dieser Datei können mit einem Neustart vom Dienst `shibd` eingelesen werden.

Hier eine Beispiel-Konfiguration mit Apache 2.4:

~~~~
<VirtualHost *:443>
RewriteEngine on
RewriteRule .* - [E=X_REMOTE_USER:%{LA-F:REMOTE_USER}]
RequestHeader set X-Remote-User "%{X_REMOTE_USER}e"

ProxyPass /Shibboleth.sso !
ProxyPass /shibboleth !
ProxyPass /shibboleth-sp !
Alias /shibboleth-sp /usr/share/shibboleth

ProxyPass / http://127.0.0.1:80/
ProxyPassReverse / http://127.0.0.1:80/

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

Unter Debian 8 aktivieren Sie die notwendigen Module z.B. mit:

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


## easydb-Konfiguration

Prinzipiell ist die easydb-Konfiguration für Kerberos und Shibboleth ähnlich, jedoch wird bei Kerberos nur der Nutzername per HTTP-Header an die Applikation weitergereicht. Wenn mehr Informationen für die Autorisierung notwendig sind, ist momentan ein Plugin notwendig, dass kundenspezifisch implementiert wird und z.B. einen LDAP-Server nach Informationen über den Nutzer fragt.

Diese Konfiguration kommt in die zentrale Datei `easydb-server.yml`, deren Speicherort Sie bei der [Installation](/sysadmin/installation/installation.md) festgelegt haben.

Die komplette Liste der Optionen ist im Kapitel [YAML-Dateien](/sysadmin/konfiguration/yaml/yaml.md) aufgeführt.

### gemeinsame Konfiguration

Das `sso`-Plugin muss aktiviert sein, damit die folgende Konfiguration Wirkung zeigt.

Die Werte der HTTP-Header können direkt benutzt werden oder es können eigene Variablen definiert und nachbearbeitet werden (Abschnitt `mapping`). Für den Nutzer können der Login-Name (`login`), der Darstellungsname (`displayname`) und die primäre E-Mail-Adresse (`email`) gesetzt werden (Abschnitt `user`). Dabei kann jeweils der Wert aus verschiedenen Variablen zusammengesetzt werden. Gruppen werden auch aus den Variablen ermittelt, diese können nach einem Trennzeichen aufgeteilt werden (Abschnitt `groups`). Es kann mehrere Quellen für Gruppen geben, es handelt sich bei `groups` um eine Liste. Diese aus dem SSO-System ermittelten Gruppen können im Webfrontend auf [easydb-Gruppen](/webfrontend/rightsmanagement/groups/groups.md) abgebildet werden.

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

### kundenspezifisches Plugin mit LDAP-Anbindung

Mit einem Plugin können Nutzer- und Gruppen-Informationen aus einem LDAP-Server bezogen werden. Auch die Anbindung an ein Microsoft Active Directory ist möglich.

Ein Beispiel für die Konfiguration des Plugins wäre:

~~~~
easydb-server:
sso:
ldap:
machine_bind:
url: 'ldap://ldap.example.com'
who: 'bind-user@example.com'
cred: 'PASSWORD'
~~~~


## Frontend-Konfiguration

Für die Konfiguration des Webfrontends stehen verschiedene Variablen zur Verfügung, die in der .yml eingestellt werden.

Beipiel 1:

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

> Im Beispiel 1 wird ein automatischer Login probiert, sinnvoll falls die Eingabe der Kennung nicht notwendig ist (sondern z.B. ein Kerberos-Ticket verwendet wird). Sollte das binnen 5 Sekunden nicht gelingen, erscheint der Login-Dialog mit dem Link "Anmeldedienst verwenden". Ein Klick auf diesen Link öffnet per default ein iframe, aber im Beispiel statt dessen ein separates Browser-Fenster in der Größe 600 x  400 Pixel, mit der in Shibboleth konfigurierten URL.

Beipiel 2:

~~~~
easydb-server:
sso:
auth_method:
client:
login:
visible: true
show_errors: true
~~~~

> Im Beispiel 2 wird kein automatischer Login probiert, Es erscheint der Login-Dialog. Im Login Dialog wird bei Klick auf "Anmeldedienst verwenden" ein iframe angezeigt, mit der in Shibboleth konfigurierten URL.


Die Variablen werden alle im Pfad **sso &#8614; auth_method &#8614; client** konfiguriert.


| Variable                                         | Typ           | Pflicht | Erklärung | Default-Wert |
|--------------------------------------------------|---------------|---------|-----------|--------------|
| login                                        |               |         | Einstellungen zum Aufruf der SSO-Anmeldung vom Login-Dialog aus. Ohne diesen Block ist die SSO-Anmeldung nicht im Login-Dialog sichtbar.| |
| &#8614; timeout                                | Integer       | Nein    | Anzahl der Millisekunden bevor der Single-Sign-On-Iframe automatisch beendet wird, wenn nicht vorher authentifiziert wurde. Der Wert 0 schaltet den Timeout aus. Der Timeout wird nur berücksichtigt, wenn `visible=false` ist.| 5000 |
| &#8614; window_open                              | String       | Nein    | Wenn gesetzt, wird das SSO-System beim Aufruf von der Login-Seite in einem separaten Browser-Fenster geöffnet. Das Browser-Fenster wird mit den angegebenen window.open Parametern gestartet. Der Parameter ist der *strWindowFeatures* wie in [window.open](https://developer.mozilla.org/en-US/docs/Web/API/Window/open) beschrieben. *strWindowName* ist immer `\_blank`. | - |
| &#8614; visible                                  | Boolean       | Nein    | Wenn gesetzt, wird der Iframe-Aufruf sichtbar in einem Modal-Dialog angezeigt. | true |
| &#8614; show_errors                               | Boolean       | Nein    | Wenn gesetzt, wird bei Fehlern der Iframe sichtbar. | true |
| &#8614; visually_preferred                        | Boolean       | Nein    | Wenn gesetzt, hat der Login-Dialog ein Design bei dem das SSO-Login im Vordergrund steht. | false |
| autostart                                    |               |         | Einstellungen zum automatischen Start des SSO-Anmeldung. Ohne den Block, ist Autostart inaktiv.| |
| &#8614; timeout                                | Integer       | Nein    | Anzahl der Millisekunden bevor der Single-Sign-On-Iframe automatisch beendet wird, wenn nicht vorher authentifiziert wurde. Der Wert 0 schaltet den Timeout aus. Der Timeout wird nur berücksichtigt, wenn **visible=false** ist.| 5000 |
| &#8614; visible                                  | Boolean       | Nein    | Wenn gesetzt, wird der Iframe-Aufruf sichtbar in einem Modal-Dialog angezeigt. | true |
| &#8614; show_errors                               | Boolean       | Nein    | Wenn gesetzt, wird bei Fehlern der Iframe sichtbar. | true |
| &#8614; anonymous_fallback                       | Boolean       | Nein    | Wenn gesetzt, wird bei Fehlern versucht den Benutzer anonym anzumelden. | false |


> Vom Login aus kann man mit CTRL-Mausklick erzwingen: `visible=true`, `show_errors=true` und `timeout=0`. Mit ALT-Mausklick werden die Einstellungen für window_open ignoriert.
