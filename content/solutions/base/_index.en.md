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

In the central configuration file `easydb5-master.yml`, whose folder has been set during the [installation](../../sysadmin/installation)

| Variable | Type | Description |
|----------|------|-------------|
| `external-user-schema` | Bool | true: Schema (a.k.a. data model) is mapped from the docker host into the docker container "easydb-server" via the docker-feature "volume". Example path see [Creation of containers](../../sysadmin/installationi/#start). Easydb allows changing the data model |
|  |  | false: The schema (a.k.a. data model) is inside the "easydb-server" docker container only and is not to be changed. It is crafted by Programmfabrik and delivered via easydb updates. |

~~~~~
easydb-server:
  [...]
  extension:
    external-user-schema: true
    
~~~~~

The last line is necessary; The others were given to demonstrate the correct indentation.

Also, the example shows the correct parent entry `extension`. If it is missing in your file, it must also be added now.
