---
menu:
  main:
    name: "5.114 (Mid March 2023)"
    identifier: "5.114"
    parent: "releases"
    weight: -614
---


> This version **does not require** a new index build

# Version 5.114.0

*Released on 22.03.2023*

# Webfrontend

## Improved

* **Connector**: improved warnings
* **Full screen view**: View is closed when result is to be displayed in search
* **Detail/Editor**: creation time visible in footer
* **Plugins**: Pool information available in replacements

## Fixed

* **Search**: Creating child records fixed when sidebar was closed.
* **Mask Editor**: Input of comments only from spaces/line breaks fixed.
* **Search**: Selection of all records of page in table view fixed.
* **Crop tool**: Fixed error when creating a new version
* **Connector**: Fixed error when accessing unavailable instance.
* **CSV Importer**: Warnings and log download improved

# Server

## Improved

* **/api/v1/db**: extended asset information for `all_versions`.
* **export mapping**: date and time types supported in XML mapping

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/chrome:5.114.0         sha256:72a179dc663bdc40f04aa0806f843b969e2964aa562354eb9bf1d4b175d285cc
docker.easydb.de/pf/eas:5.114.0            sha256:d08967f091e9271754be3bb8375b945dab43a499ffdad84fde72f7a49aafa63d
docker.easydb.de/pf/elasticsearch:5.114.0  sha256:2ac0c307bc4a03300ee0c149cae11872efa99d9a55816db952dfc965b0dd93d2
docker.easydb.de/pf/fylr:5.114.0           sha256:7497b710c403f8a2caf578becff863aa5c92eab8bad67ec394b9de0d4f23feb9
docker.easydb.de/pf/postgresql-11:5.114.0  sha256:ae079511532c3957af64c424da309655c978820a870a75cc46130b376a93f2c8
docker.easydb.de/pf/postgresql-14:5.114.0  sha256:35ac0f1df3612e3d883c56c04f74581fd74fbac6204e8c1ee7396e283142e4dc
docker.easydb.de/pf/server-base:5.114.0    sha256:03abffa0c49775a83ab3e29e40f3fd69af7651c68facb2035a34745b74f6659e
docker.easydb.de/pf/webfrontend:5.114.0    sha256:156f1caaf68220fa7f4c9989903ab0473f66361281cb8419dc74b8287cbd7cb4
```

