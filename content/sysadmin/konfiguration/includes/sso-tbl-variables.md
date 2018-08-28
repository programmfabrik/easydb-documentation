| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `environment`                              |               |         | Most SSO systems (such as Shibboleth) allow access to authenticated user properties using environment variables. With the following options, these variables can be used through the `sso` plugin.| |
| `enviroment.mapping`                          |               |         | with `mapping` variables can be extracted from the environment and rewritten | |
| `enviroment.mapping.<var>`                  |               |         | definable variable name, which may only consist of letters and underscores | |
| `enviroment.mapping.<var>.attr`             | String        | Yes      | Environment variable with value of the variable to be set | |
| `enviroment.mapping.<var>.regex_match`      | String        | No    | Regular expression for finding parts of the attribute value. An example would be `"@.$"`to find all characters from the "@" to the end (so-called "scope"). | |
| `enviroment.mapping.<var>.regex_replace`    | String        | No    | Value to replace the part found by `regex_match`. The "Scope" from the example above could be replaced by an empty string (`""`) or also by a fixed value (`": shibboleth"`) | |
| `enviroment.user`                             |               |         | defines the properties of the user. Format strings can be used to define the final values for the properties from environment variables and variables defined via `mapping`. In addition to variable values, you can also use fixed texts. An example of the value of `displayname` would be `"SSO user % (givenName)s % (sn)"`: the first name (`givenName`) and last name (`sn`) are preceded by the fixed text "SSO user". | |
| `enviroment.user.login`                    | Format-String | No    | Format for `login` of the SSO user | "%(eppn)s" |
| `enviroment.user.displayname`              | Format-String | No    | Format for `displayname` of the SSO user | "%(displayName)s" |
| `enviroment.user.email`                    | Format-String | No    | Format für primäre E-Mail des SSO-Nutzers | |
| `enviroment.groups`                           | List         |         | | |
| `enviroment.groups.attr`                     | String        | Yes      | Environment variable or variable set in `mapping` with GroupList | |
| `enviroment.groups.divider`                  | String        | No    | Separator for group list | ";" |
| `ldap`                                     |               |         | LDAP | |
| `ldap.machine_bind`                     |               |         | Configuration for server access to the LDAP server (SSO plug-ins may need these variables) | |
| `ldap.machine_bind.url`                      | String        | No    | LDAP-Server-URL | |
| `ldap.machine_bind.who`                      | String        | No    | login (i.e. only AUTH_SIMPLE supported: User) | |
| `ldap.machine_bind.cred`                     | String        | No    | credential (i.e. only AUTH_SIMPLE supported: Password) | |
