~~~
 The paths are for paths in the container, not for paths directly on your server that is running the docker container.
~~~


#  Troubleshooting

##  Troubleshoot EAS startup

In exceptional cases, the EAS does not start correctly. First, try to restart the EAS using the init script:

~~~
/etc/init.d/easydb-asset-server restart
~~~

If an error occurs, first consult the log files of the EAS. Any errors can be found in `eas-worker.log` (in a few cases also in `eas-exception.log`) in the EAS-log directory (usually `/var/opt/easydb/log/eas` "EAS_LOG_DIR":../conf/#eas_log_dir).

### Occupied OpenOffice ports (from EAS 4.2.38)

From version 4.2.38 onwards, the EAS checks whether all network ports available for the use of OpenOffice are available (see also "EAS_SOFFICE_BASEPORT":../conf/#eas_soffice_baseport). Under certain circumstances, it may happen that, when the EAS is terminated, OpenOffice parts will continue to block the ports. This circumstance is now recognized at the start of the EAS and can be recognized in the log by an error message of the following type:

~~~
eas_general (32598): 2013-11-18 11: 12: 45,777: ERROR: designated port already in use:
  TCPv4 127.0.0.1:2002 - 0.0.0.0:0 (LISTEN)
~~~

Prior to version 4.2.38, this error was not detected automatically and led to creeping problems, e.g. OpenOffice processes that run under full load.

To solve the problem, please finish the OpenOffice process. You can use this process for example. With the following call to ` ps `:

~~~
ps -edalf | grep 'soffice.bin. * Port = 2002'
~~~

After the process is finished, the EAS should restart.

##  Add new color profiles

Color profiles are separated in `/opt/easydb/eas/eas/data/profiles` by color space in the directories `rgb` and `cmyk`. New color profiles can be copied to the directories, which are then available.

##  Restart all failed jobs

On the PostgreSQL database of the EAS, the following can be executed:

~~~
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
~~~

