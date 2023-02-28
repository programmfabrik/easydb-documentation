---
title: "SSO"
menu:
  main:
    name: "SSO"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/sso"
    weight: -938
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# SSO

The easydb allows the use of various single-sign-on systems, in conjunction with the free software "Apache" HTTP server, which then protects the easydb. Mainly supported SSO systems are:

* [Kerberos](kerberos)
* [Shibboleth](shibboleth)

Another SSO System some customer use is Active Directory. Active Directory may refer to either "Azure AD" (related to Office 365 Login), in which case you can then use the chapter [Shibboleth](shibboleth) (or in other words "SAML"). Or Active Directory may refer to the more traditional Domain Controller variant, in which case you can use the chapters [Kerberos](kerberos) and [LDAP](../ldap) (both of which are crucial parts of the Domain Controller). An example configuration for "Azure AD" can be found [here](azure_ad).

LDAP ist not a whole SSO system in itself but can be used in addition. Typically to deliver group membership information after a successfull Kerberos login.

Apart from the mentioned ones, other systems can be connected if they are based on the protection of resources in the web server and can pass the information of the authenticated user to the easydb via HTTP headers.

> HINT: Please check your easydb contract, whether you have licensed "authentication" to link easydb to any of the above.

Other relevant chapters are:

* [Mapping of SSO attributes to easydb](attribute_mapping) ("server variables")
* [Group Mapping](/en/webfrontend/rightsmanagement/groups/#authentication-services)
* [SSO Frontend Configuration](frontend_configuration) (user experience during login)
* [Label for the SSO button in the login dialogue](/de/webfrontend/administration/base-config/login/#anmeldedienste-sso)


## Enable easydb-sso-plugin

in `easydb-server.yml`:

```yaml
plugins:
  enabled+:
    - base.sso
```
