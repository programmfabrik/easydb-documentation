---
title: "Apache2"
menu:
  main:
    name: "Apache2"
    identifier: "sysadmin/konfiguration/recipes/apache2"
    parent: "sysadmin/konfiguration/recipes"
    weight: 1
---
# Apache configuration

## HTTPS

**Enable requirered ssl modules**
```apache
a2enmod ssl
a2enmod proxy
a2enmod proxy_http
a2enmod rewrite
apache2ctl configtest
```

**Enable https**
```apache
Listen *:443
<VirtualHost *:443>
    ProxyPass / http://127.0.0.1:80/
    ProxyPassReverse / http://127.0.0.1:80/

    SSLEngine on
    SSLCertificateFile /etc/ssl/private/cert.pem
    SSLCertificateKeyFile /etc/ssl/private/key.pem
    # ggf. weitere SSL-Konfiguration je nach Ihren Anforderungen
</VirtualHost>
```

**Redirect http requests to https**
```apache
Listen 1.2.3.4:80
<VirtualHost *:80>
    RewriteEngine on
    RewriteRule ^/(.*) https://as.in.certificate.example.com/$1 [R]
</VirtualHost>
```

for more see [**this**](/en/sysadmin/konfiguration/global/apache2/https) article

## Hotfolder

```apache
<VirtualHost *:443>
	AliasMatch ^/upload(.*)$ /media/upload$1
	<Location /upload>
		ProxyPass "!"
		Require all granted
		DAV on
		Options -MultiViews
		ErrorDocument 404 "Not Found"
		ErrorDocument 500 "Internal Server Error"
		ErrorDocument 502 "Bad Gateway"
	</Location>

	ProxyPass / http://127.0.0.1:80/
	ProxyPassReverse / http://127.0.0.1:80/
	…
</VirtualHost>
```

**Enable WebDAV modules**
```apache
a2enmod dav_fs
```

for more see [**this**](/en/sysadmin/konfiguration/global/apache2/hotfolder) article

## SSO

**Enable sso modules**
```apache
a2enmod shib2
a2enmod socache_shmcb
a2enmod headers
a2enmod ssl
a2enmod rewrite
a2enmod proxy_http
a2enmod proxy
apache2ctl configtest && apache2ctl restart
```

### Kerberos

**Enable kerberos**
```apache
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
```

### Shibboleth

**Enable shibboleth**
```apache
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
```

for more see [**this**](/en/sysadmin/konfiguration/global/apache2/sso) article
