---
title: "Apache2"
menu:
  main:
    name: "Apache2"
    identifier: "sysadmin/konfiguration/apache2"
    parent: "sysadmin/konfiguration"
---
# Apache configuration

## HTTPS

**Enable requirered ssl modules**
{{< getFileContent file="/content/sysadmin/konfiguration/includes/apache2/enable-ssl-modules.md" markdown="true" >}}

**Enable https**
{{< getFileContent file="/content/sysadmin/konfiguration/includes/apache2/enable-https.md" markdown="true" >}}

**Redirect http requests to https**
{{< getFileContent file="/content/sysadmin/konfiguration/includes/apache2/redirect-http-to-https.md" markdown="true" >}}

for more see [**this**](/en/sysadmin/konfiguration/https) article

## Hotfolder

{{< getFileContent file="/content/sysadmin/konfiguration/includes/apache2/enable-hotfolder.md" markdown="true" >}}

**Enable WebDAV modules**
{{< getFileContent file="/content/sysadmin/konfiguration/includes/apache2/enable-webdav-module.md" markdown="true" >}}

for more see [**this**](/en/sysadmin/konfiguration/hotfolder) article

## SSO

**Enable sso modules**
{{< getFileContent file="/content/sysadmin/konfiguration/includes/apache2/enable-sso-modules.md" markdown="true" >}}

### Kerberos

**Enable kerberos**
{{< getFileContent file="/content/sysadmin/konfiguration/includes/apache2/sso-kerberos-with-https.md" markdown="true" >}}

### Shibboleth

**Enable shibboleth**
{{< getFileContent file="/content/sysadmin/konfiguration/includes/apache2/sso-shibboleth-with-https.md" markdown="true" >}}

for more see [**this**](/en/sysadmin/konfiguration/sso) article
