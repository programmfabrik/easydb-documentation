---
title: "elasticsearch.yml"
layout: config
menu:
  main:
    name: "elasticsearch.yml"
    identifier: "sysadmin/konfiguration/elasticsearch.yml"
    parent: "sysadmin/konfiguration"
    weight: 8000
elasticsearch.yml:
  - elasticsearch.connect_timeout_ms
  - elasticsearch.transfer_timeout_ms
  - elasticsearch.fielddata_memory
  - elasticsearch.settings
  - elasticsearch.begin_with_wildcards_allowed
---
# elasticsearch.yml

## Variables

{{< getFileContent file="/content/sysadmin/konfiguration/includes/elasticsearch.var.md" markdown="true" >}}