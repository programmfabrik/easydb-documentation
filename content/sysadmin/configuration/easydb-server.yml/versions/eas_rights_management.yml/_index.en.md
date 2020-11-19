---
title: "eas_rights_management"
menu:
  main:
    name: "eas_rights_management"
    identifier: "sysadmin/configuration/easydb-server.yml/versions/rightsmanagement"
    weight: -950
    parent: "sysadmin/configuration/easydb-server.yml/versions"
eas_rights_management.yml:
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

# eas_rights_management.yml

This file contains configuration settings that are relevant for the rights management. The settings always refer to variants of file previews. The files are divided into file classes:

* **image**
* **video**
* **audio**
* **office**
* **archive**
* **vector2d**
* **vector3d**
* **unknown**

## Variables

| Variable <div style="width:250px"></div>           | Typ <div style="width:100px"></div> | Required | Default | Description |
|----------------------------------------------------|---------------|---------|-----------|--------------|
| `eas:`                                             |               |         |         |              |
| &#8680;`rights_management:`                        |               |         |         |              |
| &#8680;&#8680;`<class>`                            |               |         |         |Configuration for EAS class (image, video, audio, office, directory, unknown, vector2d, vector3d) | |
| &#8680;&#8680;&#8680;`versions:`                   | [ ] Hierarchy |         |         |              |
| &#8680;&#8680;&#8680;&#8680;`version:`             | String        | Yes     |         |Name of the variant, wich must match the variant in `eas.produce_config`. |    |
| &#8680;&#8680;&#8680;&#8680;`size_print:`          | String        | No      |         |Variant as displayed in the Download and Export Manager. | |
| &#8680;&#8680;&#8680;&#8680;`size_limit:`          | Integer       | No      |         |Pixel limit for the rights management. If it is necessary to decide whether a download variant is allowed for the user during a mass download, this size is used and compared with the size of the preview. The variant is released if it is less than or equal to the limit in pixels. | |
| &#8680;&#8680;&#8680;&#8680;`export:`              | Boolean       | Yes     |         | If set, the variant is always available for download or export. | |
| &#8680;&#8680;&#8680;&#8680;`rightsmanagement:`    | Boolean       | No      |         | If set, this variant not allowed by the rights management and requires permission via the rights management. |
| &#8680;&#8680;&#8680;&#8680;`group:`               | String        | No      |         | Variants for the Export Manager can be gatherd in groups and are available in the URLs area, then. Group names can be chosen arbitrarily, but there are only following translations available in easydb: **thumbnail** (small), **preview** (preview), **huge** (large). | |
| &#8680;&#8680;&#8680;&#8680;`zoomable:`            | Boolean       | No      |         | If set, this variant is declared as zoomable. The frontend then displays the zoomer if desired. Only **PNG** and **JPEG** can be zoomed. |
| &#8680;&#8680;&#8680;&#8680;`watermark:`           | Boolean       | No      | `false` | Whether the version has a watermark |
| &#8680;&#8680;&#8680;&#8680;`standard:`            | Boolean       | No      | `false` | Whether the version is included in standard |

# Example eas_rights_management.yml:

```yaml
eas:
  rights_management:
    image:
      versions:
        - version: small
          size_print: 250px
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
    video:
      versions:
        - version: small
          size_print: 250px
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
    audio:
      versions:
        - version: small
          size_print: 250px (small)
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
    office:
      versions:
        - version: small
          size_print: 250px (small)
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
    archive:
      versions:
        - version: small
          size_print: 250px (small)
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
    unknown:
      versions: []
    vector2d:
      versions:
        - version: small
          size_print: 250px
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
    vector3d:
      versions: []
```

For complete examples about versioning in easydb5, please refer to [this](../example).