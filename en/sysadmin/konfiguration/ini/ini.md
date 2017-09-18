# INI files

## Structure and loading sequence

The Easydb server is primarily configured by INI files. The INI files are loaded in the following order:

- `/etc/opt/easydb/server/easydb-server.ini`, if available
- `easydb-server.ini` in the current path if it exists
- Other files specified as arguments in the command line (with `--configfile`) in the order in which they were specified

An INI file can also include other configuration files with the `include.files` variable.
The value is a comma-separated list of configuration files, which are loaded at the end, in the order in which they are.
If relative paths are specified, refer to the directory where the configuration file is located.

The order is important because variables are replaced when they occur again.

An example:

```
/etc/opt/easydb/server/easydb-server.ini: existiert nicht

/home/easydb/easydb-server.ini
[janitor]
enabled = true
...

/home/easydb/config/myconfig.ini
[janitor]
enabled = false
[logging]
pf = warn
[include]
files = debug/debug.ini, /home/eas/config.ini
...

/home/easydb/config/debug/debug.ini
[logging]
pf = debug
```

When the Easydb server is started ...

```
$ cd /home/easydb
$ ./easydb-server --configfile config/myconfig.ini
```

... the following files are loaded:

1. /home/easydb/easydb-server.ini
2. /home/easydb/config/myconfig.ini, diese Datei überschriebt die Variable janitor.enabled
3. /home/easydb/config/debug/debug.ini (relativer Pfad), diese Datei überschreibt die Variable logging.debug
4. /home/eas/config.ini

Finally, the variables have the following values:


```
[janitor]
enabled = false
[logging]
pf = debug
```

## Variables

Easydb uses the following variables:

| Section | Variable | Format | Explanation |
|-------------------|---------------------------|-------------------|-----------|
| Include | Files | List of files | Other INI files that are included. As explained above, a configuration file can include additional configuration files |
| Schema | Base\_dir | Directory | Directory for the base schema (\*) |
| Schema | User\_dir | Directory | Directory for the user schema (\*) (1) |
| Frontend | Dsn | DataSourceName | DSN specification for the database (\*), e.g. `Port = 5440 user = postgres dbname = easy5-digitalasset` |
| debug | exporter_sleep | Integer | DEBUG: Delay for export in seconds. |
| debug | exporter_fail | Boolean | DEBUG: If set to "true", the export is set to "failed", if set additionally, after the delay. |
| debug | exporter_warnings | Boolean | DEBUG: If true, the export writes a warning to the log. |
| debug | Search_sleep | Integer | DEBUG: Delay for the search in seconds. |
| Directory  |Pflib | Directory | Directory where the plant is located (\*)
| Directory | Output | Directory | Directory used for export (\*) |
| Directory | Logfile | File | Logfile (\*) |
| Directory | Imexporter | File | Directory where the Easydb server or Imexporter is (\*) |
| Directory | Server\_errors | Directory | Directory for storing error details (if not specified, `{directory.logfile} .errors` is used) |
| Directory | Plans | Directory | Directory for the plans of the Imexporter (if not specified, the current directory is used)
| Directory | Umask | Linux umask | Value for the `umask` variable for the server process (default: 022) |
| Indexer | Entabled | Bool | Whether to start the indexer (default: true) |
| Indexer | Objects \_per \_batch | Int | How many objects are processed in a batch (default: 1000)
| Frontend-server | Num_services | Int | Number of front-end services (\*) |
| Frontend-server | Socket | File | File used as a socket for the processes (\*)
| Upload-server | Num_services | Int | Number of Uploader Services (\*) |
| Upload-server | Socket | File | File used as a socket for the processes (\*) |
| Janitor | Enabled | Bool | Whether the Janitor is started (default: true) |
| Mailer | Interval | Int | Interval between runs, in seconds. For each run, the mailer processes the mailer queue (default: 60) |
| Mailer | Max_attempts | Int | Maximum number of attempts made by the mailer to send a particular e-mail before it is marked as "uninvitable" (default: 3) |
| Mailer | Sender_address | E-mail | Address of the sender for server e-mails (default: "easydb-server@localhost") |
| Mailer | Envelope_address | E-mail | Envelope address for server emails (\*) |
| Exporter | Num_workers | Int | Number of workers (default: 0) (3) |
| System | Allowed_origins | Comma-separated list of addresses Allowed Origins for CORS Requests. If the list is empty or the variable does not exist, CORS is not allowed
| L10n | L10n \_dir | Directory | Directory with the l10 configuration: see[L10n configuration](./sysadmin/configuration/l10n/l10n.md) (\*) |
| Eas | Url | URL | URL of the EAS for access from the Easydb server (\*)
| Eas | External \_url | URL | URL of the EAS for external access (if not set, `eas.url` is taken)
| Eas | Instance | Text | Name of the EAS instance used (\*) |
| Eas | Produce-settings | File | Produce settings for the EAS: see[EAS configuration](./sysadmin/eas/eas.md) (\*) |
| Eas | Rightsmanagement-settings | File | EAS configuration management settings: see[EAS Configuration](./sysadmin/eas/eas.md) (\*) |
| Default pics  |Background | File | Default background image |
| Default pics | User \_avatar | File | Pre - set |
| Default pics | Logo | File | Preset Logo |
| Elasticsearch | Url | URL | Elasticsearch server URL (\*) |
| Elasticsearch | Settings | File | Elasticsearch index settings (\*) |
| Default-client | ? | ? | Client settings: see below |
| Email | `<Template>` | File | E-mail Templates: see[E-mail Configuration](./sysadmin/configuration/email/email.md) |
| Config | Config-settings | File | For runtime configuration settings, see[Runtime Configuration Settings](./sysadmin/configuration/baseconfig/baseconfig.md) (\*)
| Logging | `<Component>` | Level | Logging configuration: see below |
| Solution | Name Text | Text | Name of the solution |
| Solution | Plugins | Comma-separated list of files | List of plugins that should be loaded: see[Plugin configuration](./sysadmin/configuration/plugin/plugin.md) |



