---
title: "34 - Troubleshooting"
menu:
  main:
    name: "Troubleshooting"
    identifier: "sysadmin/eas/faq"
    parent: "sysadmin/eas"
---

#  Troubleshooting

## Corrupted Asset Read Access

When reading files over a certian size (e.g. 2 MB) from a CIFS file system, using Apache inside docker, then the read access does not give expected results but instead different data each read, and each time corrupted data (e.g. invalid JPG). To prevent this, the MMap optimization feature in Apache needs to be turned off. (Default: on).

Inside the docker container easydb-eas the following setting is required: (in `/etc/apache2/sites-enabled/easydb-asset-server.conf`)

```
EnableMMap off
```

Beware: Making changes inside of the container will be overwritten by updates and other cotnainer recreations.

Instead we advise to use the following method instead:

To make this configuration persistent, set outside of the docker container: (in e.g. `/srv/easydb/config/eas.yml` in case your base directory is /srv/easydb)

```
apache-mmap: "off"
```

((List of valid configuration options)[/en/sysadmin/konfiguration/eas])

And restart the container with:

```
docker restart easydb-eas
```

## Troubleshoot EAS startup

In exceptional cases, the EAS does not start correctly. First, try to restart the EAS using the init script:

```bash
docker restart easydb-eas
```

To view the log messages during startup, this can be extended to:

```
docker restart easydb-eas; docker logs --tail 1 -f easydb-eas
```

For later review of the log messages you can also look into the log file `eas-worker.log`. In a few cases also `eas-exception.log`.
Those are placed into `/srv/easydb/eas/log/` outside of the container, assuming your base directory is `/srv/easydb`.
Inside of the container it is usually `/var/opt/easydb/log/eas` (setting (EAS_LOG_DIR)[../conf/#eas_log_dir]).

### Occupied OpenOffice ports (from EAS 4.2.38)

From version 4.2.38 onwards, the EAS checks whether all network ports available for the use of OpenOffice are available (see also (EAS_SOFFICE_BASEPORT)[../conf/#eas_soffice_baseport]). Under certain circumstances, it may happen that, when the EAS is terminated, OpenOffice parts will continue to block the ports. This circumstance is now recognized at the start of the EAS and can be recognized in the log by an error message of the following type:

```bash
eas_general (32598): 2013-11-18 11: 12: 45,777: ERROR: designated port already in use:
  TCPv4 127.0.0.1:2002 - 0.0.0.0:0 (LISTEN)
```

Prior to version 4.2.38, this error was not detected automatically and led to creeping problems, e.g. OpenOffice processes that run under full load.

To solve the problem, please finish the OpenOffice process. You can use this process for example. With the following call to ` ps `:

```bash
ps -edalf | grep 'soffice.bin. * Port = 2002'
```

After the process is finished, the EAS should restart.

##  Add new color profiles

Color profiles are separated in `/opt/easydb/eas/eas/data/profiles` by color space in the directories `rgb` and `cmyk`. New color profiles can be copied to the directories, which are then available.

The directory `/opt/easydb/eas/eas/data/profiles` is inside of the container `easydb-eas`. To add color profiles persistently, you need to map that directory as a docker volume to a directory outside of the container.

##  Restart all failed jobs

1. Connect to the PostgreSQL database of the EAS.

```
docker exec -ti easydb-pgsql psql -U postgres eas
```

2. On the PostgreSQL database of the EAS, the following can be executed:

```sql
BEGIN;

UPDATE eas.job SET job_status = 'pending' WHERE job_id IN (
  SELECT DISTINCT ON(derived_asset_id) job_id
  FROM eas.job
  JOIN eas.derived_asset USING(derived_asset_id)
  WHERE derived_asset.derived_asset_status = 'failed'
  ORDER BY derived_asset_id, job_time_created DESC
);

UPDATE eas.derived_asset
SET derived_asset_status = 'pending'
WHERE derived_asset_status = 'failed'
  AND derived_asset_id IN (
    SELECT derived_asset_id
    FROM eas.job
    WHERE job_status IN ('failed', 'pending')
  );

COMMIT;
```
