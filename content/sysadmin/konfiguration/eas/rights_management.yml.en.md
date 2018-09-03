---
title: rights_management.yml
layout: config
menu:
  main:
    name: "rights_management.yml"
    identifier: sysadmin/konfiguration/eas/rights_management.yml
    parent: sysadmin/konfiguration/eas
    weight: 2
easydb-server.yml:
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
---
# rights_management.yml

## EAS variables

{{< getFileContent file="/content/sysadmin/konfiguration/includes/eas_rightsmanagement.var.md" markdown="true" >}}

## Example eas rights_management:

{{< getFileContent file="/content/sysadmin/konfiguration/includes/eas-example-configuration.md" markdown="true" >}}