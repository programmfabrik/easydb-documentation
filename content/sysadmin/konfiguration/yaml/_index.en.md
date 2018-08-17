---
title: "49 - YAML-Data"
menu:
  main:
    name: "YAML-Data"
    identifier: "sysadmin/konfiguration/yaml"
    parent: "sysadmin/konfiguration"
---
# YAML configuration

Structure and load order

The Easydb server is configured by YAML files. The YAML files are loaded in the following order:

`easydb5-master.yml` in the folder you defined during [installation](/en/sysadmin/installation).
Under the hood, i.e. in the docker container, `easydb-server.yml` is first loaded in the current path, if available. This should only be relevant for you as a customer in exceptional cases.
Generally, other files are loaded that are specified as arguments in the command line (with `--configfile`) in the order in which they are specified.

A YAML file can also include other configuration files:

The variable **include_before** is a list of files that are loaded before the file in which it is defined
The variable **include_after** is a list of files that are loaded after the file in which it is defined

The files are defined either with an absolute path or relative to the YAML file in which they were specified.

Outside of the docker-container we recommend to include everything in the one YAML-file `easydb5-master.yml`.

## Types

Variables are structured in maps, but a general map is not a valid type for a variable. The types supported are:

| Easydb-Type   | YAML-Type                | Comments |
|---------------|--------------------------|----------|
| String        | String                   | |
| Integer       | Integer                  | |
| Boolean       | Boolean, String, Integer | `true`: `true, "on", "1", 1` |
|               |                          | `false`: `false, "off", "0", 0, null`, not set |
| File          | String                   | either absolute or relative to the YAML file in which the variable is defined |
| Catalogue     | String                   | as file |
| File-List     | Sequence of Strings      | not set = `null` = empty list |
|               |                          | each file is absolute or relative to the YAML file in which it is defined, i.e. a list can contain files with different relative paths |

## replacements

If a variable has already been defined, its value is replaced if it is redefined at a later time. Further opportunities are:

- `variable+`: adds a new value (only valid for lists). Example: Activate two more plugins with the list "enabled":
```YAML
  plugins:
    enabled+:
      - base.custom-data-type-link
      - base.custom-data-type-gnd
```
- `variable-`:
  - if the variable is a list, the specified values are deleted from the list
  - if the variable is a scalar, it becomes undefined
  - if the variable is a map, all variables below it are undefined

- `variable-key`: only for lists of maps, remove all entries from the list whose value for "key" is included in the specified list

## List of variables

**Easydb-Server**

### 0 Level easydb-server.yml config
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| **base**                                           |                |          |             |         |
| **solution**                                       |                |          | Configuration of the Solution | |
| **server**                                         |                |          | server settings | |
| **schema**                                         |                |          | Schema-Settings | |
| **eas**                                            |                |          | EAS-Configuration | |
| **config**                                         |                |          | Basis-Configuration | |
| **default_pics**                                   |                |          | default images | |
| **plugins**                                        |                |          | plug-in configuration | |
| **elasticsearch**                                  |                |          | Elasticsearch Configuration | |
| **email**                                          |                |          | Email Templates | |
| **ldap**                                           | List           |          | List of LDAP configurations | |
| **sso**                                            |                |          | Single Sign-on Configuration | |
| **default_client**                                 |                |          | Client Configuration | |
| **hotfolder**                                      |                |          | | |
| **imexporter-database**              |                |          | Schema-Settings | |
| **debug**                      | |

---
### Base
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `plugins`                                   | File-List      | No       | List of base plugins | (empty) |

---
### Solution
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `name`                                     | String         | Yes      | Name of the Solutio usedn | |
| `plugins`                                  | File-List      | No       | List of Solution Plugins | (empty) |

---
### Server
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `external_url`                             | String         | No       | URL for the Server connection from outside of Easydb | |
| **directory**                              |                |          | Files and directories | |
| **exporter**                              |                |          | Exporter processes | |
| **janitor**                                |                |          | Janitor process | |
| **imexporter**                             |                |          | Imexporter processes | |
| **frontend**                               |                |          | Frontend processes | |
| **upload-server**                          |                |          | upload processes | |
| **indexer**                                |                |          | Indexer Processes | |
| **mailer**                                 |                |          | mailer process | |
| **api**                                    |                |          | API options | |

#### Directory
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `imexporter`                       | Catalogue      | Yes      | Imexporter Directory | |
| `pflib`                            | Catalogue      | Yes      | Directory where the pflib is located | |
| `output`                           | Catalogue      | Yes      | output directory | |
| `logfile`                          | File           | Yes      | Log-File | `/tmp/easydb-server.log` |
| `umask`                            | Integer        | Yes      | umask | `022` |
| `server_errors`                    | Catalogue      | No       | Catalog for Server Error Information | `<directory/logfile>.errors` |
| `l10n_dir`                         | Catalogue      | Yes      | Catalogues for the L10n configuration | |

