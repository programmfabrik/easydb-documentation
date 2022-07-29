---
menu:
  main:
    name: "5.103 (July 2022)"
    identifier: "5.103"
    parent: "releases"
    weight: -603
---

> This version **does not require a new index build**

# Version 5.103.2

*Released on 29.07.2022*

# Webfrontend

## Fixed

* **Lists**: show objecttypes with read but no create permissions

# Server

## Fixed

* **Search**: fix system right `system.group[global_custom_bag_read]` for `acl` searches

# Version 5.103.1

*Released on 27.07.2022*

# Webfrontend

## Fixed

* **Export**: don't automatically apply first template
* **Print**: fix error when opening print dialog

# Server

## Fixed

* **Wordpress plugin**: fixed OAuth configuration

# Version 5.103.0

*Released on 20.07.2022*

# Webfrontend

## New

* **Messages**: permanent messages can be provided with icon
* **General**: customer logo can be configured as a link to a web page

## Improved

* **Editor**: everywhere on EAS columns can be clicked if they don't contain an asset yet
* **Rights manager**: when assigning rights it is shown for which user/group rights are currently assigned
* **Print dialog**: Field selection for PDF templates and standard layouts
* **CSV importer**: metadata mapping for rput option disabled because not applicable

## Fixed

* **Image view**: Preview images with watermark are used again if no sufficiently large versions without watermark are available
* **Search**: Search by aspect ratio fixed
* **Detail**: Panel is displayed again even if it contains only a CustomFieldRenderer
* **Editor**: calendar allowed time selection even if the field could hold only one date, fixed
* **Editor**: fixed incorrect mask selection

# Server

## Improved

* **Base configuration**: new parameter `system.logo.external_url`
* **EAS**: watermark size is also accepted as a simple number
* **Messages**: `webfrontend_props` are output for `pending_tasks`, if available

## Fixed

* **General**: cache invalidation when changing reverse links
* **General**: support of long column names for some data types fixed
* **EAS**: Status uses end time instead of start time for recently finished jobs (recent-done/recent-failed)
* **EAS**: Workaround for writing metadata to files with existing invalid metadata
* **Search**: Wildcard search does not search in tokens

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome               sha256:fd0a83f7f0e2432c21689386e78b205a86466b6fbe8dfb48192c7c8e2b7c09be
docker.easydb.de/pf/eas                  sha256:d9ea068020505588b2dee54dd8a4b54cf20692a8d77384a5618d6defdb1fbbc7
docker.easydb.de/pf/elasticsearch        sha256:9a19a70271f3e09a4757bec670fc00f012d3b7185ed383e4c8d5cc7bc121fa4f
docker.easydb.de/pf/fylr                 sha256:b545f0227558d4e8b55d705127aa4cc418edea6c75e99ff64132b3aee33d2702
docker.easydb.de/pf/postgresql-11        sha256:30eb077d11e7a1e7185b3623bec46c6bae65e9d2156393490ec9322ebc673985
docker.easydb.de/pf/postgresql-14        sha256:308a7a809706fcd80e60aba523dba8adbd7609c0e606e08ea8083d22173c8890
docker.easydb.de/pf/server-base          sha256:9a768a503d73fa5ee07d56a5eb713885687d312c9d7211387ec960f78ff2ed68
docker.easydb.de/pf/webfrontend          sha256:802dd582c392aac237f063ec4050225f0e06dda22b63f581435cb4013a598660
```

Translated with www.DeepL.com/Translator (free version)
