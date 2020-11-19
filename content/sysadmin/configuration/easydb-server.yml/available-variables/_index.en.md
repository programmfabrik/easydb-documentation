---
title: "List of variables for easydb-server.yml"
menu:
  main:
    name: "List of variables"
    identifier: "sysadmin/configuration/easydb-server.yml/variables"
    weight: -999
    parent: "sysadmin/configuration/easydb-server.yml"
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
  - server.api.settings.buildsuggest
  - server.api.settings.reindex
  - server.api.user.include_password
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
  - elasticsearch.default_template
  - elasticsearch.transfer_timeout_ms
  - elasticsearch.fielddata_memory
  - elasticsearch.settings
  - elasticsearch.begin_with_wildcards_allowed
  - elasticsearch.max_limit
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
  - nodejs.node_runner_binary
  - nodejs.node_modules
  - nodejs.node_runner_app
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
smtp:
  - server
  - from-address
  - hostname
---

# Available variables

## List of variables

**Please note that most of the following variables are set by default, so you do not need to configure them.**

> In yml-files created by Programmfabrik we use an indentation of 2 spaces per &#8680;.

| Variable <div style="width:300px"></div>           | Type           | Required | Description | Default |
|----------------------------------------------------|----------------|----------|-------------|---------|
| `include_before`                                   | File-List      | No       | List of files that are loaded before the file in which it is defined | |
|                                                    |                |          |             |         |
| `include_after`                                    | File-List      | No       | List of files that are loaded after the file in which it is defined | |
|                                                    |                |          |             |         |
| `base` | | | |
| &#8680;`plugins`                                   | File-List      | No       | List of base plugins | (empty) |
| &#8680;`exporter` | | | |
| &#8680;&#8680;`batch_size`                       | Integer        | Yes      | Batch Size | `100` |
| &#8680;&#8680;`max_xml_size_for_xslt`            | Integer        | Yes      | Max. size for XML Files to allow XSLT post processing (in MB) | `10` |
| &#8680;&#8680;`num_workers`                      | Integer        | Yes      | Number of Workers | `0` |
|                                                    |                |          |             |         |
| `debug` | | | |
| &#8680;`exporter_fail`        |
| &#8680;`exporter_sleep`       |
| &#8680;`exporter_warnings`    |
| &#8680;`search_sleep`         |
|                                                    |                |          |             |         |
| `default_client`              |                   |                |          | Settings used by client, see [extra page](../webfrontend) |
|                                                    |                |          |             |         |
| `default_pics` | | | |
| &#8680;`background`                               | File           | No       | for the background | |
| &#8680;`logo`                                     | File           | No       | for the Easydb logo | |
| &#8680;`user_avatar`                              | File           | No       | for user images | |
|                                                    |                |          |             |         |
| `eas` | | | |
| &#8680;`external_url`                             | String         | No       | URL for the EAS connection from outside of Easydb. Only set this, if the EAS is running on a different Server. By default, this is the same as `server.external_url`. In Docker Containers, always `server.external_url` is used. | |
| &#8680;`instance`                                 | String         | Yes      | Name of the  EAS-Instance | |
| &#8680;`produce_settings`                         | File           | Yes      | EAS-Produce-Settings (JSON) | |
| &#8680;`supervisor_enabled`                       | Boolean        | Yes      | Whether the supervisor is running | `true` |
| &#8680;`thumbnail_size`                           | Integer        | Yes      | Thumbnail size| `128` |
| &#8680;`url`                                      | String         | Yes      | URL for the EAS connection | |
| &#8680;`vhost`                                    | String         | No       | V-Host | |
| &#8680;`rights_management` | | | |
| &#8680;&#8680;`<class>`                        |                |          | Configuration for EAS class (image, video, audio, office, directory, unknown) | |
| &#8680;&#8680;&#8680;`versions` | | | |
| &#8680;&#8680;&#8680;&#8680;`export`           | Boolean        | Yes      | Whether the version is available for export | |
| &#8680;&#8680;&#8680;&#8680;`group`            | String         | No       | Display name for the version grouping | |
| &#8680;&#8680;&#8680;&#8680;`rightsmanagement` | Boolean        | No       | Whether the version is right-managed | `false` |
| &#8680;&#8680;&#8680;&#8680;`size_limit`       | Integer        | No       | Version size  (determines the maximum size that can be produced if one has the right) | |
| &#8680;&#8680;&#8680;&#8680;`size_print`       | String         | No       | display text for the Version | |
| &#8680;&#8680;&#8680;&#8680;`standard`         | Boolean        | No       | Whether the version is included in standard | `false` |
| &#8680;&#8680;&#8680;&#8680;`version`          | String         | Yes      | Name of the Version | |
| &#8680;&#8680;&#8680;&#8680;`watermark`        | Boolean        | No       | Whether the version has a watermark | `false` |
| &#8680;&#8680;&#8680;&#8680;`zoomable`         | Boolean        | No       | Whether the version is available for the zoomer | `false` |
|                                                    |                |          |             |         |
| `elasticsearch`
| &#8680;`begin_with_wildcards_allowed`             | Boolean        | No       | Whether Suggest wildcards are allowed at the beginning | `false` |
| &#8680;`connect_timeout_ms`                       | Integer        | Yes      | connection timeout (ms) | `30000` (30 seconds) |
| &#8680;`default_template`                         | File           | No       | [Elasticsearch index template](https://www.elastic.co/guide/en/elasticsearch/reference/5.6/indices-templates.html) file. Can be used to override per-index settings, such as number of shards. |`es_default_template.json` ¹ |
| &#8680;`fielddata_memory`                         | String-List    | No       | Index fields that use `"memory"` as Fielddata type | |
| &#8680;`settings`                                 | File           | Yes      | Index-Settings (JSON) | |
| &#8680;`synonym_list`                             | File           | No       | synonym mapping file either in Solr or WordNet format (see https://www.elastic.co/guide/en/elasticsearch/reference/5.6/analysis-synonym-tokenfilter.html). The file is used on index creation time, so if this value is changed, the index has to be recreated. | |
| &#8680;`transfer_timeout_ms`                      | Integer        | Yes      | transmission timeout (ms) | `300000` (5 minutes) |
| &#8680;`url`                                      | String         | Yes      | URL | |
| &#8680;`max_limit`                                | Integer        | Yes      | maximum for `search.limit` for elasticsearch requests | `1000` |
|                                                    |                |          |             |         |
| `fastcgi-read-timeout`                            | Integer        | No       | Timeout for API requests in seconds. It does not affect upload and download requests, which already have higher timeouts. Only available when using Docker containers. | `300` (5 minutes) |
| `fylr-read-timeout`                               | Integer        | No       | Timeout for requests to the `fylr` server (e.g. for PDF creation). Only available when using Docker containers. | `300` (5 minutes) |
| `hostnames` | | | |
| &#8680;`eas`                               | String           | Yes       | name of the eas container | easydb-eas |
| &#8680;`fylr`                                     | String           | Yes       | name of the fylr container | easydb-fylr |
| &#8680;`server`                              | String           | Yes       | name of the server container | easydb-server |
| &#8680;`elasticsearch`                              | String           | Yes       | name of the elasticsearch container | easydb-elasticsearch |
| `imexporter-database` | | | |
| &#8680;`dsn`                        | String         | Yes      | DSN for the Database connection | |
| &#8680;`schema`                     | String         | Yes      | Database Scheme | ||`schema` | | | |
|                                                    |                |          |             |         |
| `plugins`
| &#8680;`url_prefix_internal`                      | String         | No       | URL prefix for internal connections | value of `"url_prefix"` |
| &#8680;`url_prefix_external`                      | String         | No       | URL prefix for external connections | value of `"url_prefix"` |
| &#8680;`url_prefix`                               | String         | No       | URL prefix for internal or external connections | (no prefix) |
|                                                    |                |          |             |         |
| `schema` | | | |
| &#8680;`base_dir`                                 | Catalogue      | Yes      | Base-Schema-Folder | |
| &#8680;`dsn`                                      | String         | Yes      | DSN for the Database connection | |
| &#8680;`user_dir`                                 | Catalogue      | Yes      | User-Schema-Folder | |
|                                                    |                |          |             |         |
 `server` | | | |
