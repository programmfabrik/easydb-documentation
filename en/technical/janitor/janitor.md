# Janitor

The Janitor is a process running inside the easydb-server. Its purpose is to clean up temporary data in filesystem or database.

For a list of configuration options see the [YAML configuration reference](/sysadmin/konfiguration/yaml/yaml.html).

The following tasks are performed by the Janitor process:

* All files prepared by exports older than a configurable period are removed. The default retention period is 3 days. Exports which are affected by this cleanup have to be restarted before any files can be downloaded again.
* All events of the types `OBJECT_INDEX` and `API_PROGRESS` older than 1 week are removed from the database.
* The clients blocked because of too many wrong login attempts are checked and released if the blocking period is over.

By default the Janitor runs every 10 minutes. This interval should only be changed if there are load problems related to the Janitor process. The client block check runs at a separate, smaller interval which can't be configured.