Comments:

(\*) Required variables: The server does not start if no value is set for it.

\(1) The user schema is a directory where the Easydb server manages versions of the user schemas.
If you restart the Easydb server, the directory may be empty. The server then creates the
First (empty) schema version.

\(2) The server starts several processes for processing client requests, called "services". The more
"Services", the more client requests can be processed at the same time. A zero means that the service is even
Is not offered.

\(3) The concept of the "worker" is similar to the "service". This is about the processing of exports. The more
"Workers", the more exports can be processed at the same time.

For variables with "file" or "directory" format, you can specify a relative path that refers to the directory where the configuration file is located.

## Client Settings

Everything that appears in the `default-client` section is passed on to the client. That is, here are arbitrary
Variables. The client or client plugin will explain this in their own documentation.

### Webfrontend

| Section | Variable | Format | Explanation  |
| ------------------- | ------- | ----------- | ------------- |
| Default-client | **debug** | Boolean | If set, the client is in debug mode, i. There are e.g. In the context menu Dump Options. Default is 0. |
| Default-client | **tag_icons** | Strings | comma separated Icon names for tag icons that can be placed for tags. Font-Awesome and CUI names are allowed
| Default-client | **asset_browser_max_preview_filesize** | Integer | Up to this size, previews are displayed for the display in the asset browser. If not set to *-1*, the *original* will never be considered. If set to *0*, all sizes and also the original will be considered |
| Default-client | **webdvd_player_open_window_parameter** | String | HTML compliant string for window.open. Settings for opening the new browser window to play a web DVD |
| Default-client | **suggest_disable** | Boolean | If set, suggestions in input fields are disabled |

## Logging configuration

The log system of the Easydb server is hierarchically structured. Each logger takes the log level of the father,
Unless it specifies its own log level. The top level is `pf` and the levels are 'debug', 'info', '
"Warn", "error" and "critical".

The logging configuration is optional. An example would be:

```
[logging]
pf = warn
pf.elasticsearch = debug
pf.elasticsearch.response = error
```

This means that in general, events from level "warn" are logged, but the component "elasticsearch"
Logs everything except the events of the type "response", which are logged only from level "error".