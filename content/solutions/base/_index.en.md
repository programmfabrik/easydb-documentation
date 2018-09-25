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
| `external-user-schema` | Bool | true: Schema is expected in the var directory (mapped into the container, see Install Docu), and configuration allows changing the data model |
|  |  | false: Schema is in docker image and can not be changed |

~~~~~
easydb-server:
  [...]
  extension:
    external-user-schema: true
    
~~~~~

The last line is necessary; The others were given to demonstrate the correct indentation.

Also, the example shows the correct parent entry `extension`. If it is missing in your file, it must also be added now.
