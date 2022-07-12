---
title: "Asset Versions"
menu:
  main:
    name: "File Versions"
    identifier: "sysadmin/configuration/easydb-server.yml/versions"
    weight: -994
    parent: "sysadmin/configuration/easydb-server.yml"
---

# File versioning

## File size for download and preview

For each asset (picture, document, etc.) easydb provides automatically calculated variants of each asset, in order to be able to quickly display a small preview and to enable downloading in uniform image sizes.

These standard variants (or _versions_*) were chosen for user convenience. We recommend that you first check whether these variants are sufficient for you.

If your application requires other variants, additional variants can be configured as follows. To make the changes effective, just restart the `easydb-server` container.

* A version is created in easydb by editing the original application file, e. g. by cropping. A data record can therefore have an original file with several versions. For a clear differentiation, the different file sizes for previews and downloads is called variants here.

## Configuration

Add the following lines to the configuration, e.g. `config/easydb-server.yml`. The storage location of the `config` directory was defined during the [Installation](../../../installation).

Make sure to not create duplicate lines. If a line already exists, e.g. `include_before:`, then only put the missing line beneath it. Make sure to use correct indentation. If in doubt use a linter tool or ask us for help. Problems of this kind can prevent the easydb from starting. We suggest to keep a backup of your previous configuration.

```yaml
include_before:
  - /config/eas_rights_management.yml

eas:
  produce_settings: /config/eas_produce.json
```

The file given for `produce_settings` defines which variants are created after the upload.

Get the default configuration of variants as a starting point and for editing:

```bash
docker cp easydb-server:/easydb-5/base/eas/rights_management.yml /srv/easydb/config/eas_rights_management.yml
docker cp easydb-server:/easydb-5/base/eas/eas-produce.json      /srv/easydb/config/eas_produce.json
```

For more about the version configuration checkout [eas_rights_management.yml](eas_rights_management.yml) and [eas_produce.json](eas_produce.json).
