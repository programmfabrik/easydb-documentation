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

> Please check your easydb contract, whether you have licensed "authentication".

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

### Advanced regex example

The following will extract `abc012` after `OrgId=` from the attribut `Entitlement` into the easydb variable `department`. The extracted string may either stop at `;` or `:`. Example value of `Entitlement` is `Foo=abc012:Bar=kdfj8;OrgId=abc012:UId=;`

```yml
sso:
  environment:
    mapping:
      orgid:
        attr: Entitlement
        regex_match: '^.*OrgId=([^:;]*).*$'
        regex_replace: '\1'
    user:
      department: "%(orgid)s"
```

## Apache2 configuration

If programmfabrik installed your server then a good place to put the following lines is `/etc/apache2/sites-enabled/easydb5/include-before/shib.conf`.

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

As an alternative, below is a whole example apache VirtualHost:

```apache
<VirtualHost *:443>
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

    # easydb5 webfrontend docker container socket:
    ProxyPass / http://127.0.0.1:81/
    ProxyPassReverse / http://127.0.0.1:81/
</VirtualHost>
```

Note that the shibboleth directives are inside of the `<VirtualHost *:443>`-tag and have to be above the `ProxyPass(Reverse)` directives.

### shibd

To integrate easydb into shibboleth, easydb is used as a so called shibboleth "service provider" (SP). This is done by configuring the linux service `shibd` in `/etc/shibboleth/shibboleth2.xml`.

Typically an example config file for shibd is provided by the organization running the shibboleth identity provider (IDP) in their online documentation.

Here are some values that might need to be changed in such an example file:

```
<ApplicationDefaults entityID="https://your.easydbhostname.de/shibboleth"
```

```
<MetadataProvider [...]>
  <SignatureMetadataFilter certificate="/etc/shibboleth/provider-certificate.pem"/>
```

Additionally the certificate (in this example `provider-certificate.pem`) is usually provided by the organization running the IDP.

Typically, another certificate has to be configured in shibd, this time for the domain of your easydb server. Just a copy of the certificate (and key) used by the webserver should do the job:

```
<CredentialResolver type="File"
 key="/etc/shibboleth/my_cert/privkey.pem"
 certificate="/etc/shibboleth/my_cert/fullchain.pem"/>
```

Please take care that shibd can read these files and restart shibd to make your changes effective. We suggest to watch the log messages produced by shibd during such a restart to catch any errors.

If you are asked for the URL of your metadata, it should be https://your.easydbhostname.de/Shibboleth.sso/Metadata (you can test this by opening the URL in a browser - it should download or show XML).

To prevent redirection to another website, you may want to set the `redirectLimit` option in the 'Sessions' Element, see https://shibboleth.atlassian.net/wiki/spaces/SP3/pages/2065334342/Sessions

```
<Sessions
    redirectLimit="host">
```
