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

### rights_management.yml variables
| Variable                                           | Typ           | Pflicht | Erklärung | Default-Wert |
|----------------------------------------------------|---------------|---------|-----------|--------------|
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

## Example eas rights_management:

```yaml
eas:
  rights_management:
    image:
      versions:
        - version: small
          size_print: 250px jpg
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px jpg
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 1000px jpg (watermark)
          size_limit: 1000
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: huge
          size_print: 2000px jpg
          size_limit: 2000
          export: true
          rightsmanagement: true
          group: huge
          zoomable: true
        - version: full
          size_print: Original jpg
          export: true
          rightsmanagement: true
          group: huge
          zoomable: true
    video:
      versions:
        - version: small
          size_print: 250px jpg
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 720px jpg
          size_limit: 720
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
        - version: preview_watermark
          size_print: 720px jpg (watermark)
          size_limit: 720
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: huge
          size_print: 1920px jpg
          size_limit: 1920
          export: true
          group: huge
          rightsmanagement: true
          zoomable: true
        - version: 360p
          size_print: 360p
          size_limit: 360
          export: true
          group: preview
          rightsmanagement: true
        - version: 720p
          size_print: 720p
          size_limit: 720
          export: true
          group: preview
          rightsmanagement: true
        - version: 1920p
          size_print: 1920p
          size_limit: 1920
          export: true
          rightsmanagement: true
          group: huge
    audio:
      versions:
        - version: small
          size_print: 250px (small)
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
        - version: preview_watermark
          size_print: 1000px (watermark)
          size_limit: 1000
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: aac
          size_print: aac
          export: true
          rightsmanagement: true
    office:
      versions:
        - version: small
          size_print: 250px (small)
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
        - version: preview_watermark
          size_print: 1000px (watermark)
          size_limit: 1000
          export: true
          rightsmanagement: true
          group: preview
          zoomable: true
          watermark: true
        - version: pages
          size_print: pages
          rightsmanagement: true
          use_for_pages: true
    archive:
      versions:
        - version: small
          size_print: 250px (small)
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
        - version: directory
          size_print: directory
          group: huge
          rightsmanagement: true
    unknown:
      versions: []
    vector2d:
      versions:
        - version: small
          size_print: 250px png
          size_limit: 250
          export: true
          group: thumbnail
          rightsmanagement: false
          standard: true
        - version: preview
          size_print: 1000px png
          size_limit: 1000
          export: true
          group: preview
          rightsmanagement: true
          zoomable: true
    vector3d:
      versions: []
```