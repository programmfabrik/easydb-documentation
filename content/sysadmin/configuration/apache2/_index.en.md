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
<VirtualHost *:443>
    ProxyPass / http://127.0.0.1:81/
    ProxyPassReverse / http://127.0.0.1:81/

    SSLEngine on
    SSLCertificateFile /etc/ssl/private/cert.pem
    SSLCertificateKeyFile /etc/ssl/private/key.pem
</VirtualHost>
```

**Redirect http requests to https** so that requests are not rejected by HTTP but converted into HTTPS requests, e.g. the following information is required:

Apache:

```apache
<VirtualHost *:80>
    RewriteEngine on
    RewriteRule ^/(.*) https://as.in.certificate.example.com/$1 [R]
</VirtualHost>
```

## easydb startup

When you start the easydb-webfrontend, you can specify the local network interface, which also fits the apache config example above.

Compared to the start in chapter [Installation](../../installation), only the row with `-p` changes:

```bash
docker run -d -ti \
    ...
    -p 127.0.0.1:81:80 \
    docker.easydb.de/pf/webfrontend
```

## easydb configuration

In the central `easydb-server.yml`, whose location you set in [install](../../installation), you should change the URL from http to https:

```yaml
easydb-server:
  server:
    external_url: https://hostname.as.in.certificate.example.com
```

## Hotfolder

If you are interested in hotfolder configuration, please read the plugin article about the [hotfolder-plugin](/en/sysadmin/configuration/easydb-server.yml/plugins/hotfolder)

## SSO

If you are interested in single-sign-on (SSO) configuration, please read the plugin article about the [SSO](/en/sysadmin/configuration/easydb-server.yml/plugins/sso)
