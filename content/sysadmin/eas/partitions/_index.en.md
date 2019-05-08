---
title: "38 - Partitionen"
menu:
  main:
    name: "Partitionen"
    identifier: "sysadmin/eas/partitions"
    parent: "sysadmin/eas"
---
> The paths refer to paths in the container, not to paths directly on your server that is running the docker container.

EAS partitions
===============

The EAS supports several so-called partitions. These are described in the
Database and specified by the following properties:

- unique path
- Setting whether originals, derived originals or versions get saved
- also: other filters, priority

Selection of the target partition
=========================

Decisive for selecting the target partition for a file
above-mentioned Filter. If more than one partition remains after filtering,
One is randomly selected.

If too little space is available on the underlying file system
The partition is automatically deactivated. The border is defined by
[EAS\_PARTITION\_MIN\_FREE](../conf). Should all
Valid partitions must be disabled (`disabled = true` in the
Database, see below), these have to be created after space
Manually.

File System Layout
==================

Standard partitions are located in `/var/opt/easydb/lib/eas/assets`. Become
New partitions are created in the database
Workers created automatically, provided the permissions in the
Hierarchy are sufficient.

For delivering via Apache, the partitions are also created with
Their ID in `/var/opt/easydb/lib/eas/partitions`, in one
Standard installation looks like this:

```bash
/var/opt/easydb/lib/eas/partitions/1 -> /var/opt/easydb/lib/eas/assets/orig
/var/opt/easydb/lib/eas/partitions/2 -> /var/opt/easydb/lib/eas/assets/dest
```

The symbolic links are also managed by the EAS-Worker
Required.

Create new partitions
=========================

At the moment, there is no tool for creating new partitions
But can add more partitions to the table at database level
`Eas.partition`.

This table has the following columns:




  ---------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `partition`            ID (managed by PostgreSQL)
  `partition_name`       unique name of the partition
  `path`                 unique path to data storage
  `priority`             Priority of the partition (default` 0`, the higher, the less important)
  `store_original`       for 'originals' (uploaded files)
  `store_derived`        for 'derived originals' (e.g., rotated images)
  `store_version`        for 'versions' (e.g., various sizes)
  `all_versions`         all versions (differentiation by version names) may be stored (default:` true`). If `false`, the link table` eas.partition__version` is used.
  `all_classes`          all types (` image`, `office`, etc.) may be stored (default` true`). If `false`, the link table` eas.partition__fileclass` is used.
  `all_instances`        Assets of all instances may be placed (default:` true`). If `false`, the link table` eas.partition__instance` is used.
  `disabled`             default` false`. If `true`, the partition is not used. This flag is also set automatically if the free space on the partition becomes too small.
  `space_used`           Space consumed in bytes (is automatically filled)
  `space_free`           free space in bytes (is automatically filled)
  `auto_disabled_time`   Time of automatic deactivation (is automatically filled, as from EAS 4.2.18)
  ---------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Reactivate automatically disabled partitions
======================================================

Without sufficinet free storage space, EAS "partitions" get disabled as a saftey measure.

Once space has been created on the underlying file system, the disabled partitions have to be enabled manually.
To do this, connect with the PostgreSQL command-line client `psql` to the **eas** database.

From outside the container, the call would be:

```bash
docker exec -ti easydb-pgsql psql -U postgres eas
```

Then execute the following SQL statement, assuming that all partitions are affected:

```sql
UPDATE eas.partition SET disabled = false;
```

If you are using the default installation, the two
originally created partitions are on the same file system,
and are thus deactivated at the same time.

But if your layout is different and only one partition is affected (example: a partition named "dest"):

```sql
UPDATE eas.partition SET disabled = false WHERE partition_name = 'dest';
```

To check which partitions are affected:

```sql
SELECT partition_name,path,disabled FROM eas.partition;
```

At the end just close the connection with:
```sql
\q
```

A reload or restart is not needed.

