---
title: "Apache2"
menu:
  main:
    name: "Apache2 / HTTPS"
    identifier: "sysadmin/configuration/apache2"
    parent: "sysadmin/configuration"
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
So that requests are not rejected by HTTP but converted into HTTPS requests, e.g. The following information is required:

Apache:

```apache
Listen 1.2.3.4:80
<VirtualHost *:80>
    RewriteEngine on
    RewriteRule ^/(.*) https://as.in.certificate.example.com/$1 [R]
</VirtualHost>
```

When using port 80 through both easydb and apache, the `Listen` directive must ensure that Apache uses different IP addresses than the easydb. In this example, the easydb only uses the address of the local interface, ie 127.0.0.1.

Please replace "example.com" and "1.2.3.4" with the hostname and IP address of your server. The hostname should match the certificate.


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

for more see [**this**](/en/sysadmin/konfiguration/recipes/hotfolder) article

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

for more see [**this**](/en/sysadmin/configuration/easydb-server.yml/plugins/sso) article

# Prevent traffic without HTTPS

If you want to prevent unencrypted access, only a few changes are necessary.

## easydb startup

When you start the easydb-webfrontend, you can specify the local network interface, which can not be reached directly from outside the server.

Compared to the start in chapter [Installation](../../installation), only the penultimate row changes: It is supplemented by `127.0.0.1:`:

```bash
docker run -d -ti \
    --name easydb-webfrontend \
    --net easy5net \
    --volume=$BASEDIR/config:/config \
    -p 127.0.0.1:80:80 \
    docker.easydb.de/pf/webfrontend
```

## easydb configuration

In the central `easydb-server.yml`, whose location you set in [install](../../installation), you should change the URL from http to https:

```yaml
easydb-server:
  server:
    external_url: https://hostname.as.in.certificate.example.com
```

If you allow both http and https access, you can only specify a protocol here.

# Redirect HTTP accesses

So that requests are not rejected by HTTP but converted into HTTPS requests, e.g. The following information is required:

Apache:

```apache
Listen 1.2.3.4:80
<VirtualHost *:80>
    RewriteEngine on
    RewriteRule ^/(.*) https://as.in.certificate.example.com/$1 [R]
</VirtualHost>
```

When using port 80 through both easydb and apache, the `Listen` directive must ensure that Apache uses different IP addresses than the easydb. In this example, the easydb only uses the address of the local interface, ie 127.0.0.1.

Please replace "example.com" and "1.2.3.4" with the hostname and IP address of your server. The hostname should match the certificate.