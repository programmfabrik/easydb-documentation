---
title: "easydb-server.yml"
layout: config
menu:
  main:
    name: "easydb-server.yml"
    identifier: "sysadmin/konfiguration/easydb-server.yml"
    parent: "sysadmin/konfiguration"
    weight: 6
easydb-server.yml:
  - base.plugins
  - solution.name
  - solution.plugins
  - server.external_url
  - server.directory.imexporter
  - server.directory.pflib
  - server.directory.output
  - server.directory.logfile
  - server.directory.umask
  - server.directory.server_errors
  - server.directory.l10n_dir
  - server.directory.tmp
  - server.exporter.num_workers
  - server.exporter.batch_size
  - server.exporter.max_xml_size_for_xslt
  - server.janitor.eas_sync_commit
  - server.janitor.enabled
  - server.janitor.interval
  - server.janitor.max_age
  - server.imexporter.socket
  - server.imexporter.num_services
  - server.frontend.socket
  - server.frontend.num_services
  - server.upload-server.socket
  - server.upload-server.num_services
  - server.indexer.enabled
  - server.indexer.num_processes
  - server.indexer.objects_per_batch
  - server.mailer.enabled
  - server.mailer.interval
  - server.mailer.max_attempts
  - server.mailer.sender_address
  - server.mailer.envelope_address
  - server.api.settings.purgeall
  - server.api.settings.purgedata
  - server.api.settings.restart
  - schema.base_dir
  - schema.user_dir
  - schema.dsn
  - eas.url
  - eas.instance
  - eas.thumbnail_size
  - eas.supervisor_enabled
  - eas.vhost
  - eas.external_url  
  - eas.produce_settings
  - eas.rights_management.<class>
  - eas.rights_management.<class>.versions.version
  - eas.rights_management.<class>.versions.size_print
  - eas.rights_management.<class>.versions.size_limit
  - eas.rights_management.<class>.versions.export
  - eas.rights_management.<class>.versions.rightsmanagement
  - eas.rights_management.<class>.versions.group
  - eas.rights_management.<class>.versions.zoomable
  - eas.rights_management.<class>.versions.watermark
  - eas.rights_management.<class>.versions.standard
  - default_pics.background
  - default_pics.user_avatar
  - default_pics.logo
  - plugins.url_prefix_internal
  - plugins.url_prefix_external
  - plugins.url_prefix
  - elasticsearch.url
  - elasticsearch.connect_timeout_ms
  - elasticsearch.transfer_timeout_ms
  - elasticsearch.fielddata_memory
  - elasticsearch.settings
  - elasticsearch.begin_with_wildcards_allowed
  - imexporter-database.dsn
  - imexporter-database.schema
  - imexporter-database.server.directory.plans
  - debug.exporter_sleep
  - debug.exporter_fail
  - debug.exporter_warnings
  - debug.search_sleep
  - suggest.settings
  - suggest.aggregation_chunksize
  - suggest.document_chunksize
  - suggest.timestamps    
rights_management.yml:
  - eas.rights_management.<class>
  - eas.rights_management.<class>.versions.version
  - eas.rights_management.<class>.versions.size_print
  - eas.rights_management.<class>.versions.size_limit
  - eas.rights_management.<class>.versions.export
  - eas.rights_management.<class>.versions.rightsmanagement
  - eas.rights_management.<class>.versions.group
  - eas.rights_management.<class>.versions.zoomable
  - eas.rights_management.<class>.versions.watermark
  - eas.rights_management.<class>.versions.standard
elasticsearch.yml:
  - elasticsearch.connect_timeout_ms
  - elasticsearch.transfer_timeout_ms
  - elasticsearch.fielddata_memory
  - elasticsearch.settings
  - elasticsearch.begin_with_wildcards_allowed
---

# YAML configuration

## Structure and load order

The Easydb server is configured by YAML files. The YAML files are loaded in the following order:

- `easydb5-master.yml` in the folder you defined during [installation](/en/sysadmin/installation).
- Under the hood, i.e. in the docker container, `easydb-server.yml` is first loaded in the current path, if available. This should only be relevant for you as a customer in exceptional cases.
- Generally, other files are loaded that are specified as arguments in the command line (with `--configfile`) in the order in which they are specified.

A YAML file can also include other configuration files:

