---
title: "7 - Base"
menu:
  mainWEG:
    name: "Base"
    identifier: "solutions/base"
    parent: "solutions"
---
# Solution base

For this solution, "base", the following customization must be made so that the service can start the easydb-server.

In the central configuration file `easydb-server.yml`, whose folder has been set during the [installation](/en/sysadmin/installation)

| Variable | Type | Description |
|----------|------|-------------|
| `external-user-schema` | Bool | true: Schema (a.k.a. data model) is mapped from the docker host into the docker container "easydb-server" via the docker-feature "volume". Example path see [Creation of containers](../../sysadmin/installation/#start). Easydb allows changing the data model. |
|  |  | false: (default) The schema (a.k.a. data model) is inside the "easydb-server" docker container only and is not to be changed. The schema is crafted by Programmfabrik and delivered via easydb updates. |

~~~~~
extension:
  external-user-schema: true
~~~~~

The example shows the correct indentation hierarchy. But only add lines to your file which are not yet there. For example, do not add a second line with `extension:`.