| &#8680;`allow_all_origins`                      | Boolean        | No       | Always send CORS headers allowing Origin, ignores base configuration. Use this setting only in non-production environments as it circumvents a browser security feature. | false |
| &#8680;`api` | | | |
| &#8680;&#8680;`settings` | | | |
| &#8680;&#8680;&#8680;`buildsuggest`             | Boolean        | No       | Allow requests on `POST /api/v1/schema/buildsuggest` | `false` |
| &#8680;&#8680;&#8680;`purgeall`                 | Boolean        | No       | Allow requests on `POST /api/v1/schema/purgeall` | `false` |
| &#8680;&#8680;&#8680;`purgedata`                | Boolean        | No       | Allow requests on `POST /api/v1/schema/purgedata` | `false` |
| &#8680;&#8680;&#8680;`reindex`                  | Boolean        | No       | Allow requests on `POST /api/v1/schema/reindex` | `false` |
| &#8680;&#8680;&#8680;`restart`                  | Boolean        | No       | Allow requests on `POST /api/v1/schema/restart` | `false` |
| &#8680;&#8680;&#8680;`updatecustomdata`         | Boolean        | No       | Allow requests on `POST /api/v1/settings/updatecustomdata` | `false` |
| &#8680;&#8680;`user` | | | |
| &#8680;&#8680;&#8680;`include_password`         | Boolean        | No       | Allow requests on `GET /api/v1/user` with url parameter `include_password=true` | `false` |
| &#8680;`custom_datatype_updater` | | | |
| &#8680;&#8680;`enabled`                         | Boolean        | Yes      | Whether the custom datatype updater is running | true|
| &#8680;`directory` | | | |
| &#8680;&#8680;`imexporter`                       | Catalogue      | Yes      | Imexporter Directory | |
| &#8680;&#8680;`l10n_dir`                         | Catalogue      | Yes      | Catalogues for the L10n configuration | |
| &#8680;&#8680;`logfile`                          | File           | Yes      | Log-File | `/tmp/easydb-server.log` |
| &#8680;&#8680;`output`                           | Catalogue      | Yes      | output directory | |
| &#8680;&#8680;`pflib`                            | Catalogue      | Yes      | Directory where the pflib is located | |
| &#8680;&#8680;`plans`                            | Catalogue      | Yes      | Plans (only for Imexporter) | |
| &#8680;&#8680;`server_errors`                    | Catalogue      | No       | Catalog for Server Error Information | `<directory/logfile>.errors` |
| &#8680;&#8680;`tmp`                              | Catalogue      | Yes      | Catalogue for temporary files | |
| &#8680;&#8680;`umask`                            | Integer        | Yes      | umask | `022` |
| &#8680;`dirty_queuer`                            | | | |
| &#8680;&#8680;`num_processes`                    | Integer        | Yes      | Number of processes | `1` |
| &#8680;`exporter`                                | | | |
| &#8680;&#8680;`batch_size`                       | Integer        | Yes      | Batch Size | `100` |
| &#8680;&#8680;`max_xml_size_for_xslt`            | Integer        | Yes      | Max. size for XML Files to allow XSLT post processing (in MB) | `10` |
| &#8680;&#8680;`num_workers`                      | Integer        | Yes      | Number of Workers | `0` |
| &#8680;`external_url`                            | String         | No       | URL for the Server connection from outside of Easydb | |
| &#8680;`frontend` | | | |
| &#8680;&#8680;`fast`| | | |
| &#8680;&#8680;&#8680;`num_services`              | Integer        | No       | Number of services in "fast" group (e.g. event polling) | 0 |
| &#8680;&#8680;&#8680;`socket`                    | File           | No       | Socket of "fast" group | |
| &#8680;&#8680;`medium`| | | |
| &#8680;&#8680;&#8680;`num_services`              | Integer        | No       | Number of services in "medium" group (most requests) | 0 |
| &#8680;&#8680;&#8680;`socket`                    | File           | No       | Socket of "medium" group | |
| &#8680;&#8680;`num_services`                     | Integer        | Yes      | Number of services (deprecated; superseded by `server.frontend.slow.num_services`) | `0` |
| &#8680;&#8680;`slow`| | | |
| &#8680;&#8680;&#8680;`num_services`              | Integer        | No       | Number of services in "slow" group (e.g. synchronous download service) | 0 |
| &#8680;&#8680;&#8680;`socket`                    | File           | No       | Socket of "slow" group | |
| &#8680;&#8680;`socket`                           | File           | Yes      | Socket (deprecated; superseded by `server.frontend.slow.socket`)| `/tmp/easydb-server-frontend.sock` |
| &#8680;`imexporter` | | | |
| &#8680;&#8680;`num_services`                     | Integer        | Yes      | Number of services | `2` |
| &#8680;&#8680;`socket`                           | File           | Yes      | Socket | `/tmp/easydb-server-imexporter.sock` |
| &#8680;`indexer` | | | |
| &#8680;&#8680;`enabled`                          | Boolean        | Yes      | Whether the indexer is running | `true` |
| &#8680;&#8680;`num_processes`                    | Integer        | Yes      | Number of processes | `1` |
| &#8680;&#8680;`objects_per_batch`                | Integer        | Yes      | Number of objects in a batch | `1000` |
| &#8680;`janitor` | | | |
| &#8680;&#8680;`eas_sync_commit`                  | Boolean        | No       | Enable asset status sync to EAS. Assets not linked in easydb are removed by EAS janitor | `true` |
| &#8680;&#8680;`enabled`                          | Boolean        | Yes      | Whether the janitor is running | `true` |
| &#8680;&#8680;`interval`                         | Integer        | Yes      | How often the Janitor runs (every X seconds) | `600` (10 minutes) |
| &#8680;&#8680;`max_age`                          | Integer        | Yes      | When a file expires (after X seconds) | `259200` (3 days) |
| &#8680;`mailer` | | | |
| &#8680;&#8680;`enabled`                          | Boolean        | Yes      | Whether the mailer is running | `true` |
| &#8680;&#8680;`envelope_address`                 | String         | Yes      | Envelope Address | |
| &#8680;&#8680;`interval`                         | Integer        | Yes      | How often the mailer runs (every X seconds) | `60` (1 Minute) |
| &#8680;&#8680;`max_attempts`                     | Integer        | Yes      | Number of attempts before an e-mail is classified as undeliverable | `3` |
| &#8680;&#8680;`sender_address`                   | String         | Yes      | Sender Address | `easydb-server@localhost` |
| &#8680;`preindexer` | | | |
| &#8680;&#8680;`num_processes`                    | Integer        | Yes      | Number of processes | `1` |
| &#8680;`upload` | | | |
| &#8680;&#8680;`num_services`                     | Integer        | Yes      | Number of services | `2` |
| &#8680;&#8680;`socket`                           | File           | Yes      | Socket | `/tmp/easydb-server-upload.sock` |
|                                                    |                |          |             |         |
| `sso`              |                   |                |          | Settings used by sso, see [extra page](../plugins/sso) |
|                                                    |                |          |             |         |
| `ldap`              |                   |                |          | Settings used by ldap, see [extra page](../plugins/ldap) |
|
|`solution` | | | |
| &#8680;`name`                                    | String         | Yes      | Name of the Solution used | |
| &#8680;`plugins`                                 | File-List      | No       | List of Solution Plugins | (empty) |
|                                                    |                |          |             |         |
|`suggest` | | | |
| &#8680;`aggregation_chunksize`                   | Integer        | Yes      | Number of Objects that are used to aggregate the fields in one batch. Should not be more than `1000`. The higher the number of objects, the bigger the response size will be, also the more complex the objecttype is, the more fields will be aggregated at once. | `1000` |
| &#8680;`document_chunksize`                      | Integer        | Yes      | Batch Size (in MB) of aggregated documents that are uploaded to the Suggest Index after words and contexts were generated. Must not be more than the maximum request size of the Elasticsearch Instance | `100` |
| &#8680;`fields_per_aggregation_chunksize`        | Integer        | Yes      | Defines how many fields of an objecttype are grouped in an aggregation. The higher this number, the fewer aggregation requests are sent, but the higher the request and response sizes will be. If this value is not a positive number, all fields of an objecttype are aggregated at once. | `0` (every field is aggregated seperatedly) |
| &#8680;`max_context_map_size`                    | Integer        | Yes      | Maximum number of keys in the temporary map of words and contexts that is kept in the RAM, before a batch upload of the suggest index documents is started | `10 000` |
| &#8680;`settings`                                | File           | Yes      | Path to the JSON File with the Elasticsearch Settings for the Suggest Index | `es_suggest_settings.json` |
| &#8680;`timestamps`                              | String List    | No       | Array of Time Stamps when the Suggest Index is rebuilt. Excpected Format: `HH:MM` | `["00:00", "02:00", "04:00", "06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00", "22:00"]` |
|                                                    |                |          |             |         |
|`nodejs` | | | |
| &#8680;`node_runner_binary`                      | String         | Yes      | Path to the NodeJS instance used by the server to run JavaScript              | `"/usr/bin/env node"`              |
| &#8680;`node_modules`                            | String         | Yes      | Path to the `node_modules` folder of the NodeJS instance                      | `"../../node-runner/node_modules"` |
| &#8680;`node_runner_app`                         | String         | Yes      | Path to the [Node Runner](/en/technical/node-runner/#node-runner) script file | `"../../node-runner/app.js"`       |

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
