**DISCLAIMER**: the method of dumping and restoring an easydb-5 database is not recommended as it might result in an inconsistent database.

Sometimes (during development) it might be required to dump a database and restore it using a slightly different database schema (new columns/triggers etc. due to continued development). This procedure *might* work:

Dump the old database using the usual `pg_dump` command:

```sh
PGCLUSTER=9.1/main pg_dump -Fc -v -U postgres \
    easy5-charlotte-uni-wien \
    > easy5-charlotte-uni-wien-20140616.pgdump
```

Create an empty target database using `easydb-server`. `DROP/CREATE DATABASE` in advance to get a clean database.

Remove the prefilled data from the newly-generated database. This is required to restore e.g. pools and other base objects. `ez_config` is preserved as it contains the current database versions.

```sql
DO $DO$
  DECLARE tn text;
  BEGIN
    FOR tn IN (
      SELECT tablename
      FROM pg_tables
      WHERE schemaname = 'public' AND tablename != 'ez_config'
    )
    LOOP
      EXECUTE $$ TRUNCATE $$ || quote_ident(tn) || $$ CASCADE $$;
    END LOOP;
  END
$DO$;
```

Restore the database using `pg_restore`, but ignore DDL differences and triggers:

```sh
PGCLUSTER=9.1/main pg_restore -j4 -v -U postgres \
    --data-only --clean --disable-triggers \
    -d easy5-mad-martin-uni-wien \
    easy5-charlotte-uni-wien-20140616.pgdump
```

The Elasticsearch index will most likely be rebuild (read as "truncated") during the creation of the empty database if you don't disable the indexer. It is recommended to rebuild the complete index anyway, e.g. using:

```sh
ps -u $USER | grep es-indexer | awk '{print $1}' | xargs -i kill -HUP {}
```