#### Exporter
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `num_workers`                      | Integer        | Yes      | Number of Workers | `0` |
| `batch_size`                       | Integer        | Yes      | Batch Size | `100` |
| `max_xml_size_for_xslt`            | Integer        | Yes      | Max. size for XML Files to allow XSLT post processing (in MB) | `10` |

#### Janitor
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `eas_sync_commit`                  | Boolean        | No       | Enable asset status sync to EAS. Assets not linked in easydb are removed by EAS janitor | `true` |
| `enabled`                          | Boolean        | Yes      | Whether the janitor is running | `true` |
| `interval`                         | Integer        | Yes      | How often the Janitor runs (every X seconds) | `600` (10 minutes) |
| `max_age`                          | Integer        | Yes      | When a file expires (after X seconds) | `259200` (3 days) |

#### Imexporter
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `socket`                           | File           | Yes      | Socket | `/tmp/easydb-server-imexporter.sock` |
| `num_services`                     | Integer        | Yes      | Number of services | `2` |

#### Frontend
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `socket`                           | File           | Yes      | Socket | `/tmp/easydb-server-frontend.sock` |
| `num_services`                     | Integer        | Yes      | Number of services | `0` |

#### Upload-server
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `socket`                           | File           | Yes      | Socket | `/tmp/easydb-server-upload.sock` |
| `num_services`                     | Integer        | Yes      | Number of services | `2` |

#### Indexer
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `enabled`                          | Boolean        | Yes      | Whether the indexer is running | `true` |
| `num_processes`                    | Integer        | Yes      | Number of processes | `1` |
| `objects_per_batch`                | Integer        | Yes      | Number of objects in a batch | `1000` |

#### Mailer
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `enabled`                          | Boolean        | Yes      | Whether the mailer is running | `true` |
| `interval`                         | Integer        | Yes      | How often the mailer runs (every X seconds) | `60` (1 Minute) |
| `max_attempts`                     | Integer        | Yes      | Number of attempts before an e-mail is classified as undeliverable | `3` |
| `sender_address`                   | String         | Yes      | Sender Address | `easydb-server@localhost` |
| `envelope_address`                 | String         | Yes      | Envelope Address | |

#### API
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| **settings**                       |                |          | options for `/api/v1/settings` | |

##### Settings
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `purgeall`                 | Boolean        | No       | Allow requests on `POST /api/v1/schema/purgeall` | `false` |
| `purgedata`                | Boolean        | No       | Allow requests on `POST /api/v1/schema/purgedata` | `false` |
| `restart`                  | Boolean        | No       | Allow requests on `POST /api/v1/schema/restart` | `false` |

---
### Schema
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `base_dir`                                 | Catalogue      | Yes      | Base-Schema-Folder | |
| `user_dir`                                 | Catalogue      | Yes      | User-Schema-Folder | |
| `dsn`                                      | String         | Yes      | DSN for the Database connection | |

---
### EAS
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `url`                                      | String         | Yes      | URL for the EAS connection | |
| `instance`                                 | String         | Yes      | Name of the  EAS-Instance | |
| `thumbnail_size`                           | Integer        | Yes      | Thumbnail size| `128` |
| `supervisor_enabled`                       | Boolean        | Yes      | Whether the supervisor is running | `true` |
| `vhost`                                    | String         | No       | V-Host | |
| `external_url`                             | String         | No       | URL for the EAS connection from outside of Easydb. Only set this, if the EAS is running on a different Server. By default, this is the same as `server.external_url`. In Docker Containers, always `server.external_url` is used. | |
| `produce_settings`                         | File           | Yes      | EAS-Produce-Settings (JSON) | |
| **rights_management**                      |                | Yes      | EAS rights management configuration | |

#### Rightsmanagement
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `<class>`                        |                |          | Configuration for EAS class (image, video, audio, office, directory, unknown) | |
| **versions**               |                | Yes      | EAS-Version (`"original"` is not allowed) | |

##### Versions
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `version`          | String         | Yes      | Name of the Version | |
| `size_print`       | String         | No       | display text for the Version | |
| `size_limit`       | Integer        | No       | Version size  (determines the maximum size that can be produced if one has the right) | |
| `export`           | Boolean        | Yes      | Whether the version is available for export | |
| `rightsmanagement` | Boolean        | No       | Whether the version is right-managed | `false` |
| `group`            | String         | No       | Display name for the version grouping | |
| `zoomable`         | Boolean        | No       | Whether the version is available for the zoomer | `false` |
| `watermark`        | Boolean        | No       | Whether the version has a watermark | `false` |
| `standard`         | Boolean        | No       | Whether the version is included in standard | `false` |

