---
title: "easydb-server.yml"
layout: config
menu:
  main:
    name: "easydb-server.yml"
    identifier: "sysadmin/konfiguration/easydb-server.yml"
    parent: "sysadmin/konfiguration"
    weight: 20
easydb-server.yml:
  - base.plugins
  - debug.exporter_fail
  - debug.exporter_sleep
  - debug.exporter_warnings
  - debug.search_sleep
  - default_pics.background
  - default_pics.logo
  - default_pics.user_avatar
  - eas.external_url
  - eas.instance
  - eas.produce_settings
  - eas.rights_management.<class>
  - eas.rights_management.<class>.versions.export
  - eas.rights_management.<class>.versions.group
  - eas.rights_management.<class>.versions.rightsmanagement
  - eas.rights_management.<class>.versions.size_limit
  - eas.rights_management.<class>.versions.size_print
  - eas.rights_management.<class>.versions.standard
  - eas.rights_management.<class>.versions.version
  - eas.rights_management.<class>.versions.watermark
  - eas.rights_management.<class>.versions.zoomable
  - eas.supervisor_enabled
  - eas.thumbnail_size
  - eas.url
  - eas.vhost
  - elasticsearch.begin_with_wildcards_allowed
  - elasticsearch.connect_timeout_ms
  - elasticsearch.default_template
  - elasticsearch.fielddata_memory
  - elasticsearch.max_limit
  - elasticsearch.settings
  - elasticsearch.transfer_timeout_ms
  - elasticsearch.url
  - imexporter-database.dsn
  - imexporter-database.schema
  - imexporter-database.server.directory.plans
  - nodejs.node_modules
  - nodejs.node_runner_app
  - nodejs.node_runner_binary
  - plugins.url_prefix
  - plugins.url_prefix_external
  - plugins.url_prefix_internal
  - schema.base_dir
  - schema.dsn
  - schema.user_dir
  - server.api.settings.buildsuggest
  - server.api.settings.purgeall
  - server.api.settings.purgedata
  - server.api.settings.reindex
  - server.api.settings.restart
  - server.api.settings.updatecustomdata
  - server.custom_datatype_updater.enabled
  - server.directory.imexporter
  - server.directory.l10n_dir
  - server.directory.logfile
  - server.directory.output
  - server.directory.pflib
  - server.directory.server_errors
  - server.directory.tmp
  - server.directory.umask
  - server.dirty_queuer.num_processes
  - server.exporter.batch_size
  - server.exporter.max_xml_size_for_xslt
  - server.exporter.num_workers
  - server.external_url
  - server.frontend.num_services
  - server.frontend.socket
  - server.imexporter.num_services
  - server.imexporter.socket
  - server.indexer.num_processes
  - server.indexer.objects_per_batch
  - server.janitor.eas_sync_commit
  - server.janitor.enabled
  - server.janitor.interval
  - server.janitor.max_age
  - server.mailer.enabled
  - server.mailer.envelope_address
  - server.mailer.interval
  - server.mailer.max_attempts
  - server.mailer.sender_address
  - server.preindexer.num_processes
  - server.upload-server.num_services
  - server.upload-server.socket
  - solution.name
  - solution.plugins
  - suggest.aggregation_chunksize
  - suggest.document_chunksize
  - suggest.settings
  - suggest.timestamps
---

# easydb-server.yml

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

### base

