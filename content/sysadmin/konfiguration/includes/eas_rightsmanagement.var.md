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
