---
title: "easydb and Azure Active Directory"
menu:
  main:
    name: "Azure AD"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/sso/azure_ad"
    weight: -938
    parent: "sysadmin/configuration/easydb-server.yml/plugins/sso"
---

# connecting to Azure AD

As part of the [SSO](../) plugin, you may configure a connection to the Azure Active Directory (related to Microsoft Office 365 Login).

This page presents one example configuration. For more context, see the chapter [Shibboleth](../shibboleth) as Azure AD (at least inside easydb) is a special case of the more general [Shibboleth](../shibboleth). Both use "SAML" (Security Assertion Markup Language).

## Apache HTTP server configuration
Assumed:
- easydb webfrontend is listening on the localhost at port 81.
- You installed `libapache2-mod-shib2` (example name of the debian package).
- You activated the apache modules `socache_shmcb`, `headers`, `proxy`, `proxy_http` and `rewrite`.

```
                RewriteEngine on
                RewriteRule .* - [E=X_REMOTE_USER:%{LA-F:REMOTE_USER}]
                RequestHeader set X-Remote-User "%{X_REMOTE_USER}e"
                ProxyPass /Shibboleth.sso !
                ProxyPass /shibboleth !
                ProxyPass /shibboleth-sp !
                Alias /shibboleth-sp /usr/share/shibboleth
                <Location /test>
                        # to see all the transferred attributes (label and value): ...
                        AuthType shibboleth
                        ShibRequireSession on
                        ShibRequestSetting requireSession 1
                        ShibUseHeaders on
                        Require valid-user
                </Location>
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
```

Note that you can remove the `/test` block at any time. It is just for your convenience during setup.


## easydb configuration
Assumed:
- The attributes from SSO that you want to use are named `givenname`, `surname`, `emailaddress` and `usergroup`.
- `usergroup` is a string with multiple entries which are separated by `;`.

You can place the following into e.g. `/srv/easydb/config/easydb-server.d/azuread.yml`.

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
      login: "%(REMOTE_USER)s"
      displayname: "%(givenname)s %(surname)s"
      email: "%(emailaddress)s"
    groups:
      - attr: usergroup
        divider: ';'

  auth_method:
    client:
      login:
        visible: true
        window_open: ""
        show_errors: true
      logout:
        url: https://login.microsoftonline.com/common/wsfederation?wa=wsignout1.0
        window_open: ""
```

## shibd configuration

In the file `/etc/shibboleth/attribute-map.xml`:

```
<Attributes xmlns="urn:mace:shibboleth:2.0:attribute-map" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

    <Attribute name="urn:oasis:names:tc:SAML:attribute:subject-id" id="subject-id">
        <AttributeDecoder xsi:type="ScopedAttributeDecoder" caseSensitive="false"/>
    </Attribute>

    <Attribute name="urn:oasis:names:tc:SAML:attribute:pairwise-id" id="pairwise-id">
        <AttributeDecoder xsi:type="ScopedAttributeDecoder" caseSensitive="false"/>
    </Attribute>

    <Attribute name="urn:oid:1.3.6.1.4.1.5923.1.1.1.6" id="eppn">
        <AttributeDecoder xsi:type="ScopedAttributeDecoder" caseSensitive="false"/>
    </Attribute>
    <Attribute name="urn:mace:dir:attribute-def:eduPersonPrincipalName" id="eppn">
        <AttributeDecoder xsi:type="ScopedAttributeDecoder" caseSensitive="false"/>
    </Attribute>

    <Attribute name="urn:oid:1.3.6.1.4.1.5923.1.1.1.9" id="affiliation">
        <AttributeDecoder xsi:type="ScopedAttributeDecoder" caseSensitive="false"/>
    </Attribute>
    <Attribute name="urn:mace:dir:attribute-def:eduPersonScopedAffiliation" id="affiliation">
        <AttributeDecoder xsi:type="ScopedAttributeDecoder" caseSensitive="false"/>
    </Attribute>

    <Attribute name="urn:oid:1.3.6.1.4.1.5923.1.1.1.7" id="entitlement"/>
    <Attribute name="urn:mace:dir:attribute-def:eduPersonEntitlement" id="entitlement"/>

    <Attribute name="urn:oid:1.3.6.1.4.1.5923.1.1.1.10" id="persistent-id">
        <AttributeDecoder xsi:type="NameIDAttributeDecoder" formatter="$NameQualifier!$SPNameQualifier!$Name" defaultQualifiers="true"/>
    </Attribute>

    <Attribute name="urn:oasis:names:tc:SAML:2.0:nameid-format:persistent" id="persistent-id">
        <AttributeDecoder xsi:type="NameIDAttributeDecoder" formatter="$NameQualifier!$SPNameQualifier!$Name" defaultQualifiers="true"/>
    </Attribute>

    <Attribute name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name" id="userprincipalname"/>
    <Attribute name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress" id="emailaddress"/>
    <Attribute name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname" id="givenname"/>
    <Attribute name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname" id="surname"/>
    <Attribute name="usergroup" id="usergroup"/>

