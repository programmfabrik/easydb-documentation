---
title: "easydb-server.yml"
layout: config
menu:
  main:
    name: "easydb-server.yml"
    identifier: "sysadmin/configuration/easydb-server.yml"
    parent: "sysadmin/configuration"
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

A list of easydbs variables can be found [here](available-variables/).