- The variable **include_before** is a list of files that are loaded before the file in which it is defined
- The variable **include_after** is a list of files that are loaded after the file in which it is defined

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
```yaml
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

### base
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `plugins`                                   | File-List      | No       | List of base plugins | (empty) | #base

### solution
| Variable                                           | Typ           | Pflicht | Erklärung | Default-Wert |
|----------------------------------------------------|---------------|---------|-----------|--------------|
| `name`                                     | String         | Yes      | Name of the Solutio usedn | |
| `plugins`                                  | File-List      | No       | List of Solution Plugins | (empty) |

### server
| Variable                                           | Typ           | Pflicht | Erklärung | Default-Wert |
|----------------------------------------------------|---------------|---------|-----------|--------------|
| `external_url`                             | String         | No       | URL for the Server connection from outside of Easydb | |
| `directory.imexporter`                       | Catalogue      | Yes      | Imexporter Directory | |
| `directory.pflib`                            | Catalogue      | Yes      | Directory where the pflib is located | |
| `directory.output`                           | Catalogue      | Yes      | output directory | |
| `directory.logfile`                          | File           | Yes      | Log-File | `/tmp/easydb-server.log` |
| `directory.umask`                            | Integer        | Yes      | umask | `022` |
| `directory.server_errors`                    | Catalogue      | No       | Catalog for Server Error Information | `<directory/logfile>.errors` |
| `directory.l10n_dir`                         | Catalogue      | Yes      | Catalogues for the L10n configuration | |
| `directory.tmp`                              | Catalogue      | Yes      | Catalogue for temporary files | |
| `exporter.num_workers`                      | Integer        | Yes      | Number of Workers | `0` |
| `exporter.batch_size`                       | Integer        | Yes      | Batch Size | `100` |
| `exporter.max_xml_size_for_xslt`            | Integer        | Yes      | Max. size for XML Files to allow XSLT post processing (in MB) | `10` |
| `janitor.eas_sync_commit`                  | Boolean        | No       | Enable asset status sync to EAS. Assets not linked in easydb are removed by EAS janitor | `true` |
| `janitor.enabled`                          | Boolean        | Yes      | Whether the janitor is running | `true` |
| `janitor.interval`                         | Integer        | Yes      | How often the Janitor runs (every X seconds) | `600` (10 minutes) |
| `janitor.max_age`                          | Integer        | Yes      | When a file expires (after X seconds) | `259200` (3 days) |
| `imexporter.socket`                           | File           | Yes      | Socket | `/tmp/easydb-server-imexporter.sock` |
| `imexporter.num_services`                     | Integer        | Yes      | Number of services | `2` |
| `frontend.socket`                           | File           | Yes      | Socket | `/tmp/easydb-server-frontend.sock` |
| `frontend.num_services`                     | Integer        | Yes      | Number of services | `0` |
| `upload-server.socket`                           | File           | Yes      | Socket | `/tmp/easydb-server-upload.sock` |
| `upload-server.num_services`                     | Integer        | Yes      | Number of services | `2` |
| `indexer.enabled`                          | Boolean        | Yes      | Whether the indexer is running | `true` |
| `indexer.num_processes`                    | Integer        | Yes      | Number of processes | `1` |
| `indexer.objects_per_batch`                | Integer        | Yes      | Number of objects in a batch | `1000` |
| `mailer.enabled`                          | Boolean        | Yes      | Whether the mailer is running | `true` |
| `mailer.interval`                         | Integer        | Yes      | How often the mailer runs (every X seconds) | `60` (1 Minute) |
| `mailer.max_attempts`                     | Integer        | Yes      | Number of attempts before an e-mail is classified as undeliverable | `3` |
| `mailer.sender_address`                   | String         | Yes      | Sender Address | `easydb-server@localhost` |
| `mailer.envelope_address`                 | String         | Yes      | Envelope Address | |
| `api.settings.purgeall`                 | Boolean        | No       | Allow requests on `POST /api/v1/schema/purgeall` | `false` |
| `api.settings.purgedata`                | Boolean        | No       | Allow requests on `POST /api/v1/schema/purgedata` | `false` |
| `api.settings.restart`                  | Boolean        | No       | Allow requests on `POST /api/v1/schema/restart` | `false` |

### schema
| Variable                                           | Typ           | Pflicht | Erklärung | Default-Wert |
|----------------------------------------------------|---------------|---------|-----------|--------------|
| `base_dir`                                 | Catalogue      | Yes      | Base-Schema-Folder | |
| `user_dir`                                 | Catalogue      | Yes      | User-Schema-Folder | |
| `dsn`                                      | String         | Yes      | DSN for the Database connection | |

### eas
| Variable                                           | Typ           | Pflicht | Erklärung | Default-Wert |
|----------------------------------------------------|---------------|---------|-----------|--------------|
| `url`                                      | String         | Yes      | URL for the EAS connection | |
| `instance`                                 | String         | Yes      | Name of the  EAS-Instance | |
| `thumbnail_size`                           | Integer        | Yes      | Thumbnail size| `128` |
| `supervisor_enabled`                       | Boolean        | Yes      | Whether the supervisor is running | `true` |
| `vhost`                                    | String         | No       | V-Host | |
| `external_url`                             | String         | No       | URL for the EAS connection from outside of Easydb. Only set this, if the EAS is running on a different Server. By default, this is the same as `server.external_url`. In Docker Containers, always `server.external_url` is used. | |
| `produce_settings`                         | File           | Yes      | EAS-Produce-Settings (JSON) | |
| `rights_management.<class>`                        |                |          | Configuration for EAS class (image, video, audio, office, directory, unknown) | |
| `rights_management.<class>.versions.version`          | String         | Yes      | Name of the Version | |
| `rights_management.<class>.versions.size_print`       | String         | No       | display text for the Version | |
| `rights_management.<class>.versions.size_limit`       | Integer        | No       | Version size  (determines the maximum size that can be produced if one has the right) | |
| `rights_management.<class>.versions.export`           | Boolean        | Yes      | Whether the version is available for export | |
| `rights_management.<class>.versions.rightsmanagement` | Boolean        | No       | Whether the version is right-managed | `false` |
| `rights_management.<class>.versions.group`            | String         | No       | Display name for the version grouping | |
| `rights_management.<class>.versions.zoomable`         | Boolean        | No       | Whether the version is available for the zoomer | `false` |
| `rights_management.<class>.versions.watermark`        | Boolean        | No       | Whether the version has a watermark | `false` |
| `rights_management.<class>.versions.standard`         | Boolean        | No       | Whether the version is included in standard | `false` |


### default_pics
| Variable                                           | Typ           | Pflicht | Erklärung | Default-Wert |
|----------------------------------------------------|---------------|---------|-----------|--------------|
| `background`                               | File           | No       | for the background | |
| `user_avatar`                              | File           | No       | for user images | |
| `logo`                                     | File           | No       | for the Easydb logo | |

### plugins
| Variable                                           | Typ           | Pflicht | Erklärung | Default-Wert |
|----------------------------------------------------|---------------|---------|-----------|--------------|
| `url_prefix_internal`                      | String         | No       | URL prefix for internal connections | value of `"url_prefix"` |
| `url_prefix_external`                      | String         | No       | URL prefix for external connections | value of `"url_prefix"` |
| `url_prefix`                               | String         | No       | URL prefix for internal or external connections | (no prefix) |

### elasticsearch
| Variable                                           | Typ           | Pflicht | Erklärung | Default-Wert |
|----------------------------------------------------|---------------|---------|-----------|--------------|
| `url`                                      | String         | Yes      | URL | |
| `connect_timeout_ms`                       | Integer        | Yes      | connection timeout (ms) | `30000` (30 seconds) |
| `transfer_timeout_ms`                      | Integer        | Yes      | transmission timeout (ms) | `300000` (5 minutes) |
| `fielddata_memory`                         | String-List    | No       | Index fields that use `"memory"` as Fielddata type | |
| `settings`                                 | File           | Yes      | Index-Settings (JSON) | |
| `begin_with_wildcards_allowed`             | Boolean        | No       | Whether Suggest wildcards are allowed at the beginning | `false` |

### suggest
| Variable                | Type        | Required | Description | Default-Value |
|-------------------------|-------------|----------|-------------|---------------|
| `settings` | File | Yes | Path to the JSON File with the Elasticsearch Settings| |
| `aggregation_chunksize` | Integer | Yes | Number of Buckets for the Aggregations on Tokens and Contexts. Should not be more than `1000` | `1000` |
| `document_chunksize`    | Integer     | Yes      | Batch Size (in MB) of aggregated documents. Should not be more than `1000` (1 GB) | `100` |
| `timestamps`            | String List | No       | Array of Time Stamps when the Suggest Index is rebuilt. Excpected Format: `HH:MM` | `["00:00", "02:00", "04:00","06:00","08:00","10:00","12:00","14:00","16:00","18:00","20:00","22:00"]` |

File-List is a list of maps with "name" (String) and "file" (File).

### Exporter
These variables are only needed for the Imexporter:

#### imexporter-database
| Variable                                           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `dsn`                        | String         | Yes      | DSN for the Database connection | |
| `schema`                     | String         | Yes      | Database Scheme | |
| `server.directory.plans`              | Catalogue      | Yes      | Plans | |

### debug
| Variable                       |
|--------------------------------|
| `exporter_sleep`       |
| `exporter_fail`        |
| `exporter_warnings`    |
| `search_sleep`         |

---