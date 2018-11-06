---
title: "44 - LDAP"
layout: config
menu:
  main:
    name: "LDAP"
    identifier: "sysadmin/konfiguration/easydb-server.yml/ldap"
    parent: "sysadmin/konfiguration/easydb-server.yml"
easydb-server.yml:
  - ldap.user.protocol
  - ldap.user.server
  - ldap.user.basedn
  - ldap.user.filter
  - ldap.group.protocol
  - ldap.group.server
  - ldap.group.basedn
  - ldap.group.filter
  - ldap.enviroment.mapping.u_login.attr
  - ldap.enviroment.mapping.u_login.regex_match
  - ldap.enviroment.mapping.u_login.regex_replace
  - ldap.enviroment.mapping.g_ldap_prefix.attr
  - ldap.enviroment.mapping.g_ldap_prefix.regex_match
  - ldap.enviroment.mapping.g_ldap_prefix.regex_replace
  - ldap.enviroment.mapping.user.login
  - ldap.enviroment.mapping.user.displayname
  - ldap.enviroment.mapping.user.email
  - ldap.enviroment.mapping.groups.attr
---
# LDAP

When enabled and configured, LDAP is used as an additional authentication method when the username and password are entered. LDAP is basically tried after easydb's own authentication and is only used if there is no easydb user with the given name.

## Enable LDAP support

LDAP is implemented as a plug-in, which must be activated explicitly:
```yaml
plugins:
  enabled+:
    - base.ldap
```

## Plugin configuration

A list of configurations (in the example given below: a configuration from the first "-") is given. The first configuration is used in which the user can be authenticated. A configuration consists of a block for authenticating the user (`user`), a group for finding linked groups (` group`) and a block for mapping the LDAP information in the easydb (`environment`).

Example configuration:

```yaml
ldap:
  - user:
      protocol: ldap
      server: ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(objectClass=posixAccount)(uid=%(Login)s))'
    group:
      protocol: ldap
      server: ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(memberUid=%(user.uid)s)(objectClass=groupOfNames))'
    environment:
      mapping:
        u_login:
          attr: user.uid
          regex_match: '$'
          regex_replace: '@LDAP'
        g_ldap_prefixed:
          attr: group.cn
          regex_match: '^'
          regex_replace: 'ldap.'
      user:
        login: '%(u_login)s'
        displayname: '%(user.givenName)s %(user.sn)s'
        email: '%(user.mail)s'
      groups:
        - attr: g_ldap_prefixed
        - attr: group.cn
```

Remarks:

- The keyword "Login" is only valid in the "user" section, not in the group section (where "user.uid" would be used instead, in the example above).
- The prefixes "user.abc" and "group.abc" are easydb syntax (not LDAP syntax) for: Use the "abc" attribute of any LDAP object that matches the rules from the "user" section Environment.user) or "group".

# Frequently Asked Questions

## How to map easydb rights to members of LDAP groups

- Create an easydb group.
- Add rights to this group by using the rights management in the web frontend.
- Map one or more LDAP groups to this easydb group.

## How to map LDAP groups to easydb goups

- In Rightsmanagement - "Groups" in the webfrontend, choose one group by clicking on it.
- Choose "Authentication Services" (German: "Anmeldedienste").
- Click on the plus sign below LDAP.
- In the new line that just appeared above the plus sign, add the correct name of the LDAP group

## How to find the correct name of the LDAP group

Depending on your LDAP configuration (see above), the correct name to use in the group mapping may be the common name of the LDAP group or the distinguished name or even some other version of the LDAP group name.

To see the group names which your easydb is comparing during mapping...:
- Log into your easydb using an LDAP account which is a member of at least one group. This group should match all requirements used in your easydb configuration (see above).
- Read the last few log messages of the easydb server which include the string `group`. Here is a typical linux command to do this:

```
grep groups /srv/easydb/easydb-server/var/imexporter.log | tail
```

The output could look like the following line:

```
[c13ea92a][2018-12-31T23:59:59.999999][    68][    INFO][           base.ldap] user record: {'_groups': ['Alle-Mitarbeiter', 'sec_Kommunikation', 'Bilderarchiv'],
```

In the example above you should use one of the three group names as written there, without the single quotes, e.g. sec_Kommunikation

## How to see the easydb groups of a login session

- In your browser, open the developer tools (typically by pressing F12 on the keyboard). We are using chrome in this example.
- Choose the "network" tab in the developer tools.
- Now log into the easydb with an LDAP account which is supposed to be in at least one easydb group.
- In the developer tools, search the "Name"-column for the string "authenticate".
- In the next column(one to the right), choose "Response".
- Search for the word "groups", e.g. by using the key combination Ctrl + f and typing the word groups with your keyboard.

## Who is allowed to login?

All accounts in LDAP are allowed to login into easydb. If you want to restrict Login to certain Groups in your LDAP, then please contact us and we will discuss the implementation.