---
### Config
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `config_settings`                          | File           | Yes      | Basis-Configuration | |

---
### Default pics
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `background`                               | File           | No       | for the background | |
| `user_avatar`                              | File           | No       | for user images | |
| `logo`                                     | File           | No       | for the Easydb logo | |

---
### Plugins
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `url_prefix_internal`                      | String         | No       | URL prefix for internal connections | value of `"url_prefix"` |
| `url_prefix_external`                      | String         | No       | URL prefix for external connections | value of `"url_prefix"` |
| `url_prefix`                               | String         | No       | URL prefix for internal or external connections | (no prefix) |

---
### Elasticsearch
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `url`                                      | String         | Yes      | URL | |
| `connect_timeout_ms`                       | Integer        | Yes      | connection timeout (ms) | `30000` (30 seconds) |
| `transfer_timeout_ms`                      | Integer        | Yes      | transmission timeout (ms) | `300000` (5 minutes) |
| `fielddata_memory`                         | String-List    | No       | Index fields that use `"memory"` as Fielddata type | |
| `settings`                                 | File           | Yes      | Index-Settings (JSON) | |
| `begin_with_wildcards_allowed`             | Boolean        | No       | Whether Suggest wildcards are allowed at the beginning | `false` |

---
### Email
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `welcome_new_user`                         | File           | Yes      | | |
| `forgot_password`                          | File           | Yes      | | |
| `require_password_change`                  | File           | Yes      | | |
| `confirm_email`                            | File           | Yes      | | |
| `updated_self_service`                     | File           | Yes      | | |
| `updated_record`                           | File           | Yes      | | |
| `login_disabled`                           | File           | Yes      | | |
| `share_collection`                         | File           | Yes      | | |
| `transition_resolve`                       | File           | Yes      | | |
| `transition_reject`                        | File           | Yes      | | |
| `transport`                                | File           | Yes      | | |
| `export`                                   | File           | Yes      | | |

#### LDAP-User
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| **user**                                   |                |          | user authentication | |
| **group**                                  | List           |          | List with group configurations | |
| **environment**                            |                |          | Mapping of the extracted LDAP information. Designation and structure compatible to `sso.environment`. | |

##### LDAP-User-settings
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `protocol`                         | String (`"ldap"` or `"ldaps"`) | No       | LDAP protocol | `"ldap"` |
| `server`                           | String         | Yes      | LDAP-Server | |
| `port`                             | Integer        | No       | LDAP-Port | |
| `basedn`                           | String         | Yes      | Base-DN | |
| `scope`                            | String (`"sub"`, `"one"` or `"base"`) | No | Search-Scope | `"sub"` |
| `filter`                           | String         | Yes      | LDAP search filter for users. Replaced are: `% (login)s`, `% (login)s` and `% (LOGIN)s` with the login name. This is converted to lowercase letters, so it is retained or converted to uppercase letters. | |
| `user`                             | String         | No       | LDAP user (DN) that is used if an anonymous search (without logging on) in the LDAP is not possible. | |
| `password`                         | String         | No       | Password for the user previously specified with `user`. | |

#### Group
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `protocol`                         | String (`"ldap"` or `"ldaps"`) | No       | LDAP protocol | `"ldap"` |
| `server`                           | String         | Yes      | LDAP-Server | |
| `port`                             | Integer        | No       | LDAP-Port | |
| `basedn`                           | String         | Yes      | Base-DN | |
| `scope`                            | String (`"sub"`, `"one"` or `"base"`) | No | Search-Scope | `"sub"` |
| `filter`                           | String         | Yes      | LDAP search filter for groups. All attributes from the user entry are replaced, each with the prefix `"user."`, e.g. `% (user.uid)s`. | |
| `user`                             | String         | No       | LDAP user (DN) that is used if an anonymous search (without logging on) in the LDAP is not possible. | |
| `password`                         | String         | No       | Password for the user previously specified with `user`. | |

#### Enviroment
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `mapping`                          |                |          | With `mapping` variables can be extracted from the environment and rewritten | |

##### Mapping
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `<var>`                  |                |          | definable variable name, which may only consist of letters and underscores | |

###### var
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `attr`             | String         | Yes      | LDAP variable with value of the variable to be set. It can be applied to variables from the user entry (with prefix `"user."`, e.g. `% (user.givenName)s`) and from the group entry (with prefix `"group."`, e.g. `% (group.cn)s`). | |
| `regex_match`      | String         | No       | Regular expression for finding parts of the attribute value. An example would be `"@.$"`to find all characters from the `"@"` to the end (so-called "scope"). | |
| `regex_replace`    | String         | No       | Value to replace the part found by `regex_match`. The "Scope" from the example above could be replaced by an empty string (`""`) or also by a fixed value (`": ldap"`) | |

