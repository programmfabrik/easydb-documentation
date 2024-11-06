---
menu:
  main:
    name: "5.138 (November 2024)"
    identifier: "5.138"
    parent: "releases"
    weight: -638
---

> This version **does not require** a new index build

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
docker.easydb.de/pf/fylr:5.138.0           sha256:3b09aa74cd04dda799a3d21e35b6380c295d9be83546cc342f250d61a765cd22
docker.easydb.de/pf/postgresql-14:5.138.0  sha256:b85f6f77513e4324e4e70fb76c6d03d18612ec90d8715a6f6642ac3fa3930bfc
docker.easydb.de/pf/server-base:5.138.0    sha256:69c85e52f15ff5df94f6839bf686b94634fddb6573df19d7c6f28ee7375612d4
docker.easydb.de/pf/webfrontend:5.138.0    sha256:e4acba23fa8e0a07d16bfe5bec036e41d9147817f4853e26ff539961382b0f49
```