| Variable      | Type           | Required | Description | Default |
|---------------|----------------|----------|-------------|---------|
|`base` | | | |
|&#8193;`plugins`                                   | File-List      | No       | List of base plugins | (empty) |
|`debug` | | | |
|&#8193;`exporter_fail`        |
|&#8193;`exporter_sleep`       |
|&#8193;`exporter_warnings`    |
|&#8193;`search_sleep`         |
|`default_client`              |                   |                |          | Settings used by client, see [extra page](webfrontend) |
|`default_pics` | | | |
|&#8193;`background`                               | File           | No       | for the background | |
|&#8193;`logo`                                     | File           | No       | for the Easydb logo | |
|&#8193;`user_avatar`                              | File           | No       | for user images | |
|`eas` | | | |
|&#8193;`external_url`                             | String         | No       | URL for the EAS connection from outside of Easydb. Only set this, if the EAS is running on a different Server. By default, this is the same as `server.external_url`. In Docker Containers, always `server.external_url` is used. | |
|&#8193;`instance`                                 | String         | Yes      | Name of the  EAS-Instance | |
|&#8193;`produce_settings`                         | File           | Yes      | EAS-Produce-Settings (JSON) | |
|&#8193;`supervisor_enabled`                       | Boolean        | Yes      | Whether the supervisor is running | `true` |
|&#8193;`thumbnail_size`                           | Integer        | Yes      | Thumbnail size| `128` |
|&#8193;`url`                                      | String         | Yes      | URL for the EAS connection | |
|&#8193;`vhost`                                    | String         | No       | V-Host | |
|&#8193;`rights_management` | | | |
|&#8193;&#8193;`<class>`                        |                |          | Configuration for EAS class (image, video, audio, office, directory, unknown) | |
|&#8193;&#8193;&#8193;`versions` | | | |
|&#8193;&#8193;&#8193;&#8193;`export`           | Boolean        | Yes      | Whether the version is available for export | |
|&#8193;&#8193;&#8193;&#8193;`group`            | String         | No       | Display name for the version grouping | |
|&#8193;&#8193;&#8193;&#8193;`rightsmanagement` | Boolean        | No       | Whether the version is right-managed | `false` |
|&#8193;&#8193;&#8193;&#8193;`size_limit`       | Integer        | No       | Version size  (determines the maximum size that can be produced if one has the right) | |
|&#8193;&#8193;&#8193;&#8193;`size_print`       | String         | No       | display text for the Version | |
|&#8193;&#8193;&#8193;&#8193;`standard`         | Boolean        | No       | Whether the version is included in standard | `false` |
|&#8193;&#8193;&#8193;&#8193;`version`          | String         | Yes      | Name of the Version | |
|&#8193;&#8193;&#8193;&#8193;`watermark`        | Boolean        | No       | Whether the version has a watermark | `false` |
|&#8193;&#8193;&#8193;&#8193;`zoomable`         | Boolean        | No       | Whether the version is available for the zoomer | `false` |
|`elasticsearch` | | | |
|&#8193;`begin_with_wildcards_allowed`             | Boolean        | No       | Whether Suggest wildcards are allowed at the beginning | `false` |
|&#8193;`connect_timeout_ms`                       | Integer        | Yes      | connection timeout (ms) | `30000` (30 seconds) |
|&#8193;`default_template`                         | File           | No       | [Elasticsearch index template](https://www.elastic.co/guide/en/elasticsearch/reference/5.6/indices-templates.html) file. Can be used to override per-index settings, such as number of shards. |`es_default_template.json` ¹ |
|&#8193;`fielddata_memory`                         | String-List    | No       | Index fields that use `"memory"` as Fielddata type | |
|&#8193;`settings`                                 | File           | Yes      | Index-Settings (JSON) | |
|&#8193;`synonym_list`                             | File           | No       | synonym mapping file either in Solr or WordNet format (see https://www.elastic.co/guide/en/elasticsearch/reference/5.6/analysis-synonym-tokenfilter.html). The file is used on index creation time, so if this value is changed, the index has to be recreated. | |
|&#8193;`transfer_timeout_ms`                      | Integer        | Yes      | transmission timeout (ms) | `300000` (5 minutes) |
|&#8193;`url`                                      | String         | Yes      | URL | |
|&#8193;`max_limit`                                | Integer        | Yes      | maximum for `search.limit` for elasticsearch requests | `1000` |
|`imexporter-database` | | | |
|&#8193;`dsn`                        | String         | Yes      | DSN for the Database connection | |
|&#8193;`schema`                     | String         | Yes      | Database Scheme | ||`schema` | | | |
|`plugins`| | | |
|&#8193;`url_prefix_internal`                      | String         | No       | URL prefix for internal connections | value of `"url_prefix"` |
|&#8193;`url_prefix_external`                      | String         | No       | URL prefix for external connections | value of `"url_prefix"` |
|&#8193;`url_prefix`                               | String         | No       | URL prefix for internal or external connections | (no prefix) |
|`schema` | | | |
|&#8193;`base_dir`                                 | Catalogue      | Yes      | Base-Schema-Folder | |
|&#8193;`dsn`                                      | String         | Yes      | DSN for the Database connection | |
|&#8193;`user_dir`                                 | Catalogue      | Yes      | User-Schema-Folder | |
|`server` | | | |
|&#8193;`api` | | | |
|&#8193;&#8193;`settings` | | | |
|&#8193;&#8193;&#8193;`buildsuggest`             | Boolean        | No       | Allow requests on `POST /api/v1/settings/buildsuggest` | `false` |
|&#8193;&#8193;&#8193;`purgeall`                 | Boolean        | No       | Allow requests on `POST /api/v1/settings/purgeall` | `false` |
|&#8193;&#8193;&#8193;`purgedata`                | Boolean        | No       | Allow requests on `POST /api/v1/settings/purgedata` | `false` |
|&#8193;&#8193;&#8193;`reindex`                  | Boolean        | No       | Allow requests on `POST /api/v1/settings/reindex` | `false` |
|&#8193;&#8193;&#8193;`restart`                  | Boolean        | No       | Allow requests on `POST /api/v1/settings/restart` | `false` |
|&#8193;&#8193;&#8193;`updatecustomdata`         | Boolean        | No       | Allow requests on `POST /api/v1/settings/updatecustomdata` | `false` |
|&#8193;`custom_datatype_updater` | | | |
|&#8193;&#8193;`enabled`                          | Boolean        | Yes      | Whether the custom datatype updater is running | `true` |
|&#8193;`directory` | | | |
|&#8193;&#8193;`imexporter`                       | Catalogue      | Yes      | Imexporter Directory | |
|&#8193;&#8193;`l10n_dir`                         | Catalogue      | Yes      | Catalogues for the L10n configuration | |
|&#8193;&#8193;`logfile`                          | File           | Yes      | Log-File | `/tmp/easydb-server.log` |
|&#8193;&#8193;`output`                           | Catalogue      | Yes      | output directory | |
|&#8193;&#8193;`pflib`                            | Catalogue      | Yes      | Directory where the pflib is located | |
|&#8193;&#8193;`plans`                            | Catalogue      | Yes      | Plans (only for Imexporter) | |
|&#8193;&#8193;`server_errors`                    | Catalogue      | No       | Catalog for Server Error Information | `<directory/logfile>.errors` |
|&#8193;&#8193;`tmp`                              | Catalogue      | Yes      | Catalogue for temporary files | |
|&#8193;&#8193;`umask`                            | Integer        | Yes      | umask | `022` |
|&#8193;`dirty_queuer` | | | |
|&#8193;&#8193;`num_processes`                    | Integer        | Yes      | Number of processes | `1` |
|&#8193;`exporter` | | | |
|&#8193;&#8193;`batch_size`                       | Integer        | Yes      | Batch Size | `100` |
|&#8193;&#8193;`max_xml_size_for_xslt`            | Integer        | Yes      | Max. size for XML Files to allow XSLT post processing (in MB) | `10` |
|&#8193;&#8193;`num_workers`                      | Integer        | Yes      | Number of Workers | `0` |
|&#8193;`external_url`                             | String         | No       | URL for the Server connection from outside of Easydb | |
|&#8193;`frontend` | | | |
|&#8193;&#8193;`fast`| | | |
|&#8193;&#8193;&#8193;`num_services`              | Integer        | No       | Number of services in "fast" group (e.g. event polling) | 0 |
|&#8193;&#8193;&#8193;`socket`                    | File           | No       | Socket of "fast" group | |
|&#8193;&#8193;`medium`| | | |
|&#8193;&#8193;&#8193;`num_services`              | Integer        | No       | Number of services in "medium" group (most requests) | 0 |
|&#8193;&#8193;&#8193;`socket`                    | File           | No       | Socket of "medium" group | |
|&#8193;&#8193;`num_services`                     | Integer        | Yes      | Number of services (deprecated; superseded by `server.frontend.slow.num_services`) | `0` |
|&#8193;&#8193;`slow`| | | |
|&#8193;&#8193;&#8193;`num_services`              | Integer        | No       | Number of services in "slow" group (e.g. synchronous download service) | 0 |
|&#8193;&#8193;&#8193;`socket`                    | File           | No       | Socket of "slow" group | |
|&#8193;&#8193;`socket`                           | File           | Yes      | Socket (deprecated; superseded by `server.frontend.slow.socket`)| `/tmp/easydb-server-frontend.sock` |
|&#8193;`imexporter` | | | |
|&#8193;&#8193;`num_services`                     | Integer        | Yes      | Number of services | `2` |
|&#8193;&#8193;`socket`                           | File           | Yes      | Socket | `/tmp/easydb-server-imexporter.sock` |
|&#8193;`indexer` | | | |
|&#8193;&#8193;`num_processes`                    | Integer        | Yes      | Number of processes | `1` |
|&#8193;&#8193;`objects_per_batch`                | Integer        | Yes      | Number of objects in a batch | `1000` |
|&#8193;`janitor` | | | |
|&#8193;&#8193;`eas_sync_commit`                  | Boolean        | No       | Enable asset status sync to EAS. Assets not linked in easydb are removed by EAS janitor | `true` |
|&#8193;&#8193;`enabled`                          | Boolean        | Yes      | Whether the janitor is running | `true` |
|&#8193;&#8193;`interval`                         | Integer        | Yes      | How often the Janitor runs (every X seconds) | `600` (10 minutes) |
|&#8193;&#8193;`max_age`                          | Integer        | Yes      | When a file expires (after X seconds) | `259200` (3 days) |
|&#8193;`mailer` | | | |
|&#8193;&#8193;`enabled`                          | Boolean        | Yes      | Whether the mailer is running | `true` |
|&#8193;&#8193;`envelope_address`                 | String         | Yes      | Envelope Address | |
|&#8193;&#8193;`interval`                         | Integer        | Yes      | How often the mailer runs (every X seconds) | `60` (1 Minute) |
|&#8193;&#8193;`max_attempts`                     | Integer        | Yes      | Number of attempts before an e-mail is classified as undeliverable | `3` |
|&#8193;&#8193;`sender_address`                   | String         | Yes      | Sender Address | `easydb-server@localhost` |
|&#8193;`preindexer` | | | |
|&#8193;&#8193;`num_processes`                    | Integer        | Yes      | Number of processes | `1` |
|&#8193;`upload` | | | |
|&#8193;&#8193;`num_services`                     | Integer        | Yes      | Number of services | `2` |
|&#8193;&#8193;`socket`                           | File           | Yes      | Socket | `/tmp/easydb-server-upload.sock` |
|`solution` | | | |
|&#8193;`name`                                    | String         | Yes      | Name of the Solution used | |
|&#8193;`plugins`                                 | File-List      | No       | List of Solution Plugins | (empty) |
|`suggest` | | | |
|&#8193;`aggregation_chunksize`                   | Integer        | Yes      | Number of Objects that are used to aggregate the fields in one batch. Should not be more than `1000`. The higher the number of objects, the bigger the response size will be, also the more complex the objecttype is, the more fields will be aggregated at once. | `1000` |
|&#8193;`document_chunksize`                      | Integer        | Yes      | Batch Size (in MB) of aggregated documents that are uploaded to the Suggest Index after words and contexts were generated. Must not be more than the maximum request size of the Elasticsearch Instance | `100` |
|&#8193;`fields_per_aggregation_chunksize`        | Integer        | Yes      | Defines how many fields of an objecttype are grouped in an aggregation. The higher this number, the fewer aggregation requests are sent, but the higher the request and response sizes will be. If this value is not a positive number, all fields of an objecttype are aggregated at once. | `0` (every field is aggregated seperatedly) |
|&#8193;`max_context_map_size`                    | Integer        | Yes      | Maximum number of keys in the temporary map of words and contexts that is kept in the RAM, before a batch upload of the suggest index documents is started | `10 000` |
|&#8193;`settings`                                | File           | Yes      | Path to the JSON File with the Elasticsearch Settings for the Suggest Index | `es_suggest_settings.json` |
|&#8193;`timestamps`                              | String List    | No       | Array of Time Stamps when the Suggest Index is rebuilt. Excpected Format: `HH:MM` | `["00:00", "02:00", "04:00", "06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"]` |
|`nodejs` | | | |
|&#8193;`node_runner_binary`                      | String         | Yes      | Path to the NodeJS instance used by the server to run JavaScript              | `"/usr/bin/env node"`              |
|&#8193;`node_modules`                            | String         | Yes      | Path to the `node_modules` folder of the NodeJS instance                      | `"../../node-runner/node_modules"` |
|&#8193;`node_runner_app`                         | String         | Yes      | Path to the [Node Runner](/en/technical/node-runner/#node-runner) script file | `"../../node-runner/app.js"`       |

¹ contains somethings like:
```json
{
    "template": "*",
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    }
}
```
