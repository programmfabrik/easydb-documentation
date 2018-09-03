---
title: "33 - easydb Asset Server"
menu:
  main:
    name: "easydb Asset Server"
    identifier: "sysadmin/eas"
    parent: "sysadmin"
    weight: 40
---
easydb Asset Server
===================

The easydb asset server (also referred to as EAS in the following) is exclusively for
The calculation and management of all assets (images, videos,
Office documents, etc.), which you manage with the easydb.

[Main ingredients](installation)

[Configuration File](conf)

[Configuration at program start](initconf)

[Partitions](partitions)

[API](api)

[File Types](filetypes)

This service is also used by the easydb4, which makes the migration to the
Easydb5 is significantly simplified at this point.

> The further documentation of the EAS in the sub-capitals covers many internals that are only accessible within the EAS Docker container.
>
> There are path paths therefore refer to paths in the container, not to paths directly on your server, which runs the docker container.
