---
title: "LDAP"
menu:
  main:
    name: "LDAP"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/ldap"
    weight: -937
    parent: "sysadmin/configuration/easydb-server.yml/plugins"
---

# LDAP

When enabled and configured, LDAP is used as an additional authentication method when the username and password are entered. LDAP is basically tried after easydb's own authentication and is only used if there is no easydb user with the given name.

[LDAP Referrals](https://tools.ietf.org/html/rfc4511#section-4.1.10) are currently not supported. If the configured server can't supply the information, it won't be found.

## Variables

| Name of variable:                            | Type:     | Requirered: | Default:        | Description: |
| -------------------------------------------- | --------- | ----------- | --------------- | ------------ |
| `ldap:`                                      | List      | no          |                 | Contains the configuration informations about ldap servers |
| &#8193;`- user:`                             | Hierarchy | yes         |                 | Contains the ldap informations about the user login |
| &#8193;&#8193;`protocol:`                    | String    | yes         | `ldap`          | Defines the protocol to use (`ldap`/`ldaps`) |
| &#8193;&#8193;`server:`                      | String    | yes         |                 | Defines the address where easydb can reach the ldap server |
| &#8193;&#8193;`port:`                        | String    | yes         | 389             | Defines the port where easydb should listen at the remote ldap server | 
| &#8193;&#8193;`basedn:`                      | String    | yes         |                 | Defines the search level where easydb should look at the ldap server |
| &#8193;&#8193;`filter:`                      | String    | yes         |                 | Defines the search filter easydb should use, to match user entries. Example: '(&(objectClass=posixAccount)(uid=%(Login)s))' |
| &#8193;&#8193;`user:`                        | String    | no          |                 | Defines the user to search with. Must be in DN syntax. |
| &#8193;&#8193;`password:`                    | String    | no          |                 | Defines the password for the search-user |
| &#8193;`group:`                              | Hierarchy | no          |                 | Contains the ldap informations about ldap groups |
| &#8193;&#8193;`protocol:`                    | String    | yes         | `ldap`          | Defines the protocol to use (`ldap`/`ldaps`) |
| &#8193;&#8193;`server:`                      | String    | yes         |                 | Defines the address where easydb can reach the ldap server |
| &#8193;&#8193;`port:`                        | String    | yes         | 389             | Defines the port where easydb should listen at the remote ldap server | 
| &#8193;&#8193;`basedn:`                      | String    | yes         |                 | Defines the search level where easydb should look at the ldap server |
| &#8193;&#8193;`filter:`                      | String    | yes         |                 | Defines the search filter easydb should use, to match group entries. Example: '(&(objectClass=posixGroup)(memberUid=%(Login)s))' |
| &#8193;&#8193;`user:`                        | String    | no          |                 | Defines the user to search with. Must be in DN syntax. |
| &#8193;&#8193;`password:`                    | String    | no          |                 | Defines the password for the search-user |
| &#8193;`enviroment:`                         | Hierarchy | no          |                 |  |
| &#8193;&#8193;`mapping:`                     | [ ] Hierarchy | no          |                 | Contains the ldap-easydb mapping |
| &#8193;&#8193;&#8193;`<replace-me>`                 | Hierarchy | no          |                 | Sets a name for specific mapping which allows us later to to retrieve data from |
| &#8193;&#8193;&#8193;&#8193;`attr:`          | String    | yes         |                 | Defines which ldap-attribute should be mapped |
| &#8193;&#8193;&#8193;&#8193;`regex_match:`   | String    | no          |                 | Defines a regex which should be activated over the `attr` containing data |
| &#8193;&#8193;&#8193;&#8193;`regex_replace:` | String    | no          |                 | Defines a bunch of characters which should be set instead the regex-matched data |
| &#8193;&#8193;`user:`                        | Hierarchy | yes         |                 | Defines the ldap user attributes easydb should user for `login` etc. |
| &#8193;&#8193;&#8193;`login:`                | String    | yes         |                 | Defines the attribute easydb should use for user logins. Example: `'%(user.uid)s'` |
| &#8193;&#8193;&#8193;`displayname:`          | String    | no          |                 | Defines the attribute easydb should use for user displaynames. Example: `'%(user.givenName)s %(user.sn)s'` |
| &#8193;&#8193;&#8193;`email:`                | String    | no          |                 | Defines the attribute easydb should user for users emailaddress. Example: `'%(user.mail)s'`
| &#8193;&#8193;`group:`                       | List      | no          |                 | Defines a list of group attributes easydb should look for to find users groups |
| &#8193;&#8193;&#8193;`- attr:`               | String    | yes         |                 | Defines a specific group. Example: `'group.cn'` or via. mapping: `g_ldap_prefixed` |

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

Depending on your LDAP configuration (see below), the correct name to use in the group mapping may be the common name of the LDAP group or the distinguished name or even some other version of the LDAP group name.

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

In the example below you should use one of the three group names as written there, without the single quotes, e.g. sec_Kommunikation

## How to see the easydb groups of a login session

- In your browser, open the developer tools (typically by pressing F12 on the keyboard). We are using chrome in this example.
- Choose the "network" tab in the developer tools.
- Now log into the easydb with an LDAP account which is supposed to be in at least one easydb group.
- In the developer tools, search the "Name"-column for the string "authenticate".
- In the next column(one to the right), choose "Response".
- Search for the word "groups", e.g. by using the key combination Ctrl + f and typing the word groups with your keyboard.

## Who is allowed to login?

All accounts in LDAP are allowed to login into easydb. If you want to restrict Login to certain Groups in your LDAP, then please contact us and we will discuss the implementation.

# Plugin configuration

## Enable LDAP support for easydb

LDAP is implemented as a plug-in, which must be activated explicitly:
```yaml
plugins:
  enabled+:
    - base.ldap
```

## Examples

A list (indicated by the "-" after `ldap:` the example given below) of configurations is defined. The first configuration is used in which the user can be authenticated. A configuration consists of a block for authenticating the user (`user`), a group for finding linked groups (` group`) and a block for mapping the LDAP information in the easydb (`environment`).

```yml
plugins:
  enabled+:
    - base.ldap

ldap:
  - user:
      protocol: ldap
      server: first.ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(objectClass=posixAccount)(uid=%(Login)s))'
    group:
      protocol: ldap
      server: first.ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(memberUid=%(user.uid)s)(objectClass=posixGroup))'
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
```

Remarks:

- The keyword "Login" is only valid in the "user" section, not in the group section. Thus `user.uid` is used in the group section.
- The prefix "user" in `user.uid` is easydb syntax (not LDAP syntax) for: Use the "uid" attribute of any LDAP object that matches the rules from the user section (not the `environment.user` section).
- The prefix "group" in `group.cn` is easydb syntax (not LDAP syntax) for: Use the "cn" attribute of any LDAP object that matches the rules from the group section (not the `environment.groups` section).

### Addressing multiple ldap servers

```yml
plugins:
  enabled+:
    - base.ldap

ldap:
  - user:
      protocol: ldap
      server: first.ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(objectClass=posixAccount)(uid=%(Login)s))'
    group:
      protocol: ldap
      server: first.ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(memberUid=%(user.uid)s)(objectClass=posixGroup))'
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
  - user:
      protocol: ldap
      server: second.ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(objectClass=posixAccount)(uid=%(Login)s))'
    group:
      protocol: ldap
      server: second.ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(memberUid=%(user.uid)s)(objectClass=posixGroup))'
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
```

### LDAP using bind account

```yml
plugins:
  enabled+:
    - base.ldap

ldap:
  - user:
      protocol: ldap
      server: first.ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(objectClass=posixAccount)(uid=%(Login)s))'
      user: dn=cn=searchonly,ou=people,dc=example,dc=com
      password: binduserpassword
    group:
      protocol: ldap
      server: first.ldap.example.com
      basedn: dc=example,dc=com
      filter: '(&(memberUid=%(user.uid)s)(objectClass=posixGroup))'
      user: dn=cn=searchonly,ou=people,dc=example,dc=com
      password: binduserpassword
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

## Secure Connection

To use the ldaps protocol, in other words "SSL encryption", configure:

```
      protocol: ldaps
```

... instead of `protocol: ldap` in the user and group sections.

You may also need some or all of the following:

- Change the file `/etc/ldap/ldap.conf` inside(!) the container to now include the line

```
TLS_REQCERT never
```

- To make sure that your desired version of `ldap.conf` is used inside the container and endures re-creation of the container (e.g. during updates) create the easydb-server-container with an additional `volume` for this file:

```
docker run -d -ti \
[...]
    --volume $DIRECTORY_OUTSIDE_OF_CONTAINER/ldap.conf:/etc/ldap/ldap.conf \
    docker.easydb.de/pf/server-$SOLUTION
```

- Include additional root-certificates ("CA-certificates") into the container:

- To make sure that additional certificates you may need are used inside the container and endure re-creation of the container (e.g. during updates) create the easydb-server-container with an additional `volume` for the certificates' file:

```
docker run -d -ti \
[...]
    --volume $DIRECTORY_OUTSIDE_OF_CONTAINER/mycerts.pem:/etc/ssl/certs/mycerts.pem \
    docker.easydb.de/pf/server-$SOLUTION
```

