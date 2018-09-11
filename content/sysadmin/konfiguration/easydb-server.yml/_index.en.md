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

# easydb-server.yml

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

{{< getFileContent file="/content/sysadmin/konfiguration/includes/easydb-tbl-variable-type.md" markdown="true" >}}

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

{{< getFileContent file="/content/sysadmin/konfiguration/includes/base.var.md" markdown="true" >}}

{{< getFileContent file="/content/sysadmin/konfiguration/includes/solution.var.md" markdown="true" >}}

{{< getFileContent file="/content/sysadmin/konfiguration/includes/server.var.md" markdown="true" >}}

{{< getFileContent file="/content/sysadmin/konfiguration/includes/schema.var.md" markdown="true" >}}

{{< getFileContent file="/content/sysadmin/konfiguration/includes/eas.var.md" markdown="true" >}}

{{< getFileContent file="/content/sysadmin/konfiguration/includes/default_pics.var.md" markdown="true" >}}

{{< getFileContent file="/content/sysadmin/konfiguration/includes/plugins.var.md" markdown="true" >}}

{{< getFileContent file="/content/sysadmin/konfiguration/includes/elasticsearch.var.md" markdown="true" >}}

File-List is a list of maps with "name" (String) and "file" (File).

{{< getFileContent file="/content/sysadmin/konfiguration/includes/exporter.var.md" markdown="true" >}}

{{< getFileContent file="/content/sysadmin/konfiguration/includes/debug.var.md" markdown="true" >}}

---