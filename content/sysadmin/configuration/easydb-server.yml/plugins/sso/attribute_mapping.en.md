---
title: "SSO Attribute Mapping"
menu:
  main:
    name: "Attribute Mapping"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/sso/attribute_mapping"
    weight: -938
    parent: "sysadmin/configuration/easydb-server.yml/plugins/sso"
---

As part of the [SSO](../) plugin, you may configure a mapping of SSO attributes (typically [Shibboleth](../shibboleth)) to easydb variables:

## Attribute Mapping

Mapping of SSO attributres to easydb server variables:

| Name of yaml element:                        | Type:     | Required:   | Default:        | Description: |
| -------------------------------------------- | --------- | ----------- | --------------- | ------------ |
| `sso`                                        | Hierarchy | no          |                 | Contains the SSO definitions for [Shibboleth](../shibboleth) / [Kerberos](../kerberos) |
| &#8680;`environment`                         | Hierarchy | no          |                 | Contains the environment definitions |
| &#8680;&#8680;`mapping`                     | Hierarchy | no          |                 | Contains the mapping definitions |
| &#8680;&#8680;&#8680;`<a_name>`           | Hierarchy | no          |                 | Is a name defined my user for the explicit mapping (must be replaced with a useful name for the mapping) |
| &#8680;&#8680;&#8680;&#8680;`attr`          | String    | no          |                 | Contains the attribute-name which should be mapped |
| &#8680;&#8680;&#8680;&#8680;`regex_match`   | String    | no          |                 | Contains a regex which should match a specific attribute content |
| &#8680;&#8680;&#8680;&#8680;`regex_replace` | String    | no          |                 | Contains characters which should be placed instead the matched characters in `regex_match` |
| &#8680;&#8680;`user`                               | Hierarchy | no          |                 | Contains the definition for the attribute mapping into easydb |
| &#8680;&#8680;&#8680;`login`                       | String    | no          | `%(eppn)s`      | format to be used for login field |
| &#8680;&#8680;&#8680;`displayname`                 | String    | no          | `%(displayName)s`  | format to be used for display name field |
| &#8680;&#8680;&#8680;`email`                       | String    | no          |                 | format to be used for email address |
| &#8680;&#8680;&#8680;`address_supplement`           | String    | no          |                 | format string. The target fields are the same as in the [User API](../../../../../../technical/types/user), see there for more information. |
| &#8680;&#8680;&#8680;`company`                      | String    | no          |                 | format string. |
| &#8680;&#8680;&#8680;`country`                      | String    | no          |                 | format string. |
| &#8680;&#8680;&#8680;`department`                   | String    | no          |                 | format string. |
| &#8680;&#8680;&#8680;`first_name`                   | String    | no          |                 | format string. |
| &#8680;&#8680;&#8680;`last_name`                    | String    | no          |                 | format string. |
| &#8680;&#8680;&#8680;`house_number`                 | String    | no          |                 | format string. |
| &#8680;&#8680;&#8680;`phone`                        | String    | no          |                 | format string. |
| &#8680;&#8680;&#8680;`postal_code`                  | String    | no          |                 | format string. |
| &#8680;&#8680;&#8680;`reference`                    | String    | no          |                 | format string. |
| &#8680;&#8680;&#8680;`remarks`                      | String    | no          |                 | format string. |
| &#8680;&#8680;&#8680;`street`                       | String    | no          |                 | format string. |
| &#8680;&#8680;&#8680;`town`                         | String    | no          |                 | format string. |
| &#8680;&#8680;`group`                              | List      | no          |                 |               |
| &#8680;&#8680;&#8680;`attr`                      | String    | no          |                 | Attribute which contains the group names |
| &#8680;&#8680;&#8680;`divider`                   | String    | no          |                 | Divider contains the character which should be usen, to divide the list of groups |
|                                              |           |             |                 |                                      |
| &#8680;`auth_method`                        | Hierarchy | no          |                 | |
| &#8680;&#8680;`client`                      | Hierarchy | no          |                 | |
| &#8680;&#8680;&#8680;`login`                | Hierarchy | no          |                 | Contains the definition for the easydb-webfrontend |
| &#8680;&#8680;&#8680;&#8680;`visible`       | Bool      | no          |                 | Definies if the sso-login button should be visible at login |
| &#8680;&#8680;&#8680;&#8680;`window_open`   | String    | no          |                 |  |
| &#8680;&#8680;&#8680;&#8680;`show_errors`   | Bool      | no          |                 | Allows users to see errors during SSO-login |
| &#8680;&#8680;&#8680;`logout`               | Hierarchy | no          |                 | |
| &#8680;&#8680;&#8680;&#8680;`url`           | String    | no          |                 | Contains the url for the logout process|
| &#8680;&#8680;&#8680;&#8680;`window_open`   | String    | no          |                 | |

Configuration example:

```yml
sso:
  environment:
    mapping:
      modified_login:
        attr: REMOTE_USER
        regex_match: '@.*$'
        regex_replace: ''
    user:
      login: "%(modified_login)s"
      displayname: "%(cn)s"
      email: "%(mail)s"
    groups:
      - attr: affiliation
        divider: ';'
```

For more examples see [Shibboleth](../shibboleth).

