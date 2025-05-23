---
menu:
  main:
    name: "5.138 (November 2024)"
    identifier: "5.138"
    parent: "releases5130"
    weight: -638
---

> This version **does not require** a new index build

# Version 5.138.2

*Released on 2024-11-27*

# Webfrontend

## Fixed

* **Editor**: fixed JS error when trying to create objects with reverse-nested fields

# Version 5.138.1

*Released on 2024-11-18*

# Webfrontend

## Fixed

* **Editor**: handled saving of multiple reverse-nested objects
* **ACL editors**: increased number of groups or users in selectio
* **Templates**: fixed saving in user preferences

# Server

## Fixed

* **PDF printing**: provide environment variables for proxy configuration to Chromium process

# Version 5.138.0

*Released on 2024-11-06*

# Webfrontend

## Fixed

- **Pool Manager**: Resolved memory leak issues within the Pool Manager by cleaning up EventPoller references, preventing unexpected behaviors during pool changes.
- **Custom mask splitter detail linked**: The rendering of object references has been improved and fixed. An issue has been resolved where not all linked elements were being rendered.
- **Editor Modal New**: Fixed mask verification in the user's preferences, ensuring correct selection of the saved mask and default fallback options.
- **Date Range Expert Search**: A bug has been fixed that caused an error on the frontend when using a date range with textual representation in the expert search.

# Checksums

Here are the checksums of our Docker images (latest version):

```ini
docker.easydb.de/pf/eas:5.138.0            sha256:04e036fce52a69fb25b47736e100126dc9401ac1f049a61feb422a0df4e61b79
docker.easydb.de/pf/elasticsearch:5.138.0  sha256:93298312e5a634377feb2db6a4ae77e13c392bed9a3533532b7012c7f32711c4
docker.easydb.de/pf/fylr:5.138.1           sha256:c12fd029749c4a48e8ff056a02730ed229217c3ecf6e16c55f0622257c3ea856
docker.easydb.de/pf/postgresql-14:5.138.0  sha256:b85f6f77513e4324e4e70fb76c6d03d18612ec90d8715a6f6642ac3fa3930bfc
docker.easydb.de/pf/server-base:5.138.2    sha256:043258e27121ba57f3888375a6f49f9a0b48174597b04284ce1e8c331f52d03a
docker.easydb.de/pf/webfrontend:5.138.2    sha256:f6e3014f2e647489d7528c39be60e00fa2da70e7d8bccedff3ea8f8fb4a8ea68
```
