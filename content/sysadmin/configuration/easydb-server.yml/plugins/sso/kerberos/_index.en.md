---
title: "Kerberos"
menu:
  main:
    name: "Kerberos"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/sso/kerberos"
    weight: -949
    parent: "sysadmin/configuration/easydb-server.yml/plugins/sso"
---

# Kerberos

> Please check your easydb contract, whether you have licensed "authentication".

## Installation

Install modules needed for the apache2 to use kerberos as sso service:

### Debian 11, 12, 13
```bash
apt install libapache2-mod-auth-gssapi
```

### until Debian 10
```bash
apt install libapache2-mod-auth-kerb krb5-user
```

## SSO activation in easydb5

A list of all available variables for the sso configuration, can be found at: [SSO](../)

As programmfabrik we recommend any one, to split their configuration into different files. During this task, we will create a `kerberos.yml` located at `/srv/easydb/config/easydb-server.d/`. Since no groups are sent via. kerberos, the groups must be fetched from the ldap. As valid configuration for the kerberos sso service, you can take a look at the following example:

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
  auth_method:
    client:
      login:
        visible: true
        show_errors: true

ldap:
  - user:
      protocol: ldap
      server: ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(objectClass=user)(sAMAccountName=%(Login)s))'
    group:
      protocol: ldap
      server: ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(|(member=%(user.distinguishedName)s)(gidNumber=%(user.primaryGroupID)s))(objectClass=group))'
    environment:
      user:
        login: '%(user.sAMAccountName)s'
        displayname: '%(user.displayName)s'
      groups:
        - attr: group.cn
```

For mor informations about ldap see [ldap](../../ldap)

## Apache2 configuration

### sample for libapache2-mod-auth-gssapi

```conf
    RequestHeader set X-Remote-User "%{REMOTE_USER}s"

    <Location /api/v1/session/sso/authenticate>
        AuthType GSSAPI
        AuthName "Kerberos login"
        GssapiBasicAuth On
        GssapiLocalName On
        GssapiCredStore keytab:/PATH/TO/krb.KEYTAB
        Require valid-user
    </Location>
```
Make your keytab file readable for linux-user www-data.

### sample for libapache2-mod-auth-kerb

The following configuration assumes that you have configured https.

Add following lines to `/etc/apache2/sites-enabled/easydb.conf` below `<VirtualHost *:443>`

Before `ProxyPass`/`ProxyPassReverse`:
```conf
RewriteEngine on
RewriteRule .* - [E=X_REMOTE_USER:%{LA-F:REMOTE_USER}]
RequestHeader set X-Remote-User "%{X_REMOTE_USER}e"
```

After `ProxyPass`/`ProxyPassReverse`:
```conf
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
```

### Complete Apache2 example

```conf
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
