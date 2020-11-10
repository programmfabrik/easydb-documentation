---
title: "SSO Attribute Mapping"
menu:
  main:
    name: "SSO"
    identifier: "sysadmin/configuration/easydb-server.yml/plugins/sso/attribute_mapping"
    weight: -938
    parent: "sysadmin/configuration/easydb-server.yml/plugins/sso"
---

As part of the [SSO](SSO) plugin, you may configure a mapping of SSO attributes (typically [Shibboleth](shibboleth)) to easyd variables:

## Server variables

| Name of variable:                            | Type:     | Required:   | Default:        | Description: |
| -------------------------------------------- | --------- | ----------- | --------------- | ------------ |
| `sso:`                                       | Hierarchy | no          |                 | Contains the SSO definitions for [Shibboleth](shibboleth) / [Kerberos](kerberos) |
| &#8193;`enviroment:`                         | Hierarchy | no          |                 | Contains the enviroment definitions |
| &#8193;&#8193;`mapping:`                     | Hierarchy | no          |                 | Contains the mapping definitions |
| &#8193;&#8193;&#8193;`<replaceme>`           | Hierarchy | no          |                 | Is a name defined my user for the explicit mapping (<replaceme> must be replace against a useful name for the mapping) |
| &#8193;&#8193;&#8193;&#8193;`attr:`          | String    | no          |                 | Contains the attribute-name which should be mapped |
| &#8193;&#8193;&#8193;&#8193;`regex_match:`   | String    | no          |                 | Contains a regex which should match a specific attribute content |
| &#8193;&#8193;&#8193;&#8193;`regex_replace:` | String    | no          |                 | Contains characters which should be placed instead the matched characters in `regex_match` |
| &#8193;`user:`                               | Hierarchy | no          |                 | Contains the definition for the attribute mapping into easydb |
| &#8193;&#8193;`login:`                       | String    | no          | `%(eppn)s`      | format to be used for login field |
| &#8193;&#8193;`displayname:`                 | String    | no          | `%(displayName)s`  | format to be used for display name field |
| &#8193;&#8193;`email:`                       | String    | no          |                 | format to be used for email address |
| &#8193;&#8193;`address_supplement`           | String    | no          |                 | format string. The target fields are the same as in the [User API](../../../../../technical/types/user), see there for more information. |
| &#8193;&#8193;`company`                      | String    | no          |                 | format string. |
| &#8193;&#8193;`country`                      | String    | no          |                 | format string. |
| &#8193;&#8193;`department`                   | String    | no          |                 | format string. |
| &#8193;&#8193;`first_name`                   | String    | no          |                 | format string. |
| &#8193;&#8193;`last_name`                    | String    | no          |                 | format string. |
| &#8193;&#8193;`house_number`                 | String    | no          |                 | format string. |
| &#8193;&#8193;`phone`                        | String    | no          |                 | format string. |
| &#8193;&#8193;`postal_code`                  | String    | no          |                 | format string. |
| &#8193;&#8193;`reference`                    | String    | no          |                 | format string. |
| &#8193;&#8193;`remarks`                      | String    | no          |                 | format string. |
| &#8193;&#8193;`street`                       | String    | no          |                 | format string. |
| &#8193;&#8193;`town`                         | String    | no          |                 | format string. |
| &#8193;`group:`                              | List      | no          |                 |               |
| &#8193;&#8193;`attr:`                      | String    | no          |                 | Attribute which contains the group names |
| &#8193;&#8193;`  divider:`                   | String    | no          |                 | Divider contains the character which should be usen, to divide the list of groups |
|                                              |           |             |                 |                                      |
| &#8193;`auth_method:`                        | Hierarchy | no          |                 | |
| &#8193;&#8193;`client:`                      | Hierarchy | no          |                 | |
| &#8193;&#8193;&#8193;`login:`                | Hierarchy | no          |                 | Contains the definition for the easydb-webfrontend |
| &#8193;&#8193;&#8193;&#8193;`visible:`       | Bool      | no          |                 | Definies if the sso-login button should be visible at login |
| &#8193;&#8193;&#8193;&#8193;`window_open:`   | String    | no          |                 |  |
| &#8193;&#8193;&#8193;&#8193;`show_errors:`   | Bool      | no          |                 | Allows users to see errors during SSO-login |
| &#8193;&#8193;&#8193;`logout:`               | Hierarchy | no          |                 | |
| &#8193;&#8193;&#8193;&#8193;`url:`           | String    | no          |                 | Contains the url for the logout process|
| &#8193;&#8193;&#8193;&#8193;`window_open:`   | String    | no          |                 | |

For configuration examples see [Shibboleth](shibboleth).

