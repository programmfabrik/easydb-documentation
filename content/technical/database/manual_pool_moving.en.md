---
title: "Pool moving"
menu:
  main:
    name: "Pool moving"
    identifier: "technical/database/pool_moving"
    parent: "technical"
---
# Moving a pool using the internal database

For performance reasons it is currently not possible to move pools using the frontend. If you are aware of the implications (a time-consuming complete re-index) you may move the pool using the database as shown below.

> Before doing any manipulation in the database, ensure you have a current backup. See [Backup & Restore](../../../sysadmin/backupandrestore/) for more information.

To get the name of the PostgreSQL database, query the used database like this (assuming your easydb URL is easydb.example.com):

```
curl -s https://easydb.example.com/api/v1/settings|grep db-name
```

The result is usually easydb5 or easydb or a custom name fitting your project. We use `easydb5` in this example.

Connect to the database like this: (replace docker with podman in case you use podman e.g. on RHEL8)

```
docker exec -t -i easydb-pgsql psql -U postgres easydb5
```

To get the ID of the pool to move and the ID of the target parent, the following SQL statement gives an overview of IDs. The string `de-DE` chooses the localized name and should be adapted if the database uses another primary language:

```sql
WITH RECURSIVE _pools AS (
    SELECT "ez_pool:id", "ez_pool_id:parent", "name:de-DE",
        '' AS prefix, "ez_pool:id"::text || '/' AS path
    FROM ez_pool
    WHERE "ez_pool_id:parent" IS NULL

    UNION ALL
    SELECT ep."ez_pool:id", ep."ez_pool_id:parent", ep."name:de-DE",
        p.prefix || '  ', p.path || ep."ez_pool:id"::text || '/'
    FROM ez_pool ep
    JOIN _pools p ON (p."ez_pool:id" = ep."ez_pool_id:parent")
)
SELECT "ez_pool:id", "ez_pool_id:parent", prefix || "name:de-DE" AS name
FROM _pools
ORDER BY path;
```

The output is something like this:
```
 ez_pool:id | ez_pool_id:parent |         name          
------------+-------------------+-----------------------
          1 |            <NULL> | Alle Pools
          2 |                 1 |   Standard-Pool
          3 |                 1 |   Abteilung A
          7 |                 3 |     Arbeitsgruppe A.2
          4 |                 1 |   Abteilung B
          5 |                 4 |     Arbeitsgruppe B.1
          9 |                 5 |       Schöne Bilder
          6 |                 4 |     Arbeitsgruppe A.1
          8 |                 4 |     Arbeitsgruppe B.2
```

In this example the pool "Arbeitsgruppe A.1" has the wrong parent, it should be moved below "Abteilung A". So the ID of the pool to move is **6** and the ID of the new parent is **3**.

Please only do the following changes when there is no other work on the database. Ensure all other jobs have been processed:
```sql
SELECT count(*) FROM ez_object_job;
```
If the number is above 0, there are still pending jobs.

The actual update includes these IDs and has to increase the version of the moved pool:
```sql
UPDATE ez_pool
SET "ez_pool_id:parent" = 3, ":version" = ":version" + 1
WHERE "ez_pool:id" = 6;
```

Now check the result using the statement above:
```
 ez_pool:id | ez_pool_id:parent |         name          
------------+-------------------+-----------------------
          1 |            <NULL> | Alle Pools
          2 |                 1 |   Standard-Pool
          3 |                 1 |   Abteilung A
          6 |                 3 |     Arbeitsgruppe A.1
          7 |                 3 |     Arbeitsgruppe A.2
          4 |                 1 |   Abteilung B
          5 |                 4 |     Arbeitsgruppe B.1
          9 |                 5 |       Schöne Bilder
          8 |                 4 |     Arbeitsgruppe B.2
```

Because of the user-customizable data model it is quite hard to determine which objects have to be reindexed after such a change. So everything is reindexed below. This may be optimized, but that's not supported and you do it on your own risk.

Remove object cache in database. For large installations this may take a while:
```sql
DELETE FROM ez_object_cache;
```

Reindex everything:
```sql
SELECT easydb_reindex();
```