</Attributes>
```

In the file `/etc/shibboleth/.shibboleth2.xml`:

```
<SPConfig xmlns="urn:mace:shibboleth:2.0:native:sp:config"
    xmlns:conf="urn:mace:shibboleth:2.0:native:sp:config"
    xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
    xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol"
    xmlns:md="urn:oasis:names:tc:SAML:2.0:metadata"
    clockSkew="180">

    <OutOfProcess logger="shibd.logger">
        <Extensions>
            <Library path="adfs.so" fatal="true"/>
        </Extensions>
    </OutOfProcess>
    <InProcess logger="shibd.logger">
        <Extensions>
            <Library path="adfs-lite.so" fatal="true"/>
        </Extensions>
    </InProcess>

    <ApplicationDefaults entityID="https://archiv.kswe.ch/shibboleth"
        REMOTE_USER="userprincipalname"
        cipherSuites="DEFAULT:!EXP:!LOW:!aNULL:!eNULL:!DES:!IDEA:!SEED:!RC4:!3DES:!kRSA:!SSLv2:!SSLv3:!TLSv1:!TLSv1.1"
        signing="true" encryption="true">

        <Sessions lifetime="28800" timeout="3600" relayState="ss:mem" checkAddress="false" handlerSSL="true" cookieProps="https">

            <SSO entityID="https://sts.windows.net/288d43ef-962b-4523-b9bb-2c98269d2a7f/">
              SAML2 SAML1 ADFS
            </SSO>

            <Handler type="MetadataGenerator" Location="/Metadata" signing="false"/>

            <Handler type="Status" Location="/Status" acl="127.0.0.1 ::1 0.0.0.0"/>

            <Handler type="Session" Location="/Session" showAttributeValues="true" acl="127.0.0.1 ::1 0.0.0.0"/>

            <!-- JSON feed of discovery information. -->
            <Handler type="DiscoveryFeed" Location="/DiscoFeed"/>
        </Sessions>

        <Errors supportContact="admins@example.com"
            helpLocation="/about.html"
            styleSheet="/shibboleth-sp/main.css"/>

        <MetadataProvider type="XML" path="/etc/shibboleth/filtered-metadata.xml"/>

        <TrustEngine type="ExplicitKey"/>
        <AttributeExtractor type="XML" validate="true" reloadChanges="false" path="attribute-map.xml"/>

        <AttributeFilter type="XML" validate="true" path="attribute-policy.xml"/>

        <CredentialResolver type="File" key="sp-key.pem" certificate="sp-cert.pem"/>
    </ApplicationDefaults>

    <SecurityPolicyProvider type="XML" validate="true" path="security-policy.xml"/>

    <ProtocolProvider type="XML" validate="true" reloadChanges="false" path="protocols.xml"/>
</SPConfig>
```

> Please note that the referenced file `/etc/shibboleth/filtered-metadata.xml` was provided by our customer and was, in part, hand-crafted (for example which certificate was included). It contains, as the outer-most tag, `<EntityDescriptor [...]>[...]</EntityDescriptor>`

