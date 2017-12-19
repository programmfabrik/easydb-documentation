# YAML configuration

Structure and load order

The Easydb server is configured by YAML files. The YAML files are loaded in the following order:

`easydb5-master. yml` in the path you defined during [Installation](/sysadmin/installation/installation.html).
Under the hood, i. e. in the docker container, `easydb-server. yml` is first loaded in the current path, if available. This should only be relevant for you as a customer in exceptional cases.
Generally, other files are loaded that are specified as arguments in the command line (with `--configfile') in the order in which they are specified.

A YAML file can also include other configuration files:

The variable **include_before** is a list of files that are loaded before the file in which it is defined
The variable **include_after** is a list of files that are loaded after the file in which it is defined

The files are defined either with an absolute path or relative to the YAML file in which they were specified.

Outside of the docker-container we recommend to include everything in the one YAML-file `easydb5-master. yml`.

## Types

Variables are structured in maps, but a general map is not a valid type for a variable. The types supported are:

| Easydb-Type    | YAML-Type                 | Comments |
|---------------|--------------------------|-----------|
| String        | String                   | |
| Integer       | Integer                  | |
| Boolean       | Boolean, String, Integer | true: true, "on", "1", 1 |
|               |                          | false: false, "off", "0", 0, null, nicht gesetzt |
| File         | String                   | either absolute or relative to the YAML file in which the variable is defined |
| Catalogue  | String                   | as file |
| File-List | Sequence of Strings      | not set = null = empty list |
|               |                          | each file is absolute or relative to the YAML file in which it is defined, i. e. a list can contain files with different relative paths |

## replacements

If a variable has already been defined, its value is replaced if it is redefined at a later time. Further opportunities are:

- variable+: adds a new value (only valid for lists). Example: Activate two more plugins with the list "enabled":
```YAML
  plugins:
    enabled+:
      - base. custom-data-type-link
      - base. custom-data-type-gnd
```
- variable-:
  - if the variable is a list, the specified values are deleted from the list
  - if the variable is a scalar, it becomes undefined
  - if the variable is a map, all variables below it are undefined

- variable-key: only for lists of maps, remove all entries from the list whose value for "key" is included in the specified list

## List of variables

**Easydb-Server**

| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| **base**                                           |                |          |             |         |
| &#8614; `plugins`                                  | File-List      | No       | List of base plugins | (leer) |
| **solution**                                       |               |         | Configuration of the Solution | |
| &#8614; `name`                                     | String        | Yes      | Name of the Solutio usedn | |
| &#8614; `plugins`                                  | File-List | No    | List of Solution Plugins | (empty) |
| **server**                                         |               |         | server settings | |
| &#8614; **directory**                              |               |         | Files and directories | |
| &#8614; &#8614; `imexporter`                       | Catalogue  | Yes      | Imexporter Directory | |
| &#8614; &#8614; `pflib`                            | Catalogue  | Yes      | Directory where the pflib is located | |
| &#8614; &#8614; `output`                           | Catalogue  | Yes      | output directory | |
| &#8614; &#8614; `logfile`                          | File         | Yes      | Log-File | /tmp/easydb-server.log |
| &#8614; &#8614; `umask`                            | Integer       | Yes      | umask | 022 |
| &#8614; &#8614; `server_errors`                    | Catalogue  | No    | Catalog for Server Error Information | <directory/logfile>.errors |
| &#8614; &#8614; `l10n_dir`                         | Catalogue  | Yes      | Catalogues for the L10n configuration | |
| &#8614;  **exporter**                              |               |         | Exporter processes | |
| &#8614; &#8614; `num_workers`                      | Integer       | Yes      | Number of Workers | 0 |
| &#8614; &#8614; `batch_size`                       | Integer       | Yes      | Batch Size | 100 |
| &#8614; &#8614; `max_xml_size_for_xslt`            | Integer       | Yes      | Max. size for XML Files to allow XSLT post processing (in MB). Only used if unlimited batch size is used for the export | 1 |
| &#8614; **janitor**                                |               |         | Janitor process | |
| &#8614; &#8614; `enabled`                          | Boolean       | Yes      | Whether the janitor is running | true |
| &#8614; &#8614; `interval`                         | Integer       | Yes      | How often the Janitor runs (every X seconds) | 600 (10 minutes) |
| &#8614; &#8614; `max_age`                          | Integer       | Yes      | When a file expires (after X seconds) | 259200 (3 days) |
| &#8614; **imexporter**                             |               |         | Imexporter processes | |
| &#8614; &#8614; `socket`                           | File         | Yes      | Socket | /tmp/easydb-server-imexporter.sock |
| &#8614; &#8614; `num_services`                     | Integer       | Yes      | Number of services | 2 |
| &#8614; **frontend**                               |               |         | Frontend processes | |
| &#8614; &#8614; `socket`                           | File         | Yes      | Socket | /tmp/easydb-server-frontend.sock |
| &#8614; &#8614; `num_services`                     | Integer       | Yes      | Number of services | 0 |
| &#8614; **upload-server**                          |               |         | upload processes | |
| &#8614; &#8614; `socket`                           | File         | Yes      | Socket | /tmp/easydb-server-upload.sock |
| &#8614; &#8614; `num_services`                     | Integer       | Yes      | Number of services | 2 |
| &#8614; **indexer**                                |               |         | Indexer Processes | |
| &#8614; &#8614; `enabled`                          | Boolean       | Yes      | Whether the indexer is running | true |
| &#8614; &#8614; `num_processes`                    | Integer       | Yes      | Number of processes | 1 |
| &#8614; &#8614; `objects_pre_batch`                | Integer       | Yes      | Number of objects in a batch | 1000 |
| &#8614; **mailer**                                 |               |         | mailer process | |
| &#8614; &#8614; `enabled`                          | Boolean       | Yes      | Whether the mailer is running | true |
| &#8614; &#8614; `interval`                         | Integer       | Yes      | How often the mailer runs (every X seconds) | 60 (1 Minute) |
| &#8614; &#8614; `max_attempts`                     | Integer       | Yes      | Number of attempts before an e-mail is classified as undeliverable | 3 |
| &#8614; &#8614; `sender_address`                   | String        | Yes      | Sender Address | easydb-server@localhost |
| &#8614; &#8614; `envelope_address`                 | String        | Yes      | Envelope Address | |
| **schema**                                         |               |         | Schema-Settings | |
| &#8614; `base_dir`                                 | Catalogue  | Yes      | Base-Schema-Folder | |
| &#8614; `user_dir`                                 | Catalogue  | Yes      | User-Schema-Folder | |
| &#8614; `dsn`                                      | String        | Yes      | DSN for the Database connection | |
| **eas**                                            |               |         | EAS-Configuration | |
| &#8614; `url`                                      | String        | Yes      | URL for the EAS-Anbindung | |
| &#8614; `instance`                                 | String        | Yes      | Name of the  EAS-Instance | |
| &#8614; `thumbnail_size`                           | Integer       | Yes      | Thumbnail size| 128 |
| &#8614; `supervisor_enabled`                       | Boolean       | Yes      | Whether the supervisor is running | true |
| &#8614; `vhost`                                    | String        | No    | V-Host | |
| &#8614; `external_url`                             | String        | No    | URL for the EAS connection from outside of Easydb | |
| &#8614; `produce_settings`                         | File         | Yes      | EAS-Produce-Settings (JSON) | |
| &#8614; **rights_management**                      |               | Yes      | EAS rights management configuration | |
| &#8614; &#8614; `\<class\>`                        |               |         | Configuration for EAS class (image, video, audio, office, directory, unknown) | |
| &#8614; &#8614; &#8614; **versions**               |               | Yes      | EAS-Version ("original" ist nicht erlaubt) | |
| &#8614; &#8614; &#8614; &#8614; `version`          | String        | Yes      | Name of the Version | |
| &#8614; &#8614; &#8614; &#8614; `size_print`       | String        | No    | display text for the Version | |
| &#8614; &#8614; &#8614; &#8614; `size_limit`       | Integer       | No    | Version size  (determines the maximum size that can be produced if one has the right) | |
| &#8614; &#8614; &#8614; &#8614; `export`           | Boolean       | Yes      | Whether the version is available for export | |
| &#8614; &#8614; &#8614; &#8614; `rightsmanagement` | Boolean       | No      | Whether the version is right-managed | false |
| &#8614; &#8614; &#8614; &#8614; `group`            | String        | No    | Display name for the version grouping | |
| &#8614; &#8614; &#8614; &#8614; `zoomable`         | Boolean       | No    | Whether the version is available for the zoomer | false |
| &#8614; &#8614; &#8614; &#8614; `watermark`        | Boolean       | No    | Whether the version has a watermark | false |
| &#8614; &#8614; &#8614; &#8614; `standard`         | Boolean       | No    | Whether the version is included in" standard | false |
| **config**                                         |               |         | Basis-Configuration | |
| &#8614; `config_settings`                          | File         | Yes      | Basis-Configuration | |
| **default_pics**                                   |               |         | default images | |
| &#8614; `background`                               | File         | No    | for the background | |
| &#8614; `user_avatar`                              | File         | No    | for user images | |
| &#8614; `logo`                                     | File         | No    | for the Easydb logo | |
| **plugins**                                        |               |         | plug-in configuration | |
| &#8614; `url_prefix_internal`                      | String        | No    | URL prefix for internal connections | value of "url_prefix" |
| &#8614; `url_prefix_external`                      | String        | No    | URL prefix for external connections | value of "url_prefix" |
| &#8614; `url_prefix`                               | String        | No    | URL prefix for internal or external connections | (no prefix) |
| **elasticsearch**                                  |               |         | Elasticsearch Configuration | |
| &#8614; `url`                                      | String        | Yes      | URL | |
| &#8614; `connect_timeout_ms`                       | Integer       | Yes      | connection timeout (ms) | 30000 (30 Sekunden) |
| &#8614; `transfer_timeout_ms`                      | Integer       | Yes      | transmission timeout (ms) | 300000 (5 Minuten) |
| &#8614; `fielddata_memory`                         | String-List  | No    | Index fields that use "memory" as Fielddata type | |
| &#8614; `settings`                                 | File         | Yes      | Index-Settings (JSON) | |
| &#8614; `begin_with_wildcards_allowed`             | Boolean       | No    | Whether Suggest wildcards are allowed at the beginning | false |
| **email**                                          |               |         | Email Templates | |
| &#8614; `welcome_new_user`                         | File         | Yes      | | |
| &#8614; `forgot_password`                          | File         | Yes      | | |
| &#8614; `require_password_change`                  | File         | Yes      | | |
| &#8614; `confirm_email`                            | File         | Yes      | | |
| &#8614; `updated_self_service`                     | File         | Yes      | | |
| &#8614; `updated_record`                           | File         | Yes      | | |
| &#8614; `login_disabled`                           | File         | Yes      | | |
| &#8614; `share_collection`                         | File         | Yes      | | |
| &#8614; `transition_resolve`                       | File         | Yes      | | |
| &#8614; `transition_reject`                        | File         | Yes      | | |
| &#8614; `transport`                                | File         | Yes      | | |
| &#8614; `export`                                   | File         | Yes      | | |
| **ldap**                                           | List         |         | List of LDAP configurations | |
| &#8614; **user**                                   |               |         | user authentication | |
| &#8614; &#8614; `protocol`                         | String ("ldap" or "ldaps") | No    | LDAP protocol | ldap |
| &#8614; &#8614; `server`                           | String        | Yes      | LDAP-Server | |
| &#8614; &#8614; `port`                             | Integer       | No    | LDAP-Port | |
| &#8614; &#8614; `basedn`                           | String        | Yes      | Base-DN | |
| &#8614; &#8614; `scope`                            | String ("sub", "one" or "base") | No | Search-Scope | sub |
| &#8614; &#8614; `filter`                           | String        | Yes      | LDAP search filter for users. Replaced are: `% (login)s`, `% (login)s` and `% (LOGIN)s` with the login name. This is converted to lowercase letters, so it is retained or converted to uppercase letters. | |
| &#8614; &#8614; `user`                             | String        | No    | LDAP user (DN) that is used if an anonymous search (without logging on) in the LDAP is not possible. | |
| &#8614; &#8614; `password`                         | String        | No    | Password for the user previously specified with `user`. | |
| &#8614; **group**                                  | List         |         | List with group configurations | |
| &#8614; &#8614; `protocol`                         | String ("ldap" or "ldaps") | No    | LDAP-Protokoll | ldap |
| &#8614; &#8614; `server`                           | String        | Yes      | LDAP-Server | |
| &#8614; &#8614; `port`                             | Integer       | No    | LDAP-Port | |
| &#8614; &#8614; `basedn`                           | String        | Yes      | Base-DN | |
| &#8614; &#8614; `scope`                            | String ("sub", "one" or "base") | No | Search-Scope | sub |
| &#8614; &#8614; `filter`                           | String        | Yes      | LDAP search filter for groups. All attributes from the user entry are replaced, each with the prefix "user.", e. g. `% (user. uid)s`. | |
| &#8614; &#8614; `user`                             | String        | No    | LDAP user (DN) that is used if an anonymous search (without logging on) in the LDAP is not possible. | |
| &#8614; &#8614; `password`                         | String        | No    | Password for the user previously specified with `user`. | |
| &#8614; **environment**                            |               |         | Mapping of the extracted LDAP information. Designation and structure compatible to `sso. environment`. | |
| &#8614; &#8614; `mapping`                          |               |         | with `mapping` variables can be extracted from the environment and rewritten | |
| &#8614; &#8614; &#8614; `\<var\>`                  |               |         | definable variable name, which may only consist of letters and underscores | |
| &#8614; &#8614; &#8614; &#8614; `attr`             | String        | Yes      | LDAP variable with value of the variable to be set. It can be applied to variables from the user entry (with prefix "user.", e. g. `% (user. givenName)s`) and from the group entry (with prefix "group.", e. g. `% (group. cn)s`). | |
| &#8614; &#8614; &#8614; &#8614; `regex_match`       | String        | No    | Regular expression for finding parts of the attribute value. An example would be `"@.$"`to find all characters from the "@" to the end (so-called "scope"). | |
| &#8614; &#8614; &#8614; &#8614; `regex_replace`     | String        | No    | Value to replace the part found by `regex_match`. The "Scope" from the example above could be replaced by an empty string (`""`) or also by a fixed value (`": ldap"`) | |
| &#8614; &#8614; `user`                             |               |         | defines the properties of the user. Format strings can be used to define the final values for the properties from LDAP variables and variables defined via `mapping`. In addition to variable values, you can also use fixed texts. An example for the value of `displayname` would be `"LDAP user % (user. givenName)s % (user. sn)"`: the first name (`user. givenName`) and last name (`user. sn`) are preceded by the fixed text "LDAP user". | |
| &#8614; &#8614; &#8614; `login`                    | Format-String | No    | Format for LDAP user's `login`. | "%(user.dn)s" |
| &#8614; &#8614; &#8614; `displayname`              | Format-String | No    | Format for LDAP user's `displayname`. | "%(user.dn)s" |
| &#8614; &#8614; &#8614; `email`                    | Format-String | No    | Format for primary e-mail of LDAP user | |
| &#8614; &#8614; `groups`                           | List         |         | | |
| &#8614; &#8614; &#8614; `attr`                     | String        | Yes      | LDAP attribute or variable set in `mapping` with GroupList | |
| &#8614; &#8614; &#8614; `divider`                  | String        | No    | Separator for group list | |
| **sso**                                            |               |         | Single Sign-on Configuration | |
| &#8614; `auth_method`                              |               |         | | |
| &#8614; &#8614; `client`                           |               |         | | |
| &#8614; &#8614; &#8614; `login`                    | Boolean       | No    | If set to `true`, single sign-on authentication is enabled in the frontend. | |
| &#8614; `environment`                              |               |         | Most SSO systems (such as Shibboleth) allow access to authenticated user properties using environment variables. With the following options, these variables can be used through the `sso` plugin.| |
| &#8614; &#8614; `mapping`                          |               |         | with `mapping` variables can be extracted from the environment and rewritten | |
| &#8614; &#8614; &#8614; `\<var\>`                  |               |         | definable variable name, which may only consist of letters and underscores | |
| &#8614; &#8614; &#8614; &#8614; `attr`             | String        | Yes      | Environment variable with value of the variable to be set | |
| &#8614; &#8614; &#8614; &#8614; `regex_match`      | String        | No    | Regular expression for finding parts of the attribute value. An example would be `"@.$"`to find all characters from the "@" to the end (so-called "scope"). | |
| &#8614; &#8614; &#8614; &#8614; `regex_replace`    | String        | No    | Value to replace the part found by `regex_match`. The "Scope" from the example above could be replaced by an empty string (`""`) or also by a fixed value (`": shibboleth"`) | |
| &#8614; &#8614; `user`                             |               |         | defines the properties of the user. Format strings can be used to define the final values for the properties from environment variables and variables defined via `mapping`. In addition to variable values, you can also use fixed texts. An example of the value of `displayname` would be `"SSO user % (givenName)s % (sn)"`: the first name (`givenName`) and last name (`sn`) are preceded by the fixed text "SSO user". | |
| &#8614; &#8614; &#8614; `login`                    | Format-String | No    | Format for `login` of the SSO user | "%(eppn)s" |
| &#8614; &#8614; &#8614; `displayname`              | Format-String | No    | Format for `displayname` of the SSO user | "%(displayName)s" |
| &#8614; &#8614; &#8614; `email`                    | Format-String | No    | Format für primäre E-Mail des SSO-Nutzers | |
| &#8614; &#8614; `groups`                           | List         |         | | |
| &#8614; &#8614; &#8614; `attr`                     | String        | Yes      | Environment variable or variable set in `mapping` with GroupList | |
| &#8614; &#8614; &#8614; `divider`                  | String        | No    | Separator for group list | ";" |
| &#8614; `ldap`                                     |               |         | LDAP | |
| &#8614; &#8614; `machine_bind`                     |               |         | Configuration for server access to the LDAP server (SSO plug-ins may need these variables) | |
| &#8614; &#8614; &#8614; `url`                      | String        | No    | LDAP-Server-URL | |
| &#8614; &#8614; &#8614; `who`                      | String        | No    | login (i.e. only AUTH_SIMPLE supported: User) | |
| &#8614; &#8614; &#8614; `cred`                     | String        | No    | credential (i.e. only AUTH_SIMPLE supported: Password) | |
| **default_client**                                 |               |         | Client Configuration | |
| &#8614; `debug`                                    | Boolean       |         | If set, the client is in debug mode, i. e. there are dump options in the context menu. | false |
| &#8614; `tag_icons`                                | String        |         | Comma-separated trick. Icon names for tag icons that can be stored for tags. Font-Awesome and CUI designations are allowed | bolt, check, cloud, warning, legal |
| &#8614; `tag_colors`                               | String        |         | Comma-separated list. Color clases for the tags. | green, red, blue, yellow |
| &#8614; `asset_browser_max_preview_filesize`       | Integer       |         | Up to this size, preview images for the display in the asset browser are considered. If not set to *-1*, the *Original* is never taken into account. If set to *0*, all sizes and the original are taken into account | |
| &#8614; `video_player_use_original`                | Boolean       |         | If set, the video player also uses the original as source for the HTML5 video tag. | |
| &#8614; `audio_player_use_original`                | Boolean       |         | If set, the audio player also uses the original as source for the HTML5 audio tag. | |
| &#8614; `webdvd_player_open_window_parameter`      | String        |         | HTML compliant string for window. open. Settings for opening the new browser window to play a web DVD | |
| &#8614; `print_limit`                              | Number        | No         | Limit the maximum number of objects that can be printed. | 250 |
| &#8614; `collection_refresh_rate_seconds`          | Number        | No         | Number of seconds waited until the fixed searches in the Finder are updated. | 30 |
| &#8614; `suggest_disable`                          | Boolean       |         | If set, suggestions in input fields are disabled | |
| &#8614; `database`                                 | Map           |         | | |
| &#8614; &#8614; `level`                            | String        | No    | Overwrites the highest permitted database rights level. Allowed values are: "development","commit","current". | |
| &#8614; `watermark_configured`                     | Boolean       |       | If it's set to true, it will be possible to configure a watermark.  | false |
| **hotfolder**                                      |               |         |
| &#8614; `enabled`                                  | boolean |  No |  True if hotfolder is to be used |
| &#8614; `directory`                                | file |  No |  The working directory of the hot folder |
| &#8614; `number_of_workers`                        | integer |  No |  Number of worker threads used for uploading the objects |
| &#8614; `upload_batch_size`                        | integer |  No |  Number of objects that are uploaded from a hotfolder in one piece at most |
| &#8614; `delay`                                    | integer |  No |  Time in seconds that the process waits after a run |

File-List is a list of maps with "name" (String) and "file" (File).

**Exporter**

These variables are only needed for the Imexporter:

| Variable                             | Type           | Required | Description | Default |
|--------------------------------------|---------------|---------|-----------|--------------|
| **imexporter-database**              |               |         | Schema-Settings | |
| &#8614; `dsn`                          | String        | Yes      | DSN for the Database connection | |
| &#8614; `schema`                       | String        | Yes      | Database Scheme | |
| **server**                           |               |         | | |
| &#8614; **directory**                |               |         | | |
| &#8614; &#8614; `plans`                | Catalogue  | Yes      | Plans | |

**Debug Relevant**

| Variable                       | |
|--------------------------------|-|
| **debug**                      | |
| &#8614; `exporter_sleep`       | |
| &#8614; `exporter_fail`        | |
| &#8614; `exporter_warnings`    | |
| &#8614; `search_sleep`         | |