##### User
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `user`                             |                |          | defines the properties of the user. Format strings can be used to define the final values for the properties from LDAP variables and variables defined via `mapping`. In addition to variable values, you can also use fixed texts. An example for the value of `displayname` would be `"LDAP user % (user.givenName)s % (user.sn)"`: the first name (`user.givenName`) and last name (`user.sn`) are preceded by the fixed text "LDAP user". | |

###### User-settings
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `login`                    | Format-String  | No       | Format for LDAP user's `login`. | `"%(user.dn)s"` |
| `displayname`              | Format-String  | No       | Format for LDAP user's `displayname`. | `"%(user.dn)s"` |
| `email`                    | Format-String  | No       | Format for primary e-mail of LDAP user | |
| `groups`                           | List           |          | | |
| `attr`                     | String         | Yes      | LDAP attribute or variable set in `mapping` with GroupList | |
| `divider`                  | String         | No       | Separator for group list | |

---
### SSO
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `auth_method` --> `client`             |                |          | Configuration of the frontend login dialog, See [SSO](/en/sysadmin/konfiguration/sso) | |
| `environment`                              |                |          | Shibboleth/Kerberos/LDAP/AD. See [SSO](/en/sysadmin/konfiguration/sso)| |
| `ldap`                                     |                |          | LDAP/Active Directory. See [SSO](/en/sysadmin/konfiguration/sso) | |

---
### Default client
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `debug`                                    | Boolean        |          | If set, the client is in debug mode, i.e. there are dump options in the context menu. | `false` |
| `tag_icons`                                | String         |          | Comma-separated trick. Icon names for tag icons that can be stored for tags. Font-Awesome and CUI designations are allowed | `bolt, check, cloud, warning, legal` |
| `tag_colors`                               | String         |          | Comma-separated list. Color clases for the tags. | `green, red, blue, yellow` |
| `asset_browser_max_preview_filesize`       | Integer        |          | Up to this size, preview images for the display in the asset browser are considered. If not set to *`-1`*, the *Original* is never taken into account. If set to *`0`*, all sizes and the original are taken into account | |
| `video_player_use_original`                | Boolean        |          | If set, the video player also uses the original as source for the HTML5 video tag. | |
| `audio_player_use_original`                | Boolean        |          | If set, the audio player also uses the original as source for the HTML5 audio tag. | |
| `webdvd_player_open_window_parameter`      | String         |          | HTML compliant string for `window.open`. Settings for opening the new browser window to play a web DVD | |
| `print_limit`                              | Number         | No       | Limit the maximum number of objects that can be printed. | `250` |
| `collection_refresh_rate_seconds`          | Number         | No       | Number of seconds waited until the fixed searches in the Finder are updated. | `30` |
| `suggest_disable`                          | Boolean        |          | If set, suggestions in input fields are disabled | |
| `database`                                 | Map            |          | | |
| `level`                            | String         | No       | Overwrites the highest permitted database rights level. Allowed values are: `"development", "commit", "current"`. | |

#### Level
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `watermark_configured`                     | Boolean        |          | If it's set to `true`, it will be possible to configure a watermark.  | `false` |

---
### Hotfolder
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `enabled`                                  | boolean        | No       |  `true` if hotfolder is to be used | `true` |
| `directory`                                | file           | No       |  The working directory of the hot folder | |
| `number_of_workers`                        | integer        | No       |  Number of worker threads used for uploading the objects | `5` |
| `upload_batch_size`                        | integer        | No       |  Number of objects that are uploaded from a hotfolder in one batch at most | `10` |
| `upload_batches`                           | boolean        | No       | `true` if objects are uploaded in batches (Batch size: `upload_batch_size`) | `true` |
| `delay`                                    | integer        | No       |  Time in seconds that the process waits after a run | `10` |

File-List is a list of maps with `"name"` (String) and `"file"` (File).

---
### Exporter
These variables are only needed for the Imexporter:

#### Imexporter-database
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `dsn`                        | String         | Yes      | DSN for the Database connection | |
| `schema`                     | String         | Yes      | Database Scheme | |
| **server**                           |                |          | | |

#### Server
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| **directory**                |                |          | | |

##### Directory
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `plans`              | Catalogue      | Yes      | Plans | |

---
### Debug
| Variable                       |
|--------------------------------|
| `exporter_sleep`       |
| `exporter_fail`        |
| `exporter_warnings`    |
| `search_sleep`         |
