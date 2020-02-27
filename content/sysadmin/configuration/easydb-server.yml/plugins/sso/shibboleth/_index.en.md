---
title: "Shibboleth"
menu:
  main:
    name: "Shibboleth"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/sso/shibboleth"
    weight: -950
    parent: "sysadmin/configuration/easydb-server.yml/plugins/sso"
---

# Shibboleth

## Installation

```bash
apt-get install libapache2-mod-shib2
```

Activate apache2 requirements
```bash
a2enmod socache_shmcb
a2enmod headers
```

## SSO activation in easydb5

A list of all available variables for the sso configuration, can be found at: [SSO](../)

As programmfabrik we recommend any one, to split their configuration into different files. During this task, we will create a `shib.yml` located at `/srv/easydb/config/easydb-server.d/`. As valid configuration for the shibboleth sso service, you can take a look at the following example:

```yml
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
      displayname: "%(cn)s"
      email: "%(mail)s"
    groups:
      - attr: affiliation
        divider: ';'

  auth_method:
    client:
      login:
        visible: true
        window_open: ""
        show_errors: true
      logout:
        url: https://easydb.example.com/Shibboleth.sso/Logout
        window_open: ""
```

## Apache2 configuration

The following configuration assumes that you have configured https.

Add following lines to `/etc/apache2/sites-enabled/easydb.conf` below `<VirtualHost *:443>` but before `ProxyPass / http://127.0.0.1:81/` or `ProxyPassReverse / http://127.0.0.1:81/`
```apache2
# shibboleth
RewriteEngine on
RewriteRule .* - [E=X_REMOTE_USER:%{LA-F:REMOTE_USER}]
RequestHeader set X-Remote-User "%{X_REMOTE_USER}e"
ProxyPass /Shibboleth.sso !
ProxyPass /shibboleth !
ProxyPass /shibboleth-sp !

Alias /shibboleth-sp /usr/share/shibboleth
<Location /api/v1/session/sso/authenticate>
    AuthType shibboleth
    ShibRequireSession on
    ShibRequestSetting requireSession 1
    ShibUseHeaders on
    Require valid-user
</Location>
ErrorDocument 401 /web/sso_authentication_required.html
```

### Complete Apache2 example

```apache
<VirtualHost *:443>
    ServerAdmin administratoren@programmfabrik.de

    SSLEngine on
    SSLCertificateFile  /etc/ssl/cert.pem
    SSLCertificateKeyFile /etc/ssl/private/server-key.pem

    # shibboleth
    RewriteEngine on
    RewriteRule .* - [E=X_REMOTE_USER:%{LA-F:REMOTE_USER}]
    RequestHeader set X-Remote-User "%{X_REMOTE_USER}e"
    ProxyPass /Shibboleth.sso !
    ProxyPass /shibboleth !
    ProxyPass /shibboleth-sp !
    Alias /shibboleth-sp /usr/share/shibboleth
    <Location /api/v1/session/sso/authenticate>
        AuthType shibboleth
        ShibRequireSession on
        ShibRequestSetting requireSession 1
        ShibUseHeaders on
        Require valid-user
    </Location>
    ErrorDocument 401 /web/sso_authentication_required.html

    ProxyPass / http://127.0.0.1:81/
    ProxyPassReverse / http://127.0.0.1:81/
</VirtualHost>
```